MARKET: bg — small-business owners in Bulgaria (locale bg at `/`)
LOCALE: bg   PAIR: en-home
CONTENT TYPE: page-rewrite (keyword-map row status `planned`, owner's session 2026-11-15)
PAGE: /
SLUG: home
MAIN TERM (BizGrow/keyword-map.md): ai автоматизация
SECONDARY: автоматизация (150, KD 0); ai за бизнеса; изкуствен интелект в бизнеса (10); ai агенция (10); ai решения за бизнеса; автоматизация за малък бизнес
AHREFS: ai автоматизация | 40 | KD not stored (Ahrefs has no SERP data for this term, volume too small) | bg | 2026-11-15
H1: current „По-малко рутина. / Повече бизнес.“ ; keyword-map proposal „AI автоматизация за малкия бизнес“
SOURCE OF CURRENT PAGE: desislavamit/biz-grow @ feature/seo-improvements : site/src/i18n/dictionaries/bg.ts + HomePage.tsx, Sections.tsx, Contact.tsx, HeroVisual.tsx, commit 528ad25c3b7be5a9a48d38740ab1bc955512d2a9

## CURRENT PAGE + INVENTORY
- 00-current.md written: yes
- 00-inventory.md written: yes — 6 CTAs, 2 tokens, 8 anchors, 9 canon facts, 8 numbers, 2 labels (1 example label), 3 example rows, 0 FAQs

## SITE RULES RE-READ THIS RUN
- dictionaries / config.ts: same as reference/site-rules.md copy. Differences: branch feature/seo-improvements adds `page` and `a11y.breadcrumb` keys and content-page routes; `#ads` already removed; `hero.overlayValue` omitted (overlay is a phrase). Booking URL and email unchanged (tokens).

## OWNER INSTRUCTIONS FOR THIS PAGE (owner's session 2026-11-15)
- Formal „Вие“ everywhere; convert every „ти“ form.
- Title/meta/H1 aimed at „ai автоматизация“; keep the slogan feel. The H1 has two lines (`hero.line1` + `hero.line2`); the main term must be in the H1 or the hero body's first sentence.
- Services section: SIX cards, one per service page, each with `href`: /ai-asistent/, /avtomatizacii/, /seo-statii/, /socialni-mrezhi/, /reklama/, /seo-optimizacia/. `icon` ∈ spark | loop | brain (repeats fine).
- Losses section: add a link to /diagnostika/ („вижте всички примери за Вашия бранш“ style).
- Hero primary CTA stays booking.
- REMOVE-BY-BRIEF: hero figures „8 кратки въпроса“ / „2 мин за попълване“ (questionnaire no longer exists) → canon figures (e.g. 30 мин разговор, 48 ч доклад, 0 обвързване) or an owner item. Process step 1 wording about the 2-minute questionnaire → free diagnosis page /diagnostika/ + 30-minute call. Four-card service set incl. „Решения по поръчка“ → six cards. Ads section already removed.
- Add a FAQ section (5–7 questions, canon-answerable) before #contact (new anchor `#faq`, new key `faq`).
- Keep every other section, anchor and the hypothetical label on #results.
- Deliverable also includes `content/home.port.json` (exact `bg` shape + listed changes).

## BUYER QUESTIONS (web search bg „ai автоматизация за малък бизнес“, „AI автоматизация на бизнеса колко струва“; Ahrefs SERP „автоматизация“; ai автоматизация SERP empty in Ahrefs)
- Какво може да се автоматизира в малък бизнес? — yes (canon: messages, booking, offers, documents, invoices, connected systems, dashboards)
- Колко струва AI автоматизацията? — yes at canon level only (one-off price per fix, in the report after the diagnosis; no number)
- Откъде да започна / първо одит на процесите? — yes (free diagnosis, 30-min call, report in 48 h)
- Колко време отнема внедряването? — yes („обикновено до 2 седмици“)
- Заменя ли AI служителите / има ли човешки контрол? — yes (client approves content; real specialist runs marketing)
- Какво става с данните / GDPR? — yes, only „Работим по GDPR“
- Трябва ли дългосрочен договор / месечна поддръжка? — yes (no long-term contracts; monthly support with short report)
- Подходящо ли е за моя бранш? — yes (canon audience list)
- ROI / колко се спестява? — no (no invented numbers; only labelled examples)

## CANDIDATE NEW SOURCES (max 3 new external facts; authoritative only)
- none proposed (search results are vendor blogs; not authoritative). 0 new facts planned.

## COMPETITOR PAGES (intent only)
- digitalagent.bg/ai-avtomatizacia/ („АИ автоматизация: какво е и как работи за бизнеса“, #9 for „автоматизация“) — explainer + service intent.
- SERP for „автоматизация“ is informational (Wikipedia, Vtiger, речник); commercial page wins on clarity of what is automated.

## SIBLING PAGES (avoid copied wording and term cannibalisation; link only via conversion-links.md paths)
- /ai-asistent/ — ai асистент
- /avtomatizacii/ — автоматизация на бизнес процеси
- /seo-statii/ — seo копирайтинг
- /socialni-mrezhi/ — маркетинг в социалните мрежи
- /reklama/ — реклама в гугъл
- /seo-optimizacia/ — seo оптимизация
- /diagnostika/ — безплатна диагностика за бизнеса
The home page must not target these main terms (it may name the service in a card title linking to the page, but must not repeat the exact main term as its own focus).

## NOTES
- No earlier owner items for this page (first run).
- Canon still needs [OWNER CONFIRM] for „за дни, не месеци“ and the three example rows (E1–E3).
- Home dictionary has no `related` key; the port JSON keeps the exact `bg` shape (no `related` added), noted for the human.
