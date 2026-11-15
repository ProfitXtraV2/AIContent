# 06-verification — /avtomatizacii/ (BizGrow, new-page, bg), 2026-11-15

Step 6 run by the orchestrating agent (not a subagent), from 05b-final-draft.md. The content file and the port JSON are generated from one data structure (scratchpad build script), so every port string is byte-identical to the content file.

## RESOLVED-TO-OWNER-ITEMS
- No `[VERIFY]` external facts (0 new sources; `[[sources]]` empty). The Step 3 `[VERIFY]` on the listing line was cleared at Step 5 against the owner checker line („Публикуваш веднъж: системата качва, обновява и сваля навсякъде“, docs/content-sources/skriti-problemi.json); kept as a confirm-by-reading owner item.
- `[OWNER CONFIRM]` #kakvo-e „Правилата определяме заедно с Вас, а Вие решавате кои задачи остават в ръцете на Вашите хора.“ → sentence REMOVED (not canon); owner item 2.
- `[OWNER CONFIRM]` (Step 5, no marker) client picking a subset of fixes → owner item 3; text already canon-only.
- `[OWNER CONFIRM]` #za-kogo hotels → marker removed, text kept (all items canon: documents/dashboard are "all businesses" in the checker, guest AI assistant is canon); owner item 4.
- `[OWNER CONFIRM]` FAQ 5 → marker removed, canon answer kept; owner item 5.
- `[DATA NEEDED]` reminder channel → marker removed; owner item 6 („sms напомняне“ unplaced).
- `[DATA NEEDED]` FAQ 7 data handling → marker removed, „Да, работим по GDPR.“ kept; owner item 7.
- Step 6 standard items: new page H1/title/meta/label/eyebrow/summary approval (owner item 1); no „ти“→„Вие“ conversions (new page); no example scenarios (no label needed). Optional FAQ candidates (owner item 9).

## REMAINING FOR HUMAN
- none (no `[LINK NEEDED]`).
- Step 7 Gemini: skipped (no GEMINI_API_KEY locally).

## PORTING NOTES
- `content/avtomatizacii.port.json` is a ready `ContentPage` object (status "published", updated 2026-11-15). The `hero` section of the content file maps to `h1` + `lead`, not to `sections[]`.
- `kak-rabotim` uses `steps` (numbered list), per the coordinator's mid-run update; other lists use `bullets`.
- `tsena` keeps `[Запазете безплатна диагностика]({{BOOKING_URL}})` and the bare `{{EMAIL}}` inside paragraph strings (the renderer now resolves both). The template also shows a booking button under the lead and a CtaBand, so the page will have three booking entry points; drop the paragraph CTA at port if that is too many.
- `eyebrow` = „Услуги“ (Step 4 fallback); optional.
- No dictionary (`bg.ts`) keys change; the page lives in `site/src/content/pages/bg/`.

## SELF-CHECK
| check | result |
|---|---|
| TOML parses (python 3.14 tomllib) | pass |
| title ≤ 60 incl. " | BizGrow", no em-dash | 60, pass |
| meta_description 120–160, contains main term | 151, pass |
| primary_keyword = keyword-map term | pass |
| main term once each in title, H1, first 100 words (lead), one H2 (#kakvo-e) | pass (body count 3 = H1 block, lead, H2) |
| [[sections]] ids/headings = body blocks, same order | pass |
| em-dash / en-dash / "!" | 0 / 0 / 0 |
| bracketed markers | 0 |
| „ти“ forms | 0 (one regex hit „те“ = plural pronoun „they“, false positive) |
| banned claims / hype / PRICE / OFFER / TESTIMONIAL | 0 |
| „безплатн*“ only with the diagnosis | pass (9/9) |
| numbers | canon only: 30-минутен, 48 часа, обикновено до 2 седмици (+ step list numbering, „B2B“) |
| example label | n/a (no example scenarios) |
| inventory 00-inventory.md | 19/19 (item 18 n/a) |
| links in conversion-links.md | /ai-asistent/, /diagnostika/ + tokens {{BOOKING_URL}}, {{EMAIL}}; related /ai-asistent/, /diagnostika/, /seo-statii/ |
| port JSON strings identical to content file | pass (0 missing) |

Counts: new facts: 0 | owner items added: 9 | body words (H1 + lead + 8 sections, no FAQ): 971 | FAQ: 8 (197 words)
