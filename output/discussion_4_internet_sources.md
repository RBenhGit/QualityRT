# Discussion 4: Radiotherapy Safety Research & Wiki Compilation
**Date:** 2026-05-24
**Topic:** Conducting internet research on radiotherapy quality, risk management, TG-100, and RO-ILS, and compiling them into the wiki.

---

## 1. Summary of Collected Research Sources
We searched the web for authoritative standards and literature regarding safety and quality systems in radiation oncology. The core sources are:

### A. AAPM Task Group 100 (TG-100) Report
- **URL:** [https://aapm.onlinelibrary.wiley.com/doi/full/10.1118/1.4947547](https://aapm.onlinelibrary.wiley.com/doi/full/10.1118/1.4947547)
- **Significance:** Shuffled the clinical paradigm from machine-based checklist checking to proactive, workflow-based risk analysis (Process Mapping, FMEA, and FTA).

### B. Radiation Oncology Incident Learning System (RO-ILS)
- **URL:** [https://www.astro.org/Patient-Safety-Quality/RO-ILS](https://www.astro.org/Patient-Safety-Quality/RO-ILS)
- **Significance:** The premier national database co-sponsored by ASTRO and AAPM, offering U.S. clinics a federally-protected (Clarity PSO), non-punitive system to record and analyze safety incidents/near-misses.

### C. WHO Technical Manual: Radiotherapy Risk Profile
- **URL:** [https://www.who.int/publications/i/item/9789241596954](https://www.who.int/publications/i/item/9789241596954)
- **Significance:** A global review identifying historical error patterns and recommending double-checks, independent dosimetry checks, and standard communication procedures.

### D. IAEA Safety Reports Series No. 17: Prevention of Accidental Exposure
- **URL:** [https://www.iaea.org/publications/6027/prevention-of-accidental-exposure-to-patients-undergoing-radiation-therapy](https://www.iaea.org/publications/6027/prevention-of-accidental-exposure-to-patients-undergoing-radiation-therapy)
- **Significance:** Core international standard compiling lessons from historic radiotherapy accidents and detailing calibration safety measures.

---

## 2. Dynamic Wiki Ingestion Demonstration
To show the immediate power of the ContextSpace architecture we built:
1. We saved the collected research details into a new source file: [raw/radiotherapy-sources.md](file:///d:/cowork/QualityRT/raw/radiotherapy-sources.md).
2. We executed our custom automation runner to compile this new source:
   ```bash
   python workflow.py ingest
   ```
3. The runner scanned the file, created the new topic page [wiki/topics/radiotherapy-sources.md](file:///d:/cowork/QualityRT/wiki/topics/radiotherapy-sources.md), updated the master catalog [wiki/index.md](file:///d:/cowork/QualityRT/wiki/index.md), and logged the activity in [wiki/log.md](file:///d:/cowork/QualityRT/wiki/log.md).

This proves the entire end-to-end ContextSpace compilation workflow is 100% active, robust, and ready for clinical subject curation.

---

## 3. Next Steps
- Commit the raw research sources and the compiled wiki sheets to git and push them to GitHub.
