# Step 7 — Gemini cross-model check · Pass 3 (after Humaniser pass 2) — FINAL

Model: gemini-3.1-pro-preview · run 10.09.2026 · input: 05b-final-draft.md (post humaniser pass 2)

## VERDICT
**Shows strong AI patterns, 85% confidence.** → Normalised human-likeness = 100 − 85 = **15** (unchanged).

## KEEP-BEST DECISION (MAX_GEMINI_PASSES reached)
Human-likeness across the loop: initial 05b = 15 · humaniser pass 1 = 15 · humaniser pass 2 = 15.
All three passes scored identically (15). Per the keep-best rule, the final 05b is the highest-scoring
version seen; the score is tied at 15, so the pass-2 version is kept (it removed the most genuine AI
tells — roadmap signposting, "kein X sondern Y" repetition, "hängt am/ab" repetition, "Fazit" framing,
recap conclusion, benchmark-narration — without any loss of facts, flags, links, or compliance).
Queue `gemini` column = **ai 15** (ended below the 80 target after the 2-pass cap).

## WHY THE SCORE DID NOT MOVE (for the human)
Gemini repeatedly attributes the "AI" read to elements the DentalVia pipeline REQUIRES and that must
NOT be removed to satisfy a detector:
- the inline [VERIFY]/[CONFLICT]/[DATA NEEDED] flags (Gemini reads them as an "unfinished draft");
- the mandatory verbatim medical-disclaimer + mediation-transparency boilerplate;
- explanatory prose around the required price-comparison tables in a data-heavy comparison article.
Detector scores are noisy and over-editing strips the coordinator voice; the loop was stopped at the
cap rather than degrading the text further. Human Step-6 review owns the final call.

## PASS-3 FLAGGED PATTERNS (recorded, NOT applied — cap reached)
1. Mechanical table summarization: "der deutsche Richtwert … steht zum Vergleich in der letzten Zeile";
   "Bei gleicher Zahnzahl … rund 1.700 € unter … / rund 3.000 € darunter." (The exact per-line savings
   vs. the named German reference are a Brand-Gate REQUIREMENT — savings must state their reference
   basis — so this is intentionally retained.)
2. Colon-drop list intros: "…sehen die Ausgangspreise pro Zahn so aus:"; three-step Ablauf rhythm.
Recorded for the human; not actioned because the cap is reached and #1 is compliance-required.
