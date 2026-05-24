# FMEA in Radiotherapy: Application to Pretreatment Phases in Tomotherapy (Broggi et al. 2013)

## Bibliographic Info

- **Title:** Application of failure mode and effects analysis (FMEA) to pretreatment phases in tomotherapy
- **Authors:** Sara Broggi, Marie Claire Cantone, Anna Chiara, Nadia Di Muzio, Barbara Longobardi, Paola Mangili, Ivan Veronese
- **Journal:** Journal of Applied Clinical Medical Physics (JACMP)
- **Volume/Issue:** Volume 14, Issue 5, Pages 265–277
- **Published:** September 6, 2013
- **PMID:** 24036868
- **URL:** https://pubmed.ncbi.nlm.nih.gov/24036868/

---

## Overview

This study demonstrates a practical implementation of FMEA methodology to assess and manage patient safety risks in helical tomotherapy treatments. It focuses on the pretreatment phases — covering preplanning imaging, volume determination, and treatment planning — and identifies which failure modes carry the highest risk using RPN scoring.

---

## Methodology

### Scope
Three critical pretreatment stages were analyzed:
1. **Preplanning imaging**
2. **Volume determination (contouring)**
3. **Treatment planning**

### FMEA Process
- **74 failure modes** identified across the two main stages:
  - 38 failure modes in imaging/volume determination
  - 36 failure modes in treatment planning
- Each failure mode scored on:
  - **Severity (S):** 1–10 scale
  - **Occurrence (O):** 1–10 scale
  - **Detectability (D):** 1–10 scale
  - **RPN = S × O × D** (range: 1–1,000)
- **RPN threshold for acceptable risk:** 125
- Failure modes exceeding RPN 125 require mitigation actions.

---

## Critical Findings: High-Risk Failure Modes (RPN > 125)

Four failure modes exceeded the safety threshold:

1. **Incorrect definition or omission of overlapping anatomical region contouring**
   - Missing or incorrect contouring of structures that overlap in the treatment field.
   - Identified as the highest-risk single failure mode.

2. **Improper overlap priority assignment to structures**
   - Incorrect assignment of which structure takes dosimetric priority when structures overlap.
   - Critical because it directly affects dose distribution calculation.

3. **Unsuitable CT calibration curve selection for dose calculations**
   - Using the wrong Hounsfield Unit–to–density calibration curve.
   - Leads to systematic dose calculation errors across the entire plan.

4. **Inadequate or absent fraction number specification during planning**
   - Failure to correctly specify the number of treatment fractions.
   - Can lead to systematic over- or under-dosing of the patient.

---

## Mitigation Actions Proposed

Beyond existing safety protocols, the authors proposed additional strategies:
- Standardizing checklist templates for contouring review.
- Automating electronic data transfers (e.g., DICOM export) to reduce transcription errors.
- Establishing robust physical setups and independent plan checks.
- Implementing peer review for contour delineation, especially for complex or overlapping structures.

---

## Broader Context: High-Risk Stages in Radiotherapy

This paper confirms and quantifies findings consistent with other literature:
- **Contouring** is consistently identified as one of the highest-risk steps across all radiotherapy platforms (not just tomotherapy).
- **Treatment planning system data transfer** (e.g., DICOM, couch-density corrections) is a known high-RPN category.
- **Patient positioning** is another high-risk stage identified in the broader radiotherapy FMEA literature.

---

## Relationship to TG-100

- Broggi et al. applied the same FMEA framework advocated by TG-100 (Huq et al. 2016), but was published three years earlier — demonstrating that FMEA was already being implemented in radiotherapy before TG-100's formal endorsement.
- The RPN scoring methodology (S × O × D, scale 1–10, threshold ~125) is consistent with TG-100 guidance.
- Confirms TG-100's emphasis on contouring and treatment planning as the highest-risk phases.

---

## Related Literature

- Automated contouring FMEA: "Using Failure Mode and Effects Analysis to Evaluate Risk in the Clinical Adoption of Automated Contouring and Treatment Planning Tools" — *Practical Radiation Oncology* (2022): https://www.practicalradonc.org/article/S1879-8500(22)00008-X/fulltext
- FMEA in proton beam radiotherapy: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3679803/
