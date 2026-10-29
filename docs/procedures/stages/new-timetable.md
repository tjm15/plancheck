# Timetable and notice of intention

[Review guide](../README.md) · [Input definitions](../facts.md) · [Worked examples](../worked-examples.md)

Generated from model 0.1.0, knowledge date 2026-10-29. Rebuild with `python tools/build_procedure_docs.py`. Authored explanations live in [editorial notes](../editorial-notes.md). Legal mappings await maintainer review.

The authority publishes and maintains a timetable and a notice of intention to
prepare the plan. The timetable check is currently a broad reviewer-supplied
conclusion covering selected regulations 4, 6 and 8, rather than separate automated
checks of each milestone and revision. The five-year replacement-plan rule concerns
an existing new-system plan after adoption/approval. Initial entry into the new
system has separate rollout provisions that are not executable here.

**Who is involved:** Local planning authority

**Stage inputs:** No document types listed.

**Stage outputs:** Local plan timetable; Notice of intention to commence

Stage inputs/outputs are an indicative map; the individual rules below determine which selected document duties are conditional.

## Assertions at this stage

| Assertion | Status | Evaluator operation |
| --- | --- | --- |
| [Publish and maintain the local plan timetable with anticipated and actual milestones.](#new-timetable) | Statutory assertion | Supplied observations only |
| [Prepare and publish notice of intention with prescribed authority, area, title, timetable and publication details.](#new-notice) | Statutory assertion | Supplied observations only |
| [Begin preparation of a replacement Local Plan, by reaching gateway 1, within the five-year period after adoption or approval of the existing new-system plan.](#new-begin-replacement) | Statutory assertion | Supplied observations only |

<a id="new-timetable"></a>

## Publish and maintain the local plan timetable with anticipated and actual milestones.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.timetable`](../../../knowledge/procedures/model.json#L2913); version 0.1.0.

### Source to inspect

- [regs 4,6,8](https://www.legislation.gov.uk/uksi/2026/186/made/data.html) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: The authority’s timetable content, initial publication and subsequent revisions comply with the selected duties in 2026 regulations 4, 6 and 8 ([input `timetable_requirements_met`](../facts.md#timetable-requirements-met)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`timetable_requirements_met`](../facts.md#timetable-requirements-met) | The authority’s timetable content, initial publication and subsequent revisions comply with the selected duties in 2026 regulations 4, 6 and 8. The reviewer supplies this overall finding; the evaluator does not inspect milestones or calculate monthly updates. | Reviewer judgement; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

The current predicate asks for the reviewer's overall timetable conclusion. It
does not implement the individual monthly updates or same-day milestone revisions.
The broad claim in the rule therefore exceeds what can be independently calculated
by the evaluator. Treat its result as an attributed review record.


**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-notice"></a>

## Prepare and publish notice of intention with prescribed authority, area, title, timetable and publication details.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.notice`](../../../knowledge/procedures/model.json#L2954); version 0.1.0.

### Source to inspect

- [reg 19](https://www.legislation.gov.uk/uksi/2026/186/regulation/19/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: The notice of intention has the regulation 19 content and has been published as required, including any applicable additional details ([input `notice_intention_requirements_met`](../facts.md#notice-intention-requirements-met)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`notice_intention_requirements_met`](../facts.md#notice-intention-requirements-met) | The notice of intention has the regulation 19 content and has been published as required, including any applicable additional details. This is a reviewed bundle, not a text extraction. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

- Recorded exception: Joint-plan partners and incorporation of minerals/waste content require additional notice details under reg 19(3)-(4).

**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-begin-replacement"></a>

## Begin preparation of a replacement Local Plan, by reaching gateway 1, within the five-year period after adoption or approval of the existing new-system plan.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.begin_replacement`](../../../knowledge/procedures/model.json#L6899); version 0.1.0.

### Source to inspect

- [reg 18(1)-(2)](https://www.legislation.gov.uk/uksi/2026/186/regulation/18/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- **Yes** to: An existing Local Plan has been adopted under s 15EA or approved under Part 2; the reg 18 replacement duty is being assessed ([input `existing_new_system_plan_adopted_or_approved`](../facts.md#existing-new-system-plan-adopted-or-approved)).

### What the evaluator actually requires

- **Yes** to: Reviewer verifies that replacement-plan gateway 1 was reached within five years beginning with the day after adoption/approval of the existing new-system plan, using reg 18 ([input `replacement_gateway1_within_five_years`](../facts.md#replacement-gateway1-within-five-years)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`existing_new_system_plan_adopted_or_approved`](../facts.md#existing-new-system-plan-adopted-or-approved) | An existing Local Plan has been adopted under s 15EA or approved under Part 2; the reg 18 replacement duty is being assessed. | Recorded observation; boolean |
| [`replacement_gateway1_within_five_years`](../facts.md#replacement-gateway1-within-five-years) | Reviewer verifies that replacement-plan gateway 1 was reached within five years beginning with the day after adoption/approval of the existing new-system plan, using reg 18. | Reviewer judgement; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

The five-year period is a different question from the initial rollout date for an
authority entering the 2026 system. It is currently resolved through a reviewer
observation; the evaluator does not calculate calendar years or identify the relevant
adoption/approval event from documents.

Calendar-year calculation requires evidenced review. This is distinct from the initial rollout Schedule for entering the new system.


**Examples selecting this assertion:**

- [No automatic five-year replacement compliance finding without the period assessment.](../../../knowledge/procedures/examples.json#L2118)

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

## Connections to other stages

- [Timetable and notice of intention](new-timetable.md) → [Scoping consultation](new-scoping.md): Satisfy the cited timing and evidence requirements; see stage rules. (sequence).

These relationships are descriptive. They are not executable workflow guards.
