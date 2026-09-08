# Step 7 — Gemini check, pass 5 (after Humaniser pass 4)

Model: gemini-3.1-pro-preview (scripts/gemini_check.py) · temp 0.2 · recommendations only.
Normalized: **"Likely human-written (or heavily human-edited AI), 85% confidence"** → human-likeness = **85**.

## Result: PASS (≥ 80)
The structural-skeleton complaints from the baseline are gone (no more info-dump list,
no premature mid-article summary, no back-to-back glossary definitions, no matchmaker
symmetry). Remaining flags are minor line-level polish, not structural tells.

## Remaining minor flags (safe polish, no untouchables affected)
1. **Tautology/filler** — "Три карти покер се играе, както казва името, само с три карти" —
   drop "както казва името".
2. **Echoed "честният начин"** — appears in the demo section and again in the close. Vary one.
3. **Verb-root repetition** — "Ако тепърва започваш, започни с видео покер" (започваш/започни).
4. **Translated collocation** — "изборът ти реално мести числата" reads like "moves the
   needle/numbers"; use native casino-math phrasing (e.g. свива предимството / променя сметката).

Applying these in a light polish pass to raise the floor further and reduce read-to-read variance.

## Untouchables verified present and preserved (unchanged)
Numbers (RTP 98%, edge 2%, €100/€2), illustrative-numbers parenthetical, links
(/kazino-igri/, /otgovorna-igra/ ×2, /kak-ocenyavame/), RG lines, 18+, disclosures, dates
(07.09.2026), byline Георги Тодоров, brand Всички Казина.
