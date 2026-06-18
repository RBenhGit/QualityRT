# Brachytherapy & HDR Safety

**Type:** Topic
**Status:** mature
**Last updated:** 2026-06-18
**Sources:** [richardson-nrc-brachy-2012], [thomadsen-hdr-guidance-2014]

## Summary
Brachytherapy — the placement of sealed radioactive sources in or next to a tumor — is regulated more tightly than linac-based external beam in the US because it uses byproduct material under Nuclear Regulatory Commission (NRC) jurisdiction, and every medical event must be reported within 24 hours. High-dose-rate (HDR) remote-afterloading brachytherapy is a mature (1960s-era), statistically very safe modality (≈0.02% medical-event rate, ~5-sigma), yet the events that do occur are overwhelmingly **human task-execution failures and failures to follow existing guidance**, not gaps in the guidance itself. The dominant, recurrent failure mode across HDR is the **"length" error** — mismeasuring or mis-entering applicator / catheter / transfer-tube length, which directs dose to the wrong location. NRC-event analyses also show that "simple," non-technological errors (wrong patient, wrong side, lost seeds, fetal exposure during I-131 therapy) persist, and that newer complex deliveries (HDR partial-breast, LDR prostate, Y-90 microspheres) generate disproportionate events. The professional response is process control: site-specific SOPs, independent second checks, NIST-traceable source assay, mandatory physician + physicist presence, proctored training, and FMEA-based quality management.

## Key Facts / Claims
### NRC event analysis (Richardson 2012)
- A review of NRC-reported events Jan 2009–Dec 2010 found **147 events**, far surpassing historical rates (Ostrom: 35 in 1991–92; Thomadsen: 134 over the 21 years 1980–2001) — reflecting both more reporting and more complex/high-volume delivery [richardson-nrc-brachy-2012]
- By modality: **66 low-dose-rate (LDR), 34 radiopharmaceutical, 33 HDR, 13 Gamma Knife**, 1 unspecified [richardson-nrc-brachy-2012]
- By error type: **wrong dose (81) > wrong site (35) > lost/leaking source (14) > unintended exposure (13)**; wrong-site predominated in HDR, wrong-dose in LDR [richardson-nrc-brachy-2012]
- By cause: **human error dominated (97 of 147)**, then equipment malfunction (23), lack of training (12), communication (10) [richardson-nrc-brachy-2012]
- The single most common HDR error was **measuring or entering applicator/treatment length incorrectly (11 events)**; partial-breast applicators were especially error-prone (5 catheter-length events, including two off by 10 cm — one yielding a skin dose >68 Gy) [richardson-nrc-brachy-2012]
- Persisting "low-tech" failures: 6 fetal exposures during I-131 thyroid ablation (pregnancy/communication failures); lost prostate seeds; wrong-side Gamma Knife and Y-90 lobe; a transposed (x,y,x)-for-(x,y,z) localizer-coordinate error [richardson-nrc-brachy-2012]
- The NRC's then-current LDR prostate **medical-event definitions** were dose-based — **wrong dose = D90 < 80%** of intended, **wrong site = ≥20% of seeds outside the prostate**; ASTRO recommended shifting the definition to air-kerma (source-strength) based [richardson-nrc-brachy-2012]
- Recommended mitigations: multiple independent applicator-length measurements; vendors publishing standard applicator lengths; pre-treatment fluoroscopic/imaging verification of applicator position before any brachytherapy delivery [richardson-nrc-brachy-2012]

### ASTRO HDR safety/QM white paper (Thomadsen 2014)
- The ASTRO HDR brachytherapy safety white paper (approved Sept 2013) found the **US HDR medical-event rate in 2009–2010 was ≈0.02%** (≈8 events per 33,000 treatments/yr) — **5-sigma performance** [thomadsen-hdr-guidance-2014]
- Crucially, events were **not due to lack of guidance documents** but to failures to follow guidance already in departmental policy, or human failures in task performance [thomadsen-hdr-guidance-2014]
- Historically (per ICRP Publication 97) there were **>500 HDR brachytherapy accidents worldwide (including 1 death) before 2005**, spanning the chain from source packing to delivery; the US rate has since stabilized at <10 events/yr (~0.024%) [thomadsen-hdr-guidance-2014]
- The most common individual-application failure is the **"length" failure** (wrong transfer tube, mismeasured tube/applicator length, wrong starting position) — flagged as a target for vendor/equipment redesign [thomadsen-hdr-guidance-2014]
- **No single QMP fits all brachytherapy** — the procedural step order varies by application (e.g., tandem-and-ovoid vs. template implant), so forcing a generalized program "creates a hazardous environment"; QMPs must be built per-procedure on TG-59 principles using TG-100 tools [thomadsen-hdr-guidance-2014]
- Regulatory: the NRC mandates the **authorized user (radiation oncologist) and authorized medical physicist be physically present throughout each HDR treatment** (within unamplified-voice range) [thomadsen-hdr-guidance-2014]
- Training: the panel recommends **direct observation of ≥5 proctored patient treatments per disease site** before any team member (oncologist, physicist, dosimetrist, therapist, surgeon) practices independently [thomadsen-hdr-guidance-2014]
- Six **key measures to avoid catastrophic failures**: appropriate TG-59 team; physicist-verified commissioning of unit/TPS/each new source; **NIST-traceable well-chamber source assay at every source change** (agreeing within 5% of manufacturer); follow ABS site guidelines; independent verification of plans/programs before delivery; daily QA before any treatment [thomadsen-hdr-guidance-2014]
- The accepted dose-delivery accuracy for brachytherapy is **~15% (per AAPM TG-40), much looser than the ~5% for EBRT** — reflecting steep dose gradients and source-positioning uncertainty [thomadsen-hdr-guidance-2014]
- Source strength must be specified in a NIST-traceable quantity (air-kerma strength); **"apparent activity" is explicitly discouraged** — unit-confusion has itself caused reportable events [thomadsen-hdr-guidance-2014]
- Anticipated future hazards: model-based (Monte Carlo) dose algorithms requiring new QA; EMR loss of hand-drawn implant pictures; CT-sim replacing fluoroscopy; proliferation of applicators/radionuclides (e.g., the source-switching risk of dual Co-60/Ir-192 units) outpacing process control [thomadsen-hdr-guidance-2014]

## Connections
- [[advanced-modality-rt-safety]] — the companion ASTRO Target Safely white papers on IMRT and SRS/SBRT; small-field/commissioning failures rhyme with HDR length/assay failures
- [[fmea-radiotherapy]] — both papers explicitly point to FMEA / AAPM TG-100 as the framework for building site-specific brachytherapy QMPs; the NRC event taxonomy feeds FMEA
- [[tg100-aapm]] — TG-100 risk-based QM is the recommended tool for crafting per-procedure brachytherapy quality management
- [[incident-learning-systems-international]] — the NRC database is itself an incident-learning source; Thomadsen urges AAPM to build a dedicated HDR event-report database
- [[ro-ils]] — RO-ILS captures brachytherapy near-misses nationally and complements mandatory NRC reporting
- [[regulatory-framework-rt-usa]] — brachytherapy's byproduct-material status puts it under NRC 10 CFR 35 (medical-event reporting, physical-presence rules, Agreement States)
- [[peer-review-radiotherapy]] — the HDR white paper highlights peer review and ChartRounds as defenses against task-execution failures
- [[iaea-safety-reports-17]] — ICRP Pub 97 and IAEA accident catalogs document the historical HDR accident record this guidance responds to
- [[human-factors-rt-safety]] — "human error" causing 97/147 NRC events, and persistent wrong-patient/wrong-side failures, are classic human-factors targets
- [[audit-accreditation-radiotherapy]] — ongoing self-audit and external audit of clinical practice is a core Thomadsen recommendation; ACR HDR practice standards anchor accreditation

## Open Questions
- Did the NRC adopt ASTRO's air-kerma-based (rather than dose-based) definition of an LDR prostate medical event, and how did that change reported-event counts?
- Has a dedicated AAPM HDR brachytherapy event-report database been established as Thomadsen recommended?
- How have model-based dose-calculation algorithms (TG-186) and electronic brachytherapy changed the HDR event profile since 2014?
- Do the "length"-failure engineering fixes (vendor-published lengths, redesigned applicators) measurably reduce events?

## Raw Notes
- [richardson-nrc-brachy-2012]: Richardson S, "A 2-year review of recent Nuclear Regulatory Commission events: What errors occur in the modern brachytherapy era?" *Pract Radiat Oncol* 2:157–163 (2012). Washington Univ. / Mallinckrodt. Data from NRC Event Notification Reports (nrc.gov), Jan 2009–Dec 2010.
- [thomadsen-hdr-guidance-2014]: Thomadsen BR, Erickson BA, Eifel PJ, Hsu I-C, Patel RR, Petereit DG, Fraass BA, Rivard MJ, "A Review of Safety, Quality Management, and Practice Guidelines for High-Dose-Rate Brachytherapy" (supplemental material), *Pract Radiat Oncol* (2014). ASTRO Target Safely white paper, approved Sept 21 2013. Relies on AAPM TG-40 (Rpt 46), TG-56 (Rpt 59), TG-59 (Rpt 61), TG-53 (Rpt 62), TG-128, TG-100; ABS site-specific consensus guidelines; ICRP Pub 97.
- Historical references within: Ostrom 1991–92 misadministrations; Thomadsen 2003 (134 events, 1980–2001); ICRP Pub 97 (Prevention of HDR brachytherapy accidents, 2005).
