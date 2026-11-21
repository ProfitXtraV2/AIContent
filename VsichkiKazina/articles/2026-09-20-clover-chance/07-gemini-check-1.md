# 07 — Gemini Step-7 external check, pass 1 (Clover Chance)

Command: `python3 scripts/gemini_check.py VsichkiKazina/articles/2026-09-20-clover-chance/05b-final-draft.md`
Model: gemini-3.1-pro-preview · Exit 0

## Verbatim verdict
**Verdict: Shows AI patterns, 80% confidence** → human-likeness = 100 − 80 = **20**. Needs changes.

"Highly informative, well-structured, free of hallucinations," but shows LLM cadence.

### Flagged recommendations (style-only)
1. **Overuse of colons/semicolons balancing clauses** — break the rhythm in: „мистерия": не можеш...; „Логиката е права:..."; „...каквато я знаеш; Clover Chance..."; „...единен RTP; всяко заглавие...". Convert some to separate sentences or natural conjunctions (а, защото); leave one or two colons for emphasis.
2. **Formulaic "X: Y" subheadings** — vary „RTP: по заглавие, не по система".
3. **[VERIFY] tags** — leave intact (intentional editorial flags; Gemini is style-only and correctly did not touch them). NOT a defect; the human resolves them at review.

## Decision
human-likeness 20 < 80 → humaniser pass (step-7b), preserve every untouchable (numbers, links, RG, 18+, disclosures, dates, byline, brand, [VERIFY]). Re-check. Record best-seen.
