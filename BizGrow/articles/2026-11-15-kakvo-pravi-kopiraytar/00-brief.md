# 00-BRIEF — /saveti/kakvo-pravi-kopiraytar/

MARKET: bg — small-business owners in Bulgaria (locale bg at `/`)
LOCALE: bg   PAIR: none (no EN row in keyword-map.md)
CONTENT TYPE: new-page (article; keyword-map row status `planned`: owner's session, 2026-11-15)
PAGE: /saveti/kakvo-pravi-kopiraytar/
SLUG: kakvo-pravi-kopiraytar
MAIN TERM (BizGrow/keyword-map.md): копирайтър
SECONDARY: какво е копирайтър (40); копирайтър значение (50); добър копирайтър (20)
AHREFS: копирайтър | 600 | KD 0 | bg | 2026-11-15 (traffic potential 250; parent topic „копирайтър работа“; intents informational + commercial)
H1: (new) keyword-map proposal „Какво прави копирайтърът и кога Ви трябва“
SOURCE OF CURRENT PAGE: desislavamit/biz-grow @ feature/seo-improvements (local ~/Work/biz-grow-seo), commit a1ccf8f: no existing page (new); related copy in site/src/i18n/dictionaries/bg.ts and docs/content-sources/skriti-problemi.json
SERVICE (port file): NONE. This is an advice article: no `service` key.

## CURRENT PAGE + INVENTORY
- 00-current.md written: yes (new page; related existing copy quoted)
- 00-inventory.md written: yes — 1 booking CTA (max 1), 0 required email, 0 anchors, 2 required links, 6 canon facts, 1 canon number, 1 example-label rule, 0 existing FAQs

## SITE RULES RE-READ THIS RUN
- Site content model: `site/src/content/types.ts` `ContentPage` (path, locale, status, updated, primaryKeyword, meta{title,description}, label, summary, eyebrow?, h1, lead, sections[{id,title,paragraphs,bullets?,steps?,closing?}], faq, related, service?). Render order per section (`ContentPageView.tsx`): paragraphs → steps (ordered list) → bullets → closing paragraphs. So a section can hold: paragraphs, then at most ONE numbered list and/or ONE bullet list, then closing paragraphs. No text between the two lists. Inline syntax: `**bold**`, `[label](/path/ | #anchor | {{BOOKING_URL}} | mailto:{{EMAIL}})`, bare `{{EMAIL}}`.
- The template itself renders a header booking button („Запазете час“), a diagnosis button (link to /diagnostika/), the related cards (label + summary of each related page) and a CtaBand at the end. The body therefore needs at most ONE inline booking CTA (closing section).
- Otherwise same as reference/site-rules.md copy.

## OWNER INSTRUCTIONS FOR THIS PAGE (session brief 2026-11-15)
- ADVICE ARTICLE (informational intent). Answer: what a copywriter does; types of copy a small business needs (site texts, SEO articles, product descriptions, ads, social posts); how to brief a copywriter; what to check before hiring; when an SEO copywriter vs a general copywriter; when a content tool helps.
- Must NOT target „seo копирайтинг“ / „копирайтинг услуги“ (owned by /seo-statii/). Link to /seo-statii/ once or twice.
- No job/salary content beyond one neutral sentence if needed; NO salary numbers.
- ARTICLE RULES: question-led H2s (6–8); 900–1,400 words of body; 4–6 FAQ; one soft closing section pointing to the relevant service page and the free diagnosis (ONE booking CTA max on the page body); `eyebrow` = „Съвети“; `label` = short title for breadcrumbs/cards; `summary` ≤ 160 chars (shown on the /saveti/ hub card); NO `service` key; `related` = exactly 3 service pages.
- Canon change 2026-11-15: the document after the diagnosis is „оферта“ (never „доклад“); NO delivery periods anywhere; only the 30-minute call may carry a duration. Timing line if needed: „Срокът зависи от решението и го посочваме в офертата.“
- BizGrow's own offer here is the CONTENT TOOL (собствен инструмент за съдържание) plus the client's approval before publication. BizGrow does NOT state that it employs copywriters (team = Tier 3 unknown). The article must not imply a BizGrow copywriter team; any such need → [OWNER CONFIRM].
- Sources go in [[sources]]; a fact that needs a source but has none is left out.

## BUYER QUESTIONS (WebSearch bg 2026-11-15, Ahrefs SERP „копирайтър“, competitor headings; data only)
- Какво е копирайтър / какво означава думата? — yes (general definition, no source needed for a plain definition)
- С какво се занимава копирайтърът, какви текстове пише? — yes (site texts, product descriptions, ads, social posts, emails, SEO articles)
- Каква е разликата между копирайтър и журналист / редактор / рерайтър? — yes, general (copy aims at an action; editor polishes existing text)
- Какво е SEO копирайтър и кога ми трябва той? — yes (link /seo-statii/; do not target the term)
- Как да напиша задание (бриф) за копирайтър? — yes (goal, audience, product facts, tone, keywords, where it is published, length, deadline handled by the client)
- Как да преценя дали копирайтърът е добър? — yes (portfolio in a similar field, questions about the business, grammar, revisions discussed, sample text)
- Кога е по-удобен инструмент за съдържание? — yes (canon: content tool writes SEO articles for industry and city, SEO product descriptions for whole collections, social posts on a schedule; client approves)
- Колко струва копирайтър / заплата на копирайтър? — NO numbers (owner: no salary content beyond one neutral sentence; no prices). Skip or one neutral sentence.
- Мога ли да пиша текстовете сам? — yes, general advice
- Може ли AI да замени копирайтъра? — careful: claim rule 7, AI is a tool with human approval; no replacement claim

SERP observations (intent only, Ahrefs serp-копирайтър.json 2026-11-15): AI Overview present; jobs.bg (DR 74) #2, bg.wikipedia „Копирайтинг“ #3, webavtor.com „Какво е копирайтър и с какво се занимава“ (DR 8) #4, copywriting.bg „Какво е копирайтър и какво работят копирайтърите?“ (DR 4) #5, seomax.bg „Стани копирайтър“ #6, freelance.bg jobs #7, kakvidastanem.bg profession description. Explainer pages win with definition + tasks + types. No facts are taken from competitor pages.

## CANDIDATE NEW SOURCES (max 3 new external facts; authoritative only)
- Optional: Google Search Central „Creating helpful, reliable, people-first content“ — https://developers.google.com/search/docs/fundamentals/creating-helpful-content — supports: Google's systems aim to prioritise helpful, reliable information created for people (already used on /seo-statii/; reuse only if the synthesis needs it, with [VERIFY]).
- Otherwise none planned; the article is general advice and canon.

## SIBLING PAGES (avoid copied wording and term cannibalisation)
- / — ai автоматизация
- /ai-asistent/ — ai асистент
- /avtomatizacii/ — автоматизация на бизнес процеси
- /seo-statii/ — seo копирайтинг (secondary: копирайтинг услуги, копирайтинг, seo статии, seo текстове, писане на статии, описания на продукти) → DO NOT target; link once or twice
- /socialni-mrezhi/ — маркетинг в социалните мрежи
- /reklama/ — реклама в гугъл
- /reklama-vav-facebook/ — платена реклама във фейсбук
- /seo-optimizacia/ — seo оптимизация
- /izrabotka-na-sait/ — изработка на сайт
- /izrabotka-na-onlain-magazin/ — изработка на онлайн магазин
- /diagnostika/ — безплатна диагностика за бизнеса
- /saveti/klyuchovi-dumi/ — ключови думи (do not target; may link when mentioning keywords in a brief)
- /saveti/google-biznes-profil/ — бизнес профил в гугъл

## NOTES
- Port deliverable required in addition to content/kakvo-pravi-kopiraytar.md: content/kakvo-pravi-kopiraytar.port.json (ContentPage, status "published", updated "2026-11-15", eyebrow „Съвети“, no `service`). `related` = exactly 3 sibling service paths (suggested: /seo-statii/, /seo-optimizacia/, /socialni-mrezhi/).
- „копирайтинг“ alone (100) is a /seo-statii/ secondary; this article may use the word naturally but must not target it in title/H1/meta.
- Section ids: short latin kebab-case anchors.
- No earlier owner items for this page.
