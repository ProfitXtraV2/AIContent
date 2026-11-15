# 00-BRIEF — /saveti/klyuchovi-dumi/

MARKET: bg — small-business owners in Bulgaria (locale bg at `/`)
LOCALE: bg   PAIR: none (no EN row in keyword-map.md)
CONTENT TYPE: new-page (article) — keyword-map row status `planned`: owner's session, 2026-11-15
PAGE: /saveti/klyuchovi-dumi/
SLUG: klyuchovi-dumi
MAIN TERM (BizGrow/keyword-map.md): ключови думи
SECONDARY: ключови думи в текст (60); определяне на ключови думи (50); как се откриват ключови думи (30); пример за ключови думи (30); какво са ключови думи (20)
AHREFS: ключови думи | 80 | KD 0 | bg | 2026-11-15 (traffic potential 50; all variants informational intent) — source biz-grow docs/seo-audit/ahrefs-2026-11-15/mt-ключови_думи.json
H1: (new) keyword-map proposal „Ключови думи: как да ги изберете за сайта си“
SOURCE OF CURRENT PAGE: desislavamit/biz-grow @ feature/seo-improvements : no existing page (new article); related copy in 00-current.md, commit a1ccf8f
SERVICE: none (article: NO `service` key)

## CURRENT PAGE + INVENTORY
- 00-current.md written: yes (new page; related copy quoted)
- 00-inventory.md written: yes — 3 required links, ≤1 booking CTA, 0 existing FAQs, canon facts for the closing section

## SITE RULES RE-READ THIS RUN
- Port target `ContentPage` (site/src/content/types.ts @ a1ccf8f): path, locale, status, updated, primaryKeyword, meta{title,description}, label, summary, eyebrow, h1, lead, sections[{id,title,paragraphs[],bullets?[],steps?[],closing?[]}], faq[{question,answer}], related[], service?.
- RENDER ORDER per section (ContentPageView.tsx): paragraphs → steps (numbered) → bullets → closing paragraphs. So a section can have at most one numbered list and one bulleted list, and text after the lists goes in `closing`. Outline and draft must fit this shape (lesson from the /ai-asistent/ run, which needed a loop for this).
- Inline syntax only `**bold**` and `[label](/path/)` / `[label](#anchor)` / `[label]({{BOOKING_URL}})` / bare `{{EMAIL}}`. No tables, no H3, no images, no quotes blocks.
- The template already renders a booking button („Запазете час“) and a diagnosis button under the H1, plus FAQ and a related-pages block (cards with each page's label + summary). The body needs at most one booking CTA.
- Otherwise same as reference/site-rules.md.

## OWNER INSTRUCTIONS FOR THIS PAGE (run brief 2026-11-15)
- Advice ARTICLE (informational). Explain: what keywords are; how a small business finds them (customer questions, Google autocomplete and related searches, Search Console — general, verifiable facts only); one main term per page; using them naturally in a text (title, H1, first paragraph, headings); common mistakes (keyword stuffing — may cite Google Search Central spam policies).
- Link /seo-statii/ and /seo-optimizacia/; do NOT target their main terms („seo копирайтинг“, „seo оптимизация“) nor use them as anchors.
- ARTICLE RULES: question-led H2s (6–8), 900–1,400 words of body, 4–6 FAQ, one soft closing section pointing to the relevant service page and the free diagnosis (one booking CTA max), eyebrow „Съвети“, label short (breadcrumbs/cards), summary ≤160 chars, NO service key, related = 3 service pages.
- Canon changes: the document after the diagnosis is „оферта“ (never „доклад“); NO delivery periods anywhere; only the 30-minute call may carry a duration. Timing line if needed: „Срокът зависи от решението и го посочваме в офертата.“
- Facts that need a source but have none are left out. No tool vendors (no Ahrefs, Semrush, Ranktracker etc.) named as recommendations; Google's own free tools (Search Console, Google search autocomplete, Keyword Planner in Google Ads) may be named as general facts.

## BUYER QUESTIONS (WebSearch bg 2026-11-15 + Ahrefs matching-terms; data only)
- Какво са ключови думи? — yes (general definition: the words/phrases people type in Google)
- Как се откриват / определят ключови думи за малък бизнес? — yes: customer questions, autocomplete, related searches at the bottom of results, Search Console queries
- Какво е „дълга“ ключова фраза и кога е по-добра? — yes, general explanation, no numbers
- Какво е намерение на търсенето (информация vs покупка)? — yes, general
- Къде да сложа ключовите думи в текста (title, H1, първи абзац, подзаглавия, описание)? — yes
- Колко пъти да повторя ключовата дума? — yes: no magic number; natural use; stuffing is against Google's spam policies (source)
- Има ли значение meta keywords тагът? — yes if sourced (Google SEO Starter Guide: Google Search doesn't use it)
- Пример за ключови думи? — yes, as a clearly labelled hypothetical example (e.g. a dental practice or bakery in a city), no volumes invented
- Трябват ли платени инструменти? — answer without naming vendors: free sources first; Keyword Planner requires a Google Ads account (only if sourced; else omit)
- Колко търсения има дадена дума? — do not state any volume figure

Competitor/SERP observations (intent only): Bulgarian SERP is dominated by ranktracker.com/bg translated blog posts and Google Ads help; content is long, generic, tool-promoting. Opportunity: a short, practical, small-business-focused explanation in plain Bulgarian.

## CANDIDATE NEW SOURCES (max 3 new external facts; authoritative only; all fetched 2026-11-15, HTTP 200)
1. Google Search Central — Spam policies, "Keyword stuffing" — https://developers.google.com/search/docs/essentials/spam-policies — keyword stuffing = filling a page with keywords or numbers to manipulate rankings; examples incl. blocks of text listing cities/regions a page tries to rank for, and repeating the same words or phrases so often that it sounds unnatural.
2. Google Search Console Help — Performance report — https://support.google.com/webmasters/answer/7576553 — shows clicks, impressions, CTR, average position; data can be grouped by queries (the search terms people entered); default view = past 3 months.
3. Google Search Help — How autocomplete works — https://support.google.com/websearch/answer/7368877 — "autocomplete predictions reflect real searches that have been done on Google".
(Alternate) Google Search Central — SEO Starter Guide — https://developers.google.com/search/docs/fundamentals/seo-starter-guide — "Think about the words that a user might search for to find a piece of your content"; "Google Search doesn't use the keywords meta tag"; "Excessively repeating the same words over and over (even in variations) is tiring for users"; good title is "unique to the page, clear and concise, and accurately describes the contents of the page". Synthesis picks max 3 in total.

## SIBLING PAGES (avoid copied wording and term cannibalisation)
- / — ai автоматизация
- /ai-asistent/ — ai асистент
- /avtomatizacii/ — автоматизация на бизнес процеси
- /seo-statii/ — seo копирайтинг (also копирайтинг, seo статии, seo текстове, писане на статии) → LINK, do not target
- /socialni-mrezhi/ — маркетинг в социалните мрежи
- /reklama/ — реклама в гугъл
- /seo-optimizacia/ — seo оптимизация (also seo услуги, техническо seo, seo одит-related) → LINK, do not target
- /diagnostika/ — безплатна диагностика за бизнеса → closing link
- /saveti/kakvo-pravi-kopiraytar/ — копирайтър
- /saveti/google-biznes-profil/ — бизнес профил в гугъл
- /izrabotka-na-sait/ — изработка на сайт

## NOTES
- Port deliverable required in addition to content/klyuchovi-dumi.md: content/klyuchovi-dumi.port.json (ContentPage, no `service`). related = exactly 3 service paths from conversion-links.md: /seo-statii/, /seo-optimizacia/, /diagnostika/ (suggested).
- No earlier owner items for this page.
