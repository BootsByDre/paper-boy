# FFXIV Newsletter — Topic Configuration

**Newsletter Name:** Eorzea Weekly
**Template:** `../templates/mothercrystal.html`
**Output Path:** `../output/`
**Recipient:** hfleming42@gmail.com
**Credentials File:** `../.gmail-credentials`

---

## Search Queries

Run these searches, including the current month and year in each:

### Official News
- `"FFXIV news {month} {year}"`
- `"Final Fantasy XIV patch notes {month} {year}"`
- `"FFXIV Lodestone news {month} {year}"`
- `"site:na.finalfantasyxiv.com {month} {year}"`
- `"FFXIV maintenance OR update {month} {year}"`

### Events & Seasonal Content
- `"FFXIV event {month} {year}"`
- `"FFXIV crossover OR collaboration {month} {year}"`
- `"FFXIV seasonal event {month} {year}"`

### Developer Communication
- `"Naoki Yoshida FFXIV {month} {year}"`
- `"FFXIV Letter from the Producer {month} {year}"`
- `"FFXIV live letter {month} {year}"`
- `"FFXIV Fan Fest {month} {year}"`

### Community & Social
- `"FFXIV reddit this week {month} {year}"`
- `"FFXIV community {month} {year}"`
- `"site:reddit.com/r/ffxiv {month} {year}"`
- `"FFXIV fan art {month} {year}"`
- `"FFXIV content creator {month} {year}"`

### Trusted Sources (prioritize in this order)
1. na.finalfantasyxiv.com (The Lodestone) — official news, patch notes, maintenance schedules
2. square-enix-games.com — official announcements
3. reddit.com/r/ffxiv — community discussions, fan art, hot threads
4. Official FFXIV Twitter/X accounts
5. Major gaming outlets (IGN, Kotaku, PC Gamer, Eurogamer, etc.)
6. FFXIV community creators (YouTube, Twitch)

## Newsletter Sections

### 1. Lead Story
- The single biggest FFXIV news item of the week.
- Badge/category label should match the type (e.g., "Main Scenario", "Patch Notes", "Fan Fest", "New Raid Tier").
- Include a 2-3 sentence summary and link to source.
- Include a featured image if available.

### 2. This Week in Eorzea (3-4 items)
Each item should be categorized with one of these tags:

| Tag | CSS Class | Use For |
|-----|-----------|---------|
| Patch Notes | `tag-cyan` | Game updates, hotfixes, patch notes |
| Event | `tag-amber` | In-game events, real-world events, Fan Fest |
| Community | `tag-emerald` | Creator content, community milestones, social media buzz |
| Lore / Discussion | `tag-rose` | Lore discoveries, theory threads, heated debates |

### 3. Quote of the Week
A real, attributed quote. Acceptable sources (in priority order):
- Naoki Yoshida (Yoshi-P) or other FFXIV developers
- Notable community figures or content creators
- A particularly well-stated Reddit/forum post (attribute to the username)
- A memorable line from a gaming outlet's article or review (attribute to the author and publication)
- A notable line from official patch notes or Lodestone posts

The bar is low — any interesting, real, attributed snippet from the week counts. The goal is flavor, not formality. Try hard to find something before omitting this section. Search specifically for developer interviews, community reactions, and article pull-quotes from this week.

### 4. Hot Reddit Threads (3-5 items)
Search for the most popular/upvoted posts on r/ffxiv from this week. For each thread include:
- The post title (as a link to the Reddit thread)
- The upvote count if available
- A 1-sentence summary of what the discussion is about

Search queries to use:
- `"site:reddit.com/r/ffxiv" {month} {year}`
- `"r/ffxiv" top posts this week {month} {year}`
- `"reddit ffxiv" trending {month} {year}`

Present these as a simple list. If fewer than 3 threads are found from this week, show what you have.

### 5. YouTube Roundup (3-5 videos)
Search for recent FFXIV videos from prominent creators. Preferred creators (informational/lore focus):
- Meoni
- Desperius FFXIV
- AvvyCatte (Avvy)
- Mr Happy
- Zepla / Zepla HQ
- Ethys Asher (lore)
- Lynx Kameli
- Work to Game
- Ilya Dalamiq

Deprioritize pure stream highlight / reaction content (e.g., Xenosys Vex stream clips) in favor of informational, guide, lore, or editorial videos.

Search queries:
- `"FFXIV" "{creator name}" {month} {year}` for each creator above
- `"FFXIV" YouTube {month} {year} guide OR lore OR news`

For each video, include:
- The video title
- The creator name
- An embedded YouTube iframe so the reader can click play inline: `<iframe width="100%" height="200" src="https://www.youtube.com/embed/{VIDEO_ID}" frameborder="0" allowfullscreen></iframe>`
- Extract the VIDEO_ID from the YouTube URL (the `v=` parameter or the path after `youtu.be/`)

### 6. Community Highlights (4 cards)

| Card | What to Find |
|------|-------------|
| 🎨 Fan Art Pick | Top-upvoted fan art from r/ffxiv or Twitter this week |
| 🎬 Video of the Week | Notable YouTube/Twitch content (guides, documentaries, comedy) |
| 📊 By the Numbers | A data point, milestone, or statistic (player counts, clear rates, sales figures, etc.) |
| 🔥 Hot Thread | The most active or controversial discussion from Reddit/forums |

## Intro Paragraph Style

The intro should be 1-2 sentences that tease the top 2-3 stories. Start with "Welcome back, Warrior of Light." Use `<strong>` tags to highlight the lead story. End with a thematic sign-off like "Let's attune." or "Time to check the duty finder." Keep it casual and fun.

## Subject Line Format

`Eorzea Weekly — Week of {Month Day, Year}`
