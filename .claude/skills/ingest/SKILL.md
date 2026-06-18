---
name: ingest
description: Scan raw/ for new source files and compile them into structured, cross-linked wiki/topics/ pages following SCHEMA.md. Use this skill whenever the user says /ingest, "add to the wiki", "process new sources", "compile raw files", or drops files into raw/ and wants them indexed. Also trigger when the user asks to update the wiki from new papers, notes, or web clips.
---

Read `SCHEMA.md` before doing anything — it governs every naming, linking, and formatting decision.

## What ingest does

Ingest is a **compiler step**: raw source files are immutable inputs; wiki/topics/ pages are the living compiled output. Your job is to extract the knowledge from each new source and merge it faithfully into the wiki — never inventing facts, never deleting existing content.

---

## Step 1 — Identify new sources

1. Read `wiki/log.md` and note every source slug already listed.
2. List all files in `raw/` (including any subdirectories).
3. Cross-reference: which files are **not yet** in the log?
4. If none are new, report "Nothing new to ingest — all raw/ files are already in the log." and stop.
5. Otherwise, collect the list of new files. Process them one at a time in the steps below.

---

## Step 2 — Process each new source file

For each new file:

### 2a. Read and understand the source
- Read the full file.
- Identify the **source slug**: derive it from the filename (lowercase, hyphens, no dates unless part of the canonical identifier). E.g., `tg100-aapm-2016` from `tg100-aapm.md`.
- Identify all significant **topics**, **entities**, **methods**, and **claims** in the source.
- Flag any facts that **contradict** what you already know from the wiki — do not silently overwrite; note the conflict in Open Questions on both pages.

### 2b. For each topic/entity identified

Check `wiki/index.md` to see if a page already exists:

**If the page exists:**
- Open the page.
- Under **Key Facts / Claims**, add new discrete facts as bullet points with `[source-slug]` citations. Do not duplicate facts already present.
- Under **Connections**, add new `[[page-slug]] — one sentence` entries for any new relationships the source reveals.
- Under **Open Questions**, add questions the new source raises or partially answers.
- Under **Raw Notes**, add the source URL or reference if not already there.
- Upgrade **Status** if warranted:
  - stub → developing: if you add ≥3 substantive facts
  - developing → mature: if the page now has a rich Summary, ≥8 cited facts, and ≥5 cross-links
- Update **Last updated** to today's date.
- Update **Sources** in the frontmatter to include the new source slug.

**If the page does not exist:**
- Determine the slug: lowercase, hyphenated, specific (e.g., `adaptive-rt-qa` not `new-topic`).
- Create `wiki/topics/<slug>.md` using this exact template:

```markdown
# <Title>

**Type:** Topic | Entity | Synthesis
**Status:** stub | developing | mature
**Last updated:** YYYY-MM-DD
**Sources:** [source-slug]

## Summary
One paragraph. The most important thing to know about this topic.

## Key Facts / Claims
- Bullet list of discrete, citable facts [source-slug]

## Connections
- [[related-topic]] — one sentence on how they relate

## Open Questions
- Questions the current sources leave unanswered

## Raw Notes
Overflow space for unstructured observations, URLs, or notes not yet synthesized.
```

- Set Status to `stub` if you can write only a brief summary; `developing` if you have ≥3 cited facts and ≥2 connections.

### 2c. Back-link sweep
After creating or updating a page, search every other wiki page in `wiki/topics/` for any mention of the new page's topic (by name or concept). Add a `[[new-slug]]` Connections entry on any page that discusses the topic but doesn't yet link to it. This keeps the graph complete.

---

## Step 3 — Update wiki/index.md

- Add a new row for each **newly created** page in the table:
  `| [slug](topics/slug.md) | Type | Status | First sentence of Summary... |`
- For updated pages, update the Status column if it changed.
- Update the `*Last updated:*` line to today's date.
- Update the `*Total pages:*` count.

---

## Step 4 — Append to wiki/log.md

Add an entry at the **top** of the log (below the header) in this format:

```markdown
## YYYY-MM-DD — Ingestion run

**Operation:** Source files processed
**Sources processed:** [slug-1], [slug-2], ...
**Pages created:** `page-a`, `page-b`
**Pages updated:** `page-c` (what changed), `page-d` (what changed)
**Notes:** Any notable observations (conflicts found, status upgrades, etc.)
```

---

## Step 5 — Final report

Print a summary to the user:

```
Ingest complete.
- Sources processed: N
- Pages created: M (list them)
- Pages updated: K (list them)
- Status upgrades: (e.g., fmea-radiotherapy: stub → developing)
- Conflicts flagged: (if any)
```

---

## Rules you must never break

- **Never modify files in `raw/`** — they are immutable source of truth.
- **Never invent facts** not present in the source. Gaps belong in Open Questions.
- **Never delete existing wiki content** — only add, enrich, or flag for review.
- **Always cite** every Key Fact with `[source-slug]`.
- **Always use `[[slug]]` syntax** for internal links — never plain URLs for cross-wiki references.
- If a source is a web article you are fetching (not a local file), note the URL in Raw Notes on each page it informs.
