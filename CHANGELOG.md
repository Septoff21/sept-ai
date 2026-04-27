# Sept-AI Changelog

> Format: [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)  
> Site: https://sept-ai.netlify.app  
> Repo: https://github.com/Septoff21/sept-ai

---

## [Unreleased]

---

## [5.0.0] — Polish & Analytics *(planned)*

### Added
- Plausible Analytics (privacy-first, free tier)
- "Now" section on Me page (what I'm currently building/reading)
- Skill visualization row on Me page (icon grid, not just tags)
- "New since your last visit" dot on nav items (localStorage delta)
- System status page (`/status/`) showing last data refresh + source health

### Changed
- Full mobile responsive audit — hamburger nav, touch targets, scroll behavior
- Card hover animations: subtle `translateY(-2px)` + glow on all interactive cards
- Footer: add "Open source · MIT" + last-updated timestamp
- All empty states: friendly illustration + action CTA instead of plain text
- Font rendering: add `font-display: swap` for system font fallbacks
- Sitemap: include all pages, correct priorities

### Fixed
- Lighthouse score target: 90+ Performance, 95+ Accessibility, 100 Best Practices
- All pages have unique `<title>` + `<meta description>`
- Open Graph images verified on all key pages
- Internal link checker runs in CI

---

## [4.0.0] — Models · Daily · Agents redesign *(planned)*

### Added
- Models page: capability filter tabs (Text · Code · Vision · Multimodal · Reasoning)
- Models page: provider filter (Anthropic · OpenAI · Google · Meta · Mistral · Open)
- Models page: context window + benchmark score displayed on card
- Models page: "Best for" label (coding / reasoning / writing / multimodal)
- Daily page: proper briefing layout from `data/briefing.json`
- Daily page: "Top 5 Stories" numbered list with summaries
- Daily page: "Tool of the Day" spotlight card
- Daily page: "This Week in Numbers" stats strip
- Agents page: capability badge (CLI · API · GUI · Autonomous)
- Agents page: "Works with" provider tags on each agent card

### Changed
- Agents page: sort by GitHub stars descending by default
- Models page: curated shortlist pinned at top before full list
- Daily page: graceful fallback to last 15 news if briefing not populated

### Fixed
- Models page: category nav anchors work correctly on all screen sizes
- Agent card descriptions: truncate at 2 lines, expand on hover

---

## [3.0.0] — Tools · News redesign *(planned, next PR)*

### Added
- Tools page: live category filter tabs (All · Coding · Image · Video · Chat · Writing · Productivity · Agent · Local)
- Tools page: sort controls — Trending | Free first | Stars | A–Z
- Tools page: "Free" green badge prominent on cards when `free_quota` available
- Tools page: count per category tab e.g. "Coding (42)"
- Tools page: inline search within page (`?q=` param support)
- News page: EN / CN / All tab switcher (filters by `channel` field)
- News page: source color map — each major source gets a distinct accent
- News page: 2-col card grid on desktop, 1-col on mobile
- News page: AI summary shown on card if available
- News page: "Must Read" pinned row for top 3 items (source = Anthropic/OpenAI/DeepMind)
- News page: per-source filter pill bar

### Changed
- Tools page: removed favicon fetch fallback (was unreliable), use emoji icon only
- Tools page: card layout — cleaner, pricing shown without `💰` prefix clutter
- News page: replaced flat `hot-item` list with card grid
- News page: pagination → infinite-scroll style "Load more" button
- Both pages: sticky category nav background matches `--bg` (no blur artifact on mobile)

### Fixed
- Tools page: category order now matches `DESIGN_V2.md` priority (Coding first)
- News page: items with no `channel` field default to "EN"

---

## [2.1.0] — Homepage redesign — 2026-04-27

### Added
- Stat bar: live green pulse dot + counts (tools · models · articles)
- Quick-access 3-column grid with Lucide icons replacing "Where to start?" text block
- `@keyframes pulse` animation for the live indicator dot
- `All news →` shortcut link in Trending card header
- Footer: two-line with full nav links + GitHub link

### Changed
- Search box: `background: var(--bg2)` default, `var(--bg)` on focus; padding adjusted for Ctrl-K badge
- Trending: cleaner meta row (`display:flex`, `align-items:center`)
- News rows: hover-highlight (`background: var(--bg3)`) with smooth left indent animation
- News rows: AI summary preview shown on home page (truncated to 120 chars)
- Sidebar: 9 cards → 5 cards — removed Share, Random Discover, Daily Check-in, Recently Added
- Browse section: compact list with live counts instead of tag cloud
- Streak badge: JS inline in page, removed from baseof to avoid duplication

### Removed
- Share buttons (Twitter/LinkedIn/Copy link) — low usage, breaks aesthetic
- Random Discover card — gimmick, not useful
- Daily Check-in card — gamification noise
- Recently Added sidebar card — was duplicate of "Rising Fast"
- Weekly Digest sidebar card — data was unreliable

---

## [2.0.0] — Design System + Infrastructure — 2026-04

### Added
- Full Claude-style design system: warm palette (`#faf9f6` light / `#1a1817` dark)
- Amber accent (`#cc785c` dark / `#b5603f` light)
- Neon gradient borders via `::before` pseudo-element (amber → violet → cyan)
- Dark/Light theme toggle with `localStorage` persistence and FOUC prevention
- Lucide icons via CDN, `data-lucide` attribute pattern
- Visit streak badge in header (passive, auto-updates on page load)
- Me page (`/me/`) with: hero, real bio, 4 AI tools, 4 projects, TNG QR modal, knowledge vault overview
- Daily page (`/daily/`) with coming-soon card + news fallback
- `data/` → `site/data/` sync in Netlify build command (fix for stale data issue)
- `aggregate.yml` commits `site/data/` + `site/content/` alongside `data/`
- `PLAN_V2.md` + `DESIGN_V2.md` development docs
- `robots.txt` updated to correct domain

### Changed
- All layout templates fully translated to English (Phase 4)
- Nav menu: emoji → Lucide SVG icons
- `hugo.toml`: `disableKinds = ["taxonomy","term","RSS"]` at root level (TOML fix)
- `hugo.toml`: deprecated `paginate` → `[pagination] pagerSize = 20`
- `netlify.toml`: build command syncs `../data/*` before `hugo --minify`
- 168 content `.md` files: stripped `#` prefix from all tag values

### Fixed
- Netlify deploy failure: `#productivity` in filenames rejected by CDN
- Netlify deploy failure: deprecated Hugo `paginate` key
- TOML structure: `disableKinds` was parsed as `params.seo.disableKinds` (subtable bug)
- GitHub Actions push rejected: added `workflow` scope token

---

## [1.1.0] — Data pipeline + deploy — 2026-04

### Added
- `.github/workflows/aggregate.yml`: 6-hour cron, Python 3.12, runs aggregate.py + sync_claude_learning.py
- `.github/workflows/build-check.yml`: Hugo CI on push to main
- `netlify.toml`: Netlify build config (`base=site`, `publish=public`, Hugo 0.147.9)
- 15 new EN news sources: Anthropic, OpenAI, DeepMind, Meta AI, Mistral, ArXiv ×2, Papers With Code, HuggingFace, Simon Willison, Latent Space, Import AI, AI Alignment Forum, Cursor Blog, a16z AI
- 4 new CN sources: 虎嗅AI, 极客公园, 少数派 (+ existing 36氪, InfoQ)
- Reddit subreddits expanded: r/ClaudeAI, r/OpenAI, r/singularity, r/ChatGPT
- `static/robots.txt` updated for sept-ai.netlify.app domain
- SEO partial rewritten: absolute OG image URL, twitter:title, twitter:image

### Changed
- `news_rss.py`: AI_KEYWORDS_EN expanded (MCP, Claude Code, Cursor, Windsurf, HuggingFace, etc.)

---

## [1.0.0] — Initial release — 2026-04

### Added
- Fork from `laolaoshiren/ai-hot`, clean repo as `Septoff21/sept-ai`
- Obsidian vault skeleton at `my-content/` (7 top-level folders)
- `scripts/vault_writer.py` — unified markdown writer for vault
- `scripts/sync_claude_learning.py` — pulls Septoff21/claude-learning into `50-My-Knowledge/`
- All layout templates translated from Chinese to English
- `site/hugo.toml`: `baseURL`, `title`, `languageCode = "en"`, EN nav menu
- `README.md` rewritten in English
- `PLAN.md`: 8-phase project plan

### Changed
- `hugo.toml`: new title "Sept-AI — Your AI Navigator & Knowledge Hub"
- Nav menu items: Trending · Tools · Models · Agents · News · Providers · Daily · Me
- Search page: default keywords changed to EN (Claude, Cursor, ChatGPT, Gemini, etc.)

---

[Unreleased]: https://github.com/Septoff21/sept-ai/compare/v2.1.0...HEAD
[5.0.0]: https://github.com/Septoff21/sept-ai/compare/v4.0.0...v5.0.0
[4.0.0]: https://github.com/Septoff21/sept-ai/compare/v3.0.0...v4.0.0
[3.0.0]: https://github.com/Septoff21/sept-ai/compare/v2.1.0...v3.0.0
[2.1.0]: https://github.com/Septoff21/sept-ai/compare/v2.0.0...v2.1.0
[2.0.0]: https://github.com/Septoff21/sept-ai/compare/v1.1.0...v2.0.0
[1.1.0]: https://github.com/Septoff21/sept-ai/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/Septoff21/sept-ai/releases/tag/v1.0.0
