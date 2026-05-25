# Failure Mode and Effects Analysis (FMEA) in Radiotherapy

**Type:** Topic
**Status:** developing
**Last updated:** 2026-05-24
**Sources:** [tg100-aapm-2016], [fmea-jacmp-broggi-2013]

## Summary

Failure Mode and Effects Analysis (FMEA) is a proactive, bottom-up risk assessment tool applied to radiotherapy workflows to identify what can fail, score each failure mode by severity, occurrence, and detectability, and prioritize mitigation efforts using a Risk Priority Number (RPN). Formally endorsed by AAPM TG-100 (2016), FMEA has been implemented across radiotherapy departments worldwide and consistently identifies contouring, treatment planning data transfer, and patient positioning as the highest-risk stages of the treatment chain.

## Key Facts / Claims

- FMEA is a **bottom-up** risk analysis: starts from individual failure modes and assesses their effects upward through the system [tg100-aapm-2016]
- **RPN = Severity (S) × Occurrence (O) × Detectability (D)**, each scored on a 1–10 scale; RPN range: 1–1,000 [tg100-aapm-2016]
- Severity: how harmful is the failure if it occurs? [tg100-aapm-2016]
- Occurrence: how often does this failure happen? [tg100-aapm-2016]
- Detectability: how easily can the failure be caught before patient harm? [tg100-aapm-2016]
- Formally endorsed by AAPM **TG-100** (Huq et al., *Medical Physics*, 2016) as one of three core QM tools [tg100-aapm-2016]
- Broggi et al. (2013) applied FMEA to helical tomotherapy pretreatment phases, identifying **74 failure modes** across imaging, contouring, and planning stages [fmea-jacmp-broggi-2013]
- **RPN threshold of 125** used by Broggi et al. for acceptable risk; failure modes exceeding this require mitigation [fmea-jacmp-broggi-2013]
- Four failure modes exceeded RPN 125 in Broggi 2013: contouring of overlapping regions, overlap priority assignment, CT calibration curve selection, fraction number specification [fmea-jacmp-broggi-2013]
- **Contouring** is consistently identified as the highest-risk single failure mode across multiple FMEA studies [fmea-jacmp-broggi-2013]
- RO-ILS data confirms: treatment planning accounts for ~30% of all reported incidents nationally [tg100-aapm-2016]
- FMEA complements **Fault Tree Analysis (FTA)**: FMEA is bottom-up (failure → effect); FTA is top-down (adverse outcome → root causes) [tg100-aapm-2016]
- FMEA has been applied to automated contouring and planning tools to assess deployment risk [fmea-jacmp-broggi-2013]

## High-Risk Failure Mode Categories (Across Literature)

| Stage | Common High-RPN Failures |
|---|---|
| Contouring | Missing/incorrect overlapping structure delineation; incorrect overlap priority |
| Treatment Planning | CT calibration curve errors; fraction number errors; plan data transfer (DICOM) errors |
| Patient Setup/Positioning | Isocenter alignment errors; patient identification errors |
| Delivery | HDR brachytherapy source guide tube length errors; applicator diameter errors |

## Mitigation Strategies

- Standardized checklist templates for contouring review [fmea-jacmp-broggi-2013]
- Automated (not manual) electronic data transfers (DICOM export) to reduce transcription errors [fmea-jacmp-broggi-2013]
- Independent plan checks and peer review for complex contours [fmea-jacmp-broggi-2013]
- Robust physical setup protocols and patient ID verification at delivery [tg100-aapm-2016]

## Connections

- [[tg100-aapm]] — TG-100 is the formal AAPM endorsement of FMEA for radiotherapy QM; provides the conceptual framework
- [[ro-ils]] — RO-ILS national incident data provides empirical occurrence rates that calibrate the "O" score in FMEA
- [[who-radiotherapy-risk-profile]] — WHO's retrospective accident analysis identifies the same high-risk stages that FMEA proactively flags
- [[iaea-safety-reports-17]] — SEPAR framework complements FMEA; both address systematic safety evaluation in radiotherapy
- [[radiotherapy-sources]] — FMEA methodology is a central theme of the radiotherapy sources collection
- [[rt-quality-management]] — FMEA is a core component of a comprehensive RT QM program
- [[fmea-advanced-modalities]] — FMEA applied to MR-linac, adaptive RT, SBRT, proton, brachytherapy
- [[fmea-ai-automated-workflow]] — FMEA applied to AI-based contouring and fully automated treatment workflows
- [[human-factors-rt-safety]] — HFACS confirms the same high-risk stages (treatment planning, data transfer) as FMEA
- [[aapm-tg-suite-linac-qa]] — TG-218 patient-specific QA standards address the treatment planning output verification step identified as high-risk by FMEA

## Open Questions

- What is the best-practice RPN threshold: 125 (Broggi), 200, or institution-specific?
- How should FMEA be updated when a department introduces new technology (e.g., AI-based contouring, MR-linac)?
- Is there a standardized, nationally validated FMEA template for common radiotherapy workflows?
- How do FMEA findings from one institution transfer to another with different staffing and technology?

## Raw Notes

- Broggi et al. 2013 (JACMP): https://pubmed.ncbi.nlm.nih.gov/24036868/
- FMEA for automated contouring/planning (Practical Radiation Oncology, 2022): https://www.practicalradonc.org/article/S1879-8500(22)00008-X/fulltext
- FMEA in proton beam radiotherapy (PMC): https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3679803/
- TG-100 PDF: https://pps4rt.com/wp-content/uploads/2019/07/AAPM-TG-100-RT-Quality-Manageemnt.pdf
