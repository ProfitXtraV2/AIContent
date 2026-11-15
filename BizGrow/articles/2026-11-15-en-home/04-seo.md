# 04-seo: /en/ (en) en-home

```
SEO AUDIT: /en/ (en)
Main term: ai automation for small business | Intent: commercial + informational (explainer + service SERP per brief; not measured in Ahrefs, English demand in Bulgaria negligible, so optimised for clarity, not density) | Placement (before and after edits): title Y, H1 Y (plural variant), first 100 words Y, H2 Y
Relevance score: 91/100 (alignment 24/25 | entities 32/35 | questions 22/25 | on-page 13/15)
```

### Placement check (after edits)
| slot | text | exact uses |
|---|---|---|
| title | “AI automation for small business \| BizGrow” (42 chars incl. suffix, counted by script) | 1 |
| H1 | hero.line1 “AI automation for small businesses.” (natural plural variant) + hero.line2 “Less busywork, more business.” | 1 (variant) |
| first 100 words | hero.body sentence 1 “BizGrow provides AI automation for small business: …” (also the page's first sentence, stating the offer) | 1 |
| one H2 | #services “AI automation for small business, content and advertising in one place” | 1 |
| meta description | 153 chars (counted by script), starts with the main term | 1 |
| ogTitle | “BizGrow: AI automation for small businesses” (plural variant) | 1 (variant) |
| rest of body, FAQ, other H2s | 0 exact uses (variants only: “automate”, “Automations”, “AI solution”, “AI tools”) | 0 |

No over-placement: the exact phrase appears once each in title, hero.body and one H2; the H1 and ogTitle carry the plural. No de-flooding needed.

### ONE TERM PER PAGE (sibling main terms)
- All sibling rows in `keyword-map.md` are Bulgarian terms (ai асистент, автоматизация на бизнес процеси, seo копирайтинг, маркетинг в социалните мрежи, реклама в гугъл, seo оптимизация, безплатна диагностика за бизнеса); none can be targeted by English copy. English equivalents appear only as card titles describing the service (“AI assistant and chatbot”, “Automations”, “SEO optimisation”), with no href and no repetition, so nothing is targeted.
- The bg pair `/` (ai автоматизация) is mirrored, not linked editorially (conversion-links rule).
- Verdict: no sibling main term targeted.

### ENTITY COVERAGE
- PRESENT: tasks automated (answers to repeated questions, online booking with reminders, quotes to PDF, documents, invoices, connected programs, dashboard); channels Messenger, Instagram, WhatsApp; Google, Facebook; process (free diagnosis, 30-minute call, report with prioritised fixes and one-time prices within 48 hours, build usually within 2 weeks, monitoring + short monthly report); client control (articles and posts only after approval, real marketing specialist, chat assistant collects contact details); GDPR in the owner's wording (“We work under GDPR”); audience list (FAQ 6); no long-term contracts; transparent prices; jargon explained (chatbot, dashboard, SEO, technical SEO, B2B).
- MISSING (canon-coverable): none beyond the bg pair; the English page must not carry facts the bg page lacks.
- MISSING (not added): English-language service scope / clients outside Bulgaria (not canon; FLAG 18).
- ORPHANED: none.

### UNANSWERED BUYER QUESTIONS
- “What about data / GDPR?”: canon answer is only “We work under GDPR”, already in #reasons; not added as FAQ, mirroring the bg pair (owner option).
- “ROI / how much will I save?”: no canon numbers; left to the labelled #results examples. Not added.
- All other brief buyer questions answered by FAQ 1-7 (price answered without a number: one-time price in the report within 48 hours).

### DEFECTS
- #services card 1 “an assistant in the chat” slightly unidiomatic (Step 3 moderate) → “a chat assistant”. Body and PORT KEYS services.items[1] edited identically.
- meta.ogDescription “the build of the fixes” nominal (Step 3 moderate) → “the fixes built”; 133 chars.
- Body-link rule: no contextual links to other pages possible (see LINKS). Not a defect to fix in copy; noted for the human.
- Script check: em-dashes 0, banned/hype terms 0, prices/offers/testimonials 0, “free” only about the diagnosis, no guarantee wording.

### LINKS TO ADD
- None. Owner instruction for this run: NO links to Bulgarian pages (no service hrefs, no losses.link, no /diagnostika/). The 1-3 body-link rule is therefore met only with same-page anchors: hero.secondary “Explore services” → #services, plus nav → #services, #process, #contact. #faq and #contact remain reachable via the page. No inline `[label](#anchor)` links were added to body strings, because the home dictionary fields render as plain text on biz-grow main (`site/src/components/Sections.tsx`), so a Markdown link would print literally. Present tokens: {{BOOKING_URL}} ×4 (nav, hero, #audit, #contact), {{EMAIL}} (contact line, form mailto).

### FAQ CANDIDATES
- 7 kept from 03 (brief: 7, mirroring bg). No FAQ question repeats a body heading word for word. Answers 1-3 sentences, canon-backed; FAQ 6 sentence 1 is a long list lead-in (accepted).

### SECONDARY KEYWORDS USED
- business automation: yes, once (FAQ 1 answer, “Business automation also covers connecting the programs you already use…”); variants “Automations” (card), “automate” (FAQ 1 question).
- ai automation agency: not used. BizGrow is described in the canon as a consultancy, not an agency; using “agency” would be a new self-description, and forcing it adds nothing for a page with negligible English demand (same decision as „ai агенция“ on the bg pair).

### SEO EDITS (5-line change summary)
1. #services card 1 body: “A chatbot is an assistant in the chat that answers” → “A chatbot is a chat assistant that answers” (clarity; meaning unchanged). Mirrored in PORT KEYS services.items[1].
2. meta.ogDescription: “the build of the fixes usually within 2 weeks” → “the fixes built usually within 2 weeks” (133 chars).
3. Title (42) and meta description (153) verified by script and kept; main term placed once each in title, H1 (plural), hero.body sentence 1 and the #services H2.
4. No links added or removed; body-link rule met only by same-page anchors per owner instruction (no Bulgarian links); FLAG 18 updated with this note, FLAG 16 marked confirmed.
5. All CTAs, tokens, anchors, canon facts, numbers, example label and rows, and all 18 flags carried forward.

---

title = "AI automation for small business | BizGrow"   # 42 chars
meta_description = "AI automation for small business: a free diagnosis, a report with prioritised fixes and clear prices within 48 hours, and a build usually within 2 weeks."   # 153 chars
og_title = "BizGrow: AI automation for small businesses"   # 43 chars
og_description = "A free diagnosis with no obligation. A report with clear one-time prices within 48 hours, and the fixes built usually within 2 weeks."   # 133 chars
h1 = "AI automation for small businesses. / Less busywork, more business."
primary_keyword = "ai automation for small business"
secondary_keywords = ["business automation"]

---

## OPTIMISED PAGE

Page: /en/ | Locale: en | Type: page-rewrite | Main term: ai automation for small business

---

## AI automation for small businesses. Less busywork, more business. {#hero}

H1 (two lines):
- hero.line1: AI automation for small businesses.
- hero.line2: Less busywork, more business.

[OWNER CONFIRM: H1 change. Current “Less busywork. / More business.” becomes line1 “AI automation for small businesses.” + line2 “Less busywork, more business.” (slogan kept as line 2), mirroring the bg pair.]

BizGrow provides AI automation for small business: we find where your business loses time, choose the fixes worth building and build them for you. We start with a free diagnosis and a 30-minute call, and the build usually takes up to 2 weeks. [OWNER CONFIRM: “in days, not months” (current hero.body, hero.overlayUnit, meta.description, ogTitle/ogDescription) is not in the 2026-11-15 canon and is replaced by the canon “usually within 2 weeks”, as on the finished bg pair. Confirm, or confirm the old wording to restore it.]

[Free diagnosis]({{BOOKING_URL}})

[Explore services](#services)

Metrics (replace “8 short questions” / “2 min to fill in”, REMOVE-BY-BRIEF; canon figures only):
- **30 min** diagnosis call (label “30 minutes”)
- **48 h** to the report with prices (label “48 hours”)
- **0** obligation

[OWNER CONFIRM: hero figures “8 short questions” and “2 min to fill in” removed (the questionnaire no longer exists) and replaced by 30 min / 48 h / 0 obligation, as on the bg pair.]

## Where you lose customers and hours every day {#losses}

- Missed calls and messages after working hours
- Hours lost writing quotes and invoices by hand
- Messages on Messenger, Instagram or WhatsApp that go without a timely reply
- No time for content and social media while competitors grow
- Not knowing which numbers in your business actually matter

[OWNER CONFIRM: no `losses.link` on /en/ (the bg link points to the Bulgarian-only /diagnostika/). Heading reworded from “Every day you lose customers and hours” to mirror the bg heading.]

## AI automation for small business, content and advertising in one place {#services}

[OWNER CONFIRM: the four current cards (Automations, SEO copywriting, Creatives, Custom solutions) are replaced by six cards mirroring the bg pair, with NO href (there are no English service pages); “Custom solutions” is no longer a card. Confirm the set, titles and texts.]

- **AI assistant and chatbot.** (icon: brain) A chatbot is a chat assistant that answers repeated questions on Messenger, Instagram and WhatsApp. When it cannot help, it collects the customer's contact details.
- **Automations.** (icon: loop) We build online booking with reminders, quotes that go from a filled-in form to a finished PDF, and automatic handling of documents and invoices. We also connect the programs you already use and set up a dashboard, one screen with your key figures.
- **SEO articles and copy.** (icon: spark) Our own content tool writes articles about your industry and city, prepared for Google searches (SEO, search engine optimisation). Each article is published only after you approve it.
- **Social media and creatives.** (icon: spark) Posts with text and an image go out on a schedule once you approve them. Every month we also prepare branded visuals and advertising materials.
- **Google and Facebook ads.** (icon: loop) A real marketing specialist plans, runs and tracks your ads and reports the results to you with concrete numbers. [OWNER CONFIRM: platform names “Google and Facebook” come from the keyword-map H1 of /reklama/ (canon says only advertising and marketing); no monthly cadence for the report is stated here. Confirm the platforms and whether the specialist reports monthly.]
- **SEO optimisation.** (icon: brain) We work on your website's technical SEO (how the site is set up for search engines), on the optimisation of individual pages and on the links that point to the site.

## Three steps to a working solution {#process}

The work goes through three steps, from the first call to support for the finished solution.

1. **Diagnosis: Where time and money leak.** We start with a free diagnosis and a 30-minute call. You describe the problems you see in your business, and together we find exactly where it loses time and money. [OWNER CONFIRM: step 1 no longer mentions the 2-minute questionnaire and, unlike bg, has no link to /diagnostika/.]
2. **Build: A clear one-time price.** Within 48 hours you receive a report with prioritised fixes and clear one-time prices. We then build the specific AI solution, usually within 2 weeks.
3. **Support: A transparent report every month.** After launch we monitor the solution and improve it. Every month you receive a short report on the work done.

## What the result can look like {#results}

Example scenarios from our method, not figures from specific clients.

| Business | Problem | Result |
|---|---|---|
| Restaurant | Nobody picks up at peak hours. | Bookings 24/7, about 10 hours less manual work a week. |
| Online shop | Questions about deliveries sit unanswered for hours. | 80% of the repeated questions answered in seconds. |
| Dental clinic | Missed calls and appointments moved around. | Online booking at any time. |

[OWNER CONFIRM: example rows kept verbatim with the label; confirm the rows and figures (“24/7”, “about 10 hours”, “80%”) or supply replacements. Heading “What the result looks like” becomes “What the result can look like”, as on bg.]

## The little “extra” that changes the result {#reasons}

We explain every solution in plain language and build only AI tools that solve a specific problem in your business.

- We work under GDPR
- No long-term contracts
- Transparent prices
- A result before a large investment

[OWNER CONFIRM: reasons.lead rewritten (old: “No jargon, and no solutions “just in case”. Only tools that work, shaped to your business.”), mirroring the bg lead.]

## The first step is free {#audit}

The diagnosis commits you to nothing. We show you exactly what we can fix and what it will cost.

[Book a free diagnosis]({{BOOKING_URL}})

## Frequently asked questions {#faq}

(New section between #audit and #contact, new anchor `#faq`, new dictionary key `faq`. Items in the FAQ block below.)

[OWNER CONFIRM: new FAQ section (7 questions mirroring the bg FAQ), answered only from the canon; no GDPR/data question because the canon allows only “We work under GDPR”.]

## Contact us {#contact}

[Book a video call now]({{BOOKING_URL}})

Send us an email at {{EMAIL}}

Form: Name / Email / Description; button “Submit” (mailto {{EMAIL}}, subject “BizGrow message from”).

[OWNER CONFIRM: contact.fields.name “Names” corrected to “Name”.]

---

## FAQ

[[faq]]

1. q: What can a small business automate?
   a: The most common candidates are answers to repeated questions on Messenger, Instagram and WhatsApp, online booking with reminders, quotes, documents and invoices. Business automation also covers connecting the programs you already use so that data fills itself in, and a dashboard with your key figures in one place.

2. q: How much does it cost to build a solution?
   a: Each solution has a one-time price that depends on what exactly is built. You find the price in the report you receive within 48 hours of the diagnosis, and we work without long-term contracts.

3. q: Where do I start if I don't know what to automate?
   a: Start with the free diagnosis: book a 30-minute call and tell us about the problems you see in your business. The diagnosis commits you to nothing.

4. q: How long does the build take?
   a: Once you have the report, we build the specific solution, usually within 2 weeks.

5. q: Will AI replace the people on my team?
   a: AI takes over repeated tasks, and you stay in control: articles and posts go out only after you approve them. Your advertising is run by a real marketing specialist, and when the chat assistant cannot help, it collects the customer's contact details.

6. q: Is this suitable for my industry?
   a: We work with small businesses: restaurants and cafés, hotels and guest houses, salons, online shops, retail shops and showrooms, clinics and practices, car services and tradespeople, real estate and B2B companies (businesses that sell to other businesses). After the diagnosis, the report shows which fixes make sense for your type of business. [OWNER CONFIRM: last sentence rephrased from the bg “In the diagnosis you can see examples for your type of business”, which refers to the Bulgarian-only checker page.]

7. q: Do I have to sign a long-term contract?
   a: No, we work without long-term contracts. During support we monitor the solution, and every month you receive a short report on the work done.

---

## PORT KEYS

Strings for `site/src/i18n/dictionaries/en.ts` (type `Dictionary` in `site/src/i18n/types.ts`). Body-mapped keys repeat the copy above so later stages edit both together.

### meta
- meta.title: AI automation for small business | BizGrow (42 chars, counted by script) [OWNER CONFIRM: title change from “BizGrow [dash] Find where the business loses time”]
- meta.description: AI automation for small business: a free diagnosis, a report with prioritised fixes and clear prices within 48 hours, and a build usually within 2 weeks. (153 chars, counted by script)
- meta.ogTitle: BizGrow: AI automation for small businesses
- meta.ogDescription: A free diagnosis with no obligation. A report with clear one-time prices within 48 hours, and the fixes built usually within 2 weeks. (133 chars; Step 4 wording edit)
- meta.ogLocale: en_US (unchanged)

### a11y (unchanged)
- skipToContent “Skip to content”, primaryNav “Primary”, home “BizGrow home”, openMenu “Open menu”, closeMenu “Close menu”, newTab “(opens in a new tab)”, language “Language”, results “Free diagnosis”, step “Step”, breadcrumb “Breadcrumb”

### page (unchanged)
- home “Home”, faq “Frequently asked questions”, related “Related services”, diagnosis “Free diagnosis”

### nav (unchanged)
- nav.links: Services → #services; Process → #process; Contact us → #contact
- nav.cta: Book a call → {{BOOKING_URL}}

### hero
- hero.line1: AI automation for small businesses.
- hero.line2: Less busywork, more business.
- hero.body: BizGrow provides AI automation for small business: we find where your business loses time, choose the fixes worth building and build them for you. We start with a free diagnosis and a 30-minute call, and the build usually takes up to 2 weeks.
- hero.primary: Free diagnosis → {{BOOKING_URL}}
- hero.secondary: Explore services → #services
- hero.imageSrc: /bizgrow-banner.webp (unchanged)
- hero.imageAlt: BizGrow: AI and automation for small businesses. The banner reads: integrate AI, automate workflows, save time and costs, grow your business. [OWNER CONFIRM: reworded without the em-dash; describes the English text baked into the banner]
- hero.overlayLabel: Free diagnosis
- hero.overlayUnit: usually within 2 weeks [OWNER CONFIRM: replaces “in days, not months”]
- hero.overlayValue: not set (the overlay is a phrase)

### metrics
- { value: "30 min", caption: "diagnosis call", label: "30 minutes" }
- { value: "48 h", caption: "to the report with prices", label: "48 hours" }
- { value: "0", caption: "obligation" }

### losses
- losses.title: Where you lose customers and hours every day
- losses.items: (5, as in #losses above)
- losses.link: NOT set on /en/

### services
- services.title: AI automation for small business, content and advertising in one place
- services.items (6, NO `href`):
  1. { icon: "brain", title: "AI assistant and chatbot", body: "A chatbot is a chat assistant that answers repeated questions on Messenger, Instagram and WhatsApp. When it cannot help, it collects the customer's contact details." }
  2. { icon: "loop", title: "Automations", body: "We build online booking with reminders, quotes that go from a filled-in form to a finished PDF, and automatic handling of documents and invoices. We also connect the programs you already use and set up a dashboard, one screen with your key figures." }
  3. { icon: "spark", title: "SEO articles and copy", body: "Our own content tool writes articles about your industry and city, prepared for Google searches (SEO, search engine optimisation). Each article is published only after you approve it." }
  4. { icon: "spark", title: "Social media and creatives", body: "Posts with text and an image go out on a schedule once you approve them. Every month we also prepare branded visuals and advertising materials." }
  5. { icon: "loop", title: "Google and Facebook ads", body: "A real marketing specialist plans, runs and tracks your ads and reports the results to you with concrete numbers." } [OWNER CONFIRM: platforms in title; no monthly cadence stated]
  6. { icon: "brain", title: "SEO optimisation", body: "We work on your website's technical SEO (how the site is set up for search engines), on the optimisation of individual pages and on the links that point to the site." }

### process
- process.title: Three steps to a working solution (unchanged)
- process.lead: The work goes through three steps, from the first call to support for the finished solution.
- process.steps:
  1. { n: "1", label: "Diagnosis", title: "Where time and money leak", body: "We start with a free diagnosis and a 30-minute call. You describe the problems you see in your business, and together we find exactly where it loses time and money." }
  2. { n: "2", label: "Build", title: "A clear one-time price", body: "Within 48 hours you receive a report with prioritised fixes and clear one-time prices. We then build the specific AI solution, usually within 2 weeks." }
  3. { n: "3", label: "Support", title: "A transparent report every month", body: "After launch we monitor the solution and improve it. Every month you receive a short report on the work done." }

### results
- results.title: What the result can look like
- results.note: Example scenarios from our method, not figures from specific clients. (unchanged)
- results.rows: unchanged (3 rows, verbatim) [OWNER CONFIRM]

### reasons
- reasons.title: The little “extra” that changes the result (unchanged)
- reasons.lead: We explain every solution in plain language and build only AI tools that solve a specific problem in your business.
- reasons.items: unchanged (4)

### cta (#audit)
- cta.title: The first step is free (unchanged)
- cta.body: The diagnosis commits you to nothing. We show you exactly what we can fix and what it will cost. (unchanged)
- cta.button: Book a free diagnosis → {{BOOKING_URL}} (unchanged)

### faq (NEW key)
- faq.title: Frequently asked questions (equals page.faq)
- faq.items: the 7 { question, answer } pairs from the FAQ block above (no links in any answer)

### contact
- contact.title: Contact us
- contact.book: Book a video call now → {{BOOKING_URL}}
- contact.emailBefore: Send us an email at (+ {{EMAIL}})
- contact.fields: Name / Email / Description (name changed from “Names”)
- contact.submit: Submit
- contact.mailSubject: BizGrow message from

### footer
- footer.descriptor: We find where your business loses time and fix it with AI. (“the business” → “your business”)
- footer.services “Services”, process “Process”, contact “Contact us”, privacy “Privacy”, rights “All rights reserved.”: unchanged

Not added: `related` (the home `Dictionary` has no such key; all siblings are Bulgarian-only).

---

## INVENTORY CHECK

| item | where it now sits |
|---|---|
| C1 nav.cta “Book a call” → {{BOOKING_URL}} | PORT KEYS nav (unchanged) |
| C2 hero.primary “Free diagnosis” → {{BOOKING_URL}} | #hero |
| C3 hero.secondary “Explore services” → #services | #hero |
| C4 cta.button “Book a free diagnosis” → {{BOOKING_URL}} | #audit |
| C5 contact.book “Book a video call now” → {{BOOKING_URL}} | #contact |
| C6 contact.submit “Submit” + emailBefore “Send us an email at” | #contact |
| T1 {{BOOKING_URL}} | nav, #hero, #audit, #contact |
| T2 {{EMAIL}} | #contact (email line, form mailto); footer unchanged |
| Anchors #hero #losses #services #process #results #reasons #audit #contact | all kept, same order; #faq added before #contact (brief) |
| F1 free diagnosis | #hero (body, primary CTA, overlayLabel), a11y.results, page.diagnosis, #process 1, #audit, FAQ 3 |
| F2 30-minute call | #hero body, metrics “30 min”, #process 1, FAQ 3 |
| F3 report with prioritised fixes and clear prices within 48 h | #process 2 (“Within 48 hours you receive a report with prioritised fixes and clear one-time prices”), metrics “48 h”, meta, FAQ 2, FAQ 6 |
| F4 build usually within 2 weeks | #hero body (“usually takes up to 2 weeks”), overlayUnit, #process 2, FAQ 4, meta/og |
| F5 monitoring/improvement + short monthly report | #process 3, FAQ 7 |
| F6 one-time price | #process 2 title “A clear one-time price”, FAQ 2 |
| F7 “We work under GDPR” | #reasons |
| F8 “No long-term contracts”, “Transparent prices”, “A result before a large investment” | #reasons; FAQ 2, FAQ 7 |
| F9 diagnosis commits to nothing; what we fix and what it costs | metrics “0 obligation”, #audit, FAQ 3 |
| footer.descriptor | PORT KEYS footer (“your business”) |
| S1 chat assistant, collects contact | #services card 1, FAQ 5 |
| S2 booking, quotes PDF, documents/invoices, connected programs, dashboard | #services card 2, FAQ 1 |
| S3 own content tool, SEO articles after approval | #services card 3, FAQ 5 |
| S4 scheduled posts after approval, monthly branded visuals | #services card 4, FAQ 5 |
| S5 real marketing specialist, reports with numbers | #services card 5, FAQ 5 |
| S6 SEO optimisation: technical, on-page, links | #services card 6 |
| A1 audience list | FAQ 6 |
| N1 “8 short questions”, N2 “2 min to fill in” | REMOVED BY BRIEF → metrics “30 min” / “48 h” |
| N3 “0 obligation” | metrics |
| N4 30 min / N5 48 hours / N6 usually within 2 weeks | #hero, #process 1-2, metrics, FAQ 2-4 |
| N7 “24/7”, “about 10 hours less manual work a week” | #results row Restaurant (labelled) |
| N8 “80%” | #results row Online shop (labelled) |
| L1 example label | #results, directly above the rows, verbatim |
| L2 “in days, not months” | replaced by canon “usually within 2 weeks” (hero.body, overlayUnit, meta, og), flagged |
| E1-E3 | #results table, verbatim |
| Losses 5 | #losses 5/5 (reworded only) |
| Reasons 4 | #reasons 4/4, verbatim |
| Process step 1 questionnaire wording | REMOVED BY BRIEF → free diagnosis + 30-minute call, no link |
| Four-card set incl. “Custom solutions” | REMOVED BY BRIEF → six cards, no href |
| losses.link | not added on /en/ (brief) |
| UI strings (a11y, page, contact.fields, mailSubject, footer, imageSrc, ogLocale) | PORT KEYS; imageAlt reworded without em-dash; fields.name “Name” |
| FAQ (0 on current page) | new #faq, 7 items |

Self-check done: em-dashes 0 in the whole file (old em-dash titles quoted as “[dash]”), hype words 0, AI vocabulary 0, signposting 0, jargon explained on first use (chatbot, dashboard, SEO, technical SEO, B2B), no prices, no offers, no testimonials, no guarantee wording, GDPR only “We work under GDPR”, “free” only about the diagnosis, example label in #results, one booking CTA per section, no link to any Bulgarian page, section ids match the bg pair, main term exactly in title, hero.body sentence 1, #services H2 and meta.description (H1 carries the plural form; ogTitle the plural form); not in FAQ or other headings. “business automation” once (FAQ 1).

---

## FLAGS

1. [OWNER CONFIRM] Title change “BizGrow [dash] Find where the business loses time” → “AI automation for small business | BizGrow”; meta/og rewritten around the main term (front matter; may merge with 2 at Step 6).
2. [OWNER CONFIRM] H1 change: hero.line1 “AI automation for small businesses.” + hero.line2 “Less busywork, more business.” (#hero).
3. [OWNER CONFIRM] hero.imageAlt reworded without the em-dash (#hero / PORT KEYS).
4. [OWNER CONFIRM] “in days, not months” → canon “usually within 2 weeks” in hero.body, overlayUnit, meta, og (#hero, PORT KEYS).
5. [OWNER CONFIRM] Hero figures 8 questions / 2 min → 30 min / 48 h / 0 obligation (REMOVE-BY-BRIEF) (#hero).
6. [OWNER CONFIRM] No `losses.link` on /en/; losses heading reworded to mirror bg (#losses).
7. [OWNER CONFIRM] Six service cards without href replacing the four-card set (“Custom solutions” dropped) (#services).
8. [OWNER CONFIRM] Card title “Google and Facebook ads” (platform names not canon text); no monthly cadence stated for the specialist's report (#services).
9. [OWNER CONFIRM] Process step 1: no questionnaire, no link (unlike bg) (#process).
10. [OWNER CONFIRM] Example rows E1-E3 with “24/7”, “about 10 hours”, “80%” + heading “What the result can look like” (#results; label kept).
11. [OWNER CONFIRM] reasons.lead rewritten to mirror bg (#reasons).
12. [OWNER CONFIRM] New `#faq` section (7 questions) + new `faq` key and component; no GDPR/data question (#faq).
13. [OWNER CONFIRM] FAQ 6 last sentence rephrased away from the bg checker page (#faq).
14. [OWNER CONFIRM] contact.fields.name “Names” → “Name” (#contact).
15. FAQ canon guards inherited from bg: FAQ 4 has no timeline-in-report sentence; FAQ 7 states neither that support is optional nor required.
16. Main-term H2: “AI automation for small business, content and advertising in one place” keeps the exact phrase intact (confirmed at Step 4: exact phrase intact, the only H2 carrying the main term).
17. Port notes: exact `en` Dictionary shape + `faq`; services 6 items without href; no `losses.link`; no `related`; a11y and page unchanged; footer.descriptor “your business”.
18. For the human, not inline: no contextual body links to other pages (no English pages besides home; owner instruction 2026-11-15: no links to Bulgarian pages). Step 4: the 1-3 body-link rule is met only by same-page anchors (hero.secondary “Explore services” → #services; nav → #services, #process, #contact); no inline anchor links were added because the home dictionary fields are plain strings (biz-grow main, `Sections.tsx` renders process.lead / cta.body as text, so `[label](#anchor)` would print literally); not answerable from canon and not on the page: English-language service scope / clients outside Bulgaria, prices, ROI, data storage and tools.

No [VERIFY] (0 new external facts). No [DATA NEEDED]. No [LINK NEEDED].

## CANON ADDITIONS

none

---

## INVENTORY DIFF (00-inventory.md vs this page)

Result: PASS. Every inventory item is present with the same meaning; nothing was dropped or weakened. Step 4 edits touched only #services card 1 wording (S1 meaning unchanged: chat assistant, repeated questions on Messenger, Instagram, WhatsApp, collects contact details) and meta.ogDescription (F1, F3, F4 kept: free diagnosis, no obligation, one-time prices within 48 hours, usually within 2 weeks).

| group | status |
|---|---|
| CTAs C1–C6 | 6/6 present: “Book a call” (nav), “Free diagnosis”, “Explore services” → #services, “Book a free diagnosis”, “Book a video call now”, “Submit” + “Send us an email at” |
| Tokens T1–T2 | {{BOOKING_URL}} ×4 call sites (nav, hero, #audit, #contact); {{EMAIL}} (contact line, form mailto, footer) |
| Anchors | #hero #losses #services #process #results #reasons #audit #contact kept in order; #faq added (by brief) |
| Canon facts F1–F9 + footer.descriptor | all present, unchanged |
| Services S1–S6 | 6/6; S1 reworded only (“a chat assistant”), body and PORT KEYS identical |
| Numbers | N3 “0 obligation”, N4 30 min, N5 48 hours, N6 usually within 2 weeks, N7 “24/7” / “about 10 hours”, N8 “80%”: present. N1/N2: REMOVE-BY-BRIEF (excepted) |
| Labels | L1 verbatim in #results; L2 “in days, not months” replaced by canon wording, flagged (mirrors bg) |
| Example rows E1–E3 | verbatim |
| Losses | 5/5 |
| Reasons | 4/4 verbatim |
| FAQ | 7/7 unchanged |
| UI strings | a11y (10), page (4), contact.fields/mailSubject, footer (6), imageSrc, ogLocale present; imageAlt and “Name” flagged as before |
| Flags | 18/18 carried (16 marked confirmed at Step 4; 18 extended with the anchor-only link note) |
| REMOVE-BY-BRIEF | N1, N2, questionnaire step wording, four-card set incl. “Custom solutions”, losses.link, #ads: absent as instructed |
| PORT KEYS sync | body ↔ PORT KEYS identical for every edited string (services.items[1].body); meta strings in PORT KEYS equal the front-matter values above |
