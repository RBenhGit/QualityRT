# FMEA for AI and Automated Radiotherapy Workflows

**Type:** Topic
**Status:** developing
**Last updated:** 2026-05-25
**Sources:** [fmea-ai-automated-workflow]

## Summary

As AI-based contouring, automated treatment planning, and fully automated radiotherapy workflows (FAW) enter clinical practice, FMEA has been applied to characterize the new risk landscape. A consistent finding across multiple studies: the highest-risk points in automated workflows are **human-automation interaction points** — particularly the final manual review step — not the automated systems themselves. Automation bias, skill degradation, and inability to detect mid-level errors are the dominant risks.

## Key Facts / Claims

- **De Kerf et al. 2025** (8-centre European FMEA, *Physics and Imaging in Radiation Oncology*): assessed fully automated workflow (FAW) across 8 European RT centres using TG-100 FMEA [fmea-ai-automated-workflow]
- Highest-risk workflow steps: **Manual Review** (R*=0.46) > **Auto-segmentation** (R*=0.44) > Auto-planning (R*=0.25) > Simulation (R*=0.25) > Orchestrator (R*=0.07) [fmea-ai-automated-workflow]
- Key finding: "Points where people interact with the FAW were considered higher risk than lack of trust in the FAW itself" [fmea-ai-automated-workflow]
- **Automation bias**: reviewers anchored by automated outputs; mid-level errors (subtle, not large) are the hardest to detect [fmea-ai-automated-workflow]
- **Skill degradation**: staff lose expertise to detect and correct automated errors as manual engagement decreases [fmea-ai-automated-workflow]
- Primary risk causes: AI model generalizability (out-of-distribution patients); human error during patient preparation; protocol deviations; software errors (lowest concern) [fmea-ai-automated-workflow]
- **RPA FMEA (USA, 2022):** Integrating automated QA tools within the workflow decreased both maximum and mean RPN scores vs. manual-only workflows [fmea-ai-automated-workflow]
- AI-assisted contouring reduced intra- and inter-observer variability in prostate RT but requires structured QA to mitigate automation bias [fmea-ai-automated-workflow]
- Recommended mitigations: educational programs on FAW boundaries; automated QA systems monitoring workflow appropriateness; decision-support tools for reviewers; contingency procedures [fmea-ai-automated-workflow]
- Technical automation capability exists; clinical implementation barriers are predominantly **organizational and educational**, not technological [fmea-ai-automated-workflow]

## Connections

- [[fmea-radiotherapy]] — foundational FMEA methodology; AI FMEA extends the TG-100 framework to automated tools
- [[fmea-advanced-modalities]] — advanced modalities (MR-linac, adaptive RT) increasingly use AI-based contouring
- [[tg100-aapm]] — TG-100 is the endorsed FMEA framework applied in all AI FMEA studies
- [[human-factors-rt-safety]] — automation bias and skill degradation are human factors risks; HFACS framework identifies the same risk categories
- [[rt-patient-safety-context-map]] — AI/automation risks are a key identified gap in the field's safety coverage

## Open Questions

- At what level of AI model performance does automated QA within the workflow become sufficient to replace current manual review?
- How should FMEA be updated when AI model versions change (e.g., model retraining)?
- What RPN thresholds and mitigation requirements apply specifically to AI-based tools vs. rule-based automation?
- How does skill degradation progress quantitatively — over what timeframe do staff lose the ability to detect AI errors?

## Raw Notes

- De Kerf 2025 multicentre FMEA: https://pmc.ncbi.nlm.nih.gov/articles/PMC12005333/
- RPA FMEA (*Practical Radiation Oncology* 2022): https://www.practicalradonc.org/article/S1879-8500(22)00008-X/fulltext
- AI contouring clinical validation (PMC 2023): https://pmc.ncbi.nlm.nih.gov/articles/PMC9955359/
- AI contouring automation bias (PMC 2025): https://pmc.ncbi.nlm.nih.gov/articles/PMC12715409/
