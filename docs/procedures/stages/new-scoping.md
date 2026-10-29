# Scoping consultation

[Review guide](../README.md) · [Input definitions](../facts.md) · [Worked examples](../worked-examples.md)

Generated from model 0.1.0, knowledge date 2026-10-29. Rebuild with `python tools/build_procedure_docs.py`. Authored explanations live in [editorial notes](../editorial-notes.md). Legal mappings await maintainer review.

Scoping invites representations on what the plan ought to contain. The scoping
notice cannot precede the notice of intention. There is no fixed six-week minimum
assigned to scoping in this model. The subsequent content/evidence and proposed-plan
consultations have their own minimum periods and different document packs.

**Who is involved:** Local planning authority; General and specific consultation bodies; Representors and public

**Stage inputs:** Notice of intention to commence

**Stage outputs:** Scoping consultation notice

Stage inputs/outputs are an indicative map; the individual rules below determine which selected document duties are conditional.

## Assertions at this stage

| Assertion | Status | Evaluator operation |
| --- | --- | --- |
| [Invite relevant consultation bodies and publish a scoping notice no earlier than the notice of intention.](#new-scoping) | Statutory assertion | Date arithmetic + supplied observations |

<a id="new-scoping"></a>

## Invite relevant consultation bodies and publish a scoping notice no earlier than the notice of intention.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.scoping`](../../../knowledge/procedures/model.json#L2997); version 0.1.0.

### Source to inspect

- [reg 20](https://www.legislation.gov.uk/uksi/2026/186/regulation/20/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Every** condition below:
  - **Yes** to: The regulation 20 scoping invitations and public notice identify the prescribed matters, representation arrangements and notification opportunities, and were addressed to the appropriate consultation classes ([input `scoping_invitations_and_notice_recorded`](../facts.md#scoping-invitations-and-notice-recorded)).
  - [Calendar date on which the regulation 20 scoping consultation notice was published](../facts.md#scoping-notice-date) is on or after [Calendar date on which the regulation 19 notice of intention was made available](../facts.md#notice-intention-date).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`notice_intention_date`](../facts.md#notice-intention-date) | Calendar date on which the regulation 19 notice of intention was made available. | Recorded observation; date |
| [`scoping_invitations_and_notice_recorded`](../facts.md#scoping-invitations-and-notice-recorded) | The regulation 20 scoping invitations and public notice identify the prescribed matters, representation arrangements and notification opportunities, and were addressed to the appropriate consultation classes. | Recorded observation; boolean |
| [`scoping_notice_date`](../facts.md#scoping-notice-date) | Calendar date on which the regulation 20 scoping consultation notice was published. | Recorded observation; date |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

Reg 20 does not itself prescribe a six-week minimum; do not copy reg 23 duration into this stage.


**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

## Connections to other stages

- [Timetable and notice of intention](new-timetable.md) → [Scoping consultation](new-scoping.md): Satisfy the cited timing and evidence requirements; see stage rules. (sequence).
- [Scoping consultation](new-scoping.md) → [Gateway 1: LPA self-assessment](new-gateway1.md): Satisfy the cited timing and evidence requirements; see stage rules. (sequence).

These relationships are descriptive. They are not executable workflow guards.
