# Sept-AI · Your AI Navigator & Knowledge Hub

> **Discover. Learn. Build.** — A curated, auto-updating directory of AI tools, models, agents, and news — paired with a personal knowledge vault.

<p align="center">
  <a href="https://github.com/Septoff21/sept-ai/actions"><img src="https://img.shields.io/badge/updates-every%206h-brightgreen" alt="Auto-updated every 6h"></a>
  <a href="https://github.com/Septoff21/sept-ai/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue" alt="MIT License"></a>
  <a href="#"><img src="https://img.shields.io/badge/site-sept--ai.netlify.app-black" alt="Live Site"></a>
  <img src="https://img.shields.io/badge/built%20with-Hugo%20%7C%20Python-orange" alt="Built with Hugo and Python">
</p>

---

## 🌐 What is Sept-AI?

**Sept-AI** is a personal, open-source navigation site for everything happening in AI. It aggregates from 30+ English sources and 14+ Chinese sources every 6 hours, organizes them into a searchable, browsable catalog, and layers a personal knowledge vault on top — built on the idea that *tools + knowledge = leverage*.

### Two layers, one site

| Layer | What it is | Who maintains it |
|---|---|---|
| **🧭 Navigator** | Trending news · Tools · Models · Agents · Providers | Auto-aggregated by Python pipeline |
| **👤 Me** | Claude Learning · Prompts · Workflows · Projects | Hand-written notes (Obsidian vault) |

Both layers read from the **same Obsidian vault** at `my-content/`, so local editing, graph view, and backlinks just work.

---

## ✨ Features

- 🔥 **Trending** — Hot items across EN & CN AI communities, updated every 6 hours
- 🛠️ **Tools Directory** — 170+ curated AI applications with use cases & alternatives
- 🧠 **Models Registry** — LLMs, diffusion, multimodal — tracked from HuggingFace & OpenRouter
- 🤖 **Agents** — Autonomous AI systems, frameworks, dev tools
- 📰 **Dual-channel News** — English (Anthropic, OpenAI, DeepMind, ArXiv, Cursor, …) + Chinese (机器之心, 量子位, 知乎热榜, …)
- 🏢 **Providers** — 20+ model API providers with pricing & modality info
- ☀️ **Daily Brief** *(coming in Phase 8)* — AI-generated daily summary in EN & CN
- 👤 **Me Page** — Personal knowledge: Claude learning, prompt library, projects, contact
- 🌗 **Light & Dark** themes · **Responsive** · **Obsidian-native** data

---

## 🏗️ Architecture

```
sept-ai/
├── my-content/                 ◀── Obsidian Vault (single source of truth)
│   ├── 00-Scraped/{EN,CN}/     auto-written by scrapers
│   ├── 01-Daily-Brief/         AI-summarized daily digest
│   ├── 10-Tools/ 20-Models/ 30-Agents/ 40-Providers/
│   ├── 50-My-Knowledge/        Claude-Learning · Prompts · Workflows
│   └── 99-About-Me/            About · Projects · Support · Contact
│
├── site/                       ◀── Hugo static site
├── scripts/                    ◀── Python aggregation pipeline
├── data/                       ◀── JSON snapshots for Hugo
└── .github/workflows/          ◀── cron every 6h + auto-deploy
```

### Data flow

```
  GitHub Actions (cron 0 */6 * * *)
         │
         ▼
  scripts/aggregate.py
         │
         ├─ EN scrapers  ──►  my-content/00-Scraped/EN/{source}/
         ├─ CN scrapers  ──►  my-content/00-Scraped/CN/{source}/
         └─ sync_claude_learning.py ──►  my-content/50-My-Knowledge/Claude-Learning/
         │
         ▼
  commit + push ──► Netlify builds Hugo ──► live site
```

---

## 🚀 Quick start

### Prerequisites

- **Hugo Extended** ≥ 0.128 — `winget install Hugo.Hugo.Extended`
- **Python** ≥ 3.11
- **Git**

### Local dev

```bash
git clone https://github.com/Septoff21/sept-ai.git
cd sept-ai

# 1. Install Python deps
pip install -r scripts/requirements.txt

# 2. Run the aggregator once (takes ~1-2 min)
python scripts/aggregate.py

# 3. Sync data → site
cp -r data/* site/data/

# 4. Start Hugo dev server
cd site && hugo server --bind 0.0.0.0 --port 1313
```

Open **http://localhost:1313**.

---

## 📡 Data sources

### 🇬🇧 English channel (30 sources)

**Official AI labs:** Anthropic News · Anthropic Research · OpenAI Blog · Google DeepMind · Google AI Blog · Microsoft AI Blog · Meta AI · xAI

**Dev tools:** Cursor Changelog · HuggingFace Blog · HuggingFace Papers

**Research:** ArXiv cs.AI · Simon Willison's Weblog · Latent Space

**Media:** TechCrunch AI · The Verge AI · MIT Tech Review · Ars Technica · VentureBeat AI

**Community:** Hacker News · Reddit (r/ClaudeAI · r/OpenAI · r/MachineLearning · r/LocalLLaMA · r/artificial · r/singularity) · Product Hunt AI

**Discovery:** GitHub Trending · HuggingFace Models · OpenRouter

### 🇨🇳 Chinese channel (14 sources · personal)

机器之心 · 量子位 · 新智元 · 36氪 · InfoQ AI · 掘金 AI · 少数派 · 虎嗅 · 极客公园 · CSDN AI · V2EX · 知乎热榜 · 微博热搜 · 百度热词

---

## 🗺️ Roadmap

See [PLAN.md](./PLAN.md) for the full phase checklist.

- [x] Phase 0 — Project scaffolding (fork + local setup)
- [ ] **Phase 1 — Repo setup** *(in progress)*
- [ ] Phase 2 — Vault skeleton
- [ ] Phase 3 — Data layer refactor (EN/CN split)
- [ ] Phase 4 — English UI (i18n)
- [ ] Phase 5 — UI redesign (Claude-style · Light/Dark)
- [ ] Phase 6 — Expand data sources (+20 sources)
- [ ] Phase 7 — Me page + Buy-me-a-coffee
- [ ] Phase 8 — Ship + SEO (Netlify deploy · sitemap · OpenGraph · schema.org)

---

## 🔍 SEO & discoverability

Sept-AI is built to be findable:

- Per-page `<title>` and `<meta description>` tuned for each tool/model/news item
- OpenGraph + Twitter Card tags
- `schema.org/SoftwareApplication` JSON-LD for tools
- Auto-generated `sitemap.xml` + `robots.txt`
- RSS feed at `/index.xml`
- Hugo-minified HTML with Lighthouse-friendly defaults

---

## 🛠️ Tech stack

| Layer | Tech |
|---|---|
| Static site generator | [Hugo](https://gohugo.io/) (extended) |
| Data pipeline | Python 3.11 — feedparser, requests, trafilatura, beautifulsoup4 |
| Knowledge vault | [Obsidian](https://obsidian.md/) — markdown + backlinks + graph view |
| CI / Cron | GitHub Actions |
| Hosting | Netlify (free tier) |
| Fonts | Inter + Source Han Sans (思源黑体) |
| Icons | Lucide |

---

## 🙏 Credits

This project was originally forked from **[laolaoshiren/ai-hot](https://github.com/laolaoshiren/ai-hot)** — a Chinese AI aggregation site — and has been substantially refactored, internationalized, redesigned, and extended with a personal knowledge vault. Huge thanks to the original author for the solid foundation.

---

## ☕ Support

If Sept-AI saves you time, you can [buy me a coffee](#) via TNG or reach out at **septoff21@gmail.com**.

---

## 📄 License

[MIT](./LICENSE) · Copyright © 2026 Septoff21
