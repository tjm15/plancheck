# Regulation 22 submission

[Review guide](../README.md) · [Input definitions](../facts.md) · [Worked examples](../worked-examples.md)

Generated from model 0.1.0, knowledge date 2026-10-29. Rebuild with `python tools/build_procedure_docs.py`. Authored explanations live in [editorial notes](../editorial-notes.md). Legal mappings await maintainer review.

The authority submits the plan and the regulation 22 supporting documents to the
Secretary of State. Some items have conditions: the policies map depends on a
change to the adopted map, and representations depend on their receipt. The
model also records statutory readiness and publication/notification obligations.
Each document Boolean records supply; it does not assess its substance. The
2012 instrument is applied through the 2026 saving, using revised rather than
unqualified as-made text.

**Who is involved:** Local planning authority; Secretary of State

**Stage inputs:** Proposed Local Plan; Sustainability appraisal report; Legacy Regulation 22 consultation statement; Representations and their identifiers

**Stage outputs:** Examination library

Stage inputs/outputs are an indicative map; the individual rules below determine which selected document duties are conditional.

## Assertions at this stage

| Assertion | Status | Evaluator operation |
| --- | --- | --- |
| [Submit only after relevant regulatory requirements are met and the authority considers the plan ready for examination.](#legacy-submission-readiness) | Statutory assertion | Supplied observations only |
| [Provide Sustainability appraisal report.](#legacy-submission-sa) | Statutory assertion | Supplied observations only |
| [Provide Proposed or submission policies map.](#legacy-submission-map) | Statutory assertion | Supplied observations only |
| [Provide Legacy Regulation 22 consultation statement.](#legacy-submission-consultation) | Statutory assertion | Supplied observations only |
| [Provide Representations and their identifiers.](#legacy-submission-representations) | Statutory assertion | Supplied observations only |
| [Provide Supporting evidence selected by the authority.](#legacy-submission-evidence) | Statutory assertion | Supplied observations only |
| [Make submission documents available and notify consultation bodies and persons who requested notification.](#legacy-submission-publicity) | Statutory assertion | Supplied observations only |

<a id="legacy-submission-readiness"></a>

## Submit only after relevant regulatory requirements are met and the authority considers the plan ready for examination.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`legacy.submission_readiness`](../../../knowledge/procedures/model.json#L2171); version 0.1.0.

### Source to inspect

- [s 20(1)-(3)](https://www.legislation.gov.uk/ukpga/2004/5/section/20/2026-03-24) — PCPA 2004 section 20 immediately before commencement; point in time 2026-03-24, read with SI 2026/169 Sch 1 para 2 (legal basis)
- [Sch 1 paras 2,4](https://www.legislation.gov.uk/uksi/2026/169/schedule/1) — LURA 2023 Commencement No. 11 and Saving and Transitional Provisions Regulations 2026, SI 2026/169; revised Schedule 1 including SI 2026/333 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Every** condition below:
  - **Yes** to: The reviewer has established compliance with the relevant regulatory requirements referred to by saved PCPA section 20(2)(a), with a record of which requirements were considered ([input `legacy_regulatory_requirements_met`](../facts.md#legacy-regulatory-requirements-met)).
  - **Yes** to: The authority has recorded that it considers the legacy plan ready for independent examination under saved PCPA section 20(2)(b) ([input `lpa_ready_for_examination`](../facts.md#lpa-ready-for-examination)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`legacy_regulatory_requirements_met`](../facts.md#legacy-regulatory-requirements-met) | The reviewer has established compliance with the relevant regulatory requirements referred to by saved PCPA section 20(2)(a), with a record of which requirements were considered. This package does not derive that finding from its selected rules. | Reviewer judgement; boolean |
| [`lpa_ready_for_examination`](../facts.md#lpa-ready-for-examination) | The authority has recorded that it considers the legacy plan ready for independent examination under saved PCPA section 20(2)(b). | Reviewer judgement; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="legacy-submission-sa"></a>

## Provide Sustainability appraisal report.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`legacy.submission_sa`](../../../knowledge/procedures/model.json#L2227); version 0.1.0.

### Source to inspect

- [reg 22(1)(a)](https://www.legislation.gov.uk/uksi/2012/767/regulation/22) — Town and Country Planning (Local Planning) (England) Regulations 2012, SI 2012/767; revised Part 6 retrieved 2026-10-29; pre-2026 text as saved (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: The reviewer has verified that the sustainability appraisal report was included in the legacy examination submission ([input `legacy_submission_sa_report_provided`](../facts.md#legacy-submission-sa-report-provided)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`legacy_submission_sa_report_provided`](../facts.md#legacy-submission-sa-report-provided) | The reviewer has verified that the sustainability appraisal report was included in the legacy examination submission. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- [Late date does not silently migrate a legacy plan to the new regime.](../../../knowledge/procedures/examples.json#L871)

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="legacy-submission-map"></a>

## Provide Proposed or submission policies map.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`legacy.submission_map`](../../../knowledge/procedures/model.json#L2268); version 0.1.0.

### Source to inspect

- [reg 22(1)(b)](https://www.legislation.gov.uk/uksi/2012/767/regulation/22) — Town and Country Planning (Local Planning) (England) Regulations 2012, SI 2012/767; revised Part 6 retrieved 2026-10-29; pre-2026 text as saved (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- **Yes** to: Adoption of this legacy plan would change the adopted policies map ([input `adoption_changes_policies_map`](../facts.md#adoption-changes-policies-map)).

### What the evaluator actually requires

- **Yes** to: The reviewer has verified that the proposed or submission policies map was included in the legacy examination submission ([input `legacy_submission_policies_map_provided`](../facts.md#legacy-submission-policies-map-provided)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`adoption_changes_policies_map`](../facts.md#adoption-changes-policies-map) | Adoption of this legacy plan would change the adopted policies map. This is the condition for supplying a submission policies map under regulation 22(1)(b). | Recorded observation; boolean |
| [`legacy_submission_policies_map_provided`](../facts.md#legacy-submission-policies-map-provided) | The reviewer has verified that the proposed or submission policies map was included in the legacy examination submission. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- [Legacy submission policies map condition can be false.](../../../knowledge/procedures/examples.json#L593)
- [Unknown spatial-change condition prevents a definitive map requirement result.](../../../knowledge/procedures/examples.json#L642)

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="legacy-submission-consultation"></a>

## Provide Legacy Regulation 22 consultation statement.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`legacy.submission_consultation`](../../../knowledge/procedures/model.json#L2310); version 0.1.0.

### Source to inspect

- [reg 22(1)(c)](https://www.legislation.gov.uk/uksi/2012/767/regulation/22) — Town and Country Planning (Local Planning) (England) Regulations 2012, SI 2012/767; revised Part 6 retrieved 2026-10-29; pre-2026 text as saved (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: The reviewer has verified that the legacy Regulation 22 consultation statement was included in the legacy examination submission ([input `legacy_submission_consultation_statement_provided`](../facts.md#legacy-submission-consultation-statement-provided)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`legacy_submission_consultation_statement_provided`](../facts.md#legacy-submission-consultation-statement-provided) | The reviewer has verified that the legacy Regulation 22 consultation statement was included in the legacy examination submission. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

The consultation statement must record no representations where none were made; supporting documents depend on the authority’s judgement.


**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="legacy-submission-representations"></a>

## Provide Representations and their identifiers.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`legacy.submission_representations`](../../../knowledge/procedures/model.json#L2351); version 0.1.0.

### Source to inspect

- [reg 22(1)(d)](https://www.legislation.gov.uk/uksi/2012/767/regulation/22) — Town and Country Planning (Local Planning) (England) Regulations 2012, SI 2012/767; revised Part 6 retrieved 2026-10-29; pre-2026 text as saved (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- **Yes** to: At least one representation was received under legacy regulation 20; the submission-pack representation duty is assessed against that record ([input `reg20_representations_received`](../facts.md#reg20-representations-received)).

### What the evaluator actually requires

- **Yes** to: The reviewer has verified that the representations and their identifiers was included in the legacy examination submission ([input `legacy_submission_representations_provided`](../facts.md#legacy-submission-representations-provided)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`legacy_submission_representations_provided`](../facts.md#legacy-submission-representations-provided) | The reviewer has verified that the representations and their identifiers was included in the legacy examination submission. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission. | Recorded observation; boolean |
| [`reg20_representations_received`](../facts.md#reg20-representations-received) | At least one representation was received under legacy regulation 20; the submission-pack representation duty is assessed against that record. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="legacy-submission-evidence"></a>

## Provide Supporting evidence selected by the authority.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`legacy.submission_evidence`](../../../knowledge/procedures/model.json#L2393); version 0.1.0.

### Source to inspect

- [reg 22(1)(e)](https://www.legislation.gov.uk/uksi/2012/767/regulation/22) — Town and Country Planning (Local Planning) (England) Regulations 2012, SI 2012/767; revised Part 6 retrieved 2026-10-29; pre-2026 text as saved (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: The reviewer has verified that the supporting evidence selected by the authority was included in the legacy examination submission ([input `legacy_submission_supporting_evidence_provided`](../facts.md#legacy-submission-supporting-evidence-provided)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`legacy_submission_supporting_evidence_provided`](../facts.md#legacy-submission-supporting-evidence-provided) | The reviewer has verified that the supporting evidence selected by the authority was included in the legacy examination submission. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

The consultation statement must record no representations where none were made; supporting documents depend on the authority’s judgement.


**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="legacy-submission-publicity"></a>

## Make submission documents available and notify consultation bodies and persons who requested notification.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`legacy.submission_publicity`](../../../knowledge/procedures/model.json#L2434); version 0.1.0.

### Source to inspect

- [reg 22(3)](https://www.legislation.gov.uk/uksi/2012/767/regulation/22) — Town and Country Planning (Local Planning) (England) Regulations 2012, SI 2012/767; revised Part 6 retrieved 2026-10-29; pre-2026 text as saved (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: The reviewer has checked regulation 22(3) availability and notifications, including required recipients, the practicability qualification and the as-soon-as-reasonably-practicable timing ([input `legacy_submission_publicity_recorded`](../facts.md#legacy-submission-publicity-recorded)).

**Timing:** submission → publication and notices; as soon as reasonably practicable.

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`legacy_submission_publicity_recorded`](../facts.md#legacy-submission-publicity-recorded) | The reviewer has checked regulation 22(3) availability and notifications, including required recipients, the practicability qualification and the as-soon-as-reasonably-practicable timing. Finding an examination-library webpage alone is insufficient. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

- Recorded exception: Reg 22(3)(a)(iii): availability of representations/supporting documents qualified by practicability.

**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

## Connections to other stages

- [Regulation 19 publication / Regulation 20 representations](legacy-publication.md) → [Regulation 22 submission](legacy-submission.md): Follow statutory preparation, publication and submission requirements. (sequence).
- [Regulation 22 submission](legacy-submission.md) → [Independent examination and hearings](legacy-examination.md): Follow statutory preparation, publication and submission requirements. (sequence).
- [Pre-examination preparation](legacy-readiness.md) → [Regulation 22 submission](legacy-submission.md): Checklist supports readiness; not a statutory gateway. (advisory).

These relationships are descriptive. They are not executable workflow guards.
