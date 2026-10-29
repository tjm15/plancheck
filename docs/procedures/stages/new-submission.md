# Submission after gateway 3

[Review guide](../README.md) · [Input definitions](../facts.md) · [Worked examples](../worked-examples.md)

Generated from model 0.1.0, knowledge date 2026-10-29. Rebuild with `python tools/build_procedure_docs.py`. Authored explanations live in [editorial notes](../editorial-notes.md). Legal mappings await maintainer review.

Successful prescribed-requirements advice triggers submission under PCPA section
15D(1). The examination submission pack under regulation 34 differs from the
gateway 3 pack, even where document names overlap. The two sets of supply facts
must not be treated as interchangeable. The package records publication of the
submission date and material, with detailed mechanics still requiring review.

**Who is involved:** Local planning authority; Secretary of State

**Stage inputs:** Gateway 3 completion statement; Proposed Local Plan

**Stage outputs:** Examination library

Stage inputs/outputs are an indicative map; the individual rules below determine which selected document duties are conditional.

## Assertions at this stage

| Assertion | Status | Evaluator operation |
| --- | --- | --- |
| [Submit the proposed Local Plan when the appointed person advises that prescribed requirements are met.](#new-submit-after-gateway3) | Statutory assertion | Supplied observations only |
| [Provide Proposed or submission policies map.](#new-submission-policies-map) | Statutory assertion | Supplied observations only |
| [Provide Gateway 3 completion statement.](#new-submission-gateway3-completion) | Statutory assertion | Supplied observations only |
| [Provide Summary of consultation and engagement.](#new-submission-engagement-summary) | Statutory assertion | Supplied observations only |
| [Provide Proposed-plan consultation summary.](#new-submission-plan-summary) | Statutory assertion | Supplied observations only |
| [Provide Representations on conformity with operative SDS.](#new-submission-sds-representations) | Statutory assertion | Supplied observations only |
| [Provide Statement of compliance.](#new-submission-compliance) | Statutory assertion | Supplied observations only |
| [Provide Statement of soundness.](#new-submission-soundness) | Statutory assertion | Supplied observations only |
| [Provide Environmental report under SEA reg 12.](#new-submission-environmental-report) | Statutory assertion | Supplied observations only |
| [Provide SEA screening determination reasons under reg 9(3).](#new-submission-screening-reasons) | Statutory assertion | Supplied observations only |
| [Provide Supporting evidence selected by the authority.](#new-submission-supporting-evidence) | Statutory assertion | Supplied observations only |
| [Publish the submission date and specified documents, and notify requesters and other appropriate persons.](#new-submission-publicity) | Statutory assertion | Supplied observations only |

<a id="new-submit-after-gateway3"></a>

## Submit the proposed Local Plan when the appointed person advises that prescribed requirements are met.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.submit_after_gateway3`](../../../knowledge/procedures/model.json#L5337); version 0.1.0.

### Source to inspect

- [s 15D(1)](https://www.legislation.gov.uk/ukpga/2004/5/section/15D) — PCPA 2004 section 15D; revised text retrieved 2026-10-29 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- **Yes** to: Assessor advises that all prescribed gateway 3 requirements are met ([input `assessor_all_prescribed_requirements_met`](../facts.md#assessor-all-prescribed-requirements-met)).

### What the evaluator actually requires

- **Yes** to: Plan submitted for examination ([input `plan_submitted`](../facts.md#plan-submitted)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`assessor_all_prescribed_requirements_met`](../facts.md#assessor-all-prescribed-requirements-met) | The appointed assessor advises that every reg 32 requirement is met. This records the advice, not an application-generated soundness or legal-compliance certificate. | Reviewer judgement; boolean |
| [`plan_submitted`](../facts.md#plan-submitted) | The proposed Local Plan has been submitted to the Secretary of State for independent examination under PCPA section 15D(1). | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

Gateway 3 success is not a soundness recommendation or adoption.


**Examples selecting this assertion:**

- [Gateway 3 success triggers submission; it cannot establish the examination soundness finding.](../worked-examples.md#gateway3-not-soundness-verdict)
- [Unmet requirements require remedy and reassessment; submission trigger is not activated.](../../../knowledge/procedures/examples.json#L548)

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-submission-policies-map"></a>

## Provide Proposed or submission policies map.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.submission_policies_map`](../../../knowledge/procedures/model.json#L5380); version 0.1.0.

### Source to inspect

- [reg 34(1)(a)](https://www.legislation.gov.uk/uksi/2026/186/regulation/34/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: The reviewer has verified that the proposed or submission policies map was included in the new-system examination submission ([input `new_submission_policies_map_provided`](../facts.md#new-submission-policies-map-provided)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`new_submission_policies_map_provided`](../facts.md#new-submission-policies-map-provided) | The reviewer has verified that the proposed or submission policies map was included in the new-system examination submission. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-submission-gateway3-completion"></a>

## Provide Gateway 3 completion statement.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.submission_gateway3_completion`](../../../knowledge/procedures/model.json#L5421); version 0.1.0.

### Source to inspect

- [reg 34(1)(b)](https://www.legislation.gov.uk/uksi/2026/186/regulation/34/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: The reviewer has verified that the gateway 3 completion statement was included in the new-system examination submission ([input `new_submission_gateway3_completion_provided`](../facts.md#new-submission-gateway3-completion-provided)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`new_submission_gateway3_completion_provided`](../facts.md#new-submission-gateway3-completion-provided) | The reviewer has verified that the gateway 3 completion statement was included in the new-system examination submission. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-submission-engagement-summary"></a>

## Provide Summary of consultation and engagement.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.submission_engagement_summary`](../../../knowledge/procedures/model.json#L5462); version 0.1.0.

### Source to inspect

- [reg 34(1)(c)](https://www.legislation.gov.uk/uksi/2026/186/regulation/34/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: The reviewer has verified that the summary of consultation and engagement was included in the new-system examination submission ([input `new_submission_engagement_summary_provided`](../facts.md#new-submission-engagement-summary-provided)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`new_submission_engagement_summary_provided`](../facts.md#new-submission-engagement-summary-provided) | The reviewer has verified that the summary of consultation and engagement was included in the new-system examination submission. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-submission-plan-summary"></a>

## Provide Proposed-plan consultation summary.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.submission_plan_summary`](../../../knowledge/procedures/model.json#L5503); version 0.1.0.

### Source to inspect

- [reg 34(1)(d)](https://www.legislation.gov.uk/uksi/2026/186/regulation/34/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: The reviewer has verified that the proposed-plan consultation summary was included in the new-system examination submission ([input `new_submission_plan_summary_provided`](../facts.md#new-submission-plan-summary-provided)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`new_submission_plan_summary_provided`](../facts.md#new-submission-plan-summary-provided) | The reviewer has verified that the proposed-plan consultation summary was included in the new-system examination submission. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-submission-sds-representations"></a>

## Provide Representations on conformity with operative SDS.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.submission_sds_representations`](../../../knowledge/procedures/model.json#L5544); version 0.1.0.

### Source to inspect

- [reg 34(1)(e)](https://www.legislation.gov.uk/uksi/2026/186/regulation/34/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- **Every** condition below:
  - **Yes** to: A spatial development strategy is operative in relation to the plan area so that the selected regulation 28 conformity/document requirements apply ([input `operative_sds`](../facts.md#operative-sds)).
  - **Yes** to: At least one conformity representation was received under regulation 28; copies must be included where the selected pack requires them ([input `sds_representations_received`](../facts.md#sds-representations-received)).

### What the evaluator actually requires

- **Yes** to: The reviewer has verified that the representations on conformity with operative SDS was included in the new-system examination submission ([input `new_submission_sds_representations_provided`](../facts.md#new-submission-sds-representations-provided)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`new_submission_sds_representations_provided`](../facts.md#new-submission-sds-representations-provided) | The reviewer has verified that the representations on conformity with operative SDS was included in the new-system examination submission. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission. | Recorded observation; boolean |
| [`operative_sds`](../facts.md#operative-sds) | A spatial development strategy is operative in relation to the plan area so that the selected regulation 28 conformity/document requirements apply. | Recorded observation; boolean |
| [`sds_representations_received`](../facts.md#sds-representations-received) | At least one conformity representation was received under regulation 28; copies must be included where the selected pack requires them. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-submission-compliance"></a>

## Provide Statement of compliance.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.submission_compliance`](../../../knowledge/procedures/model.json#L5596); version 0.1.0.

### Source to inspect

- [reg 34(1)(f)](https://www.legislation.gov.uk/uksi/2026/186/regulation/34/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: The reviewer has verified that the statement of compliance was included in the new-system examination submission ([input `new_submission_compliance_provided`](../facts.md#new-submission-compliance-provided)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`new_submission_compliance_provided`](../facts.md#new-submission-compliance-provided) | The reviewer has verified that the statement of compliance was included in the new-system examination submission. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-submission-soundness"></a>

## Provide Statement of soundness.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.submission_soundness`](../../../knowledge/procedures/model.json#L5637); version 0.1.0.

### Source to inspect

- [reg 34(1)(g)](https://www.legislation.gov.uk/uksi/2026/186/regulation/34/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: The reviewer has verified that the statement of soundness was included in the new-system examination submission ([input `new_submission_soundness_provided`](../facts.md#new-submission-soundness-provided)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`new_submission_soundness_provided`](../facts.md#new-submission-soundness-provided) | The reviewer has verified that the statement of soundness was included in the new-system examination submission. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-submission-environmental-report"></a>

## Provide Environmental report under SEA reg 12.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.submission_environmental_report`](../../../knowledge/procedures/model.json#L5678); version 0.1.0.

### Source to inspect

- [reg 34(1)(h)](https://www.legislation.gov.uk/uksi/2026/186/regulation/34/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- **Yes** to: An environmental report has been prepared under regulation 12 of the SEA Regulations 2004 ([input `environmental_report_prepared`](../facts.md#environmental-report-prepared)).

### What the evaluator actually requires

- **Yes** to: The reviewer has verified that the environmental report under SEA reg 12 was included in the new-system examination submission ([input `new_submission_environmental_report_provided`](../facts.md#new-submission-environmental-report-provided)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`environmental_report_prepared`](../facts.md#environmental-report-prepared) | An environmental report has been prepared under regulation 12 of the SEA Regulations 2004. This triggers the selected pack’s report-copy requirement; it does not decide whether an assessment should have been undertaken. | Recorded observation; boolean |
| [`new_submission_environmental_report_provided`](../facts.md#new-submission-environmental-report-provided) | The reviewer has verified that the environmental report under SEA reg 12 was included in the new-system examination submission. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-submission-screening-reasons"></a>

## Provide SEA screening determination reasons under reg 9(3).

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.submission_screening_reasons`](../../../knowledge/procedures/model.json#L5720); version 0.1.0.

### Source to inspect

- [reg 34(1)(i)](https://www.legislation.gov.uk/uksi/2026/186/regulation/34/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- **Yes** to: The authority has made the SEA regulation 9(1) determination that the plan is unlikely to have significant environmental effects, with a reasons statement under regulation 9(3) ([input `sea_no_significant_effects_determination`](../facts.md#sea-no-significant-effects-determination)).

### What the evaluator actually requires

- **Yes** to: The reviewer has verified that the sEA screening determination reasons under reg 9(3) was included in the new-system examination submission ([input `new_submission_screening_reasons_provided`](../facts.md#new-submission-screening-reasons-provided)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`new_submission_screening_reasons_provided`](../facts.md#new-submission-screening-reasons-provided) | The reviewer has verified that the sEA screening determination reasons under reg 9(3) was included in the new-system examination submission. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission. | Recorded observation; boolean |
| [`sea_no_significant_effects_determination`](../facts.md#sea-no-significant-effects-determination) | The authority has made the SEA regulation 9(1) determination that the plan is unlikely to have significant environmental effects, with a reasons statement under regulation 9(3). This records the determination, not this evaluator’s environmental judgement. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-submission-supporting-evidence"></a>

## Provide Supporting evidence selected by the authority.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.submission_supporting_evidence`](../../../knowledge/procedures/model.json#L5762); version 0.1.0.

### Source to inspect

- [reg 34(1)(j)](https://www.legislation.gov.uk/uksi/2026/186/regulation/34/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: The reviewer has verified that the supporting evidence selected by the authority was included in the new-system examination submission ([input `new_submission_supporting_evidence_provided`](../facts.md#new-submission-supporting-evidence-provided)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`new_submission_supporting_evidence_provided`](../facts.md#new-submission-supporting-evidence-provided) | The reviewer has verified that the supporting evidence selected by the authority was included in the new-system examination submission. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-submission-publicity"></a>

## Publish the submission date and specified documents, and notify requesters and other appropriate persons.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.submission_publicity`](../../../knowledge/procedures/model.json#L5803); version 0.1.0.

### Source to inspect

- [reg 34(2)](https://www.legislation.gov.uk/uksi/2026/186/regulation/34/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: The authority published the submission date and prescribed submission material and notified requesters and other appropriate persons under regulation 34 ([input `new_submission_publicity_recorded`](../facts.md#new-submission-publicity-recorded)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`new_submission_publicity_recorded`](../facts.md#new-submission-publicity-recorded) | The authority published the submission date and prescribed submission material and notified requesters and other appropriate persons under regulation 34. Exact availability and recipient requirements require review. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

## Connections to other stages

- [Gateway 3: prescribed requirements](new-gateway3.md) → [Submission after gateway 3](new-submission.md): Assessor advises all prescribed requirements met. (decision).
- [Repeat gateway 3 after remedial work](new-gateway3-repeat.md) → [Submission after gateway 3](new-submission.md): Assessor advises all prescribed requirements met. (decision).
- [Submission after gateway 3](new-submission.md) → [Independent examination and hearings](new-examination.md): Plan submitted; Secretary of State appoints examiner. (sequence).

These relationships are descriptive. They are not executable workflow guards.
