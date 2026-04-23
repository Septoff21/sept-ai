#!/usr/bin/env python3
"""
backfill_vault.py — one-shot: rewrite every item in data/news.json as a
markdown file into the vault. Useful after a fresh clone to populate
my-content/00-Scraped/ without waiting for multiple scraper cycles.

Usage:
    python scripts/backfill_vault.py
"""

import json
from pathlib import Path

from vault_writer import write_news_batch

REPO_ROOT = Path(__file__).resolve().parent.parent
NEWS_PATH = REPO_ROOT / "data" / "news.json"


def main() -> None:
    if not NEWS_PATH.exists():
        print(f"⚠️ {NEWS_PATH} not found — run the scrapers first.")
        return

    items = json.loads(NEWS_PATH.read_text(encoding="utf-8"))
    print(f"📂 Loaded {len(items)} items from news.json")

    # Ensure every item has a channel (lang → channel fallback handled in vault_writer)
    stats = write_news_batch(items)
    print(
        f"✅ Backfill complete: wrote {stats['written']} md files "
        f"({stats['en']} EN / {stats['cn']} CN, skipped {stats['skipped']})"
    )


if __name__ == "__main__":
    main()
