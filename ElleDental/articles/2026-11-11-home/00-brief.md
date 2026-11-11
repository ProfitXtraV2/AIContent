# 00-BRIEF — ELLE Dental — / (home)

MARKET: bg — Bulgarian patients, София (local clinic, ж.к. Света Троица)
CONTENT TYPE: page-rewrite (one of the 28 addresses) — one-off manual run authorised by the owner on 2026-11-11 (UX restructure of the home page; all site text through ContentAI). Brand otherwise stays PAUSED.
PAGE: / (slug `home`)
PAGE TYPE / GROUP: home / (no group)
MAIN TERM (WebPortals _publisher/keyword-map.md): дентална клиника софия + зъболекар софия
VARIANTS: зъболекар, дентална клиника в София, зъболекар в Света Троица, дентален кабинет
AHREFS: дентална клиника софия | 500 | KD 0 | topic-backlog.md (2026-11-11); зъболекар софия | 1,000 | KD 54 | same
H1: Зъболекар и дентална клиника в София, Света Троица (current = keyword-map proposal; keep)
SOURCE OF CURRENT PAGE: ProfitXtraV2/WebPortals @ feature/elledental-original-look (LOCAL, uncommitted modification on top of 1737a44a7a2e538e14db5989e1a80aa41784fdbe) : ElleDental/_publisher/content/home.md — deviation from step 0 on the owner's instruction (this is the newest home text).

## THE BRIEF (owner, 2026-11-11) — UX restructure

The page template now renders the body in two places:
1. Everything BEFORE a line containing exactly `<!-- more -->` appears directly under the hero, ABOVE the treatment cards and the doctor cards.
2. Everything AFTER it appears lower down, after the doctor cards and the photo tiles, followed by the FAQ.

(Confirmed in the publisher: `build_site.py` MORE_MARKER = "<!-- more -->"; BODY = before, BODY_MORE = after.)

**Part 1 (before `<!-- more -->`)** must be short:
- 2-3 sentences that say what the clinic is and where, containing „зъболекар“ and „дентална клиника в София“ naturally (main terms: „дентална клиника софия“, „зъболекар софия“).
- Then a compact list of 4-6 quick facts, one line each, taken ONLY from facts already on the current page:
  - adults and children;
  - the two doctors (keep their existing link tokens `[{{DOCTOR_ONE_NAME}}](/{{DOCTOR_ONE_SLUG}}/)`, `[{{DOCTOR_TWO_NAME}}](/{{DOCTOR_TWO_SLUG}}/)`);
  - the dated Superdoc rating — NOT on the current page, so it is NOT used;
  - languages;
  - the location in ж.к. Света Троица.

**Part 2 (after `<!-- more -->`)**:
- A shortened „what to expect at a visit“ section (keep W4-W7 from the inventory).
- Then ONE clear block for address, hours and booking, using the existing tokens (`{{ADDRESS_FULL}}`, `{{HOURS_REGULAR}}`, `{{HOURS_CLOSED}}`, `{{HOURS_NOTE}}`, `{{PHONE}}`, `{{PHONE_TEL}}`, `{{DOCTOR_ONE_SUPERDOC}}`, `{{DOCTOR_TWO_SUPERDOC}}`, as the current page uses them) and a link to `/kontakti/` for the map and directions.

**Remove** from the body: the long treatment list and the doctors' biography paragraphs (the page's own treatment cards and doctor cards already show both). Keep any safety or practical facts.
Keep all `[[faq]]` entries (improve wording only if needed). Keep title, meta_description and h1 unless the SEO step finds a defect. Keep the existing `[[clinical_items]]` entry verbatim.
Professional ELLE VOICE throughout. **Target 250-400 body words in total** (both parts together; current body ≈ 488 words incl. tokens).

The line `<!-- more -->` must appear exactly once, alone on its line, in every draft from step 2 onwards and in the deliverable.

## CURRENT PAGE + INVENTORY
- 00-current.md written: yes
- 00-inventory.md written: yes — 8 warnings/practical, 0 risks, 0 contraindications, 5 numbers, 28 links, 13 tokens, 0 sources, 1 existing clinical item, 4 FAQs (with REMOVE-BY-BRIEF marks)

## SITE RULES RE-READ THIS RUN
- banned-terms.json: same as reference/site-rules.md §2. claim-exceptions.json: [] (same). keyword-map.md home row: same as conversion-links / backlog. clinic.json: same constants. build_site.py (local, uncommitted): adds the `<!-- more -->` split (BODY / BODY_MORE) — new since the 2026-11-11 site-rules copy.

## PATIENT QUESTIONS (web search „дентална клиника софия зъболекар въпроси“, 2026-11-11)
- Do you treat children as well as adults? — yes, answered (FAQ Q1)
- Is there an emergency/duty service? — yes, answered (FAQ Q4: no)
- How do I book? — yes (FAQ Q3)
- What happens at the first visit / are alternatives explained? — yes (body, what to expect)
- Prices / health-fund (НЗОК) — NO: prices are banned; НЗОК not in canon → not answered
- Doctor qualifications — doctor pages / doctor cards (not in body per brief)

## CANDIDATE NEW SOURCES
- None. No new medical facts on this page.

## SIBLING PAGES (avoid copied wording)
- /za-nas/ (approach), /kontakti/ (address/hours/booking), doctor pages (bios).

## NOTES
- Existing clinical item CI1 stays verbatim (it still covers the doctors' data shown in the doctor cards and the treatment groups).
