# Project documentation

This directory will hold technical design decisions, research, provenance conventions and architecture notes as the implementation develops.

## Procedural knowledge foundation

The [readable review guide](procedures/README.md) is the starting point for
understanding and auditing the model. It includes the two procedural routes,
stage pages with plain-language predicates and source links, complete input
definitions, and ten worked examples with actual evaluator results.

The [Local Plan procedural package](../knowledge/procedures/README.md) provides
versioned JSON data, schemas, an evidence-aware reference evaluator and regression
examples for the saved 2012 and new 2026 systems. The
[source recovery and verification record](procedural-source-review.md) explains
what was recovered, the legislation checked and the remaining coverage limits.

This is implemented foundation work subject to maintainer review, not an adopted
application architecture or a claim that the Local Plan environment is complete.

## Decision discipline
Distinguish **accepted decisions**, **working hypotheses**, **open questions** and **implemented behaviour**. Proposals in planning conversations or research notes are not adopted architecture until explicitly reviewed.

## Immediate priorities
- Establish the GitHub-native development and documentation workflow.
- Recover and catalogue existing research and examination-guidance artefacts without uploading private or non-redistributable content.
- Define representative planning cases and evaluate the common planning information model against them.
- Keep the website synchronised with actual repository status.

Track actionable work in GitHub Issues rather than duplicating a separate backlog here.
