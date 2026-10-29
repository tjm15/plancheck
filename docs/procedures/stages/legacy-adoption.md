# Adoption and publication

[Review guide](../README.md) · [Input definitions](../facts.md) · [Worked examples](../worked-examples.md)

Generated from model 0.1.0, knowledge date 2026-10-29. Rebuild with `python tools/build_procedure_docs.py`. Authored explanations live in [editorial notes](../editorial-notes.md). Legal mappings await maintainer review.

The authority's resolution and adopted content must fall within saved PCPA
section 23. Adoption as recommended and adoption with required main modifications
are distinct statutory routes, with limits on additional modifications. Regulation
26 then governs publication and notices. The Inspector's recommendation and the
authority's adoption resolution are separate acts; one does not prove the other.

**Who is involved:** Local planning authority

**Stage inputs:** Final recommendations and reasons

**Stage outputs:** Proposed Local Plan; Adoption statement

Stage inputs/outputs are an indicative map; the individual rules below determine which selected document duties are conditional.

## Assertions at this stage

| Assertion | Status | Evaluator operation |
| --- | --- | --- |
| [Publish the adopted plan, adoption statement and SA report; send the statement to requesters and the Secretary of State.](#legacy-adoption-publication) | Statutory assertion | Supplied observations only |
| [Adopt by resolution only within saved section 23, including required main modifications and the limit on additional modifications.](#legacy-adoption-conditions) | Statutory assertion | Supplied observations only |

<a id="legacy-adoption-publication"></a>

## Publish the adopted plan, adoption statement and SA report; send the statement to requesters and the Secretary of State.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`legacy.adoption_publication`](../../../knowledge/procedures/model.json#L2829); version 0.1.0.

### Source to inspect

- [reg 26](https://www.legislation.gov.uk/uksi/2012/767/regulation/26) — Town and Country Planning (Local Planning) (England) Regulations 2012, SI 2012/767; revised Part 6 retrieved 2026-10-29; pre-2026 text as saved (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: The adopted legacy plan, adoption statement and sustainability appraisal report were made available, requesters notified and the adoption statement sent to the Secretary of State under regulation 26 ([input `legacy_adoption_publication_recorded`](../facts.md#legacy-adoption-publication-recorded)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`legacy_adoption_publication_recorded`](../facts.md#legacy-adoption-publication-recorded) | The adopted legacy plan, adoption statement and sustainability appraisal report were made available, requesters notified and the adoption statement sent to the Secretary of State under regulation 26. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="legacy-adoption-conditions"></a>

## Adopt by resolution only within saved section 23, including required main modifications and the limit on additional modifications.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`legacy.adoption_conditions`](../../../knowledge/procedures/model.json#L6755); version 0.1.0.

### Source to inspect

- [s 23(2)-(5)](https://www.legislation.gov.uk/ukpga/2004/5/section/23/2026-03-24) — PCPA 2004 section 23 immediately before commencement; point in time 2026-03-24, read with SI 2026/169 Sch 1 (legal basis)
- [Sch 1 paras 2,4(6)](https://www.legislation.gov.uk/uksi/2026/169/schedule/1) — LURA 2023 Commencement No. 11 and Saving and Transitional Provisions Regulations 2026, SI 2026/169; revised Schedule 1 including SI 2026/333 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: Reviewer confirms adoption complies with saved section 23 ([input `legacy_adoption_conditions_met`](../facts.md#legacy-adoption-conditions-met)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`legacy_adoption_conditions_met`](../facts.md#legacy-adoption-conditions-met) | Adoption is by resolution within saved s 23(2)-(5): as recommended, or with all recommended main modifications; additional modifications together do not materially affect the applicable policies. | Reviewer judgement; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- [Legacy statutory non-adoption can coexist with recommended curative modifications and a permitted adoption route.](../worked-examples.md#legacy-non-adoption-with-curative-modifications)

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

## Connections to other stages

- [QA, fact check and final report](legacy-reporting.md) → [Adoption and publication](legacy-adoption.md): Authority chooses adoption permitted by saved s 23, with required main modifications and only permitted additional changes. (decision).

These relationships are descriptive. They are not executable workflow guards.
