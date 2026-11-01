#!/usr/bin/env python3
"""The dashboard's copy of an open pack PR: docs/data/social/previews/<pack id>/ holds preview.json
(the posts' fields, pack.json, the checks) and the posts' images, so the page shows the posts as the
networks will without reading the PR through the API. The page holds no key and the repository may
be private; GitHub Pages (or the local copy) serves these files like the rest of the data.

social-pr.yml writes it after every review pass (pr_sync.review), intake.py when it opens the PR of
a post written on the dashboard, and social-on-merge.yml removes it when the PR is merged or closed.
"""
import json
import shutil
from pathlib import Path

from social import pack as packmod


def folder(root, pack_id):
    return Path(root) / "docs" / "data" / "social" / "previews" / pack_id


def collect(pack_dir, pr, result=None):
    """(preview data, {file name: bytes}) of a pack as its PR holds it. result: checks.run's, if known."""
    pack_dir = Path(pack_dir)
    p = packmod.load(pack_dir)
    images, files = {}, {}
    for post in p["meta"].get("posts", []):
        pid = post["post_id"]
        if pid not in p["posts"]:
            continue                                         # deleted in the PR
        names = [v["file"] for v in post.get("visuals") or [] if (pack_dir / "visuals" / v["file"]).is_file()]
        images[pid] = names
        files.update({n: (pack_dir / "visuals" / n).read_bytes() for n in names})
    fixes = []
    if result is not None:
        fixes = [f"{pid} · {r['check']}: {r['detail']}" for pid, rs in result.get("posts", {}).items() for r in rs if not r["ok"]]
        fixes += [f"pack · {r['check']}: {r['detail']}" for r in result.get("pack", []) if not r["ok"]]
    head = pr.get("head") or {}
    data = {"pack_id": p["meta"]["pack_id"],
            "pr": {"number": pr.get("number"), "title": pr.get("title", ""), "html_url": pr.get("html_url", ""),
                   "state": "open", "merged": False, "head": {"ref": head.get("ref", ""), "sha": head.get("sha", "")}},
            "meta": p["meta"], "posts": {pid: {"fields": f} for pid, f in p["posts"].items()}, "images": images,
            "checks": None if result is None else {"state": "success" if result["ok"] else "failure",
                                                   "text": "all checks pass" if result["ok"] else f"{len(fixes)} check(s) failing"},
            "fixes": fixes}
    return data, files


def write(root, data, files):
    """The preview folder of a pack, written afresh. Returns the folder."""
    d = folder(root, data["pack_id"])
    if d.exists():
        shutil.rmtree(d)
    d.mkdir(parents=True)
    (d / "preview.json").write_bytes((json.dumps(data, ensure_ascii=False, indent=1) + "\n").encode("utf-8"))
    for name, raw in files.items():
        (d / Path(name).name).write_bytes(raw)
    return d


def remove(root, pack_id):
    d = folder(root, pack_id)
    if d.exists():
        shutil.rmtree(d)
        return True
    return False
