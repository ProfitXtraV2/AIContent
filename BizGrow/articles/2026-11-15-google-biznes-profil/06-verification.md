# 06-verification — /saveti/google-biznes-profil/ (Step 6)

Run by the orchestrator (fresh read of the Step 6 inputs: 05b-final-draft.md, 00-current.md, 00-inventory.md, verification-policy.md, site-rules.md, content-file template, keyword-map.md). Content file and port JSON generated from one data structure by `_tmp/build.py`, so the strings are identical in both.

## RESOLVED-TO-OWNER-ITEMS
| # | claim | URL | HTTP | quote |
|---|---|---|---|---|
| F1 | added + verified profile → found in Search and Maps; add/claim without monetary payment | https://support.google.com/business/answer/2911778?hl=bg | 200 (curl -sL, 2026-11-15) | „Когато добавите и потвърдите бизнес профила си, клиентите могат да намират бизнеса ви в Търсене и Карти.“ / „Можете да добавите или заявите бизнеса си без парично заплащане.“ |
| F2 | verification gives ownership; options depend on business type | https://support.google.com/business/answer/7107242?hl=bg | 200 | „Когато потвърдите бизнеса си в Google, придобивате собствеността върху бизнес профила си“ / „Наличните за вас опции за потвърждаване зависят от типа на бизнеса ви“ |
| F3 | verification reviews up to 5 working days, rarely longer | same as F2 | 200 | „прегледите за потвърждаване отнемат до 5 работни дни“ / „В редки случаи прегледите може да отнемат повече време.“ |
Procedural steps in #syzdavane / #zayavyavane and the ownership-request sentence paraphrase S1 („Отворете business.google.com/add.“, „Кликнете върху Добавете бизнеса си в Google.“, „Изберете „Заявяване на този бизнес““, „…можете да подадете заявка за собственост до настоящия му собственик.“). UI labels used: only „Добавете бизнеса си в Google“ and „Заявяване на този бизнес“, both verbatim in S1.
The #danni list (име, адрес, телефон, уебсайт, работно време, снимки и видеоклипове) is general advice that matches support.google.com/business/answer/7039811 („Предоставете работното време, уебсайта, телефонния номер и местоположението си…“, „Публикувайте снимки и видеоклипове…“) but is not presented as a Google claim; not counted as a sourced fact and not listed in [[sources]].

OWNER CONFIRM markers → owner items 5–10; gate items carried. One non-canon sentence removed at Step 6 per „keep only what is known“: #bizgrow „Нищо не се публикува без Вашето одобрение.“ (approval for profile posts/photos is not in canon; owner item 11).

## REMAINING FOR HUMAN
- None blocking. The /diagnostika/ open item 21 („отзиви“ vs „оценки и коментари“) affects this page too (owner item 8).

## PORTING NOTES
- New file `site/src/content/pages/bg/google-biznes-profil.ts`: export a `ContentPage` with the object in `content/google-biznes-profil.port.json` (no `service` key, `eyebrow` „Съвети“), register it in `site/src/content/index.ts`, and list it on the /saveti/ hub (card uses `label` + `summary`).
- Sections use `paragraphs`, `bullets`, `steps`, `closing` (types.ts @ a1ccf8f). The booking CTA and the email line are paragraphs of #bizgrow (same pattern as the seo-statii port).
- The content file's `hero` section holds only the lead (`lead` in the port); it is not a port section.

## SELF-CHECK (python 3.14 tomllib)
| check | result |
|---|---|
| TOML parses | PASS |
| title ≤ 60 incl. „ | BizGrow“, no em-dash | PASS (54) |
| meta 120–160 with main term | PASS (140) |
| summary ≤ 160 | PASS (148) |
| primary_keyword = keyword-map term; title / first 100 words / one H2 | PASS (H1 is the keyword-map proposal with the variant „Google бизнес профил“) |
| section ids/headings = body blocks, in order | PASS (hero + 8) |
| question-led H2s 6–8 | PASS (8) |
| body 900–1,400 words excl. FAQ | PASS (918 sections only; 978 with lead) |
| FAQ 4–6 | PASS (6) |
| em-dashes / bracketed markers / „ти“ forms | 0 / 0 / 0 |
| banned claims, hype, price/offer/testimonial („отзив*“) | 0 in visible copy |
| „доклад“ / delivery periods | 0 / 0 (only „30-минутен разговор“) |
| numbers | 30 (canon), 5 (F3 sourced), step numbering only |
| „безплатн*“ only for the diagnosis | PASS (2) |
| booking CTA exactly one; {{EMAIL}} | PASS (1; 1) |
| links in conversion-links.md | PASS (/ai-asistent/, /socialni-mrezhi/, /diagnostika/) |
| inventory I1–I8 | PASS: I1 „[Запазете безплатна диагностика]({{BOOKING_URL}})“; I2 „[безплатната диагностика](/diagnostika/)“; I3 „[поддържа профила жив](/socialni-mrezhi/)“; I4 „[AI асистент](/ai-asistent/)“; I5 „с публикации, снимки и актуална информация всеки месец“; I6 „подготвяме отговор за Вашето одобрение“; I7 „30-минутен разговор … оферта с приоритизирани решения и ясни еднократни цени. Срокът зависи от решението и го посочваме в офертата.“; I8 „Диагностиката не Ви обвързва с нищо. Работим без дългосрочни договори.“ |
| port: strings identical to the content file; related = 3 sibling paths; no em-dash | PASS |

new facts: 3
owner items added: 12
