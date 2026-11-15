# 00-BRIEF — BizGrow /reklama-vav-facebook/

MARKET: bg — small-business owners in Bulgaria (locale bg at `/`)
LOCALE: bg   PAIR: none (no EN row in keyword-map.md)
CONTENT TYPE: new-page (keyword-map row status `planned`: owner's session, 2026-11-15, "second Ahrefs pass; /reklama/ becomes Google-only")
PAGE: /reklama-vav-facebook/
SLUG: reklama-vav-facebook
MAIN TERM (BizGrow/keyword-map.md): платена реклама във фейсбук
SECONDARY: реклама във фейсбук (100, KD 0); фейсбук реклама (150, KD 0; moved from /reklama/); реклама във facebook (50); платена реклама в инстаграм (60); реклама в инстаграм (50, KD 0; moved from /reklama/); реклама във фейсбук цени (30); колко струва реклама във фейсбук (20); успешна реклама във фейсбук (30)
AHREFS: платена реклама във фейсбук | 150 | KD 0 | bg | 2026-11-15 (biz-grow docs/seo-audit/ahrefs-2026-11-15/mt-реклама_във.json; traffic potential 100; intents informational + commercial)
H1: keyword-map proposal „Реклама във Facebook и Instagram“ (new page, no current H1). The proposal does not carry the main term „платена реклама във фейсбук“; Outline/SEO decide whether to keep it or add the term (e.g. „Платена реклама във Facebook и Instagram“, the natural Latin-script variant). Any deviation from the keyword-map proposal gets an owner item.
SOURCE OF CURRENT PAGE: none (new page). Related current copy read from desislavamit/biz-grow @ feature/seo-improvements (local ~/Work/biz-grow-seo), commit a1ccf8f: site/src/i18n/dictionaries/bg.ts, site/src/content/types.ts, site/src/content/pages/bg/reklama.ts, docs/content-sources/skriti-problemi.json.
SERVICE (schema.org name, launching session's brief): „Реклама във Facebook и Instagram“

## CURRENT PAGE + INVENTORY
- 00-current.md written: yes (new page: lists existing owner copy that describes the marketing specialist, wording reference only)
- 00-inventory.md written: yes (20 items: 1+ booking CTA, email token optional, links /diagnostika/ + /reklama/ + /socialni-mrezhi/, 7 canon service facts, 4 process steps, 4 policies, 0 FAQs to preserve, 0 example labels required)

## SITE RULES RE-READ THIS RUN
- docs/ai-consultancy-spec.md / dictionaries / config.ts: same as reference/site-rules.md copy. config.ts has `bookingUrl` and `email` (written only as `{{BOOKING_URL}}` / `{{EMAIL}}`). Page model `ContentPage` in `site/src/content/types.ts`: path, locale, status, updated, primaryKeyword, meta{title,description}, label, summary, eyebrow?, h1, lead, sections[{id,title,paragraphs,bullets?,steps?,closing?}], faq[{question,answer}], related[], service?.
- Canon change 2026-11-15 (owner): the document after the diagnosis is „оферта“ (never „доклад“); NO delivery periods anywhere (no „до 48 часа“, „до 2 седмици“, „за дни“); only the 30-minute call carries a duration. Timing line if needed: „Срокът зависи от решението и го посочваме в офертата.“

## OWNER INSTRUCTIONS FOR THIS PAGE (launching session, 2026-11-15)
- Service page: paid advertising on Facebook and Instagram run by the marketing specialist (canon service 4).
- Main term „платена реклама във фейсбук“; secondaries per keyword-map (incl. „фейсбук реклама“, „реклама в инстаграм“, „колко струва реклама във фейсбук“).
- /reklama/ now covers Google only: link to it for Google Ads; never target its terms („реклама в гугъл“, „гугъл реклама“, „google ads …“, „онлайн реклама“, „реклама в интернет“, „ppc реклама“, „маркетинг специалист“).
- General facts about how Meta ads are billed only from Meta's official pages (max 3 sourced facts; a page that cannot be read is left out).
- Price: how BizGrow's price is formed, no numbers. Whether the ad budget (paid to Meta) is separate from BizGrow's fee is an OPEN OWNER ITEM: do not state it either way.
- 7–8 H2 sections + 6–8 FAQ.
- Deliverable also includes `content/reklama-vav-facebook.port.json` (ContentPage JSON) with exactly 3 related sibling paths from conversion-links.md (not /, not itself).
- REMOVE-BY-BRIEF: none.

## BUYER QUESTIONS (Ahrefs SERP for „платена реклама във фейсбук“ 2026-11-15; Ahrefs matching terms; 2 Bulgarian web searches 2026-11-15)
- Какво е платена реклама във Facebook и как работи? — partly: Tier B (Meta pricing page: the advertiser sets a daily or lifetime budget; can pause/cancel at any time); BizGrow side canon (specialist plans, runs, tracks)
- Колко струва реклама във фейсбук / реклама във фейсбук цени? — partly: Meta says cost depends on objective, ad quality, bidding strategy, performance goal, budget type (Tier B); BizGrow price per canon (formed after the free diagnosis, one-off, depends on what is built); NO numbers; budget-separation = owner item
- Как се прави реклама във фейсбук (стъпки, настройки)? — yes at a general level via BizGrow process + what the specialist does (plans, runs, tracks, reports)
- Как да направим реклама в инстаграм / платена реклама в инстаграм? — partly: the specialist plans Facebook and Instagram campaigns (brief I10); no platform mechanics beyond sources
- Подсилване (boost) на публикация или реклама през Ads Manager? — no canon/source readable (Meta help page 347839548598012 is JS-rendered) → avoid or answer only with canon („специалистът планира кампаниите“); do not explain boost mechanics
- Успешна реклама във фейсбук: от какво зависи? — partly: Meta source (objective, ad quality …) for cost; no promise of success; canon: data-driven campaigns, numbers in reports
- Как разбирам какво ми носи рекламата? — yes (canon: reports with numbers, what each euro returns; short monthly report)
- Кой прави визиите/рекламните материали? — yes (canon: криейтиви всеки месец → /socialni-mrezhi/)
- Може ли да спра рекламата? — yes (Tier B: „You can cancel or pause your ad at any time.“) + canon no long-term contracts
- Има ли договор / обвързване? — yes (canon)
- Чий е рекламният акаунт / достъпи, Pixel, Conversions API? — no (Tier 3 unknown) → do not answer; possible owner item
- Facebook или Google? — partly: link /reklama/ for Google; no performance comparison claims
- Колко бързо има резултат? — no (no guarantees, no periods) → answer around it

## CANDIDATE NEW SOURCES (max 3 new external facts; authoritative only)
All three from ONE official Meta for Business page (not a Help Center article; the Help Center articles are JS-rendered and unreadable):
- Meta for Business „Facebook Ads pricing“ — https://www.facebook.com/business/ads/pricing — fetched 2026-11-15 via WebFetch (readable body; plain curl returns HTTP 400 to non-browser clients, so Step 6 must re-check with WebFetch, not curl). Quotes:
  - S1 (budget): „Your budget is your most valuable cost control tool when creating an ad.“; daily budget: „This is the average amount you're willing to spend on an ad set or campaign per day.“; lifetime budget: „This is the amount you're willing to spend over the entire run of an ad or campaign.“
  - S2 (cost factors): „Your ad campaign’s objective plays a large role in impacting the cost of your ads.“; „These include: ad specifications (ad quality, bidding strategy, and performance goal) …“ (the list goes on with type of budget and objective)
  - S3 (control): „You can cancel or pause your ad at any time.“
- NOT usable (body JS-rendered, empty to fetch, 2026-11-15): Meta Business Help „Как да подсилите публикация във Facebook“ https://bg-bg.facebook.com/business/help/347839548598012 ; „How Meta Charges for Ads“ https://www.facebook.com/business/help/716180208457684 ; „About Ad Auctions“ https://www.facebook.com/business/help/430291176997542 → no facts from them.
- Do NOT use from the pricing page: the „$5 / six days“ recommendation, „up to 75% over daily budget“, the 2 million audience figure, the 5% opportunity-score figure (numbers that invite misreading; not needed).

## COMPETITOR PAGES (intent and structure only, never facts)
SERP „платена реклама във фейсбук“ (Ahrefs 2026-11-15): AI overview citing Meta Help + agencies; videos; #3 bg-bg.facebook.com help „Как да подсилите публикация“ (DR 100); #4 linkbox.bg „Плащане на реклама във Фейсбук“ (DR 32); #5 shopify.com/bg „Колко струват рекламите във Facebook“ (DR 97); #6 advanceacademy.bg „Как се прави реклама във Фейсбук: цена, настройки и измерване“ (DR 34); #7 a Facebook group post on accounting for ad payments; #8 neradigital.bg service page (DR 0); #9 improve.bg service page (DR 26); #10 marketingacademy.bg (DR 12). Intent: mixed informational/commercial: how it works + cost/payment + how to set up and measure + agency service. Winning shape: service page that answers „как работи + колко струва (как се формира) + как се измерва“ + FAQ.

## SIBLING PAGES (to avoid copied wording and term cannibalisation)
- / — ai автоматизация
- /reklama/ — реклама в гугъл (Google-only after the split; link for Google Ads)
- /socialni-mrezhi/ — маркетинг в социалните мрежи (NB its secondaries „реклама в социалните мрежи“, „социални мрежи реклама“, „рекламни визии“, „криейтиви“, „управление на социални мрежи“: do not target these here; link for monthly creatives and organic posts)
- /ai-asistent/ — ai асистент (owns „чатбот за фейсбук“, „чатбот messenger“; link only if replies to ad messages come up)
- /avtomatizacii/ — автоматизация на бизнес процеси
- /seo-statii/ — seo копирайтинг
- /seo-optimizacia/ — seo оптимизация
- /diagnostika/ — безплатна диагностика за бизнеса (link for the free diagnosis)
- /izrabotka-na-sait/, /izrabotka-na-onlain-magazin/ — изработка на сайт / онлайн магазин

## NOTES
- No earlier runs for this page. Other pages run in parallel in the same worktree; this run writes only in articles/2026-11-15-reklama-vav-facebook/ (temp files in its `_tmp/`).
- The home page copy no longer mentions „8 кратки въпроса“; never mention it. The diagnosis is /diagnostika/.
- Open owner items expected: ad budget separate from BizGrow's fee or not; who owns the ad account / access; whether Messenger/Audience Network placements are also run; H1 deviation from keyword-map (if any).
