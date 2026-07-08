# Departmental Incident Reporting Dataset (Israel, 2004–2026)

**Type:** Topic
**Status:** developing
**Last updated:** 2026-07-08
**Sources:** [incident-reporting-xlsx-il]

## Summary

A bilingual (Hebrew/English) Excel-based incident-reporting and taxonomy system from a radiotherapy department. The log carries **1,014 serial numbers**, but the serial number is assigned ahead of and independent of actual reporting — it is pre-allocated for future incidents as well. A row counts as an actual **report** if it carries a populated **date of harm ("מועד הפגיעה") or report date ("מועד דיווח")** (either one is sufficient); by this definition **871 of 1,014 (86%) are reports**, and the remaining 143 (14%) — which have neither date populated — are reserved/unreported slots excluded from all report-volume statistics on this page. Critically, **the ILS did not exist / was not in use before October 2017; the 38 reports dated before that point were entered retrospectively (after the fact) once the system launched, and the ILS became part of routine ongoing departmental operation from October 2017 onward** (833 of 871 reports) — this distinction should govern any trend interpretation of the pre-Oct-2017 period. It is a real, primary-source instance of exactly the kind of departmental incident learning system (ILS) described abstractly in [[incident-learning-systems-international]] — structured around a process-stage taxonomy, a free-text-derived keyword dictionary (41 keywords, 799 tagged mentions), a dual severity scoring scheme (medical + dosimetric, closely mirroring the AAPM/Ford consensus scales), and a linked corrective-action/task-management tracker. Unlike the wiki's other ILS pages (which summarize published literature about ILS), this page summarizes a live operational dataset — the wiki's first ingested primary-source safety database rather than a secondary analysis of one.

## Key Facts / Claims

### Scope and volume
- **1,014 serial numbers** exist in the log, but the serial number is pre-assigned independently of whether a report has actually been filed — the excess numbers are **reserved for future incidents and have no report filed against them at all** (confirmed: they are not missing/undated existing reports, simply unused reserved slots). A row counts as a **report** if it has a populated date of harm or report date (either suffices): **871 of 1,014 (86%)** qualify; the remaining 143 (14%) reserved serial numbers have no report and are excluded from all volume statistics below. (An earlier draft of this page used report-date-only as the reporting criterion, yielding 817; per user clarification, harm-date-only rows are also genuine reports and are now included — see 2026-07-08 correction in Raw Notes.) [incident-reporting-xlsx-il]
- **Retrospective vs. routine-operation periods:** the departmental ILS **did not exist / was not in use before October 2017**. The 38 reports dated before that point were entered **retrospectively** once the system launched; the ILS became part of **routine, ongoing departmental operation starting October 2017**. Of the 871 reports: **38 (4%) predate October 2017 (retrospective)**, and **833 (96%) fall in the October-2017-onward routine-operation period** [incident-reporting-xlsx-il]
- This distinction means the pre-Oct-2017 counts (2015–2017: 17, 8, 24 = 49 reports across ~2.75 years) reflect events entered after the fact, not contemporaneous logging — they should **not** be read as evidence of the department's reporting culture or reporting *rate* during 2015–2017 (there was no active reporting system to generate a rate), and should not be extrapolated or compared against the post-Oct-2017 routine-operation trend on a like-for-like basis [incident-reporting-xlsx-il]
- Each report is dated by its report date when available, falling back to its date of harm when the report date is blank (this assigns every one of the 871 reports to a single calendar quarter/year for trend purposes) [incident-reporting-xlsx-il]
- **Annual report counts (871 total; retrospective years in *italics*):** *17 (2015)* → *8 (2016)* → *24 (2017, partial: includes both retrospective and routine-operation months)* → 66 (2018) → 93 (2019) → 55 (2020) → 100 (2021) → 130 (2022) → 90 (2023) → 115 (2024) → 130 (2025) → 43 (2026, partial year through May) [incident-reporting-xlsx-il]
- A separate summary table in the source workbook ("results new" sheet) presents a similar but not identical yearly tally (17, 8, 23, 60, 68, 52, 90, 128, 90, 115, 129 for 2015–2025). Most years match within <1% (2015, 2016, 2023, 2024 exact; 2022 and 2025 within ~1–1.5%) and the difference is not material. Three years diverge more (2017: +4%; 2018: +9%; 2021: +10%; **2019: +27%**, 93 vs. 68) — these larger gaps are noted for completeness but not investigated further, since the report-date/harm-date recomputation is the more directly auditable method and is used throughout this page [incident-reporting-xlsx-il]
- Restricting to the **routine-operation period only (Oct 2017 – May 2026, 833 reports)**, the rising-then-plateauing annual count (peaking at 130/yr in 2022 and 2025) is a fair basis for the "rising report volume = healthier reporting culture" heuristic proposed by Nyflot et al. for departmental ILS [incident-reporting-xlsx-il], [incident-learning-systems-international]
- This 871-report count is also consistent with the severity-score sample sizes reported elsewhere on this page (case severity n=870, total severity n=871) — a useful internal cross-check that the harm-date-or-report-date definition of "report" matches how the source workbook's own severity tallies were built [incident-reporting-xlsx-il]

### Quarterly report counts (871 reports; report date, or date of harm if report date is blank)

*Quarters before 2017-Q4 (marked †) predate the ILS's existence and were entered retrospectively; they are not directly comparable to later, routine-operation quarters.*

| Quarter | Reports | Quarter | Reports | Quarter | Reports | Quarter | Reports |
|---|---|---|---|---|---|---|---|
| 2015-Q1 † | 6 | 2018-Q3 | 15 | 2021-Q1 | 24 | 2023-Q4 | 13 |
| 2015-Q2 † | 3 | 2018-Q4 | 14 | 2021-Q2 | 27 | 2024-Q1 | 17 |
| 2015-Q3 † | 5 | 2019-Q1 | 40 | 2021-Q3 | 25 | 2024-Q2 | 28 |
| 2015-Q4 † | 3 | 2019-Q2 | 15 | 2021-Q4 | 24 | 2024-Q3 | 41 |
| 2016-Q2 † | 4 | 2019-Q3 | 20 | 2022-Q1 | 44 | 2024-Q4 | 29 |
| 2016-Q3 † | 2 | 2019-Q4 | 18 | 2022-Q2 | 35 | 2025-Q1 | 45 |
| 2016-Q4 † | 2 | 2020-Q1 | 17 | 2022-Q3 | 25 | 2025-Q2 | 43 |
| 2017-Q1 † | 2 | 2020-Q2 | 12 | 2022-Q4 | 26 | 2025-Q3 | 21 |
| 2017-Q2 † | 10 | 2020-Q3 | 15 | 2023-Q1 | 27 | 2025-Q4 | 21 |
| 2017-Q3 † | 1 | 2020-Q4 | 11 | 2023-Q2 | 24 | 2026-Q1 | 19 |
| 2017-Q4 | 11 | | | 2023-Q3 | 26 | 2026-Q2 | 24 |
| 2018-Q1 | 16 | | | | | | |
| 2018-Q2 | 21 | | | | | | |

**Total: 871 reports (38 retrospective †, 2015-Q1–2017-Q3; 833 routine-operation, 2017-Q4–2026-Q2)** [incident-reporting-xlsx-il]

- Peak quarters are **2025-Q1 (45 reports)** and **2022-Q1 (44 reports)**, both within the routine-operation period. There was no centralized/administrative batch-reporting practice at year-start (per user confirmation), so the Q1 peaks are not a reporting-process artifact. One tentative, unconfirmed hypothesis: earlier periods may have coincided with staff awareness-raising training that temporarily increased reporting rates, but this is not verified in the source data [incident-reporting-xlsx-il]
- Within the routine-operation period (2017-Q4 onward), quarterly volume is noisy but trends upward through 2025, consistent with the annual totals above; no single quarter accounts for a disproportionate share of the total. The 2015-Q1–2017-Q3 quarters predate the ILS's existence (entered retrospectively after launch) and should be read separately, not as the start of a continuous reporting trend [incident-reporting-xlsx-il]

### Data structure (Reporter-level fields)
- Each record carries 18 structured fields: serial number, date of harm, date reported, **process stage**, **injury/event type**, **nature of harm**, **frequency** (one-time vs. repeated), **primary cause category**, time of event, **facility/unit**, **treatment method**, **case urgency**, **contributing parameters**, **conclusions/corrective action**, plus separate **case, medical, and dosimetric severity scores** and free-text notes [incident-reporting-xlsx-il]
- This field set closely parallels — but was developed independently of, or in parallel to — the AAPM/Ford consensus "Reporter's form" (Level 1, 18 elements) described in [[incident-learning-systems-international]] [incident-reporting-xlsx-il]

### Process-stage distribution (where incidents originate, n=870)
- On-treatment ("מהלך טיפול" / during treatment): 235 (27%) — the single largest stage, consistent with [[incident-learning-systems-international]]'s finding that treatment delivery is the most vulnerable point for incidents reaching patients [incident-reporting-xlsx-il]
- Simulation: 156 (18%); Reception/intake: 129 (15%); Pre-treatment: 95 (11%); Prescription: 78 (9%); Quality control/check: 64 (7%); Planning: 50 (6%); Contouring/marking: 30 (3%); Other: 21 (2%); Follow-up: 12 (1%) [incident-reporting-xlsx-il]

### Event type and harm outcome (n=867)
- Unsafe condition / safety case (no direct harm requiring only monitoring): 313 (36%)
- Administrative event: 273 (31%)
- Near miss: 143 (16%)
- Harm occurred to patient: 138 (16%) [incident-reporting-xlsx-il]
- Of harm nature (n=865): 705 (81%) resulted in no injury, 150 (17%) single-patient injury, 10 (1%) multiple patients injured — i.e., the overwhelming majority of logged events are near-misses or no-harm events, consistent with the near-miss-to-incident ratios reported in [[incident-learning-systems-international]] [incident-reporting-xlsx-il]

### Frequency and primary cause (n=864/866)
- 777 (90%) one-time events vs. 87 (10%) recurring/systemic events [incident-reporting-xlsx-il]
- Primary cause categories: work culture 275 (32%), human error 233 (27%), communication 194 (22%), work procedure/process 124 (14%), technical failure 29 (3%), other 11 (1%) — human/organizational factors (culture + human error + communication + procedure = 95%) dominate over pure technical failure, matching the broader RT safety literature's emphasis in [[human-factors-rt-safety]] [incident-reporting-xlsx-il]

### Facility and modality (n=608/561)
- By facility: Linac 1/2: 148 (24%), Simulation unit: 141 (23%), Linac 4/5: 129 (21%), Linac 3: 39 (6%), physician office: 34 (6%), N/A: 34 (6%), reception/corridor: 30 (5%), brachytherapy suite: 21 (3%), nursing area: 16 (3%), contact therapy: 15 (2%) [incident-reporting-xlsx-il]
- By treatment method: 3D conformal 186 (33%), IMRT 155 (28%), SBRT 116 (21%), SRS/SRT 40 (7%), brachytherapy 24 (4%), clinical setup 20 (4%), contact therapy 15 (3%), TBI/TSI/TLI/TSET combined ~25 (4%) [incident-reporting-xlsx-il]

### Urgency, contributing factors, and conclusions (n=622/837/732)
- Case urgency at time of event: routine 444 (71%), urgent 94 (15%), expedited/fast-track 75 (12%), N/A 9 (1%) [incident-reporting-xlsx-il]
- Contributing parameters: more than one factor present 287 (34%), single factor 327 (39%), none identified 223 (27%) — over a third of events are multi-factorial, echoing the median-7-causal-factors finding in [[human-factors-rt-safety]] (Evans 2017) [incident-reporting-xlsx-il]
- Conclusions/corrective actions: reinforcement of existing procedure 385 (53%), change to existing procedure 213 (29%), no change needed 63 (9%), new procedure written 55 (8%), investigation continuing 16 (2%) — the department overwhelmingly resolves events with procedural reinforcement or revision rather than the "stronger actions" (forcing functions, automation) that [[incident-learning-systems-international]] (Clark et al.) found more durably effective [incident-reporting-xlsx-il]

### Severity scoring
- Dual severity scales recorded per incident: **case severity** (n=870, mean 3.99, median 4, range 1–11) and a combined **total severity** score (n=871, mean 4.20, median 4, range 0–19) — the presence of separate medical and dosimetric severity columns mirrors the two-axis (medical 0–10 / dosimetric 1–10) consensus scale in [[incident-learning-systems-international]], though this department's scale extends beyond 10 for combined/total scoring [incident-reporting-xlsx-il]
- A full severity-score frequency histogram is tabulated (case severity 1–11 and total severity 0–19), enabling reconstruction of the department's own severity distribution curve; both distributions are strongly right-skewed toward low severity, consistent with published ILS severity distributions [incident-reporting-xlsx-il]

### Free-text keyword taxonomy (799 tagged mentions across 41 keywords) — full table

| # | Keyword (Hebrew) | English gloss | Count | % of 799 |
|---|---|---|---|---|
| 1 | תיעוד לא תקין | Improper/deficient documentation | 157 | 19.6% |
| 2 | תקשורת לקויה | Poor communication | 74 | 9.3% |
| 3 | מתן טיפול באופן שגוי | Treatment delivered incorrectly | 69 | 8.6% |
| 4 | העברת מידע | Information transfer issue | 69 | 8.6% |
| 5 | תכנון שגוי | Planning error | 56 | 7.0% |
| 6 | אי עמידה בזמנים | Timeliness/deadline failure | 54 | 6.8% |
| 7 | סריקה לא תקינה | Improper scan/imaging | 53 | 6.6% |
| 8 | היעדר תיעוד | Absence of documentation | 37 | 4.6% |
| 9 | עבודה שלא על פי הנוהל | Work not per procedure | 25 | 3.1% |
| 10 | כמעט ניתן טיפול שגוי | Near-miss incorrect treatment | 22 | 2.8% |
| 11 | שגיאה בזיהוי מטופל | Patient identification error | 19 | 2.4% |
| 12 | זימון תור לא מספק | Inadequate appointment scheduling | 12 | 1.5% |
| 13 | תיק ללא אישורים מספקים | Chart lacking sufficient approvals | 12 | 1.5% |
| 14 | אי ביצוע הנחיה (צוות) | Staff non-compliance with instruction | 12 | 1.5% |
| 15 | מתן טיפול שלא על פי הפרוטוקול | Treatment not per protocol | 11 | 1.4% |
| 16 | סימון שגוי | Marking/contouring error | 10 | 1.3% |
| 17 | בעיות קיבוע | Immobilization problems | 9 | 1.1% |
| 18 | מתן טיפול בהיעדר מרשם | Treatment given without prescription | 8 | 1.0% |
| 19 | אי ביצוע הנחיה (מטופלים) | Patient non-compliance with instruction | 8 | 1.0% |
| 20 | מרשם שגוי | Incorrect prescription | 7 | 0.9% |
| 21 | חבלה גופנית | Physical injury | 7 | 0.9% |
| 22 | חוסר תשומת לב | Lack of attention | 7 | 0.9% |
| 23 | שגיאת Care Path | Care-path error | 6 | 0.8% |
| 24 | כמעט פגיעה במתקן | Near-miss equipment/facility harm | 6 | 0.8% |
| 25 | שגיאה טכנית | Technical error | 5 | 0.6% |
| 26 | צוות חסר | Understaffing | 5 | 0.6% |
| 27 | היעדר מרשם | Missing prescription | 4 | 0.5% |
| 28 | היעדר צילומים | Missing images | 4 | 0.5% |
| 29 | כמעט סימון שגוי | Near-miss marking error | 4 | 0.5% |
| 30 | עומס יתר | Overload | 4 | 0.5% |
| 31 | חוסר בהבנת דרישות הטיפול | Misunderstanding of treatment requirements | 4 | 0.5% |
| 32 | סריקה חוזרת | Repeat scan | 3 | 0.4% |
| 33 | פגיעה במתקן | Equipment/facility harm | 3 | 0.4% |
| 34 | חוסר יעילות בעבודה | Work inefficiency | 3 | 0.4% |
| 35 | מיקום לא ניתן לשחזור | Non-reproducible positioning | 2 | 0.3% |
| 36 | מתן טיפול ללא בקרת איכות | Treatment given without QC | 2 | 0.3% |
| 37 | כמעט שגיאה בזיהוי מטופל | Near-miss patient-ID error | 2 | 0.3% |
| 38 | נוהל חסר | Missing procedure | 2 | 0.3% |
| 39 | כמעט מתן טיפול ללא בקרת איכות | Near-miss treatment without QC | 1 | 0.1% |
| 40 | תגובה טוקסית של מטופל | Toxic patient reaction | 1 | 0.1% |
| — | **Total** | | **799** | **100%** |

[incident-reporting-xlsx-il]

- Documentation-related issues (improper documentation + absence of documentation combined) account for **194 mentions (24.3%)** of all tagged keyword mentions — the single largest thematic cluster, ahead of communication (9.3%) and combined planning/scanning errors [incident-reporting-xlsx-il]
- The top 4 keywords (documentation, communication, incorrect treatment delivery, information transfer) together account for **46.1%** of all 799 tagged mentions — a small set of recurring themes drives the bulk of reported issues [incident-reporting-xlsx-il]
- The long tail is thin: 15 of the 40 keywords (38%) each account for ≤0.5% of mentions (≤4 occurrences), indicating most distinct failure descriptors are rare, one-off phenomena rather than systemic patterns [incident-reporting-xlsx-il]
- A parallel "Taxonomy New" mapping sheet translates the department's local Hebrew keyword set onto the standardized English RO-ILS/AAPM causal-factor categories (e.g., "Laterality Incorrect," "Patient or patient information incorrect," "Prescription dose, fractionation incorrect and/or calculation error," "Treatment plan isodose distribution unacceptable"), showing the department has deliberately aligned its local taxonomy to the national/international standard described in [[incident-learning-systems-international]] and [[human-factors-rt-safety]] [incident-reporting-xlsx-il]

### Governance and workflow
- The workbook includes an **Event Summary** sheet (glossary, case abstract, meeting conclusions, QI meeting date, attendees, external report flag, report-sent date) and a **Task Management** sheet (taxonomy tag, case summary, meeting conclusions, QI meeting date, assigned tasks, person responsible, target completion date, actual completion date) — implementing a full reporter → analyst → corrective-action-tracking pipeline in a single spreadsheet, functionally equivalent to the three-level (Reporter/Analyst/Responder) data structure recommended by the AAPM consensus in [[incident-learning-systems-international]] [incident-reporting-xlsx-il]

## Connections

- [[incident-learning-systems-international]] — this dataset is a concrete, primary-source instance of a departmental ILS; its field structure, dual severity scales, and taxonomy closely parallel the AAPM/Ford consensus recommendations and the University of Washington/Ottawa departmental ILS case studies already summarized there
- [[human-factors-rt-safety]] — the dominance of work-culture, human-error, and communication as primary causes (95% combined) and the high rate of multi-factorial events (34%) both corroborate this page's causal-factor findings
- [[ro-ils]] — this department's taxonomy mapping sheet explicitly aligns local Hebrew categories to RO-ILS/AAPM English causal-factor terminology
- [[rt-quality-management]] — the linked Task Management/corrective-action tracker is a working example of the QM feedback loop described generically in that page
- [[radiation-safety-culture-healthcare]] — sustained, rising report volume during the routine-operation period (Oct 2017–2025) is one of the IAEA safety-culture indicators (Trait 9: Environment for Raising Concerns) discussed there; the pre-Oct-2017 retrospective backfill does not qualify as such evidence since it was not contemporaneous reporting
- [[rt-patient-safety-context-map-hebrew]] — this is a Hebrew-language operational artifact; relevant to the Hebrew-language synthesis page's audience and context

## Open Questions

- ~~What triggered the sharp rise in reporting from 2018 onward?~~ **Answered:** the departmental ILS did not exist / was not in use before October 2017; the 38 pre-October-2017 reports were entered retrospectively once the system launched, and the ILS became routine ongoing operation from October 2017 onward (833 reports) — this fully explains the step change around 2017/2018.
- ~~Of the 143 serial numbers with neither a harm date nor a report date, are these incidents that occurred but were never logged, or reserved slots for future incidents?~~ **Answered:** confirmed reserved slots only — no reports exist for these 143 serial numbers.
- ~~Do the Q1 peaks (2022, 2025) reflect centralized/administrative batch reporting?~~ **Answered:** no, there was no centralized/administrative batch-reporting practice. One unconfirmed possibility raised by the user: earlier periods may have coincided with staff awareness-raising training that temporarily boosted reporting, but this is not verified.
- How many of the 1,014 records have completed corrective actions in the Task Management sheet vs. remain open/in-progress? The extracted sample showed placeholder/`#REF!` values in early rows, suggesting the tracker may have unresolved formula references.
- Is this dataset from a single department/institution, and can it be attributed (with appropriate anonymization) for comparison against published ROSIS/RO-ILS/SAFRON aggregate statistics?
- Does the "documentation deficiency" keyword cluster (24% of tagged mentions) reflect genuine root-cause documentation failures, or an artifact of how the free-text tagging/search was performed (e.g., a broad keyword match)?
- How does this department's severity distribution (mean total severity 4.2, range 0–19) map onto the standard 0–10 AAPM consensus scales — is the >10 range a distinct combined/summed score rather than a single severity axis?
- The source workbook's own "results new" yearly summary table diverges from the harm-date-or-report-date recomputation by >5% in three years (2018: +9%, 2021: +10%, 2019: +27%); most other years match within <1% and are not treated as a discrepancy. The cause of the larger 2019 gap in particular remains unexplained.

## Raw Notes

- Source file: `raw/Incident reporting.xlsx` — an Excel workbook (.xlsx) with 9 worksheets: "Incident Reporting" (raw log, 1,014 serial-numbered rows × 18 fields, of which 871 carry a date of harm and/or a report date and count as reports), "Event summary" (case narratives/meeting metadata), "Taxonomy" (41-keyword frequency dictionary), "טבלת פרמטרים" / parameter table (Hebrew/English dropdown vocabulary for all coded fields, including full severity-scale definitions), "Results" (cross-tabulated frequency counts per category value), "results new" (monthly/yearly trend series and severity histograms), "calc sheet" (keyword search helper calculations), "Taxonomy New" (Hebrew-to-English causal-factor taxonomy crosswalk), "Task management" (corrective-action tracker).
- All per-field breakdowns elsewhere on this page (process stage, event type, cause, facility, modality, urgency, severity, taxonomy keywords) are drawn from the full 1,014-row log (counting non-blank field values, regardless of date status), since those fields are populated independent of whether either date is present. Only the report-volume/trend statistics (annual and quarterly counts) are restricted to the 871 rows with a harm date and/or report date, per the reporting definition established above.
- The workbook also embeds 25 native Excel charts (trend lines, pie/bar breakdowns by stage, cause, severity) which were not individually extracted here (data-only cell values were read via openpyxl; chart visual encodings were not reproduced) — a future ingest could recreate these visualizations from the underlying "Results"/"results new" tables if needed.
- All content is in mixed Hebrew and English; Hebrew field values were preserved and translated into English within this page's Key Facts. No raw file content was altered — `raw/Incident reporting.xlsx` remains the immutable source.
- Row/column references for verification: incident log = sheet "Incident Reporting", rows 2–1015; keyword taxonomy = sheet "Taxonomy", rows 2–41; severity histograms = sheet "results new", columns L–O; yearly totals = sheet "results new", columns H/J.
- 2026-07-08 enrichment: quarterly report-count table computed from "Incident Reporting" column C (מועד דיווח, report date) for all rows with a populated date; full 41-row keyword taxonomy table transcribed verbatim from sheet "Taxonomy" (columns A/B, with column D percentages recomputed against the stated total of 799).
- 2026-07-08 correction (user clarification): the reporting definition was widened from "report date populated" (817 rows) to "date of harm OR report date populated" (871 rows), per the user's statement that a harm date alone is sufficient evidence a report occurred. All annual/quarterly counts, the Summary, and the Scope-and-volume section were recomputed under this wider definition, adding the 2015-Q1–2017-Q4 quarters (54 additional reports) that the report-date-only definition had excluded.
- 2026-07-08 correction #2 (user clarification): reports dated before October 2017 were entered retrospectively as a one-time backfill for control/audit purposes, not logged contemporaneously; the ILS entered routine ongoing operation only from October 2017. Split the 871 reports into 38 retrospective (2015-Q1–2017-Q3) and 833 routine-operation (2017-Q4–2026-Q2) reports; marked retrospective quarters with † in the quarterly table; reworded the Summary, Scope-and-volume, and Connections (safety-culture link) sections to avoid treating the pre-Oct-2017 retrospective sample as evidence of a contemporaneous reporting trend or safety-culture signal.
- 2026-07-08 correction #3 (user answers to 5 open items): (1) recomputed the "results new" vs. raw-log annual discrepancy as percentages — most years match within <1% and are not a real discrepancy; only 2018 (+9%), 2021 (+10%), and 2019 (+27%) are material and remain unexplained. (2) Confirmed the 143 excess serial numbers have no report filed against them at all (reserved slots only, not undated existing reports). (3) Confirmed the ILS simply did not exist/was not in use before October 2017 — reworded from "retrospective backfill for control/audit purposes" (an inference that overstated the source's documentation) to "system did not exist; reports were entered after the fact once it launched." (4) Confirmed all documented reports (harm-date-or-report-date rule) are already included — no further filtering needed. (5) Confirmed there was no centralized/administrative batch reporting driving the Q1 peaks; user raised an unconfirmed hypothesis that earlier periods may have coincided with staff awareness-training campaigns. Removed three now-resolved Open Questions and updated the remaining ones accordingly.
