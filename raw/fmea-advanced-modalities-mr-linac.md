# FMEA for Advanced Radiotherapy Modalities: MR-Linac, Adaptive RT, and SBRT

## Overview

Failure Mode and Effects Analysis (FMEA) has been applied to advanced and novel radiotherapy modalities including MR-guided adaptive radiotherapy (MRgRT), SBRT, proton therapy, brachytherapy, and stereotactic radiosurgery (SRS). These workflows introduce modality-specific risks not present in conventional LINAC-based radiotherapy.

---

## Source 1: Klüter et al. 2021 — MR-Guided Adaptive Radiotherapy (MR-Linac)

- **Title:** A practical implementation of risk management for the clinical introduction of online adaptive Magnetic Resonance-guided radiotherapy
- **Authors:** Sebastian Klüter, Oliver Schrenk, et al. (University Hospital Heidelberg, Germany)
- **Journal:** Physics and Imaging in Radiation Oncology
- **Year:** 2021
- **PMID:** 33898779
- **PMC:** https://pmc.ncbi.nlm.nih.gov/articles/PMC8058032/

### FMEA Results

**Risk Identification (89 total hazards):**
- MR-specific/device-specific: 30 hazards (34%)
- Online adaptive treatment planning: 41 hazards (46%)
- General workflow: 18 hazards (20%)

**Pre-Mitigation Classification:**
- Low-risk (Class I): 11 (12%)
- Medium-risk (Class II): 19 (21%)
- High-risk (Class III): 59 (66%)

**Post-Mitigation Classification:**
- Low-risk: 28 (31%)
- Medium-risk: 61 (68%)
- High-risk: 0 (all eliminated)

**Three highest-priority risks:**
1. Undetected MRI-incompatible cardiac pacemaker (S=5, P=3)
2. Incorrect target volume recontouring (S=4, P=5)
3. Electron density assignment errors (S=4, P=5)

**Key Mitigation Strategies:**
- Standardized operating procedures (SOPs) for each protocol step
- Four-eye verification principle for critical steps
- Automated plan integrity checking tools
- Secondary Monte Carlo dose calculations
- Enhanced staff training programs
- Daily stability monitoring

**Conclusion:** "Execution of the P-FMECA within an interdisciplinary team helped all involved occupational groups to develop and foster an open culture of safety."

---

## Source 2: Wilke et al. 2025 — MR-Enhanced Daily Adaptive SBRT

- **Title:** Safety in MR-enhanced daily adaptive SBRT Radiotherapy using a conventional C-arm linear accelerator: An FMEA approach
- **Authors:** Wilke L., Christ S.M., Dal Bello R., et al. (11 authors, University Hospital Zurich, Switzerland)
- **Journal:** Zeitschrift für Medizinische Physik
- **Year:** 2025 (June 3)
- **PMC:** https://pmc.ncbi.nlm.nih.gov/articles/PMC12766485/

### FMEA Results

**Framework:** AAPM TG-100
**Team:** 11 experts (5 physicists, 3 therapists, 3 oncologists)
**RPN Classification:**
- Low risk: RPN < 125
- Medium risk: RPN 125–250
- High risk: RPN > 250

**Initial Analysis:**
- Total failure modes: 23 across 8 process steps
- Median RPN: 63 (range 8–240)
- 17 low-risk (74%), 6 medium-risk (26%), 0 high-risk

**Before Mitigation:**
- 6 medium-risk failure modes: 4 during plan preparation, 2 during adaptive planning

**After Mitigation:**
- All 23 failure modes reduced to low-risk
- Median RPN decreased to 24 (range 6–96)

**Key Interventions:**
- Checklists verifying correct MRI selection and standard optimization constraints
- Scripts automating margin generation and auxiliary structure creation
- Automated monitoring: changes >20% in PTV size or MLC opening triggered physician-physicist review

**Adaptive vs. Conventional RT Risk Differences:**
- Time pressure during online planning creates heightened error vulnerability
- Deformable image registration introduces registration uncertainty
- Rapid contour adaptation requires standardized constraint libraries
- Real-time decision-making limits human error detection

**Code sharing:** ESAPI code published publicly on GitHub for broader adoption

---

## Broader Context: FMEA Across Modalities

TG-100 FMEA framework has been applied across:
- Proton-beam radiotherapy
- Brachytherapy (HDR/LDR)
- Intraoperative electron radiation therapy
- Stereotactic radiosurgery (SRS)
- SBRT
- Internal skin irradiation
- Intrapelvic irradiation

**Common findings across all advanced modalities:**
- Plan preparation and adaptive planning are consistently highest-risk steps
- Interdisciplinary team participation (physicists + therapists + oncologists) is essential
- Novel workflows require FMEA before clinical introduction, not after
- Mitigation via automation and checklist enhancement consistently reduces risks to low-risk level
- Regular FMEA updates (typically every 2–3 years or with major workflow changes) are required
