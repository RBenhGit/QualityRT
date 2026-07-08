# ILS Criteria in Radiotherapy — What, Why, and How

**Date:** 2026-06-18
**Topic:** Synthesis of criteria for Incident Learning Systems (ILS) in radiation oncology using a What / Why / How framework
**Primary Authority:** Ford EC et al., "Consensus recommendations for incident learning database structures in radiation oncology," *Med Phys* 39(12):7272–7290 (2012)
**Sources:** [ford-ils-consensus-2012], [incident-learning-systems-international], [ro-ils], [nyflot-ils-metrics-2015], [clark-5yr-incident-learning-2013], [pawlicki-ils-levels-2017]

---

## WHAT — What Is an ILS?

An Incident Learning System (ILS) is a structured, multi-level feedback mechanism for reporting, analyzing, and acting on near-misses, unsafe conditions, and adverse events in the radiation oncology workflow. "Incident reporting" alone is insufficient — **the full feedback loop of report → analysis → follow-up → intervention is what constitutes incident *learning***, not merely incident *reporting*. [ford-ils-consensus-2012]

The consensus paper defines **"incident"** broadly as any unwanted or unexpected change from normal system behavior that causes or has the potential to cause adverse effects — including deviations that do not reach the patient. AHRQ further classifies events into three types [ford-ils-consensus-2012], [ro-ils]:

| Type | Definition |
|---|---|
| **Incident (actual)** | Reached and affected the patient |
| **Near Miss** | Could have caused harm; intercepted before reaching patient |
| **Unsafe Condition** | Raises the probability of a future event |

---

## WHY — Why Is an ILS Required?

**Clinical stakes are high.** RT protocol deviations are consistently associated with worse survival in cooperative-group trials (NSCLC ~13% survival decrement; head & neck HR 1.99; meta-analysis HR 1.74). Safe delivery is not administrative — it is clinically decisive. [ro-ils]

**Incidents are common.** Estimated error rate in RT: **1 per 600 patients**; in some series, approximately **one near-miss per patient treatment course**. Whatever the true rate, it is worse than modern anesthesiology. [ford-ils-consensus-2012]

**Near-misses vastly exceed actual incidents.** ROSIS near-miss-to-incident ratio: **13.8:1**; Ganesh's literature estimate: **~600 events before a major accident**. Systematic capture of near-misses is the only mechanism to intervene before catastrophe. [incident-learning-systems-international]

**Aviation precedent.** The Commercial Aviation Safety Team (CAST) reduced fatal accident risk by **73% in 10 years** through systematic investigation of crashes and near-misses. Nuclear power has used in-plant and international incident learning for decades. Radiation oncology safety performance lags these industries. [ford-ils-consensus-2012]

**Regulatory mandate.** EU Directive 2013/59/EURATOM (Article 62) makes recording and analyzing accidental/unintended exposures a **legal requirement** for all EU member states. [incident-learning-systems-international]

**Accreditation requirement.** ILS participation (or enrollment in a PSO) satisfies ASTRO accreditation Standard 7 (Culture of Safety) and ACR requirements; qualifies as ABR MOC Part 4 PQI. [ro-ils]

---

## HOW — The Complete Criteria for an Effective ILS

### 1. Structural Criteria — Five Required Components [ford-ils-consensus-2012]

| Component | What It Contains |
|---|---|
| **Definitions** | Standardized RT-specific terminology (incident, near miss, safety barrier, adverse event, etc.) |
| **Process Maps** | 91 EBRT steps / 88 brachy steps across 8 phases; 35/32 safety barriers identified |
| **Severity Scales** | Dual: medical harm (0–10) + dosimetric deviation (<5% to >100%); never conflated |
| **Causal Taxonomy** | Six top-level categories with subcategories; designed for inter-rater robustness |
| **Data Elements** | Three-level structure (Reporter → Analyst → Responder); Required/Recommended/Optional |

---

### 2. Functional Requirements — 14 Criteria Ranked by Priority [ford-ils-consensus-2012]

| Rank | Requirement | Notes |
|---|---|---|
| 1 | **Electronic** | Enables data mining, filtering, interconnectivity |
| 2 | **Easy to use** | Front-line reporters; target entry time <1 minute |
| 3 | **Provides feedback** | To both the clinic and the individual reporter |
| 4 | **Standards-compliant** | Enables cross-institutional data sharing |
| 5 | **Validated with test cases** | Also useful for staff training |
| 6 | **Statistical analysis & filtering** | By process step, cause, severity, date |
| 7 | **Supports near-miss capture** | Near-misses are the primary learning signal |
| 8 | **Incident investigation tools** | RCA structures, severity tagging |
| 9 | **Semi-anonymous reporting** | Option must exist; rare use = sign of healthy culture |
| 10 | **Corrective action tracking** | Follow-up management system |
| 11 | **Multisite support** | For national/international systems |
| 12 | **Workflow tools** | Manager alerts, escalation, close-out tracking |
| 13 | **Secure communication** | Between users (e.g., analyst ↔ reporter) |
| 14 | **Clear reporting threshold** | Consistent definition of what is reportable |

---

### 3. Severity Scales — Exact Descriptors [ford-ils-consensus-2012]

**Medical Severity (0–10):**

| Score | Consequence |
|---|---|
| 10 | Premature death |
| 8/9 | Life-threatening — intervention essential; possible recurrence from underdose |
| 7 | Permanent major disability (or grade 3/4 permanent toxicity) |
| 5/6 | Permanent minor disability (or grade 1/2 permanent toxicity) |
| 3/4 | Temporary side effects — major, requiring treatment/hospitalization |
| 2 | Temporary side effects — intervention indicated |
| 1 | Temporary side effects — intervention not indicated |
| 0 | No harm |

**Dosimetric Deviation (1–10):**

| Score | Dose Deviation from Prescription |
|---|---|
| 9/10 | >100% absolute deviation to any structure |
| 7/8 | >25–100% absolute deviation |
| 5/6 | >10–25% absolute deviation |
| 3/4 | >5–10% absolute deviation |
| 1/2 | <5% absolute deviation |

> **Note:** A Clinical Action Scale (A–D) operates independently of medical severity to drive follow-up urgency — some low-severity events (e.g., wrong MRN entered) warrant an A-score due to downstream cascade risk. [ford-ils-consensus-2012]

---

### 4. Causal Taxonomy — Six Categories [ford-ils-consensus-2012]

| Category | Key Subcategories |
|---|---|
| **Organizational management** | Staffing, capital resources, policies/procedures, training, communication, physical environment, leadership/safety culture |
| **Technical** | Acceptance testing, equipment design, maintenance, IT infrastructure |
| **Human behavior** | Acting outside scope, slip, poor judgment, language, intentional violations, negligence |
| **Patient-related** | Cognitive/language issues, non-compliance, physical inability |
| **External factors** | Natural environment, hazards beyond facility control |
| **Procedural issues** | Failure to detect, interpret, select correct rule, develop effective plan, or execute plan |

> Root-cause analysis pitfalls explicitly named: (1) blaming an individual as the only cause; (2) focusing solely on staffing; (3) relying on policies/procedures in isolation — all have weak impact on behavior. [ford-ils-consensus-2012]

---

### 5. Three-Level Data Structure [ford-ils-consensus-2012]

| Level | Who Completes It | Key Content |
|---|---|---|
| **1 — Reporter** | Front-line staff; <1 min | Date, incident type, fractions affected, narrative, where found, modality (18 elements) |
| **2 — Analyst** | Second investigator | Medical/dosimetric severity, causal taxonomy, process step of origin, equipment details (38 elements) |
| **3 — Responder** | QM team | Safety barriers activated, corrective/preventive/learning actions, incident closure (7 elements) |

---

### 6. Operational / Investigation Timeline Criteria [ford-ils-consensus-2012]

| Incident Severity | Required Response |
|---|---|
| **Serious** | Initial investigation by next business day; individual + domain members + supervisor + senior management + physician notified immediately |
| **Minor / near-miss** | Initial investigation within 10 working days; individual + supervisor |
| **All incidents** | Written policy required; designated person responsible for initial review; closure tracked |

---

### 7. Success Metrics [nyflot-ils-metrics-2015]

| Metric | Target Direction |
|---|---|
| Report volume | Rising |
| Unique reporters | Rising (broad staff distribution) |
| Mean Near-Miss Risk Index (NMRI) | Declining |
| Anonymous report fraction | <2% |
| High-reliability interventions (forcing functions) | Increasing share |

> Ottawa Hospital demonstrated a **54% decrease in serious incidents in year one**, sustained over 5 years. [clark-5yr-incident-learning-2013]

---

### 8. Legal / Cultural Criteria

| Criterion | Mechanism |
|---|---|
| Confidentiality protection | PSQIA 2005 (USA) — federal privilege; upheld in federal court 2014 |
| Just culture / non-punitive | Prerequisite for honest reporting; anonymous option signals cultural deficit |
| EU legal compliance | Article 62, Directive 2013/59/EURATOM |
| Cross-system compatibility | Must map to ROSIS, SAFRON, AHRQ Common Formats, NROR |

---

## Decisions Made

- Full text of Ford et al. 2012 ingested into `wiki/topics/incident-learning-systems-international.md` with large weight — all 14 functional requirements, dual severity scales, causal taxonomy, three-level data structure, and operational recommendations now captured in the wiki.
- Summary structured using What / Why / How framework per user request.

## Next Steps

- Consider saving this synthesis as a formal wiki page at `wiki/topics/ils-criteria-synthesis.md`.
- Candidates for future ingest to fill identified gaps: investigator training standards (London Protocol, TreatSafely Foundation), proton therapy / MR-Linac ILS criteria, SAFRON vs. AAPM taxonomy comparison.
