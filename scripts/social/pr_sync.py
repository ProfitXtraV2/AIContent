#!/usr/bin/env python3
"""What the social PR workflows do (tech spec flow 2 and flow 3).

    python3 scripts/social/pr_sync.py review <pr number> --pr-dir <PR head checkout>
    python3 scripts/social/pr_sync.py redo <pr number> --comment-id <id>
    python3 scripts/social/pr_sync.py merged <pr number>

Runs from the main checkout: the scripts and the settings, library and operator list are main's;
the PR's files are read from --pr-dir as data and nothing in them is ever run.

review (social-pr.yml, on every push to the PR):
  1. The review view replaces the PR description (edits made there are overwritten, AC 38). The
     English references are the drafting agent's, in the pack; nothing here translates.
  2. The checks run on the head commit: commit status `social-checks`, and one sticky comment.
redo (on a `/redo` comment): the PR is labelled "redo requested" for the dashboard; the next
  drafting run does the redo.
merged (social-on-merge.yml, PR closed): the checks again on the merged files, a comment with
  the result and "not approved" when someone without write access (or a bot) merged; the registry row becomes
  merged or closed; the dashboard data is rebuilt.

Environment: GITHUB_TOKEN (Actions), GITHUB_REPOSITORY.
"""
import argparse
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from social import (board, brands, checks, github, ids, pack as packmod, preview_export, review_view,  # noqa: E402
                    settings as settingsmod)

MARKER = "<!-- social-checks -->"
BRAND_OF_DIR = {b["dir"]: k for k, b in brands.BRANDS.items()}


def packs_in(files):
    """[(brand, pack folder relative path)] the PR touches."""
    out = []
    for f in files:
        parts = Path(f).parts
        if len(parts) >= 4 and parts[1] == "social" and parts[2] == "packs" and parts[0] in BRAND_OF_DIR:
            item = (BRAND_OF_DIR[parts[0]], "/".join(parts[:4]))
            if item not in out:
                out.append(item)
    return out


def review(gh, number, pr_dir, root=brands.ROOT, preview_root=None):
    """One pass of flow 2 for a pack or fix PR. preview_root: the main checkout to write the
    dashboard's preview of the pack into (preview_export.py). Returns {pack_id: result}."""
    pr = gh.pull(number)
    if not str(pr["head"]["ref"]).startswith("social/"):
        return {}
    files = [f["filename"] for f in gh.pull_files(number)]
    targets = packs_in(files)
    head = pr["head"]["sha"]
    results, bodies, comments = {}, [], []
    for brand_key, rel in targets:
        d = Path(pr_dir) / rel
        if not (d / "pack.json").exists():
            continue
        p = packmod.load(d)
        s = settingsmod.load(brand_key, root)
        first = checks.run(p, checks.context_for(p, brand_key, root))
        body = review_view.render(p, first, s, brand_key, commit_sha=head,
                                  repo=os.environ.get("GITHUB_REPOSITORY", github.REPO))
        final = checks.run(p, checks.context_for(p, brand_key, root, pr_body=body))
        results[p["meta"]["pack_id"]] = final
        if preview_root is not None:
            preview_export.write(preview_root, *preview_export.collect(d, dict(pr, head=dict(pr["head"], sha=head)), final))
        bodies.append(body)
        comments.append(checks.markdown(final, p["meta"]["pack_id"]))
    if not results:
        return {}
    gh.update_pull(number, body="\n\n---\n\n".join(bodies))
    ok = all(r["ok"] for r in results.values())
    fails = sum(1 for r in results.values() for rs in r["posts"].values() for x in rs if not x["ok"]) + \
        sum(1 for r in results.values() for x in r["pack"] if not x["ok"])
    gh.status(head, "success" if ok else "failure", "social-checks",
              "all checks pass" if ok else f"{fails} check(s) failing")
    gh.sticky_comment(number, MARKER, "\n\n".join(comments))
    return results


def redo(gh, number, comment_id):
    pr = gh.pull(number)
    if str(pr["head"]["ref"]).startswith("social/"):
        gh.add_labels(number, ["redo requested"])


def merged(gh, number, root=brands.ROOT, today=None):
    """Flow 3 after a pack or fix PR closes: re-check, warn, record. Returns the registry status."""
    pr = gh.pull(number)
    ref = str(pr["head"]["ref"])
    if not ref.startswith("social/"):
        return None
    pack_id = ref.split("/", 2)[-1]
    fix = "-fix-" in pack_id
    base_pack = pack_id.split("-fix-")[0]
    files = [f["filename"] for f in gh.pull_files(number)]
    targets = packs_in(files)
    brand_key = targets[0][0] if targets else "vsichkikazina"
    s = settingsmod.load(brand_key, root)
    status = "merged" if pr.get("merged_at") else "closed"
    lines = []
    if status == "merged":
        by = (pr.get("merged_by") or {}).get("login", "")
        approved = github.Team(gh).merged(pr)
        for _b, rel in targets:
            d = Path(root) / rel
            if (d / "pack.json").exists():
                p = packmod.load(d)
                r = checks.run(p, checks.context_for(p, brand_key, root))
                lines.append(checks.markdown(r, p["meta"]["pack_id"]).replace("### Social checks", "### After-merge checks", 1))
        if not approved:
            lines.insert(0, f"⚠️ **Not approved**: this PR was merged by @{by}, who has no write access to this "
                            f"repository (or is a bot). Only a merge by someone with write access approves posts; these "
                            f"posts become \"Needs fix\" and go into a fix PR.")
        gh.comment(number, "\n\n".join(lines) if lines else "Merged.")
    for _b, rel in targets:                                        # the dashboard's preview of an open PR goes
        preview_export.remove(root, Path(rel).name)
    p_path = board.packs_path(brand_key, root)
    text = board._read(p_path)
    today = today or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    row = {"pack_id": pack_id, "source": (ids.parse_pack_id(base_pack) or {}).get("source", ""), "status": status,
           "updated": today, "pr": f"#{number}", "branch": ref}
    if status == "merged" and not approved:
        row["note"] = f"merged by {(pr.get('merged_by') or {}).get('login', '?')}, who cannot approve"
    if fix:
        row["note"] = (row.get("note", "") + f"; fix PR of {base_pack}").strip("; ")
    p_path.write_text(board.upsert_pack(text, row), encoding="utf-8")
    return status


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("review")
    r.add_argument("number", type=int)
    r.add_argument("--pr-dir", required=True)
    r.add_argument("--preview-root", help="the main checkout, to write the dashboard's preview of the pack into")
    d = sub.add_parser("redo")
    d.add_argument("number", type=int)
    d.add_argument("--comment-id", required=True)
    m = sub.add_parser("merged")
    m.add_argument("number", type=int)
    a = ap.parse_args(argv)
    gh = github.from_env()
    if gh is None:
        print("GITHUB_TOKEN is not set", file=sys.stderr)
        return 2
    gh.repo = os.environ.get("GITHUB_REPOSITORY", gh.repo)
    if a.cmd == "review":
        results = review(gh, a.number, a.pr_dir, preview_root=a.preview_root)
        print({k: v["ok"] for k, v in results.items()} or "not a social pack PR")
        return 0
    if a.cmd == "redo":
        redo(gh, a.number, a.comment_id)
        return 0
    if a.cmd == "merged":
        print(merged(gh, a.number) or "not a social pack PR")
        return 0
    return 2


if __name__ == "__main__":
    sys.exit(main())
