# Published Feed — the contract

`published/` is AIContent's generic, git-native feed of **approved (ready-to-deploy)**
articles. Any target site pulls it and renders it. Built by `scripts/build_feed.py`.

## Layout
```
published/
  index.json                 # manifest (see below)
  <slug>/
    article.md               # final body (markdown, from the H1 on)
    meta.json                # metadata (schema below)
    images/…                 # the article's images (svg/webp)
```

## meta.json (schema_version 1)
| field | type | notes |
|---|---|---|
| schema_version | int | 1 |
| slug | string | folder minus leading YYYY-MM-DD- |
| title | string | title-tag (else H1, else query) |
| meta_description | string | ~120–160 chars |
| body_path | string | always "article.md" |
| author | string | "Георги Тодоров" |
| date_published / date_modified | string | ISO date |
| keywords | string[] | target keywords |
| images | array | {path, alt} |
| section_hint | string | generic type (guide/review/comparison/news) — NOT a site category |
| content_hash | string | sha256 of meta(minus hash)+body; drives idempotency |
| status | string | always "approved" (only ready-to-deploy articles are in the feed) |

## index.json
`{schema_version, count, generated_utc, articles:[{slug,title,date_modified,content_hash,status}]}`
— consumers diff `content_hash` to find new/changed articles.

## Article library (not read by publishers)

`library/<brand>/` keeps a copy of every **approved and live** item, for social posts (product
spec A8). Built by `scripts/build_library.py` in the approve-on-merge job and the social board
workflow. **Publishers never read it.** The feed above is built exactly as before: the list of
approved items, their files and their `content_hash` do not change, and live copies and the live
marker stay outside `published/` (`scripts/tests/test_feed_unchanged.py`).

```
library/<brand>/
  index.json                 # {library_schema, brand, items:[{slug,id,kind,board_status,live,article_version}], missing:[…]}
  <slug>/
    item.json                # library_schema 1 (below)
    article.md               # the article body, as text
```

`item.json`: `brand`, `id`, `slug`, `kind` (`article` | `hub-intro`), `type`, `board_status`
(`approved` | `posted`), `live` (board `posted`), `folder`, `pr`, `title`, `meta_description`,
`keywords`, `body_path`, `images` (`{path, name, alt, sha256, review: {score, integrity_ok,
source}}`), `article_version`, `operator_or_bonus` (+ reason), `built_utc`.

**The article version** is the sha256 of the canonical JSON `{title, meta_description, body,
images: [{name, alt, sha256}]}`: only what a post can quote. Status, the live marker, the
opportunity score and dates are left out, so going live alone never changes it. It is not the
feed's `content_hash`, which also covers status, score and dates.

Image review scores come from the article's last `08-image-review-*.md`, and only when it names
the image unambiguously; otherwise `score` is `unknown`.
