# 00-brief — /izrabotka-na-onlain-magazin/

MARKET: bg — small-business owners in Bulgaria (locale bg at `/`)
LOCALE: bg   PAIR: none (no EN pair in keyword-map.md)
CONTENT TYPE: new-page (keyword-map row status `planned`; owner 2026-11-15)
PAGE: /izrabotka-na-onlain-magazin/
SLUG: izrabotka-na-onlain-magazin
MAIN TERM (BizGrow/keyword-map.md): изработка на онлайн магазин
SECONDARY: създаване на онлайн магазин (300, KD 0); изработка на онлайн магазин цена (100–150, KD 2); изработване на онлайн магазин (100, KD 6); платформа за онлайн магазин (150, KD 0); изработка онлайн магазин (90)
AHREFS: изработка на онлайн магазин | 1,100 | KD 0 | bg | 2026-11-15 (traffic potential 150; intent informational + commercial)
H1: keyword-map proposal „Изработка на онлайн магазин“ (new page, no current H1)
SOURCE OF CURRENT PAGE: desislavamit/biz-grow @ feature/seo-improvements (local ~/Work/biz-grow-seo) : no page yet; related copy in site/src/i18n/dictionaries/bg.ts + docs/content-sources/skriti-problemi.json, commit a1ccf8f
SERVICE (schema name, run brief): „Изработка на онлайн магазин“

## CURRENT PAGE + INVENTORY
- 00-current.md written: yes (new page; reference copy only)
- 00-inventory.md written: yes — 3 CTA/link items (booking, email, /diagnostika/), 2 tokens, 0 anchors, 13 canon facts, 1 canon number (30 минути), 0 example labels, 0 FAQs

## SITE RULES RE-READ THIS RUN
- Site repo @ a1ccf8f: content pages are typed `ContentPage` objects (site/src/content/types.ts): path, locale, status, updated, primaryKeyword, meta{title,description}, label, summary, eyebrow?, h1, lead, sections[{id,title,paragraphs[],bullets?[],steps?[],closing?[]}], faq[{question,answer}], related[], service?, tool?. `steps` and `closing` are newer than reference/site-rules.md §5; no other difference.
- Home copy (bg.ts) is now in „Вие“ register; process step 2 already says „оферта с приоритизирани решения и ясни еднократни цени“ and the home FAQ says „Срокът зависи от решението и го посочваме в офертата.“

## OWNER INSTRUCTIONS FOR THIS PAGE (run brief, owner's session 2026-11-15)
- Service page for canon service 6 (building online shops). 7–8 H2 + 6–8 FAQ. `service` = „Изработка на онлайн магазин“.
- Use the canon checker capabilities for shops where relevant: courier-status AI answers (link /ai-asistent/), SEO product descriptions for whole collections (link /seo-statii/), automatic messages for abandoned carts, connecting orders/spreadsheets/accounting so data fills itself in (link /avtomatizacii/).
- No platforms (WordPress, Shopify, WooCommerce …), payment or courier integrations, delivery times or prices unless canon: raise owner items.
- City variants (Варна, Бургас …) NOT targeted (no local offices, doorway risk).
- Canon changes 2026-11-15: the document after the diagnosis is „оферта“ (never „доклад“); NO delivery periods anywhere (no „до 48 часа“, „до 2 седмици“, „за дни“); only the 30-minute call carries a duration. Timing line if needed: „Срокът зависи от решението и го посочваме в офертата.“
- Extra deliverable: content/izrabotka-na-onlain-magazin.port.json (ContentPage object, strings identical to the content file; related = exactly 3 sibling paths from conversion-links.md).

## BUYER QUESTIONS (PAA, competitor headings/FAQ, suggestions)
Sources: Ahrefs SERP JSON serp-изработка_на_онлайн_магазин.json (2026-11-15: a1.bg DR 71 #1, then DR 0–39 studios: memotion.net, spinfludigital.com, evolutionofdreams.com, webprogress.bg, profiowebstudio.com, Webness (Shopify), Digital Hills (WooCommerce), raz.bg, FoxCode); WebFetch of webprogress.bg #5 headings + FAQ (data only); WebSearch bg „изработка на онлайн магазин цена въпроси“.
- Колко струва изработка на онлайн магазин / от какво зависи цената? — yes, formation only: one-off price, depends on what is built, given in the offer after the diagnosis; no number, no range
- Колко време отнема изработката? — yes, only with the canon line „Срокът зависи от решението и го посочваме в офертата.“
- Коя платформа е най-добра за онлайн магазин (WooCommerce, Shopify, собствено решение)? — no (platforms not canon) → [OWNER CONFIRM]; may say the choice is discussed in the diagnosis/offer only if phrased without naming platforms or promising a specific one
- Какви плащания и доставки/куриери се свързват? — no (payment/courier integrations not canon) → [OWNER CONFIRM]; canon only: an AI connected to the courier answers parcel-status questions
- Мога ли сам да поддържам магазина след пускането? / поддръжка — partly: canon monthly support with a short report; whether the client edits products himself is not canon → [OWNER CONFIRM]
- Магазинът ще се вижда ли в Google веднага? — no guarantee; can point to SEO product descriptions (/seo-statii/) and SEO optimisation (/seo-optimizacia/) without promising positions
- Как да описвам много продукти? — yes: SEO product descriptions for whole collections (canon, „за минути“ NOT used)
- Какво се случва с изоставените колички? — yes: automatic messages for abandoned carts (canon; „едни от най-лесните продажби“ is a claim, not used)
- „Къде ми е поръчката?“ въпроси от клиенти — yes: AI connected to the courier answers with parcel status (canon wording; „в реално време“ kept only as the owner's checker wording if the Gate allows)
- Прехвърляне на данни между поръчки, таблици и счетоводство — yes: connecting systems so data fills itself in (canon)
- Домейн, хостинг, SSL, кой притежава магазина, обучение, ревизии — no (Tier 3 / not canon) → do not answer, or [OWNER CONFIRM]
- Има ли договор / обвързване? — yes: no long-term contracts; the diagnosis commits to nothing

## CANDIDATE NEW SOURCES (max 3 new external facts; authoritative only)
- none planned. A shop-building page does not need external statistics; the synthesis may propose at most one Tier B fact only from an authoritative source (e.g. a public regulator) and must flag it [VERIFY].

## SIBLING PAGES (to avoid copied wording and term cannibalisation)
- / — ai автоматизация
- /izrabotka-na-sait/ — изработка на сайт (being drafted in parallel; this page must not target „изработка на сайт“, „изработка на уебсайт“, „поддръжка на сайт“; link there for ordinary websites and website maintenance)
- /ai-asistent/ — ai асистент (courier-status answers: link there)
- /avtomatizacii/ — автоматизация на бизнес процеси (connecting orders, spreadsheets, accounting: link there)
- /seo-statii/ — seo копирайтинг (product descriptions: link there)
- /seo-optimizacia/ — seo оптимизация (owns „seo за онлайн магазин“, „seo оптимизация на онлайн магазин“: never target them here; link there)
- /socialni-mrezhi/ — маркетинг в социалните мрежи
- /reklama/ — реклама в гугъл; /reklama-vav-facebook/ — платена реклама във фейсбук
- /diagnostika/ — безплатна диагностика за бизнеса

## NOTES
- Home results row „Онлайн магазин … 80% от повтарящите се въпроси с отговор за секунди.“ is a hypothetical example still under [OWNER CONFIRM] per canon; not reused here.
- Checker wording outside canon, not used: „за минути“, „в твоя тон“, „едни от най-лесните продажби“.
