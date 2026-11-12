"""AC 12: adding the article library changes nothing the publisher reads.

1. The feed (published/) built with and without library/ is byte for byte the same.
2. The publisher's classification loop (WebPortals VsichkiKazina/_publisher/run_publish.py,
   lines 511–527, copied below) queues no live slug, vk-0001 and vk-0003 included.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_feed as bf  # noqa: E402
import build_library as bl  # noqa: E402
from test_build_library import make_repo  # noqa: E402


def snapshot(published):
    out = {}
    for f in sorted(p for p in published.rglob("*") if p.is_file()):
        data = f.read_bytes()
        if f.name == "index.json":                     # generated_utc is a time stamp
            obj = json.loads(data)
            obj.pop("generated_utc", None)
            data = json.dumps(obj, sort_keys=True).encode()
        out[f.relative_to(published).as_posix()] = data
    return out


def feed(root):
    """build_feed.main() for a test repository (local files only, no content branches)."""
    queue = (root / "VsichkiKazina" / "content-queue.md").read_text(encoding="utf-8")
    entries = []
    for row in bf.select_approved(queue):
        draft = bf.parse_final_draft((root / "VsichkiKazina" / "articles" / row["folder"] / "05b-final-draft.md")
                                     .read_text(encoding="utf-8"))
        meta = bf.build_meta(row, draft, bf.extract_images(draft["body"]))
        meta["content_hash"] = bf.content_hash(draft["body"], meta)
        entries.append({"meta": meta, "body": draft["body"], "folder": row["folder"]})
    out = root / "published"
    out.mkdir(exist_ok=True)
    for e in entries:                                    # write_feed without the git image copy
        d = out / e["meta"]["slug"]
        if bf._existing_hash(d) == e["meta"]["content_hash"]:
            continue
        (d / "images").mkdir(parents=True, exist_ok=True)
        (d / "article.md").write_text(e["body"] + "\n", encoding="utf-8")
        (d / "meta.json").write_text(json.dumps(e["meta"], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    index = bf.build_index(entries)
    index["generated_utc"] = "x"
    (out / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return out


def test_feed_is_identical_with_and_without_the_library(tmp_path):
    a = make_repo(tmp_path / "a")
    b = make_repo(tmp_path / "b")
    plain = snapshot(feed(a))
    items, missing = bl.build(b)
    bl.write(b / "library" / "vsichkikazina", items, missing, "vsichkikazina")
    with_library = snapshot(feed(b))
    assert plain == with_library
    items, missing = bl.build(b)                          # library rebuilt after the feed: still the same
    bl.write(b / "library" / "vsichkikazina", items, missing, "vsichkikazina")
    assert snapshot(b / "published") == plain
    assert (b / "library" / "vsichkikazina" / "index.json").exists()
    assert not any("library" in k for k in plain)


def classify(feed_index, state):
    """Copied from WebPortals run_publish.py (lines 511–527)."""
    retries, hub_intros, queue = [], [], []
    for art in feed_index["articles"]:
        slug = art["slug"]
        feed_hash = art["content_hash"]
        if slug in state:
            if state[slug]["content_hash"] == feed_hash:
                retries.append((slug, art))
            elif slug.startswith("hub-intro-"):
                hub_intros.append((slug, art))
            else:
                queue.append((slug, art))
        else:
            if slug.startswith("hub-intro-"):
                hub_intros.append((slug, art))
            else:
                queue.append((slug, art))
    return retries, hub_intros, queue


def test_publisher_queues_no_live_slug(tmp_path):
    root = make_repo(tmp_path)
    (root / "VsichkiKazina" / "articles" / "2026-09-07-bezplatni" / "images").mkdir(parents=True)
    (root / "VsichkiKazina" / "articles" / "2026-09-07-bezplatni" / "05b-final-draft.md").write_text(
        "# Безплатни игри\n\nдемо режим\n", encoding="utf-8")
    items, missing = bl.build(root)                       # the backfill: vk-0003 gets its library copy
    bl.write(root / "library" / "vsichkikazina", items, missing, "vsichkikazina")
    assert {e["item"]["id"] for e in items} >= {"vk-0001", "vk-0003"}
    index = json.loads((feed(root) / "index.json").read_text(encoding="utf-8"))
    live = {"bakara-pravila": {"content_hash": "deployed-long-ago"}, "bezplatni": {"content_hash": "x"}}
    retries, hubs, queue = classify(index, live)
    queued = {slug for slug, _ in queue}
    assert queued == {"razigravane", "nv-casino-bonus"}   # the approved, not-yet-live articles only
    assert not queued & {"bakara-pravila", "bezplatni"}   # vk-0001 and vk-0003 never queued
    assert {slug for slug, _ in hubs} == {"hub-intro-casino-payments"}
