# 05-gate-report: /en/ (en) en-home

Step 5 Brand Gate (fresh context), 2026-11-15. Inputs: 00-current.md, 00-inventory.md,
00-brief.md, 04-seo.md (OPTIMISED PAGE, FAQ, PORT KEYS, FLAGS); rules: agents/brand-gate-bizgrow.md,
prompts/step-5-brand-gate.md, reference/site-rules.md, reference/verification-policy.md,
markets/bg/author.md (canon + B2B claim rules), markets/en/author.md, keyword-map.md,
conversion-links.md. Pair compared: articles/2026-11-15-home/content/home.md (+ home.port.json).

Mechanical checks run by script on 04-seo.md: em-dashes 0; en-dashes used as dashes 0;
exclamation marks 0; banned/hype/AI-vocabulary terms in page copy 0 (hits only in the SEO
stage's own notes); “free” only about the diagnosis (incl. “The first step is free”, current
copy, refers to the diagnosis); title 42 chars, meta description 153, ogDescription 133.

```
BRAND COMPLIANCE SCORECARD — /en/ (en)
Verdict: PASS
Total: 92/100
Voice 18/20 | Language 14/15 | Trust & claims 19/20 | Usefulness 14/15 | Anti-AI 14/15 | SEO 13/15
```

## BLOCKING CHECKS

1. NOTHING LOST: PASS. C1–C6, T1–T2, the 8 anchors, F1–F9 + footer.descriptor, N3–N8, L1
   (verbatim in #results), E1–E3 (verbatim), losses 5/5, reasons 4/4 and all UI strings are
   present. Removed items are all on the brief's REMOVE-BY-BRIEF list (N1, N2, questionnaire
   wording in step 1, four-card set incl. “Custom solutions”, losses.link, #ads). L2 “in days,
   not months” replaced by canon wording and flagged (FLAG 4), as on the bg pair.
2. FACTS ALLOWED LIST: PASS. Every statement about BizGrow is canon or flagged current-page
   copy. Line-by-line comparison with the bg pair: no English fact is missing from the bg page.
   The two wording differences from bg are brief-driven and flagged: process step 1 (“You
   describe the problems you see in your business”, no checker page; FLAG 9) and FAQ 6 sentence 2
   (“After the diagnosis, the report shows which fixes make sense for your type of business”,
   which restates the canon report with prioritised fixes; FLAG 13). No vendor, tool, team,
   price, client count, office, phone or legal data.
   **Monthly cadence for the marketing specialist (checked as instructed):** card 5 body reads
   “A real marketing specialist plans, runs and tracks your ads and reports the results to you
   with concrete numbers.” in the body and in PORT KEYS services.items[5]: no cadence. FAQ 5
   (“Your advertising is run by a real marketing specialist”) has no cadence either. The only
   monthly statements are canon: card 4 (monthly branded visuals, canon service 3), process step
   3 title and body and FAQ 7 (monthly support report, canon process 4). PASS; the cadence
   question stays an owner item (FLAG 8).
3. BANNED CLAIMS: PASS. No guarantee, ranking, traffic, savings or ROI promise; no “#1”,
   “leading”, “the best”; no price, range, discount or offer; no testimonial or client name; no
   hype word. “ai automation agency” deliberately not used (Step 4 note; consistent with bg).
4. NUMBERS: PASS. 30 min / 30-minute, 48 h / 48 hours, usually within 2 weeks / usually up to 2
   weeks (with “usually” every time), 0 obligation (canon: the diagnosis commits to nothing);
   24/7, about 10 hours, 80% only inside the labelled #results rows (FLAG 10); “Three steps” and
   step numbers are current copy. No new numbers, 0 [VERIFY].
5. HYPOTHETICAL LABEL: PASS. “Example scenarios from our method, not figures from specific
   clients.” directly above the rows in #results.
6. GDPR WORDING: PASS. Only “We work under GDPR” (#reasons). No data/GDPR FAQ (as bg).
7. REGISTER („Вие“): N/A (English page). English address is a consistent formal “you”.
8. CTA RULES: PASS. Every booking CTA uses {{BOOKING_URL}} (nav “Book a call”, hero “Free
   diagnosis”, #audit “Book a free diagnosis”, #contact “Book a video call now”); email only as
   {{EMAIL}}; one booking CTA per section; no hard-coded URL or address. “Free diagnosis” (noun
   CTA) and “Book a video call now” are inventory items C2 and C5, kept as the bg pair kept
   „Безплатна диагностика“ and „Запазете видеоразговор сега“; “now” is not scarcity wording.
9. ONE TERM PER PAGE: PASS. “ai automation for small business” exactly once each in the title,
   hero.body sentence 1 (first 100 words) and the #services H2; the H1 carries “AI automation for
   small businesses”, which is the keyword-map H1 for /en/. Also in meta description. No sibling
   main term is targeted (all siblings are Bulgarian terms; card titles have no href).
10. LINKS & ANCHORS: PASS. Section ids equal the bg pair in the same order (hero, losses,
   services, process, results, reasons, audit, faq, contact). No link to any Bulgarian page (no
   href on cards, no losses.link, no /diagnostika/), per the brief. Only same-page anchors and
   tokens. #faq is not yet in conversion-links.md (moderate 1).
11. BIZGROW VOICE: PASS. No fragments used as style (short items are list labels, card titles and
   the owner's slogan line), no rhetorical questions outside FAQ questions, no verdict lines, no
   slang, no hype, no exclamation marks. Jargon explained on first use: chatbot (“a chat
   assistant that answers…”), dashboard (“one screen with your key figures”), SEO (“search engine
   optimisation”), technical SEO (“how the site is set up for search engines”), B2B (“businesses
   that sell to other businesses”).

## CRITICAL (blocks)

None.

## MODERATE (no edit by the gate)

1. `#faq` is not listed in the Section anchors table of `BizGrow/conversion-links.md` (same
   finding as on the bg pair). For the human: register it when the FAQ component is ported.
2. Contextual body-link rule (1–3 links) is met only by same-page anchors (hero.secondary →
   #services, nav). Unavoidable under the owner's “no links to Bulgarian pages” instruction and
   because home dictionary strings render as plain text (FLAG 18). For the human.
3. Hero overlay pairs overlayLabel “Free diagnosis” with overlayUnit “usually within 2 weeks”;
   read together it can suggest the diagnosis itself takes up to 2 weeks. Identical to the bg
   pair's final port (`home.port.json`), so not changed here; raise with FLAG 4 so the owner sees
   the pairing when deciding the overlay wording.
4. Spelling is British (“optimisation”, “prioritised”, already in the current copy) while
   meta.ogLocale stays “en_US” (inventory). Not a brand defect; note for the human.
5. #services H2 “AI automation for small business, content and advertising in one place” carries
   the exact main term; the phrase order makes “content and advertising” read slightly as
   objects of “for small business”. Acceptable; changing it would break the exact-term
   placement (FLAG 16).

## PILLAR NOTES

- Voice 18/20: calm, specific, consultancy register; sentences mostly 10–22 words. Minus for
  hero.body sentence 1 (24 words) and the long FAQ 6 list sentence (accepted, mirrors bg).
- Language 14/15: plain professional English, natural rather than translated. Minus for the
  slightly keyword-shaped “provides AI automation for small business” and the H2 parse above.
- Trust & claims 19/20: canon-tight; examples labelled; client control stated (approval before
  publication, a real marketing specialist, the assistant collects the contact). Minus for the
  flagged non-canon items still awaiting the owner (platform names in card 5, example rows).
- Usefulness 14/15: concrete tasks; next steps clear (free diagnosis → report within 48 hours →
  build usually within 2 weeks → support with a short monthly report); starting costs nothing.
- Anti-AI 14/15: no em-dashes, signposting, antithesis endings or boilerplate; “in days, not
  months” antithesis already gone. Minus for the canon triad “plans, runs and tracks” (canon
  wording, kept).
- SEO 13/15: placements exact, lengths in range, first sentence states the offer, FAQ answers
  1–2 sentences and none repeats a heading. Minus for the unregistered #faq anchor and no
  contextual links (both outside copy control).

## PHASE 2

Not required (verdict PASS, zero criticals). No edits applied. The gate-passed text is the
`## OPTIMISED PAGE`, `## FAQ` and `## PORT KEYS` blocks of `04-seo.md` unchanged, with all 18
FLAGS carried. Body and PORT KEYS strings were compared and are identical (hero.body, services
items 1–6, process lead and steps, results, reasons.lead, cta, contact; meta strings equal the
front-matter values). `[OWNER CONFIRM]` count: unchanged from 04-seo.md. No source, CTA, token,
anchor, example label or flag removed; no fact or number added.

## OWNER ITEMS TO RAISE (for Step 6)

1. Title change to “AI automation for small business | BizGrow”; meta description and OG texts
   rewritten around the main term (FLAG 1).
2. H1: hero.line1 “AI automation for small businesses.” + hero.line2 “Less busywork, more
   business.” (FLAG 2).
3. hero.imageAlt reworded without the em-dash, describing the banner's English text (FLAG 3).
4. “in days, not months” → canon “usually within 2 weeks” in hero.body, overlayUnit, meta and OG;
   include moderate 3 (overlay pairing with “Free diagnosis”) (FLAG 4).
5. Hero figures 8 questions / 2 min → 30 min / 48 h / 0 obligation (FLAG 5).
6. No losses.link on /en/; losses heading reworded to mirror bg (FLAG 6).
7. Six service cards without href replacing the four-card set; “Custom solutions” dropped
   (FLAG 7).
8. Card 5 “Google and Facebook ads”: platform names not canon text (from the /reklama/
   keyword-map H1); no monthly cadence stated for the specialist's report, same as the bg gate
   decision. Owner to confirm the platforms and whether the specialist reports monthly (FLAG 8).
9. Process step 1: no questionnaire and, unlike bg, no link to /diagnostika/ (FLAG 9).
10. Example rows E1–E3 with “24/7”, “about 10 hours”, “80%” and heading “What the result can look
    like” (label kept) (FLAG 10).
11. reasons.lead rewritten to mirror bg (FLAG 11).
12. New #faq section (7 questions) + `faq` key and component; no GDPR/data question unless the
    owner supplies wording (FLAG 12).
13. FAQ 6 sentence 2 rephrased away from the Bulgarian-only checker page (FLAG 13).
14. contact.fields.name “Names” → “Name” (FLAG 14).
For the human (not owner decisions): FLAGS 15–18 (FAQ canon guards, main-term H2, port notes,
anchor-only links), moderates 1, 2 and 4; `related` not added (home Dictionary has no such key).

## VOICE NOTES (protect in later steps)

- Keep the exact main-term phrase in title, hero.body sentence 1 and the #services H2.
- Keep card 5 without any cadence (“reports the results to you with concrete numbers”).
- Keep “usually” on every 2-week mention and “within 48 hours” on the report.
- Keep the plain-word glosses (chatbot, dashboard, SEO, technical SEO, B2B).
- Keep L1 verbatim directly above the #results rows.
