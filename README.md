# Newsletter System — Project README

> **Read this file first** when starting a new session involving newsletters.
> It contains everything you need to understand the project structure, conventions, and how to make changes.

---

## Overview

This is a newsletter generation system. Run `/generate-newsletter <topic>` to search the web for current news on a given topic and compile it into a rich HTML newsletter.

The system is designed to support **multiple newsletters** with shared rules. Right now there's one — **Eorzea Weekly** (FFXIV news) — but the architecture supports adding more topics easily.

## Folder Structure

```
Newsletters/
├── README.md                  ← You are here. Project context and conventions.
├── config/
│   ├── shared.md              ← Universal rules: date handling, recency enforcement,
│   │                             writing style, image handling,
│   │                             email delivery, verification checklist.
│   │                             ALL newsletters inherit these rules.
│   ├── ffxiv.md               ← FFXIV-specific: search queries, trusted sources,
│   │                             section structure, tag categories, intro style.
│   └── (future topic configs go here)
├── templates/
│   ├── mothercrystal.html     ← "Style C" — dark blue/cyan/purple Hydaelyn crystal theme.
│   │                             Used by the FFXIV newsletter.
│   └── (future templates go here)
├── output/
│   ├── eorzea-weekly-latest.html    ← Most recent newsletter (overwritten each week)
│   └── eorzea-weekly-YYYY-MM-DD.html ← Dated archive copies
└── .gmail-credentials         ← (Optional) Gmail App Password for email delivery.
                                  Line 1: sender email, Line 2: app password.
                                  If this file doesn't exist, email is skipped silently.
```

## Running a Newsletter

```
/generate-newsletter ffxiv        # normal run, writes to output/
/generate-newsletter ffxiv test   # dry run, writes to output/ffxiv-test.html only
```

The test mode generates output without overwriting the production `latest.html` file, and provides a summary of what it found and any issues.

## How Things Work

### Adding a New Newsletter

1. Create a new topic config: `config/{topic}.md` (follow `ffxiv.md` as a template)
2. Choose or create an HTML template in `templates/`
3. Run `/generate-newsletter {topic}` — it inherits all shared rules automatically

### Editing an Existing Newsletter

- **Change search queries or sources:** Edit the topic config (e.g., `config/ffxiv.md`)
- **Change writing style, recency rules, or shared behavior:** Edit `config/shared.md`
- **Change the visual design:** Edit the template in `templates/`
All changes take effect on the next run.

### Key Design Decisions

- **Single source of truth:** The config files ARE the instructions. The scheduled task prompt just points to them. No duplication.
- **Strict recency enforcement:** The shared config has non-negotiable rules about only using content from the last 8 days, verified by publication date. This prevents hallucinated or outdated content.
- **No training data for content:** The task is explicitly told it has ZERO reliable knowledge about any topic and must source everything from live web searches.
- **Graceful degradation:** If a section has no real news, it says "quiet week" rather than fabricating. If email credentials don't exist, it just saves the HTML file.

## Newsletter Sections (FFXIV)

The FFXIV newsletter has these sections (in order):
1. **Lead Story** — The biggest news of the week with featured image
2. **This Week in Eorzea** — 3-4 news briefs with category tags (cyan/amber/emerald/rose)
3. **Quote of the Week** — A notable quote from devs, creators, articles, or community (broadened to make it easier to fill)
4. **Hot on r/ffxiv** — 3-5 top Reddit threads with vote counts and links
5. **YouTube Roundup** — 3-5 videos from preferred creators with embedded YouTube players (prioritizes informational/lore content from Meoni, Desperius, AvvyCatte, Mr Happy, Zepla, Ethys Asher, etc.)
6. **Community Highlights** — 4-card grid (fan art, video, stats, hot thread)


