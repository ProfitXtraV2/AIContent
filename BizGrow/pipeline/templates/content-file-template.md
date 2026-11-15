<!--
BizGrow content file template (Step 6 deliverable: articles/<date>-<slug>/content/<slug>.md).

WHY MARKDOWN + TOML: the BizGrow site is a Next.js static export. Its copy lives in typed
TypeScript dictionaries (site/src/i18n/dictionaries/bg.ts and en.ts, type in
site/src/i18n/types.ts) and page components, NOT in Markdown files. This file is a PORTING
SOURCE: the human / the owner's session copies each section into the matching dictionary key
(`dictionary_key`) or creates a new key + component for a new section, then runs `npm run lint`,
`npx tsc --noEmit` and `npm run build` in the site repo. The pipeline never edits the site repo.

RULES: TOML must parse (python3 tomllib). No em-dashes. No bracketed markers. No „ти“ forms
(bg). Every [[sections]] entry has exactly one body block `## <heading> {#<id>}` with the same
heading and id, in the same order. EN files use the same section ids as their BG pair.
Remove this comment block in the delivered file.
-->
+++
title = "<main term or page name> | BizGrow"            # ≤ 60 characters incl. " | BizGrow"; no em-dash
meta_description = "<120–160 characters, contains the primary keyword, written for this page>"
h1 = "<current H1 or keyword-map proposal; a change gets an owner item>"
slug = "<home | en-home | keyword-map slug>"
locale = "<bg | en>"
primary_keyword = "<exactly the keyword-map term for this address>"
secondary_keywords = ["<term>", "<term>"]
status = "draft"
last_updated = "<YYYY-MM-DD, run date>"

[[sections]]
id = "<anchor id, e.g. hero>"
heading = "<visible heading; for the hero this is the H1 lines>"
kind = "<hero | paragraphs | list | steps | cards | table | cta | contact | faq>"
dictionary_key = "<existing key, e.g. hero, services, process.steps; empty string for a new section>"

[[sections]]
id = "<next anchor>"
heading = "<…>"
kind = "<…>"
dictionary_key = "<…>"

[[faq]]
q = "<question in the page's language>"
a = "<1–3 complete, formal sentences>"

[[sources]]
title = "<only for Tier B external facts>"
url = "<https://…, returned 200 on the run date>"
checked_by = ""
checked_on = ""

[[owner_items]]
item = "<existing items first, unchanged; then new ones: what changed or what the owner must confirm/supply>"
decision = ""
decided_by = ""
decided_on = ""
+++

## <hero heading> {#hero}

<Opening: the first sentence states what BizGrow offers on this page; main term once in the first 100 words.>

[<Запазете безплатна диагностика | Book a free diagnosis>]({{BOOKING_URL}})

## <section heading> {#<id>}

<Paragraphs of 2–4 sentences, or a list:>
- **<Card title>.** <1–2 sentence body.>

## <example section heading, if any> {#results}

<Explicit label: „Примерни сценарии по нашия метод, не данни от конкретни клиенти.“>

## <contact heading> {#contact}

<Booking CTA via {{BOOKING_URL}}; email via {{EMAIL}}.>
