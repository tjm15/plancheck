# Gateway 2: observations and advice

[Review guide](../README.md) · [Input definitions](../facts.md) · [Worked examples](../worked-examples.md)

Generated from model 0.1.0, knowledge date 2026-10-29. Rebuild with `python tools/build_procedure_docs.py`. Authored explanations live in [editorial notes](../editorial-notes.md). Legal mappings await maintainer review.

An appointed assessor provides observations and advice during preparation. The
authority must request that advice after the content/evidence summary and send
what it considers necessary on the request date. The legislation does not specify
a fixed draft-plan/map pack at this gateway. The guide recommends useful supporting
material, and those recommendations remain advisory. Separate rules cover the
indicative assessment duration and publication of advice and supplied material.

**Who is involved:** Local planning authority; Secretary of State appointed gateway assessor

**Stage inputs:** Content and evidence consultation summary; Supporting evidence selected by the authority

**Stage outputs:** Gateway 2 observations and advice

Stage inputs/outputs are an indicative map; the individual rules below determine which selected document duties are conditional.

## Assertions at this stage

| Assertion | Status | Evaluator operation |
| --- | --- | --- |
| [Seek gateway 2 observations and advice no earlier than the day after publication of the content and evidence summary.](#new-gateway2-sequence) | Statutory assertion | Date arithmetic + supplied observations |
| [Send the assessor, on the request date, documents or information the authority considers necessary for the prescribed observations and advice.](#new-gateway2-necessary-material) | Statutory assertion | Date arithmetic + supplied observations |
| [Provide emerging draft plan or relevant emerging policy detail where possible to assist gateway 2.](#new-gateway2-draft-plan) | Advisory guidance | Supplied observations only |
| [Provide an emerging policies map where possible to assist gateway 2.](#new-gateway2-draft-map) | Advisory guidance | Supplied observations only |
| [Provide Gateway 2 covering letter.](#new-gateway2-cover) | Advisory guidance | Supplied observations only |
| [Provide Draft statement of compliance.](#new-gateway2-compliance) | Advisory guidance | Supplied observations only |
| [Provide Draft statement of soundness.](#new-gateway2-soundness) | Advisory guidance | Supplied observations only |
| [Provide Evidence register with completion dates.](#new-gateway2-index) | Advisory guidance | Supplied observations only |
| [Aim to complete gateway 2 in four to six weeks.](#new-gateway2-target) | Service target | Supplied observations only |
| [Publish assessor advice as soon as reasonably practicable and simultaneously make submitted material available, notify requesters and send copies to persons identified in the advice.](#new-gateway2-publication) | Statutory assertion | Supplied observations only |

<a id="new-gateway2-sequence"></a>

## Seek gateway 2 observations and advice no earlier than the day after publication of the content and evidence summary.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.gateway2_sequence`](../../../knowledge/procedures/model.json#L3353); version 0.1.0.

### Source to inspect

- [reg 26(1)-(2)](https://www.legislation.gov.uk/uksi/2026/186/regulation/26/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- [Gateway 2 request date](../facts.md#gateway2-requested) is at least the next calendar day after [Content/evidence summary publication date](../facts.md#content-summary-published).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`content_summary_published`](../facts.md#content-summary-published) | Calendar date on which the regulation 24 content/evidence consultation summary was made available. | Recorded observation; date |
| [`gateway2_requested`](../facts.md#gateway2-requested) | Calendar date on which the authority sought gateway 2 observations and advice under regulation 26. | Recorded observation; date |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- [Gateway 2 request must follow summary publication by at least one calendar day.](../../../knowledge/procedures/examples.json#L1525)
- [Following-day gateway 2 request meets the sequence assertion.](../../../knowledge/procedures/examples.json#L1568)

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-gateway2-necessary-material"></a>

## Send the assessor, on the request date, documents or information the authority considers necessary for the prescribed observations and advice.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.gateway2_necessary_material`](../../../knowledge/procedures/model.json#L3393); version 0.1.0.

### Source to inspect

- [reg 26(3)](https://www.legislation.gov.uk/uksi/2026/186/regulation/26/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Every** condition below:
  - **Yes** to: Material the authority considers necessary for gateway 2 has been supplied ([input `gateway2_necessary_material_sent`](../facts.md#gateway2-necessary-material-sent)).
  - [Gateway 2 request date](../facts.md#gateway2-requested) and [Gateway 2 material transmission date](../facts.md#gateway2-material-sent) are **the same calendar date**.

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`gateway2_material_sent`](../facts.md#gateway2-material-sent) | Calendar date on which the authority sent the material it considered necessary for gateway 2 advice. | Recorded observation; date |
| [`gateway2_necessary_material_sent`](../facts.md#gateway2-necessary-material-sent) | Authority records what it considers necessary for reg 26(2) advice and supplies that material. Lack of an emerging draft plan/map alone does not falsify this judgement. | Reviewer judgement; boolean |
| [`gateway2_requested`](../facts.md#gateway2-requested) | Calendar date on which the authority sought gateway 2 observations and advice under regulation 26. | Recorded observation; date |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

Read regulation 26(3): it fixes the **authority's judgement of necessity** and
**same-day transmission**, not a named mandatory draft-plan/map pair. The predicate
therefore combines one reviewed necessity/supply observation with equality of two
calendar dates. A false necessity observation can fail the assertion; an absent
recommended draft plan cannot substitute for that observation. Review what the
authority actually considered necessary and what was sent.

Discretion concerns what is necessary; this is a duty, not an unrestricted option to supply nothing.


**Examples selecting this assertion:**

- [Absent draft plan/map are advisory gaps; necessary-material duty can still be met.](../worked-examples.md#gateway2-no-draft-plan)
- [Discretion on document selection does not remove the statutory supply duty.](../../../knowledge/procedures/examples.json#L381)

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-gateway2-draft-plan"></a>

## Provide emerging draft plan or relevant emerging policy detail where possible to assist gateway 2.

**Advisory guidance · responsible actor: Local planning authority**

Rule [`new.gateway2_draft_plan`](../../../knowledge/procedures/model.json#L3451); version 0.1.0.

### Source to inspect

- [3.6.9-3.6.11](https://www.gov.uk/guidance/procedural-guide-for-examinations-and-gateways-under-the-town-and-country-planning-local-planning-england-regulations-2026) — Procedural guide for Examinations and Gateways under the 2026 Regulations; first edition; updated 2026-08-26 (guidance)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: Emerging draft plan or relevant policy detail supplied at gateway 2 ([input `new_gateway2_plan_provided`](../facts.md#new-gateway2-plan-provided)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`new_gateway2_plan_provided`](../facts.md#new-gateway2-plan-provided) | An emerging draft plan or relevant emerging policy detail is supplied to assist gateway 2, as recommended by the procedure guide. This observation concerns gateway 2 supporting material, not the gateway 3 or examination submission packs. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `advisory_gap`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

The advisory-gap output answers whether the recommended emerging detail was supplied.
It does not answer whether the authority complied with regulation 26(3). To audit
the legal duty, inspect the separate necessary-material rule and evidence. The guide
allows useful policy detail without requiring a full emerging draft plan.

Recommended supporting material; absence alone does not establish breach of reg 26(3).


**Examples selecting this assertion:**

- [Absent draft plan/map are advisory gaps; necessary-material duty can still be met.](../worked-examples.md#gateway2-no-draft-plan)
- [Current guidance edition is not asserted to have applied before publication.](../../../knowledge/procedures/examples.json#L1685)

**Recorded version interval:** 2026-08-26 to no end encoded, selected by assessment date. **Verification:** guidance_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-gateway2-draft-map"></a>

## Provide an emerging policies map where possible to assist gateway 2.

**Advisory guidance · responsible actor: Local planning authority**

Rule [`new.gateway2_draft_map`](../../../knowledge/procedures/model.json#L3492); version 0.1.0.

### Source to inspect

- [3.6.9-3.6.11](https://www.gov.uk/guidance/procedural-guide-for-examinations-and-gateways-under-the-town-and-country-planning-local-planning-england-regulations-2026) — Procedural guide for Examinations and Gateways under the 2026 Regulations; first edition; updated 2026-08-26 (guidance)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: Emerging policies map supplied at gateway 2 ([input `new_gateway2_policies_map_provided`](../facts.md#new-gateway2-policies-map-provided)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`new_gateway2_policies_map_provided`](../facts.md#new-gateway2-policies-map-provided) | An emerging policies map was supplied to assist gateway 2 as recommended by guidance. Its absence alone does not establish a breach of regulation 26(3). | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `advisory_gap`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

Recommended supporting material; absence alone does not establish breach of reg 26(3).


**Examples selecting this assertion:**

- [Absent draft plan/map are advisory gaps; necessary-material duty can still be met.](../worked-examples.md#gateway2-no-draft-plan)

**Recorded version interval:** 2026-08-26 to no end encoded, selected by assessment date. **Verification:** guidance_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-gateway2-cover"></a>

## Provide Gateway 2 covering letter.

**Advisory guidance · responsible actor: Local planning authority**

Rule [`new.gateway2_cover`](../../../knowledge/procedures/model.json#L3533); version 0.1.0.

### Source to inspect

- [3.6.3](https://www.gov.uk/guidance/procedural-guide-for-examinations-and-gateways-under-the-town-and-country-planning-local-planning-england-regulations-2026) — Procedural guide for Examinations and Gateways under the 2026 Regulations; first edition; updated 2026-08-26 (guidance)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: A covering letter was supplied with the gateway 2 material, as recommended by the procedure guide ([input `new_gateway2_gateway2_cover_provided`](../facts.md#new-gateway2-gateway2-cover-provided)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`new_gateway2_gateway2_cover_provided`](../facts.md#new-gateway2-gateway2-cover-provided) | A covering letter was supplied with the gateway 2 material, as recommended by the procedure guide. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `advisory_gap`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

Recommended supporting material; absence alone does not establish breach of reg 26(3).


**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-08-26 to no end encoded, selected by assessment date. **Verification:** guidance_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-gateway2-compliance"></a>

## Provide Draft statement of compliance.

**Advisory guidance · responsible actor: Local planning authority**

Rule [`new.gateway2_compliance`](../../../knowledge/procedures/model.json#L3574); version 0.1.0.

### Source to inspect

- [3.6.5](https://www.gov.uk/guidance/procedural-guide-for-examinations-and-gateways-under-the-town-and-country-planning-local-planning-england-regulations-2026) — Procedural guide for Examinations and Gateways under the 2026 Regulations; first edition; updated 2026-08-26 (guidance)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: A draft statement of compliance was supplied to assist gateway 2; this is the recommended draft, not the mandatory completed gateway 3 statement ([input `new_gateway2_draft_compliance_provided`](../facts.md#new-gateway2-draft-compliance-provided)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`new_gateway2_draft_compliance_provided`](../facts.md#new-gateway2-draft-compliance-provided) | A draft statement of compliance was supplied to assist gateway 2; this is the recommended draft, not the mandatory completed gateway 3 statement. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `advisory_gap`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

Recommended supporting material; absence alone does not establish breach of reg 26(3).


**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-08-26 to no end encoded, selected by assessment date. **Verification:** guidance_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-gateway2-soundness"></a>

## Provide Draft statement of soundness.

**Advisory guidance · responsible actor: Local planning authority**

Rule [`new.gateway2_soundness`](../../../knowledge/procedures/model.json#L3615); version 0.1.0.

### Source to inspect

- [3.6.5](https://www.gov.uk/guidance/procedural-guide-for-examinations-and-gateways-under-the-town-and-country-planning-local-planning-england-regulations-2026) — Procedural guide for Examinations and Gateways under the 2026 Regulations; first edition; updated 2026-08-26 (guidance)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: A draft statement of soundness was supplied to assist gateway 2; this is the recommended draft, not an examiner’s finding of soundness ([input `new_gateway2_draft_soundness_provided`](../facts.md#new-gateway2-draft-soundness-provided)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`new_gateway2_draft_soundness_provided`](../facts.md#new-gateway2-draft-soundness-provided) | A draft statement of soundness was supplied to assist gateway 2; this is the recommended draft, not an examiner’s finding of soundness. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `advisory_gap`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

Recommended supporting material; absence alone does not establish breach of reg 26(3).


**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-08-26 to no end encoded, selected by assessment date. **Verification:** guidance_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-gateway2-index"></a>

## Provide Evidence register with completion dates.

**Advisory guidance · responsible actor: Local planning authority**

Rule [`new.gateway2_index`](../../../knowledge/procedures/model.json#L3656); version 0.1.0.

### Source to inspect

- [3.6.13](https://www.gov.uk/guidance/procedural-guide-for-examinations-and-gateways-under-the-town-and-country-planning-local-planning-england-regulations-2026) — Procedural guide for Examinations and Gateways under the 2026 Regulations; first edition; updated 2026-08-26 (guidance)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: An evidence register, including expected completion dates for outstanding evidence where relevant, was supplied to assist gateway 2 under the guide ([input `new_gateway2_evidence_index_provided`](../facts.md#new-gateway2-evidence-index-provided)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`new_gateway2_evidence_index_provided`](../facts.md#new-gateway2-evidence-index-provided) | An evidence register, including expected completion dates for outstanding evidence where relevant, was supplied to assist gateway 2 under the guide. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `advisory_gap`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

Recommended supporting material; absence alone does not establish breach of reg 26(3).


**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-08-26 to no end encoded, selected by assessment date. **Verification:** guidance_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-gateway2-target"></a>

## Aim to complete gateway 2 in four to six weeks.

**Service target · responsible actor: Secretary of State appointed gateway assessor**

Rule [`new.gateway2_target`](../../../knowledge/procedures/model.json#L3697); version 0.1.0.

### Source to inspect

- [3.5.2; 3.5.10](https://www.gov.uk/guidance/procedural-guide-for-examinations-and-gateways-under-the-town-and-country-planning-local-planning-england-regulations-2026) — Procedural guide for Examinations and Gateways under the 2026 Regulations; first edition; updated 2026-08-26 (guidance)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: An evidenced review establishes whether gateway 2 met the guide’s indicative four-to-six-week duration, allowing for its stated qualifications ([input `gateway2_target_met`](../facts.md#gateway2-target-met)).

**Timing:** gateway 2 start → report; indicative four-to-six-week range, not a legal maximum.

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`gateway2_target_met`](../facts.md#gateway2-target-met) | An evidenced review establishes whether gateway 2 met the guide’s indicative four-to-six-week duration, allowing for its stated qualifications. This is a service target, not a statutory time limit. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `target_missed`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

- Recorded exception: Further work during gateway can extend the indicative period.

**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-08-26 to no end encoded, selected by assessment date. **Verification:** guidance_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-gateway2-publication"></a>

## Publish assessor advice as soon as reasonably practicable and simultaneously make submitted material available, notify requesters and send copies to persons identified in the advice.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.gateway2_publication`](../../../knowledge/procedures/model.json#L3745); version 0.1.0.

### Source to inspect

- [reg 26(5)](https://www.legislation.gov.uk/uksi/2026/186/regulation/26/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)
- [s 15CA(5)](https://www.legislation.gov.uk/ukpga/2004/5/section/15CA) — PCPA 2004 section 15CA; revised text retrieved 2026-10-29 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: Gateway 2 advice was published as soon as reasonably practicable; on the publication day the advice and supplied material were made available, requesters/appropriate persons notified and copies sent to persons identified in the advice ([input `gateway2_publication_and_notices_recorded`](../facts.md#gateway2-publication-and-notices-recorded)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`gateway2_publication_and_notices_recorded`](../facts.md#gateway2-publication-and-notices-recorded) | Gateway 2 advice was published as soon as reasonably practicable; on the publication day the advice and supplied material were made available, requesters/appropriate persons notified and copies sent to persons identified in the advice. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

## Connections to other stages

- [Content and evidence consultation](new-content.md) → [Gateway 2: observations and advice](new-gateway2.md): Satisfy the cited timing and evidence requirements; see stage rules. (sequence).
- [Gateway 2: observations and advice](new-gateway2.md) → [Consultation on proposed Local Plan](new-publication.md): Satisfy the cited timing and evidence requirements; see stage rules. (sequence).

These relationships are descriptive. They are not executable workflow guards.
