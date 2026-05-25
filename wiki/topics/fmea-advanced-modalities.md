# FMEA for Advanced Radiotherapy Modalities

**Type:** Topic
**Status:** developing
**Last updated:** 2026-05-25
**Sources:** [fmea-advanced-modalities-mr-linac]

## Summary

FMEA has been successfully applied to advanced radiotherapy modalities including MR-guided adaptive radiotherapy (MRgRT), online adaptive SBRT, proton therapy, brachytherapy, and SRS. These workflows introduce modality-specific failure modes not present in conventional LINAC-based RT — particularly around time pressure, deformable image registration uncertainty, and the complexity of online replanning. Mitigation via automation, checklists, and interdisciplinary FMEA teams consistently reduces all risk categories to acceptable levels before clinical introduction.

## Key Facts / Claims

- TG-100 FMEA framework has been applied to: proton-beam RT, brachytherapy (HDR/LDR), SBRT, SRS, intraoperative electron RT, intrapelvic irradiation, and internal skin irradiation [fmea-advanced-modalities-mr-linac]
- **Klüter et al. 2021** (MR-linac, Heidelberg): P-FMECA identified **89 hazards** — 34% MR-device-specific, 46% adaptive planning, 20% general workflow [fmea-advanced-modalities-mr-linac]
- Pre-mitigation: 66% high-risk; post-mitigation: 0% high-risk (100% eliminated) [fmea-advanced-modalities-mr-linac]
- Three highest-priority MR-linac risks: undetected MRI-incompatible pacemaker (S=5,P=3); incorrect target volume recontouring (S=4,P=5); electron density assignment errors (S=4,P=5) [fmea-advanced-modalities-mr-linac]
- **Wilke et al. 2025** (adaptive SBRT, Zurich): 23 failure modes across 8 steps; median RPN 63; post-mitigation median RPN 24 (all reduced to low-risk) [fmea-advanced-modalities-mr-linac]
- RPN thresholds used: low <125, medium 125–250, high >250 [fmea-advanced-modalities-mr-linac]
- **Adaptive-specific risks** vs. conventional RT: time pressure during online planning; deformable image registration uncertainty; real-time decision-making limits error detection [fmea-advanced-modalities-mr-linac]
- **Key mitigation strategies** across modalities: four-eye verification principle, automated plan integrity checks, secondary Monte Carlo dose calculations, daily stability monitoring, SOPs per protocol step [fmea-advanced-modalities-mr-linac]
- Interdisciplinary teams (physicists + therapists + oncologists) are essential — single-discipline FMEA misses hazards [fmea-advanced-modalities-mr-linac]
- Novel workflows require FMEA **before** clinical introduction, not after [fmea-advanced-modalities-mr-linac]
- Regular FMEA updates recommended every 2–3 years or with major workflow changes [fmea-advanced-modalities-mr-linac]

## Connections

- [[fmea-radiotherapy]] — foundational FMEA methodology and RPN scoring framework; advanced modalities extend the same approach
- [[tg100-aapm]] — TG-100 is the endorsed framework applied in all these studies
- [[fmea-ai-automated-workflow]] — adaptive RT workflows increasingly incorporate AI-based contouring, introducing automation-specific risks
- [[rt-patient-safety-context-map]] — advanced modalities are a key gap in the field's current safety coverage
- [[aapm-tg-suite-linac-qa]] — TG-142 and MR-linac QA guidance complement FMEA risk analysis

## Open Questions

- How does FMEA scale to fully automated adaptive workflows with no human in-the-loop?
- What are the unique FMEA findings for proton therapy vs. photon therapy?
- How do HDR brachytherapy FMEA results compare to MR-linac FMEA results in failure mode severity?
- Are there validated FMEA templates for MR-linac workflows that departments can adopt directly?

## Raw Notes

- Klüter 2021 (MR-linac FMEA, Heidelberg): https://pmc.ncbi.nlm.nih.gov/articles/PMC8058032/
- Wilke 2025 (adaptive SBRT FMEA, Zurich): https://pmc.ncbi.nlm.nih.gov/articles/PMC12766485/
- ESAPI code shared publicly on GitHub by Wilke et al. for broader adoption
