# Withdrawal publication

[Review guide](../README.md) · [Input definitions](../facts.md) · [Worked examples](../worked-examples.md)

Generated from model 0.1.0, knowledge date 2026-10-29. Rebuild with `python tools/build_procedure_docs.py`. Authored explanations live in [editorial notes](../editorial-notes.md). Legal mappings await maintainer review.

Regulation 38 requires withdrawal publicity, notifications and specified changes
to document availability while retaining the withdrawal statement and timetable.
This stage describes those consequences. It is not a complete account of all
withdrawal powers, directions or routes into withdrawal.

**Who is involved:** Local planning authority

**Stage inputs:** Attributed professional decision record

**Stage outputs:** Withdrawal statement

Stage inputs/outputs are an indicative map; the individual rules below determine which selected document duties are conditional.

## Assertions at this stage

| Assertion | Status | Evaluator operation |
| --- | --- | --- |
| [Publish withdrawal, notify invited consultation participants and cease specified availability, retaining the withdrawal statement and timetable.](#new-withdrawal-publication) | Statutory assertion | Supplied observations only |

<a id="new-withdrawal-publication"></a>

## Publish withdrawal, notify invited consultation participants and cease specified availability, retaining the withdrawal statement and timetable.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.withdrawal_publication`](../../../knowledge/procedures/model.json#L6599); version 0.1.0.

### Source to inspect

- [reg 38](https://www.legislation.gov.uk/uksi/2026/186/regulation/38/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: The authority made the regulation 38 withdrawal statement available, notified the required consultation participants and ceased the specified availability while retaining the timetable and withdrawal statement ([input `new_withdrawal_publicity_recorded`](../facts.md#new-withdrawal-publicity-recorded)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`new_withdrawal_publicity_recorded`](../facts.md#new-withdrawal-publicity-recorded) | The authority made the regulation 38 withdrawal statement available, notified the required consultation participants and ceased the specified availability while retaining the timetable and withdrawal statement. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

Public availability rule; does not instruct deletion of internal evidence or history.


**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

## Connections to other stages


These relationships are descriptive. They are not executable workflow guards.
