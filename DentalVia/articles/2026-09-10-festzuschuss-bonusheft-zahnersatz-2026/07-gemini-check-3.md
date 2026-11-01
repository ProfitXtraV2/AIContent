# Step 7 — Gemini cross-model check · Pass 3 (after Humaniser pass 2) — FINAL

Model: gemini-3.1-pro-preview · run 10.09.2026 · input: 05b-final-draft.md (post humaniser pass 2)

## VERDICT
**Shows AI patterns, 75% confidence.** → Normalised human-likeness = 100 − 75 = **25** (unchanged).

## KEEP-BEST DECISION (MAX_GEMINI_PASSES reached)
Human-likeness across the loop: initial 05b = 25 · humaniser pass 1 = 25 · humaniser pass 2 = 25.
Tied at 25 across all three. Per keep-best, the highest-scoring version is kept; the pass-2 version is
retained (it removed the most genuine tells — the numeric signposting, the "Angenommen" setup, the
chiasmus, the glossary rhythm, and the regurgitated recap section — with no loss of facts, flags, links,
or compliance). Queue `gemini` column = **ai 25** (ended below the 80 target after the 2-pass cap).

## WHY THE SCORE DID NOT MOVE (for the human)
Gemini explicitly names the inline [VERIFY] tags as an "AI-assisted drafting" signal and reads the
verbatim medical-disclaimer + mediation-transparency boilerplate and the didactic explainer rhythm of an
insurance guide as AI tells. These are pipeline requirements that must NOT be removed to satisfy a
detector; detector scores are noisy and further editing would strip the coordinator voice. The loop was
stopped at the cap. Human Step-6 review owns the final call.

## PASS-3 RESIDUAL (recorded, not actioned — cap reached)
Didactic rhythm; slightly over-polished transitions; a "call-to-action wrap-up" read at the CTA. The CTA
block and both compliance lines are mandatory and stay verbatim.
