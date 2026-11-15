# 00-inventory — /en/ (en) en-home

Source: `00-current.md` (biz-grow @ feature/seo-improvements, 528ad25, `site/src/i18n/dictionaries/en.ts`).
Every item must survive every editing stage with the same meaning (reworded allowed), unless listed
under REMOVE-BY-BRIEF (owner's session 2026-11-15, see `00-brief.md`). Pair: the finished Bulgarian
page `articles/2026-11-15-home/content/home.md` + `home.port.json` (structure, section ids, facts,
FAQ questions and changes are mirrored).

## CTAs (6)
- C1 nav.cta "Book a call" → {{BOOKING_URL}}
- C2 hero.primary "Free diagnosis" → {{BOOKING_URL}} (stays booking)
- C3 hero.secondary "Explore services" → #services
- C4 cta.button "Book a free diagnosis" → {{BOOKING_URL}} (#audit)
- C5 contact.book "Book a video call now" → {{BOOKING_URL}}
- C6 contact.submit "Submit" (form → mailto {{EMAIL}}) + contact.emailBefore "Send us an email at"

## Tokens (2)
- T1 {{BOOKING_URL}} (C1, C2, C4, C5)
- T2 {{EMAIL}} (contact block, form, footer)

## Anchors (8)
- #hero, #losses, #services, #process, #results, #reasons, #audit, #contact (nav: #services, #process, #contact; footer same). #top on wrapper.
- New by brief: #faq (as on the Bulgarian pair).

## Canon facts (9)
- F1 Free diagnosis — hero.primary, a11y.results, overlayLabel, page.diagnosis, cta
- F2 30-minute conversation — process step 1
- F3 Report with prioritised solutions and clear prices within 48 hours — process step 2
- F4 Build of the specific AI solution, usually within 2 weeks — process step 2
- F5 Monitoring/improvement + short monthly report — process step 3 ("A transparent report every month")
- F6 One-time price ("A clear one-time price") — process step 2 title
- F7 "We work under GDPR" — reasons
- F8 "No long-term contracts", "Transparent prices", "A result before a large investment" — reasons
- F9 The diagnosis commits you to nothing (metrics "0 obligation"; cta.body "We show you exactly what we can fix and what it will cost.")
- (also) footer.descriptor "We find where the business loses time and fix it with AI."

## Numbers (8)
- N1 metrics "8 short questions" — REMOVE-BY-BRIEF
- N2 metrics "2 min / to fill in / 2 minutes" — REMOVE-BY-BRIEF
- N3 metrics "0 obligation" — keep
- N4 30-minute — keep; N5 48 hours — keep; N6 usually within 2 weeks — keep
- N7 results "24/7", "about 10 hours less manual work a week" (restaurant) — inside labelled hypothetical example; owner confirm (as on bg)
- N8 results "80%" (online shop) — inside labelled hypothetical example; owner confirm (as on bg)

## Labels (2)
- L1 results.note "Example scenarios from our method, not figures from specific clients." — must stay in #results
- L2 "in days, not months" (meta.description, ogTitle/ogDescription, hero.body, overlayUnit) — not canon; the bg pair replaced it with the canon "usually within 2 weeks" and raised an owner item; mirror that.

## Example rows (3, hypothetical)
- E1 Restaurant / Nobody picks up at peak hours. / Bookings 24/7, about 10 hours less manual work a week.
- E2 Online shop / Questions about deliveries sit unanswered for hours. / 80% of the repeated questions answered in seconds.
- E3 Dental clinic / Missed calls and appointments moved around. / Online booking at any time.

## Losses (5)
- missed calls and messages after hours; hours writing quotes and invoices by hand; no timely reply on Messenger/Instagram/WhatsApp; no time for content and social networks while competitors grow; not knowing which business numbers matter

## Reasons (4)
- We work under GDPR; No long-term contracts; Transparent prices; A result before a large investment

## FAQ (0)
- The current page has no FAQ. Brief adds one, mirroring the 7 questions of the bg pair.

## UI strings to keep (a11y, page, contact.fields, footer)
- a11y.* (10 keys), page.* (4 keys), contact.fields name/email/description ("Names" may be corrected to "Name"), contact.mailSubject, footer.* (6 keys), hero.imageSrc "/bizgrow-banner.webp", hero.imageAlt (contains an em-dash → reword), meta.ogLocale "en_US".

## REMOVE-BY-BRIEF (owner's session 2026-11-15, mirrored from the bg pair)
- N1, N2 and process step 1 "You fill in a free 2-minute AI diagnosis of the site" → the free diagnosis + 30-minute conversation (no questionnaire, and NO link to /diagnostika/: Bulgarian-only page).
- Services: the four-card set incl. "Custom solutions" → six cards mirroring the bg pair, WITHOUT href (no English service pages).
- losses.link: omitted on /en/ (the bg link goes to the Bulgarian-only /diagnostika/).
- #ads section — already removed upstream.
