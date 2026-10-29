# Local Plan procedural knowledge

**Start with the [readable review guide](../../docs/procedures/README.md).**
It explains the model, compares the two procedures and links to stage-by-stage
assertions and ten worked examples. The pages show each source, the actual
predicate, evidence definitions and what still depends on a reviewer. This file
is the technical reference for running and maintaining the package.

This is a reviewable foundation for the wider Planner's Assistant: versioned
procedural knowledge for ordinary English Local Plans in the saved 2012 system
and the 2026 system. It is not an implemented Local Plan application or an
exhaustive compliance service. The knowledge date is **29 October 2026**.

The initial package contains 25 stages, 110 rules, 45 document types and 49
synthetic examples. It reuses recovered guidance to locate relevant passages,
but bases statutory assertions on the underlying legislation. All rule mappings
remain marked `maintainer_review_pending`; that review is distinct from the
recorded primary-text checks.

## Run locally

Use Python 3.12 and a virtual environment. The validator does not fetch sources
or send case data anywhere.

```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-procedures.txt
python tools/procedure_model.py validate
python -m unittest discover -s tests -v
python tools/procedure_model.py evaluate --case knowledge/procedures/example-case.json
```

Run commands from the repository root. `validate` checks schemas, cross-references,
normative/source consistency and every expected example result. `examples` runs
the examples separately. Invalid data or failed examples produce a non-zero exit
status. An evaluated `not_satisfied` assertion is ordinary JSON output, not a
validation error. CI runs validation and the test suite on relevant changes.

## Files and contracts

| File | Purpose |
| --- | --- |
| [model.json](model.json) | Regimes, actors, documents, stages, fact definitions, rules, transitions and explicit coverage gaps |
| [sources.json](sources.json) | Official source URLs, editions/versions, retrieval dates, licences and editorial caveats |
| [schemas/](schemas/) | JSON Schema Draft 2020-12 contracts for model, sources and evidence-backed cases |
| [examples.json](examples.json) | Synthetic cases with expected routes and individual assertion results |
| [example-case.json](example-case.json) | Standalone gateway 2 example for the CLI |
| [../../tools/procedure_model.py](../../tools/procedure_model.py) | Replaceable reference validator and evaluator |
| [../../tests/test_procedure_model.py](../../tests/test_procedure_model.py) | Integrity, provenance, uncertainty and regression tests |
| [../../docs/procedural-source-review.md](../../docs/procedural-source-review.md) | Recovery record, legal verification and important interpretation decisions |
| [../../docs/procedures/README.md](../../docs/procedures/README.md) | Human review route, stage catalogue, evidence definitions and worked results |
| [NOTICE.md](NOTICE.md) | Source attribution and licensing |

Rules have stable IDs and explicit versions, regime, actor, stage, normative
status, applicability and check expressions, document references, source locators,
temporal intervals, timing metadata, exceptions and verification state. Facts
distinguish recorded observations from professional judgements. Stage inputs and
outputs describe artefact types; they do not prescribe a storage system.

`transitions` describe cited relationships, including repeated gateway 3, a
pause/resumption path and discretionary steps. Their conditions are explanatory
text, **not executable workflow guards**. Only the rule expressions are evaluated.
The graph is not a complete state machine and does not assert that every possible
withdrawal, intervention or procedural variation is enumerated.

## Applicability and time

Supply an evidenced legal basis, not just a submission date:

| Case context | Routing behaviour |
| --- | --- |
| `pcpa_15c` | New-system preparation under the commenced 2026 framework |
| `saved_2012`, submission by 31 December 2026 inclusive | Saved legacy route; examination/adoption may continue later |
| `saved_2012`, later submission with verified plan-specific direction and valid later deadline | Saved legacy route |
| `saved_2012`, separately evidenced saving eligibility | Explicit review of the applicable statutory saving, including alternative limbs |
| Unknown basis or missing eligibility evidence | `unknown` |
| Late legacy submission without an established saving | `legacy_eligibility_unestablished`; never silently converted into a new-system plan |
| Other jurisdiction, unsupported plan/route, or assessment before 25 March 2026 | `out_of_scope` |

The collection page's “on or after 31 December 2026” wording is not used as a
universal regime switch. SI 2026/169 Schedule 1 paragraph 4 includes that date in
the ordinary saved-system deadline and permits specified extensions. A declared
legal basis and reviewer observations are inputs whose authenticity the evaluator
cannot independently establish.

There are three separate time concepts: `knowledge_date` records the research
cutoff; each rule's `temporal` interval bounds the version represented; and case
facts record procedural event dates. `assessment_date` selects the represented
version. This initial package supports assessments from 25 March 2026 and does
not reconstruct all earlier law. Guidance versions start at their recorded update
dates. For a retrospective event, select the appropriate assessment/source version;
do not assume that a current assessment recreates the rules operative at every
earlier event. Future dates are scenarios under the recorded law, not predictions
that it will remain unchanged.

The executable calendar arithmetic is deliberately limited to the express
calendar-date comparisons: six weeks = 42 days, eight weeks = 56 days, same-day
requirements and “day after” sequencing. Four-month, five-year, working-day and
six-calendar-month assessments require evidenced reviewer observations. A response
on the pause's final calendar date is not automatically late: actual delivery
before expiry must be established. No working-day calendar, time-zone assumption
or electronic deemed-receipt rule is silently supplied.

## Evidence and evaluation

A case selects specific `rule_ids`. Select the assertions relevant to the stage
and event being reviewed; the evaluator does not infer which future duties are
already due. `not_satisfied` means that the selected assertion is false on the
supplied observations; it is not a finding of an overdue obligation or unlawfulness.

Each observed fact has a value and non-empty `evidence_refs`. Referenced evidence
records contain a kind, locator and note. Real cases should identify a document
revision and paragraph/page, a dated decision, a consultation register or another
reviewable record. Do not use the synthetic fixtures as evidence about an authority.
The `context.basis_evidence_refs` records the basis for selecting the regime.
Routing output also retains evidence for submission dates and any direction used.

An omitted fact or a `null` value is unknown. `false` is an evidenced negative
observation. Boolean strings such as `"false"` are rejected. There is no automatic
extraction of facts from files and no inference that a document's existence proves
its adequacy. Compound `*_recorded` observations mean the reviewer has checked the
full cited assertion, including required recipients and timing where specified.
They are not satisfied merely by finding a file with a matching name.

| Result | Meaning |
| --- | --- |
| `satisfied` | Selected assertion follows from supplied observations |
| `not_satisfied` | Selected statutory assertion is false on those observations |
| `advisory_gap` | Recommended practice is absent; not a statutory breach |
| `target_missed` | Service target or policy expectation is not met |
| `unknown` | Necessary evidence, judgement or supported applicability is missing |
| `not_applicable` | Different regime/version or an expressly false applicability condition |

Expressions use three-valued logic: a known false conjunct can settle an `all`
expression even if another fact is unknown; a known true disjunct can settle an
`any` expression. Every result still reports missing facts, evidence references,
rule version and source version/locator. There is no aggregate compliance score.

Some exceptions are executable conditions, such as the legacy map-change trigger,
SEA document alternatives and an operative spatial development strategy. Others
are recorded as review notes, especially special directions outside ordinary
procedure. Consumers must not treat free-text exceptions as automatically resolved.

## Integration and change discipline

These JSON files are the canonical authored data. The Python evaluator is a small
reference implementation, not a choice of PlanCheck backend, database, interface
or reasoning architecture. Its schema dependency is isolated in
`requirements-procedures.txt`.

Document and fact IDs can connect to an evidence repository, policy identifiers,
spatial geometries, consultation records, plan versions, scenarios and monitoring
outcomes. For example, the policies-map rules need actual geographical-policy
evidence, and gateway 3's measurable outcomes can later connect to monitoring.
Procedural knowledge supplies constraints and provenance to those capabilities;
it does not define the whole product as a checklist or document viewer.

For a source update:

1. Inspect the official legislation, amendments, commencement and savings, then
   the relevant guidance edition. Record unresolved editorial effects.
2. Preserve a source/version record and precise provision or paragraph locator.
   Guidance may support an explanation but cannot supply a `legal_basis` citation.
3. Update the rule version and temporal coverage. If historical coexistence is
   needed, retain a separate package release; do not overwrite the only historical
   record and claim that this evaluator supports multiple versions of one rule ID.
4. Record how an exception is handled: executable predicate, evidenced judgement
   or unsupported route. Add boundary, missing-evidence and wrong-regime examples.
5. Run validation and tests; have a maintainer review the legal mapping separately
   from the software checks. Tests cannot establish that an interpretation is right.

Version `0.1.0` is a provisional interchange contract. Git history preserves this
release. There is no permanent architecture decision and no runtime network
dependency on the source websites.

Readable stage, fact and worked-example pages are rebuilt with
`python tools/build_procedure_docs.py`. CI runs the same command with `--check`
to detect drift. Interpretation notes in `docs/procedures/editorial-notes.md`
remain hand-authored and require substantive review.

## Coverage limits

The implemented spine covers preparation, consultation, readiness, submission,
hearing participation, modifications, pauses, reporting, adoption and withdrawal.
The new system includes all three gateways, the twelve regulation 32 assessment
headings and repeated gateway 3. The saved legacy system includes selected duties within Regulations
18–27, checklist practice and the saved examination/adoption decision conditions.

The model's `coverage.gaps` is part of the data contract. In particular, initial
rollout cohorts/latest dates, detailed publication mechanics and consultee
directories, substantive SEA/HRA and soundness judgements, special/joint and
intervention routes, standalone minerals/waste plans and court-challenge arithmetic
need further work. It does not automatically monitor legislation changes. These
limits must accompany any integration that exposes its findings.
