# 00-brief — /diagnostika/

MARKET: bg — small-business owners in Bulgaria (locale bg at `/`)
LOCALE: bg   PAIR: none (no EN pair planned)
CONTENT TYPE: new-page (keyword-map row status `planned`; owner's session 2026-11-15; topic-backlog #2)
PAGE: /diagnostika/
SLUG: diagnostika
MAIN TERM (BizGrow/keyword-map.md): безплатна диагностика за бизнеса   SECONDARY: дигитализация на бизнеса; къде губи време бизнесът
AHREFS: безплатна диагностика за бизнеса | no measurable volume | KD – | bg | 2026-11-15 (conversion page; "no measurable search term")
H1: keyword-map proposal „Безплатна диагностика: къде губи време Вашият бизнес“ (new page, no current H1)
SOURCE OF CURRENT PAGE: biz-grow @ feature/seo-improvements (local ~/Work/biz-grow-seo), commit 528ad25c3b7be5a9a48d38740ab1bc955512d2a9: docs/content-sources/skriti-problemi.json (untracked owner source), site/src/content/types.ts, site/src/content/diagnostika/types.ts, site/src/components/Checker.tsx, ContentPageView.tsx, dictionaries/bg.ts (home canon wording)

## CURRENT PAGE + INVENTORY
- 00-current.md written: yes (owner checker source verbatim + home-page canon lines)
- 00-inventory.md written: yes — 1 booking CTA + email line, 2 tokens, 0 existing anchors, 8 canon facts, 29 problem items (hours/types/solutions exact), 2 labels (hours estimate; examples not client data), 0 FAQs

## SITE RULES RE-READ THIS RUN
- config.ts: bookingUrl and email present (tokens {{BOOKING_URL}}, {{EMAIL}} stand for them). Home dictionary still says „2-минутна AI диагностика на сайта“ (informal, superseded by owner decision: replaced by this page). Same as reference/site-rules.md otherwise.
- Page model: ContentPage (site/src/content/types.ts) with `tool: "diagnostika"`, no `service`; checker data CheckerData (site/src/content/diagnostika/types.ts). In the rendered page the checker's 4 group titles are H2s, then page sections are H2s, then FAQ.

## OWNER INSTRUCTIONS FOR THIS PAGE (owner's session brief, 2026-11-15)
- The owner's "Скрити проблеми" checker becomes this page. Rewrite EVERY string to formal „Вие“ (29 pain/fix pairs, 4 group titles + subs, 9 business-type names, solution titles, UI labels), keeping each item's meaning, business types, hours and solution keys exactly, in source order.
- Hours are owner estimates and must be labelled „ориентировъчно, на база типични случаи“.
- "29 реални примера" may NOT be claimed as client data; call them examples.
- Structure: short lead explaining how to use the checker (pick business type, tick what applies, see rough hours a week, book the free diagnosis + 30-min call → report in 48 h, canon) → the checker (rendered by the site) → 2–3 short H2 sections (what happens in the free diagnosis; what you get; no obligation) → 4–6 FAQ.
- Solution key → page, one href per key: a → /avtomatizacii/, t → /seo-statii/, c → /socialni-mrezhi/, m → /reklama/. (AI assistant items conceptually relate to /ai-asistent/, but keep one href per key; /ai-asistent/ may be linked from body copy.)
- Deliverables: content/diagnostika.md (template) + content/diagnostika.port.json = {"page": ContentPage, "checker": CheckerData}; port rules: strings identical to content file; inline only **bold** and [label](/path/ or #anchor); no em-dashes; meta.title ≤ 60 incl. " | BizGrow"; meta.description 120–160; related = exactly 3 sibling paths from conversion-links.md (not / and not itself); "tool":"diagnostika", no service; status "published", updated "2026-11-15".
- REMOVE-BY-BRIEF: the source footer line („© 2026 BizGrow · …“) is not page copy; the claim „29 реални примера“ (replaced by „примери“).

## BUYER QUESTIONS (web search bg 2026-11-15: „безплатна диагностика за бизнеса автоматизация консултация“, „дигитализация на бизнеса безплатна консултация малък бизнес къде губи време“; Ahrefs SERP files contain no SERP for this term)
- What exactly does the free diagnosis include (interview, analysis, recommendations, report)? — yes (canon: 30-min call, report in 48 h with prioritised fixes and one-off prices)
- Am I obliged to buy anything afterwards? — yes (canon: commits to nothing; no long-term contracts)
- How long does it take / when do I get the result? — yes (30 min; report within 48 h)
- What should I prepare / which processes to look at first (the slowest, most repetitive ones: invoicing, offers, enquiries, bookings)? — yes, partially (checker items; no new facts)
- How much does the fix cost after the diagnosis? — yes, without a number (one-off price per fix in the report; depends on what is built)
- How long does building take? — yes (usually up to 2 weeks)
- Are the hours exact? — yes (rough estimates based on typical cases)
- Is my data safe? — only „Работим по GDPR“
- What if my business type is not listed? — yes („B2B / друго“ filter, „Всички бизнеси“)

## CANDIDATE NEW SOURCES (max 3 new external facts; authoritative only)
- none (a conversion page; search returned only vendor blogs, not Tier B)

## SIBLING PAGES (to avoid copied wording and term cannibalisation)
- / — ai автоматизация
- /ai-asistent/ — ai асистент
- /avtomatizacii/ — автоматизация на бизнес процеси
- /seo-statii/ — seo копирайтинг
- /socialni-mrezhi/ — маркетинг в социалните мрежи
- /reklama/ — реклама в гугъл
- /seo-optimizacia/ — seo оптимизация
(do not target these terms; generic mentions of the services in the checker fixes are fine)

## NOTES
- Owner decisions: the "8 questions / 2-minute AI diagnosis" questionnaire is replaced by this page; never mention "8 questions" or "2-минутна".
- „за дни, не месеци“ needs [OWNER CONFIRM] if used (avoid).
- Pain details with numbers (21:30, 10 въпроса, 23:00, …) are illustrative; keep them inside the labelled examples and raise one owner item.
