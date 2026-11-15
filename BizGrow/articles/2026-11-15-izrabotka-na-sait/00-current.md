# 00-current — /izrabotka-na-sait/ (new page)

Source: desislavamit/biz-grow @ feature/seo-improvements (local worktree ~/Work/biz-grow-seo), commit a1ccf8fe827ac1fd41ca48d9a22030b757861922.

There is NO current copy for /izrabotka-na-sait/: the page does not exist yet
(`site/src/content/pages/bg/` holds ai-asistent, avtomatizacii, diagnostika, reklama, seo-optimizacia, seo-statii, socialni-mrezhi; no izrabotka-na-sait). The home services list (bg.ts `services.items`) has no website-building card.

Site context the new page sits in (verbatim, for reference only, not inventory):
- Home process lead (bg.ts `process.lead`): „Работата минава през три стъпки, от първия разговор до поддръжката на готовото решение.“
- Home process step 1 body: „Започвате от [безплатната диагностика](/diagnostika/), където отбелязвате проблемите, които познавате от своя бизнес. След това в 30-минутен разговор уточняваме къде точно бизнесът Ви губи време и пари.“
- Owner checker (skriti-problemi.json), site-related pains („ти“-era wording, intent only): „Сайтът ти не се е променял от месеци — и Google те подминава за сметка на конкуренцията.“ (fix: SEO articles tool → /seo-statii/); „Менюто и цените се смениха — но в сайта, Google и Facebook стои старото.“ (fix: „Обновяване от едно място“).
- Template `ContentPageView.tsx` renders: breadcrumb (label), eyebrow, H1, lead, booking button „Запазете час“ ({{BOOKING_URL}} via BookingLink), button „Безплатна диагностика“ → /diagnostika/, sections, FAQ, related, CTA band.
- `site/src/content/types.ts` (this commit): strings accept `**bold**`, `[label](href)` with href a root path, an #anchor, `{{BOOKING_URL}}` or `mailto:{{EMAIL}}`; a bare `{{EMAIL}}` prints the address as a mailto link. PageSection = {id, title, paragraphs, bullets?, steps?, closing?}.
