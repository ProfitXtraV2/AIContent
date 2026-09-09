# VsichkiKazina Publisher Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** In the target repo `ProfitXtraV2/WebPortals` (site `VsichkiKazina`), build a scheduled
AI-agent publisher that pulls AIContent's `published/` feed, renders each `approved` article into
the site's exact HTML template (brand-aligned body + internal backlinks + correct category),
runs a Gemini SEO inspection, FTP-deploys to production, and writes the status back to AIContent
as `posted`.

**Architecture:** Hybrid — **deterministic Python scripts** own the page *chrome* (template fill,
JSON-LD, sitemap/index upsert, category routing, FTP, SEO-check API call, state) and are unit
tested; an **AI-agent orchestration doc** (`publish-run.md`) owns the *judgment* work (markdown→
HTML body in brand voice, backlink selection, SEO fixes) and drives the run. Runs as a cloud
routine, Tue–Fri 09:30 Sofia.

**Tech Stack:** Python 3 (stdlib: `json`, `re`, `hashlib`, `ftplib`, `urllib`, `pathlib`,
`html`, `xml.etree`), pytest. No SSG — we render into built HTML directly.

**Where the work lands:** repo root `/Users/georgitodorov/Work/WebPortals` (a git repo, remote
`ProfitXtraV2/WebPortals`); all new files under `VsichkiKazina/_publisher/`. Work on a feature
branch; `main` here is the deploy source.

## Global Constraints

- **Consumes the contract only:** reads AIContent's `published/index.json` + `<slug>/{article.md,meta.json,images/*}` (raw from the public repo). Never reaches into AIContent internals.
- **Feed is approved-only:** deploy nothing that isn't in the feed.
- **Author = Person "Георги Тодоров"** in both the visible byline (`<p class="updated">`) and the JSON-LD `Article.author` (replace the site's current Organization author). Brand name exactly **Всички Казина**.
- **Chrome is byte-stable:** header/nav/`altm` modal/footer/`<script>`/CSS+JS `?v=` hashes are copied verbatim from the live template; only per-post fields vary.
- **Deterministic scripts, stdlib-only, unit-tested;** the agent does only body/backlinks/SEO-fixes.
- **No duplicates, failure-safe:** every article keyed by stable `slug` + the `<category>/<slug>/` path pinned in `.published-state.json`; re-runs update in place; FTP failure ⇒ article stays `approved`, no write-back, retried next run.
- **Careful category routing:** place each article in the correct existing section via `category-map.json`; default `blog/` only when unsure; recorded path is stable.
- **SEO gate before deploy:** Gemini audits the rendered HTML; PASS ≥ 80; ≤ 2 fixes; keep-best; hard-block FTP on score < 60 or a broken internal link / missing canonical|H1.
- **Sync `main` first** each run; abort on dirty/conflicted tree.
- **Secrets (never committed):** `FTP_HOST/FTP_USER/FTP_PASS/FTP_DIR`, `GEMINI_API_KEY`, `AICONTENT_TOKEN` (for the write-back). Required only at live-run time; build + dry-run need none.
- **RG/disclosure:** keep the site's compliance footer + `altm` note; never fabricate operator facts/offers.

---

## File Structure (all under `VsichkiKazina/_publisher/`)

- `templates/blog-post.html` — chrome template extracted from a live post, with `{{PLACEHOLDERS}}`.
- `category-map.json` — site sections → {label, path_prefix, when_to_use} for routing.
- `brand-book.md` — derived voice/terminology/RG/linking/author rules the agent aligns to.
- `render.py` — deterministic: `fill_template`, `build_jsonld`, `route_category`, `upsert_sitemap`, `upsert_index_card`, `render_page`, state helpers, CLI.
- `seo_inspect.py` — Gemini SEO audit of a rendered HTML file (+ `prompts/seo-inspect.md`).
- `deploy_ftp.py` — upload changed files via FTP (creds from env; `--dry-run`).
- `publish-run.md` — the AI-agent orchestration (the full run).
- `tests/test_render.py`, `tests/test_deploy.py` — pytest.
- `.published-state.json` — idempotency state (generated).

---

## Task 1: Extract the chrome template + `fill_template`

**Files:**
- Create: `VsichkiKazina/_publisher/templates/blog-post.html`
- Create: `VsichkiKazina/_publisher/render.py`
- Test: `VsichkiKazina/_publisher/tests/test_render.py`

**Interfaces:**
- Produces: `fill_template(template: str, fields: dict) -> str` — replaces every `{{KEY}}` with
  `fields[KEY]`; raises `ValueError` listing any `{{...}}` left unfilled.

- [ ] **Step 1: Build the template** — copy `VsichkiKazina/blog/koe-kazino-da-izberete/index.html`
  to `templates/blog-post.html` verbatim, then replace ONLY the per-post fields with placeholders,
  leaving header/nav/`altm`/footer/scripts and all `?v=` hashes untouched:
  - `<title>{{TITLE}}</title>`; `<meta name="description" content="{{META_DESC}}">`
  - canonical + `og:url` → `{{CANONICAL}}`; `og:title` → `{{TITLE}}`; `og:description` → `{{META_DESC}}`; `og:image` → `{{OG_IMAGE}}`
  - the Article + BreadcrumbList `<script type="application/ld+json">` blocks → a single `{{JSONLD}}`
  - breadcrumb last `<span>{{TITLE}}</span>`
  - `<span class="post-card__cat">{{CATEGORY_LABEL}}</span>`; `<time datetime="{{DATE_ISO}}">{{DATE_BG}}</time>`
  - `<h1>{{TITLE}}</h1>`; `<p class="updated">{{AUTHOR}}</p>`
  - article body region → `{{BODY}}`
  - related-posts `<ul class="post-grid">…</ul>` inner → `{{RELATED}}`

- [ ] **Step 2: Write the failing test**

```python
# VsichkiKazina/_publisher/tests/test_render.py
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import render as r

def test_fill_template_replaces_all():
    out = r.fill_template("<h1>{{TITLE}}</h1><p>{{AUTHOR}}</p>",
                          {"TITLE": "Заглавие", "AUTHOR": "Георги Тодоров"})
    assert out == "<h1>Заглавие</h1><p>Георги Тодоров</p>"

def test_fill_template_raises_on_unfilled():
    try:
        r.fill_template("<h1>{{TITLE}}</h1>{{MISSING}}", {"TITLE": "x"})
        assert False, "expected ValueError"
    except ValueError as e:
        assert "MISSING" in str(e)
```

- [ ] **Step 3: Run test to verify it fails** — `python3 -m pytest VsichkiKazina/_publisher/tests/test_render.py -v` → FAIL (no module `render`).

- [ ] **Step 4: Implement** (`render.py`)

```python
#!/usr/bin/env python3
"""Deterministic rendering + site-index upkeep for the VsichkiKazina publisher."""
import html
import json
import re
from pathlib import Path

_PLACEHOLDER = re.compile(r"\{\{([A-Z_]+)\}\}")


def fill_template(template, fields):
    """Replace every {{KEY}} with fields[KEY]; error if any placeholder is left unfilled."""
    def sub(m):
        key = m.group(1)
        if key not in fields:
            raise KeyError(key)
        return str(fields[key])
    try:
        out = _PLACEHOLDER.sub(sub, template)
    except KeyError as e:
        raise ValueError(f"no value for placeholder {{{{{e.args[0]}}}}}") from None
    leftover = _PLACEHOLDER.findall(out)
    if leftover:
        raise ValueError(f"unfilled placeholders: {sorted(set(leftover))}")
    return out
```

- [ ] **Step 5: Run test to verify it passes**, then **commit**:

```bash
python3 -m pytest VsichkiKazina/_publisher/tests/test_render.py -v
git add VsichkiKazina/_publisher/templates/blog-post.html VsichkiKazina/_publisher/render.py VsichkiKazina/_publisher/tests/test_render.py
git commit -m "feat(publisher): chrome template + fill_template"
```

---

## Task 2: `category-map.json` + `route_category`

**Files:** Modify `render.py`; Create `VsichkiKazina/_publisher/category-map.json`; Test in `test_render.py`.

**Interfaces:** `route_category(meta: dict, category_map: dict) -> dict` → the chosen category
`{"key","label","path_prefix"}`. Deterministic default = `blog`.

- [ ] **Step 1: Author `category-map.json`** — the site's real sections with routing keywords:

```json
{
  "default": "blog",
  "categories": {
    "blog":        {"label": "Ръководство", "path_prefix": "blog", "keywords": ["ръководство","новини","обяснение","данъци","закон","лиценз"]},
    "kazino-igri": {"label": "Казино игри", "path_prefix": "kazino-igri", "keywords": ["ротативки","рулетка","блекджек","бакара","кено","игри на живо","покер"]},
    "slot-igri":   {"label": "Слот игри",   "path_prefix": "slot-igri", "keywords": ["слот","слотове","rtp","волатилност","провайдър","pragmatic","amusnet"]},
    "bonusi":      {"label": "Бонуси",       "path_prefix": "bonusi", "keywords": ["бонус","завъртания","без депозит","кешбек","промоция"]}
  }
}
```

- [ ] **Step 2: Failing test**

```python
CATMAP = json.loads((Path(r.__file__).parent / "category-map.json").read_text(encoding="utf-8"))

def test_route_by_section_hint_and_keywords():
    assert r.route_category({"section_hint": "guide", "keywords": ["ротативки"]}, CATMAP)["key"] == "kazino-igri"
    assert r.route_category({"section_hint": "guide", "keywords": ["бонус без депозит"]}, CATMAP)["key"] == "bonusi"

def test_route_defaults_to_blog():
    assert r.route_category({"section_hint": "news", "keywords": ["данъци"]}, CATMAP)["key"] == "blog"
    assert r.route_category({"section_hint": "guide", "keywords": ["нещо неясно"]}, CATMAP)["key"] == "blog"
```

- [ ] **Step 3: Run → FAIL.**
- [ ] **Step 4: Implement** (append to `render.py`)

```python
def route_category(meta, category_map):
    """Pick the site category whose keywords best match the article's keywords; default blog.
    Deterministic: first category (in map order) with the most keyword hits wins; 0 hits → default."""
    text = " ".join(meta.get("keywords", []) + [meta.get("title", "")]).lower()
    best_key, best_hits = category_map["default"], 0
    for key, cat in category_map["categories"].items():
        hits = sum(1 for kw in cat.get("keywords", []) if kw.lower() in text)
        if hits > best_hits:
            best_key, best_hits = key, hits
    cat = category_map["categories"][best_key]
    return {"key": best_key, "label": cat["label"], "path_prefix": cat["path_prefix"]}
```

- [ ] **Step 5: Run → PASS; commit** `feat(publisher): category-map + route_category`.

---

## Task 3: `build_jsonld` (Article + BreadcrumbList, Person author)

**Files:** Modify `render.py`; Test in `test_render.py`.

**Interfaces:** `build_jsonld(meta: dict, url: str) -> str` → the two `<script type="application/ld+json">…</script>`
blocks (Article with `author` = Person "Георги Тодоров", plus BreadcrumbList), concatenated.

- [ ] **Step 1: Failing test**

```python
META3 = {"title": "Как работи разиграването", "meta_description": "Кратко.",
         "date_published": "2026-09-07", "date_modified": "2026-09-07",
         "images": [{"path": "images/x.webp", "alt": "инфографика"}]}

def test_build_jsonld_person_author_and_breadcrumb():
    out = r.build_jsonld(META3, "https://vsichkikazina.bg/blog/kak-raboti-razigravaneto/")
    assert out.count('application/ld+json') == 2
    assert '"@type":"Article"' in out and '"@type":"BreadcrumbList"' in out
    assert '"author":{"@type":"Person","name":"Георги Тодоров"}' in out
    assert '"datePublished":"2026-09-07"' in out
    assert '"item":"https://vsichkikazina.bg/blog/kak-raboti-razigravaneto/"' in out
```

- [ ] **Step 2: Run → FAIL.**
- [ ] **Step 3: Implement** (append)

```python
def build_jsonld(meta, url):
    """Article (Person author = Георги Тодоров) + BreadcrumbList JSON-LD, matching the site."""
    img = "https://vsichkikazina.bg/assets/img/og-default.png"
    if meta.get("images"):
        img = url + meta["images"][0]["path"]
    article = {
        "@context": "https://schema.org", "@type": "Article",
        "headline": meta["title"], "description": meta.get("meta_description", ""),
        "image": img, "mainEntityOfPage": url,
        "datePublished": meta.get("date_published", ""),
        "dateModified": meta.get("date_modified", ""),
        "author": {"@type": "Person", "name": "Георги Тодоров"},
        "publisher": {"@type": "Organization", "name": "Всички Казина"},
        "inLanguage": "bg",
    }
    crumb = {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Начало", "item": "https://vsichkikazina.bg/"},
            {"@type": "ListItem", "position": 2, "name": meta["title"], "item": url},
        ],
    }
    dump = lambda o: json.dumps(o, ensure_ascii=False, separators=(",", ":"))
    return ('<script type="application/ld+json">' + dump(article) + "</script>\n"
            '<script type="application/ld+json">' + dump(crumb) + "</script>")
```

- [ ] **Step 4: Run → PASS; commit** `feat(publisher): build_jsonld (Person author + breadcrumb)`.

---

## Task 4: `upsert_sitemap` (idempotent by URL)

**Files:** Modify `render.py`; Test in `test_render.py`.

**Interfaces:** `upsert_sitemap(sitemap_xml: str, loc: str, lastmod: str) -> str` — returns the
XML with the `<url>` for `loc` inserted or its `<lastmod>` updated; never duplicates a `loc`.

- [ ] **Step 1: Failing test**

```python
SITEMAP = ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           '<url><loc>https://vsichkikazina.bg/</loc><lastmod>2026-09-01</lastmod></url>\n</urlset>\n')

def test_upsert_sitemap_add_then_update_no_dup():
    once = r.upsert_sitemap(SITEMAP, "https://vsichkikazina.bg/blog/a/", "2026-09-07")
    assert once.count("<loc>https://vsichkikazina.bg/blog/a/</loc>") == 1
    twice = r.upsert_sitemap(once, "https://vsichkikazina.bg/blog/a/", "2026-09-09")
    assert twice.count("<loc>https://vsichkikazina.bg/blog/a/</loc>") == 1
    assert "2026-09-09" in twice and "2026-09-07" not in twice.split("blog/a/")[1][:60]
```

- [ ] **Step 2: Run → FAIL.**
- [ ] **Step 3: Implement** (append)

```python
def upsert_sitemap(sitemap_xml, loc, lastmod):
    """Insert or update a <url><loc>…</loc><lastmod>…</lastmod></url> entry, keyed by loc."""
    entry = f"<url><loc>{loc}</loc><lastmod>{lastmod}</lastmod></url>"
    pat = re.compile(r"<url>\s*<loc>" + re.escape(loc) + r"</loc>.*?</url>", re.S)
    if pat.search(sitemap_xml):
        return pat.sub(entry, sitemap_xml)
    return sitemap_xml.replace("</urlset>", entry + "\n</urlset>")
```

- [ ] **Step 4: Run → PASS; commit** `feat(publisher): upsert_sitemap (idempotent by loc)`.

---

## Task 5: `upsert_index_card` (blog listing, idempotent by href)

**Files:** Modify `render.py`; Test in `test_render.py`.

**Interfaces:** `upsert_index_card(index_html: str, card_html: str, href: str) -> str` — inserts
`card_html` at the top of `<ul class="post-grid">`, or replaces the existing `<li>` whose link is
`href`; never duplicates.

- [ ] **Step 1: Failing test**

```python
INDEX = '<ul class="post-grid">\n<li class="post-card"><a class="post-card__link" href="/blog/old/">old</a></li>\n</ul>'

def test_upsert_index_card_add_and_replace():
    card = '<li class="post-card"><a class="post-card__link" href="/blog/a/">A</a></li>'
    once = r.upsert_index_card(INDEX, card, "/blog/a/")
    assert once.count('href="/blog/a/"') == 1 and 'href="/blog/old/"' in once
    twice = r.upsert_index_card(once, card.replace(">A<", ">A2<"), "/blog/a/")
    assert twice.count('href="/blog/a/"') == 1 and ">A2<" in twice
```

- [ ] **Step 2: Run → FAIL.**
- [ ] **Step 3: Implement** (append)

```python
def upsert_index_card(index_html, card_html, href):
    """Upsert a post-card <li> into <ul class="post-grid"> keyed by its href; newest first."""
    li = re.compile(r'<li class="post-card">(?:(?!</li>).)*?href="' + re.escape(href) + r'".*?</li>', re.S)
    if li.search(index_html):
        return li.sub(card_html.strip(), index_html)
    return re.sub(r'(<ul class="post-grid">\s*)', r"\1" + card_html.strip() + "\n", index_html, count=1)
```

- [ ] **Step 4: Run → PASS; commit** `feat(publisher): upsert_index_card (idempotent by href)`.

---

## Task 6: `render_page` (wire chrome + jsonld + fields) + state helpers

**Files:** Modify `render.py`; Test in `test_render.py`.

**Interfaces:**
- `render_page(meta, body_html, category, related_html, template, canonical) -> str` — builds the
  full page: computes JSON-LD, formats the BG date, sets byline `Георги Тодоров`, fills the template.
- `load_state(path) -> dict` / `save_state(path, state) -> None` (state = `{slug: {path, content_hash, deployed_utc}}`).

- [ ] **Step 1: Failing test**

```python
def test_render_page_fills_and_has_person_author(tmp_path):
    template = "<title>{{TITLE}}</title>{{JSONLD}}<span class=\"post-card__cat\">{{CATEGORY_LABEL}}</span>" \
               "<time datetime=\"{{DATE_ISO}}\">{{DATE_BG}}</time><h1>{{TITLE}}</h1>" \
               "<p class=\"updated\">{{AUTHOR}}</p><div>{{BODY}}</div><ul>{{RELATED}}</ul>" \
               "<link rel=\"canonical\" href=\"{{CANONICAL}}\"><meta content=\"{{META_DESC}}\">" \
               "<meta content=\"{{OG_IMAGE}}\">"
    meta = {"title": "Т", "meta_description": "оп", "date_published": "2026-09-07",
            "date_modified": "2026-09-07", "images": []}
    cat = {"key": "blog", "label": "Ръководство", "path_prefix": "blog"}
    out = r.render_page(meta, "<p>тяло</p>", cat, "<li>rel</li>", template,
                        "https://vsichkikazina.bg/blog/t/")
    assert "{{" not in out                      # no leftover placeholders
    assert '<p class="updated">Георги Тодоров</p>' in out
    assert "07.09.2026" in out                  # BG date format
    assert "Ръководство" in out and "<p>тяло</p>" in out

def test_state_roundtrip(tmp_path):
    p = tmp_path / ".published-state.json"
    r.save_state(p, {"a": {"path": "blog/a", "content_hash": "h", "deployed_utc": "t"}})
    assert r.load_state(p)["a"]["content_hash"] == "h"
    assert r.load_state(tmp_path / "missing.json") == {}
```

- [ ] **Step 2: Run → FAIL.**
- [ ] **Step 3: Implement** (append)

```python
_BG_MONTH = None  # dates are already ISO; BG display is DD.MM.YYYY


def _bg_date(iso):
    y, m, d = iso.split("-")
    return f"{d}.{m}.{y}"


def render_page(meta, body_html, category, related_html, template, canonical):
    og_image = "https://vsichkikazina.bg/assets/img/og-default.png"
    if meta.get("images"):
        og_image = canonical + meta["images"][0]["path"]
    fields = {
        "TITLE": html.escape(meta["title"], quote=True),
        "META_DESC": html.escape(meta.get("meta_description", ""), quote=True),
        "CANONICAL": canonical, "OG_IMAGE": og_image,
        "JSONLD": build_jsonld(meta, canonical),
        "CATEGORY_LABEL": category["label"],
        "DATE_ISO": meta.get("date_published", ""),
        "DATE_BG": _bg_date(meta["date_published"]) if meta.get("date_published") else "",
        "AUTHOR": "Георги Тодоров",
        "BODY": body_html, "RELATED": related_html,
    }
    return fill_template(template, fields)


def load_state(path):
    path = Path(path)
    if path.exists():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except ValueError:
            return {}
    return {}


def save_state(path, state):
    Path(path).write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
```

- [ ] **Step 4: Run → PASS; commit** `feat(publisher): render_page + state helpers`.

Note: `{{TITLE}}` appears in the real template both in `<title>`/`og:title` (attribute-safe,
escaped) and in visible `<h1>`/breadcrumb. HTML-escaping the title is safe in both places. If a
future title legitimately needs raw markup in the H1, split into `TITLE`/`TITLE_HTML` then — YAGNI now.

---

## Task 7: `seo_inspect.py` (Gemini SEO audit of the rendered HTML)

**Files:** Create `VsichkiKazina/_publisher/seo_inspect.py`, `VsichkiKazina/_publisher/prompts/seo-inspect.md`.

**Interfaces:** CLI `python3 seo_inspect.py <rendered.html>` → prints `SEO SCORE: <0-100>` + verdict
+ fixes; exit 0 ok, exit 2 unavailable. Mirrors AIContent's `gemini_check.py` (stdlib urllib,
reads `GEMINI_API_KEY`, model `gemini-3.1-pro-preview`).

- [ ] **Step 1: Write `prompts/seo-inspect.md`** — a verbatim prompt: "Act as a technical SEO
  auditor. Given a rendered HTML page, score it 0–100 for on-page SEO and list concrete fixes.
  Check: `<title>` length (~≤60), meta description (~120–160), exactly one `<h1>` + logical
  H2/H3, primary-keyword presence without stuffing, internal links present and non-empty, every
  `<img>` has non-empty `alt`, valid JSON-LD Article + BreadcrumbList, `<link rel=canonical>`
  present, OG tags present, readability, no thin content. Output first line exactly
  `SEO SCORE: <n>`; then `VERDICT: PASS|NEEDS WORK`; then bullet fixes. Do not rewrite the page."

- [ ] **Step 2: Implement `seo_inspect.py`** — copy the structure of AIContent
  `scripts/gemini_check.py` (same repo pattern): read `GEMINI_API_KEY`, POST
  `{"contents":[{"parts":[{"text": PROMPT + "\n\n---HTML---\n\n" + html}]}],"generationConfig":{"temperature":0.2}}`
  to `…/models/gemini-3.1-pro-preview:generateContent`, print the response text, exit 2 on any
  error. Add `parse_score(text) -> int|None` that reads the `SEO SCORE: <n>` line.

- [ ] **Step 3: Test `parse_score`** (no network):

```python
# tests/test_seo.py
import sys; from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import seo_inspect as s
def test_parse_score():
    assert s.parse_score("SEO SCORE: 84\nVERDICT: PASS\n- ok") == 84
    assert s.parse_score("no score here") is None
```

- [ ] **Step 4: Run → PASS; commit** `feat(publisher): seo_inspect.py + prompt`.

---

## Task 8: `deploy_ftp.py` (upload changed files, creds from env, dry-run)

**Files:** Create `VsichkiKazina/_publisher/deploy_ftp.py`; Test `tests/test_deploy.py`.

**Interfaces:** `plan_uploads(local_root: Path, rel_paths: list[str]) -> list[str]` (pure — the
files that would upload); `upload(rel_paths, dry_run=False)` (uses `ftplib.FTP` with
`FTP_HOST/USER/PASS/DIR`; `--dry-run` prints and skips network).

- [ ] **Step 1: Failing test** (dry-run path, no network/creds)

```python
# tests/test_deploy.py
import sys; from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import deploy_ftp as d
def test_plan_uploads_lists_existing(tmp_path):
    (tmp_path / "blog" / "a").mkdir(parents=True)
    (tmp_path / "blog" / "a" / "index.html").write_text("x")
    got = d.plan_uploads(tmp_path, ["blog/a/index.html", "missing.html"])
    assert got == ["blog/a/index.html"]        # missing dropped, never invented
```

- [ ] **Step 2: Run → FAIL.**
- [ ] **Step 3: Implement**

```python
#!/usr/bin/env python3
"""FTP-deploy changed files to production. Creds from env. Never invents files."""
import ftplib
import os
import sys
from pathlib import Path


def plan_uploads(local_root, rel_paths):
    """The subset of rel_paths that actually exist locally (deterministic, testable)."""
    return [p for p in rel_paths if (Path(local_root) / p).is_file()]


def upload(rel_paths, local_root=".", dry_run=False):
    local_root = Path(local_root)
    to_send = plan_uploads(local_root, rel_paths)
    if dry_run:
        for p in to_send:
            print(f"DRY-RUN would upload: {p}")
        return 0
    host, user, pw = os.environ.get("FTP_HOST"), os.environ.get("FTP_USER"), os.environ.get("FTP_PASS")
    base = os.environ.get("FTP_DIR", "").rstrip("/")
    if not all([host, user, pw]):
        print("FTP_UNAVAILABLE: FTP_HOST/FTP_USER/FTP_PASS not set", file=sys.stderr)
        return 2
    with ftplib.FTP(host) as ftp:
        ftp.login(user, pw)
        for rel in to_send:
            remote = f"{base}/{rel}" if base else rel
            _ensure_dirs(ftp, remote.rsplit("/", 1)[0])
            with open(local_root / rel, "rb") as fh:
                ftp.storbinary(f"STOR {remote}", fh)
            print(f"uploaded: {remote}")
    return 0


def _ensure_dirs(ftp, path):
    parts, cur = [p for p in path.split("/") if p], ""
    for part in parts:
        cur += "/" + part
        try:
            ftp.mkd(cur)
        except ftplib.error_perm:
            pass  # exists


if __name__ == "__main__":
    args = sys.argv[1:]
    dry = "--dry-run" in args
    files = [a for a in args if a != "--dry-run"]
    sys.exit(upload(files, dry_run=dry))
```

- [ ] **Step 4: Run → PASS; commit** `feat(publisher): deploy_ftp.py (env creds, dry-run, no invented files)`.

---

## Task 9: `brand-book.md` (derived from the live site)

**Files:** Create `VsichkiKazina/_publisher/brand-book.md`.

- [ ] **Step 1: Derive + write** — read several live pages (`blog/*/index.html`, `index.html`,
  `otgovorna-igra/`, `kak-ocenyavame/`) and codify, with concrete examples pulled from them:
  voice (calm, second-person „вие/ти" — match existing posts, factual, no hype); terminology
  (разиграване/превъртане, RTP, волатилност, НАП, лицензиран оператор); the compliance footer +
  18+ + helpline `0888 99 18 66`; **author byline = Георги Тодоров** (Person); brand name **Всички
  Казина**; internal-link policy (3–6 contextual links, ≥1 to a category/money page, natural
  anchors, only existing pages); the `post__meta` category label vocabulary
  (Ръководство/Речник/Правила/…); the operator-alt `altm` modal is kept verbatim.
- [ ] **Step 2: Commit** `docs(publisher): brand-book derived from the live site`.

---

## Task 10: `publish-run.md` (the AI-agent orchestration)

**Files:** Create `VsichkiKazina/_publisher/publish-run.md`.

- [ ] **Step 1: Write the run doc** (analogue of AIContent `daily-run.md`), steps VERBATIM:
  0. **Sync `main` first** (`git checkout main && git pull --no-rebase`); abort on dirty/conflicted.
  1. **Pull the feed** — fetch AIContent `published/index.json` + changed `<slug>/`; new/changed = `content_hash` ≠ `.published-state.json`; approved-only by construction.
  2. Build the **link-map** from the live `sitemap.xml` + page titles.
  3. Per article: **route category** (`render.route_category` + `category-map.json`); read the pinned path from state if present (stable). **Convert `article.md` → clean body HTML** in the site's classes, aligned to `brand-book.md` (preserve every number/link/RG/flag/date; author Георги Тодоров). **Insert 3–6 internal backlinks** from the link-map (≥1 category/money page, natural anchors, only existing pages, no dupes). Copy images to `<category>/<slug>/images/`. Build 3 **related-post** cards. Call `render.render_page(...)` → write `<category>/<slug>/index.html`. **Upsert** `blog/index.html` card + `sitemap.xml` (`render.upsert_index_card`/`upsert_sitemap`).
  4. **SEO inspect** the rendered file (`seo_inspect.py`): PASS ≥ 80; apply safe fixes (title/meta/headings/alt/anchors — never facts) and re-render ≤ 2×; keep-best; **hard-block** on score < 60 or a broken internal link / missing canonical|H1.
  5. **Commit** rendered files to WebPortals.
  6. **FTP-upload** the changed files (`deploy_ftp.py`) — only on a passing page.
  7. **Write status back to AIContent** — for fully-uploaded articles only: clone/pull AIContent with `AICONTENT_TOKEN`, set the queue row `status: posted` + `posted_date`, run `build_dashboard.py`, commit/push (pull-then-push). Failure/partial ⇒ leave `approved`, no write-back.
  8. **Update `.published-state.json`** (`slug → {path, content_hash, deployed_utc}`).
  - Idempotency + failure-safety + secrets exactly as the Global Constraints state.
- [ ] **Step 2: Commit** `docs(publisher): publish-run.md agent orchestration`.

---

## Task 11: End-to-end dry-run harness + docs

**Files:** Create `VsichkiKazina/_publisher/README.md`; run a full dry-run.

- [ ] **Step 1: Full suite green** — `python3 -m pytest VsichkiKazina/_publisher/tests -v` (all tasks' tests).
- [ ] **Step 2: Manual render dry-run** — write a throwaway script/notebook cell that: takes one
  real AIContent feed article (or a fixture `meta.json`+`article.md`), routes category, renders a
  page with a stub body, runs `deploy_ftp.py --dry-run` on the output path, and asserts the page
  has no `{{ }}` left, one `<h1>`, canonical set, Person author. Confirm, then delete the throwaway.
- [ ] **Step 3: Write `README.md`** — how to run the publisher, the required secrets, the schedule,
  and the "test/iterate on main" note. Commit `docs(publisher): README + dry-run verified`.

---

## Task 12: Schedule the cloud routine (needs the user's secrets)

**Files:** none (routine config).

- [ ] **Step 1: Prerequisites from the user** — set on the routine's environment:
  `FTP_HOST`, `FTP_USER`, `FTP_PASS`, `FTP_DIR`, `GEMINI_API_KEY`, `AICONTENT_TOKEN`.
- [ ] **Step 2: Create the routine** (RemoteTrigger) pointed at `ProfitXtraV2/WebPortals`, running
  `VsichkiKazina/_publisher/publish-run.md`, cron `30 6 * * 2-5` (Tue–Fri 09:30 Sofia summer;
  `30 7 * * 2-5` winter), allowed tools `Bash,Read,Write,Edit,Glob,Grep`.
- [ ] **Step 3: First run as dry-run** (a `--dry-run` / `hold` flag in `publish-run.md`) to render +
  commit without FTP, verify the built pages on a branch, then enable live deploy.

---

## Self-Review

**1. Spec coverage:** feed pull (T10), sync-main-first (T10.0), category routing (T2/T10),
deterministic chrome + Person author (T1/T3/T6), brand alignment (T9/T10), internal backlinks
(T10 + link-map), sitemap/index idempotent upsert (T4/T5), SEO inspection + gate (T7/T10),
FTP deploy (T8/T10), status write-back to `posted` (T10.7), no-duplicates/failure-safe (state in
T6, path pinning T10), schedule + secrets (T12). ✅ Covers spec §2–§10.

**2. Placeholder scan:** deterministic tasks carry complete code + tests; the agent doc (T10) and
brand-book (T9) are prose deliverables (like `daily-run.md`), not code — their content is fully
specified, not "TODO". ✅

**3. Type consistency:** `route_category` returns `{key,label,path_prefix}` consumed by
`render_page(category=…)`; `render_page(meta, body_html, category, related_html, template,
canonical)` matches its test and T10 call; `upsert_sitemap`/`upsert_index_card` signatures match
their tests and T10. `meta` keys come from the feed contract (`PUBLISHED_FEED.md`). ✅

## Dependencies / notes
- Depends on sub-project 1 (the `published/` feed) — now merged to AIContent `main`. ✅
- Live deploy + write-back need the T12 secrets (user-provided); everything else builds + dry-runs without them.
- Template can go stale if the site's chrome/CSS-version changes — refresh `templates/blog-post.html` from a live post when that happens.
