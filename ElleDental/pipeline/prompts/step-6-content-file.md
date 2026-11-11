# Step 6 — Verification + WebPortals content file (fresh context)

Inputs: `05b-final-draft.md` (body + title + meta + FAQ + flags), `00-current.md`,
`00-inventory.md`, `reference/verification-policy.md`, `reference/site-rules.md`,
`templates/content-file-template.md`.

1. For every `[VERIFY: … — URL]`: fetch the URL, confirm HTTP 200 (`curl -sI`), quote the
   supporting passage in `06-verification.md`. Confirmed → keep the sentence, remove the marker,
   add the source to `[[sources]]` (empty `checked_by`/`checked_on`) if not already there, add a
   `[[clinical_items]]` entry (new fact, source, quote; decision fields empty). Unreachable /
   ambiguous / disagreeing → remove the sentence, log it under REMAINING FOR HUMAN.
2. For every `[DATA NEEDED]` / `[CONFLICT]` (medical) → remove the marker, keep only what is
   known, add a `[[clinical_items]]` request. `[LINK NEEDED]` → plain text, logged.
3. Add `[[clinical_items]]` entries for: each emergency-wording change (old → new), an H1 change,
   each doctor-profile fact used, and anything the Brand Gate listed under CLINICAL ITEMS.
   Keep every existing `[[clinical_items]]` entry unchanged, in its original order, first.
4. Assemble `content/<slug>.md` from the template: front matter fields as on the current page;
   `last_updated` = today; `status`, `slug`, `type`, `group`, `related`, `written_by`,
   `performed_by` unchanged; NO `reviewed_by` / `reviewed_on` / `also_reviewed_by`.
5. Self-check and record results in `06-verification.md`:
   - TOML parses (`python3 -c "import tomllib; …"`, Python ≥ 3.11);
   - title length ≤ 60 incl. ` | ELLE Dental Clinic`, contains „София“; meta ≤ 155;
   - zero `—`; zero bracketed markers in the body; zero banned terms (site-rules.md §2,
     negation rule); zero PRICE/OFFER/TESTIMONIAL matches;
   - six standard H2 patterns + exact `## Кога да се обадите веднага` + `{{URGENT_CARE}}`
     (treatment pages); botulinum rules if applicable;
   - every `00-inventory.md` item present (list item → quote);
   - every link in `conversion-links.md`; every token from the current page still present.
   Any failure → fix at the stage that caused it and re-run forward; never patch here.
6. `06-verification.md`: RESOLVED-TO-CLINICAL-ITEMS (claim, URL, quote), REMAINING FOR HUMAN,
   self-check table, counts (`new facts: N`, `clinical items added: N`, `existing kept: N`).
