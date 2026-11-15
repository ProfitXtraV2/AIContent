# 01-synthesis — /en/ (en) en-home — 2026-11-15

Inputs read: `pipeline/agents/synthesis.md`, `pipeline/prompts/step-1-synthesis.md`, `pipeline/markets/en/author.md`, `pipeline/markets/bg/author.md` (canon + B2B claim rules), `pipeline/reference/site-rules.md`, `pipeline/reference/verification-policy.md`, `00-brief.md`, `00-current.md`, `00-inventory.md`, the finished Bulgarian pair `articles/2026-11-15-home/content/home.md` + `home.port.json`, `BizGrow/conversion-links.md`.

## SYNTHESIS REPORT

Page: /en/ | Locale: en | Type: page-rewrite | Main term: ai automation for small business (secondary: ai automation agency, business automation) | Intent: commercial with an informational layer. An English-speaking small-business owner wants to know first what can be automated, who builds it, how the work goes, what it costs (how the price is formed), and how to start without risk.

Current facts kept: 10 (F1 to F9 + footer descriptor) | Unconfirmed current facts: 2 (“in days, not months”, the three example rows with their figures) | New sourced facts: 0 (≤3) | Excluded weak claims: 4 | OWNER CONFIRM: 14

Buyer questions answerable (canon): what a small business can automate; how the price is formed (one-time price per fix, in the report within 48 hours, no number); where to start (free diagnosis + 30-minute call, no obligation); how long the build takes (usually within 2 weeks); whether AI replaces staff (client approves content, a real marketing specialist runs ads, the chat assistant collects the contact when it cannot help); whether it suits my industry (canon audience list); long-term contract and support (none; monthly short report).

Not answerable (need the owner): concrete prices or ranges; ROI or hours saved for a real business; where data is stored and which AI models or tools are used; GDPR detail beyond “We work under GDPR”; whether the team works in English with English-speaking clients and serves businesses outside Bulgaria (relevant to an `/en/` audience; not stated anywhere, so the page does not claim it); response times; team, legal data, address, phone.

Excluded claims (with why):
1. ROI / “save X hours” / “cut costs by X%” figures from English vendor and agency blogs (dev.to guides, intuz.com, petronellatech.com): NEW-WEAK, vendor marketing, not authoritative; no invented numbers.
2. “AI automation costs from $X per month” style price ranges seen in search results: NEW-WEAK and banned (no prices).
3. “24/7 support” / instant response promises on agency pages: not canon; a guarantee of response time.
4. Claims of named tools or platforms (Zapier, Make, n8n, OpenAI) as “what we use”: Tier C (vendors and models used), never stated.

Localisation notes:
- English-speaking readers in Bulgaria (expats, foreign-owned businesses) read the same canon; nothing in the canon is Bulgaria-specific except the audience, which transfers unchanged.
- Spelling follows the current `en.ts` (British: “prioritised”, “optimisation”) while `ogLocale` stays `en_US` as on the current page. Consistency of spelling is a wording choice for Step 4/5, not a fact.
- Plain words first, jargon explained once: chatbot (“an assistant in the chat”), dashboard (“one screen with your key figures”), SEO (“search engine optimisation, how pages are prepared for Google searches”), B2B (“businesses that sell to other businesses”).
- “in days, not months” (current hero.body, overlayUnit, meta, OG) is replaced by the canon “usually within 2 weeks”, mirroring the bg pair.
- No link to any Bulgarian page: the bg `losses.link`, the bg service `href`s, and the `/diagnostika/` links in process step 1 and FAQ 3 are all dropped; the free diagnosis is reached through the booking CTAs (`{{BOOKING_URL}}`). The bg FAQ 6 line “In the diagnosis you can see examples for your type of business” (it refers to the bg checker page) is rephrased to a canon statement about the diagnosis call and report.
- Main term placement: title, H1 (“AI automation for small businesses.”), first sentence of the hero body, and one H2 (#services). Secondary “business automation” used once in FAQ 1; “ai automation agency” not forced into the copy (the page says what BizGrow does; the keyword may go into og/meta at Step 4 if it fits naturally).
- “related” (3 sibling paths) is not added: the home `Dictionary` type has no `related` key and every sibling is Bulgarian-only. Same handling as the bg pair; reported to the human.

Sources: none new. All facts are Tier A (canon or current page confirmed by canon) or labelled examples already on the page.

### FACT INVENTORY

| # | Claim | Tag | Where in draft |
|---|---|---|---|
| F1 | Free diagnosis | CURRENT | hero CTA, overlayLabel, a11y.results, page.diagnosis, #process 1, #audit, FAQ 3 |
| F2 | 30-minute call | CURRENT | hero body, metric 1, #process 1, FAQ 3 |
| F3 | Report with prioritised fixes and clear one-time prices within 48 hours | CURRENT | metric 2, meta, #process 2, FAQ 2 |
| F4 | Build of the specific AI solution, usually within 2 weeks | CURRENT | hero body, overlayUnit, meta, #process 2, FAQ 4 |
| F5 | Monitoring/improvement + short monthly report | CURRENT | #process 3, FAQ 7 |
| F6 | One-time price per fix, depends on what is built | CURRENT (canon PRICES) | #process 2 title, FAQ 2 |
| F7 | “We work under GDPR” | CURRENT | #reasons |
| F8 | No long-term contracts; Transparent prices; A result before a large investment | CURRENT | #reasons, FAQ 2, FAQ 7 |
| F9 | The diagnosis commits you to nothing; “we show you exactly what we can fix and what it will cost” | CURRENT | metric 3, #audit, FAQ 3 |
| F10 | “We find where your business loses time and fix it with AI.” | CURRENT | footer.descriptor |
| S1 | Chat assistant on Messenger, Instagram, WhatsApp; collects the contact when it cannot help | CURRENT (canon services + skriti-problemi) | #services card 1, FAQ 5 |
| S2 | Online booking with reminders; quotes form → PDF; documents and invoices; connecting existing programs so data fills itself in; dashboard | CURRENT (canon) | #services card 2, FAQ 1 |
| S3 | Own content tool writes SEO articles for the client's industry and city; published after approval | CURRENT (canon) | #services card 3, FAQ 5 |
| S4 | Social posts (text + image) on a schedule after approval; branded visuals and ad materials every month | CURRENT (canon) | #services card 4, FAQ 5 |
| S5 | A real marketing specialist plans, runs and tracks ads and reports with numbers | CURRENT (canon); platform names = OWNER CONFIRM | #services card 5, FAQ 5 |
| S6 | SEO optimisation: technical SEO, on-page, links | CURRENT (canon) | #services card 6 |
| A1 | Audience list (restaurants and cafés … B2B) | CURRENT (canon) | FAQ 6 |
| U1 | “in days, not months” | CURRENT-UNCONFIRMED → replaced by canon wording | owner item |
| E1–E3 | Restaurant / Online shop / Dental clinic rows incl. “24/7”, “about 10 hours”, “80%” | EXAMPLE | #results, label kept |
| R1 | “8 short questions”, “2 min to fill in”, questionnaire in step 1 | REMOVE-BY-BRIEF | removed |

## THE DRAFT

Page: /en/ | Locale: en | Type: page-rewrite | Main term: ai automation for small business

Front-matter proposals (for Step 4):
- title: “AI automation for small business | BizGrow” (42 chars) [OWNER CONFIRM: title change from “BizGrow — Find where the business loses time”, mirroring the bg pair]
- meta_description: “AI automation for small business: a free diagnosis, a report with prioritised fixes and clear prices within 48 hours, and a build usually within 2 weeks.” (153 chars)
- ogTitle: “BizGrow: AI automation for small businesses”
- ogDescription: “A free diagnosis with no obligation. A report with clear one-time prices within 48 hours, and the build of the fixes usually within 2 weeks.” (140 chars)
- ogLocale: “en_US” (unchanged)

UI strings kept unchanged in meaning: nav links “Services” / “Process” / “Contact us” (#services, #process, #contact), nav.cta “Book a call” → `{{BOOKING_URL}}`; a11y.* (10 keys), page.* (4 keys), footer.* (descriptor reworded to “We find where your business loses time and fix it with AI.”), contact.mailSubject “BizGrow message from”, hero.imageSrc “/bizgrow-banner.webp”.

hero.imageAlt: “BizGrow: AI and automation for small businesses. The image reads: integrate AI, automate workflows, save time and costs, grow your business.” [OWNER CONFIRM: imageAlt reworded without the em-dash; it describes the English text baked into the banner]

hero.overlayLabel: “Free diagnosis” | hero.overlayUnit: “usually within 2 weeks” [OWNER CONFIRM: “in days, not months” (hero.body, overlayUnit, meta, OG) is not in the 2026-11-15 canon and is replaced by the canon “usually within 2 weeks”; confirm, or confirm the old wording to restore it]

## AI automation for small businesses. Less busywork, more business. {#hero}

[OWNER CONFIRM: H1 change from “Less busywork. / More business.” to hero.line1 “AI automation for small businesses.” + hero.line2 “Less busywork, more business.”, mirroring the bg pair]

BizGrow provides AI automation for small business: we find where your business loses time, choose the fixes that are worth building and build them for you. We start with a free diagnosis and a 30-minute call, and the build usually takes up to 2 weeks.

[Free diagnosis]({{BOOKING_URL}})

[Explore services](#services)

- **30 min** diagnosis call (label: “30 minutes”)
- **48 h** to the report with prices (label: “48 hours”)
- **0** obligation

[OWNER CONFIRM: hero figures “8 short questions” and “2 min to fill in” removed (the questionnaire no longer exists) and replaced by the canon figures 30 min / 48 h / 0 obligation, as on the bg pair]

## Where you lose customers and hours every day {#losses}

- Missed calls and messages after working hours
- Hours lost writing quotes and invoices by hand
- Messages on Messenger, Instagram or WhatsApp that go without a timely reply
- No time for content and social media while competitors grow
- Not knowing which numbers in your business actually matter

[OWNER CONFIRM: no `losses.link` on /en/; the bg link points to the Bulgarian-only /diagnostika/. Heading reworded from “Every day you lose customers and hours” to mirror the bg heading]

## AI automation, content and advertising for small businesses {#services}

[OWNER CONFIRM: the four current cards (Automations, SEO copywriting, Creatives, Custom solutions) are replaced by six cards mirroring the bg pair, with NO href (no English service pages); “Custom solutions” is no longer a card. Confirm the set, titles and texts]

- **AI assistant and chatbot.** (icon: brain) A chatbot is an assistant in the chat that answers repeated questions on Messenger, Instagram and WhatsApp. When it cannot help, it collects the customer's contact details.
- **Automations.** (icon: loop) We build online booking with reminders, quotes that go from a filled-in form to a finished PDF, and automatic handling of documents and invoices. We also connect the programs you already use and set up a dashboard, one screen with your key figures.
- **SEO articles and copy.** (icon: spark) Our own content tool writes articles about your industry and city, prepared for Google searches (SEO, search engine optimisation). Each article is published only after you approve it.
- **Social media and creatives.** (icon: spark) Posts with text and an image go out on a schedule once you approve them. Every month we also prepare branded visuals and advertising materials.
- **Google and Facebook ads.** (icon: loop) A real marketing specialist plans, runs and tracks your ads, and reports the results to you with concrete numbers. [OWNER CONFIRM: platform names “Google and Facebook” come from the keyword-map H1 of /reklama/ (canon says only advertising and marketing); no monthly cadence for the report is stated; confirm the platforms and whether the specialist reports monthly]
- **SEO optimisation.** (icon: brain) We work on your website's technical SEO (how the site is set up for Google search), on the optimisation of individual pages and on the links that point to the site.

## Three steps to a working solution {#process}

The work goes through three steps, from the first call to support for the finished solution.

1. **Diagnosis: Where time and money leak.** We start with a free diagnosis and a 30-minute call. You describe the problems you see in your business, and together we find exactly where it loses time and money. [OWNER CONFIRM: step 1 no longer mentions the 2-minute questionnaire and, unlike bg, has no link to /diagnostika/]
2. **Build: A clear one-time price.** Within 48 hours you receive a report with prioritised fixes and clear one-time prices. We then build the specific AI solution, usually within 2 weeks.
3. **Support: A transparent report every month.** After launch we monitor the solution and improve it. Every month you receive a short report on the work done.

## What the result can look like {#results}

Example scenarios from our method, not figures from specific clients.

| Business | Problem | Result |
|---|---|---|
| Restaurant | Nobody picks up at peak hours. | Bookings 24/7, about 10 hours less manual work a week. |
| Online shop | Questions about deliveries sit unanswered for hours. | 80% of the repeated questions answered in seconds. |
| Dental clinic | Missed calls and appointments moved around. | Online booking at any time. |

[OWNER CONFIRM: example rows kept verbatim with the label; confirm the rows and figures (“24/7”, “about 10 hours”, “80%”) or supply replacements. Heading “What the result looks like” → “What the result can look like”, as on bg]

## The little “extra” that changes the result {#reasons}

We explain every solution in plain language and build only AI tools that solve a specific problem in your business.

- We work under GDPR
- No long-term contracts
- Transparent prices
- A result before a large investment

[OWNER CONFIRM: reasons.lead rewritten (old: “No jargon, and no solutions “just in case”. Only tools that work, shaped to your business.”), mirroring the bg lead]

## The first step is free {#audit}

The diagnosis commits you to nothing. We show you exactly what we can fix and what it will cost.

[Book a free diagnosis]({{BOOKING_URL}})

## Frequently asked questions {#faq}

[OWNER CONFIRM: new FAQ section (#faq, 7 questions mirroring the bg FAQ) between #audit and #contact, answered only from the canon; no GDPR/data question added because the canon allows only “We work under GDPR”]

(Q/A in the PROPOSED FAQ below.)

## Contact us {#contact}

[Book a video call now]({{BOOKING_URL}})

Send us an email at {{EMAIL}}

- Name
- Email
- Description

[Submit](mailto:{{EMAIL}})

[OWNER CONFIRM: contact.fields.name “Names” corrected to “Name”]

## PROPOSED FAQ

**What can a small business automate?**
The most common candidates are answers to repeated questions on Messenger, Instagram and WhatsApp, online booking with reminders, quotes, documents and invoices. Business automation also covers connecting the programs you already use so that data fills itself in, and a dashboard with your key figures in one place.

**How much does it cost to build a solution?**
Each solution has a one-time price that depends on what exactly is built. You find the price in the report you receive within 48 hours of the diagnosis, and we work without long-term contracts.

**Where do I start if I don't know what to automate?**
Start with the free diagnosis: book a 30-minute call and tell us about the problems you see in your business. The diagnosis commits you to nothing.

**How long does the build take?**
Once you have the report, we build the specific solution, usually within 2 weeks.

**Will AI replace the people on my team?**
AI takes over repeated tasks, and you stay in control. Articles and posts go out only after you approve them, and your advertising is run by a real marketing specialist. When the chat assistant cannot help, it collects the customer's contact details.

**Is this suitable for my industry?**
We work with small businesses: restaurants and cafés, hotels and guest houses, salons, online shops, retail shops and showrooms, clinics and practices, car services and tradespeople, real estate and B2B companies (businesses that sell to other businesses). After the diagnosis, the report shows which fixes make sense for your type of business. [OWNER CONFIRM: last sentence rephrased from the bg “In the diagnosis you can see examples for your type of business”, which refers to the Bulgarian-only checker page]

**Do I have to sign a long-term contract?**
No, we work without long-term contracts. During support we monitor the solution, and every month you receive a short report on the work done.

## INVENTORY CHECK

- C1 nav.cta “Book a call” → `{{BOOKING_URL}}`: UI strings line.
- C2 hero.primary “Free diagnosis” → `{{BOOKING_URL}}`: #hero.
- C3 hero.secondary “Explore services” → #services: #hero.
- C4 cta.button “Book a free diagnosis” → `{{BOOKING_URL}}`: #audit.
- C5 contact.book “Book a video call now” → `{{BOOKING_URL}}`: #contact.
- C6 contact.submit “Submit” + emailBefore “Send us an email at” + `{{EMAIL}}`: #contact.
- T1 `{{BOOKING_URL}}` ×4 (C1, C2, C4, C5); T2 `{{EMAIL}}`: #contact (+ footer, form).
- Anchors: #hero, #losses, #services, #process, #results, #reasons, #audit, #faq (new), #contact, all present; nav/footer #services #process #contact unchanged.
- F1–F10: see FACT INVENTORY table (all placed).
- N3 “0 obligation”: hero metric 3; N4 30-minute, N5 48 hours, N6 usually within 2 weeks: hero, #process, FAQ; N7/N8 inside labelled #results rows. N1/N2 REMOVE-BY-BRIEF.
- L1 example label: #results, first line under the heading. L2 “in days, not months”: replaced by canon wording, owner item.
- E1–E3: #results table, verbatim.
- Losses (5): #losses, all five reworded only.
- Reasons (4): #reasons, verbatim.
- UI strings (a11y, page, fields, footer, imageSrc, imageAlt, ogLocale): front-matter / UI lines.

## FLAGS

- [OWNER CONFIRM] ×14 inline: title; imageAlt; “in days, not months” → “usually within 2 weeks”; H1; hero figures; no losses.link + losses heading; six service cards without href; ad platforms and report cadence; process step 1 (no questionnaire, no link); example rows + results heading; reasons.lead rewrite; new FAQ section; FAQ 6 last sentence; “Names” → “Name”. Step 6 may merge title+H1 into one owner item as on the bg pair.
- [VERIFY]: none.
- [DATA NEEDED]: none in the text (prices, ROI, data location, models, English-language service scope listed under “Not answerable”).
- [LINK NEEDED]: none.

CANON ADDITIONS: none.

## SELF-CHECK

Em-dashes 0 in copy (only quoted as the old wording to be removed); hype words 0; AI vocabulary 0; jargon explained (chatbot, dashboard, SEO, B2B; PDF as a brand-level term); invented facts or numbers 0; guarantee wording 0; GDPR only “We work under GDPR”; prices/offers/testimonials 0; “free” only for the diagnosis; example label present in #results; CTA wording approved (“Book a call”, “Free diagnosis”, “Explore services”, “Book a free diagnosis”, “Book a video call now”, “Submit”), one booking CTA per section; no link to any Bulgarian page; section ids match the bg pair; main term in title, H1, first sentence and #services H2.
