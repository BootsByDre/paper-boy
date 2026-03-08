---
description: Generate a newsletter HTML file for a given topic. Usage: /generate-newsletter <topic> [test]
---

Generate a newsletter HTML file using the paper-boy newsletter system.

Arguments: $ARGUMENTS
- First argument: topic name (e.g. "ffxiv") — maps to /Users/harry/code/paper-boy/config/{topic}.md
- Optional second argument: "test" — dry run mode, output to {name}-test.html without overwriting latest

Steps:
1. Read /Users/harry/code/paper-boy/config/shared.md (universal rules — apply these to every run)
2. Read /Users/harry/code/paper-boy/config/{topic}.md (topic config — get template path, output path, sections, search queries)
3. Search the web and compile the newsletter HTML following those configs
4. In normal mode: write to the output paths specified in the topic config (latest + dated archive)
   In test mode: write ONLY to /Users/harry/code/paper-boy/output/{name}-test.html, then print a brief summary of sections populated and any issues
5. Do not send any email — HTML output only
6. Do not skip the verification checklist at the end of shared.md
