# 07 — Gemini text check, pass 1 (BASELINE draft) · vk (теглене на тото днес)

Command: `python3 scripts/gemini_check.py .../05b-final-draft.md`
Normalized human-likeness: **90** (verbatim: „Likely human-written, 90% confidence.") → **PASS** (≥ 80).

## Verdict (verbatim)
**Verdict: Likely human-written, 90% confidence.**

This article is exceptionally well-crafted and reads like the work of a seasoned human copywriter or an expert editor who has thoroughly humanized an initial draft. It lacks the typical AI hallmarks (fluff, robotic transitions, moralizing conclusions, or overly symmetrical paragraphs).

It contains highly specific, practical human knowledge that AI rarely generates without explicit prompting — such as the exact 30-minute window when the Toto website is unavailable ("онлайн сайтът на тотализатора е недостъпен за кратко... между 18:40 и 19:10 ч.") and idiomatic, natural phrasing ("Телевизионните тегления не са от вчера", "Един тираж надживява ефира си с ден"). The editorial voice is strong and opinionated ("последните числа са факт, но не са подсказка").

### Recommendations (style-only; facts/RG/disclosures/[VERIFY] untouched)
1. Didactic signposting (meta-commentary): „Затова по-долу е кога и къде е самото теглене, и къде стои последният тираж, а не кои числа са паднали." → delete; the preceding sentences already explain why numbers aren't listed, and the H2s announce the structure.
2. Repetitive conditional „Ако…" framing across several transitions → convert one or two into direct statements.
3. „Neat bow" heading „Колко струва играта и защо проверявате трезво" → simplify to be less preachy.

### Process note (NOT resolved by autopilot)
- `[VERIFY: точният канал на БНТ…]` survived into the finished text by design — human Step 6 resolves it.

## Keep-best ledger
- Baseline (pass 1): **HL 90** (PASS). Highest so far = 90.
- Action: apply the safe rec #1 (+ light #2/#3) as a humaniser pass, re-check (pass 2), KEEP the higher HL.
