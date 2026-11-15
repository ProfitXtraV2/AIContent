# 06-verification: /reklama/ (bg, new-page)

Run: 2026-11-15, Step 6, fresh context. Inputs: 05b-final-draft.md (body = gate version verbatim), 05-gate-report.md (OWNER ITEMS 1-10), 00-current.md, 00-inventory.md, BizGrow/keyword-map.md, BizGrow/conversion-links.md, pipeline/reference/verification-policy.md, pipeline/reference/site-rules.md, pipeline/templates/content-file-template.md, biz-grow-seo `site/src/content/types.ts` (read-only).

Deliverables:
- `content/reklama.md` (Markdown + TOML front matter, status "draft")
- `content/reklama.port.json` (ContentPage object, generated mechanically from the content file so every string is identical)

## RESOLVED-TO-OWNER-ITEMS

HTTP check: `curl -sI -L -A 'Mozilla/5.0'` returns **404 for HEAD** on both support.google.com pages (Google Help does not answer HEAD requests); a full GET (`curl -sL -A 'Mozilla/5.0' -w '%{http_code}'`) returns **200** for both, with the expected Bulgarian page titles. The passages below are quoted from the GET response body (HTML stripped).

| # | claim on the page | where | URL | GET | quote (bg) | verdict |
|---|---|---|---|---|---|---|
| F1 | „Google таксува рекламодателя само когато някой кликне върху рекламата.“ / „Google таксува при клик върху рекламата.“ / FAQ 1 „Google таксува само при клик“ / FAQ 3 „рекламодателят плаща само когато някой кликне“ | #kak-raboti, #cena, FAQ 1, FAQ 3 | https://support.google.com/google-ads/answer/6227565?hl=bg (title „Използване на Google Ads за онлайн маркетинг“) | 200 | Under the heading „Колко плащате за Google Ads“: „С оферирането за цена на кликване (CPC) Ви таксуваме само когато някой е достатъчно заинтересуван да кликне върху рекламата Ви и да посети уебсайта Ви.“ | Supported for CPC bidding, which the source presents as the answer to „Колко плащате за Google Ads“. **Caveat:** the source scopes it to CPC and the same section adds „При кампании, за които плащате за реализации, е възможно дневните разходи да надвишават дневния Ви бюджет повече от 2 пъти.“ The page states it without the CPC qualifier. Kept (removal would also orphan the PPC gloss and FAQ 3); the caveat is written into owner item 1 and listed under REMAINING FOR HUMAN. Not altered here (policy: never alter a fact to match a source). |
| F2 | „Вие решавате каква средна сума да се изразходва за рекламата всеки ден, тоест какъв да бъде дневният бюджет.“ / #cena / FAQ 1 „Вие решавате средната дневна сума“ | #kak-raboti, #cena, FAQ 1 | https://support.google.com/google-ads/answer/6227565?hl=bg | 200 | „Вие контролирате бюджета си в Google Ads. Вие решавате средната сума, която искате да изразходвате всеки ден.“ (and „…средния Ви дневен бюджет…“) | Supported verbatim. Kept. |
| F3 | „Според Google то зависи от конкуренцията с други рекламодатели и от рекламния ранг…“; „По-високата сума сама по себе си не осигурява определено място.“; FAQ 2 „По-високата сума сама по себе си не осигурява най-горното място.“ | #kak-raboti, FAQ 2 | https://support.google.com/google-ads/answer/2472742?hl=bg (title „Показване на рекламите Ви на първа страница“) | 200 | „Покриването или надвишаването на тази прогнозна стойност обаче не Ви гарантира рекламно разположение. Крайното разположение продължава да зависи от конкуренцията на други рекламодатели, рекламния Ви ранг, настройките Ви за бюджета и профила, както и поведението на потребителите.“ The estimates the passage refers to include „Прогноза за офертата за първа позиция“. | Supported (the page names two of the four factors after „не зависи само от сумата“, which is accurate; FAQ 2's „най-горното място“ matches the first-position estimate). Kept. |

All three facts: inline `[VERIFY]` markers removed, both URLs in `[[sources]]` with empty `checked_by`/`checked_on`, one owner item each (items 1-3). Sourced facts on the page: 3 (policy maximum).

`[OWNER CONFIRM]` inline markers (2) removed: #cena pricing model (owner item 4) and ad budget vs fee (owner item 5); neither left a claim in the text. `[DATA NEEDED]` (2, not inline) → owner items 7 and 8. No `[LINK NEEDED]` markers.

## REMAINING FOR HUMAN

1. **F1 wording (judgement call, flagged not patched).** The source limits „таксуваме само когато … кликне“ to CPC bidding („С оферирането за цена на кликване (CPC)“) and mentions pay-for-conversions campaigns. The page's #kak-raboti sentence, #cena sentence, FAQ 1 and FAQ 3 state charge-on-click without that qualifier. If the owner or reviewer wants strict alignment, re-run from Step 2/4 (where the sentence originated) adding „при оферирането за цена на кликване“; Step 6 does not rewrite facts.
2. HEAD vs GET: both Google Help URLs answer HEAD with 404 and GET with 200. If a later automated link check uses HEAD only, it will report these sources as broken; check with GET.
3. Meta (Facebook/Instagram) facts: none on the page (the Meta help page was JS-rendered at Step 0 and not used); no claim about Meta pricing or placement was added.
4. No sentence was removed in this step.

## PORTING NOTES

- **New page, no dictionary keys change.** The page is a `ContentPage` object (`site/src/content/types.ts`), not a dictionary entry: all `[[sections]]` have `dictionary_key = ""`. Suggested file: `site/src/content/pages/bg/reklama.ts` exporting the object in `content/reklama.port.json`. No new key in `Dictionary` (`site/src/i18n/types.ts`) is needed. Nav/cards that list services may need the label/summary (owner item 13).
- **status:** the content file is `status = "draft"` (pipeline rule: never approved); the port JSON is `"status": "published"` as requested by the launching session so the page builds. Publishing still waits for the owner items, in particular item 11 (whole new page).
- **Hero mapping:** the hero block (`{#hero}`) → `h1` + `lead`. The hero has a single paragraph and no CTA line, so `lead` is that paragraph verbatim. `eyebrow`, `label`, `summary`, `service`, `related` come from the extra front-matter keys.
- **Sections:** 8 sections, ids and titles = body blocks. Paragraph text, `bullets` (#specialist, #za-kogo; leading „- “ removed) and `steps` (#proces; leading „1. “-„4. “ removed, numbering left to the ordered-list renderer) are copied verbatim.
- **CTAs and tokens:** per the launching session's update (the site now renders `[label]({{BOOKING_URL}})`, `[label](mailto:{{EMAIL}})` and a bare `{{EMAIL}}` in any string, and `types.ts` documents this), the booking CTAs are kept exactly as in the content file: #proces `[Запазете безплатна диагностика]({{BOOKING_URL}})` and #diagnostika `[Запазете час]({{BOOKING_URL}})`, each as its own string in `paragraphs`. The #diagnostika bare `{{EMAIL}}` is kept inside its sentence. No replacement with /diagnostika/ and no template-level CTA needed.
- **Order in #proces:** content order is paragraph, CTA, numbered steps. In the port the CTA is the second `paragraphs` entry and the steps render after paragraphs, so the visual order is identical.
- **FAQ:** 8 entries, `q`/`a` → `question`/`answer` verbatim; FAQ 5 keeps the /socialni-mrezhi/ link.
- **Internal links used:** /seo-optimizacia/ (#kak-raboti), /socialni-mrezhi/ (#facebook-instagram, FAQ 5), /diagnostika/ (#proces step 1). The pages /seo-optimizacia/ and /socialni-mrezhi/ must exist (or links be hidden) when this page goes live; /reklama/ itself must be added to any sitemap/related lists of its siblings.
- **Sources:** not rendered by ContentPage; the human decides whether to show them.
- After porting: `npm run lint`, `npx tsc --noEmit`, `npm run build` in the site repo (pipeline does not run these).

## SELF-CHECK

Script: scratchpad `reklama_selfcheck.py` (Python 3.14, tomllib), run on the final files. Result: **67/67 PASS, 0 FAIL.** (An initial run flagged digits 1-4; these were the Markdown step numbering, the check was corrected to ignore list numbering. No file content changed.)

| check | result | detail |
|---|---|---|
| TOML parses (tomllib) | PASS |  |
| port JSON parses | PASS |  |
| primary_keyword == keyword-map term | PASS | реклама в гугъл |
| title <= 60 incl. | BizGrow | PASS |
| meta_description 120-160 | PASS | 148 chars |
| meta contains main term | PASS |  |
| sections == body blocks (id, heading, order) | PASS | 9 blocks |
| hero first, kind hero | PASS |  |
| 8 H2 sections after hero | PASS |  |
| dictionary_key empty for all | PASS |  |
| hero heading == h1 | PASS |  |
| main term in title (once) | PASS |  |
| main term in H1 (variant Google, owner item) | PASS | „Google“ in H1, title uses „Гугъл“ |
| main term in first 100 words | PASS |  |
| main term in exactly one H2 | PASS | Как работи рекламата в Гугъл за малък бизнес |
| zero em-dash in whole file | PASS |  |
| zero em-dash in port JSON | PASS |  |
| zero bracketed markers (file) | PASS |  |
| zero „ти“ forms in visible text | PASS | [] |
| zero lowercase courtesy pronouns | PASS | [] |
| no 2nd-sg verb endings (-иш/-еш/-аш/-яш) | PASS | [] |
| zero banned claims/hype | PASS | [] |
| „безплатн*“ only for the diagnosis | PASS | [] |
| zero PRICE | PASS |  |
| zero OFFER | PASS |  |
| zero TESTIMONIAL | PASS |  |
| GDPR only owner wording | PASS |  |
| numbers only canon (2, 30, 48) | PASS | ['2', '30', '48'] |
| every link in conversion-links.md | PASS | ['/diagnostika/', '/seo-optimizacia/', '/socialni-mrezhi/', '{{BOOKING_URL}}'] |
| no hard-coded URL/email in visible text | PASS |  |
| {{BOOKING_URL}} x2 (#proces, #diagnostika), max one per section | PASS |  |
| {{EMAIL}} present | PASS |  |
| CTA wording approved | PASS |  |
| related = 3 paths from conversion-links, not / or /reklama/ | PASS |  |
| inventory I1 booking CTA | PASS | „[Запазете безплатна диагностика]({{BOOKING_URL}})“ |
| inventory I2 EMAIL | PASS | „{{EMAIL}}“ |
| inventory I3 /diagnostika/ | PASS | „(/diagnostika/)“ |
| inventory I4 real specialist plans/runs/tracks | PASS | „жив маркетинг специалист планира, пуска и следи“ |
| inventory I5 reports with numbers | PASS | „отговаря пред Вас с числа“ |
| inventory I6 each invested euro | PASS | „какво връща всяко вложено евро“ |
| inventory I7 planning+execution, report | PASS | „поема планирането и изпълнението, а при Вас остава отчетът“ |
| inventory I8 data-driven campaigns | PASS | „Кампании на база данни“ |
| inventory I9 Google + Facebook/Instagram | PASS | „Реклама във Facebook и Instagram“ |
| inventory I10 creatives monthly -> /socialni-mrezhi/ | PASS | „рекламни материали можем да подготвяме всеки месец“ |
| inventory I11 free diagnosis + 30-min call | PASS | „безплатна диагностика и 30-минутен разговор“ |
| inventory I12 48h report, one-off prices | PASS | „До 48 часа получавате доклад с приоритизирани решения и ясни еднократни цени“ |
| inventory I13 usually up to 2 weeks | PASS | „обикновено до 2 седмици“ |
| inventory I14 monthly support + report | PASS | „месечна поддръжка, за която получавате кратък месечен отчет“ |
| inventory I15 no long-term contracts | PASS | „без дългосрочни договори“ |
| inventory I16 transparent prices | PASS | „Цените ни са прозрачни“ |
| inventory I17 GDPR | PASS | „Работим по GDPR.“ |
| inventory I18 commits to nothing | PASS | „не Ви обвързва с нищо“ |
| inventory I10 link /socialni-mrezhi/ | PASS |  |
| port meta.title == title | PASS |  |
| port meta.description == meta_description | PASS |  |
| port label/summary/eyebrow/service equal | PASS |  |
| port lead == hero body | PASS |  |
| port faq == [[faq]] | PASS |  |
| port section ids/titles == body blocks | PASS |  |
| every port section string occurs verbatim in content body | PASS | [] |
| every content body line present in port JSON | PASS | [] |
| port status/path/updated/locale | PASS |  |
| port inline syntax allowed only | PASS | [] |
| port meta.title <= 60, description 120-160 | PASS |  |
| content file status draft, last_updated | PASS |  |
| sources: empty checked_by/on | PASS | 2 sources |
| owner_items: decision fields empty | PASS | 15 items |

Example scenarios: none on the page (I19 n/a), so no example-label check applies. FAQ answers are 1-3 sentences, none repeats a body heading word for word.

## COUNTS

- Body word count (H1 + lead + 8 section headings and bodies, excluding FAQ; link URLs and tokens not counted): **749**
- FAQ word count: 274
- Sections: hero + 8 H2 | FAQ: 8 | bullets: 10 (4 + 6) | steps: 4
- Booking CTAs: 2 (`{{BOOKING_URL}}`) | `{{EMAIL}}`: 1 | internal links: 4 (3 distinct paths)
- title: 59 characters | meta_description: 148 characters
- new facts: 3 (F1-F3, Tier B, sources 2)
- owner items carried from gate report: 10 (items 1-10)
- owner items added: 5 (items 11-15: new page as a whole, H1, label/summary/eyebrow/service/related, „ти“→„Вие“ paraphrases, „отстъпки“→„оферти“)
- owner items total: 15 | sentences removed: 0

## OWNER ITEMS (as in the content file)

1. F1 charge on click (CPC caveat), source 6227565, quote.
2. F2 advertiser decides the average daily amount, source 6227565, quote.
3. F3 placement depends on competition and ad rank; higher amount does not assure placement, source 2472742, quotes.
4. Pricing model of the specialist's ongoing work vs canon one-off price per solution.
5. Is the ad budget paid to Google/Meta separate from BizGrow's fee (no claim in text).
6. Title „Гугъл“ vs H1 „Google“; label, summary, eyebrow (carried from gate item 6).
7. Whose ad account is used (DATA NEEDED).
8. Minimum ad budget; tracking tools; time to first results (DATA NEEDED).
9. Does the client take part in choosing channels („заедно с Вас“ removed).
10. Ads-specific scope of the free diagnosis wording.
11. New page /reklama/: all copy is new AI text and needs approval.
12. H1 of the new page (from keyword-map) and its difference from the title.
13. Card/nav fields: label, summary, eyebrow, service, related.
14. „ти“→„Вие“ paraphrases of the owner's „Скрити проблеми“ copy (#specialist, #za-kogo).
15. „Пускаш отстъпки наслуки“ rendered as „пускате оферти към клиентите без ясен план“ (banned OFFER word).
