# Sept-AI · V2 Design System & Phase Plan

> **Author:** Claude (Design lead) + Septoff21 (Product)  
> **Goal:** Make sept-ai.netlify.app beautiful, fast, and useful — the AI navigator you actually want open every day.  
> **Constraint:** 100% free stack, no JS frameworks, Hugo templates only.  
> **Last updated:** 2026-04

---

## 🎨 Design Philosophy

**Three words:** Clean · Alive · Personal

| Principle | What it means |
|---|---|
| **Clean** | Every element earns its place. No decorative noise. If you can remove it and not notice, it's gone. |
| **Alive** | The site should feel like it just updated. Live indicators, timestamps, fresh data signals. |
| **Personal** | This is Septoff21's navigator, not a generic directory. Voice, personality, and real tool choices visible. |

---

## 🎨 Design Tokens (established in V1, maintained)

```css
/* Dark (default) */
--bg:      #1a1817   /* warm near-black, not cold gray */
--bg2:     #242220   /* cards */
--bg3:     #2e2b29   /* subtle surfaces */
--text:    #e8e3dc   /* warm white */
--text2:   #a09990   /* secondary */
--text3:   #635c56   /* muted */
--accent:  #cc785c   /* amber — primary CTA */
--border:  #38332e

/* Light */
--bg:      #faf9f6   /* warm off-white */
--accent:  #b5603f

/* Neon accents (borders, highlights) */
--neon-amber:  #cc785c
--neon-violet: #7c3aed
--neon-cyan:   #06b6d4
--neon-green:  #10b981
```

**Typography:**  
System stack: `-apple-system, BlinkMacSystemFont, "Inter", "Segoe UI", "Noto Sans SC", sans-serif`  
No custom font load = zero CLS, zero network cost.

**Icons:** Lucide (CDN, ~5kb gzip). All icons via `data-lucide` attribute.

---

## 📐 Layout System

```
Header (sticky, 56px)
├── Logo + "Updated every 6h"
├── Nav (Trending · Tools · Models · Agents · News · Providers · Daily · Me)
└── Theme toggle + Streak badge

Neon gradient divider (2px, amber→violet→cyan)

Main (max-width: 1200px, padding: 0 20px)
├── [Page-specific content]
└── Grid: 1fr 330px (collapses to 1fr on mobile < 768px)

Footer
├── "SEPT-AI — AI navigator, refreshed every 6h"
└── Nav links: Home · Tools · Models · News · Me · GitHub
```

---

## ✅ V2.1 — Homepage Redesign (DONE — 2026-04-27)

**What changed:**
- Replaced hidden `<h1>` SEO hack with stat bar
- Stat bar: live green pulse dot + tool/model/article counts
- "Where to start?" → 3-column quick-access with Lucide icons
- Trending: added "All news →" shortcut, cleaner meta row
- News: hover-highlight rows with AI summary preview
- Sidebar: removed 4 noise widgets (Share, Random, Check-in, Recently Added)
- Sidebar Browse: compact list with counts
- Footer: two-line, proper nav links
- Search: better styling, position:relative for dropdown

**Before vs After sidebar count:** 9 cards → 5 cards

---

## 📋 V2.2 — Tools Page (NEXT)

**Current state:** Tools page shows a grid of cards, basic filter by category via URL.

**Target:**
```
Tools (170+)
├── [Search bar — pre-filled from ?q=]
├── [Category filter bar — horizontal pill tabs]
│    All · Coding · Writing · Image · Video · Audio · Research · Productivity
├── [Sort: Trending | New | Free first | A-Z]
└── [Grid: 3 col → 2 col → 1 col]
     ┌─────────────────────┐
     │ [Icon] Name    🔥HOT│
     │ Description text    │
     │ Pricing · Tags      │
     └─────────────────────│

```

**Specific changes:**
- [ ] Add category pill filter tabs (JS, no reload)
- [ ] Add sort controls (trending / free / alphabetical)
- [ ] Tool card: show free-tier badge in green when available
- [ ] Tool card: "HOT" badge visible on trending tools
- [ ] "No results" empty state when filter returns 0
- [ ] Count badge on each category tab ("Coding (42)")
- [ ] Mobile: 1 col, filter tabs scroll horizontally

---

## 📋 V2.3 — News Page

**Current state:** Long flat list, pagination at bottom.

**Target:**
```
News
├── [EN | CN | All] tab switcher
├── [Source filter: All · Anthropic · OpenAI · HuggingFace · ...]
└── News cards (not rows):
    ┌──────────────────────────────┐
    │ SOURCE · 2h ago              │
    │ Article title (2 lines max)  │
    │ AI Summary (1 line)          │
    │ [Read →]                     │
    └──────────────────────────────┘
```

**Specific changes:**
- [ ] EN/CN/All tab switcher (JS filter on `channel` field)
- [ ] Source badge with distinct color per major source
- [ ] Card grid (not flat list): 2-col on desktop
- [ ] AI summary shown on card if available
- [ ] Pinned "must-read" row for top 3 items

---

## 📋 V2.4 — Models Page

**Current state:** Table/list of models with basic info.

**Target:**
```
Models
├── [Filter: All · Text · Code · Vision · Multimodal]
├── [Provider: All · Anthropic · OpenAI · Google · Meta ...]
└── Model cards:
    ┌─────────────────────────────┐
    │ [Provider logo] Model name  │
    │ Provider · Context window   │
    │ ████████ Quality score      │
    │ Free / Paid / API           │
    └─────────────────────────────┘
```

**Specific changes:**
- [ ] Capability filter tabs
- [ ] Context window shown
- [ ] "Best for coding / writing / reasoning" label
- [ ] Provider color coding

---

## 📋 V2.5 — Daily Page

**Current state:** Placeholder "coming soon" + latest news fallback.

**Target:** A single-page daily digest:
```
Daily Brief — 2026-04-27
━━━━━━━━━━━━━━━━━━━━━━━━

🔥 Top 5 Stories Today
   [numbered list with summaries]

🛠 Tool of the Day
   [spotlight card]

📈 What's Rising
   [3 trending tools]

📊 This Week in Numbers
   N new tools · N articles · N models updated
```

**Specific changes:**
- [ ] Read from `data/briefing.json` + `data/daily.json`
- [ ] Fallback gracefully if data not populated yet
- [ ] Mobile-first layout (single column)

---

## 📋 V2.6 — Navigation & Mobile

**Current state:** Nav is functional but collapses to icon-only on mobile.

**Target:**
- [ ] Mobile: hamburger menu (pure CSS, no JS required)
- [ ] Active page highlight more visible
- [ ] "New" dot on nav items when section has updates since last visit (localStorage)
- [ ] Keyboard navigation (already have Ctrl+K for search)

---

## 📋 V2.7 — Me Page Polish

**Current state:** Full content populated (2026-04-27).

**Improvements:**
- [ ] Add a "Now" section: what I'm currently working on / reading
- [ ] Skill/tech visual (simple icon row, not just tags)
- [ ] Link to openclaw-newbie-baseline with live status badge
- [ ] Add actual avatar/photo if user wants

---

## 📋 V2.8 — Performance & SEO Audit

- [ ] Lighthouse score target: 90+ Performance, 95+ Accessibility
- [ ] Add `loading="lazy"` to all images
- [ ] Verify all pages have unique `<title>` and `<meta description>`
- [ ] Check Open Graph images on all key pages
- [ ] Add Plausible Analytics (privacy-first, free for low traffic)
- [ ] Verify sitemap covers all pages

---

## 🗓 Execution Order

| Priority | Phase | Effort | Impact |
|---|---|---|---|
| 1 | V2.2 Tools page | Medium | ⭐⭐⭐⭐ High (most-visited page) |
| 2 | V2.3 News page | Medium | ⭐⭐⭐⭐ High (daily content) |
| 3 | V2.5 Daily page | Low | ⭐⭐⭐ Medium (signature feature) |
| 4 | V2.4 Models page | Medium | ⭐⭐⭐ Medium |
| 5 | V2.6 Mobile nav | Low | ⭐⭐⭐ Medium |
| 6 | V2.7 Me polish | Low | ⭐⭐ Low (personal) |
| 7 | V2.8 SEO/perf | Low | ⭐⭐ Low but long-term |

---

## 🔄 Update Cadence

- **V2.1** ✅ Done (2026-04-27)
- **V2.2** → Tools page (next session)
- **V2.3** → News page
- **Major review:** Monthly — check what's actually being used, drop what isn't

---

## 💡 Design Rules (for Claude to follow when building)

1. **No inline style soup for layout** — use CSS classes in baseof.html where possible
2. **Every card must have a hover state** — border-color change at minimum
3. **Sidebar max 5 cards** — enforce ruthlessly
4. **Mobile first for new components** — test at 375px width mentally
5. **Empty states always** — if data is missing, show a helpful placeholder
6. **No emoji as primary icons** — Lucide SVG preferred, emoji only for decorative flair
7. **Color = meaning** — amber=action, green=free/good, cyan=info, violet=special
8. **Links must be obvious** — either blue, accent, or underlined — never gray-on-gray
