#!/usr/bin/env python3
"""Validate and evaluate selected procedural assertions, never certify a plan.

The evaluator is a replaceable reference implementation. The JSON data and
schemas are the interchange format; no database or application stack is assumed.
"""
from __future__ import annotations

import argparse
from datetime import date
import json
from pathlib import Path
import sys

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[1] / "knowledge" / "procedures"


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"),
                      object_pairs_hook=_unique_object)


def schema_check(value, name, root=ROOT):
    schema = read_json(root / "schemas" / name)
    Draft202012Validator.check_schema(schema)
    registry = Registry().with_resource(
        "case.schema.json",
        Resource.from_contents(read_json(root / "schemas" / "case.schema.json")),
    )
    errors = list(Draft202012Validator(
        schema, registry=registry, format_checker=FormatChecker()
    ).iter_errors(value))
    if errors:
        lines = [f"{name}:{'/'.join(map(str, e.absolute_path))}: {e.message}"
                 for e in errors]
        raise ValueError("\n".join(lines))


def index(items, kind):
    result = {}
    for item in items:
        if item["id"] in result:
            raise ValueError(f"Duplicate {kind} id: {item['id']}")
        result[item["id"]] = item
    return result


def expression_facts(expr):
    if expr["op"] == "eq":
        return {expr["fact"]}
    if expr["op"] == "date_gap_at_least":
        return {expr["start"], expr["end"]}
    if expr["op"] in {"all", "any"}:
        return set().union(*(expression_facts(e) for e in expr["args"]))
    if expr["op"] == "constant":
        return set()
    raise ValueError(f"Unsupported expression: {expr['op']}")


def validate_model(model, sources, root=ROOT):
    schema_check(model, "model.schema.json", root)
    schema_check(sources, "sources.schema.json", root)
    tables = {k: index(model[k], k) for k in
              ("actors", "documents", "stages", "facts", "rules", "regimes", "transitions")}
    src = index(sources["sources"], "sources")

    def refs(values, table, context):
        for value in values:
            if value not in tables[table]:
                raise ValueError(f"{context}: unknown {table} reference {value}")

    def citations(items, context):
        for item in items:
            if item["source"] not in src:
                raise ValueError(f"{context}: unknown source {item['source']}")
            if item["role"] == "legal_basis" and src[item["source"]]["kind"] != "legislation":
                raise ValueError(f"{context}: guidance cannot supply a legal basis")

    def expressions(expr, context):
        refs(expression_facts(expr), "facts", context)
        if expr["op"] == "date_gap_at_least":
            for key in (expr["start"], expr["end"]):
                if tables["facts"][key]["type"] != "date":
                    raise ValueError(f"{context}: date operation on non-date {key}")
        if expr["op"] == "eq":
            kind = tables["facts"][expr["fact"]]["type"]
            expected = "boolean" if type(expr["value"]) is bool else "string"
            if kind != expected:
                raise ValueError(f"{context}: comparison value has wrong type")
        for child in expr.get("args", []):
            expressions(child, context)

    for stage in model["stages"]:
        refs(stage["actors"], "actors", stage["id"])
        refs(stage["inputs"] + stage["outputs"], "documents", stage["id"])
        refs([stage["regime"]], "regimes", stage["id"])
        citations(stage["sources"], stage["id"])
    for regime in model["regimes"]:
        citations(regime["sources"], regime["id"])
    for rule in model["rules"]:
        rid = rule["id"]
        refs([rule["actor"]], "actors", rid)
        refs([rule["stage"]], "stages", rid)
        refs(rule["documents"], "documents", rid)
        if tables["stages"][rule["stage"]]["regime"] != rule["regime"]:
            raise ValueError(f"{rid}: stage/regime mismatch")
        citations(rule["sources"], rid)
        if rule["status"] == "statutory":
            if not any(c["role"] == "legal_basis" for c in rule["sources"]):
                raise ValueError(f"{rid}: statutory rule has no legislative basis")
            if rule["verification"]["level"] != "primary_text_checked":
                raise ValueError(f"{rid}: statutory rule lacks primary-text verification")
        if rule["verification"]["checked_on"] > model["knowledge_date"]:
            raise ValueError(f"{rid}: verification is after knowledge date")
        end = rule["temporal"]["effective_to"]
        if end and end < rule["temporal"]["effective_from"]:
            raise ValueError(f"{rid}: inverted validity interval")
        expressions(rule["applicability"], rid)
        expressions(rule["check"], rid)
    for transition in model["transitions"]:
        ends = [transition["from_stage"], transition["to_stage"]]
        refs(ends, "stages", transition["id"])
        if len({tables["stages"][s]["regime"] for s in ends}) != 1:
            raise ValueError("Transition crosses regimes without an explicit migration model")
        citations(transition["sources"], transition["id"])
    return tables


def validate_case(case, model, root=ROOT):
    schema_check(case, "case.schema.json", root)
    facts = index(model["facts"], "facts")
    evidence = index(case["evidence"], "evidence")
    rules = index(model["rules"], "rules")
    for key, observed in case["facts"].items():
        if key not in facts:
            raise ValueError(f"Unknown fact: {key}")
        value = observed["value"]
        kind = facts[key]["type"]
        if value is not None:
            if kind == "boolean" and type(value) is not bool:
                raise ValueError(f"{key}: expected a JSON boolean")
            if kind in {"date", "string"} and not isinstance(value, str):
                raise ValueError(f"{key}: expected a string")
            if kind == "date":
                if not FormatChecker().conforms(value, "date"):
                    raise ValueError(f"{key}: invalid ISO calendar date")
        for eid in observed["evidence_refs"]:
            if eid not in evidence:
                raise ValueError(f"{key}: missing evidence {eid}")
    for eid in case["context"]["basis_evidence_refs"]:
        if eid not in evidence:
            raise ValueError(f"Missing legal-basis evidence: {eid}")
    if len(set(case["rule_ids"])) != len(case["rule_ids"]):
        raise ValueError("Duplicate requested rule IDs")
    for rid in case["rule_ids"]:
        if rid not in rules:
            raise ValueError(f"Unknown rule: {rid}")
    if set(case.get("expected", {})) - set(case["rule_ids"]):
        raise ValueError("Expected outcome names a rule not selected")


def value_of(facts, key):
    return facts.get(key, {}).get("value")


def evaluate_expression(expr, facts):
    """Strong Kleene three-valued logic: missing/null observations stay unknown."""
    op = expr["op"]
    if op == "constant":
        return expr["value"]
    if op == "eq":
        value = value_of(facts, expr["fact"])
        return None if value is None else value == expr["value"]
    if op == "date_gap_at_least":
        start, end = (value_of(facts, expr[x]) for x in ("start", "end"))
        if start is None or end is None:
            return None
        return (date.fromisoformat(end) - date.fromisoformat(start)).days >= expr["days"]
    if op in {"all", "any"}:
        values = [evaluate_expression(child, facts) for child in expr["args"]]
        if op == "all":
            return False if False in values else None if None in values else True
        return True if True in values else None if None in values else False
    raise ValueError(f"Unsupported expression: {op}")


def select_regime(case, model):
    """Require a documented plan basis; submission date never chooses new law."""
    c, facts = case["context"], case["facts"]
    sources = ["savings-2026", "regs-2026"]
    routing_facts = set()
    def observation(key):
        routing_facts.add(key)
        return value_of(facts, key)
    def result(regime, reason):
        evidence = set(c["basis_evidence_refs"])
        for key in routing_facts:
            evidence.update(facts.get(key, {}).get("evidence_refs", []))
        return {"regime": regime, "reason": reason, "sources": sources,
                "evidence_refs": sorted(evidence),
                "facts_considered": sorted(routing_facts)}
    if c["jurisdiction"] != "England" or c["plan_kind"] != "local_plan":
        return result("out_of_scope", "This package covers ordinary English Local Plans only.")
    if c["assessment_date"] < model["scope"]["supported_assessment_from"]:
        return result("out_of_scope", "Historical pre-commencement profiles are not encoded.")
    if c["procedure_route"] != "ordinary_lpa":
        return result("out_of_scope", "Special/intervention routes need their own procedural profile.")
    if c["legal_basis"] == "unknown":
        return result("unknown", "Plan legal basis must be established; the date alone is insufficient.")
    if c["legal_basis"] == "pcpa_15c":
        return result("new", "Documented s 15C plan basis; 2026 preparation framework.")
    if observation("legacy_savings_eligibility_confirmed") is True:
        return result("legacy", "Case-specific saving eligibility expressly evidenced by reviewer.")
    submitted = observation("submission_date")
    if submitted is None:
        return result("unknown", "Saved regime declared, but relevant saving eligibility is not evidenced.")
    regime = next(r for r in model["regimes"] if r["id"] == "legacy")
    cutoff = regime["ordinary_submission_cutoff"]
    if submitted <= cutoff:
        return result("legacy", "Submission by inclusive saved-regime deadline; examination/adoption can continue later.")
    directed = observation("directed_legacy_deadline")
    if observation("legacy_direction_verified") is True and directed and directed > cutoff and submitted <= directed:
        return result("legacy", "Plan-specific later deadline under Sch 1 para 4(5) evidenced.")
    return result("legacy_eligibility_unestablished", "Ordinary deadline exceeded; establish a statutory saving or direction. Do not switch the plan automatically.")


def evaluate(case, model, sources, root=ROOT):
    validate_model(model, sources, root)
    validate_case(case, model, root)
    route = select_regime(case, model)
    rule_index = index(model["rules"], "rules")
    src = index(sources["sources"], "sources")
    route["source_details"] = [{"source": sid, "url": src[sid]["url"],
                                "version": src[sid]["version"]}
                               for sid in route["sources"]]
    results = []
    for rid in case["rule_ids"]:
        rule = rule_index[rid]
        used = expression_facts(rule["applicability"]) | expression_facts(rule["check"])
        missing = sorted(k for k in used if value_of(case["facts"], k) is None)
        applicable = evaluate_expression(rule["applicability"], case["facts"])
        check = evaluate_expression(rule["check"], case["facts"])
        when = rule["temporal"]
        at = case["context"]["assessment_date"]
        if route["regime"] not in {"new", "legacy"}:
            state, reason = "unknown", "Regime/applicability cannot be established within supported scope."
        elif route["regime"] != rule["regime"]:
            state, reason = "not_applicable", "Rule belongs to the other procedural regime."
        elif at < when["effective_from"] or (when["effective_to"] and at > when["effective_to"]):
            state, reason = "not_applicable", "Assessment falls outside this rule version's temporal interval."
        elif applicable is False:
            state, reason = "not_applicable", "Documented applicability condition is false."
        elif applicable is None or check is None:
            state, reason = "unknown", "Required observations or applicability facts are missing/null."
        elif check:
            state, reason = "satisfied", "Selected assertion supported by the supplied observations."
        else:
            state = {"statutory": "not_satisfied", "guidance": "advisory_gap",
                     "service_target": "target_missed", "policy_expectation": "target_missed"}[rule["status"]]
            reason = "Selected assertion is not supported; this is not an overall legal compliance verdict."
        evidence_refs = sorted({eid for k in used if k in case["facts"]
                                for eid in case["facts"][k]["evidence_refs"]})
        results.append({"rule_id": rid, "rule_version": rule["version"], "status": state,
                        "normative_status": rule["status"], "reason": reason,
                        "missing_facts": missing, "evidence_refs": evidence_refs,
                        "sources": [{**c, "url": src[c["source"]]["url"],
                                     "version": src[c["source"]]["version"]} for c in rule["sources"]],
                        "verification": rule["verification"]})
    return {"case_id": case["id"], "model_version": model["model_version"],
            "knowledge_date": model["knowledge_date"], "route": route,
            "limitations": ["Selected assertions only; no overall compliance or soundness certification.",
                            "Future event dates are projections under the recorded source versions; legal updates are not detected.",
                            "Professional judgements are supplied evidence, not computed findings."],
            "results": results}


def load_package(root=ROOT):
    return read_json(root / "model.json"), read_json(root / "sources.json")


def run_examples(model, sources, root=ROOT):
    cases = read_json(root / "examples.json")
    schema_check(cases, "cases.schema.json", root)
    index(cases["cases"], "case")
    for case in cases["cases"]:
        report = evaluate(case, model, sources, root)
        actual = {r["rule_id"]: r["status"] for r in report["results"]}
        if actual != case.get("expected", {}):
            raise ValueError(f"{case['id']}: expected {case.get('expected')}, got {actual}")
        if report["route"]["regime"] != case["expected_route"]:
            raise ValueError(f"{case['id']}: wrong route {report['route']}")
    return len(cases["cases"])


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["validate", "examples", "evaluate"])
    parser.add_argument("--case", type=Path, help="JSON case path for evaluate")
    args = parser.parse_args(argv)
    try:
        model, sources = load_package()
        if args.command == "validate":
            validate_model(model, sources)
            count = run_examples(model, sources)
            print(f"Validated {len(model['rules'])} rules, {len(model['stages'])} stages and {count} examples.")
        elif args.command == "examples":
            print(f"Passed {run_examples(model, sources)} procedural examples.")
        else:
            if args.case is None:
                parser.error("evaluate requires --case")
            print(json.dumps(evaluate(read_json(args.case), model, sources), indent=2))
        return 0
    except (ValueError, OSError, KeyError) as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
