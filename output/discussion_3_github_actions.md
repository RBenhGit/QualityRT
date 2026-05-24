# Discussion 3: GitHub Actions "Actions Commands" Integration
**Date:** 2026-05-24
**Topic:** Architecting and designing manually-triggerable GitHub Actions workflows for ingest, query, and lint.

---

## 1. Context & Rationale
The user requested adding `ingest`, `query`, and `lint` as "actions commands" in the project.
- **Interpretation:** In GitHub repositories, "Actions Commands" refers to **GitHub Actions workflows** using `workflow_dispatch` manual triggers.
- **Benefit:** This allows you or anyone collaborating on the project to perform operations (like querying the wiki or compiling raw files) directly from the GitHub browser interface under the "Actions" tab, without running anything locally!
- **Core Requirements:**
  1. A backend automation script (`workflow.py`) that executes the actual logic.
  2. GitHub Actions configuration files (`.github/workflows/*.yml`) wrapping the script commands.
  3. Continuous Deployment credentials/mechanisms (e.g. standard `${{ secrets.GITHUB_TOKEN }}` for pushing updates back to the repo, and a `GEMINI_API_KEY` secret for LLM capabilities).

---

## 2. System Architecture Design

### A. Automatic Commit & Push for Ingest
When a manual `/ingest` action runs on GitHub:
- The runner scans `raw/` for new files.
- It compiles them into markdown files under `wiki/topics/`.
- It updates the index and logs.
- The action uses a Git author to commit these updates and push them back to the active branch automatically!

### B. Rich UI Output for Query & Lint
Since GitHub Actions run in a background terminal, reading raw logs is inconvenient.
- We will leverage **GitHub Actions Step Summaries** (`$GITHUB_STEP_SUMMARY`).
- When `/query` or `/lint` runs, `workflow.py` will format the output in beautiful Markdown (collapsible sections, tables, bold citations).
- The workflow will pipe this directly into the summary, showing the result as a premium-styled summary page directly in your browser.

### C. Mock Mode Fallback
To ensure that the GitHub Action works out-of-the-box even before you configure a secret `GEMINI_API_KEY`:
- If `GEMINI_API_KEY` is not present in the environment, the python engine enters **Mock Mode**.
- In Ingest: It creates placeholder files derived from filenames.
- In Query: It answers using keyword search on `wiki/topics` and prints a structured static summary.
- In Lint: It executes full local link validation and orphan detection (which are deterministic and don't need an LLM anyway!).

---

## 3. Decisions Made
- Build `.github/workflows/ingest.yml`, `.github/workflows/query.yml`, and `.github/workflows/lint.yml` as independent manual workflow files.
- Set up automated Git commits on Ingest to keep the wiki synchronized automatically.
- Deliver results through the premium GitHub Step Summary interface.

---

## 4. Next Steps
- Implement `workflow.py` CLI script.
- Create `.github/workflows/` directory and add the three workflow YAML files.
- Document GitHub Actions in `README.md` and `SCHEMA.md`.
- Test and push!
