# Reading and reviewing the Local Plan procedural model

The package represents **claims about procedure**, with the source, conditions and
evidence needed to assess each claim. Read this guide and the linked examples
before opening the JSON. You can review the legal mapping without running Python.

Start with [the gateway 2 worked example](worked-examples.md#gateway2-no-draft-plan).
It shows the central distinction: a recommended draft plan can be absent while a
separate statutory duty to supply necessary material is satisfied on the recorded
authority judgement. Every result links to the actual assertion, its plain-language
test and its official source.

## Where to look

| Question | Read |
| --- | --- |
| What is the model claiming, and what can it actually calculate? | The explanation below |
| What happens at a particular stage? | [Stage index](stage-index.md): choose the saved legacy or 2026 route |
| Why does a particular example produce that answer? | [Ten worked examples](worked-examples.md), with actual inputs and evaluated results |
| What does an input really mean? | [Evidence input register](facts.md), also available inside each rule's expandable input table |
| Where did the legal interpretations come from? | [Source-recovery and verification record](../procedural-source-review.md), then each rule's official provision links |
| How are the data and evaluator maintained or run? | [Technical package documentation](../../knowledge/procedures/README.md) |

## The three layers to keep in mind

| Layer | Concrete example | What it establishes |
| --- | --- | --- |
| A claim derived from a source | At gateway 2, send material the authority considers necessary on the request date | An interpretation to verify against regulation 26(3) |
| Observations about a plan | The authority records its necessity judgement; material was sent on 1 October; advice was requested on 1 October | Attributable evidence supplied by the case author |
| An evaluated assertion | The dates match and the necessity/supply observation is Yes | The encoded test is satisfied on those observations |

The evaluator does not read the authority's documents and discover the observations
for itself. It also does not independently reproduce an Inspector's judgement. The
source mapping, the truth of an observation and the correctness of a computation
are three separate things to review.

A **stage** groups related work. A **rule** is one selected assertion to assess.
A **fact** is an input, such as a publication date or the authority's recorded
judgement. An **evidence record** identifies the document, decision or register
supporting that input. An **output** is an artefact or finding produced at a stage.
The JSON stores these relationships with stable IDs so that later PlanCheck
components can refer to them.

## How the two procedures differ

This is an orientation to the represented spine, not an assertion that every
sub-obligation has already been encoded. Follow the stage links for the exact scope.

| Procedural question | Saved legacy route | 2026 route |
| --- | --- | --- |
| How is preparation organised? | Regulation 18 engagement; subsequent publication and submission stages | Timetable, intention notice, scoping and an LPA self-assessment at gateway 1 |
| When is material consulted upon? | Proposed submission material under regulations 19–20; selected minimum is six weeks | Content/evidence consultation has six weeks; subsequent proposed-plan consultation has eight weeks |
| What happens before examination? | Pre-examination checklist in guidance; saved statutory readiness and regulation 22 submission duties | Appointed-assessor gateway 2 advice, then gateway 3 prescribed-requirements assessment and possible repeats |
| Is a draft plan mandatory at gateway 2? | No equivalent statutory gateway | Supply necessary material as judged by the authority; emerging draft plan/map detail is recommended supporting practice |
| Is a statement of soundness an examiner's finding? | A document or authority argument does not itself decide soundness | The mandatory gateway 3 statement and the examiner's later soundness conclusion remain separate |
| What is needed for the statutory hearing entitlement? | Representation seeking change, plus request to be heard | Representation, plus request to be heard |
| Do curative main-modification recommendations require an LPA request? | The saved provision does | The new provision has no equivalent request condition |
| How is a pause treated? | Qualified guidance on usual duration | Statutory notice, response and end-of-pause decision conditions, with a prescribed six-month maximum |

[Full saved legacy stages](stage-index.md#saved-legacy-system) ·
[Full 2026 stages](stage-index.md#2026-system).

## One assertion, read from source to result

Open [gateway 2: necessary material](stages/new-gateway2.md#new-gateway2-necessary-material).
The page presents the following audit trail in order:

1. **Claim and status.** The LPA must send the assessor what it considers necessary,
   on the request date. This is labelled statutory and assigned to the LPA.
2. **Official provision.** Regulation 26(3), with the legislation version. Read it
   and decide whether the stated claim fairly represents it.
3. **Applicability.** The case must be in the 2026 route and represented time
   interval. The caller has selected this stage/assertion for review.
4. **Executable meaning.** A reviewer-supplied necessity/supply observation must be
   Yes, and the request and transmission dates must be the same calendar date.
5. **Evidence definitions.** Expand the input table to see exactly what each
   observation means and which one requires judgement.
6. **Example and output.** The worked case supplies Yes and matching dates, so the
   selected statutory assertion is satisfied. Its absent draft plan/map produce
   advisory gaps under separate rules.

You can disagree at any of those layers. For instance, a mistaken reading of the
provision calls for a rule correction; an unsupported necessity judgement calls
for better case evidence; incorrect date comparison calls for a software fix.
A passing example cannot settle either of the first two disagreements.

## What the program does, and what remains supplied

| Operation | Current implementation |
| --- | --- |
| Compare two calendar dates | Calculates their difference, including the 42-day and 56-day minima and day-after/same-day requirements |
| Combine known, false and missing observations | Evaluates the explicit conditions using three-valued logic |
| Select a procedural regime | Uses declared legal basis, scope and evidenced saving facts in `select_regime`; this routing logic is Python code rather than a rule in the JSON |
| Determine which obligations are already due | Caller selects assertions; stage progression and due dates are not inferred |
| Decide whether a document was supplied | Accepts the reviewer’s evidence-backed observation |
| Decide whether content is adequate, a plan is sound or the authority had regard to advice | Accepts an attributable judgement; does not make the substantive finding |
| Calculate calendar months, years or working days | Accepts a reviewed period assessment; does not approximate these as fixed day counts |
| Check several inputs are mutually consistent | No general contradiction check: a supplied assessor finding and a supplied document inventory could conflict |
| Track repeated gateway 3 assessments | Records a reviewed summary and descriptive loop; does not execute or store each iteration |

The stage pages make this boundary visible for every assertion. An operation marked
“supplied observations only” can still be a useful source-linked review record,
but it should not be described as an independently automated legal check.

## How to read the possible answers

| Answer | Interpretation |
| --- | --- |
| `satisfied` | The selected encoded assertion follows from the supplied observations |
| `not_satisfied` | A selected statutory assertion is false on those observations |
| `advisory_gap` | The recommended practice represented by the rule is absent |
| `target_missed` | The selected service/policy target observation is false |
| `unknown` | A necessary observation, judgement or supported applicability is unresolved |
| `not_applicable` | The rule is from a different regime/version, or its applicability condition is known to be false |

**Unknown is different from No.** “I have not checked whether the statement was
supplied” is unknown. “The checked inventory confirms it was not supplied” is No.
For a conjunction, one established false condition can settle the result even if
another condition is unknown; for a disjunction, one established true condition
can settle it. Missing inputs are still listed in the report.

`not_satisfied` does not by itself mean “already overdue” or determine the
consequence for the whole plan. The evaluator does not decide when the caller
should assess a future action. Likewise, `not_applicable` for a person's statutory
hearing entitlement does not prohibit inviting that person to participate.

## Dates and transitional applicability

The initial law/profile is recorded as at **29 October 2026**, with supported
assessment dates from 25 March 2026. Three dates must not be confused:

- **Knowledge date:** when the encoded source review was undertaken.
- **Assessment date:** selects which represented rule version is used.
- **Event dates:** the actual or hypothetical publication, deadline, submission
  and other dates supplied in a case.

The present evaluator selects versions by assessment date. It does not reconstruct
a historical rule version independently for each event date. Future events in the
examples are scenarios under the recorded source versions. A null end date on a
rule means that no end is encoded; it does not guarantee future legal validity.

Regime selection requires an evidenced plan basis. Under the encoded saving,
ordinary legacy submission can be on 31 December 2026, eligible examination/adoption
can continue later, and a verified plan-specific direction can provide a later
deadline. Unknown saving eligibility stays unresolved. See the [boundary example](worked-examples.md#legacy-cutoff-inclusive)
and [unverified-direction example](worked-examples.md#late-legacy-unverified-direction).

## What still needs substantive review

The individual pages deliberately show where a rule has no example, bundles
several duties into one observation, or depends on an expert conclusion. The
package-wide gaps also include initial rollout cohorts, complete publication and
consultee mechanics, substantive SEA/HRA determinations, specialised routes and
court-deadline calculations.

The review should therefore ask **“does this assertion and its evidence definition
faithfully represent the cited provision?”**, followed by **“does the evaluator
implement that stated predicate?”** The source mapping remains pending maintainer
review. No new independent legal approval is claimed by generating these pages.

## Maintaining the readable pages

The explanations in this guide and [editorial notes](editorial-notes.md) are
hand-authored. The stage catalogue, input register and example result tables are
built from the model and evaluated fixtures, so changes cannot silently leave an
old explanation of the predicate or result in place.

```sh
python tools/build_procedure_docs.py
python tools/build_procedure_docs.py --check
```

The first command rebuilds the derived pages; the second fails if they have drifted
from their inputs. Source interpretation notes still need human review: automatic
synchronisation prevents stale transcription, not an incorrect interpretation.
