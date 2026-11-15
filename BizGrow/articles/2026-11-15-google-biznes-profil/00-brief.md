# 00-brief — /saveti/google-biznes-profil/

MARKET: bg — small-business owners in Bulgaria (locale bg at `/`)
LOCALE: bg   PAIR: none (no EN pair in keyword-map.md)
CONTENT TYPE: new-page, ADVICE ARTICLE (keyword-map row status `planned`; owner's session 2026-11-15)
PAGE: /saveti/google-biznes-profil/
SLUG: google-biznes-profil
MAIN TERM (BizGrow/keyword-map.md): бизнес профил в гугъл
SECONDARY: гугъл бизнес профил (150); създаване на бизнес профил в гугъл (60); гугъл бизнес (60); гугъл май бизнес (20); потвърждаване на бизнес профил в гугъл (20)
AHREFS: бизнес профил в гугъл | 100 | KD 0 | bg | 2026-11-15
H1: keyword-map proposal „Как да създадете и поддържате Google бизнес профил“ (new page). Main-term placement note: the main term is the colloquial „бизнес профил в гугъл“; place it verbatim once in title-or-meta / first 100 words / one H2 as the SEO stage decides; elsewhere write „Google бизнес профил“ / „бизнес профил в Google“.
SOURCE OF CURRENT PAGE: desislavamit/biz-grow @ feature/seo-improvements : no page yet; related copy in docs/content-sources/skriti-problemi.json + site/src/content/pages/bg/socialni-mrezhi.ts, commit a1ccf8f

## CURRENT PAGE + INVENTORY
- 00-current.md written: yes (new page; reference copy only)
- 00-inventory.md written: yes — 4 CTA/link items (+ optional email), 1 token required, 0 anchors, 4 canon facts, 1 canon number (30 минути), 0 example labels, 0 FAQs

## SITE RULES RE-READ THIS RUN
- site/src/content/types.ts @ a1ccf8f: ContentPage {path, locale, status, updated, primaryKeyword, meta{title,description}, label, summary, eyebrow?, h1, lead, sections[{id,title,paragraphs[],bullets?[],steps?[],closing?[]}], faq[], related[], service?, tool?}. Difference vs reference/site-rules.md §5: sections now also have `steps` (numbered) and `closing` (paragraphs after lists). Logged.
- Canon change 2026-11-15 (run brief + author.md): the post-diagnosis document is „оферта“, never „доклад“; NO delivery periods anywhere; only the 30-minute call carries a duration.

## OWNER INSTRUCTIONS FOR THIS PAGE (run brief, owner's session 2026-11-15)
- ADVICE ARTICLE (informational how-to), not a service page. Explain step by step how to create, verify and keep up a Google Business Profile, using ONLY facts from Google's official help (support.google.com/business: 2911778 add/claim, 7107242 verify, 7039811 get started). Max 3 sourced facts; keep the steps general where no source is used; NEVER invent UI labels (button names only if quoted in the source passages below).
- Then what to keep up monthly (posts, photos, hours, replies to ratings and comments). Canon: BizGrow keeps the profile alive and prepares replies for approval. Link /socialni-mrezhi/ and /ai-asistent/.
- ARTICLE RULES: question-led H2s (6–8); 900–1,400 words of body; 4–6 FAQ; ONE soft closing section pointing to the relevant service page and the free diagnosis (one booking CTA max on the whole page); eyebrow „Съвети“; `label` short title for breadcrumbs/cards; `summary` ≤160 chars; NO `service` key; `related` = 3 service pages (from conversion-links.md; suggested /socialni-mrezhi/, /ai-asistent/, /diagnostika/ or /seo-optimizacia/).
- Facts that need a source but have none are left out.
- Extra deliverable: content/google-biznes-profil.port.json (ContentPage object, strings identical to the content file).

## BUYER QUESTIONS (Ahrefs SERP JSON serp-бизнес_профил_в_гугъл.json; WebSearch bg query; competitor titles: seomax.bg "От създаването до…", ss-studio.bg "15 стъпки")
- Как да създам бизнес профил в Google? — yes (2911778 steps, general)
- Как да заявя профил, който вече съществува в Google Карти? — yes (2911778)
- Как се потвърждава бизнес профилът и защо е нужно? — yes (7107242: verification gives ownership; options depend on business type)
- Колко време отнема потвърждаването? — yes, sourced (7107242: reviews up to 5 working days, rarely longer) — candidate sourced fact
- Струва ли нещо профилът? — yes, sourced (2911778/7039811: без парично заплащане) — candidate; do NOT use the word „безплатен“ for it
- Какво да попълня в профила (работно време, сайт, телефон, местоположение, снимки)? — yes (7039811)
- Как да отговарям на оценки и коментари? — general practice only, no external numbers; canon: BizGrow prepares replies for approval
- Колко често да обновявам профила / публикации? — general; canon monthly upkeep by BizGrow
- Дали профилът ще ме изкара първи в Google Карти? — no promise allowed (no guarantees, no ranking claims)
- Мога ли да имам профил без адрес / с зона на обслужване? — NOT in fetched passages → leave out or keep general ("следвайте указанията на Google за адреса")

## CANDIDATE NEW SOURCES (max 3 new external facts; authoritative only; fetched 2026-11-15, HTTP 200 via WebFetch)
1. Google Business Profile Help, „Добавяне или заявяване на бизнес профила ви“ — https://support.google.com/business/answer/2911778?hl=bg
   Verbatim: „Когато добавите и потвърдите бизнес профила си, клиентите могат да намират бизнеса ви в Търсене и Карти.“ / „Можете да добавите или заявите бизнеса си без парично заплащане.“ / „Само бизнесите, които отговарят на условията за бизнес профил, могат да добавят или заявяват местоположението си.“ / Steps: „Отворете business.google.com/add.“ „Кликнете върху Добавете бизнеса си в Google.“ „За да добавите подробности за бизнеса си, изпълнете инструкциите на екрана.“ „Изберете опция за потвърждаване и изпълнете стъпките на екрана.“ / Claim: „От компютъра си отворете Google Карти.“ „Потърсете името на бизнеса и града си.“ „Изберете „Заявяване на този бизнес““ → „Управление сега“. / „Ако бизнес профил в Google е потвърден и сте упълномощени да го управлявате, можете да подадете заявка за собственост до настоящия му собственик.“
2. Google Business Profile Help, „Потвърдете бизнеса си в Google“ — https://support.google.com/business/answer/7107242?hl=bg
   Verbatim: „Когато потвърдите бизнеса си в Google, придобивате собствеността върху бизнес профила си“ / „Наличните за вас опции за потвърждаване зависят от типа на бизнеса ви“ / options: „Телефон или SMS“, „Имейл“, „Видеообаждане на живо“; „Потвърждаването чрез пощенска картичка не е налице за всички бизнеси.“ / „прегледите за потвърждаване отнемат до 5 работни дни“ / „В редки случаи прегледите може да отнемат повече време.“
3. Google Business Profile Help, „Първи стъпки с Google Business Profile“ — https://support.google.com/business/answer/7039811?hl=bg
   Verbatim: „С бизнес профил в Google можете да управлявате как бизнесът ви се показва в Карти и Търсене без парично заплащане.“ / „Предоставете работното време, уебсайта, телефонния номер и местоположението си, за да са видими за клиентите в Google.“ / „Публикувайте снимки и видеоклипове на бизнеса си и предлаганите от него продукти и услуги.“ / „Събирайте и отговаряйте на отзиви от клиентите.“ (page does not mention posts)
Rule: max 3 NEW sourced FACTS on the page (count facts, not URLs). Suggested three: (a) verification gives ownership + options depend on business type; (b) verification review up to 5 working days; (c) profile without payment / shows in Search and Maps. Steps that only paraphrase the on-screen flow generally ("отворете Google Карти, потърсете бизнеса си") may cite the same URL; the gate decides the count.

## SIBLING PAGES (to avoid copied wording and term cannibalisation)
- / — ai автоматизация
- /ai-asistent/ — ai асистент
- /avtomatizacii/ — автоматизация на бизнес процеси
- /seo-statii/ — seo копирайтинг
- /socialni-mrezhi/ — маркетинг в социалните мрежи (this article links to it for the monthly upkeep; never target its term)
- /reklama/ — реклама в гугъл (do NOT use „реклама в гугъл“ / Google Ads terms here)
- /seo-optimizacia/ — seo оптимизация (do not target; „локално seo“ is a parked phase-2 term, do not target it either)
- /diagnostika/ — безплатна диагностика за бизнеса
- /saveti/kakvo-pravi-kopiraytar/ — копирайтър; /saveti/klyuchovi-dumi/ — ключови думи

## NOTES
- House wording: „оценки и коментари в Google“, not „отзиви“ (site-rules §3; /diagnostika/ owner item 21 still open — raise again as an owner item if relevant).
- „безплатн*“ only about the diagnosis; for the profile use the sourced „без парично заплащане“ wording or leave out.
- No ranking/visibility promises (no "ще Ви изкара в топ 3 на Картите").
- Checker detail „3 снимки от 2022“ is illustrative; do not reuse as a fact.
