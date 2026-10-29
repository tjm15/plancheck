# Statutory examination pause

[Review guide](../README.md) · [Input definitions](../facts.md) · [Worked examples](../worked-examples.md)

Generated from model 0.1.0, knowledge date 2026-10-29. Rebuild with `python tools/build_procedure_docs.py`. Authored explanations live in [editorial notes](../editorial-notes.md). Legal mappings await maintainer review.

The examiner may pause for further work, notifying the authority and Secretary
of State of the matters and period. The period cannot begin before notification
and cannot exceed the prescribed six months. The authority responds before expiry
and publishes its response. At the end, withdrawal requires the examiner's conclusion
that unresolved matters leave no prospect of a sound plan; otherwise examination
resumes. Months and actual before-expiry delivery are reviewed inputs, not fixed-day
approximations.

**Who is involved:** Examining Inspector; Local planning authority; Secretary of State

**Stage inputs:** Notice of examination pause and required work

**Stage outputs:** Pause response, modifications and further evidence

Stage inputs/outputs are an indicative map; the individual rules below determine which selected document duties are conditional.

## Assertions at this stage

| Assertion | Status | Evaluator operation |
| --- | --- | --- |
| [Notify the LPA and Secretary of State of the pause, required work and period.](#new-pause-notice) | Statutory assertion | Supplied observations only |
| [A statutory examination pause cannot exceed six months or begin before notification.](#new-pause-maximum) | Statutory assertion | Date arithmetic + supplied observations |
| [Before pause expiry send the work-response document, proposed modifications or statement of none, and further soundness evidence; publish them.](#new-pause-response) | Statutory assertion | Supplied observations only |
| [Recommend withdrawal with reasons if outstanding notified matters leave no prospect of a sound plan at pause end.](#new-pause-withdrawal) | Statutory assertion | Supplied observations only |
| [Resume examination unless withdrawal is recommended under the pause provision.](#new-pause-resumption) | Statutory assertion | Supplied observations only |

<a id="new-pause-notice"></a>

## Notify the LPA and Secretary of State of the pause, required work and period.

**Statutory assertion · responsible actor: Examining Inspector**

Rule [`new.pause_notice`](../../../knowledge/procedures/model.json#L6092); version 0.1.0.

### Source to inspect

- [s 15DA(2)](https://www.legislation.gov.uk/ukpga/2004/5/section/15DA) — PCPA 2004 section 15DA; revised text retrieved 2026-10-29 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: The examiner notified the authority and Secretary of State of the decision to pause, the matters requiring work and the pause period under PCPA section 15DA(2) ([input `pause_notice_recorded`](../facts.md#pause-notice-recorded)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`pause_notice_recorded`](../facts.md#pause-notice-recorded) | The examiner notified the authority and Secretary of State of the decision to pause, the matters requiring work and the pause period under PCPA section 15DA(2). | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-pause-maximum"></a>

## A statutory examination pause cannot exceed six months or begin before notification.

**Statutory assertion · responsible actor: Examining Inspector**

Rule [`new.pause_maximum`](../../../knowledge/procedures/model.json#L6133); version 0.1.0.

### Source to inspect

- [s 15DA(3)](https://www.legislation.gov.uk/ukpga/2004/5/section/15DA) — PCPA 2004 section 15DA; revised text retrieved 2026-10-29 (legal basis)
- [reg 36(1)](https://www.legislation.gov.uk/uksi/2026/186/regulation/36/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Every** condition below:
  - **Yes** to: Reviewer confirms the pause period is within six calendar months ([input `pause_within_six_calendar_months`](../facts.md#pause-within-six-calendar-months)).
  - [Pause commencement date](../facts.md#pause-begins) is on or after [Pause notification date](../facts.md#pause-notified).

**Timing:** pause commencement → pause end; s 15DA(3) and reg 36(1); month arithmetic requires review.

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`pause_begins`](../facts.md#pause-begins) | Calendar date on which the notified examination pause begins. | Recorded observation; date |
| [`pause_notified`](../facts.md#pause-notified) | Calendar date on which the examiner gave the authority the section 15DA(2) notice. | Recorded observation; date |
| [`pause_within_six_calendar_months`](../facts.md#pause-within-six-calendar-months) | The reviewer has checked the notified pause period against the six-calendar-month maximum in section 15DA(3) and regulation 36(1). The evaluator does not approximate months as a fixed number of days. | Reviewer judgement; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- [Six-month statutory pause maximum is distinct from examination target.](../worked-examples.md#new-pause-limit)

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-pause-response"></a>

## Before pause expiry send the work-response document, proposed modifications or statement of none, and further soundness evidence; publish them.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.pause_response`](../../../knowledge/procedures/model.json#L6195); version 0.1.0.

### Source to inspect

- [s 15DA(5)-(7)](https://www.legislation.gov.uk/ukpga/2004/5/section/15DA) — PCPA 2004 section 15DA; revised text retrieved 2026-10-29 (legal basis)
- [reg 36(3)-(4)](https://www.legislation.gov.uk/uksi/2026/186/regulation/36/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Every** condition below:
  - **Yes** to: Pause response has the required contents ([input `pause_response_contents_recorded`](../facts.md#pause-response-contents-recorded)).
  - **Yes** to: Reviewer confirms delivery before the actual pause expiry ([input `pause_response_before_expiry`](../facts.md#pause-response-before-expiry)).
  - **Yes** to: Pause response publication and notifications completed as required ([input `pause_response_published`](../facts.md#pause-response-published)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`pause_response_before_expiry`](../facts.md#pause-response-before-expiry) | Reviewer establishes delivery before the end of the notified pause period, using the notice and actual delivery/receipt evidence. Calendar dates alone do not decide a same-day case. | Reviewer judgement; boolean |
| [`pause_response_contents_recorded`](../facts.md#pause-response-contents-recorded) | The response states what work the authority undertook, sets out proposed modifications or states that none are proposed, and supplies any further soundness evidence the authority has under section 15DA(6). | Recorded observation; boolean |
| [`pause_response_published`](../facts.md#pause-response-published) | Publication, reg 88 availability and required reg 36(4) notifications recorded, including their timing under reg 36(3)-(4). | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

The response-date and expiry-date facts alone cannot decide a same-day delivery
question. The predicate requires an expressly reviewed before-expiry finding,
plus reviewed contents and publication. The source's response deadline and the
subsequent publication timing are different requirements; the bundled observations
must preserve that distinction in their evidence.

Before-expiry timing needs evidenced review of the actual period and delivery. Same-day dates alone give unknown, not a breach. Publication is as soon as reasonably practicable afterwards under reg 36(3), with same-day availability and notifications under (4).


**Examples selecting this assertion:**

- [Same-day dates do not establish breach or compliance before actual pause expiry.](../worked-examples.md#pause-response-date-only)
- [Delivery timing is resolved by evidence reviewed against the actual notified period.](../../../knowledge/procedures/examples.json#L1847)

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-pause-withdrawal"></a>

## Recommend withdrawal with reasons if outstanding notified matters leave no prospect of a sound plan at pause end.

**Statutory assertion · responsible actor: Examining Inspector**

Rule [`new.pause_withdrawal`](../../../knowledge/procedures/model.json#L6256); version 0.1.0.

### Source to inspect

- [s 15DA(8)](https://www.legislation.gov.uk/ukpga/2004/5/section/15DA) — PCPA 2004 section 15DA; revised text retrieved 2026-10-29 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- **Every** condition below:
  - **Yes** to: The notified pause period has ended, so the post-pause decision condition is being assessed ([input `pause_ended`](../facts.md#pause-ended)).
  - **Yes** to: At pause end, the examiner considers that the notified matters have not been dealt with and consequently there is no prospect of a sound plan under section 15DA(8) ([input `unresolved_matters_no_soundness_prospect`](../facts.md#unresolved-matters-no-soundness-prospect)).

### What the evaluator actually requires

- **Yes** to: The examiner recommended withdrawal and gave reasons under the applicable new-system withdrawal condition ([input `withdrawal_recommended_with_reasons`](../facts.md#withdrawal-recommended-with-reasons)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`pause_ended`](../facts.md#pause-ended) | The notified pause period has ended, so the post-pause decision condition is being assessed. | Recorded observation; boolean |
| [`unresolved_matters_no_soundness_prospect`](../facts.md#unresolved-matters-no-soundness-prospect) | At pause end, the examiner considers that the notified matters have not been dealt with and consequently there is no prospect of a sound plan under section 15DA(8). Unfinished work alone does not establish this compound judgement. | Reviewer judgement; boolean |
| [`withdrawal_recommended_with_reasons`](../facts.md#withdrawal-recommended-with-reasons) | The examiner recommended withdrawal and gave reasons under the applicable new-system withdrawal condition. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- [Unknown soundness prospect prevents a withdrawal conclusion merely because some matters remain.](../../../knowledge/procedures/examples.json#L1611)

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-pause-resumption"></a>

## Resume examination unless withdrawal is recommended under the pause provision.

**Statutory assertion · responsible actor: Examining Inspector**

Rule [`new.pause_resumption`](../../../knowledge/procedures/model.json#L6308); version 0.1.0.

### Source to inspect

- [s 15DA(9)](https://www.legislation.gov.uk/ukpga/2004/5/section/15DA) — PCPA 2004 section 15DA; revised text retrieved 2026-10-29 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- **Every** condition below:
  - **Yes** to: The notified pause period has ended, so the post-pause decision condition is being assessed ([input `pause_ended`](../facts.md#pause-ended)).
  - **No** to: The examiner made a withdrawal recommendation under section 15DA(8), determining whether section 15DA(9) requires resumption ([input `withdrawal_under_15da8`](../facts.md#withdrawal-under-15da8)).

### What the evaluator actually requires

- **Yes** to: The examination resumed at the end of the pause where no section 15DA(8) withdrawal recommendation was made ([input `examination_resumed`](../facts.md#examination-resumed)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`examination_resumed`](../facts.md#examination-resumed) | The examination resumed at the end of the pause where no section 15DA(8) withdrawal recommendation was made. | Recorded observation; boolean |
| [`pause_ended`](../facts.md#pause-ended) | The notified pause period has ended, so the post-pause decision condition is being assessed. | Recorded observation; boolean |
| [`withdrawal_under_15da8`](../facts.md#withdrawal-under-15da8) | The examiner made a withdrawal recommendation under section 15DA(8), determining whether section 15DA(9) requires resumption. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

## Connections to other stages

- [Independent examination and hearings](new-examination.md) → [Statutory examination pause](new-pause.md): Examiner decides matters may be resolved through further work. (discretion).
- [Statutory examination pause](new-pause.md) → [Independent examination and hearings](new-examination.md): No s 15DA(8) withdrawal recommendation at pause end. (decision).

These relationships are descriptive. They are not executable workflow guards.
