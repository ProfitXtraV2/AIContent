# 07 — Gemini Step-7 external check, pass 1 (Plinko)

Command: `python3 scripts/gemini_check.py VsichkiKazina/articles/2026-09-20-plinko/05b-final-draft.md`
Model: gemini-3.1-pro-preview · Exit 0

## Verbatim verdict
**Verdict: Shows AI patterns, 80% confidence** → human-likeness = 100 − 80 = **20**. Needs changes.

Highly informative and factually flawless, but shows structural/stylistic LLM hallmarks: symmetrical parallelisms, didactic signposting, "deceptive simplicity" hook. Facts/figures/RG/disclosures bypassed and left intact.

### Flagged recommendations (style-only)
1. **"Deceptive simplicity" hook** — *"Простият вид лъже: отдолу стои чиста статистика."* Remove the dramatic personification; transition directly into the mechanics.
2. **Didactic signposting / meta-commentary** — *"Тук е най-честото недоразумение."* and *"Погледнато по този начин, бутонът за риск е избор на волатилност..."* Delete the announce-what-I'll-explain and the self-summary; let the point stand.
3. **"Not X, but Y" wrap-up** — *"Това не е лош късмет, а формата на самата дъска."* Integrate into the binomial explanation instead of a standalone punchline.
4. **Symmetrical parallelism** — *"Търсиш ли дълга игра... Гониш ли върха от 1000x..."* Break the mirrored "Verb + ли + condition" rhythm; use different sentence structures.
5. **Preachy metaphor** — *"...а не число, върху което да строиш плана си за вечерта."* Ground it: hitting the max multiplier is a statistical outlier, not to be expected in a normal session.

## Decision
human-likeness 20 < 80 → apply recs via fresh Humaniser pass (step-7b), preserve every untouchable (numbers, links, RG, 18+, disclosures, dates, byline, brand). Then re-check. Record best-seen.
