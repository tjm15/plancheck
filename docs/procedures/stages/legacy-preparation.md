# Preparation and engagement

[Review guide](../README.md) · [Input definitions](../facts.md) · [Worked examples](../worked-examples.md)

Generated from model 0.1.0, knowledge date 2026-10-29. Rebuild with `python tools/build_procedure_docs.py`. Authored explanations live in [editorial notes](../editorial-notes.md). Legal mappings await maintainer review.

The authority prepares its plan and engages the appropriate bodies and people.
The model represents the invitation and consideration duties in regulation 18.
It does not give this stage an automatic six-week minimum. The later publication
consultation has a different legal basis and a prescribed minimum. Evidence of
engagement and evidence that responses influenced consideration are different
inputs; an invitation register cannot establish both.

**Who is involved:** Local planning authority; General and specific consultation bodies; Representors and public

**Stage inputs:** No document types listed.

**Stage outputs:** Supporting evidence selected by the authority

Stage inputs/outputs are an indicative map; the individual rules below determine which selected document duties are conditional.

## Assertions at this stage

| Assertion | Status | Evaluator operation |
| --- | --- | --- |
| [Invite the Regulation 18 consultation classes and take their representations into account.](#legacy-engagement) | Statutory assertion | Supplied observations only |

<a id="legacy-engagement"></a>

## Invite the Regulation 18 consultation classes and take their representations into account.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`legacy.engagement`](../../../knowledge/procedures/model.json#L1941); version 0.1.0.

### Source to inspect

- [reg 18(1)-(3)](https://www.legislation.gov.uk/uksi/2012/767/regulation/18) — Town and Country Planning (Local Planning) (England) Regulations 2012, SI 2012/767; revised Part 6 retrieved 2026-10-29; pre-2026 text as saved (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Every** condition below:
  - **Yes** to: The authority has identified the appropriate consultation bodies and residents/businesses under regulation 18 and recorded the required invitations to make representations ([input `legacy_reg18_invitations_recorded`](../facts.md#legacy-reg18-invitations-recorded)).
  - **Yes** to: The authority has considered the representations received in preparing the plan; the reviewer has checked the response record rather than merely counted submissions ([input `legacy_reg18_responses_considered`](../facts.md#legacy-reg18-responses-considered)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`legacy_reg18_invitations_recorded`](../facts.md#legacy-reg18-invitations-recorded) | The authority has identified the appropriate consultation bodies and residents/businesses under regulation 18 and recorded the required invitations to make representations. | Recorded observation; boolean |
| [`legacy_reg18_responses_considered`](../facts.md#legacy-reg18-responses-considered) | The authority has considered the representations received in preparing the plan; the reviewer has checked the response record rather than merely counted submissions. | Reviewer judgement; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

No fixed six-week minimum is imposed by reg 18 itself; SCI and other duties require separate assessment.


**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

## Connections to other stages

- [Preparation and engagement](legacy-preparation.md) → [Regulation 19 publication / Regulation 20 representations](legacy-publication.md): Follow statutory preparation, publication and submission requirements. (sequence).

These relationships are descriptive. They are not executable workflow guards.
