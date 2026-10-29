# QA, fact check and final report

[Review guide](../README.md) · [Input definitions](../facts.md) · [Worked examples](../worked-examples.md)

Generated from model 0.1.0, knowledge date 2026-10-29. Rebuild with `python tools/build_procedure_docs.py`. Authored explanations live in [editorial notes](../editorial-notes.md). Legal mappings await maintainer review.

At the end of examination the Inspector makes reasoned recommendations, and the
authority publishes them. Under the saved statutory text, a recommendation of
non-adoption can coexist with recommended curative main modifications. The saved
adoption provision then permits adoption with those modifications. The stage label
also mentions QA and fact checking, but their administrative steps are not encoded
as individual checks in this release.

**Who is involved:** Examining Inspector; Local planning authority

**Stage inputs:** Attributed professional decision record

**Stage outputs:** Final recommendations and reasons

Stage inputs/outputs are an indicative map; the individual rules below determine which selected document duties are conditional.

## Assertions at this stage

| Assertion | Status | Evaluator operation |
| --- | --- | --- |
| [Publish final recommendations and reasons and notify those who requested notification.](#legacy-report-publication) | Statutory assertion | Supplied observations only |
| [After examination, recommend adoption with reasons where it is reasonable to conclude that the plan is sound and meets the saved legal requirements.](#legacy-report-adopt) | Statutory assertion | Supplied observations only |
| [After examination, recommend non-adoption with reasons where the statutory condition for recommending adoption is not met.](#legacy-report-non-adoption) | Statutory assertion | Supplied observations only |

<a id="legacy-report-publication"></a>

## Publish final recommendations and reasons and notify those who requested notification.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`legacy.report_publication`](../../../knowledge/procedures/model.json#L2786); version 0.1.0.

### Source to inspect

- [reg 25](https://www.legislation.gov.uk/uksi/2012/767/regulation/25) — Town and Country Planning (Local Planning) (England) Regulations 2012, SI 2012/767; revised Part 6 retrieved 2026-10-29; pre-2026 text as saved (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: Final legacy recommendations and reasons were published and required notifications sent under regulation 25, using the correct trigger if a relevant Secretary of State direction applies ([input `legacy_report_publication_recorded`](../facts.md#legacy-report-publication-recorded)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`legacy_report_publication_recorded`](../facts.md#legacy-report-publication-recorded) | Final legacy recommendations and reasons were published and required notifications sent under regulation 25, using the correct trigger if a relevant Secretary of State direction applies. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

- Recorded exception: If a relevant Secretary of State direction follows the recommendation, reg 25(1)(b) changes the publication trigger.

**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="legacy-report-adopt"></a>

## After examination, recommend adoption with reasons where it is reasonable to conclude that the plan is sound and meets the saved legal requirements.

**Statutory assertion · responsible actor: Examining Inspector**

Rule [`legacy.report_adopt`](../../../knowledge/procedures/model.json#L6641); version 0.1.0.

### Source to inspect

- [s 20(7)-(7A)](https://www.legislation.gov.uk/ukpga/2004/5/section/20/2026-03-24) — PCPA 2004 section 20 immediately before commencement; point in time 2026-03-24, read with SI 2026/169 Sch 1 para 2 (legal basis)
- [Sch 1 para 2(1)(a)](https://www.legislation.gov.uk/uksi/2026/169/schedule/1) — LURA 2023 Commencement No. 11 and Saving and Transitional Provisions Regulations 2026, SI 2026/169; revised Schedule 1 including SI 2026/333 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- **Every** condition below:
  - **Yes** to: Independent examination completed ([input `examination_completed`](../facts.md#examination-completed)).
  - **Yes** to: Legacy examiner considers the plan sound and compliant with the saved legal requirements ([input `plan_sound_and_legal`](../facts.md#plan-sound-and-legal)).

### What the evaluator actually requires

- **Yes** to: The examiner recommended adoption and gave reasons under the selected regime’s statutory recommendation condition ([input `adoption_recommended_with_reasons`](../facts.md#adoption-recommended-with-reasons)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`adoption_recommended_with_reasons`](../facts.md#adoption-recommended-with-reasons) | The examiner recommended adoption and gave reasons under the selected regime’s statutory recommendation condition. | Recorded observation; boolean |
| [`examination_completed`](../facts.md#examination-completed) | The examiner has carried out the independent examination; the final recommendation provisions are now being assessed. | Recorded observation; boolean |
| [`plan_sound_and_legal`](../facts.md#plan-sound-and-legal) | Inspector considers it reasonable to conclude that the legacy plan meets s 20(5)(a) requirements and is sound. Read with the 2026 saving: the excluded s 33A duty is not tested. | Reviewer judgement; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- [Legacy statutory non-adoption can coexist with recommended curative modifications and a permitted adoption route.](../worked-examples.md#legacy-non-adoption-with-curative-modifications)

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="legacy-report-non-adoption"></a>

## After examination, recommend non-adoption with reasons where the statutory condition for recommending adoption is not met.

**Statutory assertion · responsible actor: Examining Inspector**

Rule [`legacy.report_non_adoption`](../../../knowledge/procedures/model.json#L6698); version 0.1.0.

### Source to inspect

- [s 20(7)-(7A)](https://www.legislation.gov.uk/ukpga/2004/5/section/20/2026-03-24) — PCPA 2004 section 20 immediately before commencement; point in time 2026-03-24, read with SI 2026/169 Sch 1 para 2 (legal basis)
- [Sch 1 para 2(1)(a)](https://www.legislation.gov.uk/uksi/2026/169/schedule/1) — LURA 2023 Commencement No. 11 and Saving and Transitional Provisions Regulations 2026, SI 2026/169; revised Schedule 1 including SI 2026/333 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- **Every** condition below:
  - **Yes** to: Independent examination completed ([input `examination_completed`](../facts.md#examination-completed)).
  - **No** to: Legacy examiner considers the plan sound and compliant with the saved legal requirements ([input `plan_sound_and_legal`](../facts.md#plan-sound-and-legal)).

### What the evaluator actually requires

- **Yes** to: Legacy non-adoption recommendation and reasons issued ([input `non_adoption_recommended_with_reasons`](../facts.md#non-adoption-recommended-with-reasons)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`examination_completed`](../facts.md#examination-completed) | The examiner has carried out the independent examination; the final recommendation provisions are now being assessed. | Recorded observation; boolean |
| [`non_adoption_recommended_with_reasons`](../facts.md#non-adoption-recommended-with-reasons) | Inspector recommends non-adoption and gives reasons under saved s 20(7A). This may coexist with curative modifications under s 20(7C). | Recorded observation; boolean |
| [`plan_sound_and_legal`](../facts.md#plan-sound-and-legal) | Inspector considers it reasonable to conclude that the legacy plan meets s 20(5)(a) requirements and is sound. Read with the 2026 saving: the excluded s 33A duty is not tested. | Reviewer judgement; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

A curative modification recommendation under s 20(7C) can accompany non-adoption under s 20(7A); s 23(2A)-(3) permits adoption with those main modifications.


**Examples selecting this assertion:**

- [Legacy statutory non-adoption can coexist with recommended curative modifications and a permitted adoption route.](../worked-examples.md#legacy-non-adoption-with-curative-modifications)

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

## Connections to other stages

- [Independent examination and hearings](legacy-examination.md) → [QA, fact check and final report](legacy-reporting.md): Examination completed; statutory recommendations. (decision).
- [Main modifications and consultation](legacy-modifications.md) → [QA, fact check and final report](legacy-reporting.md): Consultation and response consideration complete. (sequence).
- [QA, fact check and final report](legacy-reporting.md) → [Adoption and publication](legacy-adoption.md): Authority chooses adoption permitted by saved s 23, with required main modifications and only permitted additional changes. (decision).

These relationships are descriptive. They are not executable workflow guards.
