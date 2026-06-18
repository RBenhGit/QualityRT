# Safety in Advanced RT Modalities (IMRT, SRS/SBRT)

**Type:** Topic
**Status:** mature
**Last updated:** 2026-06-18
**Sources:** [moran-imrt-safety-2011], [solberg-srs-sbrt-safety-2012], [schiff-dose-dissonance-2017]

## Summary
Advanced external-beam modalities — intensity-modulated radiation therapy (IMRT) and stereotactic radiosurgery / stereotactic body radiation therapy (SRS/SBRT) — deliver highly conformal, often ablative doses that improve outcomes but compress the margin of error and multiply process complexity. The ASTRO **Target Safely** white-paper series (IMRT 2011, SRS/SBRT 2012, plus IGRT, HDR, and peer-review papers) codifies the human-process and programmatic safeguards specific to each. Recurring themes: commissioning and small-field dosimetry are catastrophic single points of failure; QA must be end-to-end (not just equipment); time pressure that encourages skipping QA is the core hazard; and these techniques demand dedicated training, defined roles, robust hand-offs, and forced time-outs.

## Key Facts / Claims
### IMRT (Moran et al. 2011)
- The ASTRO IMRT safety white paper (approved Feb 2011) was endorsed by AAPM, AAMD, ASRT, and accepted by the ACR Commission on Radiation Oncology [moran-imrt-safety-2011]
- IMRT's conformality advantage is **counterbalanced by planning/delivery complexity**; an example IMRT workflow has **54 process steps and 15 hand-offs**, underscoring the need for clear roles and robust hand-offs [moran-imrt-safety-2011]
- Hazards split into **environmental** (no SOPs, haste, habituation, inadequate QA, lack of continuing education) and **technical** (inadequate commissioning, inadequate delivery-parameter validation, improper process use, uninvestigated plan-vs-QA discrepancies) [moran-imrt-safety-2011]
- **IMRT is considered unsafe to deliver emergently** because clinical pressure encourages skipping QA steps; the paper recommends a **"forced time-out"** and SOPs that *empower staff to halt* planning/treatment and forbid skipping QA [moran-imrt-safety-2011]
- Catastrophic-failure safeguards include independent dose verification, end-to-end data-transfer testing, patient-specific QA before first treatment, visual aperture review, and second-person review at multiple steps [moran-imrt-safety-2011]
- There is **no national consensus on IMRT QA pass/fail criteria**; the paper recommends each clinic validate its QA by deliberately creating errored plans that *should* fail [moran-imrt-safety-2011]

### SRS / SBRT (Solberg et al. 2012)
- The ASTRO SRS/SBRT white paper (approved April 2011) emphasizes that **the high dose per fraction shrinks the margin of error** — a small localization error in one fraction can underdose the tumor by ≥20% or seriously overdose adjacent normal tissue [solberg-srs-sbrt-safety-2012]
- Major publicized accidents illustrate the stakes: **Florida calibration error (77 patients, 2004–05); Toulouse, France output-factor error (145 patients; 31% 12-month trigeminal neuropathy); Springfield, MO (152 patients, 2004–09); a cranial-localization-accessory error across 7 US/European centers; backup-jaw errors (a French patient died; an Evanston, IL patient left in a vegetative state)** [solberg-srs-sbrt-safety-2012]
- Errors span all technologies (linac and Gamma Knife); a 1998 Gamma Knife 4-mm collimator output factor was corrected ~10%; an NRC database review found 13 gamma SRS events (2005+), 7 wrong-location [solberg-srs-sbrt-safety-2012]
- Echoing the UK experience (only 2 of 181 incidents non-human-error), most accidents are attributable to **human error compounded by equipment-design limits and inadequate QA systems** [solberg-srs-sbrt-safety-2012]
- **Small-field dosimetry is a critical vulnerability** (loss of lateral electronic equilibrium below ~10 mm); independent verification of small-field measurements and **independent absolute-calibration checks (e.g., the Radiological Physics Center)** are deemed essential [solberg-srs-sbrt-safety-2012]
- Commissioning must be **end-to-end** (whole treatment chain, anthropomorphic phantoms), not just equipment; pencil-beam dose algorithms are generally inadequate for the heterogeneities involved [solberg-srs-sbrt-safety-2012]
- SRS/SBRT is **not a single technique** — proficiency at one site (e.g., spine) does not transfer to another (e.g., lung); the paper urges site-specific training, that SRS/SBRT training become mandatory in residency, and that ACR-ASTRO accreditation become mandatory [solberg-srs-sbrt-safety-2012]

### Dose-prescription dissonance (Schiff 2017, on Das et al.)
- A 10-institution, ~5,100-patient study (Das et al.) found **compliance with the ICRU-83 IMRT prescribing/reporting standard (2010) was very low** — target naming, dose-prescription reporting, and dose-to-target levels varied significantly by institution, site, and technique [schiff-dose-dissonance-2017]
- Nearly **95% of patients had D50 above 100% of prescribed dose (103.5 ± 6.9%)**, with significant inter-institutional variability in D95, D50, and homogeneity index — i.e., "what dose was actually prescribed/delivered" is not standardized [schiff-dose-dissonance-2017]
- This "dose dissonance" undermines comparison of outcomes across trials (QUANTEC, radiogenomics); the editorial calls for **unifying dose prescription with international guidelines (ICRU-83) in every clinical trial** — a standardization-as-safety argument [schiff-dose-dissonance-2017]

## Connections
- [[fmea-advanced-modalities]] — FMEA has been applied to these same advanced modalities (MR-linac, SBRT, etc.); the catastrophic-failure focus parallels FMEA's high-risk failure modes
- [[peer-review-radiotherapy]] — prospective (pre-planning) peer review is especially high-impact for SBRT (target definition is the #1 peer-review priority); the IMRT paper defers peer-review detail to the dedicated ASTRO white paper
- [[tg100-aapm]] — TG-100 risk-based QM is the proactive framework these modality-specific safeguards instantiate
- [[human-factors-rt-safety]] — "forced time-outs," halt-authority, and avoiding emergent IMRT are human-factors defenses; most SRS/SBRT accidents trace to human error + design limits
- [[audit-accreditation-radiotherapy]] — the SRS/SBRT paper argues ACR-ASTRO accreditation should be mandatory; commissioning review is a low-compliance SPA indicator
- [[iaea-safety-reports-17]] — the historical SRS/SBRT accidents extend the accident catalog of the IAEA safety reports
- [[regulatory-framework-rt-usa]] — the paper highlights state/federal regulatory inconsistencies (radioactive vs X-ray sources) and calls for centralized event registries
- [[brachytherapy-hdr-safety]] — the companion high-dose modality with its own ASTRO HDR safety white paper

## Open Questions
- Has national consensus on IMRT patient-specific QA pass/fail criteria (gamma thresholds) since emerged?
- What is the current uptake of mandatory SRS/SBRT training and accreditation?
- How do MR-linac / online adaptive workflows change the catastrophic-failure profile for these modalities?

## Raw Notes
- [moran-imrt-safety-2011]: Moran JM, Dempsey M, Eisbruch A, Fraass BA, Galvin JM, Ibbott GS, Marks LB, "Safety considerations for IMRT: Executive summary," *Pract Radiat Oncol* 1:190–195 (2011). ASTRO Target Safely white paper.
- [solberg-srs-sbrt-safety-2012]: Solberg TD, Balter JM, Benedict SH, Fraass BA, Kavanagh B, Miyamoto C, Pawlicki T, Potters L, Yamada Y, "Quality and safety considerations in stereotactic radiosurgery and stereotactic body radiation therapy: Executive summary," *Pract Radiat Oncol* 2:2–9 (2012). ASTRO Target Safely white paper.
- [schiff-dose-dissonance-2017]: Schiff PB, "Dose Dissonance in Radiation Oncology: Consensus Needed When Prescribing Dose in Radiation Therapy," *Pract Radiat Oncol* (2017), doi:10.1016/j.prro.2017.04.018. NYU. Editorial on Das et al. *Pract Radiat Oncol* 7:e145–e155 (ICRU-83 compliance, ~5,100 patients, 10 academic centers).
- ASTRO Target Safely white-paper series also includes IGRT (Jaffray 2013), HDR brachytherapy (Thomadsen 2014), and peer review (Marks 2013).
