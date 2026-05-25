# FMEA for AI and Automated Radiotherapy Workflows

## Overview

As AI-based contouring, automated treatment planning, and fully automated radiotherapy workflows (FAW) are introduced into clinical practice, FMEA has been applied to assess the new risk landscape. A consistent finding across studies: the highest-risk points in automated workflows are the **human-automation interaction points**, not the automated systems themselves.

---

## Source 1: De Kerf et al. 2025 — Multicentre Prospective FMEA of Fully Automated Workflow

- **Title:** Multicentre prospective risk analysis of a fully automated radiotherapy workflow
- **Lead Author:** Geert De Kerf (Iridium Netwerk, Antwerp, Belgium)
- **Journal:** Physics and Imaging in Radiation Oncology
- **Year:** 2025 (April 6)
- **DOI:** 10.1016/j.phro.2025.100765
- **PMC:** https://pmc.ncbi.nlm.nih.gov/articles/PMC12005333/

### Participating Institutions (8 European centers)
Iridium Netwerk (Belgium), Cliniques Universitaires Saint Luc (Belgium), University Medical Center Groningen (Netherlands), Abano Terme Hospital (Italy), Careggi University Hospital (Italy), Maastro (Netherlands), Odense University Hospital (Denmark), The Netherlands Cancer Institute (Netherlands), and IBA (Belgium).

### Workflow Components Analyzed
1. Patient assignment to automated protocol
2. CT simulation
3. Auto-segmentation
4. Auto-planning
5. Dose calculation
6. Manual review (final step — only human checkpoint)

### Critical Findings

**Risk Score by Step (normalized R*):**
1. Manual Review: R* = 0.46 (HIGHEST — "Human oversight at the review stage is essential")
2. Auto-segmentation: R* = 0.44
3. Auto-planning: R* = 0.25
4. Simulation: R* = 0.25
5. FAW Orchestrator: R* = 0.07 (lowest)

**Primary Risk Causes:**
1. AI model generalizability failures (out-of-distribution patients/protocols)
2. Human error during patient preparation
3. Protocol deviations and inappropriate workflow assignments
4. Software errors (lowest concern)

**Key Failure Modes:**
- Inadequate manual review of automated outputs
- Incorrect protocol assignment to patients
- Suboptimal segmentation from protocol misuse
- Communication gaps in FAW documentation
- Treatment delays

### The Automation Paradox
"Points where people interact with the FAW were considered higher risk than lack of trust in the FAW itself."
- Technical components demonstrate reliability
- Human factors at review/oversight stages dominate actual risk
- Staff expressed concern about progressive **skill degradation** — reduced manual involvement leads to loss of ability to detect and correct automated errors

### Automation Bias
Reviewers may fail to identify mid-level errors (large deviations are easy to catch; subtle errors are not) — a phenomenon consistent with automation-induced anchoring.

### Recommendations
1. Educational programs on FAW boundaries and error recognition
2. Automated QA systems monitoring workflow appropriateness
3. Decision-support tools helping reviewers evaluate automation output quality
4. Contingency procedures for unforeseen automation failures

---

## Source 2: Radiation Planning Assistant FMEA (USA)

- **Title:** Using Failure Mode and Effects Analysis to Evaluate Risk in the Clinical Adoption of Automated Contouring and Treatment Planning Tools
- **Journal:** Practical Radiation Oncology
- **Year:** 2022
- **PMID:** 35305941
- **URL:** https://www.practicalradonc.org/article/S1879-8500(22)00008-X/fulltext

### Key Findings
- Applied FMEA to the Radiation Planning Assistant (RPA), an automated contouring and planning tool
- Multidisciplinary team scored failure modes on 1–10 scales (S, O, D) per TG-100 recommendations
- Compared risk in: (a) manual processes, (b) automated workflow without QA, (c) automated workflow with integrated automated QA
- **Integrating automated QA tools led to decreases in both maximum and mean risk scores**
- Automated plan QA can effectively increase patient safety compared to manual-only workflows

---

## Source 3: Multicentre AI-Contouring Clinical Validation (2023)

- **Title:** Automated Contouring and Planning in Radiation Therapy: What Is 'Clinically Acceptable'?
- **Journal:** Diagnostics (MDPI)
- **Year:** 2023
- **PMC:** https://pmc.ncbi.nlm.nih.gov/articles/PMC9955359/

### Key Findings
- AI-assisted contouring reduced intra- and inter-observer variability in prostate radiotherapy
- However: structured quality assurance and human oversight are essential to mitigate **automation bias** while leveraging AI efficiency
- Defines "clinically acceptable" as the threshold at which automated outputs can be used with minimal or no human correction — but the threshold is modality- and structure-specific

---

## Key Themes Across All Studies

1. **Human-automation interface is the highest-risk zone** — not the AI/automation itself
2. **Skill degradation** is a systemic risk: as automated workflows reduce manual engagement, staff lose the expertise to detect errors in automated outputs
3. **Automation bias** consistently identified: reviewers are anchored by automated outputs and less likely to question them
4. **Automated QA within the workflow** (not just at the end) is the most effective mitigation strategy
5. **Mid-level errors are the hardest to detect** — large deviations are obvious; subtle systematic errors are easily missed under automation

---

## URLs and References

- De Kerf 2025 (multicentre FMEA): https://pmc.ncbi.nlm.nih.gov/articles/PMC12005333/
- RPA FMEA (Practical Radiation Oncology 2022): https://www.practicalradonc.org/article/S1879-8500(22)00008-X/fulltext
- AI contouring clinical validation (PMC 2023): https://pmc.ncbi.nlm.nih.gov/articles/PMC9955359/
- AI contouring automation bias (PMC 2025): https://pmc.ncbi.nlm.nih.gov/articles/PMC12715409/
