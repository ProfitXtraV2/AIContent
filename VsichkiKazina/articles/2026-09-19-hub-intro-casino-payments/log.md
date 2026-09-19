# Pipeline log — hub-intro-casino-payments

- 00-brief.md — assembled from pipeline/templates/00-brief-template-vsichkikazina.md with
  the backlog row's query/keywords/angle. No external web research (educational hub-intro,
  no operator-specific/time-sensitive facts). Ahrefs enrichment skipped per orchestrator.
- 01-synthesis.md — Synthesis stage (agents/synthesis.md + prompts/step-1-synthesis.md).
  0 external sources (waived by brief for this content type). Fact inventory is general
  non-operator payments domain knowledge. No [VERIFY]/[CONFLICT] flags raised.
- 01.5-outline.md — Outline/Architect stage. Structure respects hub-intro hard constraints:
  no H1, exactly 2 H2s, 350-500 word budget, varied section shapes, no signature elements
  (not a persona review).
- 02-draft.md — Author stage (pipeline/markets/bg/author.md guide/editorial register, NOT
  VOICE_BG_review.md — this is not a review). Byline Георги Тодоров per hard brand rule.
  No Протокол block, no anecdotes, no fabricated operator figures. Initial word count 388
  (within 350-500 band). Caught and fixed one "не X, а Y" paragraph-ending antithesis during
  drafting (the confirmed top BG AI-tell) before moving to Humaniser.
- 03-humanised.md — Humaniser Phase 1 evaluation: HUMAN-LIKE, 51/60. No Phase 2 rewrite
  needed (score already above the 48 HUMAN-LIKE threshold).
- 04-seo.md — SEO Copywriter stage. Audit found no flooding, no missing high-priority
  entities, all 3 required internal links already naturally anchored. Added title tag (48
  chars) and meta description (148 chars); no body wording changed.
- 05-gate-report.md — Brand Gate: PASS, 96/100, zero criticals, zero moderates requiring
  fixes. Step 5b light re-check run as a safety pass: nothing to fix (zero em-dashes, no
  signposting, no tables/lists present).
- 05b-final-draft.md — final pre-external-check text. Body word count: 388.
- Images (Step 8): SKIPPED ENTIRELY per hub-intro spec + orchestrator override — no
  images/ folder, no image stage.
- Ahrefs enrichment: skipped per orchestrator override.
- Dedup / anti-cannibalization: N/A per orchestrator override (target category page exists
  by design).
- Number diff check: no numbers appear in the body prose at all (by design — no
  operator-specific figures). The only numbers anywhere in the file are the fixed footer
  template's dates (19.09.2026) and the RG hotline number (0888 99 18 66), both from the
  unmodified brand template, identical at every stage. No drift.
- 07-gemini-check-1.md — Step 7 external Gemini check, pass 1 on the pre-Gemini 05b:
  "Shows AI patterns, 75% confidence" -> human-likeness 25 (below 80 target). Flags:
  ти/вие register mix, redundant restatement, one overloaded run-on sentence, repetitive
  closing summary, missing "със" before "закръгляния".
- content(hub-intro-casino-payments): humaniser pass 1 — applied Gemini's recommendations
  via a fresh Humaniser pass (step-7b-apply-gemini-recs.md): unified register to ти
  throughout, cut the redundant "differs by casino" restatement, split the overloaded
  reliability/support sentence into two, removed the repetitive closing summary sentence,
  fixed "с закръгляния" -> "със закръгляния". Facts, all 3 links, RG line, and disclosures
  unchanged. Quick Brand Gate re-check: still clean. Body word count 364 after the edit
  (topped up from 346 with one added sentence about checking the support channel, to stay
  within the 350-500 band without reintroducing any flagged pattern).
- 07-gemini-check-2.md — Step 7 pass 2 on the revised 05b: "Likely human-written, 85%
  confidence" -> human-likeness 85. PASS (>= GEMINI_TARGET_CONFIDENCE 80). Kept as final —
  highest score seen (25 -> 85); no further Humaniser pass needed, MAX_GEMINI_PASSES (2)
  cap not reached.
- 06-verification.md — no [VERIFY] flags (content type carries no time-sensitive/operator
  facts by design); images: none (hub-intro spec); Brand Gate 96/100; Gemini human 85
  (1 humaniser pass).

## Final state
- gemini column value for content-queue.md (added by the orchestrator): human 85
- Brand Gate: 96/100, PASS
- Final body word count: 364 (350-500 band)
- Images: none (hub-intro spec — no image stage run)
