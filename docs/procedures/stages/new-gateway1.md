# Gateway 1: LPA self-assessment

[Review guide](../README.md) · [Input definitions](../facts.md) · [Worked examples](../worked-examples.md)

Generated from model 0.1.0, knowledge date 2026-10-29. Rebuild with `python tools/build_procedure_docs.py`. Authored explanations live in [editorial notes](../editorial-notes.md). Legal mappings await maintainer review.

Gateway 1 is the authority's self-assessment of readiness. It covers programme,
governance, engagement, anticipated plan content and relevant SEA obligations.
The authority publishes it only after both the statutory four-month notice period
and the scoping deadline permit. The evaluator calculates the day-after-scoping
comparison but asks a reviewer to resolve the calendar-month condition. Publication
of the scoping summary is a further, later act.

**Who is involved:** Local planning authority

**Stage inputs:** Local plan timetable; Scoping consultation notice

**Stage outputs:** Gateway 1 self-assessment summary; Summary of scoping consultation

Stage inputs/outputs are an indicative map; the individual rules below determine which selected document duties are conditional.

## Assertions at this stage

| Assertion | Status | Evaluator operation |
| --- | --- | --- |
| [Publish an LPA self-assessment covering timetable, governance, engagement, anticipated content and SEA obligations.](#new-gateway1-summary) | Statutory assertion | Supplied observations only |
| [Publish self-assessment no earlier than the later of the first day after the four-month notice period and the day after the scoping deadline.](#new-gateway1-timing) | Statutory assertion | Date arithmetic + supplied observations |
| [Publish scoping summary no earlier than the day after gateway 1 publication.](#new-scoping-summary) | Statutory assertion | Date arithmetic + supplied observations |

<a id="new-gateway1-summary"></a>

## Publish an LPA self-assessment covering timetable, governance, engagement, anticipated content and SEA obligations.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.gateway1_summary`](../../../knowledge/procedures/model.json#L3049); version 0.1.0.

### Source to inspect

- [reg 21(1)-(2)](https://www.legislation.gov.uk/uksi/2026/186/regulation/21/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: The LPA self-assessment summary addresses timetable compliance, project management/governance, consultation/engagement, anticipated plan content and relevant SEA obligations under regulation 21(2) ([input `gateway1_contents_recorded`](../facts.md#gateway1-contents-recorded)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`gateway1_contents_recorded`](../facts.md#gateway1-contents-recorded) | The LPA self-assessment summary addresses timetable compliance, project management/governance, consultation/engagement, anticipated plan content and relevant SEA obligations under regulation 21(2). | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

Self-assessment, not assessor approval or a soundness determination.


**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-gateway1-timing"></a>

## Publish self-assessment no earlier than the later of the first day after the four-month notice period and the day after the scoping deadline.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.gateway1_timing`](../../../knowledge/procedures/model.json#L3090); version 0.1.0.

### Source to inspect

- [reg 21(3)](https://www.legislation.gov.uk/uksi/2026/186/regulation/21/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Every** condition below:
  - **Yes** to: The reviewer has checked that gateway 1 publication is no earlier than the first day after the four-month period beginning with notice-of-intention publication ([input `four_calendar_month_notice_period_elapsed`](../facts.md#four-calendar-month-notice-period-elapsed)).
  - [Calendar date on which the LPA made its gateway 1 self-assessment summary available](../facts.md#gateway1-published) is at least the next calendar day after [Calendar deadline stated for representations in the regulation 20 scoping consultation](../facts.md#scoping-deadline).

**Timing:** notice of intention made available → gateway 1 publication; first day after statutory four-month period; also after scoping deadline. Month arithmetic deliberately not automated..

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`four_calendar_month_notice_period_elapsed`](../facts.md#four-calendar-month-notice-period-elapsed) | The reviewer has checked that gateway 1 publication is no earlier than the first day after the four-month period beginning with notice-of-intention publication. Calendar-month arithmetic is supplied as a reviewed conclusion. | Reviewer judgement; boolean |
| [`gateway1_published`](../facts.md#gateway1-published) | Calendar date on which the LPA made its gateway 1 self-assessment summary available. | Recorded observation; date |
| [`scoping_deadline`](../facts.md#scoping-deadline) | Calendar deadline stated for representations in the regulation 20 scoping consultation. | Recorded observation; date |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

- Recorded exception: Rollout Schedule imposes additional latest dates depending on authority and existing plan history.

**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-scoping-summary"></a>

## Publish scoping summary no earlier than the day after gateway 1 publication.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.scoping_summary`](../../../knowledge/procedures/model.json#L3149); version 0.1.0.

### Source to inspect

- [reg 22](https://www.legislation.gov.uk/uksi/2026/186/regulation/22/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Every** condition below:
  - **Yes** to: The scoping summary records the prescribed consultation activity, main issues and their treatment, or the absence of representations, under regulation 22 ([input `scoping_summary_contents_recorded`](../facts.md#scoping-summary-contents-recorded)).
  - [Calendar date on which the regulation 22 scoping consultation summary was made available](../facts.md#scoping-summary-published) is at least the next calendar day after [Calendar date on which the LPA made its gateway 1 self-assessment summary available](../facts.md#gateway1-published).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`gateway1_published`](../facts.md#gateway1-published) | Calendar date on which the LPA made its gateway 1 self-assessment summary available. | Recorded observation; date |
| [`scoping_summary_contents_recorded`](../facts.md#scoping-summary-contents-recorded) | The scoping summary records the prescribed consultation activity, main issues and their treatment, or the absence of representations, under regulation 22. | Recorded observation; boolean |
| [`scoping_summary_published`](../facts.md#scoping-summary-published) | Calendar date on which the regulation 22 scoping consultation summary was made available. | Recorded observation; date |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

## Connections to other stages

- [Scoping consultation](new-scoping.md) → [Gateway 1: LPA self-assessment](new-gateway1.md): Satisfy the cited timing and evidence requirements; see stage rules. (sequence).
- [Gateway 1: LPA self-assessment](new-gateway1.md) → [Content and evidence consultation](new-content.md): Satisfy the cited timing and evidence requirements; see stage rules. (sequence).

These relationships are descriptive. They are not executable workflow guards.
