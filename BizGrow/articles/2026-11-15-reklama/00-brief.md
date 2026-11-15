# 00-BRIEF — BizGrow /reklama/

MARKET: bg — small-business owners in Bulgaria (locale bg at `/`)
LOCALE: bg   PAIR: none (no EN row in keyword-map.md)
CONTENT TYPE: new-page (keyword-map row status `planned`: owner's session, 2026-11-15)
PAGE: /reklama/
SLUG: reklama
MAIN TERM (BizGrow/keyword-map.md): реклама в гугъл
SECONDARY: гугъл реклама (100, KD 0); google реклама (80, KD 5); google ads реклама (90, KD 0); реклама в google (50, KD 1); реклама в гугъл цена (50, KD 0); онлайн реклама (150, KD 2); реклама в интернет (150, KD 0); ppc реклама (150, KD 0); фейсбук реклама (150, KD 0); реклама в инстаграм (50, KD 0); маркетинг специалист (150, KD 0; jobs SERP, secondary only)
AHREFS: реклама в гугъл | 400 | KD 0 | bg | 2026-11-15 (topic-backlog.md row 4: commercial)
H1: keyword-map proposal „Реклама в Google и Facebook с маркетинг специалист“ (new page, no current H1). Note: the H1 must carry the main term once; the proposal uses „Реклама в Google“ (Latin spelling), which is the natural variant of „реклама в гугъл“. Outline/SEO decide; any deviation from the keyword-map proposal gets an owner item.
SOURCE OF CURRENT PAGE: none (new page). Related current copy read from desislavamit/biz-grow @ feature/seo-improvements (local ~/Work/biz-grow-seo), commit 528ad25: site/src/i18n/dictionaries/bg.ts, site/src/content/types.ts, docs/content-sources/skriti-problemi.json.
SERVICE (schema.org name, from the owner's session brief): „Реклама в Google и Facebook“

## CURRENT PAGE + INVENTORY
- 00-current.md written: yes (new page: no current copy; lists the existing site copy that describes the marketing specialist, for wording reference only)
- 00-inventory.md written: yes (new page: the mandatory items this page must carry: 1 booking CTA token, 1 email token optional, canon facts for the marketing-specialist service, process, policies, price formation; 0 FAQs to preserve; 0 example labels unless an example is added)

## SITE RULES RE-READ THIS RUN
- docs/ai-consultancy-spec.md / dictionaries / config.ts: same as reference/site-rules.md copy. config.ts has `bookingUrl` and `email` (written only as `{{BOOKING_URL}}` / `{{EMAIL}}`). Page model is `ContentPage` in `site/src/content/types.ts` (path, meta, label, summary, eyebrow, h1, lead, sections[{id,title,paragraphs,bullets?}], faq, related, service).

## OWNER INSTRUCTIONS FOR THIS PAGE (owner's session, 2026-11-15)
- Service page for the marketing specialist: Google Ads and Facebook/Instagram advertising planned, run and tracked by a real specialist who reports with numbers (what each euro returns).
- Cover how advertising in Google works for a small business at a practical level: only general, verifiable facts; max 3 sourced external facts.
- What BizGrow does; how reporting works (canon wording only); how price is formed (no numbers). The ad budget itself being separate from BizGrow's fee is NOT in the canon → state only what a source supports about the ad platform (Google charges the advertiser for clicks; the advertiser sets the daily budget) and raise an owner item about whether BizGrow's price excludes the ad budget.
- 6–8 H2 sections + 6–8 FAQ.
- Deliverable also includes `content/reklama.port.json` (ContentPage JSON) with 3 related sibling paths.
- REMOVE-BY-BRIEF: none.

## BUYER QUESTIONS (SERP titles for „реклама в гугъл“, Ahrefs 2026-11-15; web search 2026-11-15)
- Какво е реклама в Google (Google Ads) и как работи? — yes (Tier B Google help: pay when someone clicks; you decide the average daily amount; placement depends on competition, ad rank, quality, budget settings)
- Колко струва реклама в Гугъл / „реклама в гугъл цена“? — partly: explain how price is formed without numbers; Google ad cost depends on clicks and the budget the advertiser sets (Tier B); BizGrow price per canon (formed after the free diagnosis, depends on what is built, no long-term contracts); no numbers
- Как се прави реклама в Гугъл (стъпки)? — yes at a general level via the BizGrow process + what the specialist does (plans, runs, tracks)
- Предимства и недостатъци на рекламата в Google? — partly; avoid opinions; can say the ad shows to people searching, cost tied to clicks (source)
- Гарантира ли по-висока оферта първо място? — yes (Tier B: covering or exceeding the forecast does not guarantee placement)
- Google или Facebook/Instagram реклама: кое е за мен? — partly: the specialist plans which channels; no claims about performance
- Как разбирам какво ми носи рекламата? — yes (canon: reports with numbers, shows what each euro returns; monthly short report)
- Има ли договор / обвързване? — yes (canon: no long-term contracts; diagnosis commits to nothing)
- Кой прави рекламите/визиите? — yes (canon: криейтиви всеки месец, link /socialni-mrezhi/)
- Колко бързо има резултат? — no (Tier C, no guarantees) → answer around it, no promise

## CANDIDATE NEW SOURCES (max 3 new external facts; authoritative only)
- Google Ads Help (bg) „Използване на Google Ads за онлайн маркетинг“ — https://support.google.com/google-ads/answer/6227565?hl=bg — HTTP 200 (2026-11-15) — quotes: „Ви таксуваме само когато някой е достатъчно заинтересуван да кликне върху рекламата Ви“; „Вие решавате средната сума, която искате да изразходвате всеки ден.“
- Google Ads Help (bg) „Показване на рекламите Ви на първа страница“ — https://support.google.com/google-ads/answer/2472742?hl=bg — HTTP 200 (2026-11-15) — quotes: „Крайното разположение продължава да зависи от конкуренцията на други рекламодатели, рекламния Ви ранг“; „се основават на качествения рейтинг на ключовата Ви дума и досегашната конкуренция“; „Покриването или надвишаването на тази прогнозна стойност обаче не Ви гарантира рекламно разположение.“
- Meta Business Help „About Ad Auctions“ — https://www.facebook.com/business/help/430291176997542 — HTTP 200 but body is JS-rendered; the passage could not be read → NOT usable as a source this run (no Meta facts in the text).

## COMPETITOR PAGES (intent and structure only, never facts)
SERP „реклама в гугъл“ (Ahrefs 2026-11-15): AI overview; support.google.com (#2); onlinereklamabg.com „Платена Реклама в Google | Реклама в Гугъл Цена“ (#3); ads.google (#4); bg.wikipedia Google Ads (#5); maxgraphic.bg service page with a price in the title (#6); seomax.bg „Предимства и недостатъци“ (#7); groweasy.bg „Как се прави реклама в Гугъл | 6 стъпки“ (#8); digital.softuni.bg (#9). Intent: mixed informational/commercial: what it is + how it works + price + steps. Winning shape per NICHE-ANALYSIS: „какво е + как работи + цена/как се формира + FAQ“.

## SIBLING PAGES (to avoid copied wording and term cannibalisation)
- / — ai автоматизация
- /ai-asistent/ — ai асистент
- /avtomatizacii/ — автоматизация на бизнес процеси
- /seo-statii/ — seo копирайтинг
- /socialni-mrezhi/ — маркетинг в социалните мрежи (NB: its secondaries include „реклама в социалните мрежи“, „социални мрежи реклама“, „рекламни визии“, „криейтиви“: do not target these here; link to /socialni-mrezhi/ for creatives)
- /seo-optimizacia/ — seo оптимизация (do not target „seo“ terms; link for organic results)
- /diagnostika/ — безплатна диагностика за бизнеса (link for the free diagnosis)

## NOTES
- No earlier runs for this page. Other pages run in parallel in the same worktree; this run writes only in articles/2026-11-15-reklama/.
- The home page copy still says „8 кратки въпроса / 2-минутна AI диагностика“: never mention it (owner decision); the diagnosis is /diagnostika/.
