# BizGrow — site rules the pipeline must satisfy (reference, binding)

Written 2026-11-15 at onboarding from the `biz-grow` repo (`desislavamit/biz-grow`, local
`~/Work/biz-grow`): `docs/ai-consultancy-spec.md` (build spec v2), `site/src/i18n/dictionaries/
bg.ts` and `en.ts`, `site/src/i18n/config.ts`, plus the owner's decisions of 2026-11-15
(services, process, audience, "professional version" voice). **If the site repo or a later owner
decision differs from this copy, the site repo / owner wins**: re-read the spec, the two
dictionaries and `config.ts` at the start of every run and log any difference in `log.md`.

The pipeline never writes to the site repo. It produces a content file; a human ports it into
the dictionaries and components and runs the site's own checks (`npm run lint`,
`npx tsc --noEmit`, `npm run build`).

---

## 1. Claims (B2B). These rules override SEO goals.

- AI text is a **draft** until the owner approves it. The pipeline never marks a page approved.
- **Facts about BizGrow only from the canon** in `markets/bg/author.md` (owner-confirmed
  2026-11-15). UNKNOWN and never stated: prices, team names, company legal data, address, phone,
  client names, case results (plus the Tier 3 list in the author file).
- **No invented numbers.** A figure is allowed only if it is canon, inside a clearly labelled
  hypothetical example or estimate, or an external fact with an authoritative source in
  `[[sources]]` (max 3 new sourced facts per page per run; `verification-policy.md`).
- **Example scenarios are hypothetical and labelled** as such in the same section. The current
  label: „Примерни сценарии по нашия метод, не данни от конкретни клиенти.“ / "Example scenarios
  from our method, not figures from specific clients."
- **No guarantees** of rankings, positions in Google, traffic, leads, sales, revenue, savings, ROI
  or response times.
- **GDPR** only in the owner's wording („Работим по GDPR“ / "We work under GDPR").
- **Never remove** a CTA, `{{TOKEN}}`, section anchor, canon fact, example label or FAQ from a
  page being rewritten, unless the brief lists it under REMOVE-BY-BRIEF.

## 2. Banned claims and words

Matched case-insensitively on visible text, title, meta description, headings, FAQ and ALT.
`*` = any ending.

| term / pattern | locale | notes |
|---|---|---|
| гарантир*, гаранци*, guarantee* | bg, en | no guarantee of any outcome; never excused by negation unless the owner's own copy uses it |
| първо място в Google, топ позиции, #1 / №1, лидер*, най-добрите, най-добър | bg | also "rank #1", "top of Google", "leading", "the best" in en |
| революцион*, магия, магическ*, невероят*, уникал*, безпрецедент* | bg | hype |
| трансформира* бизнеса, следващо ниво, без никакви усилия, напълно автоматично, безкрайни възможности, мощен AI | bg | hype |
| revolutionary, magic*, game-chang*, cutting-edge, next level, seamless, effortless*, unlock, supercharg*, skyrocket*, limitless | en | hype |
| 10x, x10, удвои* (продажби/приходи), double your | bg, en | outcome promises |
| 100% (with GDPR / съвместим* / compliant / сигурн* / secure) | bg, en | compliance or security guarantee |
| сертифицира* / certified (about BizGrow or GDPR) | bg, en | not in canon |
| безплатн* / free — anything other than the diagnosis | bg, en | only the diagnosis is free |
| само днес, ограничени места, побързайте, last chance, limited spots, hurry | bg, en | urgency / scarcity |
| „ти“ forms: губиш, попълваш, получаваш, …; Открий, Запази, поправи (singular imperatives); твой*, теб, тебе; „те/ти“ as pronouns | bg | register: formal „Вие“ only |

Pipeline stance: prefer to avoid even negated forms of a banned term.

## 3. No prices, offers or testimonials

- PRICE: a digit followed by лв / лева / евро / € / EUR / BGN / $ → forbidden on every page.
  Price talk stays at the canon level: „ясни еднократни цени в офертата“ (no deadline), „прозрачни
  цени“, „без дългосрочни договори“.
- OFFER: промоци*, отстъпк*, ваучер*, discount*, promo*, voucher* → forbidden.
- TESTIMONIAL: отзив*, „мнения на клиенти“, „доволни клиенти“, client names or logos, "what our
  clients say" → forbidden (the spec removed the mockup's testimonial panel on purpose).

## 4. CTAs and contact

- Booking: every book-now CTA links the Google Calendar appointment page, written as the token
  `{{BOOKING_URL}}` (it stands for `site.bookingUrl` in `site/src/i18n/config.ts`; the site's
  `BookingLink` component opens it in a new tab). Never hard-code the URL.
- Email: always the token `{{EMAIL}}` (stands for `site.email`). Never hard-code the address.
- Approved CTA wording (BG): „Запазете безплатна диагностика“, „Запазете час“, „Запазете
  видеоразговор“, „Изпратете“, „Разгледайте услугите“. (EN): "Book a free diagnosis", "Book a
  call", "Book a video call", "Submit", "Explore services". A formal-imperative equivalent is
  allowed; a „ти“ imperative is not. The current BG copy's „Безплатна диагностика“ (noun CTA)
  may stay.
- At most one booking CTA per section; no urgency or scarcity wording.
- No phone number, address or messenger handle as a contact channel (unknown).

## 5. Page structure

- Home pages (`/`, `/en/`) keep the sections and anchors of spec §3: `#hero`, `#losses`,
  `#services`, `#process`, `#results`, `#reasons`, `#audit`, `#contact` (`#ads` was removed by
  the owner's session on 2026-11-15). The nav links
  `#services`, `#process`, `#contact`. Renaming or removing an anchor needs the brief.
- Both locales have identical sections; the English page uses the same section ids.
- The current site lists four service cards (Автоматизации, SEO копирайтинг, Креативи, Решения по
  поръчка). The owner-confirmed services (2026-11-15) are AI автоматизации, собствен инструмент
  за съдържание, криейтиви всеки месец, маркетинг специалист and SEO оптимизация. A home-page
  rewrite aligns the cards to the service pages in `BizGrow/keyword-map.md` (one card per page,
  each card linking to its page) and records the change as an `[[owner_items]]` entry.
- Multi-page site (2026-11-15): content pages are Next.js routes rendered from a typed
  `ContentPage` object (`site/src/content/types.ts` on branch `feature/seo-improvements`):
  `meta.title`, `meta.description`, `label` (breadcrumb/card name), `summary` (one sentence for
  cards), optional `eyebrow`, `h1`, `lead`, `sections[]` (`id`, `title`, `paragraphs[]`,
  optional `bullets[]`), `faq[]`, `related[]` (3 paths), `service` (schema name). Inline syntax:
  `**bold**` and `[label](/path/)` or `[label](#anchor)` only. Internal links use root paths
  from `BizGrow/conversion-links.md`; the site makes them relative.
- Service pages (new-page): see `agents/outline-architect.md` default order; about 5–8 H2s.
- Card copy: title + 1–2 sentence body; list items one sentence or one noun phrase.

## 6. SEO limits

- `title` ≤ 60 characters **including** ` | BizGrow` (or `BizGrow | …` on the home page if the
  owner prefers; one pattern per site), unique, no em-dash. The current titles
  („BizGrow — Открий къде бизнесът губи време“) use an em-dash and „ти“-era wording: a rewrite
  replaces them.
- `meta_description` 120–160 characters, written for that page, contains the main term, no
  skeleton repeated across pages, no em-dash.
- One main search term per address (`BizGrow/keyword-map.md`). Place it **once each** in the
  title, the H1, the first 100 words and one H2. Never target another address's main term.
- The first sentence states what the page offers or answers.
- FAQ: `[[faq]]` entries (`q`, `a`), answers of 1–3 sentences that stand alone and are supported
  by the canon or sources; never a body heading word for word.
- hreflang, canonical and Open Graph are produced by the site layouts; the pipeline supplies
  only title, meta description and OG text if the brief asks.

## 7. Language and voice

- Bulgarian: formal „Вие“ with capitalised courtesy forms (Вие, Ви, Вас, Ваш, Вашия, Вашата,
  Вашите) in direct address; no „ти“ forms anywhere. Brand and platform names in Latin script
  (BizGrow, Messenger, Instagram, WhatsApp, Google, GDPR, AI, SEO, PDF). Quotes „…“.
- English: plain professional English. Quotes “…”.
- No em-dashes (—) in either language. Use a comma, colon, full stop, or the hyphen in ranges.
- BIZGROW VOICE (owner decision 2026-11-15, full text in `markets/bg/author.md`): a professional
  consultancy speaking to small-business owners; complete sentences, mostly 10–22 words;
  paragraphs of 2–4 sentences; lists for services and steps; no slang, no fragments as style, no
  hype, no jargon without explanation.

## 8. Content file format (the pipeline's final output)

The site is a Next.js static export whose copy lives in typed TypeScript dictionaries
(`site/src/i18n/dictionaries/bg.ts`, `en.ts`; type in `site/src/i18n/types.ts`), not in Markdown.
The pipeline therefore delivers a **porting source**: Markdown with TOML front matter between
`+++` lines. Full template with comments: `templates/content-file-template.md`.

```
+++
title = "… | BizGrow"                 # ≤ 60 chars incl. suffix, no em-dash
meta_description = "…"                # 120–160 chars, contains the primary keyword
h1 = "…"
slug = "home"                         # home | en-home | keyword-map slug (en- prefix for English)
locale = "bg"                         # bg | en
primary_keyword = "…"                 # exactly the keyword-map term for this address
secondary_keywords = ["…", "…"]
status = "draft"
last_updated = "YYYY-MM-DD"

[[sections]]
id = "services"                       # anchor; equals the body block id
heading = "…"
kind = "cards"                        # hero | paragraphs | list | steps | cards | table | cta | contact | faq
dictionary_key = "services"           # existing dictionary key, or "" for a new one

[[faq]]
q = "…"
a = "…"

[[sources]]
title = "…"
url = "…"
checked_by = ""
checked_on = ""

[[owner_items]]
item = "…"                            # what the owner must confirm or supply
decision = ""
decided_by = ""
decided_on = ""
+++

## <heading> {#<id>}
<body of that section>
```

Body in Markdown: one `## <heading> {#<id>}` block per `[[sections]]` entry, in the same order;
cards and steps as Markdown lists (`- **Title.** Body.`); CTAs as `[CTA text]({{BOOKING_URL}})`.
Tokens in use (keep verbatim, never expand): `{{BOOKING_URL}}`, `{{EMAIL}}`.

The final content file contains **no** `[VERIFY]`, `[OWNER CONFIRM]`, `[DATA NEEDED]` or
`[LINK NEEDED]` markers. Every open question becomes an `[[owner_items]]` entry or a line in
`06-verification.md` under REMAINING FOR HUMAN.
