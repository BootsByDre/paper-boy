# Paper Boy — Claude Code Project

This is a newsletter generation system migrated from Claude Cowork to Claude Code.

## How to Generate a Newsletter

Use the `/generate-newsletter` skill:

```
/generate-newsletter ffxiv        # normal run, writes to output/
/generate-newsletter ffxiv test   # dry run, writes to output/ffxiv-test.html only
```

The skill reads `config/shared.md` (universal rules) and `config/{topic}.md` (topic-specific config), then searches the web and writes the HTML output.

## Project Structure

```
paper-boy/
├── CLAUDE.md                          ← You are here
├── README.md                          ← Detailed docs (note: some sections reference old Cowork setup)
├── config/
│   ├── shared.md                      ← Universal rules: recency, writing style, verification checklist
│   └── ffxiv.md                       ← FFXIV newsletter config: queries, sources, sections, output paths
├── templates/
│   └── mothercrystal.html             ← HTML template used by the FFXIV newsletter
├── output/                            ← Generated newsletters go here
└── .claude/skills/generate-newsletter/ ← The skill definition
```

## What Was Removed (vs. Cowork)

- **Scheduled tasks** — no longer automated; run manually via the skill
- **Email delivery** — HTML output only, no email sending

## Adding a New Newsletter

1. Create `config/{topic}.md` (use `ffxiv.md` as a template)
2. Choose or create an HTML template in `templates/`
3. The skill will pick it up automatically via `/generate-newsletter {topic}`
