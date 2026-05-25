# Human Factors and Safety Culture in Radiotherapy

## Overview

Human factors — including staffing levels, fatigue, communication failures, supervision quality, and organizational culture — are significant contributors to radiotherapy safety events. Multiple frameworks (HFACS, BN-HFACS, crew resource management) have been applied to analyze and mitigate these risks.

---

## Source 1: Weintraub et al. 2021 — HFACS Analysis of RT Safety Events

- **Title:** Human factor associations with safety events in radiation therapy
- **Authors:** Sheri M Weintraub, Bill J Salter, C Lynn Chevalier, Sarah Ransdell
- **Journal:** Journal of Applied Clinical Medical Physics
- **Year:** 2021, Vol. 22(10):288–294
- **DOI:** 10.1002/acm2.13420
- **PMC:** https://pmc.ncbi.nlm.nih.gov/articles/PMC8504582/

### Methodology
- Analyzed 141 incident reports from the SAFRON (Safety in Radiation Oncology) incident learning system
- Applied the **HFACS (Human Factors Analysis and Classification System)** framework
- HFACS categorizes contributing factors across 4 hierarchical tiers

### HFACS Framework: 4-Tier Hierarchy

**Tier 1 — Unsafe Acts (34% of factors):**
- Skill-based errors: errors during familiar, routine tasks performed without conscious thought
- Decision errors: lacking knowledge or experience
- Perceptual errors: compromised sensory input
- Routine and exceptional violations

**Tier 2 — Preconditions for Unsafe Acts (29% of factors):**
- Environmental factors (physical/technical conditions)
- Personnel factors (communication, coordination, planning, fitness for duty)
- Operator conditions (fatigue, stress, distraction, illness)

**Tier 3 — Supervision (33% of factors):**
- Inadequate supervision
- Inappropriate planned operations
- Failure to address known problems

**Tier 4 — Organizational Influences (4% of factors):**
- Resource management
- Safety culture and climate
- Corporate processes

### Critical Findings

**Supervision-Error Relationships:**
- Inadequate supervision → 25% increased likelihood of decision errors
- Decision errors were **6.26× more likely** when supervision failures were present (odds ratio = 6.26)

**Treatment Planning Errors:**
- Significant association between skill-based errors and treatment planning failures
- "Treatment planning safety events are influenced by slips made without thought while routine tasks are performed"

**QA Deficiencies:**
- Decision-type errors associated with QA failures — "safety events involving QA work are influenced by lacking knowledge or skill"

### 15 RT-Specific Error Types Identified
Approval errors, documentation errors, equipment malfunction, image guidance misinterpretation, treatment planning errors, collisions, QA failures, scheduling errors, simulation errors, treatment setup/delivery errors, wrong patient identification, patient-related problems (and others)

### Recommendations
1. Include supervisory factors in all safety improvement efforts
2. Balance automation with cognitive engagement to reduce mindless skill-based slips in treatment planning
3. Improved training and education to address knowledge deficits underlying QA errors
4. Apply HFACS systematically to reveal organizational and environmental root causes

---

## Source 2: HFACS-Bayesian Network Hybrid Analysis (2024)

- **Title:** Causal analysis of radiotherapy safety incidents based on a hybrid model of HFACS and Bayesian network
- **Journal:** Frontiers in Public Health
- **Year:** 2024
- **PMC:** https://pmc.ncbi.nlm.nih.gov/articles/PMC11169683/

### Innovation
First application of a **Bayesian Network-HFACS hybrid model** to radiotherapy incidents. Provides quantitative causal analysis rather than just frequency counting — enabling identification of root-cause relationships.

### Dataset
81 incidents from the RO-ILS database

### Key Error Distributions
- Skill-based errors: **37.5% prior probability** — highest among unsafe acts
- Treatment planning phase: most frequent errors, particularly "wrong data transfer or setting"
- Patient setup and target delineation: elevated error rates

### Most Influential Factors

**Level 2 Preconditions (most impactful):**
- Operator conditions (49.6% prior probability): inattention, mental fatigue, physical fatigue
- Personnel factors (59.8%): poor team communication and coordination
- Environmental factors: inadequate lighting, noise, equipment design

**Organizational Climate:**
- Organizational climate significantly influences personnel factors (sensitivity: 3.37)
- Organizational policies and procedures require strengthening

### Causal Sensitivity Analysis
- Operator conditions most strongly cause skill-based errors (sensitivity: 1.70)
- Personnel factors primarily drive decision errors and routine violations
- Environmental factors predominantly cause perceptual errors

### Recommendations
1. **Workload rationalization** to reduce operator fatigue and inattention
2. **Systematic peer verification** for information transfer during plan approval
3. **Standardized written procedures** to minimize verbal communication errors
4. **Safety culture development** through regular education and blame-free environments
5. **Environmental improvements**: lighting, equipment interface design
6. **Enhanced team communication** across physicians, physicists, and therapists

---

## Source 3: Crew Resource Management (CRM) Training in RT

- **Title:** Improving Incident Reporting in a Hospital-Based Radiation Oncology Department: The Impact of a Customized Crew Resource Training and Event Reporting Intervention
- **PMC:** https://pmc.ncbi.nlm.nih.gov/articles/PMC8020487/

### Key Findings
- Customized CRM training (adapted from aviation) improved incident reporting rates
- CRM addresses communication, teamwork, situational awareness, and decision-making
- Failures in communication, leadership, and decision-making within a "culture of retribution" are known contributors to adverse outcomes

---

## Key Themes Across All Human Factors Studies

1. **Skill-based errors** (routine slips in familiar tasks) are the most common error type in RT — not knowledge deficits
2. **Supervision quality** has an outsized effect on all other error types (6× multiplier for decision errors)
3. **Fatigue and mental inattention** are the highest-probability operator conditions contributing to errors
4. **Poor communication and coordination** at team interfaces (physician-physicist-therapist) is a persistent systemic risk
5. **Safety culture** (blame-free, just culture) is necessary but not sufficient — organizational processes and adequate staffing are equally important
6. **Treatment planning** is the highest human-factor-risk phase, consistent with FMEA findings (30% of RO-ILS incidents)
7. **Automation introduces new human factor risks**: skill degradation, automation bias, reduced vigilance

---

## Relationship to Other Frameworks

- HFACS findings directly confirm FMEA/TG-100 findings: same stages (treatment planning, contouring, data transfer) identified as highest risk
- RO-ILS and SAFRON provide the incident data that human factors studies analyze
- The IAEA defense-in-depth principle addresses the systemic/organizational layer that HFACS Tier 4 covers
- Just culture (RO-ILS design principle) directly addresses the HFACS finding that blame cultures suppress reporting

---

## References

- Weintraub 2021 (HFACS): https://pmc.ncbi.nlm.nih.gov/articles/PMC8504582/
- BN-HFACS hybrid 2024: https://pmc.ncbi.nlm.nih.gov/articles/PMC11169683/
- CRM training (PMC): https://pmc.ncbi.nlm.nih.gov/articles/PMC8020487/
- PSNet Radiation Safety primer: https://psnet.ahrq.gov/primer/radiation-safety
- Human factors and systems engineering approach (Red Journal 2007): https://www.redjournal.org/article/S0360-3016(07)04291-5/fulltext
- Risks in oncology and RT (NCBI Bookshelf): https://www.ncbi.nlm.nih.gov/books/NBK585623/
