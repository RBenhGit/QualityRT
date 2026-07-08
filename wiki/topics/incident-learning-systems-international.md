# International Radiotherapy Incident Learning Systems

**Type:** Topic
**Status:** mature
**Last updated:** 2026-07-08
**Sources:** [incident-learning-systems-international], [ford-ils-consensus-2012], [nyflot-ils-metrics-2015], [kim-ils-tbi-impact-2017], [rosis-cunningham-2010], [clark-5yr-incident-learning-2013], [pawlicki-ils-levels-2017], [incident-reporting-xlsx-il]

## Summary

Multiple national and international incident learning systems (ILS) exist for radiation oncology alongside RO-ILS (U.S.). The global landscape is anchored by SAFRON (IAEA, global), ROSIS (Europe/ESTRO), and RO-ILS (USA), with national systems in Canada (NSIR-RT), the UK (NRLS), and developing programs in Australia/New Zealand. Systems differ in scope, governance, legal protections, and degree of specialty-specificity. RO-ILS is by far the largest, with 41,516 events from 781 facilities as of 2024.

## Key Facts / Claims

- **RO-ILS 10-year report (Ford et al., IJROBP, 2026):** 781 facilities enrolled; 41,516 events — largest volume of any national or international RT incident learning system [incident-learning-systems-international]
- 24% of RO-ILS events were actual incidents reaching patients; ~10% rated potentially severe or critical [incident-learning-systems-international]
- Over 100 educational releases issued by RO-ILS (case studies, safety notices, webinars, themed reports) [incident-learning-systems-international]
- **ROSIS (Radiation Oncology Safety Information System):** Founded 2001; European, supported by ESTRO; first major shared incident learning system in RT; collected first 1,074 reports [incident-learning-systems-international]
- **ROSIS first-1074 analysis (Cunningham et al. 2010):** 101 departments (70 European, rest global), 1,074 reports (Jan 2003–Aug 2008); web forms launched Jan 2003 (ESTRO server), dedicated www.rosis.info site Oct 2004; grew out of the EU-funded ESQUIRE project [rosis-cunningham-2010]
- ROSIS departments covered ~150,000 patients/yr ≈ **3% of the world's ~5.1 million annual RT patients** (UNSCEAR) [rosis-cunningham-2010]
- ROSIS defines an **incident as any incorrect delivery of radiation**; **97.7% of reports were external beam, 1.9% brachytherapy**; ~51% resulted in some incorrect delivery [rosis-cunningham-2010]
- Where treatment was undetected before delivery, on average **22% of prescribed fractions were delivered incorrectly** (mostly minor dosimetric consequence) [rosis-cunningham-2010]
- **Most incidents originate in pre-treatment but are detected later**: only 258 of process-related incidents caught before treatment vs 754 at the treatment sub-process [rosis-cunningham-2010]
- Top detection methods: **"found at time of patient treatment" (43%) and chart-check (33%)**; radiation therapists at the treatment unit detected ~56% of incidents [rosis-cunningham-2010]
- ROSIS documented a **near-incident-to-incident ratio of 13.8:1** for treatment-preparation errors (Holmberg & McClean), underscoring large under-reporting of near misses [rosis-cunningham-2010]
- Participating departments used an average of **7 QA/QC methods ("defence-in-depth")**; least common were in-vivo dosimetry (34%) and formal quality management systems (35%) [rosis-cunningham-2010]
- "Working with awareness" (vigilant staff) detected as many incidents as chart-check + in-vivo dosimetry + portal imaging combined — a core safety-culture behaviour [rosis-cunningham-2010]
- **SAFRON ("Safety Reporting and Learning System for Radiotherapy," IAEA Division of Nuclear Safety & Security — see [pawlicki-ils-levels-2017] below for the authoritative expansion):** IAEA-launched December 2012; global scope; >50 registered facilities worldwide; >1,300 reports; developed by some of the same people as ROSIS [incident-learning-systems-international]
- **UK NRLS:** NHS-administered, national but not RT-specific; less detailed for radiation oncology than RO-ILS [incident-learning-systems-international]
- **Canada NSIR-RT / CARS-PSO:** Developed following AAPM 2012 Work Group on Prevention of Errors report (same report that informed RO-ILS) [incident-learning-systems-international]
- **Australia/New Zealand:** RANZCR has explored centralized reporting; national system in development as of 2022 [incident-learning-systems-international]
- **Ford 2018 review** (*Medical Physics*): most comprehensive comparative analysis of global RT incident learning systems [incident-learning-systems-international]
- A real departmental incident-reporting dataset (Israel, bilingual Hebrew/English, 1,014 records, 2004–2026) independently converged on a nearly identical field structure to the AAPM consensus Reporter's form (18 fields), a dual medical/dosimetric severity scale, and a keyword taxonomy explicitly crosswalked to RO-ILS/AAPM causal-factor English terminology — see [[departmental-incident-reporting-dataset-il]] for full detail [incident-reporting-xlsx-il]

### ILS database structure (AAPM consensus, Ford et al. 2012)
- The **AAPM Work Group on the Prevention of Errors (WGPE)** produced consensus recommendations for RT incident-learning database structures (workshop April 14–15, 2011, Washington DC; published *Med Phys* 2012); reviewed/approved by AAPM, ASTRO, and SROA [ford-ils-consensus-2012]
- Participation from ASTRO, ACR, NIH, CRCPD, AAMD, ASRT, COMP, and Dr. Ola Holmberg (core ROSIS/SAFRON architect) — broad North American consensus with deliberate international compatibility [ford-ils-consensus-2012]
- Five standardized structural components: **definitions, process maps, severity scales, causal taxonomy, and data elements** [ford-ils-consensus-2012]

#### Functional Requirements (Table I — ranked by priority)
The consensus paper defines 14 key functional requirements for any ILS, in approximate priority order [ford-ils-consensus-2012]:

| Priority | Requirement | Notes |
|---|---|---|
| 1 | **Electronic** | Ease of use; data mining; interconnectivity |
| 2 | **Ease of use** | Especially for front-line reporters; target <1 min entry |
| 3 | **Provide feedback** | To both the clinic and the person reporting |
| 4 | **Compliant with standard** | Supports extra-institutional data sharing |
| 5 | **Validated with test-case scenarios** | Test cases also useful for training users |
| 6 | **Statistical analysis & filtering** | Filtering by process map step, cause, and other fields |
| 7 | **Support for near-miss incidents** | Near-misses are the primary learning signal |
| 8 | **Tools for incident investigation** | RCA structures, severity tagging |
| 9 | **Semi-anonymous reporting** | Option must exist; rarely used = sign of good culture |
| 10 | **Corrective action tracking** | Management system for tracking follow-up |
| 11 | **Multisite support** | For national/international distributed systems |
| 12 | **Workflow tools** | Alerts to managers, escalation pages |
| 13 | **Secure communication tools** | Tools for communicating between users |
| 14 | **Clear reporting threshold** | Ensure consistency in what is considered reportable |

#### Process Maps
- Consensus **process maps** define **91 process steps for EBRT and 88 for brachytherapy**, across 8 phases: patient assessment → imaging for RT planning → treatment planning → pre-treatment review and verification → treatment delivery → on-treatment QM → post-treatment completion → equipment/software QM [ford-ils-consensus-2012]
- **35 (EBRT) / 32 (brachytherapy) "safety barriers"** (SBs) are identified within those steps — process steps whose primary function is to stop an error from occurring or propagating [ford-ils-consensus-2012]
- Key SBs include: patient ID verification (dual method), pathology report review, peer review of treatment decision (tumor board), independent dose calculation, IMRT QA, time-out at treatment delivery, image-guided verification, in-vivo dosimetry, weekly physics/physician/therapist chart checks [ford-ils-consensus-2012]
- Process map differs from TG-100's IMRT process tree: the most notable difference is the explicit labeling of safety barriers — deliberately excluded from TG-100 because FMEA handles barriers through the detectability score [ford-ils-consensus-2012]

#### Severity Scales (Two Complementary Scales)
**Medical severity scale (0–10):**

| Score | Consequence |
|---|---|
| 10 | Premature death |
| 8/9 | Life-threatening — intervention essential; possible recurrence from underdose |
| 7 | Permanent major disability (or grade 3/4 permanent toxicity) |
| 5/6 | Permanent minor disability (or grade 1/2 permanent toxicity) |
| 3/4 | Temporary side effects — major treatment/hospitalization |
| 2 | Temporary side effects — intervention indicated |
| 1 | Temporary side effects — intervention not indicated |
| 0 | No harm |

**Dosimetric deviation scale (1–10):**

| Score | Dose Deviation |
|---|---|
| 9/10 | >100% absolute deviation from total prescription to any structure |
| 7/8 | >25–100% absolute deviation |
| 5/6 | >10–25% absolute deviation |
| 3/4 | >5–10% absolute deviation |
| 1/2 | <5% absolute deviation |

- Both scales must be assigned for every incident — large dosimetric deviation can have minor clinical consequence and vice versa; the two scales must never be conflated [ford-ils-consensus-2012]
- An additional **Clinical Action Scale (A–D)** guides follow-up priority independently of severity: A = highest priority (notify senior management, supervisor, physician immediately); B–D = decreasing urgency. Some low-severity incidents (e.g., wrong MRN entry) receive high action scores due to downstream cascade risk [ford-ils-consensus-2012]

#### Causal Taxonomy (Six Top-Level Categories)
The taxonomy is designed to be used by individuals with varied expertise; robustness, ease of use, and inter-system mappability are the four design criteria [ford-ils-consensus-2012]:

| Category | Key Subcategories |
|---|---|
| **1. Organizational management** | Staffing, capital resources, policies/procedures, training, communication, physical environment, leadership/safety culture |
| **2. Technical** | Acceptance testing/commissioning, equipment design, maintenance failures, IT/environment |
| **3. Human behavior** | Acting outside scope, slip, poor judgment, language issues, intentional violations, negligence |
| **4. Patient-related** | Misleading representation, cognitive/language issues, non-compliance, physical inability |
| **5. External factors** | Natural environment, hazards (beyond facility control) |
| **6. Procedural issues** | Failure to detect, interpret, select correct rule, develop effective plan, or execute plan |

- Root-cause analysis pitfalls explicitly named: (1) blaming an individual as the only cause; (2) focusing exclusively on staffing; (3) focusing too heavily on policies/procedures in isolation — all have weak impact on behavior [ford-ils-consensus-2012]

#### Three-Level Data Element Structure
- **Level 1 — Reporter's form**: 18 elements; completed by front-line reporter; designed for <1 minute entry; includes date, incident type (actual/near-miss/unsafe), person affected, fractions delivered incorrectly, narrative description, where found, treatment modality [ford-ils-consensus-2012]
- **Level 2 — Analyst's form**: 38 elements; completed by a second investigator; includes medical/dosimetric severity, causal taxonomy, process step of origin, equipment/system details, staff roles, patient demographics [ford-ils-consensus-2012]
- **Level 3 — Responder's form**: 7 elements; completed as part of follow-up; tracks safety barriers that prevented/failed to prevent propagation, corrective action, preventive action, learning actions, closure [ford-ils-consensus-2012]
- Elements flagged as "Required," "Recommended," or "Optional"; data to be shared across institutions requires stripping/encrypting patient-identifying fields [ford-ils-consensus-2012]

#### Operational Recommendations
- A **written policy** must govern ILS operations; one person must be identified as responsible for initial report review [ford-ils-consensus-2012]
- **Investigation timelines**: serious incidents → initial investigation by next business day (involving individual, domain members, supervisor, senior management); minor incidents/near-misses → within 10 working days [ford-ils-consensus-2012]
- **Aviation analogy**: CAST (Commercial Aviation Safety Team) reduced fatal accident risk by 73% in 10 years through systematic investigation of crashes and near-misses — the model for radiation oncology ILS [ford-ils-consensus-2012]
- These consensus structures are the direct basis for RO-ILS and several national/departmental systems [ford-ils-consensus-2012]

### Departmental ILS impact & metrics (Univ. of Washington)
- A departmental near-miss ILS logged **1,897 reports over 2 years (1.0 report/patient)** — far higher volume than most prior RT systems, reflecting a strong reporting culture [nyflot-ils-metrics-2015]
- A **Near-Miss Risk Index (NMRI), 0–4** (none/mild/moderate/severe/critical), was developed to prioritize near-miss events; combines severity and probability like an FMEA risk score [nyflot-ils-metrics-2015]
- **Proposed metrics of ILS "success":** rising report volume, rising number of unique reporters, declining mean NMRI over time, broad distribution of reports across staff roles and workflow steps, and a low fraction of anonymous reports [nyflot-ils-metrics-2015]
- Mean NMRI fell significantly over the first year (1.68 → 1.42, p<.001); reporting was broadly distributed (therapists 35%, dosimetrists 29%, physicists 24%); <2% anonymous [nyflot-ils-metrics-2015]
- Highest-risk near-misses **originated in imaging for treatment planning** and were most often **caught in on-treatment QM** (weekly physics checks, portal/CBCT review) [nyflot-ils-metrics-2015]
- AHRQ Hospital Survey data show higher incident-reporting rates correlate with **fewer** actual safety incidents — supporting high-volume reporting as a positive sign [nyflot-ils-metrics-2015]
- Using total body irradiation (TBI) as a model, an ILS generated **117 quality-improvement interventions** over 3.5 years; classified by Joint Commission reliability schema, only **11% were "Most Reliable" (forcing functions/automation), 17% "Somewhat Reliable" (checklists/standardization), and 72% "Least Reliable" (training/policy)** [kim-ils-tbi-impact-2017]
- High-reliability interventions clustered on equipment/IT and human-error events; **communication was the most common causal factor but yielded the lowest-quality interventions** [kim-ils-tbi-impact-2017]
- FMEA is repeatedly cited as a useful **complement** to reactive incident learning [kim-ils-tbi-impact-2017]

### 5-year program outcomes (Clark et al., Ottawa Hospital)
- Over 5 years (2007–2011): **2,506 incident reports across 345,792 treatments (0.7% incident rate); only 49 (1.95%) reached/impacted a patient** [clark-5yr-incident-learning-2013]
- A **54% decrease in serious incidents in the first year**, sustained thereafter — among the strongest published evidence that ILS reduces real harm [clark-5yr-incident-learning-2013]
- **70–80% of incidents were caused by lack of, inadequate, or failure to follow standard procedures**; next most common causes were communication and work-planning issues [clark-5yr-incident-learning-2013]
- Treatment preparation originated >50% of all incidents, but **treatment delivery was the most vulnerable point for incidents that actually reached patients**; 35% of nonminor actual incidents were incorrect patient setup/shifts [clark-5yr-incident-learning-2013]
- **Tomotherapy units (integrated planning + imaging, minimal data transfer) were markedly less error-prone**: 7 of 142 treatment-unit incidents, none patient-impacting [clark-5yr-incident-learning-2013]
- Interventions favored the US NCPS "stronger actions" (forcing functions, interlocks, process simplification, table indexing, beam-name standardization) over weaker ones (double checks, reminders, training) [clark-5yr-incident-learning-2013]
- A cumbersome hospital-wide electronic reporting interface **cut reporting volume nearly in half** (150.8 → 78.6 reports/quarter), prompting reversion to paper — usability is decisive for ILS uptake [clark-5yr-incident-learning-2013]
- A key cultural benefit was **bridging the professional silos** between radiation therapy, radiation oncology, and medical physics [clark-5yr-incident-learning-2013]

### Local / national / international levels (Pawlicki et al. 2017)
- ILS operate at three levels — **local, national, international** — with the same goals; larger (national/international) pools enable wider comparison and faster learning, while local systems give the granular detail needed to interrogate which safety barrier failed [pawlicki-ils-levels-2017]
- **ROSIS evolved into ROSEIS** (Radiation Oncology Safety Education and Information System) and was absorbed into the ESTRO platform after the original ROSIS's lack of dedicated funding threatened its sustainability (vendor support from Elekta/Varian helped) [pawlicki-ils-levels-2017]
- **SAFRON = "Safety Reporting and Learning System for Radiotherapy,"** managed by the IAEA Division of Nuclear Safety & Security; ROSEIS and SAFRON taxonomies are **broadly compatible** to enable cross-jurisdiction data sharing [pawlicki-ils-levels-2017]
- **European Council Directive 2013/59/EURATOM (Article 62) makes recording and analysing accidental/unintended exposures a legal requirement** for EU member states [pawlicki-ils-levels-2017]
- The Canadian **NSIR-RT taxonomy** (Milosevic et al. 2016) has 6 data groups — impact, discovery, patient, details, treatment delivery, investigation — with 35 items; a good taxonomy must be intuitive, robust (inter-rater consistent), and mappable to other systems [pawlicki-ils-levels-2017]
- Investigators often lack formal training in event analysis; structured methods (e.g. the **London Protocol**, Canadian Patient Safety Institute framework, TreatSafely Foundation courses) address this [pawlicki-ils-levels-2017]
- Ganesh's literature estimate: **~600 events typically occur before a major accident** — reinforcing the value of capturing near misses [pawlicki-ils-levels-2017]

## System Comparison

| System | Region | Launch | Governance | Scale | Legal Protection |
|---|---|---|---|---|---|
| RO-ILS | USA | 2014 | ASTRO/AAPM | 41,516 events | PSQIA federal |
| ROSIS | Europe | 2001 | ESTRO | ~1,074+ | Varies by country |
| SAFRON | Global | 2012 | IAEA | ~1,300+ | Varies by country |
| NRLS | UK | 2003 | NHS | All-specialty | NHS framework |
| NSIR-RT | Canada | ~2013 | National | Specialty-specific | Canadian PSO law |
| RANZCR | AUS/NZ | In development | RANZCR | National | TBD |

## Connections

- [[ro-ils]] — RO-ILS is the U.S. system; this page provides the international context and comparison
- [[iaea-safety-reports-17]] — IAEA is the governance body behind SAFRON; same organization behind the foundational safety reports
- [[human-factors-rt-safety]] — SAFRON data used in HFACS analysis studies; ROSIS data used in comparative research
- [[rt-patient-safety-context-map]] — international ILS landscape is a key gap identified in the context map
- [[radiation-safety-culture-healthcare]] — Trait 8 (Problem Identification and Resolution) and Trait 9 (Environment for Raising Concerns) are the safety culture prerequisites for effective incident learning; ILS only works when staff don't fear retaliation for reporting; declining NMRI and rising report volume track measurable safety-culture improvement
- [[fmea-radiotherapy]] — FMEA (proactive) and incident learning (reactive) are complementary; the consensus causal taxonomy and severity scales deliberately differ from TG-100's FMEA scales but cover similar ground
- [[tg100-aapm]] — the consensus ILS process maps parallel (but differ from) the TG-100 IMRT process tree; TG-100 omits "safety barriers" because FMEA handles barriers via the detectability score
- [[rt-accidents-aviation-lessons]] — incident learning's rationale (Heinrich 1:30:300) and the critique of counting reports vs. learning
- [[brachytherapy-hdr-safety]] — the NRC brachytherapy event database is a mandatory incident-reporting complement to voluntary ILS
- [[departmental-incident-reporting-dataset-il]] — a real, primary-source departmental ILS dataset (1,014 incidents, 2004–2026) whose structure closely parallels the AAPM/Ford consensus recommendations documented on this page

## Open Questions

- What are the exact reporting rates per facility in SAFRON vs. RO-ILS?
- How does the absence of PSQIA-equivalent protection in European/global systems affect reporting rates?
- Has a formal comparison of failure mode distributions across RO-ILS, ROSIS, and SAFRON been published?
- What is the current status of the Australian/New Zealand national RT ILS?

## Raw Notes

- RO-ILS 10-year report (Ford et al. 2026, IJROBP): https://pubmed.ncbi.nlm.nih.gov/41218661/
- Ford 2018 review (*Medical Physics*): https://aapm.onlinelibrary.wiley.com/doi/full/10.1002/mp.12800
- SAFRON (IAEA portal): https://www.iaea.org/resources/rpop/resources/databases-and-learning-systems/safron
- ROSIS first report (PubMed 2010): https://pubmed.ncbi.nlm.nih.gov/21087801/
- RANZCR Inside News (June 2022): https://issuu.com/ranzcr/docs/inside_news_june_2022/s/16241410
- [ford-ils-consensus-2012]: Ford EC et al., "Consensus recommendations for incident learning database structures in radiation oncology," *Med Phys* 39(12):7272–7290 (2012)
- [nyflot-ils-metrics-2015]: Nyflot MJ et al., "Metrics of success: Measuring impact of a departmental near-miss incident learning system," *Pract Radiat Oncol* 5:e409–e416 (2015)
- [kim-ils-tbi-impact-2017]: Kim A et al., "Are we making an impact with incident learning systems? Analysis of QI interventions using total body irradiation as a model system," *Pract Radiat Oncol* (2017), doi:10.1016/j.prro.2017.05.010
- [rosis-cunningham-2010]: Cunningham J, Coffey M, Knöös T, Holmberg O, "Radiation Oncology Safety Information System (ROSIS) – Profiles of participants and the first 1074 incident reports," *Radiother Oncol* 97:601–607 (2010). www.rosis.info
- [roils-first-year-2015]: Hoopes DJ et al., "RO-ILS: A report from the first year of experience," *Pract Radiat Oncol* 5:312–318 (2015)
- [clark-5yr-incident-learning-2013]: Clark BG, Brown RJ, Ploquin J, Dunscombe P, "Patient safety improvements in radiation treatment through 5 years of incident learning," *Pract Radiat Oncol* 3:157–163 (2013). Ottawa Hospital.
- [pawlicki-ils-levels-2017]: Pawlicki T, Coffey M, Milosevic M, "Incident Learning Systems for Radiation Oncology: Development and Value at the Local, National and International Level," *Clin Oncol* 29:562–567 (2017). Note: ROSIS→ROSEIS (ESTRO); SAFRON = Safety Reporting and Learning System for Radiotherapy (IAEA).
