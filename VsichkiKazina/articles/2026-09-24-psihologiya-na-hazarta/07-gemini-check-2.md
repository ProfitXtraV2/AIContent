# Gemini Step-7 external check — pass 2 (after Humaniser pass 1)

Command: `python3 scripts/gemini_check.py 05b-final-draft.md`

**Verdict: Shows strong AI patterns, 80% confidence.** → human-likeness = 100 − 80 = **20**

Marginal gain from pass 1 (15 → 20). Detector remains harsh on this behavioural-science topic. New flags identified for pass 2 humaniser:
1. "Not X, but Y" faux-profound contrasts in intro and conclusion (one was introduced by the pass-1 edit) → remove.
2. Robotic SEO link shoehorning ("генератор, чиито понятия…" awkward; closing 3-link wrap-up) → integrate organically, trim the closing link dump.
3. Dramatic pivot "Това не е случайност в дизайна." → delete, merge.
4. Meta-summary transition "Тук работят наведнъж всички капани отгоре." → drop, show the combination narratively.
5. Over-symmetrical pacing → add sentence-length variance.

All untouchables preserved; em-dash 0. → apply Humaniser pass 2 (final, MAX_GEMINI_PASSES=2).
