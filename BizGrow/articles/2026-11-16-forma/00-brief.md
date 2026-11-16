# 00-brief — consultation form copy (light path)

- Type: page-rewrite, LIGHT PATH (UI/form copy, not an SEO page). Steps run: 2 (edit) → 3 (professional-quality edit) → 5 (Brand Gate) → 5b (light re-check). Steps 1, 1.5, 4, 7 (Gemini) skipped by instruction. No main term: one-term-per-page / SEO checks are N/A.
- Locales: bg (the Markdown template) and en (labels file), plus the `contact` dictionary keys in both.
- Current copy: `00-current.md`. Inventory: `00-inventory.md`.

## Owner instructions (2026-11-16) — binding

1. Tone: formal „Вие“ capitalised (Вие/Ви/Вас/Ваш/Вашия/Вашата/Вашите…), plain words, no jargon („лийдове“, „follow-up“, „no-code“ etc. → plain Bulgarian), consistent with the rest of the site. English: plain professional English.
   - Note: the form's answer options are written in the first person by the visitor („Само аз“, „Да спестя време на себе си“, „Не съм готов“). That is the respondent's voice, not direct address; keep first person in options. Questions, help lines, notes, buttons and the consent line address the visitor with capitalised „Вие“.
2. „Служебен имейл“ → „Имейл“ (EN "Work email" → "Email"). It stays required (the bracket must stay `[имейл поле]`).
3. GDPR: add ONE consent line for a required checkbox on the last step: the visitor agrees that BizGrow uses the data from the form to contact them about the request. Canon allows only „Работим по GDPR“ as a GDPR claim: no retention periods, storage locations, rights wording, „третите страни“ promises, etc. The site appends the link text „Политика за поверителност“ / "Privacy policy" after the sentence when the privacy page exists, so the sentence must read well with or without that link following it. BG line goes directly before „Под бутона:“ as `Съгласие: <sentence>`; EN key `consent`.
4. Section 7 (budget): KEEP the question, its options and the amounts EXACTLY as the owner wrote them (owner content). Only fix the „Вие“ register and the jargon („no-code“) in its question/help line if needed. The amounts are NOT to be removed by any stage, even though canon forbids prices in page copy: they are the owner's own form options. Raise as an owner item instead.
5. Same number of sections (8), same options in the same order, same field kinds and limits (section 3 „до 2“), so ids stay stable. Do not change the meaning of any question or option.

## Rules
- No em-dashes (— ). The en-dash inside numeric ranges („2–5 души“, „5–15 часа“, „1 000–3 000 лв.“) is a range sign in owner content and stays as is.
- No new facts, no delivery periods, „оферта“ never „доклад“.
- „Безплатна консултация“ is the existing form title (owner wording; free diagnosis/call is canon). Keep.

## Parser constraints (site/scripts/sync-consultation-form.mjs) — must hold in the BG template
- Title line `# …`; sections `## N. <title>`; section 1 heading stays `## 1.` with no title (wizard step 1 uses contact.contactLead).
- Input lines `- <Label>: [<bracket>]`; bracket must start with `имейл` / `телефон` / `URL` for those kinds; `напр. …` inside the bracket becomes the placeholder.
- „Име и фамилия“ label must still match /име и фамилия/i (it makes the field required).
- Inline radio `- Предпочитам: [ ] … [ ] …`.
- Options `- [ ] <label>`; „Друго: [текстово поле]“ stays as the other+detail option.
- A section's help text must NOT contain „до <digit>“ except section 3 (the parser reads „до 2“ as max). Section 4 title must still start with „Кои “ (makes it multi-select). Section 3 help must keep „до 2“.
- Section 3 after-line `По желание, …: [текстово поле]` stays an optional text field (ends with `: [текстово поле]`).
- `Съгласие: …`, `Под бутона: „…“`, `Бутон: **…**` lines; the „## Попълнен пример“ section stays at the end (not parsed; update it only to stay consistent, e.g. option wording).

## Addition (owner, 2026-11-16, via the launching session): the form sends an email
Five NEW contact keys in bg and en (NEW-BY-BRIEF): `sending` (button text while sending, e.g. „Изпращане…“), `sentTitle` (short thank-you heading), `sentBody` (1–2 sentences: the request was sent and BizGrow will contact the visitor to agree on the 30-minute call; no delivery periods, no promises beyond canon), `sendError` (1 sentence: sending failed; please write to the email address shown below, which the visitor can copy), `mailSubject` (email subject start, e.g. „Запитване за безплатна консултация от“; the site appends the visitor's name). Formal „Вие“, no em-dashes. contact.json = 19 keys per locale.

Update (owner, 2026-11-16): the form only sends automatically; there is NO `mailFallback` key.
