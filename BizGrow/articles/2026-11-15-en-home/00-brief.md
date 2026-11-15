MARKET: en — English-speaking owners (locale en at `/en/`)
LOCALE: en   PAIR: home (/, finished 2026-11-15: articles/2026-11-15-home/content/home.md + home.port.json)
CONTENT TYPE: page-rewrite (keyword-map row status `planned`, owner's session 2026-11-15, "page-rewrite after `/`")
PAGE: /en/
SLUG: en-home
MAIN TERM (BizGrow/keyword-map.md): ai automation for small business
SECONDARY: ai automation agency, business automation
AHREFS: ai automation for small business | not measured | KD not measured | bg | — (English demand in Bulgaria negligible per NICHE-ANALYSIS-2026-11-15 §English; write for clarity, not keyword density)
H1: current "Less busywork. / More business." ; keyword-map proposal "AI automation for small businesses"
SOURCE OF CURRENT PAGE: desislavamit/biz-grow @ feature/seo-improvements : site/src/i18n/dictionaries/en.ts + HomePage.tsx, Sections.tsx, Contact.tsx, HeroVisual.tsx, commit 528ad25c3b7be5a9a48d38740ab1bc955512d2a9

## CURRENT PAGE + INVENTORY
- 00-current.md written: yes
- 00-inventory.md written: yes — 6 CTAs, 2 tokens, 8 anchors (+ #faq new), 9 canon facts, 8 numbers, 2 labels (1 example label), 3 example rows, 0 FAQs

## SITE RULES RE-READ THIS RUN
- dictionaries / types.ts / config.ts: same as reference/site-rules.md copy. Differences: types.ts on the branch already has `losses.link?`, `services.items[].href?` and top-level `faq?`; en.ts does not use them yet. The English site has no content pages (app/(en)/ = home only). Booking URL and email unchanged (tokens).

## OWNER INSTRUCTIONS FOR THIS PAGE (owner's session 2026-11-15, via the orchestrator)
- Mirror the finished Bulgarian page: same structure, section ids, facts, FAQ questions and changes, written natively in plain professional English (not a literal translation). A fact not on the bg page is not on the en page.
- H1 (hero.line1 + hero.line2) carries the main term: line1 ≈ "AI automation for small businesses." + line2 slogan ("Less busywork, more business."). Title/meta aimed at the main term.
- Services: SIX cards mirroring the bg cards (AI assistant and chatbot; Automations; SEO articles and copy; Social media and creatives; Google and Facebook ads; SEO optimisation), `icon` ∈ spark | loop | brain, NO `href` (no English service pages; the Bulgarian pages are Bulgarian-only).
- Losses: NO `losses.link` (the bg link points to the Bulgarian-only /diagnostika/).
- No link to any Bulgarian page anywhere in the en copy (process step 1 and FAQ "where do I start" link /diagnostika/ on bg: on en they describe the free diagnosis / 30-minute call without a link; the free diagnosis CTA is the booking link). The bg FAQ "suitable for my industry" ends with "In the diagnosis you can see examples for your type of business" (refers to the bg checker page): rephrase so it does not point to a page that does not exist in English.
- Hero primary CTA stays booking.
- Hero figures: 30 min / 48 h / 0 obligation (canon), replacing "8 short questions" / "2 min to fill in" (REMOVE-BY-BRIEF). No questionnaire.
- Add a FAQ section (#faq, new key `faq`, 7 questions mirroring the bg FAQ) between #audit and #contact.
- "in days, not months" → canon "usually within 2 weeks" (owner item, as on bg).
- Keep every other section, anchor and the hypothetical label on #results; anchors #services, #process, #contact, #faq must work.
- Deliverable also includes `content/en-home.port.json` (exact `en` shape + faq; services 6 items without href; no losses.link; keep a11y and page).

## BUYER QUESTIONS (WebSearch bg „AI автоматизация за малък бизнес въпроси“ and en "AI automation for small business FAQ"; Ahrefs serp-ai_автоматизация.json is empty; no English SERP data exists for BG)
- What can a small business automate? — yes (canon: messages, booking + reminders, quotes, documents, invoices, connecting existing programs, dashboard)
- What does AI automation cost? — yes at canon level only (one-time price per solution, in the report within 48 h; no number)
- Where do I start / audit the processes first? — yes (free diagnosis, 30-min conversation, report in 48 h)
- How long does it take to build? — yes ("usually within 2 weeks")
- Does AI replace staff / is there human control? — yes (client approves content; a real marketing specialist runs ads; the chat assistant collects the contact when it cannot help)
- What about data / GDPR? — only "We work under GDPR" (no FAQ, as on bg)
- Long-term contract / ongoing maintenance? — yes (no long-term contracts; support with short monthly report)
- Is it right for my industry? — yes (canon audience list)
- ROI / how much will I save? — no (no invented numbers; vendor-blog figures are not authoritative)

## CANDIDATE NEW SOURCES (max 3 new external facts; authoritative only)
- none (search results are vendor blogs; not authoritative). 0 new facts planned, as on the bg pair.

## COMPETITOR PAGES (intent only)
- English results (dev.to guides, vendor/agency pages such as intuz.com, petronellatech.com) are explainer + service intent: what can be automated, cost, where to start. Not facts.

## SIBLING PAGES (avoid copied wording and term cannibalisation)
- / — ai автоматизация (bg pair; mirror, do not link editorially)
- /ai-asistent/ — ai асистент
- /avtomatizacii/ — автоматизация на бизнес процеси
- /seo-statii/ — seo копирайтинг
- /socialni-mrezhi/ — маркетинг в социалните мрежи
- /reklama/ — реклама в гугъл
- /seo-optimizacia/ — seo оптимизация
- /diagnostika/ — безплатна диагностика за бизнеса
All siblings are Bulgarian-only; the en page does not link them (owner's instruction for this run).

## NOTES
- No earlier owner items for this page (first run). Owner items on the bg pair (H1, "in days, not months", six cards, ads platforms/monthly cadence, example rows, hero figures, FAQ, imageAlt) apply here too and are mirrored.
- The `en` dictionary has no `related` key (home `Dictionary` type, not `ContentPage`); a "related = 3 sibling paths" rule from the orchestrator conflicts with "exact shape of en" and "no links to Bulgarian pages": not added, reported to the human (same handling as the bg pair).
- hero.imageSrc "/bizgrow-banner.webp" has English baked-in text; imageAlt describes it; keep the meaning without the em-dash.
