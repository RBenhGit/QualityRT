# AAPM Task Group Reports: The Linac QA Suite

**Type:** Topic
**Status:** developing
**Last updated:** 2026-05-25
**Sources:** [aapm-tg-suite-linac-qa]

## Summary

A suite of AAPM Task Group reports governs equipment-focused quality assurance for radiotherapy linear accelerators and patient-specific QA, complementing the workflow/risk-based approach of TG-100. The suite progresses from foundational prescriptive QA (TG-40, 1994) through modern machine QA (TG-142, 2009), to its implementation guide (TG-198, 2021), to patient-specific IMRT/VMAT QA standards (TG-119, TG-218). TG-100 and TG-142 are explicitly complementary: TG-100 determines what to prioritize based on risk; TG-142 defines what to measure and how often.

## Key Facts / Claims

- **TG-40 (1994):** Foundational comprehensive LINAC QA; Part A (administrators) + Part B code of practice; established written QA plan requirement; superseded by TG-142 in 2009 [aapm-tg-suite-linac-qa]
- TG-40 lead author: Gerald J. Kutcher et al.; *Medical Physics* 21(4):581–618, 1994; PMID 8058027 [aapm-tg-suite-linac-qa]
- **TG-142 (2009):** Major update replacing TG-40; added CBCT QA, MLC QA, asymmetric jaw QA, dynamic/virtual wedge; separated tests by treatment type (non-IMRT, IMRT, SRS/SBRT) [aapm-tg-suite-linac-qa]
- TG-142 SRS/SBRT tolerances are stricter than IMRT (e.g., 1 mm vs. 2 mm for beam steering) [aapm-tg-suite-linac-qa]
- TG-142 test structure: **Daily QA** (output constancy, lasers, interlocks), **Monthly QA** (field size, ODI, crosshair, CBCT), **Annual QA** (full calibration, flatness/symmetry, MLC, IMRT delivery) [aapm-tg-suite-linac-qa]
- **TG-198 (2021):** Practical implementation guide for TG-142; measurement procedures, equipment recommendations, record-keeping; *Medical Physics* DOI 10.1002/mp.14992 [aapm-tg-suite-linac-qa]
- **TG-119:** Established IMRT commissioning benchmarks and the original **3%/3 mm gamma criterion** for patient-specific QA [aapm-tg-suite-linac-qa]
- **TG-218 (2018):** Tolerance and action limit framework for IMRT/VMAT patient-specific QA; recommends **3%/2 mm** gamma criterion (more stringent than TG-119's 3%/3 mm) [aapm-tg-suite-linac-qa]
- TG-218 standard action level: **90% gamma passing rate** (plan must be re-evaluated); standard tolerance level: **95%** [aapm-tg-suite-linac-qa]
- TG-218 mandates assessment of clinical significance of dose errors when plans fail, not just the gamma number [aapm-tg-suite-linac-qa]
- **TG-100 vs. TG-142:** TG-100 = risk-based/workflow-focused (what to prioritize); TG-142 = prescriptive/equipment-focused (what to check and how often); explicitly complementary [aapm-tg-suite-linac-qa]

## The TG Suite at a Glance

| Report | Year | Focus | Type |
|---|---|---|---|
| TG-40 | 1994 | Comprehensive LINAC QA | Prescriptive (foundational) |
| TG-119 | 2009 | IMRT commissioning benchmarks | Standards |
| TG-142 | 2009 | Modern LINAC machine QA | Prescriptive (equipment) |
| TG-100 | 2016 | Workflow risk analysis (FMEA/FTA) | Risk-based |
| TG-198 | 2021 | Implementation guide for TG-142 | Practical guide |
| TG-218 | 2018 | Patient-specific IMRT/VMAT QA tolerances | Standards |

## Connections

- [[tg100-aapm]] — TG-100 is the risk-based complement to the prescriptive TG suite; TG-100 informs which TG-142 tests deserve highest priority
- [[fmea-radiotherapy]] — FMEA identifies treatment planning and data transfer as high-risk; TG-218 addresses the QA measurement standards for the planning output
- [[rt-patient-safety-context-map]] — the TG suite represents a key gap previously identified: complementary AAPM reports beyond TG-100
- [[fmea-advanced-modalities]] — TG-142 MR-linac QA guidance and TG-198 provide the prescriptive equipment layer for advanced modality workflows

## Open Questions

- Has TG-142 been updated for MR-linac and proton therapy equipment?
- What is AAPM TG-275 and how does it complement TG-100 for clinical workflow QA?
- How do TG-218 gamma passing rates correlate with actual clinical outcomes (dosimetric errors → patient harm)?
- What is the recommended integration of TG-100 FMEA risk scores with TG-218 action levels?

## Raw Notes

- TG-40 (AAPM Report 46 PDF): https://www.aapm.org/pubs/reports/RPT_46.PDF
- TG-40 PubMed: https://pubmed.ncbi.nlm.nih.gov/8058027/
- TG-142 (IROC/MD Anderson PDF): http://irochouston.mdanderson.org/RPC/home_page/files/TG-142%20-%20QA%20of%20medical%20accelerators.pdf
- TG-198 (*Medical Physics* 2021): https://aapm.onlinelibrary.wiley.com/doi/10.1002/mp.14992
- TG-218 evaluation (PMC 2024): https://pmc.ncbi.nlm.nih.gov/articles/PMC11163510/
