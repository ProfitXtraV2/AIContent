# 06-verification: /reklama/ (bg, new-page) · fix loop 1

Run: 2026-11-15, Step 6, **fix loop 1**, fresh context. Reason for the loop: the first Step 6 run (kept as `06-verification.r1.md`, `content/reklama.r1.md`, `content/reklama.port.r1.json`) found that F1 („Google таксува само при клик“) was only partly supported, because the source limits it to CPC bidding. Steps 4, 5 and 5b were re-run; the F1 sentence now carries the CPC condition in all four places. Everything else in 05b is unchanged.

Inputs: 05b-final-draft.md (loop 1), 05-gate-report.md (OWNER ITEMS TO RAISE 1-10), 00-current.md, 00-inventory.md, BizGrow/keyword-map.md, BizGrow/conversion-links.md, pipeline/reference/verification-policy.md, pipeline/reference/site-rules.md, pipeline/templates/content-file-template.md, biz-grow-seo `site/src/content/types.ts` (read-only).

Deliverables (overwritten):
- `content/reklama.md` (Markdown + TOML front matter, status "draft", last_updated 2026-11-15)
- `content/reklama.port.json` (ContentPage object, status "published", updated 2026-11-15, generated mechanically from the content file so every string is identical)

Difference against r1 deliverables: exactly the four F1 sentences (#kak-raboti, #cena, FAQ 1, FAQ 3) and the text of owner item 1. A scripted comparison confirms the content file body, FAQ, title, meta, label, summary and eyebrow equal 05b-final-draft.md with the inline markers stripped (40/40 body lines, 8/8 FAQ).

## RESOLVED-TO-OWNER-ITEMS

HTTP check (re-run in loop 1): `curl -sI -L -A 'Mozilla/5.0'` returns **404 for HEAD** on both support.google.com pages (Google Help does not answer HEAD requests); a full GET (`curl -sL -A 'Mozilla/5.0' -w '%{http_code}'`) returns **200** for both, with the expected Bulgarian page titles („Използване на Google Ads за онлайн маркетинг - Помощ за Google Ads“, „Показване на рекламите Ви на първа страница - Помощ за Google Ads“). Every quote below was found verbatim in the GET body (HTML stripped, whitespace normalised).

| # | claim on the page | where | URL | GET | quote (bg) | verdict |
|---|---|---|---|---|---|---|
| F1 | „При оферирането за цена на кликване (CPC) Google таксува рекламодателя само когато някой кликне върху рекламата.“ / #cena „…а при оферирането за цена на кликване (CPC) Google таксува само при клик върху рекламата.“ / FAQ 1 (same clause) / FAQ 3 „При оферирането за цена на кликване (CPC) в Google Ads рекламодателят плаща само когато някой кликне върху рекламата.“ | #kak-raboti, #cena, FAQ 1, FAQ 3 | https://support.google.com/google-ads/answer/6227565?hl=bg | 200 | „С оферирането за цена на кликване (CPC) Ви таксуваме само когато някой е достатъчно заинтересуван да кликне върху рекламата Ви и да посети уебсайта Ви.“ | **Supported.** Each sentence now carries the same CPC condition as the source, so the r1 caveat is resolved in the text. The source also mentions campaigns that pay for conversions („При кампании, за които плащате за реализации…“); the page makes no claim about them. Owner still confirms the source (owner item 1). |
| F2 | „Вие решавате каква средна сума да се изразходва за рекламата всеки ден, тоест какъв да бъде дневният бюджет.“ / #cena / FAQ 1 „Вие решавате средната дневна сума“ | #kak-raboti, #cena, FAQ 1 | https://support.google.com/google-ads/answer/6227565?hl=bg | 200 | „Вие решавате средната сума, която искате да изразходвате всеки ден.“ | Supported verbatim. Kept. |
| F3 | „Според Google то зависи от конкуренцията с други рекламодатели и от рекламния ранг…“; „По-високата сума сама по себе си не осигурява определено място.“; FAQ 2 „По-високата сума сама по себе си не осигурява най-горното място.“ | #kak-raboti, FAQ 2 | https://support.google.com/google-ads/answer/2472742?hl=bg | 200 | „Покриването или надвишаването на тази прогнозна стойност обаче не Ви гарантира рекламно разположение. Крайното разположение продължава да зависи от конкуренцията на други рекламодатели, рекламния Ви ранг, настройките Ви за бюджета и профила, както и поведението на потребителите.“ | Supported (the page names two of the four factors after „не зависи само от сумата“; FAQ 2's „най-горното място“ matches the source's first-position bid estimate). Kept. |

All three facts: inline `[VERIFY]` markers removed, both URLs in `[[sources]]` with empty `checked_by`/`checked_on`, one owner item each (items 1-3). Sourced facts on the page: 3 (policy maximum).

`[OWNER CONFIRM]` inline markers (2) removed: #cena pricing model (owner item 4) and ad budget vs fee (owner item 5); neither left a claim in the text. `[DATA NEEDED]` (2, not inline) → owner items 7 and 8. No `[LINK NEEDED]` markers.

## REMAINING FOR HUMAN

1. **F1 (r1 item) resolved in the text.** All four F1 sentences now carry „при оферирането за цена на кликване (CPC)“, matching the source. Nothing left for the reviewer beyond the owner's normal source check (owner item 1).
2. HEAD vs GET: both Google Help URLs answer HEAD with 404 and GET with 200. If a later automated link check uses HEAD only, it will report these sources as broken; check with GET.
3. Meta (Facebook/Instagram) facts: none on the page (the Meta help page was JS-rendered at Step 0 and not used); no claim about Meta pricing or placement was added.
4. No sentence was removed in this step.

## PORTING NOTES

- **New page, no dictionary keys change.** The page is a `ContentPage` object (`site/src/content/types.ts`), not a dictionary entry: all `[[sections]]` have `dictionary_key = ""`. Suggested file: `site/src/content/pages/bg/reklama.ts` exporting the object in `content/reklama.port.json`. No new key in `Dictionary` (`site/src/i18n/types.ts`) is needed. Nav/cards that list services may need the label/summary (owner item 13).
- **If the r1 port was already copied into the site:** only four strings change (#kak-raboti paragraph 1, #cena paragraph 2, FAQ 1 answer, FAQ 3 answer); replace them with the strings in the new `reklama.port.json`.
- **status:** the content file is `status = "draft"` (pipeline rule: never approved); the port JSON is `"status": "published"` as requested by the launching session so the page builds. Publishing still waits for the owner items, in particular item 11 (whole new page).
- **Hero mapping:** the hero block (`{#hero}`) → `h1` + `lead`. The hero has a single paragraph and no CTA line, so `lead` is that paragraph verbatim. `eyebrow`, `label`, `summary`, `service`, `related` come from the extra front-matter keys.
- **Sections:** 8 sections, ids and titles = body blocks. Paragraph text, `bullets` (#specialist, #za-kogo; leading „- “ removed) and `steps` (#proces; leading „1. “-„4. “ removed, numbering left to the ordered-list renderer) are copied verbatim.
- **CTAs and tokens:** the site renders `[label]({{BOOKING_URL}})`, `[label](mailto:{{EMAIL}})` and a bare `{{EMAIL}}` in any string (documented in `types.ts`), so the booking CTAs are kept exactly as in the content file: #proces `[Запазете безплатна диагностика]({{BOOKING_URL}})` and #diagnostika `[Запазете час]({{BOOKING_URL}})`, each as its own string in `paragraphs`. The #diagnostika bare `{{EMAIL}}` is kept inside its sentence.
- **Order in #proces:** content order is paragraph, CTA, numbered steps. In the port the CTA is the second `paragraphs` entry and the steps render after paragraphs, so the visual order is identical.
- **FAQ:** 8 entries, `q`/`a` → `question`/`answer` verbatim; FAQ 5 keeps the /socialni-mrezhi/ link.
- **Internal links used:** /seo-optimizacia/ (#kak-raboti), /socialni-mrezhi/ (#facebook-instagram, FAQ 5), /diagnostika/ (#proces step 1). The pages /seo-optimizacia/ and /socialni-mrezhi/ must exist (or links be hidden) when this page goes live; /reklama/ itself must be added to any sitemap/related lists of its siblings.
- **Sources:** not rendered by ContentPage; the human decides whether to show them.
- After porting: `npm run lint`, `npx tsc --noEmit`, `npm run build` in the site repo (pipeline does not run these).

## SELF-CHECK

Script: scratchpad `reklama_selfcheck.py` (Python 3, tomllib), the r1 checks plus three loop-1 checks (every charge-on-click sentence carries the CPC condition; CPC condition appears exactly 4 times; content file equals 05b minus markers via `reklama_cmp05b.py`). Content file built by `reklama_build_md_l1.py`, port by `reklama_build_port.py`. Result: **70/70 PASS, 0 FAIL.**

| check | result | detail |
|---|---|---|
| TOML parses (tomllib) | PASS |  |
| port JSON parses | PASS |  |
| primary_keyword == keyword-map term | PASS | реклама в гугъл |
| title <= 60 incl. \| BizGrow | PASS | 59 chars |
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
| F1: every charge-on-click sentence carries the CPC condition | PASS | 4 sentences |
| F1: CPC condition count == 4 (#kak-raboti, #cena, FAQ 1, FAQ 3) | PASS |  |
| content body/FAQ/meta == 05b-final-draft minus markers | PASS |  |

Example scenarios: none on the page (I19 n/a), so no example-label check applies. FAQ answers are 1-3 sentences.

## COUNTS

- Body word count (H1 + lead + 8 section headings and bodies, excluding FAQ; link URLs and tokens not counted): **764** (r1: 749; +15 from the CPC condition in #kak-raboti and #cena)
- FAQ word count: **288** (r1: 274)
- Sections: hero + 8 H2 | FAQ: 8 | bullets: 10 (4 + 6) | steps: 4
- Booking CTAs: 2 (`{{BOOKING_URL}}`) | `{{EMAIL}}`: 1 | internal links: 4 (3 distinct paths)
- title: 59 characters | meta_description: 148 characters
- new facts: 3 (F1-F3, Tier B, sources 2)
- owner items carried from gate report: 10 (items 1-10; item 1 text updated for the CPC wording)
- owner items added: 5 (items 11-15, carried from r1)
- owner items total: 15 | sentences removed: 0

## OWNER ITEMS (as in the content file)

1. F1: with CPC bidding Google Ads charges only on click; now worded with the CPC condition in all four places (#kak-raboti, #cena, FAQ 1, FAQ 3), so the r1 limitation note is resolved in the text; owner still confirms the source (6227565, quote).
2. F2 advertiser decides the average daily amount, source 6227565, quote.
3. F3 placement depends on competition and ad rank; higher amount does not assure placement, source 2472742, quotes.
4. Pricing model of the specialist's ongoing work vs canon one-off price per solution.
5. Is the ad budget paid to Google/Meta separate from BizGrow's fee (no claim in text).
6. Title „Гугъл“ vs H1 „Google“; label, summary, eyebrow.
7. Whose ad account is used (DATA NEEDED).
8. Minimum ad budget; tracking tools; time to first results (DATA NEEDED).
9. Does the client take part in choosing channels („заедно с Вас“ removed).
10. Ads-specific scope of the free diagnosis wording.
11. New page /reklama/: all copy is new AI text and needs approval.
12. H1 of the new page (from keyword-map) and its difference from the title.
13. Card/nav fields: label, summary, eyebrow, service, related.
14. „ти“→„Вие“ paraphrases of the owner's „Скрити проблеми“ copy (#specialist, #za-kogo).
15. „Пускаш отстъпки наслуки“ rendered as „пускате оферти към клиентите без ясен план“ (banned OFFER word).
