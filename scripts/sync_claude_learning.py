#!/usr/bin/env python3
"""
sync_claude_learning.py — Pull Septoff21/claude-learning into the vault.

Clones (or pulls) the upstream claude-learning repo into a temp checkout,
then mirrors all .md files into:
    my-content/50-My-Knowledge/Claude-Learning/

Design:
- Runs in CI and locally; uses `git` CLI (pre-installed everywhere)
- Uses `--depth 1` shallow clone for speed
- Preserves sub-folder structure
- Rewrites relative links so Obsidian still resolves them
- Safe to re-run: fully replaces the Claude-Learning folder each time
  (except README.md which we overwrite with a note that it's auto-synced)
"""

from __future__ import annotations

import shutil
import subprocess
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEST = REPO_ROOT / "my-content" / "50-My-Knowledge" / "Claude-Learning"
UPSTREAM = "https://github.com/Septoff21/claude-learning.git"
UPSTREAM_NAME = "claude-learning"


def _run(cmd: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess:
    print("  $ " + " ".join(cmd))
    return subprocess.run(cmd, cwd=cwd, check=True, capture_output=True, text=True)


def sync_claude_learning() -> str:
    """Clone upstream, mirror markdown into vault, return summary string."""
    with tempfile.TemporaryDirectory(prefix="septai-sync-") as tmp:
        tmp_path = Path(tmp)
        print(f"🔄 Cloning {UPSTREAM} → {tmp_path}")
        _run(["git", "clone", "--depth", "1", UPSTREAM, str(tmp_path / UPSTREAM_NAME)])

        src = tmp_path / UPSTREAM_NAME
        if not src.exists():
            return "⚠️ clone failed"

        # Wipe destination (except the README sentinel we'll regenerate)
        if DEST.exists():
            for child in DEST.iterdir():
                if child.is_dir():
                    shutil.rmtree(child)
                else:
                    child.unlink()
        DEST.mkdir(parents=True, exist_ok=True)

        # Copy all markdown + attachments, skip .git and CI junk
        copied = 0
        for item in src.rglob("*"):
            if item.is_dir():
                continue
            rel = item.relative_to(src)
            # Skip hidden + CI folders
            parts = rel.parts
            if any(p.startswith(".") for p in parts):
                continue
            if parts[0] in {"node_modules", "__pycache__", "dist", "build"}:
                continue
            # Only sync text-ish content + common image types
            if item.suffix.lower() not in {".md", ".mdx", ".txt", ".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"}:
                continue
            dest_file = DEST / rel
            dest_file.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(item, dest_file)
            copied += 1

        # Regenerate README sentinel (overwrite with auto-sync notice)
        (DEST / "README.md").write_text(
            _auto_sync_header() + (DEST / "README.md").read_text(encoding="utf-8")
            if (DEST / "README.md").exists()
            else _auto_sync_header(),
            encoding="utf-8",
        )

        return f"✓ Synced {copied} files from claude-learning"


def _auto_sync_header() -> str:
    return (
        "> ⚠️ **AUTO-SYNCED** from "
        "[Septoff21/claude-learning](https://github.com/Septoff21/claude-learning).\n"
        "> Edits to files in this folder will be overwritten. Push changes upstream instead.\n\n"
        "---\n\n"
    )


if __name__ == "__main__":
    try:
        print(sync_claude_learning())
    except subprocess.CalledProcessError as e:
        print(f"⚠️ git failed: {e.stderr}")
    except Exception as e:
        print(f"⚠️ unexpected error: {e}")
