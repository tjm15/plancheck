# Repeat gateway 3 after remedial work

[Review guide](../README.md) · [Input definitions](../facts.md) · [Worked examples](../worked-examples.md)

Generated from model 0.1.0, knowledge date 2026-10-29. Rebuild with `python tools/build_procedure_docs.py`. Authored explanations live in [editorial notes](../editorial-notes.md). Legal mappings await maintainer review.

A failed gateway 3 leads to work addressing the stated reasons and a further
assessment with updated documents. The process can repeat. The current executable
rule compresses the remedy/request/update/iteration duties into one reviewed
Boolean. The graph shows a loop, but the evaluator does not store or replay each
assessment cycle. This is a specific implementation limitation visible to review.

**Who is involved:** Local planning authority; Secretary of State appointed gateway assessor

**Stage inputs:** Reasoned gateway 3 conclusions for each requirement

**Stage outputs:** Reasoned gateway 3 conclusions for each requirement; Gateway 3 completion statement

Stage inputs/outputs are an indicative map; the individual rules below determine which selected document duties are conditional.

## Assertions at this stage

| Assertion | Status | Evaluator operation |
| --- | --- | --- |
| [Remedy failed prescribed requirements and seek further assessment with updated documents, repeating as necessary.](#new-gateway3-repeat) | Statutory assertion | Supplied observations only |

<a id="new-gateway3-repeat"></a>

## Remedy failed prescribed requirements and seek further assessment with updated documents, repeating as necessary.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.gateway3_repeat`](../../../knowledge/procedures/model.json#L5287); version 0.1.0.

### Source to inspect

- [reg 33(1)-(9)](https://www.legislation.gov.uk/uksi/2026/186/regulation/33/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- **No** to: Assessor advises that all prescribed gateway 3 requirements are met ([input `assessor_all_prescribed_requirements_met`](../facts.md#assessor-all-prescribed-requirements-met)).

### What the evaluator actually requires

- **Yes** to: Following failed gateway 3 advice, the authority addressed the reasons for failure and sought further assessment with updated prescribed documents under regulation 33, as soon as reasonably practicable and again if required ([input `gateway3_remedy_and_repeat_recorded`](../facts.md#gateway3-remedy-and-repeat-recorded)).

**Timing:** failed gateway advice → remedy then repeat request; as soon as reasonably practicable.

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`assessor_all_prescribed_requirements_met`](../facts.md#assessor-all-prescribed-requirements-met) | The appointed assessor advises that every reg 32 requirement is met. This records the advice, not an application-generated soundness or legal-compliance certificate. | Reviewer judgement; boolean |
| [`gateway3_remedy_and_repeat_recorded`](../facts.md#gateway3-remedy-and-repeat-recorded) | Following failed gateway 3 advice, the authority addressed the reasons for failure and sought further assessment with updated prescribed documents under regulation 33, as soon as reasonably practicable and again if required. This Boolean summarises the loop; the evaluator does not track its individual iterations. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

One Boolean currently stands in for a multi-step legal process. It is reviewable
as a recorded conclusion, but unsuitable for automatically tracking a real remedial
programme until each iteration, reason, action and resubmission is represented.


**Examples selecting this assertion:**

- [Unmet requirements require remedy and reassessment; submission trigger is not activated.](../../../knowledge/procedures/examples.json#L548)

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

## Connections to other stages

- [Gateway 3: prescribed requirements](new-gateway3.md) → [Repeat gateway 3 after remedial work](new-gateway3-repeat.md): One or more prescribed requirements not met. (remedy).
- [Repeat gateway 3 after remedial work](new-gateway3-repeat.md) → [Repeat gateway 3 after remedial work](new-gateway3-repeat.md): Further assessment again finds unmet prescribed requirements. (remedy).
- [Repeat gateway 3 after remedial work](new-gateway3-repeat.md) → [Submission after gateway 3](new-submission.md): Assessor advises all prescribed requirements met. (decision).

These relationships are descriptive. They are not executable workflow guards.
