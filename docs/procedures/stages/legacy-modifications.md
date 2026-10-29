# Main modifications and consultation

[Review guide](../README.md) · [Input definitions](../facts.md) · [Worked examples](../worked-examples.md)

Generated from model 0.1.0, knowledge date 2026-10-29. Rebuild with `python tools/build_procedure_docs.py`. Authored explanations live in [editorial notes](../editorial-notes.md). Legal mappings await maintainer review.

If the authority asks, the saved legislation provides for recommendations of
modifications that make the plan sound and meet the saved legal requirements.
The authority-request condition is important when comparing the new system.
Consultation on main modifications has a six-week minimum in Inspectorate guidance;
that normative status is retained even though environmental and fairness duties
may have their own legal bases beyond this package.

**Who is involved:** Examining Inspector; Local planning authority; Representors and public

**Stage inputs:** Proposed main modifications

**Stage outputs:** Representations on main modifications

Stage inputs/outputs are an indicative map; the individual rules below determine which selected document duties are conditional.

## Assertions at this stage

| Assertion | Status | Evaluator operation |
| --- | --- | --- |
| [Recommend necessary curative main modifications when the authority has requested them and they can achieve soundness and legal compliance.](#legacy-mm-request) | Statutory assertion | Supplied observations only |
| [Consult on proposed main modifications for at least six weeks; assess environmental implications as necessary.](#legacy-mm-consultation) | Advisory guidance | Date arithmetic + supplied observations |

<a id="legacy-mm-request"></a>

## Recommend necessary curative main modifications when the authority has requested them and they can achieve soundness and legal compliance.

**Statutory assertion · responsible actor: Examining Inspector**

Rule [`legacy.mm_request`](../../../knowledge/procedures/model.json#L2633); version 0.1.0.

### Source to inspect

- [s 20(7B)-(7C)](https://www.legislation.gov.uk/ukpga/2004/5/section/20/2026-03-24) — PCPA 2004 section 20 immediately before commencement; point in time 2026-03-24, read with SI 2026/169 Sch 1 para 2 (legal basis)
- [Sch 1 para 2(1)(a)](https://www.legislation.gov.uk/uksi/2026/169/schedule/1) — LURA 2023 Commencement No. 11 and Saving and Transitional Provisions Regulations 2026, SI 2026/169; revised Schedule 1 including SI 2026/333 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- **Every** condition below:
  - **No** to: Legacy examiner considers the plan sound and compliant with the saved legal requirements ([input `plan_sound_and_legal`](../facts.md#plan-sound-and-legal)).
  - **Yes** to: Examiner considers the defects curable through modifications ([input `curable_by_modifications`](../facts.md#curable-by-modifications)).
  - **Yes** to: Authority requested main-modification recommendations ([input `lpa_requested_modifications`](../facts.md#lpa-requested-modifications)).

### What the evaluator actually requires

- **Yes** to: Legacy curative main modifications recommended ([input `curative_modifications_recommended`](../facts.md#curative-modifications-recommended)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`curable_by_modifications`](../facts.md#curable-by-modifications) | The examiner considers that modifications can produce a sound plan; for the legacy rule they must also remedy the relevant saved legal requirements. This is a professional conclusion, not a file-presence test. | Reviewer judgement; boolean |
| [`curative_modifications_recommended`](../facts.md#curative-modifications-recommended) | The legacy examiner has recommended the modifications necessary to make the plan sound and meet the saved legal requirements, following the authority’s request where required. | Recorded observation; boolean |
| [`lpa_requested_modifications`](../facts.md#lpa-requested-modifications) | The legacy authority asked the examiner to recommend main modifications under saved PCPA section 20(7C). | Recorded observation; boolean |
| [`plan_sound_and_legal`](../facts.md#plan-sound-and-legal) | Inspector considers it reasonable to conclude that the legacy plan meets s 20(5)(a) requirements and is sound. Read with the 2026 saving: the excluded s 33A duty is not tested. | Reviewer judgement; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

The request is a condition of the saved modification-recommendation provision.
If the authority did not ask, this selected duty is not applicable; that is different
from concluding that the plan is sound, can be adopted unchanged, or cannot be
modified through any other lawful route.


**Examples selecting this assertion:**

- [Saved s 20(7C) modification duty is conditional on LPA request.](../../../knowledge/procedures/examples.json#L1297)
- [Legacy statutory non-adoption can coexist with recommended curative modifications and a permitted adoption route.](../worked-examples.md#legacy-non-adoption-with-curative-modifications)

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="legacy-mm-consultation"></a>

## Consult on proposed main modifications for at least six weeks; assess environmental implications as necessary.

**Advisory guidance · responsible actor: Local planning authority**

Rule [`legacy.mm_consultation`](../../../knowledge/procedures/model.json#L2695); version 0.1.0.

### Source to inspect

- [Stage 2; section 6](https://www.gov.uk/government/publications/examining-local-plans-procedural-practice/procedure-guide-for-local-plan-examinations) — Procedure Guide for Local Plan Examinations; 11th edition; updated 2026-08-20 (guidance)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- [Calendar deadline for representations on those legacy proposed main modifications](../facts.md#mm-deadline) is at least **42 calendar days** after [Calendar date on which the legacy proposed main modifications were published for the consultation being assessed](../facts.md#mm-published).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`mm_deadline`](../facts.md#mm-deadline) | Calendar deadline for representations on those legacy proposed main modifications. | Recorded observation; date |
| [`mm_published`](../facts.md#mm-published) | Calendar date on which the legacy proposed main modifications were published for the consultation being assessed. | Recorded observation; date |

</details>

**Results:** a true check yields `satisfied`; a false check yields `advisory_gap`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

Six-week procedural guidance is not relabelled as a period prescribed by the 2012 Regulations. Underlying SEA/HRA and fairness duties require separate analysis.


**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-08-20 to no end encoded, selected by assessment date. **Verification:** guidance_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

## Connections to other stages

- [Independent examination and hearings](legacy-examination.md) → [Main modifications and consultation](legacy-modifications.md): Curative modifications possible and authority asks for recommendation. (decision).
- [Main modifications and consultation](legacy-modifications.md) → [QA, fact check and final report](legacy-reporting.md): Consultation and response consideration complete. (sequence).

These relationships are descriptive. They are not executable workflow guards.
