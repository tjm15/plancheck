# Independent examination and hearings

[Review guide](../README.md) · [Input definitions](../facts.md) · [Worked examples](../worked-examples.md)

Generated from model 0.1.0, knowledge date 2026-10-29. Rebuild with `python tools/build_procedure_docs.py`. Authored explanations live in [editorial notes](../editorial-notes.md). Legal mappings await maintainer review.

The Inspector examines the plan and considers representations. For the statutory
hearing entitlement, the saved provision requires a representation seeking change
and a request to be heard. The authority's six-week hearing notice and notification
to non-withdrawn regulation 20 representors are separate duties. Participation
outside this entitlement can still be allowed; a false entitlement condition does
not mean that a person is prohibited from attending.

**Who is involved:** Examining Inspector; Local planning authority; Programme Officer; Representors and public

**Stage inputs:** Proposed Local Plan; Supporting evidence selected by the authority; Representations and their identifiers

**Stage outputs:** Matters, issues and questions; Hearing notice; Requested hearing statements; Attributed professional decision record

Stage inputs/outputs are an indicative map; the individual rules below determine which selected document duties are conditional.

## Assertions at this stage

| Assertion | Status | Evaluator operation |
| --- | --- | --- |
| [Give at least six weeks’ notice of hearing details and examiner name; notify non-withdrawn Regulation 20 representors.](#legacy-hearing-notice) | Statutory assertion | Date arithmetic + supplied observations |
| [A representor seeking a change who requests to be heard must have that opportunity.](#legacy-hearing-right) | Statutory assertion | Supplied observations only |
| [Consider Regulation 20 representations before recommendations.](#legacy-consider-representations) | Statutory assertion | Supplied observations only |

<a id="legacy-hearing-notice"></a>

## Give at least six weeks’ notice of hearing details and examiner name; notify non-withdrawn Regulation 20 representors.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`legacy.hearing_notice`](../../../knowledge/procedures/model.json#L2482); version 0.1.0.

### Source to inspect

- [reg 24(1)-(2)](https://www.legislation.gov.uk/uksi/2012/767/regulation/24) — Town and Country Planning (Local Planning) (England) Regulations 2012, SI 2012/767; revised Part 6 retrieved 2026-10-29; pre-2026 text as saved (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- **Yes** to: A hearing is to be held, triggering the selected hearing-notice assertion ([input `hearing_to_be_held`](../facts.md#hearing-to-be-held)).

### What the evaluator actually requires

- **Every** condition below:
  - [Calendar date on which the hearing being assessed opens](../facts.md#hearing-opens) is at least **42 calendar days** after [Calendar date on which the required hearing details and examiner name were made available for the hearing being assessed](../facts.md#hearing-notice-published).
  - **Yes** to: The hearing date, time, place and examiner name were notified to persons who made regulation 20 representations and have not withdrawn them, under legacy regulation 24(2) ([input `legacy_nonwithdrawn_representors_notified`](../facts.md#legacy-nonwithdrawn-representors-notified)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`hearing_notice_published`](../facts.md#hearing-notice-published) | Calendar date on which the required hearing details and examiner name were made available for the hearing being assessed. | Recorded observation; date |
| [`hearing_opens`](../facts.md#hearing-opens) | Calendar date on which the hearing being assessed opens. | Recorded observation; date |
| [`hearing_to_be_held`](../facts.md#hearing-to-be-held) | A hearing is to be held, triggering the selected hearing-notice assertion. | Recorded observation; boolean |
| [`legacy_nonwithdrawn_representors_notified`](../facts.md#legacy-nonwithdrawn-representors-notified) | The hearing date, time, place and examiner name were notified to persons who made regulation 20 representations and have not withdrawn them, under legacy regulation 24(2). | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="legacy-hearing-right"></a>

## A representor seeking a change who requests to be heard must have that opportunity.

**Statutory assertion · responsible actor: Examining Inspector**

Rule [`legacy.hearing_right`](../../../knowledge/procedures/model.json#L2535); version 0.1.0.

### Source to inspect

- [s 20(6)](https://www.legislation.gov.uk/ukpga/2004/5/section/20/2026-03-24) — PCPA 2004 section 20 immediately before commencement; point in time 2026-03-24, read with SI 2026/169 Sch 1 para 2 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- **Every** condition below:
  - **Yes** to: The person being assessed made a representation on this plan ([input `representation_made`](../facts.md#representation-made)).
  - **Yes** to: The person’s representation seeks a change to the legacy plan, engaging the additional condition in saved PCPA section 20(6) ([input `representation_seeks_change`](../facts.md#representation-seeks-change)).
  - **Yes** to: The person being assessed requested an opportunity to appear before and be heard by the examiner ([input `hearing_requested`](../facts.md#hearing-requested)).

### What the evaluator actually requires

- **Yes** to: The person being assessed was given an opportunity to appear before and be heard by the examiner ([input `hearing_opportunity_given`](../facts.md#hearing-opportunity-given)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`hearing_opportunity_given`](../facts.md#hearing-opportunity-given) | The person being assessed was given an opportunity to appear before and be heard by the examiner. | Recorded observation; boolean |
| [`hearing_requested`](../facts.md#hearing-requested) | The person being assessed requested an opportunity to appear before and be heard by the examiner. | Recorded observation; boolean |
| [`representation_made`](../facts.md#representation-made) | The person being assessed made a representation on this plan. The case concerns one person’s hearing entitlement. | Recorded observation; boolean |
| [`representation_seeks_change`](../facts.md#representation-seeks-change) | The person’s representation seeks a change to the legacy plan, engaging the additional condition in saved PCPA section 20(6). | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

- Recorded exception: Additional participation may be invited; absence of this entitlement is not a prohibition.

**Examples selecting this assertion:**

- [Saved s 20(6) entitlement requires a representation seeking change.](../../../knowledge/procedures/examples.json#L1181)

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="legacy-consider-representations"></a>

## Consider Regulation 20 representations before recommendations.

**Statutory assertion · responsible actor: Examining Inspector**

Rule [`legacy.consider_representations`](../../../knowledge/procedures/model.json#L2592); version 0.1.0.

### Source to inspect

- [reg 23](https://www.legislation.gov.uk/uksi/2012/767/regulation/23) — Town and Country Planning (Local Planning) (England) Regulations 2012, SI 2012/767; revised Part 6 retrieved 2026-10-29; pre-2026 text as saved (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: The examiner has considered the regulation 20 representations before making recommendations, as required by legacy regulation 23 ([input `reg20_representations_considered`](../facts.md#reg20-representations-considered)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`reg20_representations_considered`](../facts.md#reg20-representations-considered) | The examiner has considered the regulation 20 representations before making recommendations, as required by legacy regulation 23. | Reviewer judgement; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

## Connections to other stages

- [Regulation 22 submission](legacy-submission.md) → [Independent examination and hearings](legacy-examination.md): Follow statutory preparation, publication and submission requirements. (sequence).
- [Independent examination and hearings](legacy-examination.md) → [Main modifications and consultation](legacy-modifications.md): Curative modifications possible and authority asks for recommendation. (decision).
- [Independent examination and hearings](legacy-examination.md) → [Further work / pause](legacy-pause.md): Inspector allows limited further work. (discretion).
- [Further work / pause](legacy-pause.md) → [Independent examination and hearings](legacy-examination.md): Further work permits examination to continue. (advisory).
- [Independent examination and hearings](legacy-examination.md) → [QA, fact check and final report](legacy-reporting.md): Examination completed; statutory recommendations. (decision).

These relationships are descriptive. They are not executable workflow guards.
