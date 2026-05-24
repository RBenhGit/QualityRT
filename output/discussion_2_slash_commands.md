# Discussion 2: Modern Slash Commands & Skills Integration
**Date:** 2026-05-24
**Topic:** Implementing and documenting ingest, query, and lint as project-scoped slash commands and custom skills.

---

## 1. Context & Architecture Analysis
The user requested adding `/ingest`, `/query`, and `/lint` as slash commands in the project. We performed research into the standard configuration of slash commands for **Claude Code** and discovered:
- **Legacy Approach:** Files placed under `.claude/commands/<command-name>.md` are automatically registered as slash commands in legacy setups.
- **Modern Skill-Based Approach (Recommended):** Custom skills are placed under `.claude/skills/<skill-name>/SKILL.md`. This directory layout supports YAML frontmatter, specifying description, metadata, and allowed tools, making it much more robust and trigger-coherent for advanced agentic workflows.

To ensure 100% compatibility across both legacy and modern environments, we implemented both structures in the project.

## 2. Changes Made
We created the modern skill directories and files, and updated the documentation:

1. **Created Ingest Skill:** [SKILL.md](file:///d:/cowork/QualityRT/.claude/skills/ingest/SKILL.md)
   - Setup YAML frontmatter detailing triggers and permissions.
   - Incorporated full compilation and index tracking procedures.
2. **Created Query Skill:** [SKILL.md](file:///d:/cowork/QualityRT/.claude/skills/query/SKILL.md)
   - Setup YAML frontmatter detailing how to search the index, synthesise answers, and cite sources.
3. **Created Lint Skill:** [SKILL.md](file:///d:/cowork/QualityRT/.claude/skills/lint/SKILL.md)
   - Setup YAML frontmatter detailing checking for missing links, orphans, stale stubs, and index drift.
4. **Updated `README.md`:** Documented the new `.claude/skills/` folder alongside `.claude/commands/`.
5. **Updated `SCHEMA.md`:** Added a dedicated section detailing how slash commands and custom skills are configured and processed.

## 3. Decisions Made
- Support **both** legacy `.claude/commands/` and recommended `.claude/skills/` directories for maximum developer compatibility.
- Ensure YAML frontmatter exists on skills to permit intelligent tool invocation when running commands.

## 4. Next Steps
- Commit the new slash command skills to git and push them to the repository.
- Await user approval on testing or further scripts!
