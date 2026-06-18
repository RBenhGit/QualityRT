---
name: query
description: Answer research questions by searching and synthesizing the compiled wiki in wiki/topics/ and wiki/index.md, with inline citations. Use this skill whenever the user asks a research question, types /query, says "what does the wiki say about X", "summarize what we know about Y", "compare X and Y", or asks for a synthesis of any topic covered in the wiki. Also trigger when the user asks follow-up questions during a research session.
---

Read `SCHEMA.md` before doing anything — it defines citation syntax and page conventions.

## What query does

Query treats the compiled wiki as your sole source of truth. You synthesize an answer from wiki pages, cite them inline, and flag what the wiki does not yet cover. Do NOT consult `raw/` files or the internet — if knowledge isn't in the wiki, that is a gap worth naming, not a reason to go off-script.

---

## Step 1 — Understand the question

Before searching, take a moment to parse the question:
- What is the user actually asking? (concept explanation, comparison, evidence summary, open question?)
- What keywords and synonyms should you look for? (e.g., "risk analysis" → FMEA, TG-100, RPN, fault tree)
- What would a complete answer look like? (single fact, comparative table, narrative synthesis, action recommendation?)

---

## Step 2 — Locate relevant pages

1. Read `wiki/index.md` fully — it is the master catalog.
2. Identify the **3–10 most relevant pages** based on:
   - Direct topic match (page title / slug)
   - Synthesis pages that may already connect the dots
   - Pages whose Summary in the index mentions key terms
3. Note any pages those candidates link to via `[[connections]]` that might also be relevant — load those too (one transitive hop is usually enough).

---

## Step 3 — Read and synthesize

1. Read each selected page in full.
2. Build your answer. Structure it clearly:
   - **Start with a direct answer** to the question, even if nuanced.
   - **Support with evidence** — use inline citations in `[page-slug]` format after every factual claim.
   - **Use structure** (headings, tables, or bullet lists) when comparing multiple items or presenting a sequence.
   - **Surface tensions and gaps** — if two pages contradict each other, name the contradiction rather than picking a side. If the wiki has limited coverage, say so honestly.
3. Keep the answer as long as it needs to be, and no longer.

---

## Step 4 — End-of-answer metadata

After your synthesized answer, always include:

**Sources used:**
List each page you read, as `[page-slug](wiki/topics/page-slug.md)`.

**Confidence:** high | medium | low
- High: the wiki has multiple rich pages directly addressing the question.
- Medium: the wiki has relevant content but coverage is partial or indirect.
- Low: the wiki touches the topic only tangentially; answer is extrapolated.

**Gaps:**
List topics the question touches that the wiki does not yet cover well. These are candidates for future ingest.

---

## Step 5 — Offer to save as synthesis page

If your answer is non-trivial, novel, and reusable (i.e., it synthesizes across ≥3 pages and would be useful to revisit), ask the user:

> "This answer synthesizes across several pages. Would you like me to save it as a new wiki synthesis page at `wiki/topics/<suggested-slug>.md`? It will be cross-linked back to the source pages."

If the user says yes:
- Create the page using the standard SCHEMA.md template, Type: Synthesis.
- Add `[[source-page]]` connections for every page you drew from.
- Update `wiki/index.md` and append a brief note to `wiki/log.md`.

If the user says no, discard — the answer was ephemeral.

---

## Rules

- **Only use the wiki.** If the answer isn't there, say so and list it as a Gap.
- **Every factual claim must have a `[page-slug]` citation.**
- **Never guess** about facts not in the wiki — flag them as Open Questions or Gaps.
- If the user asks you to speculate or hypothesize beyond wiki content, you may do so clearly labeled as such (e.g., "Beyond what the wiki covers, one might hypothesize..."), but keep it brief and separated from cited content.
