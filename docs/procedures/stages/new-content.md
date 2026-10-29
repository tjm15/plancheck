# Content and evidence consultation

[Review guide](../README.md) · [Input definitions](../facts.md) · [Worked examples](../worked-examples.md)

Generated from model 0.1.0, knowledge date 2026-10-29. Rebuild with `python tools/build_procedure_docs.py`. Authored explanations live in [editorial notes](../editorial-notes.md). Legal mappings await maintainer review.

The authority consults on proposed content and evidence after publishing its
scoping summary. The consultation lasts at least six weeks from notice publication.
Its summary must follow the deadline and account for representations, or their
absence. This is preparatory content/evidence consultation; the later consultation
on the proposed plan has an eight-week minimum.

**Who is involved:** Local planning authority; Representors and public; General and specific consultation bodies

**Stage inputs:** Summary of scoping consultation; Proposed content and evidence

**Stage outputs:** Content and evidence consultation notice; Content and evidence consultation summary

Stage inputs/outputs are an indicative map; the individual rules below determine which selected document duties are conditional.

## Assertions at this stage

| Assertion | Status | Evaluator operation |
| --- | --- | --- |
| [Publish content/evidence and notice, notify and invite prescribed classes, no earlier than the day after scoping summary publication.](#new-content-sequence) | Statutory assertion | Date arithmetic + supplied observations |
| [Allow at least six weeks for content and evidence representations from notice publication.](#new-content-minimum) | Statutory assertion | Date arithmetic + supplied observations |
| [Publish consultation summary, including response treatment or absence of responses, no earlier than the following day after the deadline.](#new-content-summary) | Statutory assertion | Date arithmetic + supplied observations |

<a id="new-content-sequence"></a>

## Publish content/evidence and notice, notify and invite prescribed classes, no earlier than the day after scoping summary publication.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.content_sequence`](../../../knowledge/procedures/model.json#L3201); version 0.1.0.

### Source to inspect

- [reg 23(1)-(2)](https://www.legislation.gov.uk/uksi/2026/186/regulation/23/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Every** condition below:
  - **Yes** to: The regulation 23 content/evidence material and notice were made available, appropriate consultation bodies invited and required notifications recorded ([input `content_consultation_notices_recorded`](../facts.md#content-consultation-notices-recorded)).
  - [Selected consultation: publication date](../facts.md#consultation-published) is at least the next calendar day after [Calendar date on which the regulation 22 scoping consultation summary was made available](../facts.md#scoping-summary-published).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`consultation_published`](../facts.md#consultation-published) | Calendar date of the publication that starts the selected consultation period. In a legacy case this is publication of the statement of representations procedure; in a new-system case it is the relevant content/evidence or proposed-plan notice. Use a separate case for each consultation. | Recorded observation; date |
| [`content_consultation_notices_recorded`](../facts.md#content-consultation-notices-recorded) | The regulation 23 content/evidence material and notice were made available, appropriate consultation bodies invited and required notifications recorded. The contents of the published pack require review. | Recorded observation; boolean |
| [`scoping_summary_published`](../facts.md#scoping-summary-published) | Calendar date on which the regulation 22 scoping consultation summary was made available. | Recorded observation; date |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-content-minimum"></a>

## Allow at least six weeks for content and evidence representations from notice publication.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.content_minimum`](../../../knowledge/procedures/model.json#L3254); version 0.1.0.

### Source to inspect

- [reg 23(5), notice definition (b)](https://www.legislation.gov.uk/uksi/2026/186/regulation/23/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- [Selected consultation: representations deadline](../facts.md#consultation-deadline) is at least **42 calendar days** after [Selected consultation: publication date](../facts.md#consultation-published).

**Timing:** content consultation notice publication → representations deadline; calendar days: 42.

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`consultation_deadline`](../facts.md#consultation-deadline) | Last calendar date stated for receipt of representations in the selected consultation. This field must refer to the same consultation as consultation_published. | Recorded observation; date |
| [`consultation_published`](../facts.md#consultation-published) | Calendar date of the publication that starts the selected consultation period. In a legacy case this is publication of the statement of representations procedure; in a new-system case it is the relevant content/evidence or proposed-plan notice. Use a separate case for each consultation. | Recorded observation; date |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- [The new content/evidence consultation minimum is six weeks.](../../../knowledge/procedures/examples.json#L105)

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="new-content-summary"></a>

## Publish consultation summary, including response treatment or absence of responses, no earlier than the following day after the deadline.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`new.content_summary`](../../../knowledge/procedures/model.json#L3301); version 0.1.0.

### Source to inspect

- [reg 24](https://www.legislation.gov.uk/uksi/2026/186/regulation/24/made) — Town and Country Planning (Local Planning) (England) Regulations 2026, SI 2026/186; as made; in force 2026-03-25 (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Every** condition below:
  - **Yes** to: The regulation 24 summary records the content/evidence consultation, main issues and their treatment, including the required statement where no representations were received ([input `content_summary_contents_recorded`](../facts.md#content-summary-contents-recorded)).
  - [Content/evidence summary publication date](../facts.md#content-summary-published) is at least the next calendar day after [Selected consultation: representations deadline](../facts.md#consultation-deadline).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`consultation_deadline`](../facts.md#consultation-deadline) | Last calendar date stated for receipt of representations in the selected consultation. This field must refer to the same consultation as consultation_published. | Recorded observation; date |
| [`content_summary_contents_recorded`](../facts.md#content-summary-contents-recorded) | The regulation 24 summary records the content/evidence consultation, main issues and their treatment, including the required statement where no representations were received. | Recorded observation; boolean |
| [`content_summary_published`](../facts.md#content-summary-published) | Calendar date on which the regulation 24 content/evidence consultation summary was made available. | Recorded observation; date |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

## Connections to other stages

- [Gateway 1: LPA self-assessment](new-gateway1.md) → [Content and evidence consultation](new-content.md): Satisfy the cited timing and evidence requirements; see stage rules. (sequence).
- [Content and evidence consultation](new-content.md) → [Gateway 2: observations and advice](new-gateway2.md): Satisfy the cited timing and evidence requirements; see stage rules. (sequence).

These relationships are descriptive. They are not executable workflow guards.
