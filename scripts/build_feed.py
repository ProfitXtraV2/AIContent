#!/usr/bin/env python3
"""Build the generic published/ feed from approved articles. Deterministic, stdlib-only.

Reads VsichkiKazina/content-queue.md, selects status: approved rows, pulls each article's
final files from its content/<folder> git branch, and writes published/<slug>/ + index.json.
Run from repo root:  python3 scripts/build_feed.py
"""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_dashboard as bd  # reuse parse_queue

AUTHOR = "Георги Тодоров"
SCHEMA_VERSION = 1
ARTICLES_DIR = "VsichkiKazina/articles"


def slug_from_folder(folder):
    """Article slug = folder with any leading YYYY-MM-DD- stripped."""
    return re.sub(r"^\d{4}-\d{2}-\d{2}-", "", folder.strip())
