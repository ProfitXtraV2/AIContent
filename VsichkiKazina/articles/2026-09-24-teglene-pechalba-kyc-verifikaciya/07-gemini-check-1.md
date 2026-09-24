# Step 7 — Gemini cross-model check · PASS 1
Model: gemini-3.1-pro-preview (scripts/gemini_check.py) · run 24.09.2026 · input: 05b-final-draft.md (as delivered)

## VERDICT
**Shows AI patterns, 75% confidence** → normalized human-likeness = 100 − 75 = **25** → below 80 → apply recs via fresh Humaniser (step-7b) and re-check.

## Flagged patterns (verbatim from Gemini)
1. Relentless numerical signposting: „пет момента", „три неща", „три групи", „две неща", „три неща" (counting-signpost tell).
2. Repetitive hedging — „примерно" overload across the timelines/limits section.
3. Didactic/preachy paragraph-closers: „Ядосаните съобщения... Помага чист комплект..."; „Изрядните документи... обвиняват казиното."
4. Narrated drama / over-stylized hooks: „капан, който хваща играчите тихо"; „изяжда печалбата, за която си чакал".
5. Tautological filler: „Изборът на казино тук е практичен въпрос."; circular opening of the tax section.
Process note: two [VERIFY] tags present (timelines, tax) — Gemini correctly flags as process item, does NOT touch them.

## Recommendations to apply (fresh Humaniser pass, untouchables preserved)
- Remove counting setups („три неща", „две неща", „три групи"); state the items directly. Keep the 5-step flow list (genuine how-to sequence).
- Thin redundant inline „примерно" (keep illustrative marking via the H2 „(сроковете са примерни)", the SVG caption and the [VERIFY] flag — brand compliance requires figures to read as illustrative).
- Reframe preachy closers as plain practical statements.
- Make the pending-reversal warning objective; drop the „тихо" drama.
- Cut the tautological filler opener of the licence section; condense the tax opener.
- PRESERVE: every number, both [VERIFY] flags, verbatim 18+ RG line + RG block, byline/brand, internal links.
