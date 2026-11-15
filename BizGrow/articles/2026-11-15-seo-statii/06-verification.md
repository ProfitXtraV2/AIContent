# 06-verification — /seo-statii/ (Step 6, 2026-11-15)

Run by the orchestrator session (not a separate subagent), reading only the Step 6 inputs: 05b-final-draft.md, 00-current.md, 00-inventory.md, reference/verification-policy.md, reference/site-rules.md, templates/content-file-template.md, keyword-map.md. Python ≥ 3.11 for tomllib: /opt/homebrew/bin/python3.14 (system python3 lacks tomllib).

## RESOLVED-TO-OWNER-ITEMS
- [VERIFY] #kakvo-e, Google people-first content. URL https://developers.google.com/search/docs/fundamentals/creating-helpful-content → `curl -sI` HTTP/2 200 (2026-11-15). Quotes:
  - „Google's automated ranking systems are designed to prioritize helpful, reliable information that's created to benefit people, and not content that's created to manipulate search engine rankings.“
  - „Answering yes to some or all of the questions below is a warning sign that you should reevaluate how you're creating content: Is the content primarily made to attract visits from search engines?“
  Confirmed → sentence kept, marker removed, `[[sources]]` + owner item 9.
- [OWNER CONFIRM] H1 → owner item 1.
- [OWNER CONFIRM] tool handles keywords/meta descriptions → owner item 2 (text kept: general SEO practice list, not a tool claim).
- [DATA NEEDED] volume/frequency/platforms → owner item 3 (text states none).
- [OWNER CONFIRM] human review / team → owner item 4.
- [OWNER CONFIRM] languages / tone → owner item 5.
- [OWNER CONFIRM] process step 3 wording → owner item 6; the non-canon sentence „Настройваме инструмента за съдържание за Вашия бранш, град и продукти.“ REMOVED (keep only what is known); step reads „Изграждане, обикновено до 2 седмици.“
- [OWNER CONFIRM] ongoing pricing → owner item 7 (marker removed; text unchanged, canon only).
- Brand Gate owner item (client chooses fixes; sentence deleted at Gate) → owner item 8.
- New page copy (eyebrow, label, summary, FAQ) → owner item 10.
- No „ти“→„Вие“ conversions (new page). No example scenarios (no label needed).

## REMAINING FOR HUMAN
- None from [LINK NEEDED] (none raised).
- Porting: the `{{BOOKING_URL}}` CTA line and the `{{EMAIL}}` line in #diagnostika cannot be expressed in `ContentPage` (inline syntax is `**bold**` and `[label](/path/|#anchor)` only; `rich()` would print the token literally). They are kept in content/seo-statii.md and OMITTED from seo-statii.port.json. The page template (`ContentPageView.tsx`) already renders a `BookingLink` (t.nav.cta) and a /diagnostika/ button in the header; the email line needs either a site-wide contact block or token support in `rich()`. Decide at porting.

## PORTING NOTES
- Target: new file `site/src/content/pages/bg/seo-statii.ts` exporting a `ContentPage` built from content/seo-statii.port.json (strings generated programmatically from the content file, identical text). Register it in `site/src/content/index.ts`.
- No dictionary keys change; no new `Dictionary` type keys needed. The home card „SEO копирайтинг“ / „Съдържание, което те извежда в Google.“ (bg.ts services.items[1]) is outside this page; a home rewrite should replace it (implies a ranking outcome, „ти“ form) and link to /seo-statii/.
- The `hero` section of the content file maps to `h1` + `lead` (not to `sections`). Extra front-matter keys `path`, `eyebrow`, `label`, `summary`, `service`, `related` carry the remaining ContentPage fields.
- #proces numbered steps become `bullets` (rendered as a disc list); the numbering in the bold labels is lost. Optional: keep as is, or add numbering support.
- `status` is "draft" in the content file (pipeline rule) and "published" in the port JSON (per run brief); publication still needs the owner's approval of the owner items.

## SELF-CHECK
| check | result |
|---|---|
| TOML parses (python3.14 tomllib) | pass |
| title ≤ 60 incl. " | BizGrow", no em-dash | pass (56) |
| meta_description 120–160, contains primary keyword | pass (148, „SEO копирайтинг“) |
| primary_keyword = keyword-map term „seo копирайтинг“ | pass |
| main term once each in title, H1, first 100 words (lead), one H2 (#kakvo-e) | pass (body total 3 = H1, lead, H2) |
| no sibling main term targeted („seo оптимизация“ appears once as a descriptive mention + link to /seo-optimizacia/; not in title/H1/H2) | pass |
| every [[sections]] id has one body block, same heading, same order | pass (scripted) |
| 5–8 H2 / 5–8 FAQ | pass (8 / 8) |
| em-dash 0, en-dash 0 (md + port JSON) | pass |
| bracketed markers 0 (body, front matter, port JSON) | pass |
| „ти“ forms 0 | pass (one quoted „в твоя тон“ in an owner item reworded) |
| banned claims / hype (site-rules §2) 0 | pass |
| PRICE / OFFER / TESTIMONIAL 0 | pass |
| „безплатн*“ only for the diagnosis | pass (3, all diagnosis) |
| numbers only canon (30, 48, обикновено до 2) or list numbering (1–4) | pass |
| example scenarios carry label | n/a (none) |
| links only from conversion-links.md | pass (/socialni-mrezhi/, /diagnostika/, /seo-optimizacia/, {{BOOKING_URL}}, {{EMAIL}}) |
| port JSON: related = 3 sibling paths, not / or itself | pass |
| port JSON: inline syntax only bold + root/anchor links | pass (token lines omitted, see above) |

## INVENTORY (00-inventory.md)
- I1 #diagnostika „[Запазете безплатна диагностика]({{BOOKING_URL}})“
- I2 #diagnostika „изпратете имейл на {{EMAIL}}“
- I3 #proces „[безплатната диагностика](/diagnostika/)“
- I4 #uslugi „Нашият собствен инструмент за съдържание поема писането на статии…“
- I5 #uslugi „Статии за Вашия бранш и Вашия град…“
- I6 #uslugi „SEO описания на продуктите за цели колекции…“
- I7 #uslugi „AI изображения към статиите и публикациите…“
- I8 #uslugi „Текст и изображение, които се публикуват по график“
- I9 #odobrenie „Нищо не се публикува без Вашето одобрение“
- I10 #proces „Безплатна диагностика и 30-минутен разговор.“
- I11 #proces „Доклад до 48 часа. … приоритизирани решения и ясни еднократни цени.“
- I12 #proces „Изграждане, обикновено до 2 седмици.“
- I13 #proces „Поддръжка с кратък месечен отчет.“
- I14 #cena „Цената зависи от това какво изграждаме… еднократна за всяко решение… в доклада след диагностиката“
- I15 #cena „Работим без дългосрочни договори.“ „Цените са прозрачни…“
- I16 #diagnostika „Диагностиката не Ви задължава с нищо.“
All 16 present.

## COUNTS
new facts: 1 · owner items added: 10 · body words (H1+lead+sections, excl. FAQ): ~769 · FAQ words: ~266
