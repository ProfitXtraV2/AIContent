BRAND COMPLIANCE SCORECARD — hub-intro: Отговорна игра (/blog/responsible-gambling/)
Verdict: PASS
Total: 92/100
Personality 19/20 | Tone 14/15 | E-E-A-T 18/20 | Trust signals 12/15 | Language&Style
15/15 | RG 14/15

CRITICAL (blocks publish): none.

MODERATE:
- Trust-signal checklist items designed for full articles (pub/updated dates, About
  boilerplate slot, author bio slot, affiliate-disclosure footer) are template-level for
  a hub-intro: the hub-intro spec caps the body at 350–500 words with no H1/images/FAQ,
  meaning this content is inserted into the category page's existing template, which
  carries its own byline/date/footer chrome (meta.json's author field is hard-set to
  "Георги Тодоров" by the publisher regardless of body content — see scripts/build_feed.py
  AUTHOR constant). Scoped decision, not a defect: the ONE body-level trust item that
  belongs in the prose itself — the verbatim RG marker line — IS present. The Betano
  link is a plain on-site internal link per the task brief (not an affiliate redirect),
  so the affiliate-disclosure-footer and affiliate-links.md registry checks do not apply
  to this row.
- No maths/превъртане/RTP figures appear in this piece (topic doesn't call for any), so
  the "recalculate the numbers" E-E-A-T check has nothing to verify — not a gap, just not
  applicable to this content.

VERIFY QUEUE (route to human): none — no [VERIFY]/[DATA NEEDED] flags, no operator-
specific or time-sensitive claims requiring sourcing.

VOICE NOTES (protect during fixes): editorial/solidarity register throughout; the single
disclaimer negation ("не е препоръка ..., а илюстрация") is the one permitted use of that
construction, required by the brief to frame Betano as non-promotional — do not remove or
duplicate it elsewhere.

FACT & CLAIM SWEEP: no unverifiable operator/regulator claims; no tax claims; no invented
licence numbers; no claim about the site's own affiliate-licence status (not applicable,
plain internal link); no surviving [DATA NEEDED] flags; jurisdiction (България/НАП) named
on every regulatory mention.

PASS ≥ 85 with zero criticals — met. No Phase 2 fixes required.

═══════════════════════════════════ STEP 5b — LIGHT HUMANISER RE-CHECK ═══════════════════════════════════
Scanned for: em-dashes (none found — zero, correct), signposting lead-ins (none),
banned AI connectives (none), over-polished tables (none exist), excessive bullet lists
(none exist — the warning signs are woven into one sentence, not a list), other tells
(no perfectly parallel triads, no balanced both-sides closer, no generic-noun-colon-
qualifier headings, no identical paragraph lengths, no hedge-stacking).
Nothing in items 1–6 applies. Article returned UNCHANGED from Step 4/5's body.

Body word count (verified by direct diff against 02-draft.md and 04-seo.md): 358 words,
0 words/facts/links changed since Step 2 — confirms no number/fact drift across any
text-editing stage (Synthesis had no numeric facts to begin with; none were introduced).
