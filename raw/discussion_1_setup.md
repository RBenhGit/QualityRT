# Discussion 1: Initial Setup & Schema Analysis
**Date:** 2026-05-24
**Topic:** Initial setup of the cloned repository and design planning for the workflow.

---

## 1. Repository Cloned
The repository `https://github.com/RBenhGit/QualityRT.git` was successfully cloned into the workspace at `d:\cowork\QualityRT`. 

## 2. Directory Structure & Key Components
We analyzed the repository structure and found it matches Andrej Karpathy's **LLM Wiki / ContextSpace** pattern:
- **`raw/`**: The directory where raw research articles, notes, PDFs, or text dumps are placed. These files are treated as immutable source code.
- **`wiki/`**: The living, compiled knowledge base.
  - `wiki/index.md`: A master catalog of all wiki pages.
  - `wiki/log.md`: An append-only activity log tracking ingests.
  - `wiki/topics/`: Individual topic markdown files (e.g. `llm-wiki-pattern.md`).
- **`.claude/commands/`**: Slash command definitions (`ingest.md`, `query.md`, `lint.md`) containing prompt-like instructions for an LLM agent to execute the operations.

## 3. Detailed Operation Specifications

### A. Ingest Operation (`ingest`)
- **Purpose:** Compile new files from `raw/` into structured topic pages in `wiki/topics/`.
- **Steps:**
  1. Compare `raw/` files with the processed logs in `wiki/log.md` to identify new files.
  2. Parse new sources to identify significant topics, entities, methods, and claims.
  3. Create new files in `wiki/topics/<slug>.md` or update existing ones.
  4. Perform back-linking (scanning other pages for mentions of the new topic).
  5. Update the master catalog in `wiki/index.md`.
  6. Add a log entry in `wiki/log.md`.

### B. Query Operation (`query`)
- **Purpose:** Ask research questions against the compiled wiki.
- **Steps:**
  1. Read the catalog (`wiki/index.md`) to select the top 3-10 most relevant pages.
  2. Load the full content of those pages (and transitive links if necessary).
  3. Synthesize a cited, structured answer with inline citations in `[page-slug]` format.
  4. Offer to save the synthesis as a new page under `wiki/topics/` if it adds long-term value.

### C. Lint Operation (`lint`)
- **Purpose:** Perform health checks on the wiki's structure and consistency.
- **Checks:**
  1. **Broken links:** References to `[[page-slug]]` where the target file doesn't exist.
  2. **Orphan pages:** Pages with zero incoming links.
  3. **Contradictions:** Mutually conflicting claims across different pages.
  4. **Stale stubs:** Pages with `Status: stub` that haven't been updated in over 60 days.
  5. **Missing summaries:** Pages with empty or extremely brief summary sections.
  6. **Index drift:** Discrepancy between files in `wiki/topics/` and the table in `wiki/index.md`.
  7. **Uncited facts:** Bullet points in the Key Facts section lacking source citations.

---

## 4. Next Steps
We have presented an **Implementation Plan** to the user. Once the plan is approved, we will:
1. Initialize the `output/` folder inside the workspace.
2. Implement the chosen workflow automation (such as a CLI script `workflow.py`).
3. Set up environment configurations (`.env`, `requirements.txt`).
4. Validate the workflow using mock and real ingestion/query tasks.
