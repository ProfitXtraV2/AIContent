"""A pack on disk (tech spec, Data model "Pack"):

    <Brand>/social/packs/<pack-id>/
        pack.json                    machine fields (posts, sources, visuals, hashes)
        posts/<post-id>.md           what people edit, under fixed headings
        visuals/<post-id>-<n>.jpg    the images, in order (slides of a carousel)

posts/<post-id>.md:
    # vk-0300-p1-fb-1
    ## Post text                              own language, with [[LINK]] where the link goes
    ## Hashtags                               #one #two
    ## Image text                             one line per image title or slide
    ## Alt text
    ## English reference (for review only)    written by the AI with the post, never published
"""
import hashlib
import json
import re
from pathlib import Path

HEADINGS = {"post text": "text", "hashtags": "hashtags", "image text": "image_text",
            "alt text": "alt_text", "english reference (for review only)": "english"}
ORDER = ["Post text", "Hashtags", "Image text", "Alt text", "English reference (for review only)"]


def parse_post_md(text):
    """{text, hashtags: [..], image_text: [lines], alt_text, english} from a post file."""
    found = {v: [] for v in HEADINGS.values()}
    current = None
    for line in str(text or "").splitlines():
        m = re.match(r"^##\s+(.+?)\s*$", line)
        if m:
            current = HEADINGS.get(m.group(1).strip().lower())
            continue
        if line.startswith("# ") and current is None:
            continue
        if current:
            found[current].append(line)
    joined = {k: "\n".join(v).strip() for k, v in found.items()}
    return {
        "text": joined["text"],
        "hashtags": [h if h.startswith("#") else "#" + h for h in re.split(r"[\s,]+", joined["hashtags"]) if h],
        "image_text": [ln.strip() for ln in joined["image_text"].splitlines() if ln.strip()],
        "alt_text": joined["alt_text"],
        "english": joined["english"],
    }


def render_post_md(post_id, fields):
    parts = [f"# {post_id}", ""]
    values = {"Post text": fields.get("text", ""),
              "Hashtags": " ".join(fields.get("hashtags") or []),
              "Image text": "\n".join(fields.get("image_text") or []),
              "Alt text": fields.get("alt_text", ""),
              "English reference (for review only)": fields.get("english", "")}
    for h in ORDER:
        parts += [f"## {h}", values[h].strip(), ""]
    return "\n".join(parts).rstrip() + "\n"


def _sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def publish_text(fields):
    """What goes to the network: the post text, then its hashtags on their own line."""
    text = fields.get("text", "").strip()
    tags = " ".join(fields.get("hashtags") or [])
    return text + ("\n\n" + tags if tags else "")


def own_hash(fields):
    """What the English reference must match: the own-language text and image text."""
    return _sha(fields.get("text", "").strip() + "\n\x1f\n" + "\n".join(fields.get("image_text") or []))


def english_block(text_en, image_en):
    out = ["Text:", str(text_en or "").strip()]
    if image_en:
        out += ["", "Image text:"] + [f"- {t}" for t in image_en]
    return "\n".join(out)


def set_english(post, fields, english):
    """The English reference the drafting agent wrote ({"text", "image_text"}), recorded for the
    text as it is now. No English given leaves the post as it was. Returns True when set."""
    english = english or {}
    if not str(english.get("text") or "").strip():
        return False
    image = [str(x).strip() for x in english.get("image_text") or [] if str(x).strip()]
    fields["english"] = english_block(english["text"], image)
    post["en_reference_of"] = own_hash(fields)
    return True


def english_current(post, fields):
    """True when the English reference was written for the text and image text as they are now;
    an edit in the PR leaves it out of date."""
    return bool(fields.get("english", "").strip()) and post.get("en_reference_of") == own_hash(fields)


def image_text_hash(fields):
    return _sha("\n".join(fields.get("image_text") or []))


def load(pack_dir):
    """{"dir", "meta": pack.json, "posts": {post_id: fields}} for a pack folder."""
    pack_dir = Path(pack_dir)
    meta = json.loads((pack_dir / "pack.json").read_text(encoding="utf-8"))
    posts = {}
    for p in meta.get("posts", []):
        f = pack_dir / "posts" / f"{p['post_id']}.md"
        if f.exists():
            posts[p["post_id"]] = parse_post_md(f.read_text(encoding="utf-8"))
    return {"dir": pack_dir, "meta": meta, "posts": posts}


def save(pack_dir, meta, posts):
    pack_dir = Path(pack_dir)
    (pack_dir / "posts").mkdir(parents=True, exist_ok=True)
    (pack_dir / "pack.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n",
                                        encoding="utf-8")
    for pid, fields in posts.items():
        (pack_dir / "posts" / f"{pid}.md").write_text(render_post_md(pid, fields), encoding="utf-8")


def deleted_posts(pack):
    """Posts whose file a person deleted in the PR: they leave the pack (E3)."""
    return [p["post_id"] for p in pack["meta"].get("posts", []) if p["post_id"] not in pack["posts"]]


def files_hash(pack_dir, only=None):
    """sha256 over the pack's files (relative path + bytes, in path order). `only`: post IDs
    whose files count (a post's .md and visuals), plus pack.json."""
    pack_dir = Path(pack_dir)
    h = hashlib.sha256()
    for f in sorted(p for p in pack_dir.rglob("*") if p.is_file()):
        rel = f.relative_to(pack_dir).as_posix()
        if only is not None and rel != "pack.json":
            stem = Path(rel).stem
            if not any(stem == pid or stem.startswith(pid + "-") for pid in only):
                continue
        h.update(rel.encode() + b"\0" + f.read_bytes() + b"\0")
    return h.hexdigest()


def post_files_hash(pack_dir, post_id, visuals):
    """sha256 of one post's approved files: its .md and its visuals, in order (boundary 3)."""
    pack_dir = Path(pack_dir)
    h = hashlib.sha256()
    for rel in [f"posts/{post_id}.md"] + [f"visuals/{v['file']}" for v in visuals or []]:
        f = pack_dir / rel
        h.update(rel.encode() + b"\0" + (f.read_bytes() if f.exists() else b"<missing>") + b"\0")
    return h.hexdigest()


def post_meta(pack, post_id):
    return next((p for p in pack["meta"].get("posts", []) if p["post_id"] == post_id), None)
