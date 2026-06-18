---
name: lint
description: Run a full health check on the wiki — broken links, orphan pages, contradictions, stale stubs, index drift, uncited facts, and missing summaries. Use this skill whenever the user types /lint, "check the wiki", "health check", "find broken links", "audit the wiki", or asks to verify wiki consistency. Also offer to run lint after any large ingest batch.
---

Read `SCHEMA.md` before doing anything — it defines the conventions you are checking against.

## What lint does

Lint is a **read-only audit**. It reports every issue it finds, categorized and prioritized, then asks the user which issues to fix. Do NOT auto-fix anything without explicit user approval.

The goal is to keep the wiki internally consistent, well-linked, and free of stale or misleading content — so that query answers are reliable.

---

## The seven checks

Run all seven checks. Collect every finding before writing the report.

### Check 1 — Broken internal links
Scan every page in `wiki/topics/` for `[[slug]]` references. For each reference, verify that `wiki/topics/<slug>.md` exists. If it does not, record:
- The missing slug
- Every page that references it

### Check 2 — Orphan pages
For every page in `wiki/topics/`, check whether any other wiki page links to it via `[[slug]]`. If a page has **zero incoming links**, it is an orphan. Record it. (Exception: `index.md` does not count as an incoming link.)

### Check 3 — Contradictions
Read the Key Facts sections across all pages. Flag cases where two pages make **conflicting factual claims** about the same topic. Look especially for:
- Conflicting numbers (e.g., different RPN thresholds, different statistics)
- Conflicting definitions of the same method or term
- Claims that logically exclude each other

Record both pages and the specific conflicting claims.

### Check 4 — Stale stubs
Find every page where:
- `**Status:** stub` AND
- `**Last updated:**` is more than 60 days ago (relative to today)

These pages have been neglected and may need a source search or ingest.

### Check 5 — Missing or thin summaries
Find pages where the **Summary** section is:
- Empty (just a heading, no text), OR
- A single sentence of fewer than 20 words

These pages are not usable for query synthesis.

### Check 6 — Index drift
Compare `wiki/index.md` against the actual files in `wiki/topics/`:
- Pages in `wiki/topics/` but **not** in `wiki/index.md` → missing from index
- Rows in `wiki/index.md` that reference files that **don't exist** in `wiki/topics/` → dead index entries

### Check 7 — Uncited facts
Scan every **Key Facts / Claims** bullet on every page. Flag bullets that contain a factual claim (not just a structural note) but have **no `[source-slug]` citation**.

---

## Report format

```markdown
## Lint Report — YYYY-MM-DD

**Summary:** N total issues found across 7 checks.

---

### ✗ Broken Links (N)
- `[[missing-slug]]` — referenced in: [page-a.md], [page-b.md]

### ✗ Orphan Pages (N)
- [page.md] — no incoming links from any other wiki page

### ✗ Contradictions (N)
- [page-a.md] claims: "..."
  [page-b.md] claims: "..."
  → Recommend: review and reconcile; add Open Question to both pages

### ✗ Stale Stubs (N)
- [page.md] — Status: stub since YYYY-MM-DD (N days ago)

### ✗ Thin Summaries (N)
- [page.md] — Summary is empty / only N words

### ✗ Index Drift (N)
- Missing from index: `slug` (file exists at wiki/topics/slug.md)
- Dead index entry: `slug` (listed in index but file not found)

### ✗ Uncited Facts (N)
- [page.md] — bullet: "..." (no citation)

---

### Recommended Actions (prioritized)

1. **Fix broken links** — highest priority; broken links corrupt query results.
2. **Reconcile contradictions** — misleading content undermines trust.
3. **Fix index drift** — orphaned files and dead entries break navigation.
4. **Add citations to uncited facts** — improves query reliability.
5. **Enrich thin summaries** — query synthesis relies on Summary sections.
6. **Connect orphan pages** — improves discoverability and graph completeness.
7. **Triage stale stubs** — decide: enrich, merge, or mark deprecated.
```

---

## After reporting

Ask the user:

> "I found N issues. Which would you like me to fix? I can work through them by category (e.g., 'fix all broken links', 'reconcile contradictions') or item by item. I won't change anything until you say so."

When the user approves fixes, apply them carefully:
- Broken link → create a stub page or remove the dead reference (ask which)
- Contradiction → add an Open Question to both pages noting the conflict; do not silently pick a winner
- Index drift → update `wiki/index.md` to match reality
- Uncited fact → add `[source-unknown]` as a placeholder and note it in Open Questions (or remove the bullet if it cannot be sourced)
- Thin summary → expand from existing Key Facts on the page (don't invent)
- Orphan → add a `[[slug]]` connection on the most thematically related page

After applying fixes, append a brief entry to `wiki/log.md`:
```markdown
## YYYY-MM-DD — Lint pass

**Operation:** Lint and fix
**Issues found:** N (list categories)
**Issues fixed:** N (describe changes)
**Issues deferred:** N (user chose not to fix now)
```
