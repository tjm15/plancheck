# Adoption and publication

[Review guide](../README.md) · [Input definitions](../facts.md) · [Worked examples](../worked-examples.md)

Generated from model 0.1.0, knowledge date 2026-10-29. Rebuild with `python tools/build_procedure_docs.py`. Authored explanations live in [editorial notes](../editorial-notes.md). Legal mappings await maintainer review.

The authority adopts by resolution in accordance with PCPA section 15EA and the
Inspector's recommendation, including required modifications and the statutory
limit on additional changes. Publication of the adopted plan and adoption statement
then follows regulation 39. Compliance of adopted content is supplied as an
attributable judgement, rather than inferred from a resolution's existence.

**Who is involved:** Local planning authority

**Stage inputs:** Final recommendations and reasons

**Stage outputs:** Proposed Local Plan; Adoption statement

Stage inputs/outputs are an indicative map; the individual rules below determine which selected document duties are conditional.

## Assertions at this stage

| Assertion | Status | Evaluator operation |
| --- | --- | --- |
| [Adopt by resolution only in accordance with the Inspector’s recommendation, including required modifications; additional changes must not materially affect content.](#new-adoption-conditions) | Statutory assertion | Supplied observations only |
| [Publish the adopted plan and adoption statement and send the statement to requesters as soon as reasonably practicable.](#new-adoption-publication) | Statutory assertion | Supplied observations only |

<a id="new-adoption-conditions"></a>

## Adopt by resolution only in accordance with the Inspector’s recommendation, including required modifications; additional changes must not materially affect content.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.adoption_conditions`](../../../knowledge/procedures/model.json#L6515); version 0.1.0.

### Source to inspect

- [s 15EA(1)-(2),(5)-(6)](https://www.legislation.gov.uk/ukpga/2004/5/section/15EA) — PCPA 2004 section 15EA; revised text retrieved 2026-10-29 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: Adoption is by resolution in accordance with PCPA section 15EA, includes the required recommended modifications and contains only permitted additional changes that do not materially affect content ([input `adoption_conforms_to_recommendation`](../facts.md#adoption-conforms-to-recommendation)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`adoption_conforms_to_recommendation`](../facts.md#adoption-conforms-to-recommendation) | Adoption is by resolution in accordance with PCPA section 15EA, includes the required recommended modifications and contains only permitted additional changes that do not materially affect content. The reviewer supplies this legal/content judgement. | Reviewer judgement; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

Recommendation to adopt is not itself adoption and does not compel the authority to adopt.


**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-adoption-publication"></a>

## Publish the adopted plan and adoption statement and send the statement to requesters as soon as reasonably practicable.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.adoption_publication`](../../../knowledge/procedures/model.json#L6557); version 0.1.0.

### Source to inspect

- [reg 39](https://www.legislation.gov.uk/uksi/2026/186/regulation/39/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: The adopted plan and adoption statement were made available and required copies/notifications provided under regulation 39 as soon as reasonably practicable ([input `new_adoption_publicity_recorded`](../facts.md#new-adoption-publicity-recorded)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`new_adoption_publicity_recorded`](../facts.md#new-adoption-publicity-recorded) | The adopted plan and adoption statement were made available and required copies/notifications provided under regulation 39 as soon as reasonably practicable. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

## Connections to other stages

- [QA, fact check and final report](new-reporting.md) → [Adoption and publication](new-adoption.md): Authority chooses adoption consistent with recommendation. (decision).

These relationships are descriptive. They are not executable workflow guards.
