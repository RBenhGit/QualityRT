# Lessons from RT Accidents & Aviation Safety

**Type:** Topic
**Status:** mature
**Last updated:** 2026-07-11
**Sources:** [knoos-lessons-accidents-2017], [davies-aviation-safety-2017], [rt-safety-shield-pptx], [rt-safety-shield-traits-pptx]

## Summary
Two complementary 2017 *Clinical Oncology* reviews frame how radiation oncology should learn from harm. Knöös compiles the canonical external-beam and brachytherapy **accident case studies** of the last ~20 years, distilling recurring causal patterns: commissioning/calibration errors that systematically affect every patient on a unit, software/process changes whose procedures were not updated, reliance on a single physicist with no independent secondary check, and loss of awareness during unusual treatments. Davies & Delaney examine what the **aviation industry** can actually teach: not wholesale imitation (the analogy is "illusionary" because the domains differ fundamentally) but adaptation of three concepts — **investment in safety, human factors, and safety management systems (SMS)** — and a pointed critique that healthcare over-counts incident-report *rates* while under-investing in learning and action. Together they argue for defence-in-depth: independent checks, external audit, competent trained staff, defined roles, a just/no-blame culture, and proactive + concurrent + reactive safety information.

## Key Facts / Claims
### Accident case studies

#### Zaragoza, Spain (1990) — post-repair energy error
- **Correction:** earlier versions of this page wrongly named this accident "Salamanca." The source decks label it only **"Spain (1990)"**; the actual site was **Zaragoza** (Hospital Clínico Universitario), the well-documented 1990 Sagittaire-accelerator accident. Do not call it Salamanca.
- **Spain (Zaragoza), 1990:** after **engineers repaired an accelerator fault, no independent physicist check was performed** and the console **displayed a wrong value**; the machine emitted its maximum energy — **36 MeV instead of 6 MeV**. Of **27 patients** treated in the faulty state, **at least 15 died** [rt-safety-shield-traits-pptx]. (The earlier deck [rt-safety-shield-pptx] states "at least 17"; the death toll is ~15–17 in the decks and ~11–15+ in the literature — no primary source is cited in the decks, so treat as approximate.)
- Core lesson: the single point of failure was the **absence of an independent verification after a technical repair** before returning to clinical use — every patient treated in the faulty mode was harmed [rt-safety-shield-traits-pptx]
- The later deck's Insight Bar frames the common denominator across the Spain (Zaragoza) and Glasgow cases as: system overload, communication failure, and absence of double-checks at decision points [rt-safety-shield-traits-pptx]

#### From Knöös 2017
- Globally ~13,000 RT treatment units (≈1,900 Co-60) deliver ≈115 million fractions/yr — vast opportunity for the complex process to fail; the **Heinrich triangle (1 major : 30 minor : 300 near-miss)** frames why near-misses are the rich learning substrate [knoos-lessons-accidents-2017]
- **Exeter, UK (1998):** after a Co-60 source change a physicist entered the wrong measurement time, producing a 25% overdose to **153 patients**; not detected clinically but by a *national dosimetry audit* — no independent dose-rate check existed [knoos-lessons-accidents-2017]
- **Ottawa, Canada (2004):** orthovoltage re-commissioning omitted the backscatter factor for non-reference cones; over 3 years **620 patients (1,019 treatments)** were affected, 326 with clinically significant underdose up to 17%, caught only at annual review — again no documented secondary check [knoos-lessons-accidents-2017]
- **Glasgow, UK / Lisa Norris (2005–06):** a software upgrade made MU-scaling automatic, but an un-updated cranio-spinal form caused the prescription dose (1.67 Gy) to be applied twice → **67% overdose** (55.56 Gy delivered to a prescribed 33.3 Gy spinal cord target over 17 fractions); contributing factors: inexperienced planner, supervisor (non-independent) check, understaffing, procedures not updated [knoos-lessons-accidents-2017], [rt-safety-shield-pptx]
- **New York / St Vincent's (2005):** during an IMRT replan the workstation crashed; the plan was saved with the MLC **wide open** and patient-specific QA was skipped → 13 Gy instead of 2 Gy per fraction; the patient died ~2 years later [knoos-lessons-accidents-2017]
- **North Staffordshire, UK (1982–91):** an inverse-square correction was applied twice for isocentric treatments for 9 years; **1,045 patients underdosed 5–35%, with 492 local recurrences attributed to the error** [knoos-lessons-accidents-2017]
- Core lessons: new/re-commissioned units must be independently checked before clinical use (single-physicist reliance is repeatedly hazardous); internal and preferably external audit (dosimetric *and* clinical); competent trained staff; defined roles; awareness during unusual treatments; **defence-in-depth** so that if one barrier fails an independent one catches it; no-blame/just culture focused on system not individual [knoos-lessons-accidents-2017]

### Aviation safety, adapted (Davies & Delaney 2017)
- The aviation–healthcare analogy is **"illusionary"** for wholesale adoption; what succeeds is *adaptation* of specific concepts, with "lessons learned and illustrative materials" drawn from healthcare itself [davies-aviation-safety-2017]
- Three transferable concepts: **(1) investment in safety** (it is cheaper to be safe than to deal with an accident's aftermath); **(2) human factors** (the SHEL/SHELL model — software, hardware, environment, liveware — integrating the human into organisation and regulator context, not a narrow "the human factor"); **(3) a safety management system (SMS)** [davies-aviation-safety-2017]
- SMS evolved over ~7 decades (US Air Force Ballistic Missile Division 1950s–60s → ICAO mandated SMS for operators worldwide by 2006, structured on four pillars: policy, risk management, safety assurance, safety promotion incl. "just culture") [davies-aviation-safety-2017]
- The authors propose a healthcare **"Six Ps" SMS** — Philosophy, Policy, Procedures, Practices, Products, Performance — mapped to Donabedian structure/process/outcome, led from the CEO/board down [davies-aviation-safety-2017]
- An SMS needs information from **three sources: proactive (FMEA), concurrent (real-time/prospective audits), and reactive (voluntary confidential incident reports)** — no single source suffices; at Johns Hopkins, FMEA found 127 then 159 failure modes, yet FMEA *missed 42% of the actual errors* that incident reporting caught [davies-aviation-safety-2017]
- Sharp critique: healthcare over-relies on **counting and benchmarking report rates** — which "monitor reporting, not safety" — producing "a strong culture of reporting but a poor culture of learning"; aviation instead concentrates effort on prioritisation, investigation, and action, and prefers independent (non-managerial) reporting channels to avoid fear of retribution [davies-aviation-safety-2017]
- RO is converging on standardised terminology and pooled learning via SAFRON (IAEA), ROSIS, CPQR, and RO-ILS — important when introducing a new technique, to learn from others' reports [davies-aviation-safety-2017]

## Connections
- [[incident-learning-systems-international]] — both papers rest on incident learning; Knöös cites the Heinrich 1:30:300 ratio and the IAEA SRS-17 catalog; Davies critiques rate-counting vs. learning
- [[iaea-safety-reports-17]] — IAEA Safety Report 17 (≈90 accidental exposures) is the accident catalog Knöös draws from
- [[human-factors-rt-safety]] — SHEL/SHELL, just culture, awareness, and system-not-individual focus are the shared human-factors core
- [[just-culture-radiotherapy]] — both the Spain (Zaragoza) 1990 and Glasgow cases illustrate how the absence of Just Culture (fear of reporting, single-point oversight) lets system failures persist
- [[fmea-radiotherapy]] — Davies positions FMEA as the proactive leg of an SMS; notes FMEA alone missed 42% of incident-reported errors
- [[radiation-safety-culture-healthcare]] — just/no-blame culture and leadership-set safety standards are central to both
- [[advanced-modality-rt-safety]] — the St Vincent's IMRT and Glasgow cases are advanced-modality commissioning/process failures; small-field & commissioning checks echo here
- [[brachytherapy-hdr-safety]] — Knöös explicitly covers brachytherapy accidents alongside EBRT
- [[audit-accreditation-radiotherapy]] — the central remedy in Knöös is independent/external audit before clinical use
- [[rt-quality-management]] — defence-in-depth and the SMS framework are the QM scaffolding these lessons motivate
- [[ro-ils]] — named as a pooled-learning database that lets departments learn from others' events
- [[tg100-aapm]] — TG-100 FMEA is the proactive-analysis tool Davies recommends embedding in an SMS

## Open Questions
- What is the optimal balance of investment between proactive (FMEA), concurrent (audit), and reactive (reporting) safety activities for a typical department?
- How can RO shift from "counting reports" to a genuine "culture of learning" at scale?
- Would a formal, centrally mandated SMS (as ICAO mandates for aviation) measurably outperform today's sporadic adoption in healthcare?
- **Conflict — Spain 1990 (Zaragoza) death toll:** the two versions of the departmental deck disagree (15 vs 17 deaths of 27 affected patients). Neither cites an underlying primary source (e.g. IAEA Safety Reports Series 17, which Knöös draws on for other cases). What is the authoritative fatality count?

## Raw Notes
- [knoos-lessons-accidents-2017]: Knöös T, "Lessons Learnt from Past Incidents and Accidents in Radiation Oncology," *Clinical Oncology* 29:557–561 (2017). Lund University, Sweden. Case sources include the Exeter, Ottawa, Glasgow (Lisa Norris), St Vincent's NY, and North Staffordshire inquiry reports, and IAEA Safety Report Series 17.
- [davies-aviation-safety-2017]: Davies JM, Delaney G, "Can the Aviation Industry be Useful in Teaching Oncology about Safety?" *Clinical Oncology* 29:669–675 (2017). Univ. of Calgary / UNSW. Six-Ps SMS adapted from Degani & Wiener flight-deck "P" frameworks; references ICAO SMS, James Reason just culture, Johns Hopkins FMEA (Ford 2009 / Terezakis 2011).
- [rt-safety-shield-traits-pptx]: Later/expanded version of [rt-safety-shield-pptx] (`raw/Radiotherapy_Safety_Shield_with_traits.pptx`), 15 slides. Slide 3 repeats the Spain-1990/Glasgow case studies (labels the Spanish case only "ספרד/Spain") with a differing death count. See [[human-factors-rt-safety]] for the full source note.
