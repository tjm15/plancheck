# Withdrawal publication

[Review guide](../README.md) · [Input definitions](../facts.md) · [Worked examples](../worked-examples.md)

Generated from model 0.1.0, knowledge date 2026-10-29. Rebuild with `python tools/build_procedure_docs.py`. Authored explanations live in [editorial notes](../editorial-notes.md). Legal mappings await maintainer review.

This stage records what must be published and notified following withdrawal,
and the specified cessation of document availability under regulation 27. It
does not model every circumstance in which withdrawal can occur or determine
that withdrawal is the correct substantive decision.

**Who is involved:** Local planning authority

**Stage inputs:** Attributed professional decision record

**Stage outputs:** Withdrawal statement

Stage inputs/outputs are an indicative map; the individual rules below determine which selected document duties are conditional.

## Assertions at this stage

| Assertion | Status | Evaluator operation |
| --- | --- | --- |
| [Publish withdrawal, notify the reg 22(3)(b) bodies, and cease the specified document availability.](#legacy-withdrawal-publication) | Statutory assertion | Supplied observations only |

<a id="legacy-withdrawal-publication"></a>

## Publish withdrawal, notify the reg 22(3)(b) bodies, and cease the specified document availability.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`legacy.withdrawal_publication`](../../../knowledge/procedures/model.json#L2872); version 0.1.0.

### Source to inspect

- [reg 27](https://www.legislation.gov.uk/uksi/2012/767/regulation/27) — Town and Country Planning (Local Planning) (England) Regulations 2012, SI 2012/767; revised Part 6 retrieved 2026-10-29; pre-2026 text as saved (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: The legacy withdrawal statement, notifications and cessation of specified document availability have been checked against regulation 27 ([input `legacy_withdrawal_publicity_recorded`](../facts.md#legacy-withdrawal-publicity-recorded)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`legacy_withdrawal_publicity_recorded`](../facts.md#legacy-withdrawal-publicity-recorded) | The legacy withdrawal statement, notifications and cessation of specified document availability have been checked against regulation 27. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

This is a statutory publication rule, not an instruction to delete internal evidence or repository history.


**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

## Connections to other stages


These relationships are descriptive. They are not executable workflow guards.
