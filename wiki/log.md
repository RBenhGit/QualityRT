# Activity Log

Append-only chronological record of all wiki operations.

---

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
