# Consultation on proposed Local Plan

[Review guide](../README.md) · [Input definitions](../facts.md) · [Worked examples](../worked-examples.md)

Generated from model 0.1.0, knowledge date 2026-10-29. Rebuild with `python tools/build_procedure_docs.py`. Authored explanations live in [editorial notes](../editorial-notes.md). Legal mappings await maintainer review.

After gateway 2 advice is published, the authority consults on its proposed plan
and prescribed supporting material for at least eight weeks. It must have regard
to gateway advice and consultation responses; that is not automatically obedience
to every recommendation. An operative spatial development strategy and qualifying
supplementary plans introduce additional conditional steps. The consultation
summary must follow the representation deadline.

**Who is involved:** Local planning authority; Representors and public; General and specific consultation bodies; Authority responsible for operative spatial development strategy

**Stage inputs:** Gateway 2 observations and advice; Proposed Local Plan; Proposed or submission policies map

**Stage outputs:** Proposed-plan consultation notice; Proposed-plan consultation summary

Stage inputs/outputs are an indicative map; the individual rules below determine which selected document duties are conditional.

## Assertions at this stage

| Assertion | Status | Evaluator operation |
| --- | --- | --- |
| [Have regard to gateway observations/advice and consultation responses while preparing the plan.](#new-gateway-advice-regard) | Statutory assertion | Supplied observations only |
| [Publish proposed-plan submission documents and consultation notices, and invite required classes, no earlier than the day after gateway 2 advice publication.](#new-plan-sequence) | Statutory assertion | Date arithmetic + supplied observations |
| [Allow at least eight weeks for proposed-plan representations from notice publication.](#new-plan-minimum) | Statutory assertion | Date arithmetic + supplied observations |
| [On the proposed-plan publication day, notify and invite conformity representations from the operative SDS authority.](#new-sds-consultation) | Statutory assertion | Supplied observations only |
| [Publish the supplementary plans statement on the same day as the proposed-plan documents where qualifying supplementary plans are in effect.](#new-supplementary-statement) | Statutory assertion | Supplied observations only |
| [Publish a proposed-plan consultation summary no earlier than the day after the representations deadline.](#new-plan-summary) | Statutory assertion | Date arithmetic + supplied observations |

<a id="new-gateway-advice-regard"></a>

## Have regard to gateway observations/advice and consultation responses while preparing the plan.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.gateway_advice_regard`](../../../knowledge/procedures/model.json#L3792); version 0.1.0.

### Source to inspect

- [s 15CA(6)(a)-(b)](https://www.legislation.gov.uk/ukpga/2004/5/section/15CA) — PCPA 2004 section 15CA; revised text retrieved 2026-10-29 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: The authority has had regard to gateway observations/advice and consultation representations when preparing the plan under PCPA section 15CA(6)(a)-(b) ([input `gateway_advice_and_responses_considered`](../facts.md#gateway-advice-and-responses-considered)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`gateway_advice_and_responses_considered`](../facts.md#gateway-advice-and-responses-considered) | The authority has had regard to gateway observations/advice and consultation representations when preparing the plan under PCPA section 15CA(6)(a)-(b). It need not accept every recommendation. | Reviewer judgement; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

A legal duty to have regard is not a duty to accept every recommendation.


**Examples selecting this assertion:**

- [Recorded consideration can satisfy the regard assertion without a claim all advice was accepted.](../../../knowledge/procedures/examples.json#L1648)

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-plan-sequence"></a>

## Publish proposed-plan submission documents and consultation notices, and invite required classes, no earlier than the day after gateway 2 advice publication.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.plan_sequence`](../../../knowledge/procedures/model.json#L3834); version 0.1.0.

### Source to inspect

- [reg 27(1)-(2)](https://www.legislation.gov.uk/uksi/2026/186/regulation/27/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Every** condition below:
  - **Yes** to: The proposed-plan consultation pack and notice required by regulation 27 were made available and appropriate consultation bodies invited ([input `new_plan_publication_and_invitations_recorded`](../facts.md#new-plan-publication-and-invitations-recorded)).
  - [Selected consultation: publication date](../facts.md#consultation-published) is at least the next calendar day after [Calendar date on which the authority published its gateway 2 observations and advice](../facts.md#gateway2-advice-published).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`consultation_published`](../facts.md#consultation-published) | Calendar date of the publication that starts the selected consultation period. In a legacy case this is publication of the statement of representations procedure; in a new-system case it is the relevant content/evidence or proposed-plan notice. Use a separate case for each consultation. | Recorded observation; date |
| [`gateway2_advice_published`](../facts.md#gateway2-advice-published) | Calendar date on which the authority published its gateway 2 observations and advice. | Recorded observation; date |
| [`new_plan_publication_and_invitations_recorded`](../facts.md#new-plan-publication-and-invitations-recorded) | The proposed-plan consultation pack and notice required by regulation 27 were made available and appropriate consultation bodies invited. The pack includes plan, policies map, evidence details, consultation statement and relevant supporting documents. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-plan-minimum"></a>

## Allow at least eight weeks for proposed-plan representations from notice publication.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.plan_minimum`](../../../knowledge/procedures/model.json#L3889); version 0.1.0.

### Source to inspect

- [reg 27(5), notice definition (b)](https://www.legislation.gov.uk/uksi/2026/186/regulation/27/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- [Selected consultation: representations deadline](../facts.md#consultation-deadline) is at least **56 calendar days** after [Selected consultation: publication date](../facts.md#consultation-published).

**Timing:** proposed-plan consultation notice publication → representations deadline; calendar days: 56.

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`consultation_deadline`](../facts.md#consultation-deadline) | Last calendar date stated for receipt of representations in the selected consultation. This field must refer to the same consultation as consultation_published. | Recorded observation; date |
| [`consultation_published`](../facts.md#consultation-published) | Calendar date of the publication that starts the selected consultation period. In a legacy case this is publication of the statement of representations procedure; in a new-system case it is the relevant content/evidence or proposed-plan notice. Use a separate case for each consultation. | Recorded observation; date |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- [Six-week legacy publication period is sufficient for the duration assertion.](../worked-examples.md#legacy-six-weeks)
- [Six weeks is insufficient at the new proposed-plan consultation.](../worked-examples.md#new-plan-six-weeks)
- [Exactly eight weeks meets the new proposed-plan minimum.](../../../knowledge/procedures/examples.json#L193)
- [One day short of eight weeks fails.](../../../knowledge/procedures/examples.json#L236)
- [Missing dates remain unknown.](../../../knowledge/procedures/examples.json#L279)

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-sds-consultation"></a>

## On the proposed-plan publication day, notify and invite conformity representations from the operative SDS authority.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.sds_consultation`](../../../knowledge/procedures/model.json#L3936); version 0.1.0.

### Source to inspect

- [reg 28](https://www.legislation.gov.uk/uksi/2026/186/regulation/28/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- **Yes** to: A spatial development strategy is operative in relation to the plan area so that the selected regulation 28 conformity/document requirements apply ([input `operative_sds`](../facts.md#operative-sds)).

### What the evaluator actually requires

- **Yes** to: On proposed-plan consultation publication day, the authority invited the operative spatial development strategy authority’s conformity representations as required by regulation 28 ([input `sds_invitation_same_day_recorded`](../facts.md#sds-invitation-same-day-recorded)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`operative_sds`](../facts.md#operative-sds) | A spatial development strategy is operative in relation to the plan area so that the selected regulation 28 conformity/document requirements apply. | Recorded observation; boolean |
| [`sds_invitation_same_day_recorded`](../facts.md#sds-invitation-same-day-recorded) | On proposed-plan consultation publication day, the authority invited the operative spatial development strategy authority’s conformity representations as required by regulation 28. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- [No operative SDS means the specific conformity-invitation rule does not activate.](../../../knowledge/procedures/examples.json#L1722)

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-supplementary-statement"></a>

## Publish the supplementary plans statement on the same day as the proposed-plan documents where qualifying supplementary plans are in effect.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.supplementary_statement`](../../../knowledge/procedures/model.json#L3978); version 0.1.0.

### Source to inspect

- [reg 29](https://www.legislation.gov.uk/uksi/2026/186/regulation/29/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- **Yes** to: Supplementary plans meeting the condition in regulation 29 are in effect, triggering its statement requirement ([input `qualifying_supplementary_plans`](../facts.md#qualifying-supplementary-plans)).

### What the evaluator actually requires

- **Yes** to: Where regulation 29 applies, the supplementary plans statement was made available on the same day as the proposed-plan consultation documents ([input `supplementary_statement_same_day_recorded`](../facts.md#supplementary-statement-same-day-recorded)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`qualifying_supplementary_plans`](../facts.md#qualifying-supplementary-plans) | Supplementary plans meeting the condition in regulation 29 are in effect, triggering its statement requirement. The legal trigger must be checked from the actual instruments. | Recorded observation; boolean |
| [`supplementary_statement_same_day_recorded`](../facts.md#supplementary-statement-same-day-recorded) | Where regulation 29 applies, the supplementary plans statement was made available on the same day as the proposed-plan consultation documents. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-plan-summary"></a>

## Publish a proposed-plan consultation summary no earlier than the day after the representations deadline.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.plan_summary`](../../../knowledge/procedures/model.json#L4020); version 0.1.0.

### Source to inspect

- [reg 30](https://www.legislation.gov.uk/uksi/2026/186/regulation/30/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Every** condition below:
  - **Yes** to: The regulation 30 proposed-plan consultation summary contains the prescribed consultation information and treatment of issues, including the required statement if no representations were received ([input `plan_summary_contents_recorded`](../facts.md#plan-summary-contents-recorded)).
  - [Calendar date on which the regulation 30 proposed-plan consultation summary was made available](../facts.md#plan-summary-published) is at least the next calendar day after [Selected consultation: representations deadline](../facts.md#consultation-deadline).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`consultation_deadline`](../facts.md#consultation-deadline) | Last calendar date stated for receipt of representations in the selected consultation. This field must refer to the same consultation as consultation_published. | Recorded observation; date |
| [`plan_summary_contents_recorded`](../facts.md#plan-summary-contents-recorded) | The regulation 30 proposed-plan consultation summary contains the prescribed consultation information and treatment of issues, including the required statement if no representations were received. | Recorded observation; boolean |
| [`plan_summary_published`](../facts.md#plan-summary-published) | Calendar date on which the regulation 30 proposed-plan consultation summary was made available. | Recorded observation; date |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

## Connections to other stages

- [Gateway 2: observations and advice](new-gateway2.md) → [Consultation on proposed Local Plan](new-publication.md): Satisfy the cited timing and evidence requirements; see stage rules. (sequence).
- [Consultation on proposed Local Plan](new-publication.md) → [Gateway 3: prescribed requirements](new-gateway3.md): Satisfy the cited timing and evidence requirements; see stage rules. (sequence).

These relationships are descriptive. They are not executable workflow guards.
