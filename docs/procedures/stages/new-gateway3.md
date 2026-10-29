# Gateway 3: prescribed requirements

[Review guide](../README.md) · [Input definitions](../facts.md) · [Worked examples](../worked-examples.md)

Generated from model 0.1.0, knowledge date 2026-10-29. Rebuild with `python tools/build_procedure_docs.py`. Authored explanations live in [editorial notes](../editorial-notes.md). Legal mappings await maintainer review.

Gateway 3 is the appointed assessor's readiness assessment against the prescribed
regulation 32 requirements. The authority supplies the regulation 17 documents,
including completed compliance and soundness statements. This stage has three
separate questions: was the required material supplied at the right time; what
did the assessor conclude about each requirement; and were advice and successful
completion material published correctly? The model records the assessor's findings
as inputs. It does not infer soundness from the presence of documents.

**Who is involved:** Local planning authority; Secretary of State appointed gateway assessor

**Stage inputs:** Proposed Local Plan; Proposed or submission policies map; Statement of compliance; Statement of soundness

**Stage outputs:** Reasoned gateway 3 conclusions for each requirement; Gateway 3 completion statement

Stage inputs/outputs are an indicative map; the individual rules below determine which selected document duties are conditional.

## Assertions at this stage

| Assertion | Status | Evaluator operation |
| --- | --- | --- |
| [Seek gateway 3 when the authority considers prescribed requirements met, no earlier than the day after proposed-plan summary publication.](#new-gateway3-sequence) | Statutory assertion | Date arithmetic + supplied observations |
| [Provide Proposed Local Plan.](#new-gateway3-plan) | Statutory assertion | Supplied observations only |
| [Provide Proposed or submission policies map.](#new-gateway3-policies-map) | Statutory assertion | Supplied observations only |
| [Provide Statement of compliance.](#new-gateway3-compliance) | Statutory assertion | Supplied observations only |
| [Provide Statement of soundness.](#new-gateway3-soundness) | Statutory assertion | Supplied observations only |
| [Provide Summary of consultation and engagement.](#new-gateway3-engagement-summary) | Statutory assertion | Supplied observations only |
| [Provide Summary of scoping consultation.](#new-gateway3-scoping-summary) | Statutory assertion | Supplied observations only |
| [Provide Content and evidence consultation summary.](#new-gateway3-content-summary) | Statutory assertion | Supplied observations only |
| [Provide Proposed-plan consultation summary.](#new-gateway3-plan-summary) | Statutory assertion | Supplied observations only |
| [Provide Representations on conformity with operative SDS.](#new-gateway3-sds-representations) | Statutory assertion | Supplied observations only |
| [Provide Practical arrangements for examination.](#new-gateway3-practical-readiness) | Statutory assertion | Supplied observations only |
| [Provide Supplementary plans statement.](#new-gateway3-supplementary-statement) | Statutory assertion | Supplied observations only |
| [Provide Environmental report under SEA reg 12.](#new-gateway3-environmental-report) | Statutory assertion | Supplied observations only |
| [Provide SEA screening determination reasons under reg 9(3).](#new-gateway3-screening-reasons) | Statutory assertion | Supplied observations only |
| [Send additional material the authority considers necessary for the prescribed-requirements assessment.](#new-gateway3-other-material) | Statutory assertion | Supplied observations only |
| [Policies on amount, type, location and timing of development.](#new-gateway3-test-a) | Statutory assertion | Supplied observations only |
| [Area-specific vision, no more than ten measurable outcomes, and superseded-policy content or explanation.](#new-gateway3-test-b) | Statutory assertion | Supplied observations only |
| [Climate change mitigation and adaptation.](#new-gateway3-test-c) | Statutory assertion | Supplied observations only |
| [Local nature recovery strategy taken into account.](#new-gateway3-test-d) | Statutory assertion | Supplied observations only |
| [Housing and affordable-housing need assessment taken into account.](#new-gateway3-test-e) | Statutory assertion | Supplied observations only |
| [No content beyond what is permitted or required.](#new-gateway3-test-f) | Statutory assertion | Supplied observations only |
| [Required gateway requests made at the prescribed times.](#new-gateway3-test-g) | Statutory assertion | Supplied observations only |
| [Gateway 2 advice published.](#new-gateway3-test-h) | Statutory assertion | Supplied observations only |
| [Regard had to applicable statutory matters.](#new-gateway3-test-i) | Statutory assertion | Supplied observations only |
| [Prescribed independent-examination documents prepared.](#new-gateway3-test-j) | Statutory assertion | Supplied observations only |
| [Policies map accurately illustrates geographical policy application.](#new-gateway3-test-k) | Statutory assertion | Supplied observations only |
| [Practical readiness for examination.](#new-gateway3-test-l) | Statutory assertion | Supplied observations only |
| [Provide a met/not-met conclusion and reasoned justification for each prescribed requirement, electronically in typescript.](#new-gateway3-reasons) | Statutory assertion | Supplied observations only |
| [On publication of successful gateway 3 advice, also publish the completion statement and gateway 3 submission documents.](#new-gateway3-completion) | Statutory assertion | Supplied observations only |
| [Publish gateway 3 advice and make it available, notify requesters and send copies to persons identified in the advice, whether or not requirements are met.](#new-gateway3-publication) | Statutory assertion | Supplied observations only |
| [Send the gateway 3 submission documents on the gateway request date.](#new-gateway3-document-timing) | Statutory assertion | Date arithmetic + supplied observations |

<a id="new-gateway3-sequence"></a>

## Seek gateway 3 when the authority considers prescribed requirements met, no earlier than the day after proposed-plan summary publication.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.gateway3_sequence`](../../../knowledge/procedures/model.json#L4072); version 0.1.0.

### Source to inspect

- [reg 31(1)-(2)](https://www.legislation.gov.uk/uksi/2026/186/regulation/31/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Every** condition below:
  - **Yes** to: The authority considers that the regulation 32 prescribed requirements are met when seeking gateway 3 ([input `lpa_considers_prescribed_requirements_met`](../facts.md#lpa-considers-prescribed-requirements-met)).
  - [Calendar date on which the authority sought the initial gateway 3 prescribed-requirements assessment under regulation 31](../facts.md#gateway3-requested) is at least the next calendar day after [Calendar date on which the regulation 30 proposed-plan consultation summary was made available](../facts.md#plan-summary-published).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`gateway3_requested`](../facts.md#gateway3-requested) | Calendar date on which the authority sought the initial gateway 3 prescribed-requirements assessment under regulation 31. | Recorded observation; date |
| [`lpa_considers_prescribed_requirements_met`](../facts.md#lpa-considers-prescribed-requirements-met) | The authority considers that the regulation 32 prescribed requirements are met when seeking gateway 3. This is its own judgement, distinct from the appointed assessor’s subsequent advice. | Reviewer judgement; boolean |
| [`plan_summary_published`](../facts.md#plan-summary-published) | Calendar date on which the regulation 30 proposed-plan consultation summary was made available. | Recorded observation; date |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-gateway3-plan"></a>

## Provide Proposed Local Plan.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.gateway3_plan`](../../../knowledge/procedures/model.json#L4122); version 0.1.0.

### Source to inspect

- [reg 17 gateway 3 submission documents (a); reg 31(3)](https://www.legislation.gov.uk/uksi/2026/186/regulation/17/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: The reviewer has verified that the proposed Local Plan was included in the gateway 3 submission to the appointed assessor ([input `new_gateway3_plan_provided`](../facts.md#new-gateway3-plan-provided)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`new_gateway3_plan_provided`](../facts.md#new-gateway3-plan-provided) | The reviewer has verified that the proposed Local Plan was included in the gateway 3 submission to the appointed assessor. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

Document presence is not verification of its content or adequacy; documents are sent on the gateway request date.


**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-gateway3-policies-map"></a>

## Provide Proposed or submission policies map.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.gateway3_policies_map`](../../../knowledge/procedures/model.json#L4163); version 0.1.0.

### Source to inspect

- [reg 17 gateway 3 submission documents (b); reg 31(3)](https://www.legislation.gov.uk/uksi/2026/186/regulation/17/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: The reviewer has verified that the proposed or submission policies map was included in the gateway 3 submission to the appointed assessor ([input `new_gateway3_policies_map_provided`](../facts.md#new-gateway3-policies-map-provided)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`new_gateway3_policies_map_provided`](../facts.md#new-gateway3-policies-map-provided) | The reviewer has verified that the proposed or submission policies map was included in the gateway 3 submission to the appointed assessor. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

Document presence is not verification of its content or adequacy; documents are sent on the gateway request date.


**Examples selecting this assertion:**

- [The proposed policies map is a gateway 3 submission document.](../../../knowledge/procedures/examples.json#L685)

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-gateway3-compliance"></a>

## Provide Statement of compliance.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.gateway3_compliance`](../../../knowledge/procedures/model.json#L4204); version 0.1.0.

### Source to inspect

- [reg 17 gateway 3 submission documents (c); reg 31(3)](https://www.legislation.gov.uk/uksi/2026/186/regulation/17/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: The reviewer has verified that the statement of compliance was included in the gateway 3 submission to the appointed assessor ([input `new_gateway3_compliance_provided`](../facts.md#new-gateway3-compliance-provided)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`new_gateway3_compliance_provided`](../facts.md#new-gateway3-compliance-provided) | The reviewer has verified that the statement of compliance was included in the gateway 3 submission to the appointed assessor. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

Document presence is not verification of its content or adequacy; documents are sent on the gateway request date.


**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-gateway3-soundness"></a>

## Provide Statement of soundness.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.gateway3_soundness`](../../../knowledge/procedures/model.json#L4245); version 0.1.0.

### Source to inspect

- [reg 17 gateway 3 submission documents (d); reg 31(3)](https://www.legislation.gov.uk/uksi/2026/186/regulation/17/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: Statement of soundness supplied in the gateway 3 pack ([input `new_gateway3_soundness_provided`](../facts.md#new-gateway3-soundness-provided)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`new_gateway3_soundness_provided`](../facts.md#new-gateway3-soundness-provided) | The reviewer has verified that the statement of soundness was included in the gateway 3 submission to the appointed assessor. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

This is a **statement of soundness**, supplied by the authority, in the prescribed
pack. The single Boolean establishes only its provision. It neither assesses the
strength of the statement nor records the examiner's eventual conclusion. Review
the definition in regulation 17 and the sending duty in regulation 31(3) separately.

Document presence is not verification of its content or adequacy; documents are sent on the gateway request date.


**Examples selecting this assertion:**

- [Completed statement of soundness is mandatory at gateway 3.](../worked-examples.md#gateway3-missing-soundness)
- [An absent observation is not proof that the document is absent.](../../../knowledge/procedures/examples.json#L467)

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-gateway3-engagement-summary"></a>

## Provide Summary of consultation and engagement.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.gateway3_engagement_summary`](../../../knowledge/procedures/model.json#L4286); version 0.1.0.

### Source to inspect

- [reg 17 gateway 3 submission documents (e); reg 31(3)](https://www.legislation.gov.uk/uksi/2026/186/regulation/17/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: The reviewer has verified that the summary of consultation and engagement was included in the gateway 3 submission to the appointed assessor ([input `new_gateway3_engagement_summary_provided`](../facts.md#new-gateway3-engagement-summary-provided)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`new_gateway3_engagement_summary_provided`](../facts.md#new-gateway3-engagement-summary-provided) | The reviewer has verified that the summary of consultation and engagement was included in the gateway 3 submission to the appointed assessor. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

Document presence is not verification of its content or adequacy; documents are sent on the gateway request date.


**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-gateway3-scoping-summary"></a>

## Provide Summary of scoping consultation.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.gateway3_scoping_summary`](../../../knowledge/procedures/model.json#L4327); version 0.1.0.

### Source to inspect

- [reg 17 gateway 3 submission documents (f); reg 31(3)](https://www.legislation.gov.uk/uksi/2026/186/regulation/17/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: The reviewer has verified that the summary of scoping consultation was included in the gateway 3 submission to the appointed assessor ([input `new_gateway3_scoping_summary_provided`](../facts.md#new-gateway3-scoping-summary-provided)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`new_gateway3_scoping_summary_provided`](../facts.md#new-gateway3-scoping-summary-provided) | The reviewer has verified that the summary of scoping consultation was included in the gateway 3 submission to the appointed assessor. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

Document presence is not verification of its content or adequacy; documents are sent on the gateway request date.


**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-gateway3-content-summary"></a>

## Provide Content and evidence consultation summary.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.gateway3_content_summary`](../../../knowledge/procedures/model.json#L4368); version 0.1.0.

### Source to inspect

- [reg 17 gateway 3 submission documents (g); reg 31(3)](https://www.legislation.gov.uk/uksi/2026/186/regulation/17/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: The reviewer has verified that the content and evidence consultation summary was included in the gateway 3 submission to the appointed assessor ([input `new_gateway3_content_summary_provided`](../facts.md#new-gateway3-content-summary-provided)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`new_gateway3_content_summary_provided`](../facts.md#new-gateway3-content-summary-provided) | The reviewer has verified that the content and evidence consultation summary was included in the gateway 3 submission to the appointed assessor. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

Document presence is not verification of its content or adequacy; documents are sent on the gateway request date.


**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-gateway3-plan-summary"></a>

## Provide Proposed-plan consultation summary.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.gateway3_plan_summary`](../../../knowledge/procedures/model.json#L4409); version 0.1.0.

### Source to inspect

- [reg 17 gateway 3 submission documents (h); reg 31(3)](https://www.legislation.gov.uk/uksi/2026/186/regulation/17/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: The reviewer has verified that the proposed-plan consultation summary was included in the gateway 3 submission to the appointed assessor ([input `new_gateway3_plan_summary_provided`](../facts.md#new-gateway3-plan-summary-provided)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`new_gateway3_plan_summary_provided`](../facts.md#new-gateway3-plan-summary-provided) | The reviewer has verified that the proposed-plan consultation summary was included in the gateway 3 submission to the appointed assessor. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

Document presence is not verification of its content or adequacy; documents are sent on the gateway request date.


**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-gateway3-sds-representations"></a>

## Provide Representations on conformity with operative SDS.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.gateway3_sds_representations`](../../../knowledge/procedures/model.json#L4450); version 0.1.0.

### Source to inspect

- [reg 17 gateway 3 submission documents (i); reg 31(3)](https://www.legislation.gov.uk/uksi/2026/186/regulation/17/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- **Every** condition below:
  - **Yes** to: A spatial development strategy is operative in relation to the plan area so that the selected regulation 28 conformity/document requirements apply ([input `operative_sds`](../facts.md#operative-sds)).
  - **Yes** to: At least one conformity representation was received under regulation 28; copies must be included where the selected pack requires them ([input `sds_representations_received`](../facts.md#sds-representations-received)).

### What the evaluator actually requires

- **Yes** to: The reviewer has verified that the representations on conformity with operative SDS was included in the gateway 3 submission to the appointed assessor ([input `new_gateway3_sds_representations_provided`](../facts.md#new-gateway3-sds-representations-provided)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`new_gateway3_sds_representations_provided`](../facts.md#new-gateway3-sds-representations-provided) | The reviewer has verified that the representations on conformity with operative SDS was included in the gateway 3 submission to the appointed assessor. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission. | Recorded observation; boolean |
| [`operative_sds`](../facts.md#operative-sds) | A spatial development strategy is operative in relation to the plan area so that the selected regulation 28 conformity/document requirements apply. | Recorded observation; boolean |
| [`sds_representations_received`](../facts.md#sds-representations-received) | At least one conformity representation was received under regulation 28; copies must be included where the selected pack requires them. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

Document presence is not verification of its content or adequacy; documents are sent on the gateway request date.


**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-gateway3-practical-readiness"></a>

## Provide Practical arrangements for examination.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.gateway3_practical_readiness`](../../../knowledge/procedures/model.json#L4502); version 0.1.0.

### Source to inspect

- [reg 17 gateway 3 submission documents (j); reg 31(3)](https://www.legislation.gov.uk/uksi/2026/186/regulation/17/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: The reviewer has verified that the practical arrangements for examination was included in the gateway 3 submission to the appointed assessor ([input `new_gateway3_practical_readiness_provided`](../facts.md#new-gateway3-practical-readiness-provided)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`new_gateway3_practical_readiness_provided`](../facts.md#new-gateway3-practical-readiness-provided) | The reviewer has verified that the practical arrangements for examination was included in the gateway 3 submission to the appointed assessor. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

Document presence is not verification of its content or adequacy; documents are sent on the gateway request date.


**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-gateway3-supplementary-statement"></a>

## Provide Supplementary plans statement.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.gateway3_supplementary_statement`](../../../knowledge/procedures/model.json#L4543); version 0.1.0.

### Source to inspect

- [reg 17 gateway 3 submission documents (k); reg 31(3)](https://www.legislation.gov.uk/uksi/2026/186/regulation/17/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- **Yes** to: Supplementary plans meeting the condition in regulation 29 are in effect, triggering its statement requirement ([input `qualifying_supplementary_plans`](../facts.md#qualifying-supplementary-plans)).

### What the evaluator actually requires

- **Yes** to: The reviewer has verified that the supplementary plans statement was included in the gateway 3 submission to the appointed assessor ([input `new_gateway3_supplementary_statement_provided`](../facts.md#new-gateway3-supplementary-statement-provided)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`new_gateway3_supplementary_statement_provided`](../facts.md#new-gateway3-supplementary-statement-provided) | The reviewer has verified that the supplementary plans statement was included in the gateway 3 submission to the appointed assessor. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission. | Recorded observation; boolean |
| [`qualifying_supplementary_plans`](../facts.md#qualifying-supplementary-plans) | Supplementary plans meeting the condition in regulation 29 are in effect, triggering its statement requirement. The legal trigger must be checked from the actual instruments. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

Document presence is not verification of its content or adequacy; documents are sent on the gateway request date.


**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-gateway3-environmental-report"></a>

## Provide Environmental report under SEA reg 12.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.gateway3_environmental_report`](../../../knowledge/procedures/model.json#L4585); version 0.1.0.

### Source to inspect

- [reg 17 gateway 3 submission documents (l); reg 31(3)](https://www.legislation.gov.uk/uksi/2026/186/regulation/17/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- **Yes** to: An environmental report has been prepared under regulation 12 of the SEA Regulations 2004 ([input `environmental_report_prepared`](../facts.md#environmental-report-prepared)).

### What the evaluator actually requires

- **Yes** to: The reviewer has verified that the environmental report under SEA reg 12 was included in the gateway 3 submission to the appointed assessor ([input `new_gateway3_environmental_report_provided`](../facts.md#new-gateway3-environmental-report-provided)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`environmental_report_prepared`](../facts.md#environmental-report-prepared) | An environmental report has been prepared under regulation 12 of the SEA Regulations 2004. This triggers the selected pack’s report-copy requirement; it does not decide whether an assessment should have been undertaken. | Recorded observation; boolean |
| [`new_gateway3_environmental_report_provided`](../facts.md#new-gateway3-environmental-report-provided) | The reviewer has verified that the environmental report under SEA reg 12 was included in the gateway 3 submission to the appointed assessor. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

Document presence is not verification of its content or adequacy; documents are sent on the gateway request date.


**Examples selecting this assertion:**

- [A recorded no-significant-effects determination activates reasons; no prepared environmental report is asserted.](../../../knowledge/procedures/examples.json#L722)
- [Do not assume SEA applicability from absent documents.](../../../knowledge/procedures/examples.json#L773)

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-gateway3-screening-reasons"></a>

## Provide SEA screening determination reasons under reg 9(3).

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.gateway3_screening_reasons`](../../../knowledge/procedures/model.json#L4627); version 0.1.0.

### Source to inspect

- [reg 17 gateway 3 submission documents (m); reg 31(3)](https://www.legislation.gov.uk/uksi/2026/186/regulation/17/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- **Yes** to: The authority has made the SEA regulation 9(1) determination that the plan is unlikely to have significant environmental effects, with a reasons statement under regulation 9(3) ([input `sea_no_significant_effects_determination`](../facts.md#sea-no-significant-effects-determination)).

### What the evaluator actually requires

- **Yes** to: The reviewer has verified that the sEA screening determination reasons under reg 9(3) was included in the gateway 3 submission to the appointed assessor ([input `new_gateway3_screening_reasons_provided`](../facts.md#new-gateway3-screening-reasons-provided)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`new_gateway3_screening_reasons_provided`](../facts.md#new-gateway3-screening-reasons-provided) | The reviewer has verified that the sEA screening determination reasons under reg 9(3) was included in the gateway 3 submission to the appointed assessor. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission. | Recorded observation; boolean |
| [`sea_no_significant_effects_determination`](../facts.md#sea-no-significant-effects-determination) | The authority has made the SEA regulation 9(1) determination that the plan is unlikely to have significant environmental effects, with a reasons statement under regulation 9(3). This records the determination, not this evaluator’s environmental judgement. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

Document presence is not verification of its content or adequacy; documents are sent on the gateway request date.


**Examples selecting this assertion:**

- [A recorded no-significant-effects determination activates reasons; no prepared environmental report is asserted.](../../../knowledge/procedures/examples.json#L722)
- [Do not assume SEA applicability from absent documents.](../../../knowledge/procedures/examples.json#L773)

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-gateway3-other-material"></a>

## Send additional material the authority considers necessary for the prescribed-requirements assessment.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.gateway3_other_material`](../../../knowledge/procedures/model.json#L4669); version 0.1.0.

### Source to inspect

- [reg 17 gateway 3 submission documents (n); reg 31(3)](https://www.legislation.gov.uk/uksi/2026/186/regulation/17/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: The authority sent any additional documents or information it considered necessary to support the gateway 3 assessment, under the regulation 17 definition ([input `gateway3_additional_material_sent`](../facts.md#gateway3-additional-material-sent)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`gateway3_additional_material_sent`](../facts.md#gateway3-additional-material-sent) | The authority sent any additional documents or information it considered necessary to support the gateway 3 assessment, under the regulation 17 definition. The evaluator does not decide which additional evidence is necessary. | Reviewer judgement; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-gateway3-test-a"></a>

## Policies on amount, type, location and timing of development.

**Statutory assertion · responsible actor: Secretary of State appointed gateway assessor**

Rule [`new.gateway3_test_a`](../../../knowledge/procedures/model.json#L4710); version 0.1.0.

### Source to inspect

- [reg 32(a)](https://www.legislation.gov.uk/uksi/2026/186/regulation/32/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: Appointed assessor’s evidenced conclusion on reg 32(a): Policies on amount, type, location and timing of development ([input `assessor_reg32_a_satisfied`](../facts.md#assessor-reg32-a-satisfied)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`assessor_reg32_a_satisfied`](../facts.md#assessor-reg32-a-satisfied) | Appointed assessor’s evidenced conclusion on reg 32(a): Policies on amount, type, location and timing of development. Not inferred from file presence. | Reviewer judgement; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

Attributed assessor conclusion required; neither document presence nor a model-generated judgement substitutes for it.


**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-gateway3-test-b"></a>

## Area-specific vision, no more than ten measurable outcomes, and superseded-policy content or explanation.

**Statutory assertion · responsible actor: Secretary of State appointed gateway assessor**

Rule [`new.gateway3_test_b`](../../../knowledge/procedures/model.json#L4751); version 0.1.0.

### Source to inspect

- [reg 32(b)](https://www.legislation.gov.uk/uksi/2026/186/regulation/32/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: Appointed assessor’s evidenced conclusion on reg 32(b): Area-specific vision, no more than ten measurable outcomes, and superseded-policy content or explanation ([input `assessor_reg32_b_satisfied`](../facts.md#assessor-reg32-b-satisfied)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`assessor_reg32_b_satisfied`](../facts.md#assessor-reg32-b-satisfied) | Appointed assessor’s evidenced conclusion on reg 32(b): Area-specific vision, no more than ten measurable outcomes, and superseded-policy content or explanation. Not inferred from file presence. | Reviewer judgement; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

Attributed assessor conclusion required; neither document presence nor a model-generated judgement substitutes for it.

- Recorded exception: For superseded policies, reg 32(b)(iii) permits the statement-of-compliance explanation.

**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-gateway3-test-c"></a>

## Climate change mitigation and adaptation.

**Statutory assertion · responsible actor: Secretary of State appointed gateway assessor**

Rule [`new.gateway3_test_c`](../../../knowledge/procedures/model.json#L4794); version 0.1.0.

### Source to inspect

- [reg 32(c)](https://www.legislation.gov.uk/uksi/2026/186/regulation/32/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: Appointed assessor’s evidenced conclusion on reg 32(c): Climate change mitigation and adaptation ([input `assessor_reg32_c_satisfied`](../facts.md#assessor-reg32-c-satisfied)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`assessor_reg32_c_satisfied`](../facts.md#assessor-reg32-c-satisfied) | Appointed assessor’s evidenced conclusion on reg 32(c): Climate change mitigation and adaptation. Not inferred from file presence. | Reviewer judgement; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

Attributed assessor conclusion required; neither document presence nor a model-generated judgement substitutes for it.


**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-gateway3-test-d"></a>

## Local nature recovery strategy taken into account.

**Statutory assertion · responsible actor: Secretary of State appointed gateway assessor**

Rule [`new.gateway3_test_d`](../../../knowledge/procedures/model.json#L4835); version 0.1.0.

### Source to inspect

- [reg 32(d)](https://www.legislation.gov.uk/uksi/2026/186/regulation/32/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: Appointed assessor’s evidenced conclusion on reg 32(d): Local nature recovery strategy taken into account ([input `assessor_reg32_d_satisfied`](../facts.md#assessor-reg32-d-satisfied)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`assessor_reg32_d_satisfied`](../facts.md#assessor-reg32-d-satisfied) | Appointed assessor’s evidenced conclusion on reg 32(d): Local nature recovery strategy taken into account. Not inferred from file presence. | Reviewer judgement; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

Attributed assessor conclusion required; neither document presence nor a model-generated judgement substitutes for it.


**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-gateway3-test-e"></a>

## Housing and affordable-housing need assessment taken into account.

**Statutory assertion · responsible actor: Secretary of State appointed gateway assessor**

Rule [`new.gateway3_test_e`](../../../knowledge/procedures/model.json#L4876); version 0.1.0.

### Source to inspect

- [reg 32(e)](https://www.legislation.gov.uk/uksi/2026/186/regulation/32/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: Appointed assessor’s evidenced conclusion on reg 32(e): Housing and affordable-housing need assessment taken into account ([input `assessor_reg32_e_satisfied`](../facts.md#assessor-reg32-e-satisfied)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`assessor_reg32_e_satisfied`](../facts.md#assessor-reg32-e-satisfied) | Appointed assessor’s evidenced conclusion on reg 32(e): Housing and affordable-housing need assessment taken into account. Not inferred from file presence. | Reviewer judgement; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

Attributed assessor conclusion required; neither document presence nor a model-generated judgement substitutes for it.


**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-gateway3-test-f"></a>

## No content beyond what is permitted or required.

**Statutory assertion · responsible actor: Secretary of State appointed gateway assessor**

Rule [`new.gateway3_test_f`](../../../knowledge/procedures/model.json#L4917); version 0.1.0.

### Source to inspect

- [reg 32(f)](https://www.legislation.gov.uk/uksi/2026/186/regulation/32/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: Appointed assessor’s evidenced conclusion on reg 32(f): No content beyond what is permitted or required ([input `assessor_reg32_f_satisfied`](../facts.md#assessor-reg32-f-satisfied)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`assessor_reg32_f_satisfied`](../facts.md#assessor-reg32-f-satisfied) | Appointed assessor’s evidenced conclusion on reg 32(f): No content beyond what is permitted or required. Not inferred from file presence. | Reviewer judgement; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

Attributed assessor conclusion required; neither document presence nor a model-generated judgement substitutes for it.


**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-gateway3-test-g"></a>

## Required gateway requests made at the prescribed times.

**Statutory assertion · responsible actor: Secretary of State appointed gateway assessor**

Rule [`new.gateway3_test_g`](../../../knowledge/procedures/model.json#L4958); version 0.1.0.

### Source to inspect

- [reg 32(g)](https://www.legislation.gov.uk/uksi/2026/186/regulation/32/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: Appointed assessor’s evidenced conclusion on reg 32(g): Required gateway requests made at the prescribed times ([input `assessor_reg32_g_satisfied`](../facts.md#assessor-reg32-g-satisfied)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`assessor_reg32_g_satisfied`](../facts.md#assessor-reg32-g-satisfied) | Appointed assessor’s evidenced conclusion on reg 32(g): Required gateway requests made at the prescribed times. Not inferred from file presence. | Reviewer judgement; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

Attributed assessor conclusion required; neither document presence nor a model-generated judgement substitutes for it.


**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-gateway3-test-h"></a>

## Gateway 2 advice published.

**Statutory assertion · responsible actor: Secretary of State appointed gateway assessor**

Rule [`new.gateway3_test_h`](../../../knowledge/procedures/model.json#L4999); version 0.1.0.

### Source to inspect

- [reg 32(h)](https://www.legislation.gov.uk/uksi/2026/186/regulation/32/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: Appointed assessor’s evidenced conclusion on reg 32(h): Gateway 2 advice published ([input `assessor_reg32_h_satisfied`](../facts.md#assessor-reg32-h-satisfied)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`assessor_reg32_h_satisfied`](../facts.md#assessor-reg32-h-satisfied) | Appointed assessor’s evidenced conclusion on reg 32(h): Gateway 2 advice published. Not inferred from file presence. | Reviewer judgement; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

Attributed assessor conclusion required; neither document presence nor a model-generated judgement substitutes for it.


**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-gateway3-test-i"></a>

## Regard had to applicable statutory matters.

**Statutory assertion · responsible actor: Secretary of State appointed gateway assessor**

Rule [`new.gateway3_test_i`](../../../knowledge/procedures/model.json#L5040); version 0.1.0.

### Source to inspect

- [reg 32(i)](https://www.legislation.gov.uk/uksi/2026/186/regulation/32/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: Appointed assessor’s evidenced conclusion on reg 32(i): Regard had to applicable statutory matters ([input `assessor_reg32_i_satisfied`](../facts.md#assessor-reg32-i-satisfied)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`assessor_reg32_i_satisfied`](../facts.md#assessor-reg32-i-satisfied) | Appointed assessor’s evidenced conclusion on reg 32(i): Regard had to applicable statutory matters. Not inferred from file presence. | Reviewer judgement; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

Attributed assessor conclusion required; neither document presence nor a model-generated judgement substitutes for it. Only commenced matters in s 15CA(6); subsection (h) not activated by SI 2026/169 reg 3(b)(i).


**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-gateway3-test-j"></a>

## Prescribed independent-examination documents prepared.

**Statutory assertion · responsible actor: Secretary of State appointed gateway assessor**

Rule [`new.gateway3_test_j`](../../../knowledge/procedures/model.json#L5081); version 0.1.0.

### Source to inspect

- [reg 32(j)](https://www.legislation.gov.uk/uksi/2026/186/regulation/32/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: Appointed assessor’s evidenced conclusion on reg 32(j): Prescribed independent-examination documents prepared ([input `assessor_reg32_j_satisfied`](../facts.md#assessor-reg32-j-satisfied)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`assessor_reg32_j_satisfied`](../facts.md#assessor-reg32-j-satisfied) | Appointed assessor’s evidenced conclusion on reg 32(j): Prescribed independent-examination documents prepared. Not inferred from file presence. | Reviewer judgement; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

This records the appointed assessor's conclusion that the regulation 34 documents
specified in regulation 32(j) have been prepared. It is not recomputed from the
pack-presence facts. That separation preserves attribution but also means inconsistent
inputs can currently coexist: the evaluator has no cross-fact contradiction engine.

Attributed assessor conclusion required; neither document presence nor a model-generated judgement substitutes for it.


**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-gateway3-test-k"></a>

## Policies map accurately illustrates geographical policy application.

**Statutory assertion · responsible actor: Secretary of State appointed gateway assessor**

Rule [`new.gateway3_test_k`](../../../knowledge/procedures/model.json#L5122); version 0.1.0.

### Source to inspect

- [reg 32(k)](https://www.legislation.gov.uk/uksi/2026/186/regulation/32/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: Appointed assessor’s evidenced conclusion on reg 32(k): Policies map accurately illustrates geographical policy application ([input `assessor_reg32_k_satisfied`](../facts.md#assessor-reg32-k-satisfied)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`assessor_reg32_k_satisfied`](../facts.md#assessor-reg32-k-satisfied) | Appointed assessor’s evidenced conclusion on reg 32(k): Policies map accurately illustrates geographical policy application. Not inferred from file presence. | Reviewer judgement; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

Attributed assessor conclusion required; neither document presence nor a model-generated judgement substitutes for it.


**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-gateway3-test-l"></a>

## Practical readiness for examination.

**Statutory assertion · responsible actor: Secretary of State appointed gateway assessor**

Rule [`new.gateway3_test_l`](../../../knowledge/procedures/model.json#L5163); version 0.1.0.

### Source to inspect

- [reg 32(l)](https://www.legislation.gov.uk/uksi/2026/186/regulation/32/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: Appointed assessor’s evidenced conclusion on reg 32(l): Practical readiness for examination ([input `assessor_reg32_l_satisfied`](../facts.md#assessor-reg32-l-satisfied)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`assessor_reg32_l_satisfied`](../facts.md#assessor-reg32-l-satisfied) | Appointed assessor’s evidenced conclusion on reg 32(l): Practical readiness for examination. Not inferred from file presence. | Reviewer judgement; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

Attributed assessor conclusion required; neither document presence nor a model-generated judgement substitutes for it.


**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-gateway3-reasons"></a>

## Provide a met/not-met conclusion and reasoned justification for each prescribed requirement, electronically in typescript.

**Statutory assertion · responsible actor: Secretary of State appointed gateway assessor**

Rule [`new.gateway3_reasons`](../../../knowledge/procedures/model.json#L5204); version 0.1.0.

### Source to inspect

- [reg 31(4)](https://www.legislation.gov.uk/uksi/2026/186/regulation/31/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: The appointed assessor sent electronically in typescript a met/not-met conclusion and reasoned justification for each regulation 32 requirement under regulation 31(4) ([input `gateway3_reasoned_findings_sent`](../facts.md#gateway3-reasoned-findings-sent)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`gateway3_reasoned_findings_sent`](../facts.md#gateway3-reasoned-findings-sent) | The appointed assessor sent electronically in typescript a met/not-met conclusion and reasoned justification for each regulation 32 requirement under regulation 31(4). | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-gateway3-completion"></a>

## On publication of successful gateway 3 advice, also publish the completion statement and gateway 3 submission documents.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.gateway3_completion`](../../../knowledge/procedures/model.json#L5245); version 0.1.0.

### Source to inspect

- [reg 31(5)-(6)](https://www.legislation.gov.uk/uksi/2026/186/regulation/31/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- **Yes** to: Assessor advises that all prescribed gateway 3 requirements are met ([input `assessor_all_prescribed_requirements_met`](../facts.md#assessor-all-prescribed-requirements-met)).

### What the evaluator actually requires

- **Yes** to: On the day successful gateway 3 advice was published, the authority also made available the completion statement and gateway 3 submission documents under regulation 31(6) ([input `gateway3_completion_publication_recorded`](../facts.md#gateway3-completion-publication-recorded)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`assessor_all_prescribed_requirements_met`](../facts.md#assessor-all-prescribed-requirements-met) | The appointed assessor advises that every reg 32 requirement is met. This records the advice, not an application-generated soundness or legal-compliance certificate. | Reviewer judgement; boolean |
| [`gateway3_completion_publication_recorded`](../facts.md#gateway3-completion-publication-recorded) | On the day successful gateway 3 advice was published, the authority also made available the completion statement and gateway 3 submission documents under regulation 31(6). | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- [Failure at gateway 3 does not remove the advice-publication duty.](../../../knowledge/procedures/examples.json#L1981)

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-gateway3-publication"></a>

## Publish gateway 3 advice and make it available, notify requesters and send copies to persons identified in the advice, whether or not requirements are met.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.gateway3_publication`](../../../knowledge/procedures/model.json#L6802); version 0.1.0.

### Source to inspect

- [s 15CA(5)](https://www.legislation.gov.uk/ukpga/2004/5/section/15CA) — PCPA 2004 section 15CA; revised text retrieved 2026-10-29 (legal basis)
- [reg 31(5)](https://www.legislation.gov.uk/uksi/2026/186/regulation/31/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: Gateway 3 advice published as soon as reasonably practicable; same-day availability, requester notifications and copies to persons identified in the advice under reg 31(5), whether requirements are met or not ([input `gateway3_publication_and_notices_recorded`](../facts.md#gateway3-publication-and-notices-recorded)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`gateway3_publication_and_notices_recorded`](../facts.md#gateway3-publication-and-notices-recorded) | Gateway 3 advice published as soon as reasonably practicable; same-day availability, requester notifications and copies to persons identified in the advice under reg 31(5), whether requirements are met or not. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- [Failure at gateway 3 does not remove the advice-publication duty.](../../../knowledge/procedures/examples.json#L1981)

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-gateway3-document-timing"></a>

## Send the gateway 3 submission documents on the gateway request date.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.gateway3_document_timing`](../../../knowledge/procedures/model.json#L6848); version 0.1.0.

### Source to inspect

- [reg 31(3)](https://www.legislation.gov.uk/uksi/2026/186/regulation/31/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Every** condition below:
  - [Calendar date on which the authority sought the initial gateway 3 prescribed-requirements assessment under regulation 31](../facts.md#gateway3-requested) and [Date the gateway 3 submission documents were sent to the appointed assessor](../facts.md#gateway3-documents-sent) are **the same calendar date**.

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`gateway3_documents_sent`](../facts.md#gateway3-documents-sent) | Date the gateway 3 submission documents were sent to the appointed assessor. | Recorded observation; date |
| [`gateway3_requested`](../facts.md#gateway3-requested) | Calendar date on which the authority sought the initial gateway 3 prescribed-requirements assessment under regulation 31. | Recorded observation; date |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- [Document presence cannot cure sending the prescribed gateway 3 pack a day late.](../../../knowledge/procedures/examples.json#L2026)

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

## Connections to other stages

- [Consultation on proposed Local Plan](new-publication.md) → [Gateway 3: prescribed requirements](new-gateway3.md): Satisfy the cited timing and evidence requirements; see stage rules. (sequence).
- [Gateway 3: prescribed requirements](new-gateway3.md) → [Repeat gateway 3 after remedial work](new-gateway3-repeat.md): One or more prescribed requirements not met. (remedy).
- [Gateway 3: prescribed requirements](new-gateway3.md) → [Submission after gateway 3](new-submission.md): Assessor advises all prescribed requirements met. (decision).

These relationships are descriptive. They are not executable workflow guards.
