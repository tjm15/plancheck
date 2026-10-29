# Procedural source recovery and verification

Research date: **29 October 2026**. Status: implemented initial mapping, pending
maintainer review. See the [package contract and limitations](../knowledge/procedures/README.md)
and [source catalogue](../knowledge/procedures/sources.json).

## Existing work and recovery

The active development repository was inspected at commit
`77693955989b2f2465599f12083f3cf6b72eeb16`. Its README, contribution instructions,
agent instructions and development notes describe foundation-stage work. The
tracked tree contained documentation and a website scaffold, with no existing
procedural model, schemas, executable rules or guidance extraction to extend.

A previously extracted Markdown document with the title of the 2026 Examinations
and Gateways guide was located in the user's available files. Its stored creation
date was 25 October 2026. Reading it recovered sections 1–12, a glossary and
definitions. It was useful for navigating gateway and examination topics. The
retrieved text lacked an edition/publication header; exact byte fidelity to the
original stored Markdown and completeness against every official page element
were not established. It is therefore recorded as a discovery aid, not an
authoritative dated legal source or a canonical snapshot.

Searches for the earlier legacy examination extraction did not locate one. That
is a limited recovery result, not evidence that no other copy exists. No private
file identifiers or duplicate full prose extraction have been added to this public
repository. Relevant structured assertions have been checked against official
sources and encoded directly.

## Primary-source verification

The legislation below was read directly from official legislation.gov.uk text,
with the commencement instrument's official PDF also used for the saving. The
model records exact provisions on each rule. Primary-text checking does not mean
that the mappings have been independently reviewed or that all legislation
affecting every plan has been exhaustively researched.

| Source/version | Use and qualifications |
| --- | --- |
| [SI 2026/186, as made](https://www.legislation.gov.uk/uksi/2026/186/made/data.html), in force 25 March 2026 | Parts 2 and 4: timetable, preparation, consultations, gateways, document definitions, examination, pause and publication. Regulation 18's replacement-plan duty is separate from initial rollout cohorts. |
| [SI 2012/767, revised Part 6](https://www.legislation.gov.uk/uksi/2012/767/part/6) | Regulations 17–27, applied only through the saving. Revised text is essential: reg 22(2)'s paper/electronic submission prescription was omitted in 2018. |
| [SI 2026/169, revised Schedule 1](https://www.legislation.gov.uk/uksi/2026/169/schedule/1) and [official PDF](https://www.legislation.gov.uk/uksi/2026/169/pdfs/uksi_20260169_en.pdf) | Commencement and savings; paragraph 2's exclusions, paragraph 4's inclusive submission cutoff, directed extensions and continuing proceedings. |
| [SI 2026/333](https://www.legislation.gov.uk/uksi/2026/333) | Adds CIL saving paragraph 8; does not change paragraph 4's cutoff. |
| PCPA 2004 [s 20](https://www.legislation.gov.uk/ukpga/2004/5/section/20/2026-03-24) and [s 23](https://www.legislation.gov.uk/ukpga/2004/5/section/23/2026-03-24), point in time 24 March 2026 | Saved examination, hearing entitlement, recommendation and adoption provisions, always read with the saving. The old text's references to s 33A do not reactivate that excluded duty. |
| PCPA 2004 [s 15CA](https://www.legislation.gov.uk/ukpga/2004/5/section/15CA), [s 15D](https://www.legislation.gov.uk/ukpga/2004/5/section/15D), [s 15DA](https://www.legislation.gov.uk/ukpga/2004/5/section/15DA), [s 15EA](https://www.legislation.gov.uk/ukpga/2004/5/section/15EA), revised text | Gateway advice, submission, examination, participation, modifications, pause, recommendations and adoption. Commencement checked against SI 2026/169 reg 3. |
| [Planning and Infrastructure Act 2025, Schedule 2](https://www.legislation.gov.uk/ukpga/2025/34/schedule/2) | Reviewed because the PCPA pages flag outstanding effects. Paragraph 10 concerns the joint-SDS provisions and associated definitions; it does not amend the encoded examination subsections. Prospective material is not activated merely because it appears on the site. |

The source catalogue deliberately distinguishes as-made instruments, revised text,
saved point-in-time provisions and non-statutory publications. It records URLs and
retrieval dates, not an assertion that mutable websites are immutable snapshots.
The public repository preserves the actual rule release in Git. A future source
ingestion facility may add permitted, checksummed snapshots without changing the
requirement to verify commencement and amendments.

## Guidance versions

| Official publication | Recorded version and role |
| --- | --- |
| [Procedure Guide for Local Plan Examinations](https://www.gov.uk/government/publications/examining-local-plans-procedural-practice/procedure-guide-for-local-plan-examinations) | 11th edition, updated 20 August 2026. Checklist, examination practice, modifications consultation and indicative pause practice. The guide has no statutory status. |
| [Procedural guide for Examinations and Gateways under the 2026 Regulations](https://www.gov.uk/guidance/procedural-guide-for-examinations-and-gateways-under-the-town-and-country-planning-local-planning-england-regulations-2026) | First edition, updated 26 August 2026. Paragraph 1.7 identifies its non-statutory character. Gateway 2 recommendations and targets remain separate from regulations. |
| [New-style Local Plans collection](https://www.gov.uk/government/collections/local-plans-preparing-and-examining-a-new-style-local-plan-2026-regulations) | Collection scope says plans submitted on or after 31 December 2026; this is contextual guidance, not a sufficient legal regime selector. |

## Decisions that affect the model

| Question | Encoded treatment and authority |
| --- | --- |
| Does 31 December 2026 automatically select the new regime? | No. SI 2026/169 Sch 1 para 4(4) permits ordinary saved submission **no later than** that date. Para 4(5) permits a later directed date; para 4(6) continues eligible proceedings. Record the plan's legal basis and saving evidence. |
| Is duty to cooperate still a legacy examination requirement in this profile? | No. Sch 1 para 2 excludes PCPA s 33A and 2012 reg 4 from the saving. This package does not decide retrospective compliance before 25 March 2026. Other engagement and strategic obligations must not be assumed abolished. |
| Must legacy submission be both paper and electronic? | No such requirement is copied from the as-made 2012 instrument: revised reg 22(2) records its omission by SI 2017/1244 reg 5 on 15 January 2018. Current administrative instructions may still need checking separately. |
| Is the legacy pre-examination checklist a statutory gateway? | No. It is guidance, with a ten-working-day response aim. The statutory submission-readiness condition is saved PCPA s 20(2). |
| Must every consultation be six weeks? | No. Legacy reg 19/20 representations have the reg 17 six-week minimum. New content/evidence consultation has six weeks under reg 23; proposed-plan consultation has eight under reg 27. Legacy reg 18 and new reg 20 scoping are not assigned an invented six-week minimum. |
| Are a draft plan and map mandatory at gateway 2? | No fixed mandatory pack of those documents is imposed by reg 26(3). The LPA must send what it considers necessary for the prescribed advice on the request date. Guidance 3.6.9–3.6.11 recommends useful emerging detail. Absence alone is an advisory gap; an evidenced failure to supply necessary material is a different assertion. |
| Are compliance and soundness statements optional at gateway 3? | No. They are in reg 17's gateway 3 submission documents and must be sent under reg 31(3). Their draft equivalents at gateway 2 are guidance. The twelve reg 32 requirements are individually represented. |
| Does passing gateway 3 establish soundness? | No. It records the appointed assessor's prescribed-requirements advice and triggers submission under s 15D(1). Soundness is the later examination question under s 15D(5). A statement of soundness is evidence of the authority's case, not the examiner's conclusion. |
| Who has a hearing entitlement? | Saved s 20(6) concerns a representor seeking a change who requests a hearing; new s 15D(6) is not limited to representations seeking change. The legacy limitation is not a ban on inviting others. |
| Must the authority ask for curative modifications? | Saved s 20(7C) requires an LPA request. New s 15D(11) does not impose that condition. The latter concerns the completed examination and includes recommendations for modifications and adoption with reasons. |
| How do legacy recommendation and adoption interact? | Saved s 20(7A) non-adoption may coexist with s 20(7C) curative modifications. Saved s 23(2A)–(3) permits adoption with those modifications. The model keeps those statutory outputs distinct. |
| Is six months always a statutory deadline? | No. New s 15DA(3) plus reg 36(1) prescribe a maximum pause period. The new guide's examination duration and the legacy guide's usual pause length are expectations. Calendar-month calculations are not substituted with 180 days. |
| Does unresolved work always mean withdrawal? | No. New s 15DA(8) also requires the examiner's conclusion that there is no prospect of a sound plan. Under s 15D(12), the examination must not be paused or due to be paused. Missing judgement remains unknown. |
| Must gateway advice always be followed? | The statutory duty in s 15CA(6)(a) is to have regard to the advice. The model does not replace that with a duty to adopt every recommendation. Section 15CA(6)(h) is excluded from commencement and is not activated. |

## Remaining review boundary

The package exposes its gaps in data and documentation. It does not implement the
initial rollout Schedule's authority/history cohorts, complete statutory consultee
and publication rules, all substantive content/soundness requirements, SEA/HRA
trigger decisions, special intervention or joint-plan provisions, standalone
minerals/waste procedures, or judicial challenge calculations. London/operative
SDS and supplementary-plan document triggers are represented where relevant, but
do not constitute complete specialised procedural profiles.

Professional judgements need signed or otherwise attributable evidence in a real
integration. The examples intentionally use synthetic evidence. Automated tests
verify schema integrity and the stated behaviour; they do not replace legal and
planning review. No database, user interface or permanent product architecture
has been chosen by this work.
