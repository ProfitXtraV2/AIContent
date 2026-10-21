# 07 — Gemini external check, pass 2 (after humaniser pass 1) — Gamomat

Model: gemini-3.1-pro-preview · script: scripts/gemini_check.py
**Verdict: Likely human-written, 85% confidence.** → human-likeness = **85**. **PASS (≥80).**

## What changed since pass 1 (recs 1–4 applied via step-7b humaniser)
- Отрязан „neat bow" финал на „От наземните зали към онлайн"; абзацът свършва на факта + [VERIFY].
- Легендата на инфографиката преформулирана, за да не ехти с тялото („на или малко над него, в тесен диапазон").
- Демо/сравнение run-on разделен на две изречения; без насилен мост.
- Изтрит generic opener „Няколко игри направиха студиото разпознаваемо."; директен старт с Ramses Book.

## Residual notes (NOT applied — PASS reached; further edits optional/declined)
Gemini предложи още: (1) да махна „Първата е / Втората схема са" номерацията; (2) списък или прегрупиране на RTP dump; (3) да отрежа „нито под него, нито осезаемо над него". Рек 2 (bulleted list) противоречи на brand/humaniser prose-over-lists правилото → отклонен. Тъй като HL=85 е PASS, спираме тук (detector scores са шумни; over-editing маха глас). Keep-best: pass 2 = 85 (> pass 1 = 75) → final 05b.

## Decision
PASS. Final 05b = текущата версия (HL 85). Всички untouchables (RTP figures, 6 716×, 2008, 150+/35+/27, MGA/B2B/1066/2024, линкове, RG, 18+, двата [VERIFY], дати, подпис, марка) UNTOUCHED през паса. content-queue gemini = `human 85`.
