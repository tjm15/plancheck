# Main modifications and consultation

[Review guide](../README.md) · [Input definitions](../facts.md) · [Worked examples](../worked-examples.md)

Generated from model 0.1.0, knowledge date 2026-10-29. Rebuild with `python tools/build_procedure_docs.py`. Authored explanations live in [editorial notes](../editorial-notes.md). Legal mappings await maintainer review.

On completing examination, if modifications would make the plan sound, the new
statutory recommendation includes those modifications, adoption with them, and
reasons. It does not depend on the saved system's LPA-request condition. Consultation
and necessary environmental/habitats assessment work are recorded as guidance in
this package; their full underlying substantive legal framework needs a separate model.

**Who is involved:** Examining Inspector; Local planning authority; Representors and public

**Stage inputs:** Proposed main modifications

**Stage outputs:** Representations on main modifications

Stage inputs/outputs are an indicative map; the individual rules below determine which selected document duties are conditional.

## Assertions at this stage

| Assertion | Status | Evaluator operation |
| --- | --- | --- |
| [Recommend modifications and adoption with reasons if they would make it reasonable to conclude that the plan is sound.](#new-mm-recommendation) | Statutory assertion | Supplied observations only |
| [Consult on main modifications and undertake necessary environmental and habitats assessment before recommendation.](#new-mm-consultation) | Advisory guidance | Supplied observations only |

<a id="new-mm-recommendation"></a>

## Recommend modifications and adoption with reasons if they would make it reasonable to conclude that the plan is sound.

**Statutory assertion · responsible actor: Examining Inspector**

Rule [`new.mm_recommendation`](../../../knowledge/procedures/model.json#L5991); version 0.1.0.

### Source to inspect

- [s 15D(10)-(11)](https://www.legislation.gov.uk/ukpga/2004/5/section/15D) — PCPA 2004 section 15D; revised text retrieved 2026-10-29 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- **Every** condition below:
  - **Yes** to: Independent examination completed ([input `examination_completed`](../facts.md#examination-completed)).
  - **No** to: Examiner considers it reasonable to conclude that the plan is sound ([input `plan_sound`](../facts.md#plan-sound)).
  - **Yes** to: Examiner considers the defects curable through modifications ([input `curable_by_modifications`](../facts.md#curable-by-modifications)).

### What the evaluator actually requires

- **Yes** to: Examiner recommends the curative modifications and adoption with those modifications, and gives reasons for the recommendation under s 15D(11) ([input `modifications_and_adoption_recommended_with_reasons`](../facts.md#modifications-and-adoption-recommended-with-reasons)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`curable_by_modifications`](../facts.md#curable-by-modifications) | The examiner considers that modifications can produce a sound plan; for the legacy rule they must also remedy the relevant saved legal requirements. This is a professional conclusion, not a file-presence test. | Reviewer judgement; boolean |
| [`examination_completed`](../facts.md#examination-completed) | The examiner has carried out the independent examination; the final recommendation provisions are now being assessed. | Recorded observation; boolean |
| [`modifications_and_adoption_recommended_with_reasons`](../facts.md#modifications-and-adoption-recommended-with-reasons) | Examiner recommends the curative modifications and adoption with those modifications, and gives reasons for the recommendation under s 15D(11). | Recorded observation; boolean |
| [`plan_sound`](../facts.md#plan-sound) | Examiner considers it reasonable in all the circumstances to conclude that the new-system plan is sound under s 15D(5),(9)-(12). This is not derived from gateway completion or document presence. | Reviewer judgement; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

The statute does not require an LPA request equivalent to saved s 20(7C).


**Examples selecting this assertion:**

- [New modification duty does not depend on the legacy LPA request.](../../../knowledge/procedures/examples.json#L1358)
- [A final recommendation duty is not triggered just by an emerging view during examination.](../../../knowledge/procedures/examples.json#L2069)

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-mm-consultation"></a>

## Consult on main modifications and undertake necessary environmental and habitats assessment before recommendation.

**Advisory guidance · responsible actor: Local planning authority**

Rule [`new.mm_consultation`](../../../knowledge/procedures/model.json#L6048); version 0.1.0.

### Source to inspect

- [8.5-8.8](https://www.gov.uk/guidance/procedural-guide-for-examinations-and-gateways-under-the-town-and-country-planning-local-planning-england-regulations-2026) — Procedural guide for Examinations and Gateways under the 2026 Regulations; first edition; updated 2026-08-26 (guidance)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: Main modifications were consulted upon and the necessary environmental/habitats assessment work undertaken and considered before final recommendation, as described by the new procedure guide ([input `mm_consultation_and_assessments_recorded`](../facts.md#mm-consultation-and-assessments-recorded)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`mm_consultation_and_assessments_recorded`](../facts.md#mm-consultation-and-assessments-recorded) | Main modifications were consulted upon and the necessary environmental/habitats assessment work undertaken and considered before final recommendation, as described by the new procedure guide. | Reviewer judgement; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `advisory_gap`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

- Recorded exception: Further amendments without repeat consultation require Inspector satisfaction that no party is prejudiced (8.10).

**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-08-26 to no end encoded, selected by assessment date. **Verification:** guidance_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

## Connections to other stages

- [Independent examination and hearings](new-examination.md) → [Main modifications and consultation](new-modifications.md): Soundness can be achieved through modifications. (decision).
- [Main modifications and consultation](new-modifications.md) → [QA, fact check and final report](new-reporting.md): Representations considered and recommendations finalised. (sequence).

These relationships are descriptive. They are not executable workflow guards.
