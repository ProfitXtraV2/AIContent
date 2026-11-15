# Step 6 — Verification + content file (fresh context)

Inputs: `05b-final-draft.md` (body + title + meta + FAQ + flags), `00-current.md`,
`00-inventory.md`, `reference/verification-policy.md`, `reference/site-rules.md`,
`templates/content-file-template.md`, `BizGrow/keyword-map.md`.

The deliverable is `content/<slug>.md`: Markdown with TOML front matter. The BizGrow site is
Next.js with typed TypeScript dictionaries, not Markdown, so this file is a PORTING SOURCE: a
human (or the owner's session) copies each section into `site/src/i18n/dictionaries/<locale>.ts`
and the page components. The pipeline never edits the site repo.

1. For every `[VERIFY: … — URL]`: fetch the URL, confirm HTTP 200 (`curl -sI`), quote the
   supporting passage in `06-verification.md`. Confirmed → keep the sentence, remove the marker,
   add the source to `[[sources]]` (empty `checked_by`/`checked_on`) and an `[[owner_items]]`
   entry (new fact, source, quote; decision fields empty). Unreachable / ambiguous / disagreeing
   → remove the sentence, log it under REMAINING FOR HUMAN.
2. For every `[OWNER CONFIRM]` / `[DATA NEEDED]` → remove the marker, keep only what is known, add
   an `[[owner_items]]` entry (what the owner must confirm or supply). `[LINK NEEDED]` → plain
   text, logged under REMAINING FOR HUMAN.
3. Add `[[owner_items]]` entries for: an H1 change (old → new), every „ти“ → „Вие“ conversion of
   a heading or CTA (one entry listing them), every example scenario kept (confirm the label),
   and anything the Brand Gate listed under OWNER ITEMS.
4. Assemble `content/<slug>.md` from the template: `title`, `meta_description`, `h1`, `slug`,
   `locale`, `primary_keyword` (exactly the keyword-map term), `secondary_keywords`,
   `status = "draft"`, `last_updated` = today, `[[sections]]` in page order (id, heading, kind,
   dictionary_key), `[[faq]]`, `[[sources]]`, `[[owner_items]]`; then the body, one
   `## <heading> {#<id>}` block per `[[sections]]` entry, same order.
5. Self-check and record results in `06-verification.md`:
   - TOML parses (`python3 -c "import tomllib; …"`, Python ≥ 3.11);
   - `title` ≤ 60 characters incl. ` | BizGrow`, no em-dash; `meta_description` 120–160 characters
     and contains the primary keyword (or a natural grammatical variant);
   - `primary_keyword` equals the keyword-map term for this address; placed once each in title,
     H1, first 100 words and one H2;
   - every `[[sections]]` id has exactly one body block with the same id and heading, in order;
     EN page ids equal the BG pair's ids;
   - zero `—`; zero bracketed markers in the body or front matter values; zero „ти“ forms (BG);
     zero banned claims or hype words (site-rules.md §2); zero PRICE/OFFER/TESTIMONIAL matches;
   - every number is canon, labelled as an example/estimate, or backed by `[[sources]]`;
   - every example scenario carries its label;
   - every `00-inventory.md` item present (list item → quote);
   - every link in `conversion-links.md`; every token from the current page still present; CTAs
     use `{{BOOKING_URL}}` / `{{EMAIL}}`.
   Any failure → fix at the stage that caused it and re-run forward; never patch here.
6. `06-verification.md`: RESOLVED-TO-OWNER-ITEMS (claim, URL, quote), REMAINING FOR HUMAN,
   PORTING NOTES (which dictionary keys change, any new keys the `Dictionary` type in
   `site/src/i18n/types.ts` would need), self-check table, counts (`new facts: N`,
   `owner items added: N`).
