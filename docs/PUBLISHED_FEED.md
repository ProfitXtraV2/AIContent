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
