# Further work / pause

[Review guide](../README.md) · [Input definitions](../facts.md) · [Worked examples](../worked-examples.md)

Generated from model 0.1.0, knowledge date 2026-10-29. Rebuild with `python tools/build_procedure_docs.py`. Authored explanations live in [editorial notes](../editorial-notes.md). Legal mappings await maintainer review.

The legacy guide permits further work during a pause and describes a usual
six-month overall limit. This model records that as qualified guidance. It does
not import the new legislation's statutory pause mechanism or its prescribed
maximum into the saved regime. The evaluator takes the duration assessment as an
input; it does not determine whether a particular departure from guidance is justified.

**Who is involved:** Examining Inspector; Local planning authority

**Stage inputs:** Attributed professional decision record

**Stage outputs:** Supporting evidence selected by the authority

Stage inputs/outputs are an indicative map; the individual rules below determine which selected document duties are conditional.

## Assertions at this stage

| Assertion | Status | Evaluator operation |
| --- | --- | --- |
| [Further work pauses should not usually exceed six months overall.](#legacy-pause-target) | Advisory guidance | Supplied observations only |

<a id="legacy-pause-target"></a>

## Further work pauses should not usually exceed six months overall.

**Advisory guidance · responsible actor: Examining Inspector**

Rule [`legacy.pause_target`](../../../knowledge/procedures/model.json#L2738); version 0.1.0.

### Source to inspect

- [para 5.21; section 9](https://www.gov.uk/government/publications/examining-local-plans-procedural-practice/procedure-guide-for-local-plan-examinations) — Procedure Guide for Local Plan Examinations; 11th edition; updated 2026-08-20 (guidance)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: An evidenced assessment records whether the legacy further-work pause meets the guide’s usual six-month expectation, taking the guidance’s qualification into account ([input `legacy_pause_normally_within_six_months`](../facts.md#legacy-pause-normally-within-six-months)).

**Timing:** pause start → resumption; professional review; no statutory maximum asserted.

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`legacy_pause_normally_within_six_months`](../facts.md#legacy-pause-normally-within-six-months) | An evidenced assessment records whether the legacy further-work pause meets the guide’s usual six-month expectation, taking the guidance’s qualification into account. No statutory maximum is inferred. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `advisory_gap`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

- Recorded exception: Guidance qualified by “usually”; case-specific procedure may depart fairly.

**Examples selecting this assertion:**

- [Legacy six-month pause guidance is not a statutory maximum.](../../../knowledge/procedures/examples.json#L1482)

**Recorded version interval:** 2026-08-20 to no end encoded, selected by assessment date. **Verification:** guidance_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

## Connections to other stages

- [Independent examination and hearings](legacy-examination.md) → [Further work / pause](legacy-pause.md): Inspector allows limited further work. (discretion).
- [Further work / pause](legacy-pause.md) → [Independent examination and hearings](legacy-examination.md): Further work permits examination to continue. (advisory).

These relationships are descriptive. They are not executable workflow guards.
