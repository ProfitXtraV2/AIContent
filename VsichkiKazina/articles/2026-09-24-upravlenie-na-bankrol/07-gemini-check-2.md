# 07 — Gemini cross-model check · pass 2 (on 05b after Humaniser pass 1 / apply-recs)
Model: gemini-3.1-pro-preview (scripts/gemini_check.py) · run 24.09.2026

VERDICT (verbatim): **Shows strong AI patterns, 85% confidence.**
Normalized human-likeness = 100 − 85 = **15/100** → below 80, and LOWER than pass 1's 25 (detector noise).
KEEP-BEST so far: pass-1 baseline version = 25 is the best seen. One further Humaniser pass allowed (cap = 2).

## Gemini's flagged patterns + recommendations (verbatim summary)
1. „Not X, but Y" contrastive overuse (the top BG structural tell) — flagged five instances
   („не са спестяванията… а бюджет", „а не от парите за живот", „не е банкрол, а добро намерение",
   „Печалбата на екрана не е печалба, докато не е изтеглена", „инструмент за контрол…, не наказание").
   → change at least three to direct affirmative statements.
2. Forced/extended metaphor „съд" (vessel) for the account, reused across paragraphs → swap to
   натурал phrasing (сметка/баланс/бюджет; „стопява бюджета" instead of „изпразва съда").
3. Glossary-style opening definitions („Общият банкрол е…, а сесийният е…"; „Стоп-загубата… е…")
   → weave the meaning into the scenario, lead with the action/number.
4. Formulaic summary wrap-up in the closing section („Реши сумата и лимитите…") repeating the H2s
   → delete it; start the paragraph directly with „Трудното не е да измислиш правилата…".

Compliance strictly preserved per Gemini's own note (RG language, 18+, affiliate/licensing disclosures untouched).

Action: apply items 1–4 via a second FRESH Humaniser pass (step-7b), preserve every number/link/RG/18+/date/byline/brand,
then re-check (pass 3). KEEP-BEST across all versions afterwards.
