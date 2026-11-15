# 00-BRIEF — /izrabotka-na-sait/

MARKET: bg — small-business owners in Bulgaria (locale bg at `/`)
LOCALE: bg   PAIR: none (no EN row in keyword-map.md)
CONTENT TYPE: new-page (keyword-map row status `planned`: owner 2026-11-15, "we offer that")
PAGE: /izrabotka-na-sait/
SLUG: izrabotka-na-sait
MAIN TERM (BizGrow/keyword-map.md): изработка на сайт
SECONDARY: изработка на уебсайт (300, KD 0); изработка на сайтове (250, KD 3); изработка на сайт цена (200, KD 1); изработка на уеб сайт (700, KD 48); поддръжка на сайт (300, KD 5); поддръжка на уебсайт (60)
AHREFS: изработка на сайт | 900 | KD 30 | bg | 2026-11-15
H1: keyword-map proposal „Изработка на сайт за малкия бизнес“ (new page, no current H1)
SOURCE OF CURRENT PAGE: none (new page). Site context read from desislavamit/biz-grow @ feature/seo-improvements, commit a1ccf8fe827ac1fd41ca48d9a22030b757861922 (site/src/i18n/dictionaries/bg.ts, site/src/content/types.ts, site/src/content/pages/bg/*, docs/content-sources/skriti-problemi.json).

## CURRENT PAGE + INVENTORY
- 00-current.md written: yes (new page: no current copy; records the site context)
- 00-inventory.md written: yes — 0 current-page items (new page); 10 REQUIRED items R1–R10.

## SITE RULES RE-READ THIS RUN
- dictionaries / config.ts / types.ts: same as reference/site-rules.md copy. Notes:
  - Content pages render from `ContentPage` (`site/src/content/types.ts`). The template already renders a booking button („Запазете час“) and a „Безплатна диагностика“ button under the lead, plus a CTA band and related links at the end.
  - Inline syntax in `ContentPage` strings: `**bold**`, `[label](/path/)`, `[label](#anchor)`, `[label]({{BOOKING_URL}})`, bare `{{EMAIL}}`. PageSection supports paragraphs, bullets?, steps? (numbered), closing? (paragraphs after the lists).

## OWNER INSTRUCTIONS FOR THIS PAGE
- Service page: website building and website maintenance for small businesses (canon service 6). Nothing more specific is canon: no platforms (WordPress etc.), page counts, design process, hosting, domains, delivery times, prices. Anything more → OWNER CONFIRM.
- Canon change 2026-11-15: the document after the diagnosis is „оферта“ (never „доклад“); NO delivery periods anywhere (no „до 48 часа“, „до 2 седмици“, „за дни“); only the 30-minute call may carry a duration. Timing line if needed: „Срокът зависи от решението и го посочваме в офертата.“
- Competitors (DR 37–63) show prices; we explain how the price is formed, never a number or range, although „изработка на сайт цена“ is a secondary term.
- Cover: what a small-business site needs to do (contact, booking via /avtomatizacii/, SEO basics via /seo-optimizacia/ and /seo-statii/), how the work goes (canon process), maintenance (поддръжка на сайт), how price is formed.
- 7–8 H2 + 6–8 FAQ. `service` (schema name): „Изработка на сайт“.
- Must NOT target „изработка на онлайн магазин“ (sibling /izrabotka-na-onlain-magazin/): link to it for shops; do not use it as a heading or repeated phrase.

## BUYER QUESTIONS (PAA, competitor FAQ headings, suggestions)
Sources: Ahrefs SERPs „изработка на сайт“ (webdizain-bg.com, savovdesign.com „…на цена“, webpartner.bg „Изработка на сайт, поддръжка на сайт…“, slvdesign.com, eweb.bg, agma.bg „Колко струва изработката на сайт?“, techstation.bg „…цени“, denvelkoff.studio „Колко струва … Реални…“; local pack present), „изработка на уебсайт“ (AI overview; touchpoint.bg, alphabest.bg, valival.bg), „поддръжка на сайт“ (AI overview; savana-soft.com, intersoft.bg „Цени за поддръжка“, ideamax.eu „[Таблица с Цени]“, easyweb.bg, eweb.bg, websitespartners.com „Абонаментна поддръжка“). Web search (bg) 2026-11-15: „изработка на сайт въпроси колко струва какво включва поддръжка на сайт“, „"изработка на сайт" често задавани въпроси малък бизнес“. Intent only, no facts taken from competitors.
- Колко струва изработката на сайт? / От какво зависи цената? — yes (price formation, no numbers)
- Колко време отнема изработката? — yes, canon timing line only („Срокът зависи от решението и го посочваме в офертата.“)
- Какво трябва да има сайтът на малък бизнес (контакти, услуги, записване, мобилна версия)? — yes (general + sourced mobile fact)
- Трябва ли сайтът да работи добре на телефон? — yes (Google mobile-first, sourced)
- Включено ли е SEO в изработката? — partly: basics explained; full SEO is a separate service → /seo-optimizacia/; content → /seo-statii/; what exactly is included in a BizGrow build → OWNER CONFIRM
- Какво включва поддръжката на сайт? / Нужна ли е поддръжка след пускането? — partly: canon = monthly support with short report; specific tasks → OWNER CONFIRM / general wording
- Има ли абонамент / дългосрочен договор за поддръжката? — yes (no long-term contracts)
- Можете ли да направите и онлайн магазин? — yes, link /izrabotka-na-onlain-magazin/
- Мога ли да си направя сайт сам с конструктор? — partly (neutral; the diagnosis helps decide; no claims)
- На кого остават домейнът, хостингът и достъпите? — unknown → OWNER CONFIRM (do not answer with a policy)
- Можете ли да обновите съществуващ сайт (редизайн)? — unknown → OWNER CONFIRM; can say the diagnosis looks at the current site
- Ще ми донесе ли сайтът клиенти? — yes: no guarantee

## CANDIDATE NEW SOURCES (max 3 new external facts; authoritative only)
1. Google Search Central, „Mobile site and mobile-first indexing best practices“ — https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing — HTTP 200 (2026-11-15) — quotes: "Google uses the mobile version of a site's content, crawled with the smartphone agent, for indexing and ranking." / "Google recommends Responsive Web Design because it's the easiest design pattern to implement and maintain."
2. Google Search Central, „Understanding page experience in Google Search results“ — https://developers.google.com/search/docs/appearance/page-experience — HTTP 200 (2026-11-15) — quote: "Google's core ranking systems look to reward content that provides a good page experience." Self-assessment: "Do your pages have good Core Web Vitals?", "Are your pages served in a secure fashion?", "Does your content display well on mobile devices?"
3. Google Search Central, „SEO Starter Guide“ — https://developers.google.com/search/docs/fundamentals/seo-starter-guide — HTTP 200 (2026-11-15) — general reference for titles/descriptions; use only if a specific quoted passage is fetched at Step 6.

## SIBLING PAGES (to avoid copied wording and term cannibalisation)
- / — ai автоматизация
- /ai-asistent/ — ai асистент (chatbot on the site)
- /avtomatizacii/ — автоматизация на бизнес процеси (owns онлайн записване, онлайн резервации) — MUST link for booking
- /seo-statii/ — seo копирайтинг (seo статии, seo текстове) — MUST link for content
- /seo-optimizacia/ — seo оптимизация (техническо seo, seo оптимизация на сайт) — MUST link for SEO
- /socialni-mrezhi/ — маркетинг в социалните мрежи
- /reklama/ — реклама в гугъл
- /reklama-vav-facebook/ — платена реклама във фейсбук
- /diagnostika/ — безплатна диагностика за бизнеса
- /izrabotka-na-onlain-magazin/ — изработка на онлайн магазин (also: създаване на онлайн магазин, платформа за онлайн магазин) — MUST link for shops, never target

## NOTES
- First run for this page; no earlier owner items.
- Deliverables: `content/izrabotka-na-sait.md` (template) AND `content/izrabotka-na-sait.port.json` (`ContentPage`: path, locale "bg", status "published", updated "2026-11-15", primaryKeyword, meta{title,description}, label, summary, eyebrow, h1, lead, sections[{id,title,paragraphs,bullets?,steps?,closing?}], faq[{question,answer}], related[3 sibling paths], service "Изработка на сайт"). Strings identical to the content file; no em-dashes; meta.title ≤ 60 incl. " | BizGrow"; meta.description 120–160 chars. Booking/email in strings: `[label]({{BOOKING_URL}})`, bare `{{EMAIL}}`. `related` suggestion: /izrabotka-na-onlain-magazin/, /seo-optimizacia/, /avtomatizacii/.
- Niche: SERP = studio home/service pages with price tables + "колко струва" articles; AI overviews on „изработка на уебсайт“ and „поддръжка на сайт“. KD 30 main term; „изработка на уебсайт“ KD 0, „изработка на сайт цена“ KD 1, „поддръжка на сайт“ KD 5 are the realistic wins. A price-formation section and a maintenance section are required to match intent.
- Step 7: no GEMINI_API_KEY locally → skipped. Step 8: none.
