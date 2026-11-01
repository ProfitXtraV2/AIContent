"""A small repository with a library item and a pack, for the social tests."""
import copy
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_library as bl  # noqa: E402
from social import pack as packmod  # noqa: E402
from test_build_library import make_repo  # noqa: E402

COMPLIANCE = "18+ Хазартът може да пристрасти. Играйте отговорно."
SOURCE_LINE = "Банко 1:1 минус 5% комисиона."

FB = {"text": "Бакара изглежда сложна, но залозите са само три.\n\n" + SOURCE_LINE +
      "\n\nЦялото ръководство: [[LINK]]\n\n" + COMPLIANCE,
      "hashtags": ["#бакара", "#казиноигри"], "image_text": ["Три залога в бакара"],
      "alt_text": "Илюстрация: три залога в бакара на везни", "english": "Baccarat looks complicated..."}
IG = {"text": "Три залога, едно правило: комисионата.\n\n" + SOURCE_LINE +
      "\n\nЦялото ръководство е на линка в профила ни.\n\n" + COMPLIANCE,
      "hashtags": ["#бакара", "#казиноигри", "#правила"],
      "image_text": ["Бакара накратко", "Банко 1:1 минус 5% комисиона", "Пунто и равенство", "Прочетете ръководството"],
      "alt_text": "Корица: бакара за начинаещи", "english": "Three bets, one rule..."}
X = {"text": "Бакара: " + SOURCE_LINE + " [[LINK]] 18+ Играйте отговорно.",
     "hashtags": ["#бакара"], "image_text": ["Три залога в бакара"],
     "alt_text": "Три залога в бакара", "english": "Baccarat: ..."}


def post_meta(pid, account, network, fields, link, visuals, fmt="single"):
    return {"post_id": pid, "account_id": account, "network": network, "role": "launch", "format": fmt,
            "link": link, "sources": [{"line": SOURCE_LINE, "where": "Бакара: правила, залози"}],
            "numbers": [{"value": "1:1", "source_index": 0}, {"value": "5%", "source_index": 0}],
            "en_reference_of": packmod.own_hash(fields), "visuals": visuals, "redo_notes": []}


def visual(file, role, fields, kind="generated"):
    return {"file": file, "kind": kind, "role": role, "fallback_case": None, "score": 92,
            "image_text_hash": packmod.image_text_hash(fields), "sha256": "x",
            "frame": {"domain": True, "mark_18": True}}


def make_pack(tmp):
    """(root, pack dir) with the library built and pack vk-0001-p1 holding fb, ig (carousel) and x."""
    root = make_repo(tmp)
    items, missing = bl.build(root)
    bl.write(root / "library" / "vsichkikazina", items, missing, "vsichkikazina")
    version = next(e["item"]["article_version"] for e in items if e["item"]["id"] == "vk-0001")
    fb, ig, x = "vk-0001-p1-fb-1", "vk-0001-p1-ig-1", "vk-0001-p1-x-1"
    posts = {fb: copy.deepcopy(FB), ig: copy.deepcopy(IG), x: copy.deepcopy(X)}
    meta = {
        "pack_id": "vk-0001-p1", "brand": "vsichkikazina", "number": 1, "angle": "key takeaway",
        "earlier_angles": [],
        "source": {"kind": "article", "item_id": "vk-0001", "slug": "bakara-pravila", "article_version": version},
        "created_utc": "2026-11-03T09:40:00Z", "run_url": "", "fix_round": 0,
        "posts": [
            post_meta(fb, "fb-vsichkikazina", "facebook", posts[fb],
                      {"mode": "placeholder", "campaign": "bakara-pravila", "content": fb},
                      [visual(f"{fb}-1.jpg", "single", posts[fb])]),
            post_meta(ig, "ig-vsichkikazina", "instagram", posts[ig],
                      {"mode": "none", "reason": "link in profile"},
                      [visual(f"{ig}-{n}.jpg", role, posts[ig])
                       for n, role in enumerate(["cover", "point", "point", "closing"], 1)], fmt="carousel"),
            post_meta(x, "x-vsichkikazina", "x", posts[x],
                      {"mode": "placeholder", "campaign": "bakara-pravila", "content": x},
                      [visual(f"{x}-1.jpg", "single", posts[x])]),
        ],
    }
    d = root / "VsichkiKazina" / "social" / "packs" / "vk-0001-p1"
    packmod.save(d, meta, posts)
    (d / "visuals").mkdir()
    for p in meta["posts"]:
        for v in p["visuals"]:
            (d / "visuals" / v["file"]).write_bytes(b"\xff\xd8\xff jpeg " + v["file"].encode())
    return root, d


def edit_post(pack_dir, post_id, **changes):
    f = Path(pack_dir) / "posts" / f"{post_id}.md"
    fields = packmod.parse_post_md(f.read_text(encoding="utf-8"))
    fields.update(changes)
    f.write_text(packmod.render_post_md(post_id, fields), encoding="utf-8")
    return fields


def edit_meta(pack_dir, fn):
    f = Path(pack_dir) / "pack.json"
    meta = json.loads(f.read_text(encoding="utf-8"))
    fn(meta)
    f.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
