# Step 7 — Gemini cross-model check · PASS 1 (baseline draft = post-5b)

**Script:** `python3 scripts/gemini_check.py 05b-final-draft.md`
**Input version:** 05b after Brand Gate (pass 0 / baseline)

## Verdict (verbatim)
**Shows AI patterns, 70% confidence.** → human-likeness = 100 − 70 = **35**

While the text is exceptionally clean, avoids the worst AI clichés (e.g., "В днешния дигитален свят"), and uses some excellent, natural-sounding colloquialisms ("теглене не минава", "няма да опрете до затворена врата"), its underlying skeleton gives it away. The article relies on formulaic structural patterns, didactic transitions, explicit signposting, and a classic "neat bow" summary at the end.

## Flagged passages
1. **Explicit signposting / meta-commentary** — „Тази статия остава при акаунта, парите и графика." (narrates editorial scope).
2. **Formulaic summary** — the „Накратко" heading + paragraph that lists the subheadings (registration, payments, betting windows, auto-payout).
3. **Didactic filler transition** — „Последицата е съвсем осезаема." (narrated impact before the consequence).
4. **Stilted/dictionary opener** — „Залагането онлайн започва с регистрация и потвърждаване на самоличността." (truism opener).

## Concrete recommendations (style-only)
- Delete „Тази статия остава при акаунта, парите и графика." (links do the job).
- Remove the „Накратко" heading + the two summary sentences; move the final punchy warning („Когато някъде ви обещават „по-изгодно"… глоба от 500 до 2000 лв.") to the end of the „Фалшивите „тото" сайтове" section, so the article ends on a strong note, not a recap.
- Delete the filler transition „Последицата е съвсем осезаема."; start directly with „Домейн, който работи днес…".
- Cut the opening truism in „Регистрация и верификация…"; start with „БСТ събира и проверява данните…".

## Process note (from Gemini)
The `[VERIFY: данъчен режим…]` flag, the 18+ RG block, and the affiliate disclosures survived to final stage; Gemini explicitly recommends NO changes/removals to them (legally/ethically necessary). All untouchables preserved.

## Decision
HL 35 < 80 → iterate: apply the style recs via a fresh Humaniser pass (step-7b), preserving every untouchable, then re-check (pass 2). Keep-best across baseline + passes.
