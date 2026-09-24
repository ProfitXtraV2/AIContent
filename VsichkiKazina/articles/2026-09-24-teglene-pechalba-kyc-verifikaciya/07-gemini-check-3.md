# Step 7 — Gemini cross-model check · PASS 3
Model: gemini-3.1-pro-preview · run 24.09.2026 · input: 05b after Humaniser pass 2.

## VERDICT
**Shows AI patterns (Hybrid / Heavily Edited AI), 75% confidence** → normalized human-likeness = 100 − 75 = **25**.
Gemini noted „excellent localization" and „some highly natural, colloquial phrasing (e.g. „вместо да увисне за дни")".

## Scores across all versions (KEEP-BEST)
| Version | Human-likeness |
|---|---|
| Check 1 — initial 05b | 25 |
| Check 2 — after Humaniser pass 1 | 15 |
| Check 3 — after Humaniser pass 2 (current) | **25** |

Cap reached (2 Humaniser passes). Detector scores on Bulgarian casino copy are noisy and run low (the market dictionary records first-pass human-likeness averaging ~25 across the first 10 articles). Best human-likeness = **25**; the current pass-2 version ties the top score and is the cleanest, most-edited draft (fewest structural tells, natural colloquial markers present), so it is KEPT. No PASS ≥80 reached; logged for the human per the accept/iterate policy (do not loop indefinitely, over-editing strips voice).

## Residual patterns Gemini still flags (left for the human; not over-edited)
- „Tidy bow" closer „Тези няколко минути преди депозита спестяват дните забавяне после."
- Long comma-aggregated delays sentence.
- Symmetric „За самоличност… За адрес… За платежния метод…" framing.
- 5-step flow starts at депозит/игра (prerequisites) rather than at the withdrawal request.
These are stylistic, not compliance issues; every number, both [VERIFY] flags, the verbatim 18+ RG line/block, byline, brand and 4 internal links are intact and untouched across all passes.
