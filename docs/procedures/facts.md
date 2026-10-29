# Evidence input register

[Start with the review guide](README.md).

Generated from model 0.1.0, knowledge date 2026-10-29. Rebuild with `python tools/build_procedure_docs.py`. Authored explanations live in [editorial notes](editorial-notes.md). Legal mappings await maintainer review.

Each entry defines an input to the evaluator. Every value is supplied by a case author; the evaluator neither extracts these observations from documents nor independently makes the professional judgements. `null` or omission means unknown; `false` is an evidenced negative answer.

Use a rule's source and complete assertion to assess a bundled observation. Document provision, document quality and substantive findings are separate questions.

<a id="legacy-reg18-invitations-recorded"></a>

## legacy reg18 invitations recorded

The authority has identified the appropriate consultation bodies and residents/businesses under regulation 18 and recorded the required invitations to make representations.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1021).

**Used by:**
- [Invite the Regulation 18 consultation classes and take their representations into account.](stages/legacy-preparation.md#legacy-engagement)

<a id="legacy-reg18-responses-considered"></a>

## legacy reg18 responses considered

The authority has considered the representations received in preparing the plan; the reviewer has checked the response record rather than merely counted submissions.

**Type:** boolean. **Assessment:** reviewer judgement. [Canonical definition](../../knowledge/procedures/model.json#L1027).

**Used by:**
- [Invite the Regulation 18 consultation classes and take their representations into account.](stages/legacy-preparation.md#legacy-engagement)

<a id="legacy-reg19-publication-and-notices-recorded"></a>

## legacy reg19 publication and notices recorded

The proposed submission documents and statement of representations procedure have been made available and the regulation 19 consultation-body notices sent. This bundles several publication and notification duties into one reviewed observation.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1033).

**Used by:**
- [Publish the proposed submission documents and representations procedure, and send the required consultation-body notices.](stages/legacy-publication.md#legacy-publication-pack)

<a id="consultation-published"></a>

## consultation published

Calendar date of the publication that starts the selected consultation period. In a legacy case this is publication of the statement of representations procedure; in a new-system case it is the relevant content/evidence or proposed-plan notice. Use a separate case for each consultation.

**Type:** date. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1039).

**Used by:**
- [Allow at least six weeks for representations from publication of the representations procedure.](stages/legacy-publication.md#legacy-consultation-minimum)
- [Publish content/evidence and notice, notify and invite prescribed classes, no earlier than the day after scoping summary publication.](stages/new-content.md#new-content-sequence)
- [Allow at least six weeks for content and evidence representations from notice publication.](stages/new-content.md#new-content-minimum)
- [Publish proposed-plan submission documents and consultation notices, and invite required classes, no earlier than the day after gateway 2 advice publication.](stages/new-publication.md#new-plan-sequence)
- [Allow at least eight weeks for proposed-plan representations from notice publication.](stages/new-publication.md#new-plan-minimum)

<a id="consultation-deadline"></a>

## consultation deadline

Last calendar date stated for receipt of representations in the selected consultation. This field must refer to the same consultation as consultation_published.

**Type:** date. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1045).

**Used by:**
- [Allow at least six weeks for representations from publication of the representations procedure.](stages/legacy-publication.md#legacy-consultation-minimum)
- [Allow at least six weeks for content and evidence representations from notice publication.](stages/new-content.md#new-content-minimum)
- [Publish consultation summary, including response treatment or absence of responses, no earlier than the following day after the deadline.](stages/new-content.md#new-content-summary)
- [Allow at least eight weeks for proposed-plan representations from notice publication.](stages/new-publication.md#new-plan-minimum)
- [Publish a proposed-plan consultation summary no earlier than the day after the representations deadline.](stages/new-publication.md#new-plan-summary)

<a id="legacy-checklist-sent"></a>

## legacy checklist sent

The authority has completed and sent the pre-examination checklist described by the legacy procedure guide.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1051).

**Used by:**
- [Complete and send the pre-examination checklist.](stages/legacy-readiness.md#legacy-checklist)

<a id="legacy-checklist-response-target-met"></a>

## legacy checklist response target met

An evidenced review of checklist receipt and Inspectorate response establishes whether the ten-working-day service aim was met. The evaluator does not calculate working days.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1057).

**Used by:**
- [Inspectorate aims to respond to the checklist within ten working days.](stages/legacy-readiness.md#legacy-checklist-response)

<a id="legacy-regulatory-requirements-met"></a>

## legacy regulatory requirements met

The reviewer has established compliance with the relevant regulatory requirements referred to by saved PCPA section 20(2)(a), with a record of which requirements were considered. This package does not derive that finding from its selected rules.

**Type:** boolean. **Assessment:** reviewer judgement. [Canonical definition](../../knowledge/procedures/model.json#L1063).

**Used by:**
- [Submit only after relevant regulatory requirements are met and the authority considers the plan ready for examination.](stages/legacy-submission.md#legacy-submission-readiness)

<a id="lpa-ready-for-examination"></a>

## lpa ready for examination

The authority has recorded that it considers the legacy plan ready for independent examination under saved PCPA section 20(2)(b).

**Type:** boolean. **Assessment:** reviewer judgement. [Canonical definition](../../knowledge/procedures/model.json#L1069).

**Used by:**
- [Submit only after relevant regulatory requirements are met and the authority considers the plan ready for examination.](stages/legacy-submission.md#legacy-submission-readiness)

<a id="adoption-changes-policies-map"></a>

## adoption changes policies map

Adoption of this legacy plan would change the adopted policies map. This is the condition for supplying a submission policies map under regulation 22(1)(b).

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1075).

**Used by:**
- [Provide Proposed or submission policies map.](stages/legacy-submission.md#legacy-submission-map)

<a id="reg20-representations-received"></a>

## reg20 representations received

At least one representation was received under legacy regulation 20; the submission-pack representation duty is assessed against that record.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1081).

**Used by:**
- [Provide Representations and their identifiers.](stages/legacy-submission.md#legacy-submission-representations)

<a id="legacy-submission-sa-report-provided"></a>

## legacy submission sa report provided

The reviewer has verified that the sustainability appraisal report was included in the legacy examination submission. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1087).

**Used by:**
- [Provide Sustainability appraisal report.](stages/legacy-submission.md#legacy-submission-sa)

<a id="legacy-submission-policies-map-provided"></a>

## legacy submission policies map provided

The reviewer has verified that the proposed or submission policies map was included in the legacy examination submission. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1093).

**Used by:**
- [Provide Proposed or submission policies map.](stages/legacy-submission.md#legacy-submission-map)

<a id="legacy-submission-consultation-statement-provided"></a>

## legacy submission consultation statement provided

The reviewer has verified that the legacy Regulation 22 consultation statement was included in the legacy examination submission. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1099).

**Used by:**
- [Provide Legacy Regulation 22 consultation statement.](stages/legacy-submission.md#legacy-submission-consultation)

<a id="legacy-submission-representations-provided"></a>

## legacy submission representations provided

The reviewer has verified that the representations and their identifiers was included in the legacy examination submission. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1105).

**Used by:**
- [Provide Representations and their identifiers.](stages/legacy-submission.md#legacy-submission-representations)

<a id="legacy-submission-supporting-evidence-provided"></a>

## legacy submission supporting evidence provided

The reviewer has verified that the supporting evidence selected by the authority was included in the legacy examination submission. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1111).

**Used by:**
- [Provide Supporting evidence selected by the authority.](stages/legacy-submission.md#legacy-submission-evidence)

<a id="legacy-submission-publicity-recorded"></a>

## legacy submission publicity recorded

The reviewer has checked regulation 22(3) availability and notifications, including required recipients, the practicability qualification and the as-soon-as-reasonably-practicable timing. Finding an examination-library webpage alone is insufficient.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1117).

**Used by:**
- [Make submission documents available and notify consultation bodies and persons who requested notification.](stages/legacy-submission.md#legacy-submission-publicity)

<a id="hearing-notice-published"></a>

## hearing notice published

Calendar date on which the required hearing details and examiner name were made available for the hearing being assessed.

**Type:** date. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1123).

**Used by:**
- [Give at least six weeks’ notice of hearing details and examiner name; notify non-withdrawn Regulation 20 representors.](stages/legacy-examination.md#legacy-hearing-notice)
- [Publish hearing details and examiner name at least six weeks before the hearing, and notify requesters and other appropriate persons.](stages/new-examination.md#new-hearing-notice)

<a id="hearing-opens"></a>

## hearing opens

Calendar date on which the hearing being assessed opens.

**Type:** date. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1129).

**Used by:**
- [Give at least six weeks’ notice of hearing details and examiner name; notify non-withdrawn Regulation 20 representors.](stages/legacy-examination.md#legacy-hearing-notice)
- [Publish hearing details and examiner name at least six weeks before the hearing, and notify requesters and other appropriate persons.](stages/new-examination.md#new-hearing-notice)

<a id="legacy-nonwithdrawn-representors-notified"></a>

## legacy nonwithdrawn representors notified

The hearing date, time, place and examiner name were notified to persons who made regulation 20 representations and have not withdrawn them, under legacy regulation 24(2).

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1135).

**Used by:**
- [Give at least six weeks’ notice of hearing details and examiner name; notify non-withdrawn Regulation 20 representors.](stages/legacy-examination.md#legacy-hearing-notice)

<a id="hearing-to-be-held"></a>

## hearing to be held

A hearing is to be held, triggering the selected hearing-notice assertion.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1141).

**Used by:**
- [Give at least six weeks’ notice of hearing details and examiner name; notify non-withdrawn Regulation 20 representors.](stages/legacy-examination.md#legacy-hearing-notice)
- [Publish hearing details and examiner name at least six weeks before the hearing, and notify requesters and other appropriate persons.](stages/new-examination.md#new-hearing-notice)

<a id="hearing-opportunity-given"></a>

## hearing opportunity given

The person being assessed was given an opportunity to appear before and be heard by the examiner.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1147).

**Used by:**
- [A representor seeking a change who requests to be heard must have that opportunity.](stages/legacy-examination.md#legacy-hearing-right)
- [A person making representations who requests to be heard must have that opportunity.](stages/new-examination.md#new-hearing-right)

<a id="representation-made"></a>

## representation made

The person being assessed made a representation on this plan. The case concerns one person’s hearing entitlement.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1153).

**Used by:**
- [A representor seeking a change who requests to be heard must have that opportunity.](stages/legacy-examination.md#legacy-hearing-right)
- [A person making representations who requests to be heard must have that opportunity.](stages/new-examination.md#new-hearing-right)

<a id="representation-seeks-change"></a>

## representation seeks change

The person’s representation seeks a change to the legacy plan, engaging the additional condition in saved PCPA section 20(6).

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1159).

**Used by:**
- [A representor seeking a change who requests to be heard must have that opportunity.](stages/legacy-examination.md#legacy-hearing-right)

<a id="hearing-requested"></a>

## hearing requested

The person being assessed requested an opportunity to appear before and be heard by the examiner.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1165).

**Used by:**
- [A representor seeking a change who requests to be heard must have that opportunity.](stages/legacy-examination.md#legacy-hearing-right)
- [A person making representations who requests to be heard must have that opportunity.](stages/new-examination.md#new-hearing-right)

<a id="reg20-representations-considered"></a>

## reg20 representations considered

The examiner has considered the regulation 20 representations before making recommendations, as required by legacy regulation 23.

**Type:** boolean. **Assessment:** reviewer judgement. [Canonical definition](../../knowledge/procedures/model.json#L1171).

**Used by:**
- [Consider Regulation 20 representations before recommendations.](stages/legacy-examination.md#legacy-consider-representations)

<a id="curative-modifications-recommended"></a>

## curative modifications recommended

The legacy examiner has recommended the modifications necessary to make the plan sound and meet the saved legal requirements, following the authority’s request where required.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1177).

**Used by:**
- [Recommend necessary curative main modifications when the authority has requested them and they can achieve soundness and legal compliance.](stages/legacy-modifications.md#legacy-mm-request)

<a id="plan-sound-and-legal"></a>

## plan sound and legal

Inspector considers it reasonable to conclude that the legacy plan meets s 20(5)(a) requirements and is sound. Read with the 2026 saving: the excluded s 33A duty is not tested.

**Type:** boolean. **Assessment:** reviewer judgement. [Canonical definition](../../knowledge/procedures/model.json#L1183).

**Used by:**
- [Recommend necessary curative main modifications when the authority has requested them and they can achieve soundness and legal compliance.](stages/legacy-modifications.md#legacy-mm-request)
- [After examination, recommend adoption with reasons where it is reasonable to conclude that the plan is sound and meets the saved legal requirements.](stages/legacy-reporting.md#legacy-report-adopt)
- [After examination, recommend non-adoption with reasons where the statutory condition for recommending adoption is not met.](stages/legacy-reporting.md#legacy-report-non-adoption)

<a id="curable-by-modifications"></a>

## curable by modifications

The examiner considers that modifications can produce a sound plan; for the legacy rule they must also remedy the relevant saved legal requirements. This is a professional conclusion, not a file-presence test.

**Type:** boolean. **Assessment:** reviewer judgement. [Canonical definition](../../knowledge/procedures/model.json#L1189).

**Used by:**
- [Recommend necessary curative main modifications when the authority has requested them and they can achieve soundness and legal compliance.](stages/legacy-modifications.md#legacy-mm-request)
- [Recommend modifications and adoption with reasons if they would make it reasonable to conclude that the plan is sound.](stages/new-modifications.md#new-mm-recommendation)
- [Recommend withdrawal with reasons when soundness cannot be achieved by modifications and the examination is not paused or to be paused.](stages/new-reporting.md#new-report-withdraw)

<a id="lpa-requested-modifications"></a>

## lpa requested modifications

The legacy authority asked the examiner to recommend main modifications under saved PCPA section 20(7C).

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1195).

**Used by:**
- [Recommend necessary curative main modifications when the authority has requested them and they can achieve soundness and legal compliance.](stages/legacy-modifications.md#legacy-mm-request)

<a id="mm-published"></a>

## mm published

Calendar date on which the legacy proposed main modifications were published for the consultation being assessed.

**Type:** date. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1201).

**Used by:**
- [Consult on proposed main modifications for at least six weeks; assess environmental implications as necessary.](stages/legacy-modifications.md#legacy-mm-consultation)

<a id="mm-deadline"></a>

## mm deadline

Calendar deadline for representations on those legacy proposed main modifications.

**Type:** date. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1207).

**Used by:**
- [Consult on proposed main modifications for at least six weeks; assess environmental implications as necessary.](stages/legacy-modifications.md#legacy-mm-consultation)

<a id="legacy-pause-normally-within-six-months"></a>

## legacy pause normally within six months

An evidenced assessment records whether the legacy further-work pause meets the guide’s usual six-month expectation, taking the guidance’s qualification into account. No statutory maximum is inferred.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1213).

**Used by:**
- [Further work pauses should not usually exceed six months overall.](stages/legacy-pause.md#legacy-pause-target)

<a id="legacy-report-publication-recorded"></a>

## legacy report publication recorded

Final legacy recommendations and reasons were published and required notifications sent under regulation 25, using the correct trigger if a relevant Secretary of State direction applies.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1219).

**Used by:**
- [Publish final recommendations and reasons and notify those who requested notification.](stages/legacy-reporting.md#legacy-report-publication)

<a id="legacy-adoption-publication-recorded"></a>

## legacy adoption publication recorded

The adopted legacy plan, adoption statement and sustainability appraisal report were made available, requesters notified and the adoption statement sent to the Secretary of State under regulation 26.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1225).

**Used by:**
- [Publish the adopted plan, adoption statement and SA report; send the statement to requesters and the Secretary of State.](stages/legacy-adoption.md#legacy-adoption-publication)

<a id="legacy-withdrawal-publicity-recorded"></a>

## legacy withdrawal publicity recorded

The legacy withdrawal statement, notifications and cessation of specified document availability have been checked against regulation 27.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1231).

**Used by:**
- [Publish withdrawal, notify the reg 22(3)(b) bodies, and cease the specified document availability.](stages/legacy-withdrawal.md#legacy-withdrawal-publication)

<a id="timetable-requirements-met"></a>

## timetable requirements met

The authority’s timetable content, initial publication and subsequent revisions comply with the selected duties in 2026 regulations 4, 6 and 8. The reviewer supplies this overall finding; the evaluator does not inspect milestones or calculate monthly updates.

**Type:** boolean. **Assessment:** reviewer judgement. [Canonical definition](../../knowledge/procedures/model.json#L1237).

**Used by:**
- [Publish and maintain the local plan timetable with anticipated and actual milestones.](stages/new-timetable.md#new-timetable)

<a id="notice-intention-requirements-met"></a>

## notice intention requirements met

The notice of intention has the regulation 19 content and has been published as required, including any applicable additional details. This is a reviewed bundle, not a text extraction.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1243).

**Used by:**
- [Prepare and publish notice of intention with prescribed authority, area, title, timetable and publication details.](stages/new-timetable.md#new-notice)

<a id="scoping-invitations-and-notice-recorded"></a>

## scoping invitations and notice recorded

The regulation 20 scoping invitations and public notice identify the prescribed matters, representation arrangements and notification opportunities, and were addressed to the appropriate consultation classes.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1249).

**Used by:**
- [Invite relevant consultation bodies and publish a scoping notice no earlier than the notice of intention.](stages/new-scoping.md#new-scoping)

<a id="notice-intention-date"></a>

## notice intention date

Calendar date on which the regulation 19 notice of intention was made available.

**Type:** date. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1255).

**Used by:**
- [Invite relevant consultation bodies and publish a scoping notice no earlier than the notice of intention.](stages/new-scoping.md#new-scoping)

<a id="scoping-notice-date"></a>

## scoping notice date

Calendar date on which the regulation 20 scoping consultation notice was published.

**Type:** date. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1261).

**Used by:**
- [Invite relevant consultation bodies and publish a scoping notice no earlier than the notice of intention.](stages/new-scoping.md#new-scoping)

<a id="gateway1-contents-recorded"></a>

## gateway1 contents recorded

The LPA self-assessment summary addresses timetable compliance, project management/governance, consultation/engagement, anticipated plan content and relevant SEA obligations under regulation 21(2).

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1267).

**Used by:**
- [Publish an LPA self-assessment covering timetable, governance, engagement, anticipated content and SEA obligations.](stages/new-gateway1.md#new-gateway1-summary)

<a id="four-calendar-month-notice-period-elapsed"></a>

## four calendar month notice period elapsed

The reviewer has checked that gateway 1 publication is no earlier than the first day after the four-month period beginning with notice-of-intention publication. Calendar-month arithmetic is supplied as a reviewed conclusion.

**Type:** boolean. **Assessment:** reviewer judgement. [Canonical definition](../../knowledge/procedures/model.json#L1273).

**Used by:**
- [Publish self-assessment no earlier than the later of the first day after the four-month notice period and the day after the scoping deadline.](stages/new-gateway1.md#new-gateway1-timing)

<a id="scoping-deadline"></a>

## scoping deadline

Calendar deadline stated for representations in the regulation 20 scoping consultation.

**Type:** date. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1279).

**Used by:**
- [Publish self-assessment no earlier than the later of the first day after the four-month notice period and the day after the scoping deadline.](stages/new-gateway1.md#new-gateway1-timing)

<a id="gateway1-published"></a>

## gateway1 published

Calendar date on which the LPA made its gateway 1 self-assessment summary available.

**Type:** date. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1285).

**Used by:**
- [Publish self-assessment no earlier than the later of the first day after the four-month notice period and the day after the scoping deadline.](stages/new-gateway1.md#new-gateway1-timing)
- [Publish scoping summary no earlier than the day after gateway 1 publication.](stages/new-gateway1.md#new-scoping-summary)

<a id="scoping-summary-contents-recorded"></a>

## scoping summary contents recorded

The scoping summary records the prescribed consultation activity, main issues and their treatment, or the absence of representations, under regulation 22.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1291).

**Used by:**
- [Publish scoping summary no earlier than the day after gateway 1 publication.](stages/new-gateway1.md#new-scoping-summary)

<a id="scoping-summary-published"></a>

## scoping summary published

Calendar date on which the regulation 22 scoping consultation summary was made available.

**Type:** date. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1297).

**Used by:**
- [Publish scoping summary no earlier than the day after gateway 1 publication.](stages/new-gateway1.md#new-scoping-summary)
- [Publish content/evidence and notice, notify and invite prescribed classes, no earlier than the day after scoping summary publication.](stages/new-content.md#new-content-sequence)

<a id="content-consultation-notices-recorded"></a>

## content consultation notices recorded

The regulation 23 content/evidence material and notice were made available, appropriate consultation bodies invited and required notifications recorded. The contents of the published pack require review.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1303).

**Used by:**
- [Publish content/evidence and notice, notify and invite prescribed classes, no earlier than the day after scoping summary publication.](stages/new-content.md#new-content-sequence)

<a id="content-summary-contents-recorded"></a>

## content summary contents recorded

The regulation 24 summary records the content/evidence consultation, main issues and their treatment, including the required statement where no representations were received.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1309).

**Used by:**
- [Publish consultation summary, including response treatment or absence of responses, no earlier than the following day after the deadline.](stages/new-content.md#new-content-summary)

<a id="content-summary-published"></a>

## content summary published

Calendar date on which the regulation 24 content/evidence consultation summary was made available.

**Type:** date. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1315).

**Used by:**
- [Publish consultation summary, including response treatment or absence of responses, no earlier than the following day after the deadline.](stages/new-content.md#new-content-summary)
- [Seek gateway 2 observations and advice no earlier than the day after publication of the content and evidence summary.](stages/new-gateway2.md#new-gateway2-sequence)

<a id="gateway2-requested"></a>

## gateway2 requested

Calendar date on which the authority sought gateway 2 observations and advice under regulation 26.

**Type:** date. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1321).

**Used by:**
- [Seek gateway 2 observations and advice no earlier than the day after publication of the content and evidence summary.](stages/new-gateway2.md#new-gateway2-sequence)
- [Send the assessor, on the request date, documents or information the authority considers necessary for the prescribed observations and advice.](stages/new-gateway2.md#new-gateway2-necessary-material)

<a id="gateway2-necessary-material-sent"></a>

## gateway2 necessary material sent

Authority records what it considers necessary for reg 26(2) advice and supplies that material. Lack of an emerging draft plan/map alone does not falsify this judgement.

**Type:** boolean. **Assessment:** reviewer judgement. [Canonical definition](../../knowledge/procedures/model.json#L1327).

**Used by:**
- [Send the assessor, on the request date, documents or information the authority considers necessary for the prescribed observations and advice.](stages/new-gateway2.md#new-gateway2-necessary-material)

<a id="gateway2-material-sent"></a>

## gateway2 material sent

Calendar date on which the authority sent the material it considered necessary for gateway 2 advice.

**Type:** date. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1333).

**Used by:**
- [Send the assessor, on the request date, documents or information the authority considers necessary for the prescribed observations and advice.](stages/new-gateway2.md#new-gateway2-necessary-material)

<a id="new-gateway2-plan-provided"></a>

## new gateway2 plan provided

An emerging draft plan or relevant emerging policy detail is supplied to assist gateway 2, as recommended by the procedure guide. This observation concerns gateway 2 supporting material, not the gateway 3 or examination submission packs.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1339).

**Used by:**
- [Provide emerging draft plan or relevant emerging policy detail where possible to assist gateway 2.](stages/new-gateway2.md#new-gateway2-draft-plan)

<a id="new-gateway2-policies-map-provided"></a>

## new gateway2 policies map provided

An emerging policies map was supplied to assist gateway 2 as recommended by guidance. Its absence alone does not establish a breach of regulation 26(3).

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1345).

**Used by:**
- [Provide an emerging policies map where possible to assist gateway 2.](stages/new-gateway2.md#new-gateway2-draft-map)

<a id="new-gateway2-gateway2-cover-provided"></a>

## new gateway2 gateway2 cover provided

A covering letter was supplied with the gateway 2 material, as recommended by the procedure guide.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1351).

**Used by:**
- [Provide Gateway 2 covering letter.](stages/new-gateway2.md#new-gateway2-cover)

<a id="new-gateway2-draft-compliance-provided"></a>

## new gateway2 draft compliance provided

A draft statement of compliance was supplied to assist gateway 2; this is the recommended draft, not the mandatory completed gateway 3 statement.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1357).

**Used by:**
- [Provide Draft statement of compliance.](stages/new-gateway2.md#new-gateway2-compliance)

<a id="new-gateway2-draft-soundness-provided"></a>

## new gateway2 draft soundness provided

A draft statement of soundness was supplied to assist gateway 2; this is the recommended draft, not an examiner’s finding of soundness.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1363).

**Used by:**
- [Provide Draft statement of soundness.](stages/new-gateway2.md#new-gateway2-soundness)

<a id="new-gateway2-evidence-index-provided"></a>

## new gateway2 evidence index provided

An evidence register, including expected completion dates for outstanding evidence where relevant, was supplied to assist gateway 2 under the guide.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1369).

**Used by:**
- [Provide Evidence register with completion dates.](stages/new-gateway2.md#new-gateway2-index)

<a id="gateway2-target-met"></a>

## gateway2 target met

An evidenced review establishes whether gateway 2 met the guide’s indicative four-to-six-week duration, allowing for its stated qualifications. This is a service target, not a statutory time limit.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1375).

**Used by:**
- [Aim to complete gateway 2 in four to six weeks.](stages/new-gateway2.md#new-gateway2-target)

<a id="gateway2-publication-and-notices-recorded"></a>

## gateway2 publication and notices recorded

Gateway 2 advice was published as soon as reasonably practicable; on the publication day the advice and supplied material were made available, requesters/appropriate persons notified and copies sent to persons identified in the advice.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1381).

**Used by:**
- [Publish assessor advice as soon as reasonably practicable and simultaneously make submitted material available, notify requesters and send copies to persons identified in the advice.](stages/new-gateway2.md#new-gateway2-publication)

<a id="gateway-advice-and-responses-considered"></a>

## gateway advice and responses considered

The authority has had regard to gateway observations/advice and consultation representations when preparing the plan under PCPA section 15CA(6)(a)-(b). It need not accept every recommendation.

**Type:** boolean. **Assessment:** reviewer judgement. [Canonical definition](../../knowledge/procedures/model.json#L1387).

**Used by:**
- [Have regard to gateway observations/advice and consultation responses while preparing the plan.](stages/new-publication.md#new-gateway-advice-regard)

<a id="new-plan-publication-and-invitations-recorded"></a>

## new plan publication and invitations recorded

The proposed-plan consultation pack and notice required by regulation 27 were made available and appropriate consultation bodies invited. The pack includes plan, policies map, evidence details, consultation statement and relevant supporting documents.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1393).

**Used by:**
- [Publish proposed-plan submission documents and consultation notices, and invite required classes, no earlier than the day after gateway 2 advice publication.](stages/new-publication.md#new-plan-sequence)

<a id="gateway2-advice-published"></a>

## gateway2 advice published

Calendar date on which the authority published its gateway 2 observations and advice.

**Type:** date. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1399).

**Used by:**
- [Publish proposed-plan submission documents and consultation notices, and invite required classes, no earlier than the day after gateway 2 advice publication.](stages/new-publication.md#new-plan-sequence)

<a id="sds-invitation-same-day-recorded"></a>

## sds invitation same day recorded

On proposed-plan consultation publication day, the authority invited the operative spatial development strategy authority’s conformity representations as required by regulation 28.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1405).

**Used by:**
- [On the proposed-plan publication day, notify and invite conformity representations from the operative SDS authority.](stages/new-publication.md#new-sds-consultation)

<a id="operative-sds"></a>

## operative sds

A spatial development strategy is operative in relation to the plan area so that the selected regulation 28 conformity/document requirements apply.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1411).

**Used by:**
- [On the proposed-plan publication day, notify and invite conformity representations from the operative SDS authority.](stages/new-publication.md#new-sds-consultation)
- [Provide Representations on conformity with operative SDS.](stages/new-gateway3.md#new-gateway3-sds-representations)
- [Provide Representations on conformity with operative SDS.](stages/new-submission.md#new-submission-sds-representations)

<a id="supplementary-statement-same-day-recorded"></a>

## supplementary statement same day recorded

Where regulation 29 applies, the supplementary plans statement was made available on the same day as the proposed-plan consultation documents.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1417).

**Used by:**
- [Publish the supplementary plans statement on the same day as the proposed-plan documents where qualifying supplementary plans are in effect.](stages/new-publication.md#new-supplementary-statement)

<a id="qualifying-supplementary-plans"></a>

## qualifying supplementary plans

Supplementary plans meeting the condition in regulation 29 are in effect, triggering its statement requirement. The legal trigger must be checked from the actual instruments.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1423).

**Used by:**
- [Publish the supplementary plans statement on the same day as the proposed-plan documents where qualifying supplementary plans are in effect.](stages/new-publication.md#new-supplementary-statement)
- [Provide Supplementary plans statement.](stages/new-gateway3.md#new-gateway3-supplementary-statement)

<a id="plan-summary-contents-recorded"></a>

## plan summary contents recorded

The regulation 30 proposed-plan consultation summary contains the prescribed consultation information and treatment of issues, including the required statement if no representations were received.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1429).

**Used by:**
- [Publish a proposed-plan consultation summary no earlier than the day after the representations deadline.](stages/new-publication.md#new-plan-summary)

<a id="plan-summary-published"></a>

## plan summary published

Calendar date on which the regulation 30 proposed-plan consultation summary was made available.

**Type:** date. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1435).

**Used by:**
- [Publish a proposed-plan consultation summary no earlier than the day after the representations deadline.](stages/new-publication.md#new-plan-summary)
- [Seek gateway 3 when the authority considers prescribed requirements met, no earlier than the day after proposed-plan summary publication.](stages/new-gateway3.md#new-gateway3-sequence)

<a id="lpa-considers-prescribed-requirements-met"></a>

## lpa considers prescribed requirements met

The authority considers that the regulation 32 prescribed requirements are met when seeking gateway 3. This is its own judgement, distinct from the appointed assessor’s subsequent advice.

**Type:** boolean. **Assessment:** reviewer judgement. [Canonical definition](../../knowledge/procedures/model.json#L1441).

**Used by:**
- [Seek gateway 3 when the authority considers prescribed requirements met, no earlier than the day after proposed-plan summary publication.](stages/new-gateway3.md#new-gateway3-sequence)

<a id="gateway3-requested"></a>

## gateway3 requested

Calendar date on which the authority sought the initial gateway 3 prescribed-requirements assessment under regulation 31.

**Type:** date. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1447).

**Used by:**
- [Seek gateway 3 when the authority considers prescribed requirements met, no earlier than the day after proposed-plan summary publication.](stages/new-gateway3.md#new-gateway3-sequence)
- [Send the gateway 3 submission documents on the gateway request date.](stages/new-gateway3.md#new-gateway3-document-timing)

<a id="sds-representations-received"></a>

## sds representations received

At least one conformity representation was received under regulation 28; copies must be included where the selected pack requires them.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1453).

**Used by:**
- [Provide Representations on conformity with operative SDS.](stages/new-gateway3.md#new-gateway3-sds-representations)
- [Provide Representations on conformity with operative SDS.](stages/new-submission.md#new-submission-sds-representations)

<a id="environmental-report-prepared"></a>

## environmental report prepared

An environmental report has been prepared under regulation 12 of the SEA Regulations 2004. This triggers the selected pack’s report-copy requirement; it does not decide whether an assessment should have been undertaken.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1459).

**Used by:**
- [Provide Environmental report under SEA reg 12.](stages/new-gateway3.md#new-gateway3-environmental-report)
- [Provide Environmental report under SEA reg 12.](stages/new-submission.md#new-submission-environmental-report)

<a id="sea-no-significant-effects-determination"></a>

## sea no significant effects determination

The authority has made the SEA regulation 9(1) determination that the plan is unlikely to have significant environmental effects, with a reasons statement under regulation 9(3). This records the determination, not this evaluator’s environmental judgement.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1465).

**Used by:**
- [Provide SEA screening determination reasons under reg 9(3).](stages/new-gateway3.md#new-gateway3-screening-reasons)
- [Provide SEA screening determination reasons under reg 9(3).](stages/new-submission.md#new-submission-screening-reasons)

<a id="new-gateway3-plan-provided"></a>

## new gateway3 plan provided

The reviewer has verified that the proposed Local Plan was included in the gateway 3 submission to the appointed assessor. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1471).

**Used by:**
- [Provide Proposed Local Plan.](stages/new-gateway3.md#new-gateway3-plan)

<a id="new-gateway3-policies-map-provided"></a>

## new gateway3 policies map provided

The reviewer has verified that the proposed or submission policies map was included in the gateway 3 submission to the appointed assessor. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1477).

**Used by:**
- [Provide Proposed or submission policies map.](stages/new-gateway3.md#new-gateway3-policies-map)

<a id="new-gateway3-compliance-provided"></a>

## new gateway3 compliance provided

The reviewer has verified that the statement of compliance was included in the gateway 3 submission to the appointed assessor. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1483).

**Used by:**
- [Provide Statement of compliance.](stages/new-gateway3.md#new-gateway3-compliance)

<a id="new-gateway3-soundness-provided"></a>

## new gateway3 soundness provided

The reviewer has verified that the statement of soundness was included in the gateway 3 submission to the appointed assessor. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1489).

**Used by:**
- [Provide Statement of soundness.](stages/new-gateway3.md#new-gateway3-soundness)

<a id="new-gateway3-engagement-summary-provided"></a>

## new gateway3 engagement summary provided

The reviewer has verified that the summary of consultation and engagement was included in the gateway 3 submission to the appointed assessor. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1495).

**Used by:**
- [Provide Summary of consultation and engagement.](stages/new-gateway3.md#new-gateway3-engagement-summary)

<a id="new-gateway3-scoping-summary-provided"></a>

## new gateway3 scoping summary provided

The reviewer has verified that the summary of scoping consultation was included in the gateway 3 submission to the appointed assessor. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1501).

**Used by:**
- [Provide Summary of scoping consultation.](stages/new-gateway3.md#new-gateway3-scoping-summary)

<a id="new-gateway3-content-summary-provided"></a>

## new gateway3 content summary provided

The reviewer has verified that the content and evidence consultation summary was included in the gateway 3 submission to the appointed assessor. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1507).

**Used by:**
- [Provide Content and evidence consultation summary.](stages/new-gateway3.md#new-gateway3-content-summary)

<a id="new-gateway3-plan-summary-provided"></a>

## new gateway3 plan summary provided

The reviewer has verified that the proposed-plan consultation summary was included in the gateway 3 submission to the appointed assessor. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1513).

**Used by:**
- [Provide Proposed-plan consultation summary.](stages/new-gateway3.md#new-gateway3-plan-summary)

<a id="new-gateway3-sds-representations-provided"></a>

## new gateway3 sds representations provided

The reviewer has verified that the representations on conformity with operative SDS was included in the gateway 3 submission to the appointed assessor. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1519).

**Used by:**
- [Provide Representations on conformity with operative SDS.](stages/new-gateway3.md#new-gateway3-sds-representations)

<a id="new-gateway3-practical-readiness-provided"></a>

## new gateway3 practical readiness provided

The reviewer has verified that the practical arrangements for examination was included in the gateway 3 submission to the appointed assessor. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1525).

**Used by:**
- [Provide Practical arrangements for examination.](stages/new-gateway3.md#new-gateway3-practical-readiness)

<a id="new-gateway3-supplementary-statement-provided"></a>

## new gateway3 supplementary statement provided

The reviewer has verified that the supplementary plans statement was included in the gateway 3 submission to the appointed assessor. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1531).

**Used by:**
- [Provide Supplementary plans statement.](stages/new-gateway3.md#new-gateway3-supplementary-statement)

<a id="new-gateway3-environmental-report-provided"></a>

## new gateway3 environmental report provided

The reviewer has verified that the environmental report under SEA reg 12 was included in the gateway 3 submission to the appointed assessor. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1537).

**Used by:**
- [Provide Environmental report under SEA reg 12.](stages/new-gateway3.md#new-gateway3-environmental-report)

<a id="new-gateway3-screening-reasons-provided"></a>

## new gateway3 screening reasons provided

The reviewer has verified that the sEA screening determination reasons under reg 9(3) was included in the gateway 3 submission to the appointed assessor. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1543).

**Used by:**
- [Provide SEA screening determination reasons under reg 9(3).](stages/new-gateway3.md#new-gateway3-screening-reasons)

<a id="gateway3-additional-material-sent"></a>

## gateway3 additional material sent

The authority sent any additional documents or information it considered necessary to support the gateway 3 assessment, under the regulation 17 definition. The evaluator does not decide which additional evidence is necessary.

**Type:** boolean. **Assessment:** reviewer judgement. [Canonical definition](../../knowledge/procedures/model.json#L1549).

**Used by:**
- [Send additional material the authority considers necessary for the prescribed-requirements assessment.](stages/new-gateway3.md#new-gateway3-other-material)

<a id="assessor-reg32-a-satisfied"></a>

## assessor reg32 a satisfied

Appointed assessor’s evidenced conclusion on reg 32(a): Policies on amount, type, location and timing of development. Not inferred from file presence.

**Type:** boolean. **Assessment:** reviewer judgement. [Canonical definition](../../knowledge/procedures/model.json#L1555).

**Used by:**
- [Policies on amount, type, location and timing of development.](stages/new-gateway3.md#new-gateway3-test-a)

<a id="assessor-reg32-b-satisfied"></a>

## assessor reg32 b satisfied

Appointed assessor’s evidenced conclusion on reg 32(b): Area-specific vision, no more than ten measurable outcomes, and superseded-policy content or explanation. Not inferred from file presence.

**Type:** boolean. **Assessment:** reviewer judgement. [Canonical definition](../../knowledge/procedures/model.json#L1561).

**Used by:**
- [Area-specific vision, no more than ten measurable outcomes, and superseded-policy content or explanation.](stages/new-gateway3.md#new-gateway3-test-b)

<a id="assessor-reg32-c-satisfied"></a>

## assessor reg32 c satisfied

Appointed assessor’s evidenced conclusion on reg 32(c): Climate change mitigation and adaptation. Not inferred from file presence.

**Type:** boolean. **Assessment:** reviewer judgement. [Canonical definition](../../knowledge/procedures/model.json#L1567).

**Used by:**
- [Climate change mitigation and adaptation.](stages/new-gateway3.md#new-gateway3-test-c)

<a id="assessor-reg32-d-satisfied"></a>

## assessor reg32 d satisfied

Appointed assessor’s evidenced conclusion on reg 32(d): Local nature recovery strategy taken into account. Not inferred from file presence.

**Type:** boolean. **Assessment:** reviewer judgement. [Canonical definition](../../knowledge/procedures/model.json#L1573).

**Used by:**
- [Local nature recovery strategy taken into account.](stages/new-gateway3.md#new-gateway3-test-d)

<a id="assessor-reg32-e-satisfied"></a>

## assessor reg32 e satisfied

Appointed assessor’s evidenced conclusion on reg 32(e): Housing and affordable-housing need assessment taken into account. Not inferred from file presence.

**Type:** boolean. **Assessment:** reviewer judgement. [Canonical definition](../../knowledge/procedures/model.json#L1579).

**Used by:**
- [Housing and affordable-housing need assessment taken into account.](stages/new-gateway3.md#new-gateway3-test-e)

<a id="assessor-reg32-f-satisfied"></a>

## assessor reg32 f satisfied

Appointed assessor’s evidenced conclusion on reg 32(f): No content beyond what is permitted or required. Not inferred from file presence.

**Type:** boolean. **Assessment:** reviewer judgement. [Canonical definition](../../knowledge/procedures/model.json#L1585).

**Used by:**
- [No content beyond what is permitted or required.](stages/new-gateway3.md#new-gateway3-test-f)

<a id="assessor-reg32-g-satisfied"></a>

## assessor reg32 g satisfied

Appointed assessor’s evidenced conclusion on reg 32(g): Required gateway requests made at the prescribed times. Not inferred from file presence.

**Type:** boolean. **Assessment:** reviewer judgement. [Canonical definition](../../knowledge/procedures/model.json#L1591).

**Used by:**
- [Required gateway requests made at the prescribed times.](stages/new-gateway3.md#new-gateway3-test-g)

<a id="assessor-reg32-h-satisfied"></a>

## assessor reg32 h satisfied

Appointed assessor’s evidenced conclusion on reg 32(h): Gateway 2 advice published. Not inferred from file presence.

**Type:** boolean. **Assessment:** reviewer judgement. [Canonical definition](../../knowledge/procedures/model.json#L1597).

**Used by:**
- [Gateway 2 advice published.](stages/new-gateway3.md#new-gateway3-test-h)

<a id="assessor-reg32-i-satisfied"></a>

## assessor reg32 i satisfied

Appointed assessor’s evidenced conclusion on reg 32(i): Regard had to applicable statutory matters. Not inferred from file presence.

**Type:** boolean. **Assessment:** reviewer judgement. [Canonical definition](../../knowledge/procedures/model.json#L1603).

**Used by:**
- [Regard had to applicable statutory matters.](stages/new-gateway3.md#new-gateway3-test-i)

<a id="assessor-reg32-j-satisfied"></a>

## assessor reg32 j satisfied

Appointed assessor’s evidenced conclusion on reg 32(j): Prescribed independent-examination documents prepared. Not inferred from file presence.

**Type:** boolean. **Assessment:** reviewer judgement. [Canonical definition](../../knowledge/procedures/model.json#L1609).

**Used by:**
- [Prescribed independent-examination documents prepared.](stages/new-gateway3.md#new-gateway3-test-j)

<a id="assessor-reg32-k-satisfied"></a>

## assessor reg32 k satisfied

Appointed assessor’s evidenced conclusion on reg 32(k): Policies map accurately illustrates geographical policy application. Not inferred from file presence.

**Type:** boolean. **Assessment:** reviewer judgement. [Canonical definition](../../knowledge/procedures/model.json#L1615).

**Used by:**
- [Policies map accurately illustrates geographical policy application.](stages/new-gateway3.md#new-gateway3-test-k)

<a id="assessor-reg32-l-satisfied"></a>

## assessor reg32 l satisfied

Appointed assessor’s evidenced conclusion on reg 32(l): Practical readiness for examination. Not inferred from file presence.

**Type:** boolean. **Assessment:** reviewer judgement. [Canonical definition](../../knowledge/procedures/model.json#L1621).

**Used by:**
- [Practical readiness for examination.](stages/new-gateway3.md#new-gateway3-test-l)

<a id="gateway3-reasoned-findings-sent"></a>

## gateway3 reasoned findings sent

The appointed assessor sent electronically in typescript a met/not-met conclusion and reasoned justification for each regulation 32 requirement under regulation 31(4).

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1627).

**Used by:**
- [Provide a met/not-met conclusion and reasoned justification for each prescribed requirement, electronically in typescript.](stages/new-gateway3.md#new-gateway3-reasons)

<a id="gateway3-completion-publication-recorded"></a>

## gateway3 completion publication recorded

On the day successful gateway 3 advice was published, the authority also made available the completion statement and gateway 3 submission documents under regulation 31(6).

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1633).

**Used by:**
- [On publication of successful gateway 3 advice, also publish the completion statement and gateway 3 submission documents.](stages/new-gateway3.md#new-gateway3-completion)

<a id="assessor-all-prescribed-requirements-met"></a>

## assessor all prescribed requirements met

The appointed assessor advises that every reg 32 requirement is met. This records the advice, not an application-generated soundness or legal-compliance certificate.

**Type:** boolean. **Assessment:** reviewer judgement. [Canonical definition](../../knowledge/procedures/model.json#L1639).

**Used by:**
- [On publication of successful gateway 3 advice, also publish the completion statement and gateway 3 submission documents.](stages/new-gateway3.md#new-gateway3-completion)
- [Remedy failed prescribed requirements and seek further assessment with updated documents, repeating as necessary.](stages/new-gateway3-repeat.md#new-gateway3-repeat)
- [Submit the proposed Local Plan when the appointed person advises that prescribed requirements are met.](stages/new-submission.md#new-submit-after-gateway3)

<a id="gateway3-remedy-and-repeat-recorded"></a>

## gateway3 remedy and repeat recorded

Following failed gateway 3 advice, the authority addressed the reasons for failure and sought further assessment with updated prescribed documents under regulation 33, as soon as reasonably practicable and again if required. This Boolean summarises the loop; the evaluator does not track its individual iterations.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1645).

**Used by:**
- [Remedy failed prescribed requirements and seek further assessment with updated documents, repeating as necessary.](stages/new-gateway3-repeat.md#new-gateway3-repeat)

<a id="plan-submitted"></a>

## plan submitted

The proposed Local Plan has been submitted to the Secretary of State for independent examination under PCPA section 15D(1).

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1651).

**Used by:**
- [Submit the proposed Local Plan when the appointed person advises that prescribed requirements are met.](stages/new-submission.md#new-submit-after-gateway3)

<a id="new-submission-policies-map-provided"></a>

## new submission policies map provided

The reviewer has verified that the proposed or submission policies map was included in the new-system examination submission. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1657).

**Used by:**
- [Provide Proposed or submission policies map.](stages/new-submission.md#new-submission-policies-map)

<a id="new-submission-gateway3-completion-provided"></a>

## new submission gateway3 completion provided

The reviewer has verified that the gateway 3 completion statement was included in the new-system examination submission. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1663).

**Used by:**
- [Provide Gateway 3 completion statement.](stages/new-submission.md#new-submission-gateway3-completion)

<a id="new-submission-engagement-summary-provided"></a>

## new submission engagement summary provided

The reviewer has verified that the summary of consultation and engagement was included in the new-system examination submission. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1669).

**Used by:**
- [Provide Summary of consultation and engagement.](stages/new-submission.md#new-submission-engagement-summary)

<a id="new-submission-plan-summary-provided"></a>

## new submission plan summary provided

The reviewer has verified that the proposed-plan consultation summary was included in the new-system examination submission. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1675).

**Used by:**
- [Provide Proposed-plan consultation summary.](stages/new-submission.md#new-submission-plan-summary)

<a id="new-submission-sds-representations-provided"></a>

## new submission sds representations provided

The reviewer has verified that the representations on conformity with operative SDS was included in the new-system examination submission. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1681).

**Used by:**
- [Provide Representations on conformity with operative SDS.](stages/new-submission.md#new-submission-sds-representations)

<a id="new-submission-compliance-provided"></a>

## new submission compliance provided

The reviewer has verified that the statement of compliance was included in the new-system examination submission. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1687).

**Used by:**
- [Provide Statement of compliance.](stages/new-submission.md#new-submission-compliance)

<a id="new-submission-soundness-provided"></a>

## new submission soundness provided

The reviewer has verified that the statement of soundness was included in the new-system examination submission. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1693).

**Used by:**
- [Provide Statement of soundness.](stages/new-submission.md#new-submission-soundness)

<a id="new-submission-environmental-report-provided"></a>

## new submission environmental report provided

The reviewer has verified that the environmental report under SEA reg 12 was included in the new-system examination submission. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1699).

**Used by:**
- [Provide Environmental report under SEA reg 12.](stages/new-submission.md#new-submission-environmental-report)

<a id="new-submission-screening-reasons-provided"></a>

## new submission screening reasons provided

The reviewer has verified that the sEA screening determination reasons under reg 9(3) was included in the new-system examination submission. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1705).

**Used by:**
- [Provide SEA screening determination reasons under reg 9(3).](stages/new-submission.md#new-submission-screening-reasons)

<a id="new-submission-supporting-evidence-provided"></a>

## new submission supporting evidence provided

The reviewer has verified that the supporting evidence selected by the authority was included in the new-system examination submission. This input records provision of the document; it does not establish the adequacy of its contents or, by itself, the date of transmission.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1711).

**Used by:**
- [Provide Supporting evidence selected by the authority.](stages/new-submission.md#new-submission-supporting-evidence)

<a id="new-submission-publicity-recorded"></a>

## new submission publicity recorded

The authority published the submission date and prescribed submission material and notified requesters and other appropriate persons under regulation 34. Exact availability and recipient requirements require review.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1717).

**Used by:**
- [Publish the submission date and specified documents, and notify requesters and other appropriate persons.](stages/new-submission.md#new-submission-publicity)

<a id="new-hearing-requesters-notified"></a>

## new hearing requesters notified

Persons who requested notification and other persons the authority considers appropriate received the regulation 35 hearing notice with date, time, place and examiner name.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1723).

**Used by:**
- [Publish hearing details and examiner name at least six weeks before the hearing, and notify requesters and other appropriate persons.](stages/new-examination.md#new-hearing-notice)

<a id="examination-target-met"></a>

## examination target met

An evidenced duration assessment establishes whether the new examination met the government’s six-month expectation. This is distinct from the statutory pause limit and is not calculated from event dates by this evaluator.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1729).

**Used by:**
- [Government expects examinations to take no longer than six months.](stages/new-examination.md#new-examination-target)

<a id="plan-sound"></a>

## plan sound

Examiner considers it reasonable in all the circumstances to conclude that the new-system plan is sound under s 15D(5),(9)-(12). This is not derived from gateway completion or document presence.

**Type:** boolean. **Assessment:** reviewer judgement. [Canonical definition](../../knowledge/procedures/model.json#L1735).

**Used by:**
- [Recommend modifications and adoption with reasons if they would make it reasonable to conclude that the plan is sound.](stages/new-modifications.md#new-mm-recommendation)
- [Recommend adoption with reasons when the completed examination concludes it reasonable to find the plan sound.](stages/new-reporting.md#new-report-adopt)
- [Recommend withdrawal with reasons when soundness cannot be achieved by modifications and the examination is not paused or to be paused.](stages/new-reporting.md#new-report-withdraw)

<a id="mm-consultation-and-assessments-recorded"></a>

## mm consultation and assessments recorded

Main modifications were consulted upon and the necessary environmental/habitats assessment work undertaken and considered before final recommendation, as described by the new procedure guide.

**Type:** boolean. **Assessment:** reviewer judgement. [Canonical definition](../../knowledge/procedures/model.json#L1741).

**Used by:**
- [Consult on main modifications and undertake necessary environmental and habitats assessment before recommendation.](stages/new-modifications.md#new-mm-consultation)

<a id="pause-notice-recorded"></a>

## pause notice recorded

The examiner notified the authority and Secretary of State of the decision to pause, the matters requiring work and the pause period under PCPA section 15DA(2).

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1747).

**Used by:**
- [Notify the LPA and Secretary of State of the pause, required work and period.](stages/new-pause.md#new-pause-notice)

<a id="pause-within-six-calendar-months"></a>

## pause within six calendar months

The reviewer has checked the notified pause period against the six-calendar-month maximum in section 15DA(3) and regulation 36(1). The evaluator does not approximate months as a fixed number of days.

**Type:** boolean. **Assessment:** reviewer judgement. [Canonical definition](../../knowledge/procedures/model.json#L1753).

**Used by:**
- [A statutory examination pause cannot exceed six months or begin before notification.](stages/new-pause.md#new-pause-maximum)

<a id="pause-notified"></a>

## pause notified

Calendar date on which the examiner gave the authority the section 15DA(2) notice.

**Type:** date. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1759).

**Used by:**
- [A statutory examination pause cannot exceed six months or begin before notification.](stages/new-pause.md#new-pause-maximum)

<a id="pause-begins"></a>

## pause begins

Calendar date on which the notified examination pause begins.

**Type:** date. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1765).

**Used by:**
- [A statutory examination pause cannot exceed six months or begin before notification.](stages/new-pause.md#new-pause-maximum)

<a id="pause-response-contents-recorded"></a>

## pause response contents recorded

The response states what work the authority undertook, sets out proposed modifications or states that none are proposed, and supplies any further soundness evidence the authority has under section 15DA(6).

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1771).

**Used by:**
- [Before pause expiry send the work-response document, proposed modifications or statement of none, and further soundness evidence; publish them.](stages/new-pause.md#new-pause-response)

<a id="pause-response-sent"></a>

## pause response sent

Calendar date on which the authority sent its pause-response material. Retained as evidence metadata; this date alone does not decide whether delivery preceded expiry.

**Type:** date. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1777).

**Used by:**
- Not used in an assertion predicate. It may be routing evidence or retained metadata; consult the routing explanation.

<a id="pause-ends"></a>

## pause ends

Calendar date on which the notified pause period ends. Actual expiry and delivery timing must be checked before concluding that a same-day response was late.

**Type:** date. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1783).

**Used by:**
- Not used in an assertion predicate. It may be routing evidence or retained metadata; consult the routing explanation.

<a id="pause-response-published"></a>

## pause response published

Publication, reg 88 availability and required reg 36(4) notifications recorded, including their timing under reg 36(3)-(4).

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1789).

**Used by:**
- [Before pause expiry send the work-response document, proposed modifications or statement of none, and further soundness evidence; publish them.](stages/new-pause.md#new-pause-response)

<a id="withdrawal-recommended-with-reasons"></a>

## withdrawal recommended with reasons

The examiner recommended withdrawal and gave reasons under the applicable new-system withdrawal condition.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1795).

**Used by:**
- [Recommend withdrawal with reasons if outstanding notified matters leave no prospect of a sound plan at pause end.](stages/new-pause.md#new-pause-withdrawal)
- [Recommend withdrawal with reasons when soundness cannot be achieved by modifications and the examination is not paused or to be paused.](stages/new-reporting.md#new-report-withdraw)

<a id="pause-ended"></a>

## pause ended

The notified pause period has ended, so the post-pause decision condition is being assessed.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1801).

**Used by:**
- [Recommend withdrawal with reasons if outstanding notified matters leave no prospect of a sound plan at pause end.](stages/new-pause.md#new-pause-withdrawal)
- [Resume examination unless withdrawal is recommended under the pause provision.](stages/new-pause.md#new-pause-resumption)

<a id="unresolved-matters-no-soundness-prospect"></a>

## unresolved matters no soundness prospect

At pause end, the examiner considers that the notified matters have not been dealt with and consequently there is no prospect of a sound plan under section 15DA(8). Unfinished work alone does not establish this compound judgement.

**Type:** boolean. **Assessment:** reviewer judgement. [Canonical definition](../../knowledge/procedures/model.json#L1807).

**Used by:**
- [Recommend withdrawal with reasons if outstanding notified matters leave no prospect of a sound plan at pause end.](stages/new-pause.md#new-pause-withdrawal)

<a id="examination-resumed"></a>

## examination resumed

The examination resumed at the end of the pause where no section 15DA(8) withdrawal recommendation was made.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1813).

**Used by:**
- [Resume examination unless withdrawal is recommended under the pause provision.](stages/new-pause.md#new-pause-resumption)

<a id="withdrawal-under-15da8"></a>

## withdrawal under 15da8

The examiner made a withdrawal recommendation under section 15DA(8), determining whether section 15DA(9) requires resumption.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1819).

**Used by:**
- [Resume examination unless withdrawal is recommended under the pause provision.](stages/new-pause.md#new-pause-resumption)

<a id="adoption-recommended-with-reasons"></a>

## adoption recommended with reasons

The examiner recommended adoption and gave reasons under the selected regime’s statutory recommendation condition.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1825).

**Used by:**
- [Recommend adoption with reasons when the completed examination concludes it reasonable to find the plan sound.](stages/new-reporting.md#new-report-adopt)
- [After examination, recommend adoption with reasons where it is reasonable to conclude that the plan is sound and meets the saved legal requirements.](stages/legacy-reporting.md#legacy-report-adopt)

<a id="examination-completed"></a>

## examination completed

The examiner has carried out the independent examination; the final recommendation provisions are now being assessed.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1831).

**Used by:**
- [Recommend modifications and adoption with reasons if they would make it reasonable to conclude that the plan is sound.](stages/new-modifications.md#new-mm-recommendation)
- [Recommend adoption with reasons when the completed examination concludes it reasonable to find the plan sound.](stages/new-reporting.md#new-report-adopt)
- [Recommend withdrawal with reasons when soundness cannot be achieved by modifications and the examination is not paused or to be paused.](stages/new-reporting.md#new-report-withdraw)
- [After examination, recommend adoption with reasons where it is reasonable to conclude that the plan is sound and meets the saved legal requirements.](stages/legacy-reporting.md#legacy-report-adopt)
- [After examination, recommend non-adoption with reasons where the statutory condition for recommending adoption is not met.](stages/legacy-reporting.md#legacy-report-non-adoption)

<a id="paused-or-to-be-paused"></a>

## paused or to be paused

The new-system examination is paused, or the examiner has decided that it is to be paused, so the section 15D(12) withdrawal condition is not yet met.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1837).

**Used by:**
- [Recommend withdrawal with reasons when soundness cannot be achieved by modifications and the examination is not paused or to be paused.](stages/new-reporting.md#new-report-withdraw)

<a id="new-report-publicity-recorded"></a>

## new report publicity recorded

Final new-system recommendations and reasons were published and required notifications sent under regulation 37, using the applicable trigger and any relevant direction exception.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1843).

**Used by:**
- [Publish final recommendations and reasons promptly and notify requesters.](stages/new-reporting.md#new-report-publication)

<a id="adoption-conforms-to-recommendation"></a>

## adoption conforms to recommendation

Adoption is by resolution in accordance with PCPA section 15EA, includes the required recommended modifications and contains only permitted additional changes that do not materially affect content. The reviewer supplies this legal/content judgement.

**Type:** boolean. **Assessment:** reviewer judgement. [Canonical definition](../../knowledge/procedures/model.json#L1849).

**Used by:**
- [Adopt by resolution only in accordance with the Inspector’s recommendation, including required modifications; additional changes must not materially affect content.](stages/new-adoption.md#new-adoption-conditions)

<a id="new-adoption-publicity-recorded"></a>

## new adoption publicity recorded

The adopted plan and adoption statement were made available and required copies/notifications provided under regulation 39 as soon as reasonably practicable.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1855).

**Used by:**
- [Publish the adopted plan and adoption statement and send the statement to requesters as soon as reasonably practicable.](stages/new-adoption.md#new-adoption-publication)

<a id="new-withdrawal-publicity-recorded"></a>

## new withdrawal publicity recorded

The authority made the regulation 38 withdrawal statement available, notified the required consultation participants and ceased the specified availability while retaining the timetable and withdrawal statement.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1861).

**Used by:**
- [Publish withdrawal, notify invited consultation participants and cease specified availability, retaining the withdrawal statement and timetable.](stages/new-withdrawal.md#new-withdrawal-publication)

<a id="submission-date"></a>

## submission date

Calendar date on which this plan was submitted for examination, used with the declared legacy legal basis to assess the ordinary saved-regime deadline or a verified directed deadline.

**Type:** date. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1867).

**Used by:**
- Not used in an assertion predicate. It may be routing evidence or retained metadata; consult the routing explanation.

<a id="directed-legacy-deadline"></a>

## directed legacy deadline

The later plan-specific submission deadline extracted from an applicable Secretary of State direction under SI 2026/169 Schedule 1 paragraph 4(5). Supplying a date alone does not establish that a valid direction exists.

**Type:** date. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1873).

**Used by:**
- Not used in an assertion predicate. It may be routing evidence or retained metadata; consult the routing explanation.

<a id="legacy-direction-verified"></a>

## legacy direction verified

Reviewer has inspected a plan-specific Secretary of State direction under Sch 1 para 4(5), verified that it covers this plan and extracted its later deadline.

**Type:** boolean. **Assessment:** reviewer judgement. [Canonical definition](../../knowledge/procedures/model.json#L1879).

**Used by:**
- Not used in an assertion predicate. It may be routing evidence or retained metadata; consult the routing explanation.

<a id="legacy-savings-eligibility-confirmed"></a>

## legacy savings eligibility confirmed

Reviewer has established and evidenced a specific saving under SI 2026/169 Sch 1, identifying the applicable paragraph and facts. This is an alternative to the ordinary submitted-by-cutoff calculation.

**Type:** boolean. **Assessment:** reviewer judgement. [Canonical definition](../../knowledge/procedures/model.json#L1885).

**Used by:**
- Not used in an assertion predicate. It may be routing evidence or retained metadata; consult the routing explanation.

<a id="pause-response-before-expiry"></a>

## pause response before expiry

Reviewer establishes delivery before the end of the notified pause period, using the notice and actual delivery/receipt evidence. Calendar dates alone do not decide a same-day case.

**Type:** boolean. **Assessment:** reviewer judgement. [Canonical definition](../../knowledge/procedures/model.json#L1891).

**Used by:**
- [Before pause expiry send the work-response document, proposed modifications or statement of none, and further soundness evidence; publish them.](stages/new-pause.md#new-pause-response)

<a id="modifications-and-adoption-recommended-with-reasons"></a>

## modifications and adoption recommended with reasons

Examiner recommends the curative modifications and adoption with those modifications, and gives reasons for the recommendation under s 15D(11).

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1897).

**Used by:**
- [Recommend modifications and adoption with reasons if they would make it reasonable to conclude that the plan is sound.](stages/new-modifications.md#new-mm-recommendation)

<a id="non-adoption-recommended-with-reasons"></a>

## non adoption recommended with reasons

Inspector recommends non-adoption and gives reasons under saved s 20(7A). This may coexist with curative modifications under s 20(7C).

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1903).

**Used by:**
- [After examination, recommend non-adoption with reasons where the statutory condition for recommending adoption is not met.](stages/legacy-reporting.md#legacy-report-non-adoption)

<a id="legacy-adoption-conditions-met"></a>

## legacy adoption conditions met

Adoption is by resolution within saved s 23(2)-(5): as recommended, or with all recommended main modifications; additional modifications together do not materially affect the applicable policies.

**Type:** boolean. **Assessment:** reviewer judgement. [Canonical definition](../../knowledge/procedures/model.json#L1909).

**Used by:**
- [Adopt by resolution only within saved section 23, including required main modifications and the limit on additional modifications.](stages/legacy-adoption.md#legacy-adoption-conditions)

<a id="gateway3-publication-and-notices-recorded"></a>

## gateway3 publication and notices recorded

Gateway 3 advice published as soon as reasonably practicable; same-day availability, requester notifications and copies to persons identified in the advice under reg 31(5), whether requirements are met or not.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1915).

**Used by:**
- [Publish gateway 3 advice and make it available, notify requesters and send copies to persons identified in the advice, whether or not requirements are met.](stages/new-gateway3.md#new-gateway3-publication)

<a id="gateway3-documents-sent"></a>

## gateway3 documents sent

Date the gateway 3 submission documents were sent to the appointed assessor.

**Type:** date. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1921).

**Used by:**
- [Send the gateway 3 submission documents on the gateway request date.](stages/new-gateway3.md#new-gateway3-document-timing)

<a id="existing-new-system-plan-adopted-or-approved"></a>

## existing new system plan adopted or approved

An existing Local Plan has been adopted under s 15EA or approved under Part 2; the reg 18 replacement duty is being assessed.

**Type:** boolean. **Assessment:** recorded observation. [Canonical definition](../../knowledge/procedures/model.json#L1927).

**Used by:**
- [Begin preparation of a replacement Local Plan, by reaching gateway 1, within the five-year period after adoption or approval of the existing new-system plan.](stages/new-timetable.md#new-begin-replacement)

<a id="replacement-gateway1-within-five-years"></a>

## replacement gateway1 within five years

Reviewer verifies that replacement-plan gateway 1 was reached within five years beginning with the day after adoption/approval of the existing new-system plan, using reg 18.

**Type:** boolean. **Assessment:** reviewer judgement. [Canonical definition](../../knowledge/procedures/model.json#L1933).

**Used by:**
- [Begin preparation of a replacement Local Plan, by reaching gateway 1, within the five-year period after adoption or approval of the existing new-system plan.](stages/new-timetable.md#new-begin-replacement)
