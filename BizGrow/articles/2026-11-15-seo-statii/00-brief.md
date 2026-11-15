# 00-brief — /seo-statii/

MARKET: bg — small-business owners in Bulgaria (locale bg at `/`)
LOCALE: bg   PAIR: none (no EN pair in keyword-map.md)
CONTENT TYPE: new-page (keyword-map row status `planned`; owner's session 2026-11-15)
PAGE: /seo-statii/
SLUG: seo-statii
MAIN TERM (BizGrow/keyword-map.md): seo копирайтинг
SECONDARY: копирайтинг услуги (150, KD 0); копирайтинг (100, KD 0); seo статии (90, KD 0); копирайтинг услуги цени (60); seo текстове (20); писане на статии (20, KD 0); описания на продукти
AHREFS: seo копирайтинг | 100 | KD 0 | bg | 2026-11-15 (cluster ~550/month combined; topic-backlog row 3, commercial)
H1: keyword-map proposal „SEO копирайтинг и SEO статии“ (new page, no current H1)
SOURCE OF CURRENT PAGE: desislavamit/biz-grow @ feature/seo-improvements : no page yet; related copy in site/src/i18n/dictionaries/bg.ts + docs/content-sources/skriti-problemi.json, commit 528ad25
SERVICE (schema name, run brief): „SEO копирайтинг и SEO статии“

## CURRENT PAGE + INVENTORY
- 00-current.md written: yes (new page; reference copy only)
- 00-inventory.md written: yes — 3 CTA/link items (booking, email, /diagnostika/), 2 tokens, 0 anchors, 13 canon facts, 3 canon numbers, 0 example labels, 0 FAQs

## SITE RULES RE-READ THIS RUN
- Site repo @ 528ad25: content pages are typed `ContentPage` objects (site/src/content/types.ts): path, locale, status, updated, primaryKeyword, meta{title,description}, label, summary, eyebrow?, h1, lead, sections[{id,title,paragraphs[],bullets?[]}], faq[{question,answer}], related[3], service?. Same as reference/site-rules.md §5. No difference logged.
- Home copy still in „ти“ register and still mentions "8 въпроса / 2-минутна AI диагностика" (owner replaced it by /diagnostika/; never mention).

## OWNER INSTRUCTIONS FOR THIS PAGE (run brief, owner's session 2026-11-15)
- Service page for the content tool (SEO articles, product descriptions, images, scheduled social posts with client approval) framed around SEO копирайтинг / SEO статии.
- Competitors answer „какво е SEO копирайтинг“ + how it works + how price is formed: do the same with canon only.
- Price: explain how it is formed, no numbers.
- 5–8 H2 sections + 5–8 FAQ.
- Extra deliverable: content/seo-statii.port.json (ContentPage object, strings identical to the content file; related = exactly 3 sibling paths).

## BUYER QUESTIONS (PAA, competitor headings/FAQ, suggestions)
Sources: Ahrefs SERP JSON (serp-seo_копирайтинг, serp-копирайтинг_услуги, 2026-11-15); seomax.bg #1 headings; linkbox.bg #1 headings + FAQ; WebSearch (bg query returned mostly RU/UA pages: price depends on volume, topic complexity, who works on it).
- Какво е SEO копирайтинг? — yes (general definition, no external numbers needed)
- Защо SEO копирайтингът е важен за бизнеса? — yes, without guarantees (no ranking/traffic promises)
- Какво включва услугата (статии за блог, продуктови описания, текстове за социални мрежи)? — yes (canon: SEO articles for industry and city, product descriptions for whole collections, images, scheduled social posts)
- Как се пише SEO статия / какво следят търсачките (ключови думи, структура, заглавия, мета данни)? — partly; general description of SEO копирайтинг practice is allowed as explanation, but no description of how BizGrow's tool works beyond canon
- Каква е цената на копирайтинг / от какво зависи? — yes, formation only: one-off price per fix in the report after the diagnosis, depends on what is built, no long-term contracts; no number
- Предлагате ли отстъпки при дългосрочни ангажименти? — no (offers banned; answer: no long-term contracts)
- Кой пише текстовете? С колко копирайтъри разполагате? — partly: BizGrow's own tool writes, the client approves; team size UNKNOWN
- На какъв език? / в моя тон? — no (not canon) → do not answer, or [OWNER CONFIRM]
- Кога ще видя резултат в Google? — no promise; can say no guarantee of positions is given, without the banned word
- Договори и фактури? — partly: no long-term contracts; invoicing details unknown

## CANDIDATE NEW SOURCES (max 3 new external facts; authoritative only)
- Google Search Central, "Creating helpful, reliable, people-first content" — https://developers.google.com/search/docs/fundamentals/creating-helpful-content — supports the general statement that Google aims to show helpful, people-first content (optional; synthesis decides).

## SIBLING PAGES (to avoid copied wording and term cannibalisation)
- / — ai автоматизация
- /ai-asistent/ — ai асистент
- /avtomatizacii/ — автоматизация на бизнес процеси
- /socialni-mrezhi/ — маркетинг в социалните мрежи (social posts are mentioned here only briefly and linked there)
- /reklama/ — реклама в гугъл
- /seo-optimizacia/ — seo оптимизация (technical SEO; this page must not target „seo оптимизация“, link to it instead)
- /diagnostika/ — безплатна диагностика за бизнеса

## NOTES
- Home card copy „Съдържание, което те извежда в Google.“ implies a ranking outcome; not reused.
- Checker's „за минути“ and „в твоя тон“ are outside canon; not used.
