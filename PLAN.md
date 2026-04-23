# Sept-AI · Project Plan

> **Repo:** `septoff21/sept-ai` · **Deploy:** Netlify (free subdomain) · **Vault:** `my-content/` (Obsidian)
> **Focus:** International English (primary) + Chinese (personal) AI navigator & knowledge hub.

---

## 🎯 Core Principles

1. **Single source of truth** = Obsidian Vault at `my-content/`
2. **Main layer** (ai-hot navigator) + **Extension layer** (my knowledge) cleanly separated
3. **EN / CN dual channels** for news & daily brief
4. **Clean design** — Claude/Linear/Vercel aesthetic, Light + Dark
5. **Never break upstream ai-hot structure** — our additions are namespaced under `my/`

---

## 🗺️ Architecture

```
sept-ai/
├── my-content/                  ◀── Obsidian Vault (open here)
│   ├── 00-Scraped/
│   │   ├── EN/  (Anthropic, OpenAI, DeepMind, Cursor, ArXiv, HN, Reddit ...)
│   │   └── CN/  (机器之心, 量子位, 知乎, ...)
│   ├── 01-Daily-Brief/   EN/  CN/
│   ├── 10-Tools/
│   ├── 20-Models/
│   ├── 30-Agents/
│   ├── 40-Providers/
│   ├── 50-My-Knowledge/
│   │   ├── Claude-Learning/   ← synced from Septoff21/claude-learning
│   │   ├── Prompts/
│   │   └── Workflows/
│   ├── 99-About-Me/    About · Projects · Support · Contact
│   └── .obsidian/
│
├── site/                        ◀── Hugo static site
│   ├── content/  (auto-synced from my-content/ + data/)
│   ├── layouts/
│   ├── assets/   (TNG QR, logos, ...)
│   └── hugo.toml
│
├── scripts/                     ◀── Python pipeline
│   ├── aggregate.py             orchestrator (inherited)
│   ├── sources/                 one file per source
│   ├── sync_claude_learning.py  pull Septoff21/claude-learning
│   ├── vault_writer.py          writes .md into my-content/
│   └── daily_brief.py           placeholder for Phase 8
│
├── data/                        ◀── JSON snapshots (auto-generated)
├── .github/workflows/
│   ├── aggregate.yml            cron every 6h
│   └── deploy.yml               push → Netlify
└── netlify.toml
```

---

## 👤 Identity

- **GitHub:** `septoff21`
- **Email:** `septoff21@gmail.com`
- **TNG QR:** `C:/dev/buymecoffee.png` → copied to `site/assets/tng-qr.png`

---

## 📋 Phase Checklist

### ✅ Phase 1 · Repo Setup
- [ ] Create empty repo `septoff21/sept-ai` on GitHub
- [ ] Fork/copy `ai-hot` contents → new local folder `sept-ai/`
- [ ] Remove original `.git`, reinit with new remote
- [ ] Replace `CNAME`, `LICENSE`, `README.md` (new English README)
- [ ] First push to `main`

### ✅ Phase 2 · Vault Skeleton
- [ ] Create `my-content/` directory tree (all 7 top-level folders)
- [ ] Copy `.obsidian/` config from existing vault (or fresh)
- [ ] Add `.gitignore` entries for Obsidian workspace files
- [ ] Add README inside vault explaining folder convention
- [ ] Seed `99-About-Me/About.md`, `Projects.md`, `Support.md`, `Contact.md`

### ✅ Phase 3 · Data Layer Refactor
- [ ] Create `scripts/vault_writer.py` — unified markdown writer
- [ ] Refactor `news_rss.py` to tag each item with `channel: en|cn` and write to `my-content/00-Scraped/{channel}/{source}/`
- [ ] Keep existing `data/*.json` for Hugo data layer (nav, tools, models)
- [ ] Add `scripts/sync_claude_learning.py` — git-clone Septoff21/claude-learning and copy to `50-My-Knowledge/Claude-Learning/`
- [ ] Run once locally to generate initial vault content

### ✅ Phase 4 · i18n (English UI)
- [ ] Translate `hugo.toml` title/description/keywords → English
- [ ] Rewrite nav menu (English labels + Lucide icons instead of emoji)
- [ ] Translate layout templates (`baseof.html`, `index.html`, `list.html`, `single.html`, etc.)
- [ ] Translate category labels in `tools.json` / `models.json`
- [ ] Add `languageCode = "en"` and keep CN as fallback for personal pages

### ✅ Phase 5 · UI Redesign (Claude Style)
- [ ] Design system tokens: colors (light/dark), spacing, typography (Inter + 思源)
- [ ] Implement theme toggle (top-right, localStorage, prefers-color-scheme)
- [ ] Rebuild navigation bar (clean horizontal layout)
- [ ] Redesign Home: hero + Trending section + Daily Brief slot + Me CTA
- [ ] Redesign Tools/Models/Agents cards
- [ ] Redesign News list (EN/CN tab switcher)
- [ ] Responsive + mobile hamburger menu
- [ ] Replace all emoji icons with Lucide SVG

### ✅ Phase 6 · Data Sources Expansion
**New EN sources (15):**
- [ ] Anthropic News (scrape)
- [ ] Anthropic Research (scrape)
- [ ] OpenAI Blog (RSS)
- [ ] Google DeepMind (RSS)
- [ ] Google AI Blog (RSS)
- [ ] Cursor Changelog (scrape)
- [ ] Microsoft AI Blog (RSS)
- [ ] Meta AI Blog (RSS)
- [ ] xAI News (scrape)
- [ ] ArXiv cs.AI (RSS)
- [ ] HuggingFace Papers (scrape)
- [ ] HuggingFace Blog (RSS)
- [ ] Simon Willison's Weblog (RSS)
- [ ] Latent Space (RSS)
- [ ] Product Hunt AI (API)

**New CN sources (5):**
- [ ] 掘金 AI
- [ ] 少数派
- [ ] 虎嗅
- [ ] 极客公园
- [ ] CSDN AI

**New Reddit subs:**
- [ ] r/ClaudeAI, r/OpenAI, r/singularity

### ✅ Phase 7 · Me Page
- [ ] Create `/me` route + layout template
- [ ] Profile card (avatar placeholder, bio, social links)
- [ ] Section: Claude Learning (from synced content)
- [ ] Section: Prompts & Tips
- [ ] Section: My Projects (replace old Compare)
- [ ] Section: Buy me a coffee button → Modal with TNG QR + contact
- [ ] Copy `C:/dev/buymecoffee.png` → `site/assets/tng-qr.png`
- [ ] Modal dismissable, keyboard accessible

### ✅ Phase 8 · Ship It
- [ ] Hide `/search` and `/compare` from nav (keep routes, no menu link)
- [ ] `netlify.toml` with Hugo build command
- [ ] Connect repo to Netlify → auto-deploy on push
- [ ] GitHub Actions `aggregate.yml` cron every 6h
- [ ] GitHub Actions `deploy.yml` on push (if not using Netlify CI)
- [ ] Daily brief placeholder page + cron (LLM integration deferred)
- [ ] Smoke test: local build → push → live site loads

---

## 🚫 Out of scope (for now)

- Paid LLM calls for Daily Brief (Phase 8+)
- Custom domain (use Netlify subdomain first)
- Mobile app / PWA
- Multi-author / comments
- Analytics (add Plausible later)

---

## 🔄 Update cadence

- Scrapers: every 6h (GitHub Actions cron)
- Daily Brief: daily 08:00 UTC (Phase 8+)
- Manual knowledge edits: anytime via Obsidian
