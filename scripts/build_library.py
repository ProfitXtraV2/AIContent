#!/usr/bin/env python3
"""Build the article library: a copy of every approved and live item of a brand, with its
article version (product spec A8; tech spec "Article library item").

    python3 scripts/build_library.py [brand]      # brand: vsichkikazina (default)

Writes library/<brand>/<slug>/{item.json, article.md} and library/<brand>/index.json.
Social drafting, the PR checks and the publishing check read it. **The publisher never does:**
published/ is not touched, and the feed stays exactly as build_feed.py makes it
(scripts/tests/test_feed_unchanged.py).

The article version is the sha256 of {title, meta_description, body, images: [{name, alt,
sha256}]}: only what a post can quote. Status, the live marker, the opportunity score and dates
are left out, so going live alone never changes it.
"""
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_dashboard as bd  # noqa: E402
import build_feed as bf  # noqa: E402
from social import brands, operators, settings as social_settings  # noqa: E402

LIBRARY_SCHEMA = 1
KEEP = {"approved", "posted"}
SCORE_RE = re.compile(r"(?:\bscore\b[^0-9\n]{0,24}(\d{1,3})(?:\s*/\s*100)?|(\d{1,3})\s*/\s*100)", re.I)
LABEL_RE = re.compile(r"(\d{1,3})\s*/\s*100\s*\((svg|hero)\)", re.I)
NEG_RE = re.compile(r"(no|not an?|neither is an?|without|без)\s+(?:\w+\s+){0,2}$", re.I)


def canonical(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def article_version(title, meta_description, body, images):
    """sha256 over what a post can quote (A8). images: [{name, alt, sha256}]."""
    payload = {"title": title, "meta_description": meta_description, "body": body,
               "images": [{"name": i["name"], "alt": i["alt"], "sha256": i["sha256"]} for i in images]}
    return hashlib.sha256(canonical(payload).encode("utf-8")).hexdigest()


def _scores(line):
    return [int(a or b) for a, b in SCORE_RE.findall(line) if 0 <= int(a or b) <= 100]


def integrity(text):
    """True when the review says there was no integrity failure, False when it reports one,
    None when it does not say."""
    hits = [m.start() for m in re.finditer(r"integrity fail", text, re.I)]
    if not hits:
        return None
    negated = [bool(NEG_RE.search(text[max(0, i - 40):i])) for i in hits]
    return all(negated)


def review_scores(review_text, image_names):
    """{image name: score} for the images the review names unambiguously (tech spec: "Scores
    are taken from the last 08-image-review-*.md only when the match to the file is
    unambiguous"). Images left out have an unknown score."""
    lines = review_text.splitlines()
    out = {}
    for name in image_names:
        stem = Path(name).stem
        found = set()
        for ln in lines:
            if name in ln or (len(stem) > 5 and stem in ln):
                found.update(_scores(ln))
        if len(found) == 1:
            out[name] = found.pop()
    svgs = [n for n in image_names if n.lower().endswith(".svg")]
    heroes = [n for n in image_names if "hero" in n.lower()]
    for ln in lines:
        for score, label in LABEL_RE.findall(ln):
            pool = svgs if label.lower() == "svg" else heroes
            if len(pool) == 1 and pool[0] not in out:
                out[pool[0]] = int(score)
    distinct = {s for ln in lines for s in _scores(ln)}
    if len(distinct) == 1:
        score = distinct.pop()
        everyone = re.search(r"\b(both|all)\s+(images|three|two)\b|\(both images\)|\(all images\)", review_text, re.I)
        if len(image_names) == 1 or everyone:
            for n in image_names:
                out.setdefault(n, score)
    return out


def last_review(files):
    """The last 08-image-review-N.md of a list of (name, text)."""
    best, best_n = None, -1
    for name, text in files:
        m = re.match(r"08-image-review-(\d+)\.md$", name)
        if m and int(m.group(1)) > best_n:
            best, best_n = (name, text), int(m.group(1))
    return best


def build_item(brand_key, row, draft, images, review, operator_names, offer_words, built_utc):
    """One library item. images: [{name, path, alt, sha256}]; review: (name, text) or None."""
    title = draft.get("title_tag") or draft.get("h1") or row.get("query", "")
    keywords = [k.strip() for k in (row.get("keywords_or_terms") or "").split(",") if k.strip()]
    names = [i["name"] for i in images]
    scores = review_scores(review[1], names) if review else {}
    integ = integrity(review[1]) if review else None
    out_images = []
    for img in images:
        score = scores.get(img["name"])
        out_images.append({
            "path": img["path"], "name": img["name"], "alt": img["alt"], "sha256": img["sha256"],
            "review": {"score": score if score is not None else "unknown",
                       "integrity_ok": integ if score is not None else None,
                       "source": review[0] if (review and score is not None) else "unknown"},
        })
    slug = bf.slug_from_folder(row["folder"])
    flagged, reason = operators.screen(title, slug, keywords, operator_names, offer_words)
    status = row.get("status", "").lower()
    return {
        "library_schema": LIBRARY_SCHEMA,
        "brand": brand_key,
        "id": row.get("id", ""),
        "slug": slug,
        "kind": "hub-intro" if row.get("type", "").lower() == "hub-intro" else "article",
        "type": row.get("type", ""),
        "board_status": status,
        "live": status == "posted",
        "folder": row.get("folder", ""),
        "pr": row.get("pr", ""),
        "title": title,
        "meta_description": draft.get("meta_description", ""),
        "keywords": keywords,
        "body_path": "article.md",
        "images": out_images,
        "article_version": article_version(title, draft.get("meta_description", ""), draft["body"],
                                           [{"name": i["name"], "alt": i["alt"], "sha256": i["sha256"]}
                                            for i in images]),
        "operator_or_bonus": flagged,
        "operator_or_bonus_reason": reason,
        "built_utc": built_utc,
    }


class RepoReader:
    """Reads an article's files: the working tree of `root` first, then its content branch."""

    def __init__(self, root, brand_dir):
        self.root, self.brand_dir = Path(root), brand_dir

    def _git(self, *args):
        try:
            return subprocess.run(["git", *args], cwd=self.root, capture_output=True, check=True,
                                  timeout=30).stdout
        except (OSError, subprocess.SubprocessError):
            return None

    def article_dir(self, folder):
        return f"{self.brand_dir}/articles/{folder}"

    def draft(self, folder):
        """The final draft from the same source as the feed (build_feed.read_article_md): the
        content branch first, then the working tree."""
        rel = f"{self.article_dir(folder)}/05b-final-draft.md"
        for ref in (f"origin/content/{folder}", f"content/{folder}"):
            out = self._git("show", f"{ref}:{rel}")
            if out is not None:
                return out.decode("utf-8", "replace")
        local = self.root / rel
        return local.read_text(encoding="utf-8") if local.exists() else None

    def files(self, folder):
        """[(name, text)] of the article folder's review files."""
        d = self.root / self.article_dir(folder)
        if d.is_dir():
            return [(p.name, p.read_text(encoding="utf-8", errors="replace"))
                    for p in d.glob("08-image-review-*.md")]
        out = []
        for ref in (f"origin/content/{folder}", f"content/{folder}"):
            names = self._git("ls-tree", "--name-only", ref, self.article_dir(folder) + "/")
            if names is None:
                continue
            for n in names.decode().splitlines():
                base = n.rsplit("/", 1)[-1]
                if re.match(r"08-image-review-\d+\.md$", base):
                    data = self._git("show", f"{ref}:{n}")
                    if data is not None:
                        out.append((base, data.decode("utf-8", "replace")))
            break
        return out

    def image_bytes(self, folder, slug, rel_image):
        """(repo path, bytes) of an article image: published/<slug>/images/<file> when the feed
        has it, else the article folder (working tree, then branch)."""
        name = Path(rel_image).name
        pub = self.root / "published" / slug / "images" / name
        if pub.exists():
            return f"published/{slug}/images/{name}", pub.read_bytes()
        rel = f"{self.article_dir(folder)}/{rel_image}"
        local = self.root / rel
        if local.exists():
            return rel, local.read_bytes()
        for ref in (f"origin/content/{folder}", f"content/{folder}"):
            out = self._git("show", f"{ref}:{rel}")
            if out is not None:
                return rel, out
        return None, None


def image_sha256(name, data):
    """The image's hash. An SVG is text, and a Windows checkout gives it CRLF line ends where git
    and Linux have LF, so its line ends are made LF first: the article version is the same on
    every machine."""
    if str(name).lower().endswith(".svg"):
        data = data.replace(b"\r\n", b"\n")
    return hashlib.sha256(data).hexdigest()


def build(root, brand_key="vsichkikazina", reader=None, now=None):
    """(items, missing) for a brand from its queue."""
    b = brands.brand(brand_key)
    root = Path(root)
    reader = reader or RepoReader(root, b["dir"])
    queue = (root / b["dir"] / "content-queue.md").read_text(encoding="utf-8")
    s = social_settings.load(brand_key, root)
    ops = operators.current(brand_key, root, s.brand["operator_names_manual"])
    built = now or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    items, missing = [], []
    for row in bd.parse_queue(queue, brand=b["queue_format"]):
        status = (row.get("status") or "").lower()
        if status not in KEEP:
            continue
        folder = (row.get("folder") or "").strip()
        if not folder:
            missing.append({"id": row.get("id", ""), "slug": "", "board_status": status,
                            "reason": "no folder on the board"})
            continue
        text = reader.draft(folder)
        if text is None:
            missing.append({"id": row.get("id", ""), "slug": bf.slug_from_folder(folder),
                            "board_status": status, "reason": "no final draft (05b-final-draft.md)"})
            continue
        draft = bf.parse_final_draft(text)
        slug = bf.slug_from_folder(folder)
        images = []
        for img in bf.extract_images(draft["body"]):
            path, data = reader.image_bytes(folder, slug, img["path"])
            if data is None:
                continue
            images.append({"name": Path(img["path"]).name, "path": path, "alt": img["alt"],
                           "sha256": image_sha256(img["path"], data)})
        review = last_review(reader.files(folder))
        items.append({"item": build_item(brand_key, row, draft, images, review, ops,
                                         s.brand["offer_words"], built),
                      "body": draft["body"]})
    return items, missing


def write(library_dir, items, missing, brand_key):
    """Write the library. Idempotent: an item whose content is unchanged keeps its file and its
    built_utc; items no longer approved or live are removed."""
    library_dir = Path(library_dir)
    library_dir.mkdir(parents=True, exist_ok=True)
    keep = set()
    for e in items:
        item, body = dict(e["item"]), e["body"]
        d = library_dir / item["slug"]
        keep.add(item["slug"])
        f = d / "item.json"
        if f.exists():
            try:
                old = json.loads(f.read_text(encoding="utf-8"))
                if {k: v for k, v in old.items() if k != "built_utc"} == \
                        {k: v for k, v in item.items() if k != "built_utc"} and \
                        (d / "article.md").read_text(encoding="utf-8") == body + "\n":
                    item["built_utc"] = old.get("built_utc", item["built_utc"])
                    e["item"] = item
                    continue
            except (OSError, ValueError):
                pass
        d.mkdir(parents=True, exist_ok=True)
        (d / "article.md").write_text(body + "\n", encoding="utf-8")
        f.write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for d in sorted(p for p in library_dir.iterdir() if p.is_dir()):
        if d.name not in keep:
            for f in sorted(d.rglob("*"), reverse=True):
                f.unlink() if f.is_file() else f.rmdir()
            d.rmdir()
    index = {
        "library_schema": LIBRARY_SCHEMA,
        "brand": brand_key,
        # title and operator_or_bonus: the dashboard's list of the articles a request may name
        "items": [{k: e["item"][k] for k in ("slug", "id", "kind", "title", "board_status", "live", "operator_or_bonus",
                                             "article_version")}
                  for e in sorted(items, key=lambda e: e["item"]["id"])],
        "missing": sorted(missing, key=lambda m: m["id"]),
    }
    new = json.dumps(index, ensure_ascii=False, indent=2) + "\n"
    idx = library_dir / "index.json"
    if not idx.exists() or idx.read_text(encoding="utf-8") != new:
        idx.write_text(new, encoding="utf-8")
    return index


def load_item(root, brand_key, slug):
    """(item, article text) from the library, or (None, None)."""
    d = Path(root) / "library" / brand_key / slug
    try:
        return (json.loads((d / "item.json").read_text(encoding="utf-8")),
                (d / "article.md").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None, None


def load_index(root, brand_key):
    try:
        return json.loads((Path(root) / "library" / brand_key / "index.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {"items": [], "missing": []}


def main():
    brand_key = sys.argv[1] if len(sys.argv) > 1 else "vsichkikazina"
    root = Path(__file__).resolve().parents[1]
    items, missing = build(root, brand_key)
    index = write(root / "library" / brand_key, items, missing, brand_key)
    print(f"library: {len(index['items'])} item(s) for {brand_key}, {len(missing)} missing")
    return 0


if __name__ == "__main__":
    sys.exit(main())
