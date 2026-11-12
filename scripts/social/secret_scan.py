#!/usr/bin/env python3
"""Key leak scan (product spec I1; tech spec flow 14).

    python3 scripts/social/secret_scan.py <file or folder> […]       # scan files
    git diff <range> | python3 scripts/social/secret_scan.py -        # scan a diff on stdin

Looks for Google keys (AIza…), GitHub tokens (ghp_, gho_, ghs_, github_pat_), private key
headers and Cloudflare tunnel tokens (eyJhIjoi…), and — in the guest — the exact values of its
own secrets (named in SOCIAL_SECRET_ENV_NAMES, read from the environment). A finding names the
kind of key and where it is, never its value. Exit 1 on any finding.
"""
import os
import re
import sys
from pathlib import Path

PATTERNS = {
    "google-api-key": re.compile(r"AIza[0-9A-Za-z_\-]{35}"),
    "github-token": re.compile(r"\b(?:ghp|gho|ghs|ghu|ghr)_[0-9A-Za-z]{36}\b"),
    "github-pat": re.compile(r"\bgithub_pat_[0-9A-Za-z_]{60,}\b"),
    "private-key": re.compile(r"-----BEGIN (?:[A-Z]+ )?PRIVATE KEY-----"),
    "cloudflare-tunnel-token": re.compile(r"\beyJhIjoi[0-9A-Za-z_\-]{20,}"),
}
# Which work stops when a key of that kind leaks (flow 14).
STOPS = {"postiz-key": "all hand-overs", "github-app-key": "all hand-overs", "social-gemini-key": "drafting",
         "cloudflare-tunnel-token": "nothing (rotate the tunnel token)"}


def scan_text(text, where="text", own_secrets=None):
    """[{kind, where, line}] — never the value."""
    found = []
    for n, line in enumerate(str(text or "").splitlines(), 1):
        for kind, rx in PATTERNS.items():
            if rx.search(line):
                found.append({"kind": kind, "where": where, "line": n})
        for name, value in (own_secrets or {}).items():
            if value and len(value) >= 8 and value in line:
                found.append({"kind": name, "where": where, "line": n})
    return found


def own_secrets_from_env():
    """{name: value} of the guest's own secrets, by the env var names listed in
    SOCIAL_SECRET_ENV_NAMES (comma-separated, e.g. POSTIZ_API_KEY,WEBPORTALS_READ_TOKEN)."""
    names = [n.strip() for n in os.environ.get("SOCIAL_SECRET_ENV_NAMES", "").split(",") if n.strip()]
    return {n.lower().replace("_", "-"): os.environ.get(n, "") for n in names}


def scan_paths(paths, own=None):
    found = []
    for p in paths:
        p = Path(p)
        files = [f for f in p.rglob("*") if f.is_file()] if p.is_dir() else [p]
        for f in files:
            if ".git" in f.parts or f.suffix.lower() in (".jpg", ".jpeg", ".png", ".webp", ".ttf", ".woff2", ".svg"):
                continue
            try:
                text = f.read_text(encoding="utf-8")
            except (UnicodeDecodeError, OSError):
                continue
            found += scan_text(text, str(f), own)
    return found


def main(argv=None):
    args = list(sys.argv[1:] if argv is None else argv)
    own = own_secrets_from_env()
    if not args or args == ["-"]:
        found = scan_text(sys.stdin.read(), "stdin", own)
    else:
        found = scan_paths(args, own)
    for f in found:
        print(f"key found: {f['kind']} in {f['where']} line {f['line']}")
    if not found:
        print("no key found")
    return 1 if found else 0


if __name__ == "__main__":
    sys.exit(main())
