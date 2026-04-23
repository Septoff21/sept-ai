"""
vault_writer.py — Unified markdown writer for Sept-AI's Obsidian vault.

Takes any scraped item (news, tool, model, etc.) and writes it as a
front-matter markdown file into `my-content/00-Scraped/{channel}/{source}/`.

Design goals:
- Idempotent: same item on re-run → same filename, overwrites cleanly
- Safe filenames: ASCII-slug with short hash suffix to avoid collisions
- Obsidian-friendly: YAML front-matter + clean body, WikiLinks where sensible
- Preserves existing JSON pipeline: vault write is additive, never replaces
"""

from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

# Resolve repo root relative to this file so it works in CI and local
REPO_ROOT = Path(__file__).resolve().parent.parent
VAULT_ROOT = REPO_ROOT / "my-content"
SCRAPED_DIR = VAULT_ROOT / "00-Scraped"

# lang → channel folder name
LANG_TO_CHANNEL = {
    "en": "EN",
    "zh": "CN",
    "cn": "CN",
}

# Map source display names to vault sub-folder names.
# If a source isn't in this table it falls back to a sanitized version of the raw name.
SOURCE_FOLDER_MAP = {
    # English
    "Hacker News": "HackerNews",
    "Hacker News AI": "HackerNews",
    "r/MachineLearning": "Reddit",
    "r/LocalLLaMA": "Reddit",
    "r/artificial": "Reddit",
    "r/ClaudeAI": "Reddit",
    "r/OpenAI": "Reddit",
    "r/singularity": "Reddit",
    "TechCrunch AI": "Media",
    "The Verge AI": "Media",
    "MIT Tech Review": "Media",
    "Ars Technica": "Media",
    "VentureBeat AI": "Media",
    # Chinese
    "V2EX": "V2EX",
    "机器之心": "机器之心",
    "量子位": "量子位",
    "新智元": "新智元",
    "36氪": "36氪",
    "InfoQ AI": "36氪",  # group tech media under 36氪-ish bucket for now
    "知乎热榜": "知乎热榜",
    "微博热搜": "微博热搜",
}


# ---------- helpers ----------

def _slugify(text: str, max_len: int = 60) -> str:
    """ASCII-safe slug. Preserves CJK by hashing when non-ASCII dominates."""
    if not text:
        return "untitled"
    # Normalize unicode
    nfkd = unicodedata.normalize("NFKD", text)
    ascii_only = nfkd.encode("ascii", "ignore").decode("ascii")
    # Lowercase, keep alnum and hyphens
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_only).strip("-").lower()
    if len(slug) < 3:
        # Mostly non-ASCII (likely Chinese) — use short hash
        h = hashlib.md5(text.encode("utf-8")).hexdigest()[:10]
        return f"item-{h}"
    return slug[:max_len].rstrip("-")


def _safe_folder_name(name: str) -> str:
    """Make a source name safe for use as a folder name on all OSes."""
    return re.sub(r'[<>:"/\\|?*]+', "-", name).strip() or "unknown"


def _yaml_escape(value: Any) -> str:
    """Minimal YAML string escaper for front-matter values."""
    if value is None:
        return '""'
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, list):
        return "[" + ", ".join(_yaml_escape(v) for v in value) + "]"
    s = str(value).replace("\\", "\\\\").replace('"', '\\"')
    # Strip newlines/CRs which break YAML strings
    s = s.replace("\n", " ").replace("\r", " ").strip()
    return f'"{s}"'


def _front_matter(fields: dict[str, Any]) -> str:
    lines = ["---"]
    for k, v in fields.items():
        if v is None or v == "":
            continue
        lines.append(f"{k}: {_yaml_escape(v)}")
    lines.append("---")
    return "\n".join(lines)


# ---------- public API ----------

def write_news_item(item: dict[str, Any]) -> Path | None:
    """
    Write one news item to the vault as a markdown file.

    Expected item keys (all optional except title + source):
      id, title, url, source, lang, channel, published, summary,
      collected_at, priority, points, tags

    Returns the path written, or None if skipped (e.g. missing required keys).
    """
    title = (item.get("title") or "").strip()
    source = (item.get("source") or "").strip()
    if not title or not source:
        return None

    # Derive channel from lang if not provided
    channel = item.get("channel")
    if not channel:
        lang = (item.get("lang") or "").lower()
        channel = LANG_TO_CHANNEL.get(lang, "EN")
    channel = channel.upper()

    # Resolve source folder
    folder_name = SOURCE_FOLDER_MAP.get(source) or _safe_folder_name(source)
    dest_dir = SCRAPED_DIR / channel / folder_name
    dest_dir.mkdir(parents=True, exist_ok=True)

    # Filename: YYYY-MM-DD-slug-HASH.md
    date_str = (item.get("published") or item.get("collected_at") or datetime.now(timezone.utc).isoformat())[:10]
    slug = _slugify(title)
    short_id = (item.get("id") or hashlib.md5(title.encode("utf-8")).hexdigest())[:8]
    fname = f"{date_str}-{slug}-{short_id}.md"
    dest = dest_dir / fname

    # Build front-matter
    fm = {
        "title": title,
        "date": item.get("published") or item.get("collected_at"),
        "source": source,
        "source_url": item.get("url"),
        "channel": channel.lower(),
        "lang": item.get("lang"),
        "summary": item.get("summary"),
        "tags": item.get("tags") or ["news", channel.lower()],
        "priority": item.get("priority"),
        "points": item.get("points"),
    }
    body_parts = [_front_matter(fm), ""]
    summary = (item.get("summary") or "").strip()
    if summary and summary != title:
        body_parts.append(f"> {summary}\n")
    url = item.get("url")
    if url:
        body_parts.append(f"**Read more →** <{url}>\n")
    body_parts.append(f"*Collected by Sept-AI on {item.get('collected_at', '')}*")

    dest.write_text("\n".join(body_parts), encoding="utf-8")
    return dest


def write_news_batch(items: Iterable[dict[str, Any]]) -> dict[str, int]:
    """
    Write many items. Returns counts: {"written": N, "skipped": M, "en": X, "cn": Y}.
    """
    stats = {"written": 0, "skipped": 0, "en": 0, "cn": 0}
    for item in items:
        path = write_news_item(item)
        if path is None:
            stats["skipped"] += 1
            continue
        stats["written"] += 1
        channel_key = "en" if "/EN/" in str(path).replace("\\", "/") else "cn"
        stats[channel_key] += 1
    return stats


def write_raw_json_snapshot(name: str, data: Any) -> Path:
    """
    Also mirror the final aggregated JSON into the vault for reference.
    Written to my-content/00-Scraped/_snapshots/{name}.json
    """
    snap_dir = SCRAPED_DIR / "_snapshots"
    snap_dir.mkdir(parents=True, exist_ok=True)
    dest = snap_dir / f"{name}.json"
    dest.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return dest


# ---------- CLI test ----------

if __name__ == "__main__":
    sample = {
        "id": "test1234",
        "title": "Claude Opus 4.6 released — doubled context length",
        "url": "https://www.anthropic.com/news/claude-opus-4-6",
        "source": "Anthropic",
        "lang": "en",
        "published": datetime.now(timezone.utc).isoformat(),
        "summary": "Anthropic announced Claude Opus 4.6 with 2x context and better reasoning.",
        "collected_at": datetime.now(timezone.utc).isoformat(),
    }
    p = write_news_item(sample)
    print(f"Wrote: {p}")
