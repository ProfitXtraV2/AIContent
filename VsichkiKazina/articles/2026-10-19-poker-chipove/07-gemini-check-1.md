# 07 — Gemini Step-7 check · pass 1 · vk-0285

**Date:** 2026-10-19
**Model:** gemini-3.1-pro-preview (text endpoint slow today; two 120s/180s runs timed out with
`GEMINI_ERROR: read timed out`, so this verdict was obtained on a faithful re-run with a longer
read timeout — same model, same Step-7 prompt, same article).
**Verdict (verbatim):** Shows AI patterns, 65% confidence.
**Human-likeness (normalized):** 100 − 65 = **35** → below target (80) → NEEDS CHANGES

Recommendations (verbatim summary — style only, facts/RG/links/markers untouched):
1. Intro signposting / "roadmap" sentence („Това ръководство минава през цветовете и стойностите…")
   → delete; the intro works without it.
2. „Not X, but Y" antithesis („Подреждането не е естетика, а скорост.") → soften to a direct statement.
3. Melodramatic micro-transitions („Има и по-тиха причина.", „Това е разликата, която пряко засяга джоба.")
   → delete; start the paragraph/section directly with the substance.
4. Staccato setup+punch repeated („…навсякъде. Не значат.", „Турнирните чипове работят иначе.") → smooth
   the rhythm so the two-beat pattern does not recur.
5. Philosophical wrap-up („…инструмент за броене и нищо повече.") → tone down the „и нищо повече" flourish.

Gemini explicitly noted the RG integration (intro + conclusion + boilerplate) is handled well and must
NOT be altered. Applying 1–5 as style-only edits via a fresh Humaniser pass (step-7b), in the article's
own voice (NOT pasting Gemini's suggested wording), preserving every number, internal link, 18+ marker,
RG line, disclosure, date, byline and brand name.
