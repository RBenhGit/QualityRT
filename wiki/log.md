# Activity Log

Append-only chronological record of all wiki operations.

---

## 2026-07-11 — Factual correction + deck spec produced

**Operation:** Correction and output (not an ingest)
**Correction:** The 1990 Spanish radiotherapy accident was mislabeled **"Salamanca"** in `rt-accidents-aviation-lessons`. The source decks label it only "ספרד/Spain (1990)"; the actual site was **Zaragoza** (Hospital Clínico, Sagittaire accelerator). Corrected the heading, facts (engineers repaired a fault → no independent physicist recheck + wrong console display → 36 MeV instead of 6 MeV → of 27 patients ≥15 died), connections, open question, and source note. (Historical mentions in earlier log entries below left as-is per append-only.)
**Output produced:** `output/safety_shield_deck_spec.md` — a full 18-slide NotebookLM/Gamma production spec for the "מעטפת ההגנה" talk (per-slide content + visual direction + speaker notes), grounded in `Incident reporting.xlsx`/discussion_7 and `safety_culture_traits_hebrew.html`; learning-cycle slide directed to replicate the department's existing ∞ diagram.
**Notes:** No wiki topic pages created; this documents a factual fix and a session deliverable.

---

## 2026-07-11 — Ingestion run (Safety Shield deck, "with traits" version)

**Operation:** Source file processed
**Sources processed:** [rt-safety-shield-traits-pptx] (`raw/Radiotherapy_Safety_Shield_with_traits.pptx`)
**File format note:** Entirely image-based PPTX (15 slides, all PNG, 1:1 slide-to-image mapping); extracted via ZIP/XML, slides read visually. Hebrew-language departmental presentation — a later/expanded version of the same deck as [rt-safety-shield-pptx] (`raw/Radiotherapy_Safety_Shield_(6).pptx`, ingested 2026-06-26), same title ("מעטפת ההגנה"), but with additional and re-ordered content.
**Pages created:** 0
**Pages updated (5):**
- `human-factors-rt-safety` — added the 5-role "critical treatment chain" concept (slide 2); added a 36-event root-cause/stage-of-occurrence breakdown for the existing 2015–2017 local dataset (slide 9); refined the hierarchy-of-effectiveness fact with an explicit 6-tier pyramid naming personal vigilance as its own base tier (slide 5); flagged a Swiss-Cheese 4-layer *labeling* discrepancy between the two deck versions as an Open Question (not reconciled).
- `fmea-radiotherapy` — added the "Clinical Safety Shield" 3-step FMEA workflow, explicitly naming STPA (System-Theoretic Process Analysis) as a complementary technique (slide 10); added the frontline-staff-not-managers quality-champion-team rationale; new [[human-factors-rt-safety]] connection.
- `just-culture-radiotherapy` — added a new verbatim quote ("we fix systems, not people"), the Blame-Culture-past-vs-Just-Culture-today elaboration, and the "reporting is an act of clinical responsibility" reframing (slides 6, 11).
- `incident-learning-systems-international` — refined the ILS Learning Cycle model with the specific named stations on each loop (slide 8); added the new reporting form's anonymity feature as a specific mechanism behind the reporting-culture shift (slide 7).
- `rt-accidents-aviation-lessons` — flagged a contradiction: this deck states the Salamanca 1990 accident killed "at least 15" of 27 patients, vs. "at least 17" in the original deck; recorded as an unresolved Open Question rather than silently picking one figure; added the deck's "overload, communication failure, no double-checks" cross-case Insight Bar note.
- `radiation-safety-culture-healthcare` — added the deck as a corroborating source (slides 12–15 independently recap the same IAEA 10 Safety Culture Traits already documented on this page); no new facts, no content change.
**Notes:** Slides 12–15 duplicate the already-ingested IAEA Radiation Safety Culture Trait Talks Handbook content verbatim — treated as source corroboration, not new information, per schema's "no invented facts" rule. Two internal contradictions between this deck and its earlier sibling version ([rt-safety-shield-pptx]) were found and flagged rather than resolved: (1) Salamanca 1990 death toll (15 vs 17), (2) Swiss Cheese 4-layer naming/order. `wiki/index.md` Last-updated bumped to 2026-07-11; no new pages, so Total pages remains 28.

---

## 2026-07-08 — Lint pass (full 7-check audit + fixes)

**Operation:** Lint and fix, all 27 topic pages
**Issues found:** 4 (contradictions ×2, citation-style/content-quality notes ×2). Broken links 0, orphans 0, stale stubs 0, thin summaries 0, index drift 0, hard uncited-fact failures 0.
**Issues fixed:** 4
- Contradiction: `incident-learning-systems-international.md` gave two different expansions of the SAFRON acronym ("Safety in Radiation Oncology" vs. "Safety Reporting and Learning System for Radiotherapy"). Corrected the unsourced first mention to match the Pawlicki-2017-sourced authoritative expansion, with an inline pointer to the source citation.
- Contradiction: `rt-patient-safety-context-map.md`'s Foundational Literature Timeline table stated "2010 | RO-ILS launched," conflicting with `ro-ils.md`'s statement that RO-ILS was only initiated (as a concept) in 2010 and actually launched June 19, 2014. Reworded the timeline row to "RO-ILS initiated (ASTRO/AAPM 'Call to Action')" with a note pointing to the true 2014 launch date and a [[ro-ils]] cross-link.
- Citation-style: `rt-patient-safety-context-map-hebrew.md` had two taxonomy sections (treatment chain, QA suite) citing only at the section-header level rather than per-bullet like the rest of the wiki. Added per-item `[tg100-aapm-2016]` / `[aapm-tg-suite-linac-qa]` citations to every list item in both sections.
- Content quality: `discussion-1-setup.md`'s Key Facts contained verbatim markdown headings from the source material ("# Discussion 1: Initial Setup...", "## 2. Directory Structure...") instead of discrete prose facts. Rewrote as 5 substantive cited facts drawn directly from the existing raw source (repo clone details, directory structure, the three operation specs, agreed next steps) — no new information invented.
**Status upgrades:** `discussion-1-setup`: stub → developing (now has 5 substantive cited facts, meeting the schema's upgrade threshold)
**Issues deferred:** 0
**Notes:** `wiki/index.md` updated to reflect the `discussion-1-setup` status change and summary; `rt-patient-safety-context-map-hebrew.md` Last-updated bumped to 2026-07-08.

---

## 2026-07-08 — Source enrichment: quarterly + full taxonomy tables (departmental incident-reporting dataset)

**Operation:** User requested (via /query) a quarterly report-count table and the full 41-keyword taxonomy table; wiki page previously held only yearly totals and the top-9 keywords, so re-consulted `raw/Incident reporting.xlsx` directly (with user confirmation) to extract the missing detail.
**Pages updated:** `departmental-incident-reporting-dataset-il` — added a full quarterly report-count table (2018-Q1 to 2026-Q2, computed from column C "מועד דיווח"; noted 197/1,014 rows lack a report date and are excluded), and the complete 41-row keyword taxonomy table with English glosses and recomputed percentages (previously only top-9 keywords were listed); added one new Open Question about the report-date coverage gap.
**Correction 1 (same day, user follow-up):** User clarified that the serial number ("מספר סידורי") is pre-assigned ahead of and independent of actual reporting — it reserves slots for future incidents — so only the 817 rows with a populated report date should be counted as "reports." Reworded Summary, "Scope and volume," and Raw Notes to make 817 (not 1,014) the reporting denominator; replaced the previously-cited annual totals (17/8/23/60/68/52/90/128/90/115/129 for 2015–2025, sourced from the workbook's own "results new" summary tab) with annual totals recomputed directly from the report-date column (62/93/55/100/129/90/115/130/43 for 2018–2026); flagged the unresolved discrepancy between the two annual series as a new Open Question; clarified that all other per-field breakdowns (stage, cause, taxonomy, etc.) still legitimately use the full 1,014-row denominator since those fields are populated independent of report-date status.
**Correction 2 (same day, second user follow-up):** User further clarified that a date of harm ("מועד הפגיעה") alone — not only a report date — is sufficient evidence that a report occurred; only rows with *neither* date populated should be excluded. Widened the reporting definition from "report date populated" (817 rows) to "harm date OR report date populated" (871 rows, 143 excluded). Recomputed all annual totals (now 17/8/24/66/93/55/100/130/90/115/130/43 for 2015–2026, using report date when present and falling back to harm date otherwise) and the full quarterly table (now spanning 2015-Q1–2026-Q2, restoring 54 reports from 2015–2017 that the report-date-only definition had excluded). Noted that 871 matches the pre-existing severity-score sample sizes (n=870/871) already on the page — a useful internal consistency check. Updated Open Questions and Raw Notes accordingly.
**Correction 3 (same day, third user follow-up):** User provided key operational context: reports dated before October 2017 (38 of the 871) were entered **retrospectively as a one-time backfill for control/audit purposes**, not logged contemporaneously; the ILS became part of **routine, ongoing departmental operation only from October 2017 onward** (833 of 871 reports). Updated Summary and Scope-and-volume to state this distinction explicitly; marked pre-Oct-2017 quarters (2015-Q1–2017-Q3) with † in the quarterly table and noted they are not comparable to the routine-operation trend; reworded the Nyflot "rising volume = healthier culture" claim to apply only to the routine-operation period; updated the `radiation-safety-culture-healthcare` connection to exclude the retrospective backfill from the Trait-9 safety-culture signal; resolved the "what triggered the 2018 rise" Open Question (answer: the Oct-2017 transition from backfill to routine operation) and added a new Open Question about the backfill's selection methodology.
**Correction 4 (same day, fourth user follow-up — answers to 5 prior Open Questions):** (1) User instructed that annual-series discrepancies under 1% should not be treated as gaps; recomputed percentages and found most years match within <1% (exact for 2015/2016/2023/2024), with only 2018 (+9%), 2021 (+10%), and 2019 (+27%) remaining as genuine, unexplained discrepancies — reworded from a blanket "unresolved discrepancy" framing to this more precise breakdown. (2) User confirmed the 143 reserved serial numbers have **no report filed against them at all** (not undated existing reports) — resolved that Open Question outright. (3) User confirmed the ILS **did not exist / was not in use** before October 2017 (not a "backfill selected for audit purposes" as the page had inferred) — corrected the Summary, Scope-and-volume, and Raw Notes wording accordingly, and removed the now-invalid "what were the backfill selection criteria" Open Question. (4) User confirmed all documented reports (harm-date-or-report-date rule) should be included — no filtering change needed, existing approach validated. (5) User confirmed there was no centralized/administrative batch reporting behind the Q1 peaks, and raised an unconfirmed hypothesis that earlier periods may have coincided with staff awareness-training campaigns — updated the peak-quarters note accordingly and flagged the hypothesis as unconfirmed. Net result: three Open Questions resolved/removed, one reworded with more precise figures.
**Notes:** No contradictions with previously ingested content — new tables are strict elaborations of facts already summarized at a higher level (yearly totals, top-9 keywords). Report delivered to user as a standalone Hebrew statistics report (not saved as separate wiki page — data now lives directly on the source topic page).

---

## 2026-07-08 — Ingestion run (departmental incident-reporting dataset)

**Operation:** Source files processed
**Sources processed:** [incident-reporting-xlsx-il] (`raw/Incident reporting.xlsx`)
**Pages created:** `departmental-incident-reporting-dataset-il`
**Pages updated:** `incident-learning-systems-international` (added primary-source departmental dataset fact + connection; Sources list), `ro-ils` (connection), `human-factors-rt-safety` (connection), `rt-quality-management` (connection), `radiation-safety-culture-healthcare` (connection), `rt-patient-safety-context-map-hebrew` (connection, Hebrew)
**Notes:** First ingested *primary-source* safety dataset in the wiki (vs. secondary literature analyses) — a bilingual Hebrew/English Excel workbook containing 1,014 individually logged incident records (2004–2026) from a radiotherapy department, with 9 sheets: raw incident log, event-summary narratives, a 41-keyword free-text taxonomy (799 tagged mentions), a Hebrew/English parameter dictionary including full severity-scale definitions, cross-tabulated frequency results, monthly/yearly trend series with severity histograms, a Hebrew-to-English causal-factor taxonomy crosswalk (mapped explicitly onto RO-ILS/AAPM terminology), and a corrective-action task-management tracker. Extracted via `openpyxl` (data_only mode); no chart visualizations were reproduced (25 native Excel charts present but not individually re-rendered — flagged as an open question/future task). Field structure and dual severity scales independently converge on the AAPM/Ford 2012 consensus recommendations already documented in `incident-learning-systems-international`. Status set to `developing` (1 source, 6 connections, rich quantitative facts, but several open questions remain about provenance/context not present in the raw file).

---

## 2026-06-18 — Source enrichment: consensus on ILS systems (Ford et al. 2012, full text)

**Operation:** User requested full-text integration of `raw/Safety articles/consensus on ILS systems.pdf` into the ILS summary, with large weight.
**Source:** Ford EC et al., "Consensus recommendations for incident learning database structures in radiation oncology," *Med Phys* 39(12):7272–7290 (2012). Source slug: [ford-ils-consensus-2012] (previously cited from abstract; now fully ingested).
**Pages updated:** `incident-learning-systems-international.md` — major expansion of the ILS database structure section with: 14-item functional requirements table (Table I) with priority ranking, full EBRT/brachy process map phase listing with SB counts, complete dual severity scales with exact score descriptors, clinical action scale (A–D), full 6-category causal taxonomy with subcategories, three-level data element structure (Reporter/Analyst/Responder), operational/investigation timeline recommendations, CAST aviation analogy.
**Pages created:** 0

---

## 2026-06-26 — Ingestion run

**Operation:** Source file processed
**Sources processed:** [rt-safety-shield-pptx] (`raw/Radiotherapy_Safety_Shield_(6).pptx`)
**File format note:** Entirely image-based PPTX (11 slides, all PNG); extracted via ZIP/XML, slides read visually. Hebrew-language departmental presentation titled "מעטפת ההגנה: ניהול סיכונים ולמידה ארגונית בדיות רפיה" (The Safety Shield: Risk Management and Organizational Learning in Radiotherapy).

**Pages created (1):** `just-culture-radiotherapy` — three-component Just Culture framework (Blame / Just / No-Blame), ICAO SMS origin, prerequisites for ILS reporting.

**Pages updated (3):**
- `rt-accidents-aviation-lessons` — added Salamanca (Spain, 1990) accident (36MeV vs 6MeV energy confusion, 17 deaths, 27+ patients); enriched Glasgow/Lisa Norris case with dose specifics (55.56 Gy / 67% overdose); added `[[just-culture-radiotherapy]]` connection.
- `human-factors-rt-safety` — added "Clinical Safety Shield" named 4-layer framework (safety culture → procedures/QA → physics checks → clinical review/time-out); added local dept data (93% errors caught pre-patient, 2015–2017); added `[[just-culture-radiotherapy]]` connection.
- `incident-learning-systems-international` — added ILS Learning Cycle model (Knowledge Cycle ↔ Execution Cycle infinity loop); added local dept data (93% interception, structured taxonomy migration); added `[[just-culture-radiotherapy]]` connection.

**New key content from source:**
- Salamanca 1990 accident (energy confusion, not previously in wiki)
- Just Culture three-component model (now has dedicated page)
- 93% pre-patient error catch rate (Israeli RT dept, 2015–2017)
- ILS infinity loop model (Knowledge ↔ Execution cycles)
- Named "Clinical Safety Shield" framework integrating FMEA + Swiss Cheese + ILS + Just Culture

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
