# 00-BRIEF — /seo-optimizacia/

MARKET: bg — small-business owners in Bulgaria (locale bg at `/`)
LOCALE: bg   PAIR: none (no EN row in keyword-map.md)
CONTENT TYPE: new-page (keyword-map row status `planned`: owner's session 2026-11-15, "owner confirmed full SEO 2026-11-15")
PAGE: /seo-optimizacia/
SLUG: seo-optimizacia
MAIN TERM (BizGrow/keyword-map.md): seo оптимизация
SECONDARY: seo услуги (300, KD 4); seo агенция (200, KD 2); seo експерт (200, KD 1); seo оптимизация на сайт (200, KD 6); seo оптимизация на сайтове (200, KD 9); seo фирма (150, KD 12); seo компания (100, KD 0); seo услуги цена (150, KD 0); seo оптимизация цена (150, KD 0); seo цена (90, KD 0); seo за онлайн магазин (100); seo оптимизация на онлайн магазин (60, KD 0); техническо seo (250)
AHREFS: seo оптимизация | 600 | KD 29 | bg | 2026-11-15
H1: keyword-map proposal „SEO оптимизация на сайтове“ (new page, no current H1)
SOURCE OF CURRENT PAGE: none (new page). Site context read from desislavamit/biz-grow @ feature/seo-improvements, commit 528ad25c3b7be5a9a48d38740ab1bc955512d2a9 (site/src/i18n/dictionaries/bg.ts, site/src/content/types.ts, site/src/components/ContentPageView.tsx, site/src/i18n/config.ts).

## CURRENT PAGE + INVENTORY
- 00-current.md written: yes (new page: no current copy; records the site context the page sits in)
- 00-inventory.md written: yes — 0 CTAs, 0 tokens, 0 anchors, 0 FAQs carried from a current page (new page). It lists the REQUIRED items for this new page instead (owner/brief requirements that every stage must keep).

## SITE RULES RE-READ THIS RUN
- dictionaries / config.ts / types.ts: same as reference/site-rules.md copy. Notes:
  - Content pages render from `ContentPage` (`site/src/content/types.ts`). The template (`ContentPageView.tsx`) already renders a booking button („Запазете час“ via `BookingLink` → `site.bookingUrl`) and a „Безплатна диагностика“ button to `/diagnostika/` under the lead, plus a CTA band and related links at the end. Inline syntax in `ContentPage` strings: `**bold**`, `[label](/path/)`, `[label](#anchor)` only; no `{{TOKEN}}` in the port file. The content .md may still carry `{{BOOKING_URL}}` / `{{EMAIL}}` CTAs per template; the port JSON expresses the next step with links to `/diagnostika/` or `/#contact`.

## OWNER INSTRUCTIONS FOR THIS PAGE
- Service page for full SEO optimisation: technical SEO, on-page optimisation, links (canon item 5; nothing more specific is canon: no tools, audit length, link counts, positions, timelines).
- General explanations of what technical SEO / on-page / links are may use max 3 sourced facts.
- MUST link /seo-statii/ for content (SEO articles/copywriting live there; do not target „seo копирайтинг“/„seo статии“ here).
- No ranking guarantees (no positions, traffic, leads, timeframes).
- 6–8 H2 + 6–8 FAQ.
- `service` (schema name): „SEO оптимизация“.
- Prices: explain how the price is formed (one-off price per fix in the report after the free diagnosis; depends on what is built; no long-term contracts). Never a number or range, even though „seo услуги цена“ / „seo оптимизация цена“ / „seo цена“ are secondary terms.
- Do not target parked phase-2 terms „локално seo“ (/seo-optimizacia/lokalno-seo/) and „seo одит“ (/seo-optimizacia/seo-odit/): these addresses are parked and are NOT in conversion-links.md, so no links to them. A plain-word mention of a „проверка“/„преглед“ of the site is fine; avoid using „SEO одит“ / „локално SEO“ as headings or repeated phrases.

## BUYER QUESTIONS (PAA, competitor FAQ headings, suggestions)
Sources: Ahrefs SERP „seo услуги“ (2026-11-15: seomax.bg, zaharaconsult.com, netpeak.bg, maxdigital.bg, vodanamars.com, optimystica.com; AI overview present), web search „SEO оптимизация на сайт какво включва цена въпроси“, FAQ headings of seomax.bg/services/seo-optimizaciya/ and zaharaconsult.com/seo-uslugi/ (intent only, no facts taken).
- Какво включва SEO оптимизацията (техническо SEO, on-page, връзки)? — yes (canon item 5 + general explanation, sourced where needed)
- Нуждае ли се бизнесът ми от SEO оптимизация? / За кого е подходяща? — yes (canon audience)
- Защо сайтът ми не се показва в Google? — partly (general causes in plain words; no promises)
- Каква е цената на SEO услугата? — yes (how the price is formed; no numbers)
- Колко време отнема / кога ще видя резултати? — partly: no timeframe for rankings is canon; can say BizGrow does not promise positions or timelines; canon process times only (48 часа report, build обикновено до 2 седмици for fixes)
- Можете ли да гарантирате първо място? — yes (no; Google's own guidance, sourced)
- SEO или Google Ads (реклама) — кое е по-добро? — yes, carefully: link /reklama/ for ads; do not target „реклама в гугъл“
- Еднократна услуга ли е оптимизацията? — yes (one-off fixes + monthly support with a short report; no long-term contracts)
- Какво включва on-page SEO? — yes (general explanation)
- SEO за онлайн магазин? — yes (canon audience includes online shops; SEO product descriptions for whole collections are canon via the content tool → /seo-statii/)
- Кой притежава достъпите / какво остава под контрол на клиента? — partly; do not invent access policies; flag OWNER CONFIRM if needed

## CANDIDATE NEW SOURCES (max 3 new external facts; authoritative only)
1. Google Search Central, „Do you need an SEO?“ — https://developers.google.com/search/docs/fundamentals/do-i-need-seo — HTTP 200 (2026-11-15) — quote: "If they guarantee you that their changes will give you first place in search results, find someone else." Also lists what an SEO can help with: "Review of your site content or structure", "Technical advice on website development: for example, hosting, redirects, error pages, use of JavaScript", "Keyword research".
2. Google Search Central, „Spam policies for Google web search“ — https://developers.google.com/search/docs/essentials/spam-policies — HTTP 200 (2026-11-15) — quote: "Link spam is the practice of creating links to or from a site primarily for the purpose of manipulating search rankings. The following are examples of link spam: Buying or selling links for ranking purposes."
3. Google Search Central, „SEO Starter Guide“ — https://developers.google.com/search/docs/fundamentals/seo-starter-guide — HTTP 200 (2026-11-15) — general reference for on-page basics (titles, descriptions, content for people); use only if a specific quoted passage is fetched at Step 6.

## SIBLING PAGES (to avoid copied wording and term cannibalisation)
- / — ai автоматизация
- /ai-asistent/ — ai асистент
- /avtomatizacii/ — автоматизация на бизнес процеси
- /seo-statii/ — seo копирайтинг (also owns: копирайтинг услуги, seo статии, seo текстове, писане на статии, описания на продукти) — MUST be linked from this page for content
- /socialni-mrezhi/ — маркетинг в социалните мрежи
- /reklama/ — реклама в гугъл (also owns: google реклама, ppc реклама, онлайн реклама …)
- /diagnostika/ — безплатна диагностика за бизнеса
- parked, not linkable: /seo-optimizacia/lokalno-seo/ — локално seo; /seo-optimizacia/seo-odit/ — seo одит

## NOTES
- First run for this page; no earlier owner items.
- Deliverables for this run: `content/seo-optimizacia.md` (template) AND `content/seo-optimizacia.port.json` (`ContentPage` object: path, locale "bg", status "published", updated "2026-11-15", primaryKeyword, meta{title,description}, label, summary, eyebrow, h1, lead, sections[{id,title,paragraphs,bullets?}], faq[{question,answer}], related[3 sibling paths], service "SEO оптимизация"). Strings identical to the content file. Section ids short latin kebab-case. `related` = 3 sibling paths from conversion-links.md (not /, not itself) — /seo-statii/ should be one.
- Niche analysis: the SERP rewards "какво е + как работи + цена/как се формира + FAQ" service pages. KD 29 for the main term; secondary „seo услуги“ KD 4.
- Step 7: no GEMINI_API_KEY locally → skipped. Step 8: none.
