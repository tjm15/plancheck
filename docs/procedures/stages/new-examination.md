# Independent examination and hearings

[Review guide](../README.md) · [Input definitions](../facts.md) · [Worked examples](../worked-examples.md)

Generated from model 0.1.0, knowledge date 2026-10-29. Rebuild with `python tools/build_procedure_docs.py`. Authored explanations live in [editorial notes](../editorial-notes.md). Legal mappings await maintainer review.

The examiner considers whether it is reasonable to conclude that the plan is
sound. Any representor requesting to be heard has the new statutory entitlement;
the saved system's additional seeking-change condition is absent. Six-week hearing
notice is a separate procedural check. The guide's six-month examination expectation
is a target, distinct from the statutory maximum for an individual pause.

**Who is involved:** Examining Inspector; Local planning authority; Programme Officer; Representors and public

**Stage inputs:** Proposed Local Plan; Supporting evidence selected by the authority

**Stage outputs:** Matters, issues and questions; Hearing notice; Requested hearing statements; Attributed professional decision record

Stage inputs/outputs are an indicative map; the individual rules below determine which selected document duties are conditional.

## Assertions at this stage

| Assertion | Status | Evaluator operation |
| --- | --- | --- |
| [Publish hearing details and examiner name at least six weeks before the hearing, and notify requesters and other appropriate persons.](#new-hearing-notice) | Statutory assertion | Date arithmetic + supplied observations |
| [A person making representations who requests to be heard must have that opportunity.](#new-hearing-right) | Statutory assertion | Supplied observations only |
| [Government expects examinations to take no longer than six months.](#new-examination-target) | Policy expectation | Supplied observations only |

<a id="new-hearing-notice"></a>

## Publish hearing details and examiner name at least six weeks before the hearing, and notify requesters and other appropriate persons.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.hearing_notice`](../../../knowledge/procedures/model.json#L5842); version 0.1.0.

### Source to inspect

- [reg 35](https://www.legislation.gov.uk/uksi/2026/186/regulation/35/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- **Yes** to: A hearing is to be held, triggering the selected hearing-notice assertion ([input `hearing_to_be_held`](../facts.md#hearing-to-be-held)).

### What the evaluator actually requires

- **Every** condition below:
  - [Calendar date on which the hearing being assessed opens](../facts.md#hearing-opens) is at least **42 calendar days** after [Calendar date on which the required hearing details and examiner name were made available for the hearing being assessed](../facts.md#hearing-notice-published).
  - **Yes** to: Persons who requested notification and other persons the authority considers appropriate received the regulation 35 hearing notice with date, time, place and examiner name ([input `new_hearing_requesters_notified`](../facts.md#new-hearing-requesters-notified)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`hearing_notice_published`](../facts.md#hearing-notice-published) | Calendar date on which the required hearing details and examiner name were made available for the hearing being assessed. | Recorded observation; date |
| [`hearing_opens`](../facts.md#hearing-opens) | Calendar date on which the hearing being assessed opens. | Recorded observation; date |
| [`hearing_to_be_held`](../facts.md#hearing-to-be-held) | A hearing is to be held, triggering the selected hearing-notice assertion. | Recorded observation; boolean |
| [`new_hearing_requesters_notified`](../facts.md#new-hearing-requesters-notified) | Persons who requested notification and other persons the authority considers appropriate received the regulation 35 hearing notice with date, time, place and examiner name. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-hearing-right"></a>

## A person making representations who requests to be heard must have that opportunity.

**Statutory assertion · responsible actor: Examining Inspector**

Rule [`new.hearing_right`](../../../knowledge/procedures/model.json#L5895); version 0.1.0.

### Source to inspect

- [s 15D(6)](https://www.legislation.gov.uk/ukpga/2004/5/section/15D) — PCPA 2004 section 15D; revised text retrieved 2026-10-29 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- **Every** condition below:
  - **Yes** to: The person being assessed made a representation on this plan ([input `representation_made`](../facts.md#representation-made)).
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

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

Unlike saved s 20(6), the statutory wording does not limit the right to representations seeking a change.


**Examples selecting this assertion:**

- [New s 15D(6) does not contain the seeking-change restriction.](../../../knowledge/procedures/examples.json#L1242)

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-examination-target"></a>

## Government expects examinations to take no longer than six months.

**Policy expectation · responsible actor: Examining Inspector**

Rule [`new.examination_target`](../../../knowledge/procedures/model.json#L5945); version 0.1.0.

### Source to inspect

- [2.7](https://www.gov.uk/guidance/procedural-guide-for-examinations-and-gateways-under-the-town-and-country-planning-local-planning-england-regulations-2026) — Procedural guide for Examinations and Gateways under the 2026 Regulations; first edition; updated 2026-08-26 (guidance)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: Reviewer confirms the six-month examination expectation was met ([input `examination_target_met`](../facts.md#examination-target-met)).

**Timing:** examination start → completion; policy expectation; not the statutory pause limit.

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`examination_target_met`](../facts.md#examination-target-met) | An evidenced duration assessment establishes whether the new examination met the government’s six-month expectation. This is distinct from the statutory pause limit and is not calculated from event dates by this evaluator. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `target_missed`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- [Six-month statutory pause maximum is distinct from examination target.](../worked-examples.md#new-pause-limit)

**Recorded version interval:** 2026-08-26 to no end encoded, selected by assessment date. **Verification:** guidance_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

## Connections to other stages

- [Submission after gateway 3](new-submission.md) → [Independent examination and hearings](new-examination.md): Plan submitted; Secretary of State appoints examiner. (sequence).
- [Independent examination and hearings](new-examination.md) → [Statutory examination pause](new-pause.md): Examiner decides matters may be resolved through further work. (discretion).
- [Statutory examination pause](new-pause.md) → [Independent examination and hearings](new-examination.md): No s 15DA(8) withdrawal recommendation at pause end. (decision).
- [Independent examination and hearings](new-examination.md) → [Main modifications and consultation](new-modifications.md): Soundness can be achieved through modifications. (decision).
- [Independent examination and hearings](new-examination.md) → [QA, fact check and final report](new-reporting.md): Reasoned recommendation; withdrawal branch excludes pending pause. (decision).

These relationships are descriptive. They are not executable workflow guards.
