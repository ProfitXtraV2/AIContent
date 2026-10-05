# 07 — Gemini check, pass 1 (vk-0039)
Model: gemini-3.1-pro-preview · Verdict: **Shows moderate AI patterns, 65% confidence** → human-likeness = 35.

Flagged patterns:
1. Empathic staccato / forced relatability: „...без да качва документи. Разбираемо е. Само че при казината..." — validate-then-pivot.
2. Mechanical signposting: „Целта е двойна. От една страна... От друга..." — symmetrical buckets.
3. Translated English idiom: „...се връщат на масата" (back on the table).
4. Balanced wrap-up conclusion: „Ако искаш... Ако ще залагаш..." + poetic „чистият път".

Recommendations: soften intro (drop „Разбираемо е. Само че"), remove one-hand/other-hand framing,
localize the idiom, rewrite conclusion away from „Ако...Ако..." balance, replace „чистият път".
RG/18+/bio/affiliate: perfect — do not alter.

DECISION: HL 35 < 80 → apply step-7b Humaniser pass (style only; preserve all facts/links/RG/dates).
Initial-draft HL recorded = 35 (keep-best baseline).
