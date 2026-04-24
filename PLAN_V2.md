# Sept-AI · V2.0 Development Plan

> **Started:** 2026-04  
> **Cadence:** Monthly iteration (V2.1, V2.2 ...)  
> **Site:** https://sept-ai.netlify.app  
> **Repo:** https://github.com/Septoff21/sept-ai  
> **Stack:** Hugo + GitHub Actions + Netlify (100% free)

---

## ✅ V1.0 — Completed (2026-04)

| Phase | What was done |
|---|---|
| Phase 1 | Repo setup, fork from ai-hot, new remote |
| Phase 2 | Obsidian vault skeleton (`my-content/`) |
| Phase 3 | Data layer: vault_writer.py, sync_claude_learning.py |
| Phase 4 | Full EN i18n — all templates translated |
| Phase 5 | UI redesign: Claude warm palette, dark/light toggle, neon borders, Lucide icons |
| Phase 6 | 15+ EN sources + 4 CN sources added to news pipeline |
| Phase 7 | Me page with TNG QR modal, projects, contact |
| Phase 8 | Netlify deploy, GitHub Actions cron (6h), SEO, sitemap, robots.txt |

**V1 live at:** `main@33131dd` — Published ✅

---

## 🐛 V1 Bugs Fixed in V2.0 Kickoff

| Bug | Root cause | Fix |
|---|---|---|
| Netlify deploy always "Skipped" | `netlify.toml` didn't sync `data/` → `site/data/` | Added `cp -r ../data/* data/` to build command |
| GitHub Actions data not reaching Hugo | `aggregate.yml` only committed `data/`, not `site/data/` or `site/content/` | Added `site/data/` and `site/content/` to git add |
| `#` chars in tag filenames | Tag values had `#` prefix in 168 `.md` files | Python regex strip + `disableKinds` at TOML root level |
| Deprecated `paginate` key | Hugo 0.128 removed it | Changed to `[pagination] pagerSize = 20` |

---

## 🏗️ V2.0 Architecture (Auto-Update Loop)

```
Every 6 hours (GitHub Actions)
        ↓
  aggregate.py runs:
    ├── RSS / API news (40+ sources)
    ├── GitHub trending
    ├── HuggingFace models
    └── generate_news_pages.py → site/content/news/
        ↓
  git commit: data/ + site/data/ + site/content/ + my-content/
        ↓
  Netlify detects push
        ↓
  Build: cp ../data/* data/ && hugo --minify
        ↓
  Site live at sept-ai.netlify.app (updated)
```

**All free:**
- GitHub Actions: 2,000 min/month free (6h cron uses ~10 min/day = ~300 min/month)
- Netlify: 300 build min/month free (each Hugo build ≈ 10s = trivial)
- No paid APIs, no servers

---

## 📋 V2.0 Backlog

### 🎨 V2.1 — Design Overhaul (Next)
> User to provide exact design requirements

- [ ] Homepage hero section redesign
- [ ] Card layout improvements (tools, models, news)
- [ ] Me page: add personal tools list
- [ ] Me page: update bio text
- [ ] Mobile responsiveness audit
- [ ] Color palette refinement (pending user input)
- [ ] Typography improvements

**Me page tools to list (pending user input):**
- [ ] Collect from user: list of AI tools you actually use daily

### 📰 V2.2 — Content & Data Quality
- [ ] De-duplicate news items across runs
- [ ] News source reliability scoring
- [ ] Better CN/EN tab filtering on news page
- [ ] Daily brief section (auto-generated summary of top 5 news)
- [ ] Tools: add more curated entries with real reviews

### 🔍 V2.3 — Discovery Features
- [ ] Search page improvements (better UX)
- [ ] Tag/filter system for tools (by use case)
- [ ] "New this week" badge on recently added tools/models
- [ ] Trending score visible on cards

### 👤 V2.4 — Personal Knowledge Layer
- [ ] Expose selected Obsidian notes as public pages
- [ ] Claude Learning vault summaries on site
- [ ] Prompt library (selected public prompts)
- [ ] "What I'm building" section

### 📈 V2.5 — Analytics & SEO
- [ ] Add Plausible Analytics (free, privacy-friendly)
- [ ] Structured data (JSON-LD) for tools/models
- [ ] Open Graph previews for all pages
- [ ] Performance audit (Lighthouse 90+)

---

## 👤 Me Page — Information to Fill

> Complete this section and we'll update the site

### Bio
```
Name: Septoff21
Location: [TBD]
Tagline: [TBD]
About: [TBD - 2-3 sentences]
```

### Tools I Use Daily
> List your actual daily-driver AI tools here

| Tool | Category | Why I use it |
|---|---|---|
| [TBD] | [TBD] | [TBD] |

### Projects
| Project | Description | Link |
|---|---|---|
| sept-ai | AI navigator & knowledge hub | https://github.com/Septoff21/sept-ai |
| claude-learning | Claude AI learning notes | https://github.com/Septoff21/claude-learning |
| [more?] | | |

### Contact
- GitHub: https://github.com/Septoff21
- Email: septoff21@gmail.com
- Support: TNG eWallet QR (already on site)

---

## 🔄 Monthly Update Cadence

| Month | Focus |
|---|---|
| 2026-05 | V2.1: Design + Me page personal info |
| 2026-06 | V2.2: Content quality, daily brief |
| 2026-07 | V2.3: Discovery features |
| 2026-08 | V2.4: Personal knowledge layer |
| 2026-09 | V2.5: Analytics + SEO |

---

## 🛠️ Local Dev Commands

```bash
# Run site locally
cd site && hugo server -D

# Run aggregator manually
cd scripts && python aggregate.py

# Check build before push
cd site && hugo --minify

# Push to trigger Netlify deploy
git push origin main
```

---

## 📁 Key File Map

| File | Purpose |
|---|---|
| `site/hugo.toml` | Hugo config (baseURL, menu, pagination) |
| `netlify.toml` | Netlify build command + headers + redirects |
| `.github/workflows/aggregate.yml` | 6h data refresh cron |
| `.github/workflows/build-check.yml` | CI build check on PR/push |
| `scripts/aggregate.py` | Main data pipeline orchestrator |
| `scripts/news_rss.py` | RSS/scrape news from 40+ sources |
| `site/layouts/_default/baseof.html` | Master layout (theme, nav, footer) |
| `site/layouts/me/list.html` | Me page template |
| `site/layouts/daily/list.html` | Daily brief template |
| `data/*.json` | All raw data (committed, updated by Actions) |
| `site/data/*.json` | Hugo-accessible data (synced at build) |
| `my-content/` | Obsidian knowledge vault |
