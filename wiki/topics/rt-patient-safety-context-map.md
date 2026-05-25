# Context Map: Patient Safety & Quality in Radiotherapy

**Type:** Synthesis
**Status:** developing
**Last updated:** 2026-05-25
**Sources:** [tg100-aapm-2016], [ro-ils-astro-aapm], [who-radiotherapy-risk-profile-2008], [iaea-safety-reports-17-2000], [fmea-jacmp-broggi-2013]

## Summary

Radiotherapy (RT) patient safety and quality management is a multidisciplinary field at the intersection of clinical oncology, medical physics, systems engineering, and institutional safety culture. Its central challenge is that RT treatments are highly complex, multi-step clinical processes involving large teams, sophisticated technology, and irreversible biological effects — making both under-dose (tumor recurrence) and over-dose (radiation injury) potentially fatal errors. The field is organized around three complementary orientations: retrospective learning from accidents (WHO, IAEA), prospective proactive risk analysis (TG-100, FMEA), and continuous national incident learning (RO-ILS).

---

## Key Facts / Claims

- The treatment chain spans at least 8 distinct stages, each with documented failure modes [tg100-aapm-2016]
- Contouring and treatment planning together account for ~30% of all RO-ILS-reported incidents [ro-ils-astro-aapm]
- The WHO analyzed 3,125 errors and 4,616 near-misses; dosimetry errors are the most common contributing factor [who-radiotherapy-risk-profile-2008]
- Most accidents involve multiple simultaneous failures — not a single isolated error [iaea-safety-reports-17-2000]
- RPN = Severity × Occurrence × Detectability; threshold of ~125 used for mandatory mitigation [fmea-jacmp-broggi-2013]
- Defense-in-depth (multiple independent safety layers) is the foundational preventive principle [iaea-safety-reports-17-2000]
- RO-ILS is federally protected under PSQIA 2005; data cannot be used in malpractice litigation [ro-ils-astro-aapm]

---

## Domain Orientation Map

| Orientation | Approach | Key Sources |
|---|---|---|
| **Retrospective** | Learn from accidents and near-misses that already occurred | [who-radiotherapy-risk-profile], [iaea-safety-reports-17] |
| **Prospective** | Proactively map workflows and identify failure modes before they occur | [tg100-aapm], [fmea-radiotherapy] |
| **Continuous** | Ongoing national incident learning and benchmarking | [ro-ils] |

---

## Governing Bodies & Organizations

### International
- **WHO** — Radiotherapy Risk Profile (2008); evidence-based global safety recommendations [[who-radiotherapy-risk-profile]]
- **IAEA** — Safety Reports Series No. 17 (2000); accident analyses; SEPAR framework [[iaea-safety-reports-17]]

### U.S. National
- **AAPM** — TG-100 report; co-sponsor of RO-ILS [[tg100-aapm]]
- **ASTRO** — Target Safely initiative (2010); co-sponsor of RO-ILS [[ro-ils]]
- **ABR** — MOC Part 4 credit via RO-ILS participation
- **Clarity PSO** — Operations partner for RO-ILS; federally recognized Patient Safety Organization
- **RO-HAC** — 8-member expert council that reviews RO-ILS data and issues alerts

---

## Core Frameworks & Methodologies

### Process Mapping
Step-by-step documentation of every clinical activity from patient consult through treatment delivery. Surfaces hand-offs between team members — a primary error source. Foundation for FMEA. [tg100-aapm]

### Failure Modes and Effects Analysis (FMEA)
Bottom-up risk analysis starting at individual failure modes and tracing effects upward. RPN = S × O × D (each 1–10; range 1–1,000). Formally endorsed by TG-100. [[fmea-radiotherapy]]

### Fault Tree Analysis (FTA)
Top-down complement to FMEA: starts from a known adverse outcome and traces back to root causes. Used for post-incident analysis and redundant safety system design. [tg100-aapm]

### Delivery Quality Assurance (DQA)
Mandatory comprehensive QA program encompassing all activities from patient entry through follow-up — not limited to physical/technical equipment checks. [who-radiotherapy-risk-profile]

### SEPAR (Safety Evaluation of Radiation Therapy Applied to Routine Practice)
IAEA-developed structured framework for systematic safety evaluation. Provides checklists against which a facility can test its own vulnerability. [iaea-safety-reports-17]

### Defense-in-Depth
Core IAEA safety principle: multiple independent safety layers are required; no single check is sufficient. Drives requirements for independent calibration, independent plan checks, and independent patient ID verification. [iaea-safety-reports-17]

---

## The Treatment Chain (Risk by Stage)

```
Patient Referral
      │
      ▼
Decision to Treat
      │
      ▼
Imaging (CT simulation, MRI)
      │
      ▼
★ CONTOURING (target + OAR delineation) ── HIGHEST RISK
  • Incorrect/missing overlapping structures
  • Wrong overlap priority assignment
  • ~30% of RO-ILS incidents occur in planning phase
      │
      ▼
★ TREATMENT PLANNING ─────────────────────── HIGH RISK
  • CT calibration curve selection errors
  • Wrong fraction number specification
  • Ambiguous physician instructions
  • Plan revisions under time pressure
      │
      ▼
★ DATA TRANSFER (DICOM export/import) ─────── HIGH RISK
  • Manual transcription errors
  • DICOM parameter mapping errors
      │
      ▼
★ PATIENT SETUP / POSITIONING ─────────────── HIGH RISK
  • Patient identification errors
  • Isocenter alignment errors
      │
      ▼
Treatment Delivery (~26% of RO-ILS incidents)
  • HDR brachytherapy: source guide tube errors
  • Applicator diameter errors
      │
      ▼
Treatment Verification
      │
      ▼
Follow-Up
```

---

## The Incident Learning Ecosystem

```
Individual institution logs event
          │
          ▼
    RO-ILS portal (secure, PSQIA-protected)
          │
          ▼
    Clarity PSO (federal legal protection)
          │
          ▼
    RO-HAC analysis (8-person expert council)
          │
    ┌─────┴──────────────────────┐
    ▼                            ▼
Participant alerts          Quarterly benchmarking
(urgent safety patterns)    reports to institutions
          │
          ▼
Community case studies & safety notices
```

---

## Foundational Literature Timeline

| Year | Publication | Type | Key Contribution |
|---|---|---|---|
| 2000 | IAEA Safety Reports No. 17 | Retrospective | SEPAR; defense-in-depth; accident case studies |
| 2008 | WHO Radiotherapy Risk Profile | Retrospective | 3,125 errors analyzed; mandatory DQA |
| 2010 | RO-ILS launched | Continuous | National U.S. non-punitive learning system |
| 2013 | Broggi et al. (JACMP) | Practical | FMEA on tomotherapy; RPN >125 threshold |
| 2016 | AAPM TG-100 | Prospective | Formal endorsement of process mapping + FMEA + FTA |

**Intellectual lineage:** IAEA (2000) → WHO (2008) establish the evidence base → TG-100 (2016) formalizes proactive tools → RO-ILS provides continuous empirical feedback → FMEA studies (2013+) operationalize at department level.

---

## Relationships Between Sources

```
┌──────────────────────────┐
│  RETROSPECTIVE EVIDENCE  │
│  WHO + IAEA              │  "What went wrong"
│  [[who-radiotherapy-risk-profile]]
│  [[iaea-safety-reports-17]]
└───────────┬──────────────┘
            │ informs
            ▼
┌──────────────────────────┐
│   PROSPECTIVE TOOLS      │
│   TG-100 (FMEA/FTA)      │  "What could go wrong"
│   [[tg100-aapm]]         │
│   [[fmea-radiotherapy]]  │
└───────────┬──────────────┘
            │ calibrated by
            ▼
┌──────────────────────────┐
│   CONTINUOUS LEARNING    │
│   RO-ILS                 │  "What is going wrong"
│   [[ro-ils]]             │
└───────────┬──────────────┘
            │ feeds back into
            ▼
┌──────────────────────────┐
│   PRACTICAL STUDIES      │
│   Broggi 2013 + others   │  "How to fix it here"
│   [[fmea-radiotherapy]]  │
└──────────────────────────┘
```

---

## Key Concepts Glossary

| Concept | Definition | Source |
|---|---|---|
| RPN | Risk Priority Number = S × O × D; prioritizes failure modes | [fmea-radiotherapy] |
| FMEA | Failure Modes and Effects Analysis; bottom-up proactive risk tool | [fmea-radiotherapy] |
| FTA | Fault Tree Analysis; top-down root-cause tool | [tg100-aapm] |
| DQA | Delivery Quality Assurance; mandatory comprehensive QA program | [who-radiotherapy-risk-profile] |
| SEPAR | IAEA safety evaluation framework for RT | [iaea-safety-reports-17] |
| Just Culture | Non-punitive safety reporting environment | [ro-ils] |
| PSQIA | U.S. federal law protecting incident reports submitted to PSOs | [ro-ils] |
| PSO | Patient Safety Organization; federally recognized incident keeper | [ro-ils] |
| RO-HAC | Radiation Oncology Healthcare Advisory Council | [ro-ils] |
| Defense-in-Depth | Multiple independent safety layers; no single point of failure | [iaea-safety-reports-17] |
| Process Mapping | Step-by-step documentation of clinical workflow | [tg100-aapm] |

---

## Connections

- [[tg100-aapm]] — core prospective QM framework; FMEA/FTA/process mapping
- [[fmea-radiotherapy]] — FMEA methodology, RPN scoring, high-risk stages
- [[ro-ils]] — national continuous incident learning system
- [[who-radiotherapy-risk-profile]] — retrospective accident evidence base (WHO)
- [[iaea-safety-reports-17]] — retrospective accident evidence base (IAEA); SEPAR
- [[radiotherapy-sources]] — master index of the five core authoritative sources
- [[rt-quality-management]] — companion synthesis: QM program structure, glossary, key terms

## Open Questions

- How do these frameworks apply to proton therapy, brachytherapy, and adaptive/MR-guided RT?
- What are the international equivalents to RO-ILS (UK NRLS, Australian systems)?
- How does AI-assisted contouring and planning change the FMEA risk profile?
- Which AAPM task group reports (TG-40, TG-142, TG-218) complement TG-100?
- What are country-specific regulatory frameworks (NRC, state radiation control programs)?
- How do staffing ratios, fatigue, and communication training affect the risk landscape?

## Raw Notes

This page is a synthesized context map generated from all currently compiled wiki pages. It should be updated each time a major new source is ingested. Highest-priority gaps for future ingestion: brachytherapy QM, proton therapy safety, TG-142 linac QA, AI/automation risks.
