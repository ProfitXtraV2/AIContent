# 05-gate-report, / (home), 2026-11-11

```
BRAND COMPLIANCE SCORECARD — / (home)
Verdict: PASS
Total: 90/100
Professional voice 18/20 | Language 13/15 | E-E-A-T 18/20 | Medical safety 15/15 | Anti-AI 13/15 | SEO 13/15
```

Inputs judged: 04-seo.md (OPTIMISED PAGE), 00-current.md, 00-inventory.md, 00-brief.md,
pipeline/markets/bg/author.md, pipeline/reference/site-rules.md, conversion-links.md.
Context accepted: one-off manual run authorised by the owner on 2026-11-11 despite the PAUSED
banner (log.md); page type `home`, so the treatment-page H2 rules and urgent heading do not apply.

## BLOCKING CHECKS
1. NOTHING REMOVED: PASS. W1-W3 and N1 (112) are in FAQ Q4 verbatim. W4 („Лекарят преценява след преглед кое лечение е подходящо във Вашия случай“), W5 (risks, alternatives, decision is the patient's), W6 (anxiety, calm and unhurried, local anaesthetic when necessary), W7 (natural look) and W8 (preferred language at booking, in Part 2 and FAQ Q2) are present with the same meaning. 13/13 tokens present. 9/9 must-survive links present (L1-L9; L8/L9 through FAQ Q1). F1-F5 present; F6 kept as the one-line general mention allowed by the inventory. CI1 verbatim (front matter byte-identical to 00-current.md). 4/4 FAQs kept. Removed items are only those marked REMOVE-BY-BRIEF: the 19 treatment links (all linked by the treatment cards in `_publisher/templates/home.html`, orchestrator check after step 1) and the doctors' biography facts N3-N5, courses, interests, БЗС (still covered by CI1 and the doctor pages). Accepted as intentional.
2. URGENT BLOCK: N/A (home page). The no-emergency-number / duty doctor / 112 wording in FAQ Q4 is unchanged.
3. STANDARD SECTIONS: N/A (home page).
4. BANNED TERMS: PASS. 0 hits in title, meta, H1, body, FAQ.
5. NO PRICES / OFFERS / TESTIMONIALS: PASS. 0 hits.
6. NEW MEDICAL FACTS: PASS. None added.
7. NO INVENTION: PASS. Every fact (adults and children, same doctor for parent and child, languages, location, phone/Superdoc booking, /kontakti/ map, directions and enquiry form) comes from the current page. The Superdoc rating is correctly not used.
8. /botulinov-toksin/: N/A.
9. ADDRESSES & LINKS: PASS. Slug `home` unchanged; every link (/za-nas/, /kontakti/, /lechenie-na-karies-pri-deca/, /profilaktika-i-obuchenie/, doctor slug tokens, Superdoc tokens, tel:) is in conversion-links.md or is an existing token link; no external body links added; `related = []` kept.
10. ELLE VOICE: PASS. No fragment paragraphs, asides, verdict lines, colloquialisms, sentences opening with „И“/„Но“, or comma splices. The quick-fact lines are a list, which the brief requires.
11. FRONT MATTER INTENT: PASS. No review fields; title, meta_description, h1, slug, type, status, related unchanged; no written_by/group added (none on the current file).

## BRIEF STRUCTURE CHECK
- `<!-- more -->`: exactly once, alone on its line (body line 10). PASS.
- Part 1: 2 sentences, sentence 1 contains „дентална клиника в София“ and „зъболекарите“ (and „зъболекар“ appears again in Part 2); then 5 one-line quick facts (patients, doctors with the existing link tokens, languages, location, booking). PASS.
- Part 2: H2 „Какво да очаквате при посещение“ (W4-W7, /za-nas/) then one H2 block with {{ADDRESS_FULL}}, {{HOURS_REGULAR}}, {{HOURS_CLOSED}}, {{HOURS_NOTE}}, {{PHONE}}/{{PHONE_TEL}}, both Superdoc tokens and a link to /kontakti/ for map and directions. PASS.
- Length: 264 body words counted the same way as the 488-word baseline in the brief (headings and tokens included; 245 without the two H2 lines). PASS, near the lower edge.

## CRITICAL (blocks)
- None.

## MODERATE (optional polish; do not block)
- Part 2, para 1: „Лекарят преценява … Преди всяка процедура той обяснява …“. Both doctors are women, so the masculine pronoun reads oddly. The current page used „лекарят обяснява“ with no pronoun. Option: „Преди всяка процедура лекарят обяснява …“ (repeat the noun) or keep the text as it is.
- The language fact appears three times (Part 1 quick facts, booking block, FAQ Q2). This is acceptable because the brief keeps W8 at booking, but the booking-block sentence could be cut if the page ever needs fewer words. It cannot be cut now: that would take the body below 250 words.
- The „Местоположение“ quick fact repeats sentence 1. The brief requires it, so keep it.
- Title has no ` | ELLE Dental Clinic` suffix. Step 4 checked the publisher: build_site.py renders the title verbatim, and home, /za-nas/ and /kontakti/ all use this sentence-title pattern. Adding the suffix would make the title 70 chars. The brief also says to keep the title. Not a defect.

## CLINICAL ITEMS TO RAISE (for Step 6)
- None new. CI1 stays verbatim. Its phrase „групите лечения, изброени на страницата“ still applies, because the treatment cards on the rendered page list them.

## VOICE NOTES (protect during any later edit)
- Keep FAQ Q4 emergency wording verbatim (strictest wording: no emergency number, дежурен лекар / спешна помощ, 112 for breathing trouble or facial/throat swelling).
- Keep the calm third-person clinic voice in „Какво да очаквате при посещение“. Its sentences are complete and 12-25 words long.
- Keep `<!-- more -->` alone on its line, and keep body length ≥ 250 words.

## RESULT
PASS. Nothing to fix and no stage to send back. The page in 04-seo.md goes to Step 6 unchanged.
