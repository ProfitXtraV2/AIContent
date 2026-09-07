#!/usr/bin/env python3
"""External cross-model AI-pattern check via the Gemini API.

Reads GEMINI_API_KEY (and optional GEMINI_MODEL) from the environment. Sends the finished
article to Gemini with the Step-7 prompt and prints Gemini's raw verdict + recommendations
to stdout. The caller (daily-run.md Step 7) reads the verdict, decides whether to apply the
recommendations through a fresh Humaniser pass, and re-checks.

Usage:  python3 scripts/gemini_check.py <article_file> [model]
Exit:   0 = ok (verdict on stdout) · 2 = unavailable/error (caller falls back to skip)

stdlib-only (urllib) so no pip is needed in the cloud image.
"""
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

# Endpoint/model confirmed by the validation run (see scripts/GEMINI_ENDPOINT.md).
DEFAULT_MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.5-pro")
API_TMPL = "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"

PROMPT_FILE = Path(__file__).resolve().parents[1] / \
    "VsichkiKazina/pipeline/prompts/step-7-gemini-check.md"


def _prompt():
    """Extract the verbatim PROMPT block from the Step-7 prompt file."""
    text = PROMPT_FILE.read_text(encoding="utf-8")
    marker = "## PROMPT (verbatim"
    if marker in text:
        body = text.split(marker, 1)[1].split("\n", 1)[1]
        body = body.split("## Accept / iterate", 1)[0]
        return body.strip()
    return ("Act as a senior copywriter with deep knowledge of LLM writing patterns and "
            "AI-generated text detection. Evaluate whether the article reads as AI-written; "
            "give a verdict with confidence, flag exact passages/patterns, and give concrete "
            "recommendations. Do not change facts, do not rewrite it yourself, do not touch "
            "responsible-gambling language, disclosures, 18+ markers, or [VERIFY] flags.")


def main():
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        print("GEMINI_UNAVAILABLE: GEMINI_API_KEY not set", file=sys.stderr)
        return 2
    if len(sys.argv) < 2:
        print("usage: gemini_check.py <article_file> [model]", file=sys.stderr)
        return 2
    model = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_MODEL
    article = Path(sys.argv[1]).read_text(encoding="utf-8")

    url = API_TMPL.format(model=model)
    payload = json.dumps({
        "contents": [{"parts": [{"text": _prompt() + "\n\n---ARTICLE---\n\n" + article}]}],
        "generationConfig": {"temperature": 0.2},
    }).encode("utf-8")
    req = urllib.request.Request(
        url, data=payload,
        headers={"Content-Type": "application/json", "x-goog-api-key": key},
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.load(resp)
        print(data["candidates"][0]["content"]["parts"][0]["text"])
        return 0
    except urllib.error.HTTPError as e:
        print(f"GEMINI_ERROR: HTTP {e.code} {e.read()[:300]!r}", file=sys.stderr)
        return 2
    except Exception as e:  # noqa: BLE001 — any failure → caller falls back to skip
        print(f"GEMINI_ERROR: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
