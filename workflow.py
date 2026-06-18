#!/usr/bin/env python3
import os
import sys
import re
import json
import urllib.request
import urllib.error
from datetime import datetime

# Directory Constants
WORKSPACE_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_DIR = os.path.join(WORKSPACE_DIR, "raw")
WIKI_DIR = os.path.join(WORKSPACE_DIR, "wiki")
TOPICS_DIR = os.path.join(WIKI_DIR, "topics")
INDEX_PATH = os.path.join(WIKI_DIR, "index.md")
LOG_PATH = os.path.join(WIKI_DIR, "log.md")
TOPICS_DIR_URL = TOPICS_DIR.replace("\\", "/")

# Ensure base directories exist
os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(WIKI_DIR, exist_ok=True)
os.makedirs(TOPICS_DIR, exist_ok=True)

# Helper: Load API Key
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

def call_gemini(prompt: str) -> str:
    """Calls Gemini API using standard urllib to keep script zero-dependency."""
    if not GEMINI_API_KEY:
        return ""
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"
    
    payload = {
        "contents": [{
            "parts": [{
                "text": prompt
            }]
        }],
        "generationConfig": {
            "temperature": 0.2,
            "responseMimeType": "application/json" if "JSON" in prompt else "text/plain"
        }
    }
    
    req_data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=req_data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            res_data = response.read().decode("utf-8")
            res_json = json.loads(res_data)
            text = res_json["candidates"][0]["content"]["parts"][0]["text"]
            return text
    except urllib.error.HTTPError as e:
        print(f"Gemini API Error (HTTP {e.code}): {e.reason}", file=sys.stderr)
        try:
            err_body = e.read().decode("utf-8")
            print(f"Error Details: {err_body}", file=sys.stderr)
        except Exception:
            pass
        return ""
    except Exception as e:
        print(f"Unexpected API error: {str(e)}", file=sys.stderr)
        return ""

# ==================== LINT OPERATION ====================

def run_lint():
    print("Running Wiki Lint Health Check...")
    
    # 1. Read all files in topics/
    topic_files = [f for f in os.listdir(TOPICS_DIR) if f.endswith(".md")]
    topic_slugs = {f[:-3] for f in topic_files}
    
    broken_links = []
    orphan_pages = set(topic_slugs)
    uncited_facts = []
    stale_stubs = []
    missing_summaries = []
    index_drift = []
    
    # Track which pages reference which slugs
    references = {}
    
    # Parse each page
    for t_file in topic_files:
        slug = t_file[:-3]
        file_path = os.path.join(TOPICS_DIR, t_file)
        
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Parse links: [[page-slug]]
        links = re.findall(r'\[\[([a-zA-Z0-9\-_]+)\]\]', content)
        for link in links:
            if link not in topic_slugs:
                broken_links.append((slug, link))
            if link in orphan_pages and link != slug:
                orphan_pages.remove(link)
                
        # Parse Status, Last updated, Summary, and Facts
        status_match = re.search(r'\*\*Status:\*\*\s*(stub|developing|mature)', content, re.IGNORECASE)
        date_match = re.search(r'\*\*Last updated:\*\*\s*(\d{4}-\d{2}-\d{2})', content)
        
        # Check for stale stubs
        if status_match and status_match.group(1).lower() == "stub" and date_match:
            try:
                updated_date = datetime.strptime(date_match.group(1), "%Y-%m-%d")
                delta_days = (datetime.now() - updated_date).days
                if delta_days > 60:
                    stale_stubs.append((slug, date_match.group(1), delta_days))
            except ValueError:
                pass
                
        # Check Summary length
        summary_match = re.search(r'## Summary\s*\n+([^#\n][^\n]*)', content)
        if not summary_match or len(summary_match.group(1).split()) < 15:
            missing_summaries.append(slug)
            
        # Parse Key Facts / Claims
        facts_section = re.search(r'## Key Facts / Claims\s*\n+((?:-\s*[^\n]+\n*)+)', content)
        if facts_section:
            bullets = re.findall(r'-\s*([^\n]+)', facts_section.group(1))
            for b in bullets:
                # Fact should contain a source slug citation like [source-slug]
                if not re.search(r'\[[a-zA-Z0-9\-_]+\]', b):
                    uncited_facts.append((slug, b))

    # Check index drift
    indexed_pages = set()
    if os.path.exists(INDEX_PATH):
        with open(INDEX_PATH, "r", encoding="utf-8") as f:
            index_content = f.read()
        # Find all topics/slug.md links in index.md
        index_links = re.findall(r'topics/([a-zA-Z0-9\-_]+)\.md', index_content)
        indexed_pages = set(index_links)
        
    for slug in topic_slugs:
        if slug not in indexed_pages:
            index_drift.append(f"Page '{slug}.md' exists in topics/ but is not listed in index.md")
    for slug in indexed_pages:
        if slug not in topic_slugs:
            index_drift.append(f"Page '{slug}' is listed in index.md but file 'topics/{slug}.md' does not exist")

    # Format Lint Report
    report = []
    report.append(f"# Lint Report — {datetime.now().strftime('%Y-%m-%d')}\n")
    
    # 1. Broken Links
    report.append(f"### Broken Links ({len(broken_links)})")
    if broken_links:
        for pg, target in broken_links:
            report.append(f"- `[[{target}]]` referenced in [{pg}.md](file:///{TOPICS_DIR_URL}/{pg}.md)")
    else:
        report.append("- No broken links found.")
    report.append("")

    # 2. Orphan Pages (ignore index.md or logs, only check topics)
    report.append(f"### Orphan Pages ({len(orphan_pages)})")
    if orphan_pages:
        for pg in sorted(orphan_pages):
            report.append(f"- [{pg}.md](file:///{TOPICS_DIR_URL}/{pg}.md) — no incoming links")
    else:
        report.append("- No orphan pages found.")
    report.append("")

    # 3. Stale Stubs
    report.append(f"### Stale Stubs ({len(stale_stubs)})")
    if stale_stubs:
        for pg, dt, days in stale_stubs:
            report.append(f"- [{pg}.md](file:///{TOPICS_DIR_URL}/{pg}.md) — Status: stub since {dt} ({days} days ago)")
    else:
        report.append("- No stale stubs found.")
    report.append("")

    # 4. Other Issues (Uncited facts, Missing summaries, Index drift)
    other_issues_count = len(uncited_facts) + len(missing_summaries) + len(index_drift)
    report.append(f"### Consistency & Schema Verification ({other_issues_count})")
    
    if index_drift:
        report.append("**Index Drift:**")
        for drift in index_drift:
            report.append(f"- {drift}")
            
    if missing_summaries:
        report.append("**Missing / Short Summaries:**")
        for pg in missing_summaries:
            report.append(f"- [{pg}.md](file:///{TOPICS_DIR_URL}/{pg}.md) has a missing or extremely brief summary")
            
    if uncited_facts:
        report.append("**Uncited Facts / Claims:**")
        for pg, fact in uncited_facts:
            report.append(f"- [{pg}.md](file:///{TOPICS_DIR_URL}/{pg}.md): \"{fact[:60]}...\" has no citable [source-slug]")
            
    if other_issues_count == 0:
        report.append("- No consistency or schema validation issues found.")
    report.append("")

    # 5. Prioritized Recommended Actions
    report.append("### Recommended Actions")
    actions = []
    if broken_links:
        actions.append("1. **Fix Broken Links**: Create the missing files or correct the typos in internal references.")
    if index_drift:
        actions.append("2. **Resolve Index Drift**: Sync the index.md table with actual topic files using ingest.")
    if orphan_pages:
        actions.append("3. **Cross-link Orphans**: Link to orphan pages from other relevant context sheets.")
    if uncited_facts:
        actions.append("4. **Cite Key Facts**: Add source-slug brackets to claims lacking citations.")
    if not actions:
        actions.append("- All systems green! The wiki is perfectly healthy.")
    report.append("\n".join(actions))
    
    report_text = "\n".join(report)
    print(report_text)
    
    # Save report to GITHUB_STEP_SUMMARY if present
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "w", encoding="utf-8") as sf:
            sf.write(report_text)
            
    return len(broken_links) == 0 and len(index_drift) == 0

# ==================== INGEST OPERATION ====================

def run_ingest():
    print("Running Source Ingestion...")
    
    # 1. Identify processed sources in log.md
    processed_sources = set()
    if os.path.exists(LOG_PATH):
        with open(LOG_PATH, "r", encoding="utf-8") as f:
            log_content = f.read()
        # Find all brackets like [karpathy-llm-wiki-2026]
        processed_sources = set(re.findall(r'\[([a-zA-Z0-9\-_]+)\]', log_content))

    # 2. Scan raw/ directory for files
    raw_files = [f for f in os.listdir(RAW_DIR) if f != ".gitkeep"]
    new_sources = []
    
    for r_file in raw_files:
        # Create a source slug
        slug = re.sub(r'[^a-zA-Z0-9\-]', '-', r_file.lower().split('.')[0])
        # Format year/date in slug if missing, or keep it short
        if slug not in processed_sources:
            new_sources.append((r_file, slug))
            
    if not new_sources:
        print("Nothing new to ingest.")
        summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
        if summary_path:
            with open(summary_path, "w", encoding="utf-8") as sf:
                sf.write("### Source Ingestion\n- Nothing new to ingest. The wiki is up to date!")
        return True

    print(f"Found {len(new_sources)} new source(s) to process:")
    for fn, sl in new_sources:
        print(f" - {fn} -> [{sl}]")

    pages_created = []
    pages_updated = []

    for fn, source_slug in new_sources:
        file_path = os.path.join(RAW_DIR, fn)
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            source_content = f.read()

        if GEMINI_API_KEY:
            print(f"Calling Gemini to analyze and compile [{source_slug}]...")
            # We construct a prompt to extract pages in JSON format
            prompt = f"""
You are a compiler for Andrej Karpathy's LLM Wiki pattern. 
Your input is a raw source document and its source-slug: [{source_slug}].
Your output MUST be a JSON object containing the wiki pages (topics, entities, or synthesis) to create or update.

SCHEMA & TEMPLATE:
Every page must have this exact template structure:
```markdown
# <Title>

**Type:** Topic | Entity | Synthesis
**Status:** stub | developing | mature
**Last updated:** {datetime.now().strftime('%Y-%m-%d')}
**Sources:** [source-slug]

## Summary
One paragraph. The most important thing to know about this topic.

## Key Facts / Claims
- Bullet list of citable facts. Every bullet must end with its source citation, e.g. [{source_slug}]

## Connections
- [[related-topic-slug]] — one sentence on how they relate

## Open Questions
- Questions the source leaves unanswered

## Raw Notes
Overflow space.
```

JSON Output Format:
Your response must be JSON only with this structure:
{{
  "pages": {{
    "page-slug-1": "markdown content for page 1...",
    "page-slug-2": "markdown content for page 2..."
  }}
}}

RULES:
1. Slugs must be lowercase, hyphen-separated.
2. Facts must be cited exactly with `[{source_slug}]`.
3. Do not invent facts not present in the source.

Raw Source Content:
{source_content}
"""
            res_text = call_gemini(prompt)
            # Try to parse JSON from response
            try:
                # Strip markdown code blocks if any
                clean_json = res_text
                if "```json" in clean_json:
                    clean_json = clean_json.split("```json")[1].split("```")[0]
                elif "```" in clean_json:
                    clean_json = clean_json.split("```")[1].split("```")[0]
                
                parsed = json.loads(clean_json.strip())
                for slug, page_content in parsed.get("pages", {}).items():
                    target_path = os.path.join(TOPICS_DIR, f"{slug}.md")
                    if os.path.exists(target_path):
                        # Merge or update
                        with open(target_path, "r", encoding="utf-8") as tf:
                            existing_content = tf.read()
                        
                        # A simple merge of facts and summary
                        merged_content = f"{existing_content}\n\n## Updated in [{source_slug}]:\n{page_content}"
                        # In real run, we let LLM merge, but for this CLI we overwrite or append cleanly
                        # Let's overwrite with the new comprehensive version of the page
                        with open(target_path, "w", encoding="utf-8") as tf:
                            tf.write(page_content)
                        pages_updated.append(slug)
                    else:
                        with open(target_path, "w", encoding="utf-8") as tf:
                            tf.write(page_content)
                        pages_created.append(slug)
            except Exception as e:
                print(f"Error parsing Gemini response for {source_slug}: {str(e)}. Falling back to Mock Ingest.")
                # Fallback to mock
                m_created, m_updated = mock_ingest_source(source_slug, fn, source_content)
                pages_created.extend(m_created)
                pages_updated.extend(m_updated)
        else:
            # Mock Ingest Mode
            print(f"GEMINI_API_KEY not found. Running Mock Ingestion for [{source_slug}]...")
            m_created, m_updated = mock_ingest_source(source_slug, fn, source_content)
            pages_created.extend(m_created)
            pages_updated.extend(m_updated)

    # Perform back-linking check on all pages
    all_slugs = pages_created + pages_updated
    topic_files = [f for f in os.listdir(TOPICS_DIR) if f.endswith(".md")]
    for t_file in topic_files:
        file_path = os.path.join(TOPICS_DIR, t_file)
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        modified = False
        for new_slug in all_slugs:
            # If the new slug is mentioned in text but not as a link
            name_words = new_slug.replace("-", " ")
            if name_words in content.lower() and f"[[{new_slug}]]" not in content:
                # Add cross link in connections
                conn_match = re.search(r'## Connections', content)
                if conn_match:
                    content = content.replace("## Connections", f"## Connections\n- [[{new_slug}]] — Automatically linked related topic")
                    modified = True
        if modified:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)

    # 5. Update index.md
    update_index(pages_created, pages_updated)

    # 6. Append to log.md
    append_log(new_sources, pages_created, pages_updated)

    # Output to stdout and GitHub step summary
    summary_md = []
    summary_md.append("### Ingest Operation Completed successfully!\n")
    summary_md.append(f"**Processed Sources:** {len(new_sources)}")
    for fn, slug in new_sources:
        summary_md.append(f"- `{fn}` (Citation: `[{slug}]`)")
    summary_md.append("")
    summary_md.append(f"**Pages Created ({len(pages_created)}):**")
    for p in pages_created:
        summary_md.append(f"- [{p}.md](file:///{TOPICS_DIR_URL}/{p}.md)")
    summary_md.append("")
    summary_md.append(f"**Pages Updated ({len(pages_updated)}):**")
    for p in pages_updated:
        summary_md.append(f"- [{p}.md](file:///{TOPICS_DIR_URL}/{p}.md)")
        
    summary_text = "\n".join(summary_md)
    print(summary_text)
    
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "w", encoding="utf-8") as sf:
            sf.write(summary_text)
            
    return True

def mock_ingest_source(source_slug, filename, content):
    """Fallback generator to compile dummy sheets for testing without LLM costs."""
    created = []
    updated = []
    
    # Try to extract key concepts simply by finding lines with keywords
    sentences = [line.strip() for line in content.split("\n") if len(line.strip()) > 30][:5]
    if not sentences:
        sentences = ["This is an automatically ingested source research paper representing high value technical claims."]
        
    # Generate one primary page
    primary_slug = source_slug
    target_path = os.path.join(TOPICS_DIR, f"{primary_slug}.md")
    
    page_md = f"""# {primary_slug.replace("-", " ").title()}

**Type:** Topic
**Status:** stub
**Last updated:** {datetime.now().strftime('%Y-%m-%d')}
**Sources:** [{source_slug}]

## Summary
Automatically compiled stub page representing research findings from the raw source file `{filename}`.

## Key Facts / Claims
"""
    for s in sentences:
        clean_s = s.replace("-", "").strip()
        page_md += f"- {clean_s} [{source_slug}]\n"
        
    page_md += f"""
## Connections
- [[llm-wiki-pattern]] — Part of the persistent knowledge graph

## Open Questions
- What other key conclusions does this file hold?

## Raw Notes
Ingested source title: {filename}.
"""
    
    if os.path.exists(target_path):
        updated.append(primary_slug)
    else:
        created.append(primary_slug)
        
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(page_md)
        
    return created, updated

def update_index(created, updated):
    """Updates wiki/index.md rows and page counts."""
    # Scan all current pages to get accurate status and summary
    topic_files = [f for f in os.listdir(TOPICS_DIR) if f.endswith(".md")]
    rows = []
    
    for t_file in sorted(topic_files):
        slug = t_file[:-3]
        file_path = os.path.join(TOPICS_DIR, t_file)
        
        type_str = "Topic"
        status_str = "stub"
        summary_str = "No summary available."
        
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        type_match = re.search(r'\*\*Type:\*\*\s*(Topic|Entity|Synthesis)', content, re.IGNORECASE)
        status_match = re.search(r'\*\*Status:\*\*\s*(stub|developing|mature)', content, re.IGNORECASE)
        summary_match = re.search(r'## Summary\s*\n+([^#\n][^\n]*)', content)
        
        if type_match:
            type_str = type_match.group(1).title()
        if status_match:
            status_str = status_match.group(1).lower()
        if summary_match:
            summary_str = summary_match.group(1).strip()
            # Truncate summary if long
            if len(summary_str) > 80:
                summary_str = summary_str[:77] + "..."
                
        rows.append(f"| [{slug}](topics/{t_file}) | {type_str} | {status_str} | {summary_str} |")

    index_md = f"""# Wiki Index

Master catalog of all pages. Updated automatically on every ingest.

| Page | Type | Status | Summary |
|---|---|---|---|
"""
    index_md += "\n".join(rows) + "\n"
    index_md += f"""
---

*Last updated: {datetime.now().strftime('%Y-%m-%d')}*
*Total pages: {len(topic_files)}*
"""
    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        f.write(index_md)

def append_log(new_sources, created, updated):
    """Appends ingest action entries to wiki/log.md."""
    log_entry = f"""
## {datetime.now().strftime('%Y-%m-%d')} — Ingestion run

**Operation:** Source files processed
**Sources processed:** {", ".join([f"[{slug}] ({fn})" for fn, slug in new_sources])}
**Pages created:** {", ".join([f"`{p}`" for p in created]) if created else "(none)"}
**Pages updated:** {", ".join([f"`{p}`" for p in updated]) if updated else "(none)"}
**Notes:** Automated ingestion run.
"""
    if os.path.exists(LOG_PATH):
        with open(LOG_PATH, "r", encoding="utf-8") as f:
            existing = f.read()
        # Insert entry after header or at the end
        if "---" in existing:
            parts = existing.split("---", 1)
            new_log = f"{parts[0]}---\n{log_entry}{parts[1]}"
        else:
            new_log = f"{existing}\n{log_entry}"
    else:
        new_log = f"# Activity Log\n\nAppend-only chronological record of all wiki operations.\n\n---\n{log_entry}"
        
    with open(LOG_PATH, "w", encoding="utf-8") as f:
        f.write(new_log)

# ==================== QUERY OPERATION ====================

def run_query(question: str):
    print(f"Querying Wiki: \"{question}\"")
    
    # 1. Scan available pages
    topic_files = [f for f in os.listdir(TOPICS_DIR) if f.endswith(".md")]
    if not topic_files:
        print("The wiki is empty. Please run ingest first.")
        return False
        
    relevant_pages = []
    
    # Simple keyword selection
    query_words = set(re.findall(r'\w+', question.lower()))
    
    for t_file in topic_files:
        slug = t_file[:-3]
        file_path = os.path.join(TOPICS_DIR, t_file)
        
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read().lower()
            
        # Match count
        matches = sum(1 for w in query_words if w in content)
        if matches > 0:
            relevant_pages.append((slug, matches, file_path))
            
    # Sort by keyword matches
    relevant_pages.sort(key=lambda x: x[1], reverse=True)
    selected_pages = relevant_pages[:5] # Load top 5
    
    if not selected_pages:
        # Fallback to load everything if very short wiki, or just top pages
        selected_pages = [(f[:-3], 0, os.path.join(TOPICS_DIR, f)) for f in topic_files[:3]]

    # Load full contents
    context = []
    for slug, score, path in selected_pages:
        with open(path, "r", encoding="utf-8") as f:
            context.append(f"--- START PAGE: {slug} ---\n{f.read()}\n--- END PAGE: {slug} ---")

    combined_context = "\n\n".join(context)

    if GEMINI_API_KEY:
        print("Generating cited answer from Gemini...")
        prompt = f"""
You are an expert researcher querying the ContextSpace compiled wiki.
Your task is to answer this research question using ONLY the provided wiki pages context.
Do NOT use outside knowledge or internet sources.

Research Question:
{question}

Wiki Pages Context:
{combined_context}

INSTRUCTIONS:
1. Synthesize a highly-citable, structured answer.
2. Use inline citations referencing the wiki page slug in brackets, e.g. [llm-wiki-pattern].
3. At the end of the answer, list:
   - **Sources used:** a bulleted list of wiki page slugs loaded.
   - **Confidence:** high / medium / low based on context coverage.
   - **Gaps:** topics this question touches that are not covered in the wiki.
"""
        answer = call_gemini(prompt)
    else:
        # Mock Query Mode
        print("GEMINI_API_KEY not found. Running Mock Query...")
        sources_list = ", ".join([f"`{slug}`" for slug, _, _ in selected_pages])
        answer = f"""# Answer: {question}

This is a synthesized answer from the local wiki (Mock Mode active).

### Summary of findings
- We analyzed the local index catalog and loaded the following sources: {sources_list}.
- The terms in your query mapped to these topics. 

### Key facts cited
- The **LLM Wiki Pattern** serves as a compiler system where raw resources are compiled into living markdown contexts [[llm-wiki-pattern]].
- Active topic sheets under `wiki/topics/` represent the current state of synthesized research facts.

---
- **Sources used:**
"""
        for slug, _, _ in selected_pages:
            answer += f"  - `[{slug}]` (topics/{slug}.md)\n"
        answer += """- **Confidence:** Medium (Mock engine synthesis)
- **Gaps:** High-fidelity reasoning is mock-only. Configure a `GEMINI_API_KEY` for intelligent synthesis.
"""

    print("\n==================== ANSWER ====================")
    print(answer)
    print("================================================\n")
    
    # Save to Step Summary
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "w", encoding="utf-8") as sf:
            sf.write(f"### Query Results for: *\"{question}\"*\n\n{answer}")
            
    return True

# ==================== PROMOTE OPERATION ====================

def run_promote(filename: str):
    print(f"Promoting output file '{filename}' to raw source...")
    
    # 1. Locate file in output/
    output_dir = os.path.join(WORKSPACE_DIR, "output")
    source_path = os.path.join(output_dir, filename)
    
    # Try different extensions if not provided
    if not os.path.exists(source_path):
        if not filename.endswith(".md"):
            source_path = os.path.join(output_dir, filename + ".md")
            filename = filename + ".md"
            
    if not os.path.exists(source_path):
        print(f"Error: Output file not found at {source_path}")
        return False
        
    # 2. Copy to raw/
    dest_path = os.path.join(RAW_DIR, filename)
    print(f"Copying to {dest_path}...")
    try:
        with open(source_path, "r", encoding="utf-8") as sf:
            content = sf.read()
        with open(dest_path, "w", encoding="utf-8") as df:
            df.write(content)
    except Exception as e:
        print(f"Error promoting file: {str(e)}")
        return False
        
    print(f"Successfully promoted '{filename}' to raw/.")
    
    # 3. Run Ingest
    print("\n--- Starting Ingest ---")
    ingest_success = run_ingest()
    if not ingest_success:
        print("Ingest failed.")
        return False
        
    # 4. Run Lint
    print("\n--- Starting Lint ---")
    lint_success = run_lint()
    
    print("\nPromote operation completed successfully!")
    return True

# ==================== CLI RUNNER ====================

def main():
    if len(sys.argv) < 2:
        print("ContextSpace CLI Tool")
        print("Usage:")
        print("  python workflow.py ingest        - Ingest new raw files into the wiki")
        print("  python workflow.py query <q>     - Query the wiki")
        print("  python workflow.py lint          - Check the wiki health")
        print("  python workflow.py promote <f>   - Promote an output file to raw/ and run ingest + lint")
        sys.exit(1)
        
    cmd = sys.argv[1].lower()
    
    if cmd == "ingest":
        success = run_ingest()
        sys.exit(0 if success else 1)
    elif cmd == "query":
        if len(sys.argv) < 3:
            print("Error: query requires a question parameter.")
            print("Usage: python workflow.py query \"What is the main topic?\"")
            sys.exit(1)
        q = sys.argv[2]
        success = run_query(q)
        sys.exit(0 if success else 1)
    elif cmd == "lint":
        success = run_lint()
        sys.exit(0 if success else 1)
    elif cmd == "promote":
        if len(sys.argv) < 3:
            print("Error: promote requires a filename parameter.")
            print("Usage: python workflow.py promote \"discussion_1_setup.md\"")
            sys.exit(1)
        f = sys.argv[2]
        success = run_promote(f)
        sys.exit(0 if success else 1)
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)

if __name__ == "__main__":
    main()
