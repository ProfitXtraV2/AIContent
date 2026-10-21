# Step 7 — Gemini cross-model check · Pass 3 (after Humaniser pass 2) — FINAL

Model: gemini-3.1-pro-preview · run 10.09.2026 · input: 05b-final-draft.md (post humaniser pass 2)

## VERDICT
**Shows AI patterns, 75% confidence.** → Normalised human-likeness = 100 − 75 = **25** (unchanged vs pass 1).

## KEEP-BEST DECISION (MAX_GEMINI_PASSES reached)
Human-likeness across the loop: initial 05b = 15 · humaniser pass 1 = 25 · humaniser pass 2 = 25.
Highest seen = 25 (pass 1 and pass 2 tied). The pass-2 version is kept — it carries all of pass 1's gains
(de-numbered headings, flattened metaphors, broken symmetry) plus pass 2's (condensed cosmetic-exclusion,
punchier noun headings, dropped generic wrap-up), with no loss of facts, flags, links, or compliance, and
without any first-person „ich" or added list. Queue `gemini` column = **ai 25** (below the 80 target after
the 2-pass cap).

## WHY THE SCORE HELD AT 25 (for the human)
Two of Gemini's repeated recommendations could NOT be applied without breaching the brand/pipeline rules,
and they cap the score:
- It repeatedly asks to inject a first-person author voice („Aus meiner Erfahrung … rate ich …"). The
  DentalVia author rules forbid „ich" as a default voice and any first-person experiential claim.
- It asks to convert a deductions passage into a bullet list. The pipeline REDUCES lists and never adds them.
The residual read is otherwise driven by the required inline [VERIFY] flags, the verbatim compliance
boilerplate, and the inherently procedural rhythm of a tax how-to. Detector scores are noisy; over-editing
would strip the voice or breach compliance, so the loop stopped at the cap. Human Step-6 review owns the call.
