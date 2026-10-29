#!/usr/bin/env python3
"""Build readable review pages from the procedural model; --check detects drift.

Interpretation notes are authored in docs/procedures/editorial-notes.md.
Generated pages expose the encoded predicates, not independent legal approval.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from pathlib import Path
import re
import sys

# Support both direct invocation and import from the repository root.
if __package__:
    from . import procedure_model as pm
else:
    import procedure_model as pm

REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "docs" / "procedures"
STATUS = {"statutory": "Statutory assertion", "guidance": "Advisory guidance",
          "service_target": "Service target", "policy_expectation": "Policy expectation"}
RESULT = {"satisfied": "Satisfied on supplied evidence", "not_satisfied": "Selected statutory assertion fails",
          "advisory_gap": "Advisory gap", "target_missed": "Target missed",
          "unknown": "Unknown", "not_applicable": "Not applicable"}
LABELS = {
    "submission_date": "Examination submission date",
    "consultation_published": "Selected consultation: publication date",
    "consultation_deadline": "Selected consultation: representations deadline",
    "gateway2_requested": "Gateway 2 request date",
    "gateway2_material_sent": "Gateway 2 material transmission date",
    "content_summary_published": "Content/evidence summary publication date",
    "new_gateway2_plan_provided": "Emerging draft plan or relevant policy detail supplied at gateway 2",
    "new_gateway2_policies_map_provided": "Emerging policies map supplied at gateway 2",
    "gateway2_necessary_material_sent": "Material the authority considers necessary for gateway 2 has been supplied",
    "new_gateway3_soundness_provided": "Statement of soundness supplied in the gateway 3 pack",
    "assessor_all_prescribed_requirements_met": "Assessor advises that all prescribed gateway 3 requirements are met",
    "examination_completed": "Independent examination completed",
    "plan_submitted": "Plan submitted for examination",
    "plan_sound": "Examiner considers it reasonable to conclude that the plan is sound",
    "plan_sound_and_legal": "Legacy examiner considers the plan sound and compliant with the saved legal requirements",
    "legacy_direction_verified": "Plan-specific later-deadline direction verified",
    "directed_legacy_deadline": "Deadline stated in the plan-specific direction",
    "pause_within_six_calendar_months": "Reviewer confirms the pause period is within six calendar months",
    "pause_notified": "Pause notification date",
    "pause_begins": "Pause commencement date",
    "pause_ends": "Pause expiry date",
    "examination_target_met": "Reviewer confirms the six-month examination expectation was met",
    "pause_response_contents_recorded": "Pause response has the required contents",
    "pause_response_published": "Pause response publication and notifications completed as required",
    "pause_response_sent": "Pause response transmission date",
    "pause_response_before_expiry": "Reviewer confirms delivery before the actual pause expiry",
    "curable_by_modifications": "Examiner considers the defects curable through modifications",
    "lpa_requested_modifications": "Authority requested main-modification recommendations",
    "curative_modifications_recommended": "Legacy curative main modifications recommended",
    "non_adoption_recommended_with_reasons": "Legacy non-adoption recommendation and reasons issued",
    "legacy_adoption_conditions_met": "Reviewer confirms adoption complies with saved section 23",
}


def slug(value):
    return value.replace(".", "-").replace("_", "-")


def case_title(ident):
    return re.sub(r"gateway([123])", r"gateway \1", ident.replace("-", " ")).capitalize()


def cell(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


def notes():
    text = (OUT / "editorial-notes.md").read_text(encoding="utf-8")
    chunks = re.split(r"^## (stage|rule|case):([^\n]+)\n", text, flags=re.M)
    result = {}
    for i in range(1, len(chunks), 3):
        key = (chunks[i], chunks[i + 1].strip())
        if key in result:
            raise ValueError(f"Duplicate editorial note: {key}")
        result[key] = chunks[i + 2].strip()
    return result


def source_link(citation, sources):
    source = sources[citation["source"]]
    url = source["url"]
    # Direct provision links preserve source versions; the locator remains visible.
    reg = re.search(r"\breg (\d+)", citation["locator"])
    if reg and citation["source"] == "regs-2026":
        url = f"https://www.legislation.gov.uk/uksi/2026/186/regulation/{reg[1]}/made"
    elif reg and citation["source"] == "regs-2012-saved":
        url = f"https://www.legislation.gov.uk/uksi/2012/767/regulation/{reg[1]}"
    return f"[{citation['locator']}]({url}) — {source['title']}; {source['version']}"


def line_map(path):
    result = {}
    for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        match = re.match(r'\s*"id": "([^"]+)"', line)
        if match:
            result[match[1]] = i
    return result


def fact_name(fid, facts):
    # Complete definitions remain visible in the fact register and rule inputs.
    return LABELS.get(fid, facts[fid]["description"].split(". ")[0].rstrip("."))


def expression(expr, facts, depth=0):
    indent = "  " * depth
    op = expr["op"]
    if op == "constant":
        return [indent + "- No additional fact condition." if expr["value"] else indent + "- Always false."]
    if op == "eq":
        expected = {True: "Yes", False: "No"}.get(expr["value"], str(expr["value"]))
        return [indent + f"- **{expected}** to: {fact_name(expr['fact'], facts)} "
                f"([input `{expr['fact']}`](../facts.md#{slug(expr['fact'])}))."]
    if op == "date_gap_at_least":
        start = f"[{fact_name(expr['start'], facts)}](../facts.md#{slug(expr['start'])})"
        end = f"[{fact_name(expr['end'], facts)}](../facts.md#{slug(expr['end'])})"
        if expr["days"] == 0:
            text = f"{end} is on or after {start}."
        elif expr["days"] == 1:
            text = f"{end} is at least the next calendar day after {start}."
        else:
            text = f"{end} is at least **{expr['days']} calendar days** after {start}."
        return [indent + "- " + text]
    if op in {"all", "any"}:
        lines = [indent + ("- **Every** condition below:" if op == "all" else "- **At least one** condition below:")]
        consumed = set()
        for i, child in enumerate(expr["args"]):
            if i in consumed:
                continue
            # Two opposite non-strict date comparisons mean equality. Show that
            # directly, preserving the authored predicate in the canonical JSON.
            if op == "all" and child["op"] == "date_gap_at_least" and child["days"] == 0:
                reverse = next((j for j, other in enumerate(expr["args"]) if j > i
                                and other["op"] == "date_gap_at_least" and other["days"] == 0
                                and other["start"] == child["end"] and other["end"] == child["start"]), None)
                if reverse is not None:
                    consumed.add(reverse)
                    a, b = child["start"], child["end"]
                    lines.append("  " * (depth + 1) + f"- [{fact_name(a, facts)}](../facts.md#{slug(a)}) and "
                                 f"[{fact_name(b, facts)}](../facts.md#{slug(b)}) are **the same calendar date**.")
                    continue
            lines.extend(expression(child, facts, depth + 1))
        return lines
    raise ValueError(f"Unknown expression {op}")


def date_operators(expr):
    return int(expr["op"] == "date_gap_at_least") + sum(date_operators(c) for c in expr.get("args", []))


def build():
    model, catalogue = pm.load_package()
    pm.validate_model(model, catalogue)
    examples = pm.read_json(pm.ROOT / "examples.json")["cases"]
    sources = pm.index(catalogue["sources"], "source")
    stages = pm.index(model["stages"], "stage")
    rules = pm.index(model["rules"], "rule")
    facts = pm.index(model["facts"], "fact")
    actors = pm.index(model["actors"], "actor")
    documents = pm.index(model["documents"], "document")
    cases = pm.index(examples, "case")
    editorial = notes()
    for kind, ids in (("stage", stages), ("rule", rules), ("case", cases)):
        for k, ident in editorial:
            if k == kind and ident not in ids:
                raise ValueError(f"Editorial note has unknown {kind}: {ident}")
    if set(stages) != {ident for kind, ident in editorial if kind == "stage"}:
        raise ValueError("Every stage needs an authored explanation")
    model_lines = line_map(pm.ROOT / "model.json")
    example_lines = line_map(pm.ROOT / "examples.json")
    examples_for = defaultdict(list)
    used_by = defaultdict(list)
    for case in examples:
        for rid in case["rule_ids"]:
            examples_for[rid].append(case)
    for rule in rules.values():
        for fid in pm.expression_facts(rule["applicability"]) | pm.expression_facts(rule["check"]):
            used_by[fid].append(rule)
    banner = (f"Generated from model {model['model_version']}, knowledge date {model['knowledge_date']}. "
              "Rebuild with `python tools/build_procedure_docs.py`. Authored explanations live in "
              "[editorial notes](editorial-notes.md). Legal mappings await maintainer review.\n")
    pages = {}
    for stage in stages.values():
        stage_rules = [r for r in rules.values() if r["stage"] == stage["id"]]
        lines = [f"# {stage['label']}", "", "[Review guide](../README.md) · [Input definitions](../facts.md) · [Worked examples](../worked-examples.md)", "",
                 banner.replace("(editorial-notes.md)", "(../editorial-notes.md)"),
                 editorial[("stage", stage["id"])], "",
                 "**Who is involved:** " + "; ".join(actors[a]["label"] for a in stage["actors"])]
        for key, label in (("inputs", "Stage inputs"), ("outputs", "Stage outputs")):
            lines += ["", f"**{label}:** " + ("; ".join(documents[d]["label"] for d in stage[key]) or "No document types listed.")]
        lines += ["", "Stage inputs/outputs are an indicative map; the individual rules below determine which selected document duties are conditional.", "", "## Assertions at this stage", "", "| Assertion | Status | Evaluator operation |", "| --- | --- | --- |"]
        for r in stage_rules:
            operation = "Date arithmetic + supplied observations" if date_operators(r["check"]) or date_operators(r["applicability"]) else "Supplied observations only"
            lines.append(f"| [{cell(r['statement'])}](#{slug(r['id'])}) | {STATUS[r['status']]} | {operation} |")
        if not stage_rules:
            lines += ["", "No individually assigned assertions in this stage."]
        for r in stage_rules:
            r_used = sorted(pm.expression_facts(r["applicability"]) | pm.expression_facts(r["check"]))
            lines += ["", f'<a id="{slug(r["id"])}"></a>', "", f"## {r['statement']}", "",
                      f"**{STATUS[r['status']]} · responsible actor: {actors[r['actor']]['label']}**", "",
                      f"Rule [`{r['id']}`](../../../knowledge/procedures/model.json#L{model_lines[r['id']]}); version {r['version']}.", "",
                      "### Source to inspect", ""]
            lines += ["- " + source_link(c, sources) + f" ({c['role'].replace('_', ' ')})" for c in r["sources"]]
            lines += ["", "### When the assertion applies", "", "The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.", ""]
            lines += expression(r["applicability"], facts)
            lines += ["", "### What the evaluator actually requires", ""] + expression(r["check"], facts)
            timing = r["timing"]
            if timing:
                lines += ["", f"**Timing:** {timing['anchor']} → {timing['endpoint']}; {timing['calculation']}."]
            if r_used:
                lines += ["", "<details>", "<summary>Evidence inputs and their complete meanings</summary>", "", "| Input | What must be established | Input kind |", "| --- | --- | --- |"]
                for fid in r_used:
                    f = facts[fid]
                    kind = "Reviewer judgement" if f["assessment"] == "professional_judgement" else "Recorded observation"
                    lines.append(f"| [`{fid}`](../facts.md#{slug(fid)}) | {cell(f['description'])} | {kind}; {f['type']} |")
                lines += ["", "</details>"]
            failure = {"statutory": "not_satisfied", "guidance": "advisory_gap", "service_target": "target_missed", "policy_expectation": "target_missed"}[r["status"]]
            lines += ["", f"**Results:** a true check yields `satisfied`; a false check yields `{failure}`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide."]
            if r["exceptions"] or r["notes"] or ("rule", r["id"]) in editorial:
                lines += ["", "### Interpretation and review boundary", ""]
                if ("rule", r["id"]) in editorial:
                    lines += [editorial[("rule", r["id"])], ""]
                if r["notes"]:
                    lines += [r["notes"], ""]
                lines += ["- Recorded exception: " + e for e in r["exceptions"]]
            lines += ["", "**Examples selecting this assertion:**", ""]
            if examples_for[r["id"]]:
                for c in examples_for[r["id"]]:
                    target = f"../worked-examples.md#{slug(c['id'])}" if ("case", c["id"]) in editorial else f"../../../knowledge/procedures/examples.json#L{example_lines[c['id']]}"
                    lines.append(f"- [{c['description']}]({target})")
            else:
                lines += ["- No existing example selects this assertion. Its source mapping needs direct review."]
            end = r["temporal"]["effective_to"] or "no end encoded"
            lines += ["", f"**Recorded version interval:** {r['temporal']['effective_from']} to {end}, selected by assessment date. **Verification:** {r['verification']['level']}, {r['verification']['checked_on']}; {r['verification']['review']}. This metadata records the earlier check, not a fresh independent approval."]
        lines += ["", "## Connections to other stages", ""]
        for t in model["transitions"]:
            if stage["id"] in {t["from_stage"], t["to_stage"]}:
                a, b = stages[t["from_stage"]], stages[t["to_stage"]]
                lines.append(f"- [{a['label']}]({slug(a['id'])}.md) → [{b['label']}]({slug(b['id'])}.md): {t['condition']} ({t['kind']}).")
        lines += ["", "These relationships are descriptive. They are not executable workflow guards.", ""]
        pages[Path("stages") / (slug(stage["id"]) + ".md")] = "\n".join(lines)

    lines = ["# Evidence input register", "", "[Start with the review guide](README.md).", "", banner,
             "Each entry defines an input to the evaluator. Every value is supplied by a case author; the evaluator neither extracts these observations from documents nor independently makes the professional judgements. `null` or omission means unknown; `false` is an evidenced negative answer.", "",
             "Use a rule's source and complete assertion to assess a bundled observation. Document provision, document quality and substantive findings are separate questions."]
    for fid, f in facts.items():
        lines += ["", f'<a id="{slug(fid)}"></a>', "", f"## {fid.replace('_', ' ')}", "", f["description"], "",
                  f"**Type:** {f['type']}. **Assessment:** {'reviewer judgement' if f['assessment'] == 'professional_judgement' else 'recorded observation'}. "
                  f"[Canonical definition](../../knowledge/procedures/model.json#L{model_lines[fid]}).", "", "**Used by:**"]
        lines += [f"- [{r['statement']}](stages/{slug(r['stage'])}.md#{slug(r['id'])})" for r in used_by[fid]] or ["- Not used in an assertion predicate. It may be routing evidence or retained metadata; consult the routing explanation."]
    pages[Path("facts.md")] = "\n".join(lines) + "\n"

    lines = ["# Worked examples: observations, computation and interpretation", "", "[Start with the review guide](README.md).", "", banner,
             "These are selected **synthetic, isolated assertions**, not full-plan case histories. They use the current model and law recorded at the knowledge date. Future event dates are illustrative projections. The results below are generated by running the evaluator against the existing fixtures.", "",
             "| Example | Point being tested |", "| --- | --- |"]
    selected = [c for c in examples if ("case", c["id"]) in editorial]
    for i, c in enumerate(selected, 1):
        lines.append(f"| [{i}. {cell(case_title(c['id']))}](#{slug(c['id'])}) | {cell(c['description'])} |")
    for i, c in enumerate(selected, 1):
        report = pm.evaluate(c, model, catalogue)
        lines += ["", f'<a id="{slug(c["id"])}"></a>', "", f"## {i}. {case_title(c['id'])}", "", c["description"], "",
                  f"**Declared legal basis:** `{c['context']['legal_basis']}`. **Assessment date:** {c['context']['assessment_date']}. **Chosen route:** `{report['route']['regime']}`.", "", "### Supplied observations", "", "| Observation | Value |", "| --- | --- |"]
        for fid, observed in c["facts"].items():
            value = observed["value"]
            shown = "Yes" if value is True else "No" if value is False else "Unknown" if value is None else value
            lines.append(f"| [{cell(fact_name(fid, facts))}](facts.md#{slug(fid)}) | {shown} |")
        lines += ["", "### Actual evaluator results", "", "| Assertion | Result | Missing inputs |", "| --- | --- | --- |"]
        for rr in report["results"]:
            r = rules[rr["rule_id"]]
            lines.append(f"| [{cell(r['statement'])}](stages/{slug(r['stage'])}.md#{slug(r['id'])}) | {RESULT[rr['status']]} (`{rr['status']}`) | {', '.join(rr['missing_facts']) or 'None'} |")
        if not report["results"]:
            lines += ["", "This fixture tests routing only; it selects no individual assertions."]
        lines += ["", "### Why that follows", "", editorial[("case", c["id"])], "", "**Routing explanation:** " + report["route"]["reason"], "",
                  f"[Exact executable fixture](../../knowledge/procedures/examples.json#L{example_lines[c['id']]}). All evidence in this fixture is labelled synthetic."]
    pages[Path("worked-examples.md")] = "\n".join(lines) + "\n"

    lines = ["# Stage and rule index", "", "[Start with the review guide](README.md).", "", banner,
             "The pages group individual assertions into procedural stages. Each assertion has a source link, plain-language predicate, complete evidence definitions, examples where present, exceptions and the recorded review status."]
    for regime, title in (("legacy", "Saved legacy system"), ("new", "2026 system")):
        lines += ["", "## " + title, "", "| Stage | Assertions | Main output |", "| --- | --- | --- |"]
        for s in stages.values():
            if s["regime"] == regime:
                count = sum(r["stage"] == s["id"] for r in rules.values())
                lines.append(f"| [{s['label']}](stages/{slug(s['id'])}.md) | {count} | {cell('; '.join(documents[d]['label'] for d in s['outputs']))} |")
    lines += ["", "## Assertion coverage by examples", "", f"{sum(bool(examples_for[r]) for r in rules)} of {len(rules)} assertions are selected by at least one existing fixture. A source mapping without an example is visible as such on its stage page. A passing example verifies the encoded behaviour, not the correctness of the legal interpretation.", ""]
    pages[Path("stage-index.md")] = "\n".join(lines)
    return pages


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if readable pages differ from their inputs")
    args = parser.parse_args(argv)
    try:
        pages = build()
        stale = []
        for name, content in pages.items():
            path = OUT / name
            if args.check:
                if not path.exists() or path.read_text(encoding="utf-8") != content:
                    stale.append(str(path.relative_to(REPO)))
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8")
        if stale:
            raise ValueError("Readable documentation is stale: " + ", ".join(stale))
        print(f"{'Checked' if args.check else 'Built'} {len(pages)} readable review pages.")
        return 0
    except (ValueError, OSError, KeyError) as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
