# 07 — Gemini external check, pass 1 (initial draft) — Amusnet / EGT

Model: gemini-3.1-pro-preview · script: scripts/gemini_check.py
**Verdict: Shows AI patterns, 85% confidence.** → human-likeness = 100 − 85 = **15**.

## Gemini's recommendations (style-only; verbatim summary)
1. **"Not X, but Y" contrastive formula overused** — many sentences define by negation ("не за конкретна корпоративна структура", "не оператор", "не че тези правила са в твоя полза", "а не от джоба на казиното", "не гаранция", "а не абстрактен", "а не рекламния"). Convert at least half to affirmative statements.
2. **Conversational signposting / throat-clearing** — "Тук има често объркване, което си струва да изчистим.", "Има и още едно уточнение:", "Изводът от числата е практичен, а не абстрактен." Delete; start paragraphs on the core fact.
3. **Forced "what this means for you" framing** — "За теб като играч…", "За теб това значи…", "Практическото значение е…". Soften to natural statements.
4. **Formulaic AI hook** — "Ако си пускал ротативка… вероятно си играл…". Tighten; ground the opening in the provider's dominance rather than a hypothetical about the reader.
5. **Rule-of-three summary** — "същите заглавия, същата математика, само нов етикет." Break the symmetry slightly.

Process note from Gemini: flagged the surviving [VERIFY] (did NOT touch it — correct; the human resolves it at Step 6).

## Decision
Human-likeness 15 < 80 → iterate. Apply recs via a fresh Humaniser pass (step-7b), preserving every untouchable (RTP figures, EGT 2002, rebrand 2022, links, RG lines, 18+, [VERIFY], dates, byline, brand). Then re-check. Baseline human-likeness recorded = 15 (keep-best tracker).
