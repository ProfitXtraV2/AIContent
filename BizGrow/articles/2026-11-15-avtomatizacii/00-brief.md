# 00-BRIEF — /avtomatizacii/ (BizGrow)

MARKET: bg — small-business owners in Bulgaria (locale bg at `/`)
LOCALE: bg   PAIR: none (no EN row in keyword-map.md)
CONTENT TYPE: new-page (keyword-map row status `planned`; approved by the owner's session 2026-11-15, owner un-paused the pipeline for manual runs 2026-11-15)
PAGE: /avtomatizacii/
SLUG: avtomatizacii
MAIN TERM (BizGrow/keyword-map.md): автоматизация на бизнес процеси
SECONDARY: софтуер за автоматизация (100); софтуерна автоматизация (60); онлайн записване; онлайн резервации (10, KD 2); автоматични оферти; автоматизация на документи; автоматично фактуриране; sms напомняне; табло с показатели
AHREFS: автоматизация на бизнес процеси | 10 | KD not measured | BG | 2026-11-15 (topic-backlog row 7; keyword-map volume 10). Related: автоматизация 150 (KD 0, SERP informational: Wikipedia #1, technologica RPA #2, digitalagent.bg DR 12 at #9); софтуер за автоматизация 100; софтуерна автоматизация 60.
H1: keyword-map proposal „Автоматизация на бизнес процеси“
SERVICE (schema): „Автоматизация на бизнес процеси“
SOURCE OF CURRENT PAGE: none (new page). Site source read for the model: desislavamit/biz-grow @ feature/seo-improvements (local ~/Work/biz-grow-seo), commit 528ad25: `site/src/content/types.ts` (ContentPage type), `site/src/i18n/config.ts`, `docs/content-sources/skriti-problemi.json` (owner checker source), `docs/seo-audit/NICHE-ANALYSIS-2026-11-15.md`, `docs/seo-audit/keyword-map.md`, `docs/seo-audit/ahrefs-2026-11-15/serp-автоматизация.json`.

## CURRENT PAGE + INVENTORY
- 00-current.md written: yes (new page: no current copy; records the source data used)
- 00-inventory.md written: yes — required items for a new service page: 2 CTAs/tokens, 0 existing anchors, canon facts listed, 3 canon numbers, 1 example label (only if an example is used), 0 existing FAQs

## SITE RULES RE-READ THIS RUN
- types.ts (ContentPage): `path, locale, status, updated, primaryKeyword, meta{title,description}, label, summary, eyebrow?, h1, lead, sections[{id,title,paragraphs[],bullets?[]}], faq[{question,answer}], related[], service?, tool?`. Same as reference/site-rules.md §5. Inline syntax only `**bold**` and `[label](/path/)` / `[label](#anchor)`. NOTE: `#anchor` on a content page resolves to the HOME page section (`resolveHref` in config.ts), so `[…](#process)` = home `#process`. Prefer `/#process` style per conversion-links.md.
- config.ts: booking URL and email are in `site` (tokens `{{BOOKING_URL}}`, `{{EMAIL}}`). No difference from site-rules.md.

## OWNER INSTRUCTIONS FOR THIS PAGE (launching session, 2026-11-15)
- Service page: automation of business processes — online booking synced with a calendar + reminders + waitlist, automatic offers (form → PDF, offer from photos), document and invoice automation, contract templates, connecting systems, publishing listings once, real-time dashboard, AI meeting summary (all canon). Group by business area; mention which business types benefit (canon audience). 6–8 H2 + 6–8 FAQ.
- Deliverable additionally needs `content/avtomatizacii.port.json` (ContentPage object, strings exactly as in the content file, `related` = 3 sibling paths from conversion-links.md, not `/`, not itself; `meta.title` ≤ 60 incl. " | BizGrow"; `meta.description` 120–160).
- REMOVE-BY-BRIEF: none (new page).

## BUYER QUESTIONS (Bulgarian web search 2026-11-15 + SERP for „автоматизация“ + competitor headings)
- Какво е автоматизация на бизнес процеси? — yes (plain definition: repeating, rule-based tasks done by software; canon examples)
- Кои процеси да автоматизирам първо? — partly: canon process (free diagnosis finds where the business loses time; report with prioritised fixes); never name a universal "first" process
- Подходяща ли е автоматизацията за малък бизнес / за моя тип бизнес? — yes (canon audience + per-business capabilities from skriti-problemi.json)
- Трябва ли да сменя програмите, които ползвам? / Трябва ли да знам програмиране? — partly: canon says „connecting the systems a business already uses“; nothing beyond that
- Колко струва автоматизацията? — yes at canon level only (one-off price per fix in the report after the free diagnosis; depends on what is built; no long-term contracts); never a number
- Колко време отнема внедряването? — yes (canon: build usually up to 2 weeks)
- Какво става след внедряването / поддръжка? — yes (monthly support with a short report)
- Сигурни ли са данните / GDPR? — only „Работим по GDPR“
- Замества ли автоматизацията служителите? — answer within canon rule 7 (a tool; the client keeps control); avoid any claim beyond canon
- Какъв софтуер за автоматизация използвате? — NO (tools/vendors Tier 3) → owner item if asked
- Пример: колко време се спестява? — only owner's rough hours „на база типични случаи“ with that label; prefer no numbers

## CANDIDATE NEW SOURCES (max 3 new external facts; authoritative only)
- none found worth adding; search results were vendor blogs (ClickUp, beancount, Zapier) = NEW-WEAK, excluded. The page does not need an external fact.

## SIBLING PAGES (to avoid copied wording and term cannibalisation)
- / — ai автоматизация (do NOT target „ai автоматизация“ or „автоматизация“ as main term here; „автоматизация“ is a home-page secondary)
- /ai-asistent/ — ai асистент (chatbots/assistants belong there: link, do not develop)
- /seo-statii/ — seo копирайтинг
- /socialni-mrezhi/ — маркетинг в социалните мрежи
- /reklama/ — реклама в гугъл
- /seo-optimizacia/ — seo оптимизация
- /diagnostika/ — безплатна диагностика за бизнеса (link as the free diagnosis; do not use its main term verbatim as a heading)

## NOTES
- Owner checker copy (skriti-problemi.json) is informal „ти“ and contains turnaround phrasing „за минути“, „денонощно“ — canon says do not state turnaround times beyond canon; do not carry „за минути“.
- Business areas for grouping (from the checker groups): Клиенти и записвания (booking, reminders, waitlist, status messages); Оферти и продажби (offers form→PDF, offers from photos); Админ и документи (documents, invoices, contract templates, connected systems, listings once); Данни и решения (dashboard, AI meeting summary).
- Business types per capability (checker `t` field): booking — resto, salon, clinic, auto; calendar+reminders+waitlist — salon, clinic, resto; offers form→PDF — b2b, retail, auto, estate; offers from photos — auto, b2b; connected systems — shop, retail, b2b; documents — all; contract templates — b2b, estate; listings once — estate; dashboard — all; AI meeting summary — b2b; repair-status messages — auto.
- Port JSON `related` candidates: /ai-asistent/, /diagnostika/, /seo-statii/ (or /reklama/).
