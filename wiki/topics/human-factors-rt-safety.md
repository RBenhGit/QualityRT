# Human Factors and Safety Culture in Radiotherapy

**Type:** Topic
**Status:** mature
**Last updated:** 2026-06-18
**Sources:** [human-factors-rt-safety], [chera-normal-accident-theory-2015], [marks-swiss-cheese-2015], [thompson-hazard-detection-education-2017], [mosaly-hfacs-reliability-2015], [gao-emergent-treatments-2015], [evans-causal-factors-2017], [gensheimer-planning-time-2016], [spraker-causal-taxonomy-2017], [walker-incident-factors-2015], [mazur-workload-2013], [mullen-nmri-reliability-2016], [dominello-10yr-qa-2015]

## Summary

Human factors — including supervision quality, staffing levels, fatigue, communication failures, and organizational safety culture — are significant and often underappreciated contributors to radiotherapy safety events. The HFACS (Human Factors Analysis and Classification System) framework applied to RT incident data consistently finds that skill-based errors (routine slips) and supervision failures are the dominant drivers, with organizational climate exerting a 3.37× amplifying effect on personnel risks. Treatment planning is the highest human-factor-risk phase, consistent with FMEA findings.

## Key Facts / Claims

- **Weintraub et al. 2021** (HFACS, JACM): analyzed 141 incidents from SAFRON; Tier distribution: Unsafe Acts 34%, Preconditions 29%, Supervision 33%, Organizational 4% [human-factors-rt-safety]
- **Skill-based errors** are the most common unsafe act in RT — slips during familiar routine tasks performed without conscious attention [human-factors-rt-safety]
- **Inadequate supervision → 25% increased likelihood of decision errors**; decision errors were **6.26× more likely** when supervision failures were present [human-factors-rt-safety]
- "Treatment planning safety events are influenced by slips made without thought while routine tasks are performed" [human-factors-rt-safety]
- **BN-HFACS hybrid model (2024, Frontiers Public Health):** first quantitative causal analysis of RT incidents; 81 events from RO-ILS; skill-based errors have 37.5% prior probability [human-factors-rt-safety]
- **Operator conditions** (fatigue, inattention): 49.6% prior probability — highest precondition [human-factors-rt-safety]
- **Personnel factors** (communication, coordination): 59.8% prior probability [human-factors-rt-safety]
- **Organizational climate** has sensitivity of **3.37** on personnel factors — amplifies communication and coordination failures [human-factors-rt-safety]
- Treatment planning phase has the most errors; specifically "wrong data transfer or setting" [human-factors-rt-safety]
- **CRM (Crew Resource Management) training** adapted from aviation has been shown to improve incident reporting rates in RT departments [human-factors-rt-safety]
- "Failures in communication, leadership, and decision-making in a culture of retribution are known factors contributing to adverse outcomes" [human-factors-rt-safety]
- **Automation introduces new human factor risks**: skill degradation and automation bias (see [[fmea-ai-automated-workflow]]) [human-factors-rt-safety]

### Safety-engineering frameworks borrowed from industry
- **Reason's Swiss Cheese Model (1990):** accidents result when latent failures penetrate successive defensive layers — *organizational → workplace → people → action*; focusing only on individual behavior (incentives/discipline) is a poor strategy because **suboptimally designed layers themselves promote accidents** [marks-swiss-cheese-2015]
- **Hierarchy of effectiveness** (most→least reliable): forcing functions/constraints and automation (technology-focused, "the right thing happens naturally") > simplification/standardization > reminders/checklists/double-checks > rules/policies > training/education (least effective but most-often used) — this is the same ranking used by Clark and the Joint Commission reliability schema [marks-swiss-cheese-2015]
- **Adding process steps (e.g. another checklist) can be *detrimental*** — they cost time and add complexity that can itself raise error risk; interventions should be adopted only if they add value [marks-swiss-cheese-2015]
- The field is critiqued for **lacking patient-outcome-based quality metrics**, relying instead on process measures, satisfaction scores, and incident counts [marks-swiss-cheese-2015]
- A standard safety glossary distinguishes **slip** (doing something unintended, observable), **lapse** (failing to do something intended, often unobservable), and **mistake** (a purposeful action based on incorrect knowledge/judgment) [marks-swiss-cheese-2015]
- **Normal Accident Theory (Perrow):** failures are *normal* and expected in complex systems; systems are characterized by **linear vs interactively complex** and **loosely vs tightly coupled** [chera-normal-accident-theory-2015]
- Radiation oncology processes map across this grid: conventionally fractionated EBRT is relatively linear/loosely-coupled, while **emergent after-hours treatment, cranial SRS, and system commissioning are more tightly coupled** (failures hard to detect/correct in time) [chera-normal-accident-theory-2015]
- **Emergent treatments carry higher risk**: a companion study (Gao et al.) found severe near-misses more frequent with emergent treatment, especially weekend/holiday initiation — mitigated by process standardization, dedicated/isolated emergent workflows, verbal timeouts, and dual (physician + physicist) pretreatment chart checks [chera-normal-accident-theory-2015]
- **"Safety mindfulness"** — leadership-modeled, persistent proactive focus on safety that accepts failures will occur — is the proposed global strategy [chera-normal-accident-theory-2015]
- **Trainee hazard/incident detection ability is low** (sensitivity 0–0.35 on video tests, little improved by training); interprofessional silos are stark (40–50% of trainees rarely interact across disciplines); simulation training was no better than discussion for detection but was rated more valuable [thompson-hazard-detection-education-2017]
- **HFACS (Shappell & Wiegmann)**, built on Reason's Swiss Cheese Model, classifies events into 4 main levels (organizational influence, unsafe supervision, preconditions, unsafe acts) and 12 sublevels; RO-ILS's causal-factor structure closely mirrors it [mosaly-hfacs-reliability-2015]
- HFACS is **reliable in RT**: with 1 hour of training, novices reached ~80% agreement (66–97%) with experts on the 4 main levels, but only ~66% (50–82%) on the 12 sublevels — so detailed sublevel coding should not be delegated to untrained staff (≥65% inter-rater agreement is the accepted reliability threshold) [mosaly-hfacs-reliability-2015]

### Emergent treatments are higher-risk (Gao et al.)
- Emergent/after-hours treatments (~12% of cases; indications: intractable pain 42%, neurologic decline 24%, tumor progression 15%) had **fewer reported near-misses per treatment (0.37 vs 0.86, p<.01) but higher severity** — mean NMRI 1.9 vs 1.48, and NMRI-4 (critical) 14% vs 4% (p=.002) [gao-emergent-treatments-2015]
- **Weekend/holiday-initiated emergent treatments had 37% critical (NMRI-4) events vs 7.9% on weekdays** (p=.003), despite weekend starts being only ~3% of treatments [gao-emergent-treatments-2015]
- **53% of emergent near-misses originated in treatment planning** (vs 33% non-emergent), most at "plan information transfer" (23%); 42% were caught at pretreatment plan check (physics plan review 30%, therapist chart check 11%) [gao-emergent-treatments-2015]
- Dominant emergent root causes: communication (28%), failure to detect a developing problem/loss of attention (25%), poor judgment due to time limitation (13%); physics chart check is ~63% effective at detecting near-misses [gao-emergent-treatments-2015]
- Mitigations adopted: mandatory **resimulation for transferred patients**, in-house automated plan-checking script, and checklists/timeouts (cf. AAPM TG-201 data-transfer QA, forthcoming TG-230 checklists) [gao-emergent-treatments-2015]

### Causal-factor structure & complexity (vs. time pressure)
- Events have **multiple causes, never one**: a median of **7 causal factors per event, with no event having a single cause** — concrete empirical support for the systems/Swiss-Cheese view over "root cause"/"bad apple" thinking (causal-factor coding kappa ≈ 0.77) [evans-causal-factors-2017]
- **High-severity (high-NMRI) events cited poor human-factors engineering as a causal factor >2× as often as low-severity events** — a concretely fixable, vendor-addressable lever [evans-causal-factors-2017]
- Comparing a high-reporting institution (≈10% actual incidents) vs international SAFRON data (>80% actual incidents), SAFRON showed ~double the "inadequate policy" and human-behavior (slip/poor-judgment) causal factors — speculatively, mature high-volume incident learning bolsters policy and lowers human-error permeability [evans-causal-factors-2017]
- The current RO-ILS taxonomy under-represents **cognitive bias** (only "expectation bias" listed) despite Joint Commission emphasis; proposed additions include machine downtime, hardware failure, failure-to-follow-through on QI, and misleading workflow documentation [evans-causal-factors-2017]
- **Treatment complexity, not planning time, drives errors:** across 2,257 courses, time from simulation to first treatment was *not* predictive of severe (grade 3–4) near-misses on multivariate analysis once technique was controlled [gensheimer-planning-time-2016]
- **SBRT (18% vs 11%) and pediatric (18% vs 11% adult) treatments were the most error-prone** — technical and clinical complexity, respectively — so safety interventions should target complexity rather than simply slowing workflows [gensheimer-planning-time-2016]
- Only 8 of 2,257 courses (0.4%) had an error reach the patient (all no-harm); a high near-miss reporting rate is associated with *lower* complication rates (a healthy safety-culture signal, not an unsafe one) [gensheimer-planning-time-2016]
- The AAPM causal-factor taxonomy (7 top-level categories, 19 subcategories, **93 specific factors**) applied to 300 events: **"slip causing physical error" was the most common factor (94% of SAFRON vs ~50% of institutional events)**; "loss of attention" 78% vs ~34%; negligence/poor judgment were rare [spraker-causal-taxonomy-2017]
- **Poor human-factors engineering was the only factor more common in high-risk (33%) than low-risk (13%) institutional events** — the most concretely vendor-fixable lever [spraker-causal-taxonomy-2017]
- Communication problems were more prominent in the high-reporting institutional data (poor/incomplete ~41–47%) than in SAFRON (16%); causal factors are broadly similar across near-miss vs incident events, so fixing near-miss causes should reduce incidents [spraker-causal-taxonomy-2017]

### Predictors of incidents (Walker et al., MD Anderson)
- 189 incidents among 326,448 fractions (rate 136/10,000 patients): **37% originated in treatment planning, 30% in treatment delivery** [walker-incident-factors-2015]
- Multivariate predictors of *planning* incidents: **fewer days from plan approval to start (rushed), fewer fractions, more prescription items, longer beam duration** (i.e., complexity + time pressure) [walker-incident-factors-2015]
- Multivariate predictors of *delivery* incidents: **first day of treatment (OR 3.47), fewer fractions, more prescription items, longer beam duration; IMRT was associated with a *lower* delivery-incident rate** (automation/complexity-reduction benefit) [walker-incident-factors-2015]
- Walker found rushed timelines *do* associate with planning incidents, whereas [gensheimer-planning-time-2016] found no time effect once technique was controlled — the discrepancy is attributed to differing severity thresholds and explicit modeling of the planning-time × technique interaction [walker-incident-factors-2015]

### A "no rushed treatment" intervention reduces errors (Dominello et al., 10-yr Wayne State data)
- Over 2004–2014 (250,568 treatments, 461 delivery errors) the overall delivery-error rate was **0.18%/fraction**; a **"no rushed treatment" policy (Jan 2011)** that avoids universal large-scale replanning (LSR) when a unit is down ≤1 day cut the rate from **0.24% before to 0.08% after (p<.001)** [dominello-10yr-qa-2015]
- **Large-scale replanning fell from 18 to 4.5 episodes/year**, and the share of errors attributable to LSR dropped from 21% to 12%; **14 error reports explicitly named a rushed environment as causal** — corroborating the time-pressure→error link [dominello-10yr-qa-2015]
- **Weekend simulation/treatment error rate was ~14× higher: 1.3% vs 0.09%/fraction (p<.001)** — emergent weekend work is a distinct hazard (consistent with Gao); but there was *no* time-of-day effect within the day (p=.631) [dominello-10yr-qa-2015]
- **Complexity drives site-specific risk**: skin (0.067/course) and breast (0.050/course) were most error-prone; breast made up 41% of errors (bolus errors alone 13/45) — echoing Walker's "prescription items" complexity predictor; IMRT had a *lower* per-course deviation (0.006) than non-IMRT EBRT (0.026) [dominello-10yr-qa-2015]
- Reporting-culture gap: therapists + dosimetrists filed nearly all reports; there were **zero nurse-reported and only one physician-reported** error — underscoring the need for a non-punitive, all-discipline reporting system [dominello-10yr-qa-2015]

### Workload measurement and risk-scoring reliability
- Physician treatment-planning **workload can be quantified** subjectively (NASA-TLX) and objectively (pupil diameter ↑, blink rate ↓ under load); workload was higher for complex (NASA-TLX 66) than simple (49) cases and higher for residents than faculty [mazur-workload-2013]
- **Performance (willingness to approve a plan) declined sharply above a NASA-TLX "redline" of ~55** — mirroring the ≥50 threshold used in aviation/other industries — suggesting workload could serve as an independent QA metric [mazur-workload-2013]
- The **Near-Miss Risk Index (NMRI)** showed only *fair* inter-rater reliability among general staff (Krippendorff's α 0.38), improving to *moderate* with frequent ILS participation (0.50) and **higher still during multidisciplinary ILS meetings (0.61)** [mullen-nmri-reliability-2016]
- Physicians and dosimetrists scored most consistently; nurses and therapists least — and NMRI reliability is comparable to the AHRQ Harm Score, supporting **multidisciplinary (not individual) near-miss review** [mullen-nmri-reliability-2016]

## HFACS 4-Tier Hierarchy Applied to RT

| Tier | Category | Key RT Findings |
|---|---|---|
| 1 | Unsafe Acts (34%) | Skill-based errors most common; decision errors during QA tasks |
| 2 | Preconditions (29%) | Fatigue/inattention (49.6%); poor communication (59.8%) |
| 3 | Supervision (33%) | Inadequate supervision → 6.26× decision error risk |
| 4 | Organizational (4%) | Safety climate multiplies personnel risk (sensitivity 3.37) |

## Key Recommendations Across Studies

1. Include supervisory influences in all safety improvement efforts
2. Workload rationalization to reduce operator fatigue and inattention
3. Systematic peer verification for information transfer during planning approval
4. Standardized written procedures to minimize verbal communication errors
5. CRM training adapted from aviation for teamwork and communication
6. Blame-free safety reporting culture (just culture)
7. Environmental improvements: lighting, equipment interface design

## Connections

- [[ro-ils]] — RO-ILS and SAFRON provide the incident data analyzed in human factors studies; just culture principle in RO-ILS directly addresses HFACS Tier 3–4 findings
- [[fmea-radiotherapy]] — HFACS confirms the same high-risk stages as FMEA: treatment planning, data transfer, patient setup
- [[fmea-ai-automated-workflow]] — automation introduces new human factor risks: skill degradation, automation bias, reduced vigilance during manual review
- [[incident-learning-systems-international]] — SAFRON data was used in the Weintraub HFACS study; RO-ILS data used in BN-HFACS study
- [[rt-patient-safety-context-map]] — human factors/staffing is a key gap identified in the context map; this page addresses it
- [[radiation-safety-culture-healthcare]] — IAEA's 10 Safety Culture Traits provide the organizational framework within which human factor risks operate; organizational climate (HFACS Tier 4) directly maps to safety culture deficiencies; Just Culture principle is shared
- [[peer-review-radiotherapy]] — peer review and verbal timeouts are "double-check" defenses in the hierarchy of effectiveness; emergent treatments use dual chart checks
- [[rt-quality-management]] — the hierarchy of effectiveness and Swiss Cheese layering guide how a QM program selects interventions
- [[rt-accidents-aviation-lessons]] — the same human-factors core (SHEL/SHELL, just culture, system-not-individual) and aviation CRM lineage
- [[advanced-modality-rt-safety]] — "forced time-outs," halt-authority, and the time-pressure hazard recur in the IMRT/SRS-SBRT white papers
- [[brachytherapy-hdr-safety]] — human error caused 97/147 NRC brachytherapy events; persistent wrong-patient/wrong-side failures are human-factors targets

## Open Questions

- What is the quantitative relationship between staffing ratios and RT error rates?
- How does shift length and time-of-day affect skill-based error rates in RT?
- What does a validated CRM training curriculum for radiation oncology look like?
- How do human factor risks interact with automation risks as workflows become more automated?

## Raw Notes

- Weintraub 2021 (HFACS, JACM): https://pmc.ncbi.nlm.nih.gov/articles/PMC8504582/
- BN-HFACS hybrid 2024 (Frontiers Public Health): https://pmc.ncbi.nlm.nih.gov/articles/PMC11169683/
- CRM training in RT (PMC): https://pmc.ncbi.nlm.nih.gov/articles/PMC8020487/
- PSNet Radiation Safety primer: https://psnet.ahrq.gov/primer/radiation-safety
- Human Factors and Systems Engineering in RT (Red Journal 2007): https://www.redjournal.org/article/S0360-3016(07)04291-5/fulltext
- Risks in Oncology and RT (NCBI Bookshelf): https://www.ncbi.nlm.nih.gov/books/NBK585623/
- [chera-normal-accident-theory-2015]: Chera BS, Mazur L, Marks LB, "Applying Normal Accident Theory to radiation oncology: Failures are normal but patient harm can be prevented," *Pract Radiat Oncol* 5:325–327 (2015). Commentary on Gao et al. emergent-treatment near-miss study.
- [marks-swiss-cheese-2015]: Marks LB, Pawlicki TA, Hayman JA, "Learning to Appreciate Swiss Cheese and Other Industrial Engineering Concepts" (editorial), *Pract Radiat Oncol* 5:277–281 (2015). Source of the hierarchy-of-effectiveness figure and safety glossary; RO-ILS at 64 centers/620 events at time of writing.
- [thompson-hazard-detection-education-2017]: Thompson R et al., "Hazards and incidents: Detection and learning in radiation medicine, a comparison of 2 educational interventions," *Pract Radiat Oncol* (2017), doi:10.1016/j.prro.2017.02.006.
- [mosaly-hfacs-reliability-2015]: Mosaly PR, Mazur L, et al., "Application of human factors analysis and classification system model to event analysis in radiation oncology," *Pract Radiat Oncol* 5:113–119 (2015). UNC "Good Catch" program.
- [gao-emergent-treatments-2015]: Gao W, Nyflot MJ, et al., "Can emergent treatments result in more severe errors? An analysis of a large institutional near-miss incident reporting database," *Pract Radiat Oncol* 5:319–324 (2015). Univ. of Washington.
- [evans-causal-factors-2017]: Evans SB, "Causal Factors for Error in Radiation Oncology" (commentary), *Pract Radiat Oncol* (2017), doi:10.1016/j.prro.2017.06.005. Comments on the near-miss/adverse-event comprehensive causal-factor taxonomy study (institutional vs SAFRON data).
- [gensheimer-planning-time-2016]: Gensheimer MF, Zeng J, ... Ford EC, "Influence of planning time and treatment complexity on radiation therapy errors," *Pract Radiat Oncol* 6:187–193 (2016). Univ. of Washington.
- [spraker-causal-taxonomy-2017]: Spraker MB, Fain R, Gopan O, ... Ford E, "Evaluation of near-miss and adverse events in radiation oncology using a comprehensive causal factor taxonomy," *Pract Radiat Oncol* 7:346–353 (2017). 300 events (institutional + SAFRON); validates AAPM/RO-ILS causal-factor taxonomy.
- [walker-incident-factors-2015]: Walker GV, ... Das P, "Factors associated with radiation therapy incidents in a large academic institution," *Pract Radiat Oncol* 5:21–27 (2015). MD Anderson.
- [mazur-workload-2013]: Mazur LM, Mosaly PR, Hoyle LM, Jones EL, Marks LB, "Subjective and objective quantification of physician's workload and performance during radiation therapy planning tasks," *Pract Radiat Oncol* 3:e171–e177 (2013). UNC; NASA-TLX redline ~55.
- [mullen-nmri-reliability-2016]: Mullen T, Nyflot MJ, ... Ford EC, "Interrater reliability of a near-miss risk index for incident learning systems in radiation oncology," *Pract Radiat Oncol* 6:429–435 (2016). Univ. of Washington.
- [dominello-10yr-qa-2015]: Dominello MM, Paximadis P, Zaki M, Hammoud A, Campbell S, Komajda M, Dyson G, Bossenberger T, Burmeister J, "Ten-year trends in safe radiation therapy delivery and results of a radiation therapy quality assurance intervention," *Pract Radiat Oncol* 5:e665–e671 (2015). Wayne State / Karmanos; "no rushed treatment" / no-LSR policy; uses Radiation Error Scoring System (Konski 2009).
