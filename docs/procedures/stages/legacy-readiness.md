# Pre-examination preparation

[Review guide](../README.md) · [Input definitions](../facts.md) · [Worked examples](../worked-examples.md)

Generated from model 0.1.0, knowledge date 2026-10-29. Rebuild with `python tools/build_procedure_docs.py`. Authored explanations live in [editorial notes](../editorial-notes.md). Legal mappings await maintainer review.

The pre-examination checklist supports preparation for submission. Its place in
the Inspectorate's procedure guide does not turn it into one of the new system's
statutory gateways. The checklist and ten-working-day response aim are represented
as guidance/service practice. The statutory readiness condition sits in the
submission stage under saved PCPA section 20(2).

**Who is involved:** Local planning authority; Programme Officer

**Stage inputs:** Proposed Local Plan; Representations and their identifiers

**Stage outputs:** Legacy pre-examination checklist; Examination library

Stage inputs/outputs are an indicative map; the individual rules below determine which selected document duties are conditional.

## Assertions at this stage

| Assertion | Status | Evaluator operation |
| --- | --- | --- |
| [Complete and send the pre-examination checklist.](#legacy-checklist) | Advisory guidance | Supplied observations only |
| [Inspectorate aims to respond to the checklist within ten working days.](#legacy-checklist-response) | Service target | Supplied observations only |

<a id="legacy-checklist"></a>

## Complete and send the pre-examination checklist.

**Advisory guidance · responsible actor: Local planning authority**

Rule [`legacy.checklist`](../../../knowledge/procedures/model.json#L2084); version 0.1.0.

### Source to inspect

- [Stage 0; section 1](https://www.gov.uk/government/publications/examining-local-plans-procedural-practice/procedure-guide-for-local-plan-examinations) — Procedure Guide for Local Plan Examinations; 11th edition; updated 2026-08-20 (guidance)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: The authority has completed and sent the pre-examination checklist described by the legacy procedure guide ([input `legacy_checklist_sent`](../facts.md#legacy-checklist-sent)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`legacy_checklist_sent`](../facts.md#legacy-checklist-sent) | The authority has completed and sent the pre-examination checklist described by the legacy procedure guide. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `advisory_gap`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

Operational expectation, not a statutory gateway or legal permission to submit.


**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-08-20 to no end encoded, selected by assessment date. **Verification:** guidance_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="legacy-checklist-response"></a>

## Inspectorate aims to respond to the checklist within ten working days.

**Service target · responsible actor: Examining Inspector**

Rule [`legacy.checklist_response`](../../../knowledge/procedures/model.json#L2125); version 0.1.0.

### Source to inspect

- [Stage 0](https://www.gov.uk/government/publications/examining-local-plans-procedural-practice/procedure-guide-for-local-plan-examinations) — Procedure Guide for Local Plan Examinations; 11th edition; updated 2026-08-20 (guidance)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: An evidenced review of checklist receipt and Inspectorate response establishes whether the ten-working-day service aim was met ([input `legacy_checklist_response_target_met`](../facts.md#legacy-checklist-response-target-met)).

**Timing:** receipt of checklist → response; not computed; England holidays and receipt rules required.

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`legacy_checklist_response_target_met`](../facts.md#legacy-checklist-response-target-met) | An evidenced review of checklist receipt and Inspectorate response establishes whether the ten-working-day service aim was met. The evaluator does not calculate working days. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `target_missed`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-08-20 to no end encoded, selected by assessment date. **Verification:** guidance_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

## Connections to other stages

- [Pre-examination preparation](legacy-readiness.md) → [Regulation 22 submission](legacy-submission.md): Checklist supports readiness; not a statutory gateway. (advisory).

These relationships are descriptive. They are not executable workflow guards.
