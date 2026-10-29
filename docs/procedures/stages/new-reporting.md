# QA, fact check and final report

[Review guide](../README.md) · [Input definitions](../facts.md) · [Worked examples](../worked-examples.md)

Generated from model 0.1.0, knowledge date 2026-10-29. Rebuild with `python tools/build_procedure_docs.py`. Authored explanations live in [editorial notes](../editorial-notes.md). Legal mappings await maintainer review.

A completed examination can lead to adoption, adoption with modifications or
withdrawal recommendations, each with the relevant statutory conditions and reasons.
The withdrawal branch excludes an examination that is paused or to be paused.
Publication is a separate authority obligation. As in the legacy reporting stage,
QA/fact-check procedure appears in the stage description but is not exhaustively
encoded as separate executable duties.

**Who is involved:** Examining Inspector; Local planning authority

**Stage inputs:** Attributed professional decision record

**Stage outputs:** Final recommendations and reasons

Stage inputs/outputs are an indicative map; the individual rules below determine which selected document duties are conditional.

## Assertions at this stage

| Assertion | Status | Evaluator operation |
| --- | --- | --- |
| [Recommend adoption with reasons when the completed examination concludes it reasonable to find the plan sound.](#new-report-adopt) | Statutory assertion | Supplied observations only |
| [Recommend withdrawal with reasons when soundness cannot be achieved by modifications and the examination is not paused or to be paused.](#new-report-withdraw) | Statutory assertion | Supplied observations only |
| [Publish final recommendations and reasons promptly and notify requesters.](#new-report-publication) | Statutory assertion | Supplied observations only |

<a id="new-report-adopt"></a>

## Recommend adoption with reasons when the completed examination concludes it reasonable to find the plan sound.

**Statutory assertion · responsible actor: Examining Inspector**

Rule [`new.report_adopt`](../../../knowledge/procedures/model.json#L6358); version 0.1.0.

### Source to inspect

- [s 15D(9)](https://www.legislation.gov.uk/ukpga/2004/5/section/15D) — PCPA 2004 section 15D; revised text retrieved 2026-10-29 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- **Every** condition below:
  - **Yes** to: Independent examination completed ([input `examination_completed`](../facts.md#examination-completed)).
  - **Yes** to: Examiner considers it reasonable to conclude that the plan is sound ([input `plan_sound`](../facts.md#plan-sound)).

### What the evaluator actually requires

- **Yes** to: The examiner recommended adoption and gave reasons under the selected regime’s statutory recommendation condition ([input `adoption_recommended_with_reasons`](../facts.md#adoption-recommended-with-reasons)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`adoption_recommended_with_reasons`](../facts.md#adoption-recommended-with-reasons) | The examiner recommended adoption and gave reasons under the selected regime’s statutory recommendation condition. | Recorded observation; boolean |
| [`examination_completed`](../facts.md#examination-completed) | The examiner has carried out the independent examination; the final recommendation provisions are now being assessed. | Recorded observation; boolean |
| [`plan_sound`](../facts.md#plan-sound) | Examiner considers it reasonable in all the circumstances to conclude that the new-system plan is sound under s 15D(5),(9)-(12). This is not derived from gateway completion or document presence. | Reviewer judgement; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- [Gateway 3 success triggers submission; it cannot establish the examination soundness finding.](../worked-examples.md#gateway3-not-soundness-verdict)

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-report-withdraw"></a>

## Recommend withdrawal with reasons when soundness cannot be achieved by modifications and the examination is not paused or to be paused.

**Statutory assertion · responsible actor: Examining Inspector**

Rule [`new.report_withdraw`](../../../knowledge/procedures/model.json#L6410); version 0.1.0.

### Source to inspect

- [s 15D(10)-(12)](https://www.legislation.gov.uk/ukpga/2004/5/section/15D) — PCPA 2004 section 15D; revised text retrieved 2026-10-29 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- **Every** condition below:
  - **Yes** to: Independent examination completed ([input `examination_completed`](../facts.md#examination-completed)).
  - **No** to: Examiner considers it reasonable to conclude that the plan is sound ([input `plan_sound`](../facts.md#plan-sound)).
  - **No** to: Examiner considers the defects curable through modifications ([input `curable_by_modifications`](../facts.md#curable-by-modifications)).
  - **No** to: The new-system examination is paused, or the examiner has decided that it is to be paused, so the section 15D(12) withdrawal condition is not yet met ([input `paused_or_to_be_paused`](../facts.md#paused-or-to-be-paused)).

### What the evaluator actually requires

- **Yes** to: The examiner recommended withdrawal and gave reasons under the applicable new-system withdrawal condition ([input `withdrawal_recommended_with_reasons`](../facts.md#withdrawal-recommended-with-reasons)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`curable_by_modifications`](../facts.md#curable-by-modifications) | The examiner considers that modifications can produce a sound plan; for the legacy rule they must also remedy the relevant saved legal requirements. This is a professional conclusion, not a file-presence test. | Reviewer judgement; boolean |
| [`examination_completed`](../facts.md#examination-completed) | The examiner has carried out the independent examination; the final recommendation provisions are now being assessed. | Recorded observation; boolean |
| [`paused_or_to_be_paused`](../facts.md#paused-or-to-be-paused) | The new-system examination is paused, or the examiner has decided that it is to be paused, so the section 15D(12) withdrawal condition is not yet met. | Recorded observation; boolean |
| [`plan_sound`](../facts.md#plan-sound) | Examiner considers it reasonable in all the circumstances to conclude that the new-system plan is sound under s 15D(5),(9)-(12). This is not derived from gateway completion or document presence. | Reviewer judgement; boolean |
| [`withdrawal_recommended_with_reasons`](../facts.md#withdrawal-recommended-with-reasons) | The examiner recommended withdrawal and gave reasons under the applicable new-system withdrawal condition. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-report-publication"></a>

## Publish final recommendations and reasons promptly and notify requesters.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.report_publication`](../../../knowledge/procedures/model.json#L6472); version 0.1.0.

### Source to inspect

- [reg 37](https://www.legislation.gov.uk/uksi/2026/186/regulation/37/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: Final new-system recommendations and reasons were published and required notifications sent under regulation 37, using the applicable trigger and any relevant direction exception ([input `new_report_publicity_recorded`](../facts.md#new-report-publicity-recorded)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`new_report_publicity_recorded`](../facts.md#new-report-publicity-recorded) | Final new-system recommendations and reasons were published and required notifications sent under regulation 37, using the applicable trigger and any relevant direction exception. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

- Recorded exception: Reg 37(1)(b) changes trigger following specified Secretary of State directions.

**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

## Connections to other stages

- [Independent examination and hearings](new-examination.md) → [QA, fact check and final report](new-reporting.md): Reasoned recommendation; withdrawal branch excludes pending pause. (decision).
- [Main modifications and consultation](new-modifications.md) → [QA, fact check and final report](new-reporting.md): Representations considered and recommendations finalised. (sequence).
- [QA, fact check and final report](new-reporting.md) → [Adoption and publication](new-adoption.md): Authority chooses adoption consistent with recommendation. (decision).

These relationships are descriptive. They are not executable workflow guards.
