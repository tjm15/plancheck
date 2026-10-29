# Regulation 19 publication / Regulation 20 representations

[Review guide](../README.md) · [Input definitions](../facts.md) · [Worked examples](../worked-examples.md)

Generated from model 0.1.0, knowledge date 2026-10-29. Rebuild with `python tools/build_procedure_docs.py`. Authored explanations live in [editorial notes](../editorial-notes.md). Legal mappings await maintainer review.

Regulation 19 is publication of the proposed submission material; regulation 20
is the opportunity to make representations on it. The six-week minimum comes
from regulation 17's definition of the statement of representations procedure.
Here the evaluator can calculate the calendar interval. It relies on a separate
reviewed observation for the contents of the publication pack and notifications.

**Who is involved:** Local planning authority; Representors and public; General and specific consultation bodies

**Stage inputs:** Proposed Local Plan; Sustainability appraisal report

**Stage outputs:** Representations and their identifiers; Statement of representations procedure

Stage inputs/outputs are an indicative map; the individual rules below determine which selected document duties are conditional.

## Assertions at this stage

| Assertion | Status | Evaluator operation |
| --- | --- | --- |
| [Publish the proposed submission documents and representations procedure, and send the required consultation-body notices.](#legacy-publication-pack) | Statutory assertion | Supplied observations only |
| [Allow at least six weeks for representations from publication of the representations procedure.](#legacy-consultation-minimum) | Statutory assertion | Date arithmetic + supplied observations |

<a id="legacy-publication-pack"></a>

## Publish the proposed submission documents and representations procedure, and send the required consultation-body notices.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`legacy.publication_pack`](../../../knowledge/procedures/model.json#L1992); version 0.1.0.

### Source to inspect

- [regs 17 and 19](https://www.legislation.gov.uk/uksi/2012/767/part/6) — Town and Country Planning (Local Planning) (England) Regulations 2012, SI 2012/767; revised Part 6 retrieved 2026-10-29; pre-2026 text as saved (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- **Yes** to: The proposed submission documents and statement of representations procedure have been made available and the regulation 19 consultation-body notices sent ([input `legacy_reg19_publication_and_notices_recorded`](../facts.md#legacy-reg19-publication-and-notices-recorded)).

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`legacy_reg19_publication_and_notices_recorded`](../facts.md#legacy-reg19-publication-and-notices-recorded) | The proposed submission documents and statement of representations procedure have been made available and the regulation 19 consultation-body notices sent. This bundles several publication and notification duties into one reviewed observation. | Recorded observation; boolean |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

### Interpretation and review boundary

This rule compresses document availability, notice contents and recipient duties
into a single observation. Its input definition says what is bundled, but it cannot
show which sub-obligation failed. Decomposing the bundle is a future refinement,
not something the present passing Boolean proves has been implemented.

- Recorded exception: A submission policies map is required if adoption changes the adopted policies map.

**Examples selecting this assertion:**

- No existing example selects this assertion. Its source mapping needs direct review.

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

<a id="legacy-consultation-minimum"></a>

## Allow at least six weeks for representations from publication of the representations procedure.

**Statutory assertion · responsible actor: Local planning authority**

Rule [`legacy.consultation_minimum`](../../../knowledge/procedures/model.json#L2037); version 0.1.0.

### Source to inspect

- [reg 17, definition of statement of representations procedure (c); reg 20(2)](https://www.legislation.gov.uk/uksi/2012/767/regulation/17) — Town and Country Planning (Local Planning) (England) Regulations 2012, SI 2012/767; revised Part 6 retrieved 2026-10-29; pre-2026 text as saved (legal basis)

### When the assertion applies

The case must first match this regime and the represented version. The caller selects this assertion for review; selection does not establish that it is already due.

- No additional fact condition.

### What the evaluator actually requires

- [Selected consultation: representations deadline](../facts.md#consultation-deadline) is at least **42 calendar days** after [Selected consultation: publication date](../facts.md#consultation-published).

**Timing:** publication of representations procedure → representations deadline; calendar days: 42.

<details>
<summary>Evidence inputs and their complete meanings</summary>

| Input | What must be established | Input kind |
| --- | --- | --- |
| [`consultation_deadline`](../facts.md#consultation-deadline) | Last calendar date stated for receipt of representations in the selected consultation. This field must refer to the same consultation as consultation_published. | Recorded observation; date |
| [`consultation_published`](../facts.md#consultation-published) | Calendar date of the publication that starts the selected consultation period. In a legacy case this is publication of the statement of representations procedure; in a new-system case it is the relevant content/evidence or proposed-plan notice. Use a separate case for each consultation. | Recorded observation; date |

</details>

**Results:** a true check yields `satisfied`; a false check yields `not_satisfied`. Unresolved necessary inputs yield `unknown`; a false applicability condition yields `not_applicable`. Three-valued compound logic is explained in the review guide.

**Examples selecting this assertion:**

- [Six-week legacy publication period is sufficient for the duration assertion.](../worked-examples.md#legacy-six-weeks)
- [One day short of six weeks fails the selected statutory duration assertion.](../../../knowledge/procedures/examples.json#L56)
- [Six weeks is insufficient at the new proposed-plan consultation.](../worked-examples.md#new-plan-six-weeks)

**Recorded version interval:** 2026-03-25 to no end encoded, selected by assessment date. **Verification:** primary_text_checked, 2026-10-29; maintainer_review_pending. This metadata records the earlier check, not a fresh independent approval.

## Connections to other stages

- [Preparation and engagement](legacy-preparation.md) → [Regulation 19 publication / Regulation 20 representations](legacy-publication.md): Follow statutory preparation, publication and submission requirements. (sequence).
- [Regulation 19 publication / Regulation 20 representations](legacy-publication.md) → [Regulation 22 submission](legacy-submission.md): Follow statutory preparation, publication and submission requirements. (sequence).

These relationships are descriptive. They are not executable workflow guards.
