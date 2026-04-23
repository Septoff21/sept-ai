# Sept-AI · Content Vault

> This folder is an **Obsidian vault**. Open it in Obsidian to get graph view, backlinks, and markdown editing.

## Folder convention

| Folder | Purpose | Who writes here |
|---|---|---|
| `00-Scraped/EN/` | English news & articles, organized by source | 🤖 Scrapers only |
| `00-Scraped/CN/` | Chinese news, by source | 🤖 Scrapers only |
| `01-Daily-Brief/` | AI-generated daily digest (EN + CN) | 🤖 LLM summarizer |
| `10-Tools/` | AI tools catalog (auto + curated) | 🤖 + ✍️ hybrid |
| `20-Models/` | LLMs & model families | 🤖 + ✍️ hybrid |
| `30-Agents/` | Autonomous AI systems | 🤖 + ✍️ hybrid |
| `40-Providers/` | API / model providers | 🤖 |
| `50-My-Knowledge/` | Personal notes, prompts, workflows | ✍️ You |
| `99-About-Me/` | About · Projects · Support · Contact pages | ✍️ You |

## Editing rules

1. **Never edit files under `00-Scraped/` or `01-Daily-Brief/`** — they get overwritten every 6 hours. If you want to capture a thought, copy it to `50-My-Knowledge/`.
2. Use `[[WikiLinks]]` freely — Hugo will render them as internal links during build.
3. Put images in `50-My-Knowledge/attachments/` (Obsidian's default folder).
4. Front-matter is optional for personal notes. For scraped content, the pipeline auto-writes YAML front-matter (title, date, source, tags, lang).

## Front-matter schema

```yaml
---
title: "Claude Opus 4.6 released"
date: 2026-04-23T14:00:00Z
source: "Anthropic"
source_url: "https://www.anthropic.com/news/..."
channel: en              # en | cn
tags: [claude, anthropic, release]
summary: "One-line summary here."
---
```
