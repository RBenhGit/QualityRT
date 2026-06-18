# Activity Log

Append-only chronological record of all wiki operations.

---

## 2026-06-18 — Lint pass

**Operation:** Lint (read-only audit, all 7 checks) across 26 topic pages
**Issues found:** 1 borderline (broken links). Orphans 0, contradictions 0, stale stubs 0, thin summaries 0, index drift 0, uncited facts 0.
- Borderline broken link: `[[wiki-links]]` in `obsidian.md` — but it sits inside a backtick code span as an illustration of Obsidian's link syntax, not an intended cross-link.
**Issues fixed:** 0
**Issues deferred:** 1 — user chose option (a): leave the obsidian.md illustrative `[[wiki-links]]` as-is.
**Notes:** Post-ingest health is strong. All 26 pages have incoming links (no orphans); index count/date current (26, 2026-06-18); every Key Facts bullet carries a citation. Soft observation (not a lint failure): early RO-ILS uptake figures differ between Evans 2015 and Hoopes 2015 — different metrics/snapshots, both correctly cited. Low-priority quality note: `discussion-1-setup` Key Facts contain verbatim heading fragments rather than prose (left untouched).

---

## 2026-06-18 — Ingestion run (Safety articles batch — COMPLETE)

**Operation:** Full-fidelity ingest of the `raw/Safety articles/` batch (~43 academic PDFs + supplementary materials), per user's "All 45, full ingest" directive.

**Sources processed (28 substantive):**
- *ILS:* [ford-ils-consensus-2012], [nyflot-ils-metrics-2015], [kim-ils-tbi-impact-2017], [roils-first-year-2015], [rosis-cunningham-2010], [clark-5yr-incident-learning-2013], [pawlicki-ils-levels-2017], [evans-ro-ils-disciplines-2015]
- *Human factors:* [chera-normal-accident-theory-2015], [marks-swiss-cheese-2015], [mosaly-hfacs-reliability-2015], [gao-emergent-treatments-2015], [evans-causal-factors-2017], [gensheimer-planning-time-2016], [spraker-causal-taxonomy-2017], [walker-incident-factors-2015], [mazur-workload-2013], [mullen-nmri-reliability-2016], [thompson-hazard-detection-education-2017], [dominello-10yr-qa-2015]
- *Peer review:* [marks-peer-review-2013], [cox-contouring-rounds-2015], [matuszak-sbrt-peer-review-2016]
- *Safety culture:* [kusano-safety-culture-2015], [mazur-eventlearning-cqi-culture-2015], [chera-multifaceted-initiatives-2014]
- *Audit/accreditation:* [ritter-ebrt-audit-2012], [ford-spa-patterns-2015], [schechter-accreditation-survey-2017], [donaldson-quality-standards-2014]
- *Modality-specific:* [moran-imrt-safety-2011], [solberg-srs-sbrt-safety-2012], [schiff-dose-dissonance-2017]
- *Brachytherapy/HDR:* [richardson-nrc-brachy-2012], [thomadsen-hdr-guidance-2014]
- *Accidents/aviation:* [knoos-lessons-accidents-2017], [davies-aviation-safety-2017]
- *QM strategy:* [hayman-improving-safety-2011]

**Pages created (6):** `peer-review-radiotherapy`, `audit-accreditation-radiotherapy`, `advanced-modality-rt-safety`, `brachytherapy-hdr-safety`, `rt-accidents-aviation-lessons` (plus prior `radiation-safety-culture-healthcare` enrichment).
**Pages updated:** `incident-learning-systems-international` (consensus DB structure, NMRI metrics, TBI reliability, 5-yr outcomes, ROSIS→ROSEIS/SAFRON/EURATOM/NSIR-RT), `ro-ils` (first-year experience, AHRQ event classes, Evans rationale/accreditation role, PSQIA/Tinal v. Norton, protocol-deviation→survival), `human-factors-rt-safety` (Swiss Cheese, hierarchy of effectiveness, NAT, HFACS reliability, emergent-treatment & "no rushed treatment" data, causal taxonomy, workload), `radiation-safety-culture-healthcare` (Kusano/Mazur/Chera ILS-culture data), `rt-quality-management` (Hayman: sparse error data, hierarchy of effectiveness, Lean), `fmea-radiotherapy`, `tg100-aapm`, `iaea-safety-reports-17`, `regulatory-framework-rt-usa`, `rt-patient-safety-context-map` (back-links to all new pages).
**Status upgrades (developing→mature):** `peer-review-radiotherapy`, `audit-accreditation-radiotherapy`, `advanced-modality-rt-safety`, `brachytherapy-hdr-safety`, `rt-accidents-aviation-lessons`, `incident-learning-systems-international`, `human-factors-rt-safety`, `ro-ils`, `radiation-safety-culture-healthcare`.
**Duplicate flagged:** `enhancing quality through prepalnning peer review for.pdf` is byte-identical to `enhancing safety through preplanning peer review for SBRT.pdf` (both = Matuszak 2016, *Pract Radiat Oncol* 6:e39–e46). Ingested once as [matuszak-sbrt-peer-review-2016].
**Out of scope (logged, no page):** `Single-fraction-Radiotherapy-Should-be-the-Standard-of-Care...` (Price et al. 2017) — a palliative-fractionation/cost-effectiveness clinical argument (single- vs multi-fraction survival equivalence), not a patient-safety/QM topic; no safety angle invented per schema. The second letter on the same PDF (Karim et al., LMIC postgraduate training/JCIA accreditation) is likewise tangential.
**Supplementary-material files** (IMRT supp, audit-tool EBRT supp, 5-yr ILS supp): sparse appendix data already represented by their parent papers; HDR "supplemental material" PDF *was* the substantive Thomadsen 2014 text and was fully ingested.
**Notes:** Page-range PDF reads unavailable (pdftoppm missing) — full documents read. Log + wiki files updated incrementally throughout for durability across context limits.

---

## 2026-05-31 — Lint pass

**Operation:** Lint and fix
**Issues found:** 15 (broken links ×3, orphans ×2, contradictions ×1, thin summaries ×1, uncited facts ×8)
**Issues fixed:** 15
- Contradiction: updated RO-ILS count in `radiotherapy-sources` (">10,000" → "41,516 events from 781 facilities as of 2024")
- Broken links ×3: created stubs `claude-code`, `obsidian`, `rag-retrieval-augmented-generation`; added back-link from `llm-wiki-pattern`
- Uncited facts ×8: added `[karpathy-llm-wiki-2026]` to all Key Facts in `llm-wiki-pattern`
- Orphan `discussion-1-setup`: enriched summary, removed self-referencing connection, added incoming link from `llm-wiki-pattern`
- Orphan `rt-patient-safety-context-map-hebrew`: added incoming link from `rt-patient-safety-context-map`
- Thin summary: expanded `discussion-1-setup` summary from 13 to 30+ words
- Index updated: 18 → 21 pages
**Issues deferred:** 0

---

## 2026-05-31 — Ingestion run #2

**Operation:** Source files processed
**Sources processed:** [safety-culture-traits-summary] (safety-culture-traits-summary.md), [safety-culture-traits-hebrew] (safety_culture_traits_hebrew.html)
**Pages created:** (none — all content already compiled in `radiation-safety-culture-healthcare`)
**Pages updated:** `radiation-safety-culture-healthcare` (conflict flag added to Open Questions)
**Conflicts flagged:** `raw/safety_culture_traits_hebrew.html` contains old Trait 1 text ("לבטיחות הקרינה") — contradicts the corrected broader framing in `output/safety_culture_traits_hebrew.html` and in the wiki. Raw file is immutable; wiki and output/ hold the authoritative corrected version.

---

## 2026-05-31 — Ingestion run

**Operation:** Source files processed
**Sources processed:** [radiation-safety-culture-trait-talks] (radiation-safety-culture-trait-talks.pdf)
**Pages created:** `radiation-safety-culture-healthcare`
**Pages updated:** `human-factors-rt-safety` (added [[radiation-safety-culture-healthcare]] connection), `incident-learning-systems-international` (added [[radiation-safety-culture-healthcare]] connection), `tg100-aapm` (added [[radiation-safety-culture-healthcare]] connection), `rt-patient-safety-context-map` (added [[radiation-safety-culture-healthcare]] connection)
**Notes:** IAEA Radiation Safety Culture Trait Talks Handbook (PDF, 80pp). Created comprehensive page covering IAEA definition of safety culture, all 10 traits with sub-characteristics, incident examples from each trait, Bonn Call for Action context, and practical implementation guidance. Back-linked to 4 existing pages. New page directly addresses the organizational/behavioral layer underlying all other RT safety mechanisms in the wiki.

---

## 2026-05-26 — Ingestion run

**Operation:** Source files processed
**Sources processed:** [discussion-1-setup] (discussion_1_setup.md)
**Pages created:** `discussion-1-setup`
**Pages updated:** (none)
**Notes:** Automated ingestion run.


## 2026-05-25 — Ingestion run #3

**Operation:** Source files processed
**Sources processed:** [fmea-advanced-modalities-mr-linac], [incident-learning-systems-international], [fmea-ai-automated-workflow], [aapm-tg-suite-linac-qa], [regulatory-framework-rt-usa], [human-factors-rt-safety]
**Pages created:** `fmea-advanced-modalities`, `incident-learning-systems-international`, `fmea-ai-automated-workflow`, `aapm-tg-suite-linac-qa`, `regulatory-framework-rt-usa`, `human-factors-rt-safety`
**Pages updated:** `ro-ils` (10-year stats: 781 facilities, 41,516 events; added SAFRON/ROSIS links), `fmea-radiotherapy` (advanced modalities + AI FMEA + human factors links), `tg100-aapm` (TG suite + advanced modalities links), `rt-patient-safety-context-map` (6 open questions answered, 6 new cross-links added)
**Notes:** Sources fetched in response to open questions in rt-patient-safety-context-map. All 6 previously open questions now have dedicated wiki pages.

---

## 2026-05-25 — Query synthesis saved

**Operation:** Query → synthesis page
**Sources processed:** (none — query only)
**Pages created:** `rt-patient-safety-context-map`
**Pages updated:** `index.md`
**Notes:** Full context map of the RT patient safety and quality field synthesized from all 6 domain wiki pages.

---

## 2026-05-24 — Merge resolution

**Operation:** Merge conflict resolved between claude/fervent-mendel-fdJ3t and main
**Pages updated:** `fmea-radiotherapy` (kept main's richer version + added [[rt-quality-management]] link), `ro-ils` (kept main's richer version + added [[rt-quality-management]] link), `radiotherapy-sources` (kept main's Synthesis type + added [[rt-quality-management]] link), `index.md` (combined both: 8 total pages)
**Pages added from feature branch:** `rt-quality-management`
**Notes:** main had richer content from web-sourced ingest; feature branch contributed rt-quality-management synthesis page and back-links.

---

## 2026-05-24 — Ingestion run #2

**Operation:** Source files processed
**Sources processed:** [tg100-aapm-2016], [ro-ils-astro-aapm], [who-radiotherapy-risk-profile-2008], [iaea-safety-reports-17-2000], [fmea-jacmp-broggi-2013]
**Pages created:** `tg100-aapm`, `ro-ils`, `who-radiotherapy-risk-profile`, `iaea-safety-reports-17`, `fmea-radiotherapy`
**Pages updated:** `radiotherapy-sources` (upgraded from stub to Synthesis/developing; fully linked to all new pages)
**Notes:** All 5 raw source files fetched from web and ingested. Source URLs added to Raw Notes on each page. All pages cross-linked bidirectionally.

---

## 2026-05-24 — Re-ingestion run (full compilation)

**Operation:** Source files re-processed with full content extraction
**Sources processed:** [radiotherapy-sources] (radiotherapy-sources.md)
**Pages created:** `fmea-radiotherapy`, `ro-ils`, `rt-quality-management`
**Pages updated:** `radiotherapy-sources` (stub → developing, full content extracted), `index.md` (3 new rows)
**Notes:** Previous ingest on 2026-05-24 only captured 5 lines; this run fully compiled all 5 source sections into structured wiki pages.

---

## 2026-05-24 — Ingestion run #1

**Operation:** Source files processed
**Sources processed:** [radiotherapy-sources] (radiotherapy-sources.md)
**Pages created:** `radiotherapy-sources`
**Pages updated:** (none)
**Notes:** Automated ingestion run (incomplete — stub only).

---

## 2026-05-20 — Initial setup

**Operation:** Repository initialized
**Sources processed:** (none — schema and seed page created manually)
**Pages created:** `llm-wiki-pattern`
**Pages updated:** `index.md`
**Notes:** Bootstrapped from Karpathy's LLM Wiki pattern (April 2026 gist)
