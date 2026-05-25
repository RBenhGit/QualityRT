# AAPM Task Group Reports: The Linac QA Suite (TG-40, TG-142, TG-198, TG-218)

## Overview

A suite of AAPM Task Group reports governs equipment-focused quality assurance in radiotherapy, complementing the workflow/risk-based approach of TG-100. These reports establish prescriptive tests, frequencies, tolerances, and action levels for linear accelerators and patient-specific QA.

---

## TG-40 (1994) — Foundational LINAC QA

- **Title:** Comprehensive QA for Radiation Oncology
- **Authors:** Kutcher, Coia, Gillin, Hanson, Leibel, Morton, Palta, Purdy, Reinstein, Svensson
- **Journal:** Medical Physics, April 1994, 21(4):581–618
- **PMID:** 8058027
- **URL (AAPM Report 46):** https://www.aapm.org/pubs/reports/RPT_46.PDF

### What TG-40 Covers
- Structure: Part A for administrators; Part B code of practice (6 sections)
- Established the importance of a **written procedural QA plan** administered by a multidisciplinary committee
- Covered QA for external beam therapy equipment (linacs), brachytherapy, simulation, and treatment planning systems
- Addressed innovations of the era: computer-controlled accelerators, dynamic wedge, MLCs, portal imaging, stereotactic radiosurgery, intraoperative radiotherapy
- Relied heavily on AAPM Report 13 for dosimetry standards

### Why It Was Superseded
- Published in 1994; did not address CBCT imaging, IMRT, VMAT, or image-guided radiotherapy (IGRT)
- Replaced by TG-142 in 2009

---

## TG-142 (2009) — Modern LINAC QA

- **Title:** Task Group 142 Report: Quality Assurance of Medical Accelerators
- **Journal:** Medical Physics
- **Year:** 2009
- **URL (IROC/MD Anderson PDF):** http://irochouston.mdanderson.org/RPC/home_page/files/TG-142%20-%20QA%20of%20medical%20accelerators.pdf

### Key Improvements Over TG-40
- Added QA requirements for **CBCT (Cone-Beam CT)** systems integrated into LINACs
- Added recommendations for **MLC (Multi-Leaf Collimator)** QA
- Addressed **asymmetric jaws**, **dynamic wedge**, **virtual wedge**
- Separated tests into three categories by treatment type: non-IMRT, IMRT, and SRS/SBRT
- Stricter tolerances for SRS/SBRT (e.g., 1 mm vs. 2 mm for beam steering)

### Test Frequency Structure
- **Daily QA:** Output constancy, laser alignment, door interlocks, imaging system checks
- **Monthly QA:** Field size indicators, optical distance indicator, cross-hair centering, arc/rotation tests, CBCT QA
- **Annual QA:** Full output calibration, beam flatness/symmetry, MLC performance, IMRT delivery verification

### Relationship to TG-100
- TG-142 = **prescriptive/equipment-focused**: defines what to check and how often
- TG-100 = **risk-based/workflow-focused**: defines what to prioritize based on clinical risk
- They are complementary: TG-100 can guide which TG-142 tests deserve the most attention at a given institution based on their specific workflow risks

---

## TG-198 (2021) — Implementation Guide for TG-142

- **Title:** An Implementation Guide for TG-142 Quality Assurance of Medical Accelerators
- **Authors:** Hanley et al.
- **Journal:** Medical Physics
- **Year:** 2021
- **DOI:** 10.1002/mp.14992
- **URL:** https://aapm.onlinelibrary.wiley.com/doi/10.1002/mp.14992

### Purpose
- Practical implementation companion to TG-142
- Provides specific measurement procedures, equipment recommendations, and record-keeping guidance
- Addresses how to implement TG-142 in real clinical workflows

---

## TG-119 — IMRT Commissioning (Predecessor to TG-218)

- Defined initial acceptance criteria for IMRT delivery QA
- Established the **3%/3 mm gamma criterion** as standard for IMRT plan-specific QA
- Basis for patient-specific QA workflows; later updated/superseded by TG-218

---

## TG-218 (2018) — Patient-Specific IMRT/VMAT QA

- **Title:** Tolerance Limits and Methodologies for IMRT Measurement-Based Verification QA
- **Journal:** Medical Physics
- **Year:** 2018
- **PMC (Deng 2024 evaluation):** https://pmc.ncbi.nlm.nih.gov/articles/PMC11163510/
- **PMID (Deng 2024):** 38243604

### What TG-218 Covers
- Establishes **tolerance limits (TL)** and **action limits (AL)** for patient-specific QA (PSQA) for IMRT and VMAT
- Replaces the one-size-fits-all passing threshold with a **tolerance- and action limit-based workflow**
- Recommends **3%/2 mm** gamma criterion (more stringent than TG-119's 3%/3 mm)
- Emerging stricter criteria: 2%/2 mm and 1%/1 mm for high-precision treatments

### Key Recommendations
- **Standard AL (action level):** 90% gamma passing rate — plan must be re-evaluated if below
- **Standard TL (tolerance level):** 95% gamma passing rate — plan is acceptable above this
- Institutions should assess **clinical significance of dose errors** when plans fail, not just act on gamma number alone
- Recommends institution-specific TL/AL based on their own measurement system and plan complexity distribution

### Relationship to TG-100
- TG-218 addresses the **patient-specific QA step** within the treatment planning chain — a high-risk step identified by TG-100 FMEA
- Together with TG-100, they cover both the workflow risk analysis (TG-100) and the specific QA measurement standards at delivery (TG-218)

---

## Summary: How the TG Suite Fits Together

| Report | Year | Focus | Type |
|---|---|---|---|
| TG-40 | 1994 | Comprehensive LINAC QA | Prescriptive (foundational) |
| TG-100 | 2016 | Workflow risk analysis (FMEA/FTA) | Risk-based |
| TG-142 | 2009 | Modern LINAC machine QA | Prescriptive (equipment) |
| TG-198 | 2021 | Implementation guide for TG-142 | Practical guide |
| TG-119 | 2009 | IMRT commissioning benchmarks | Standards |
| TG-218 | 2018 | Patient-specific IMRT/VMAT QA tolerances | Standards |

**The philosophy shift:** TG-40 → TG-142 improved prescriptive machine QA. TG-100 introduced risk-based thinking. TG-218 + TG-100 together cover patient-specific QA with both measurement standards (TG-218) and risk prioritization (TG-100).
