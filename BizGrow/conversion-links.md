# Conversion Links — BizGrow

Single source of truth for **internal links, section anchors and the booking/email targets** used
in every BizGrow page the pipeline drafts. Taken from the `biz-grow` repo on **2026-11-15**
(`docs/ai-consultancy-spec.md` §3 and §5, `site/src/i18n/config.ts`).

BizGrow is a consultancy, not an affiliate site: there are **no affiliate links**, no partner
offers and no prices. Every link in this file points to the BizGrow site itself, the booking page
or the email address.

The site has the home pages plus the content pages below (planned 2026-11-15; links become live when each page is ported). A link to any address not in this file is a defect:
write `[LINK NEEDED: <topic>]` in a draft instead, and never let it reach the final content file.
When the owner's session adds pages (rows with status `planned` or `live` in `keyword-map.md`),
add them to the table below in the same change.

---

## Pages

| path | page | locale | use when |
|---|---|---|---|
| / | Home (Bulgarian, default) | bg | orientation; BizGrow in general |
| /en/ | Home (English) | en | the English pair of `/`; never as an editorial link inside Bulgarian copy |
| /ai-asistent/ | AI асистент и чатбот за бизнеса | bg | AI assistants/chatbots in Messenger, Instagram, WhatsApp, on the site |
| /avtomatizacii/ | Автоматизация на бизнес процеси | bg | booking, reminders, offers, documents, invoices, connected systems, dashboards |
| /seo-statii/ | SEO копирайтинг и SEO статии | bg | the content tool: SEO articles, product descriptions, copywriting |
| /socialni-mrezhi/ | Поддръжка на социални мрежи и криейтиви | bg | scheduled social posts, monthly creatives, visuals for ads |
| /reklama/ | Реклама в Google и Facebook | bg | the marketing specialist: Google Ads, Facebook/Instagram ads, reporting |
| /seo-optimizacia/ | SEO оптимизация на сайтове | bg | technical SEO, on-page optimisation, links |
| /diagnostika/ | Безплатна диагностика (checker) | bg | the free diagnosis; "see where your business loses time" |

## Section anchors (same ids on both locales)

| anchor | section | use when |
|---|---|---|
| #hero | Promise, CTAs, diagnosis figures | top of page |
| #losses | Daily losses | the problems BizGrow fixes |
| #services | Services | pointing to the service list |
| #process | Three steps | how the work goes |
| #results | Example scenarios (hypothetical, labelled) | what a result can look like; never as "client results" |
| #reasons | Why this offer (GDPR, no long-term contracts, transparent prices) | policies |
| #audit | CTA band: the first step is free | the free diagnosis |
| #contact | Contact: booking, email, form | contacting BizGrow |

On a separate page, link a home-page section as `/#<anchor>` (bg) or `/en/#<anchor>` (en).

## Booking and email (tokens only)

| token | stands for | link rule |
|---|---|---|
| `{{BOOKING_URL}}` | `site.bookingUrl` in `site/src/i18n/config.ts` (Google Calendar appointment page; the site opens it in a new tab via `BookingLink`) | every book-now CTA: „Запазете безплатна диагностика“, „Запазете час“, „Запазете видеоразговор“ / "Book a free diagnosis", "Book a call", "Book a video call" |
| `{{EMAIL}}` | `site.email` in `site/src/i18n/config.ts` (rendered as a `mailto:` link) | "write to us" lines and the contact block |

Never write the booking URL or the email address in the copy; the tokens keep one source of
truth in `config.ts`.

---

## Link rules

1. **Only addresses, anchors and tokens from this file.** Never invent a path.
2. **Body links:** 1–3 contextual links per page; every link and CTA the current page has is
   kept (removal = defect).
3. **Anchors** are plain words an owner would use, never exact-match stuffing.
4. **Booking:** at most one booking CTA per section; no urgency wording („само днес“,
   „ограничени места“, "limited spots").
5. **No external links in the body** except `[[sources]]` (Tier B facts), which the human
   decides how to show. No competitor agencies, tool vendors, directories or portals.
6. **No phone, address or messenger handle** as a contact channel (unknown).
