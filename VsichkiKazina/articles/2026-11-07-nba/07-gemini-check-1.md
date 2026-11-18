# 07 — Gemini Step-7 external check — pass 1 (BASELINE)

**Command:** `python3 scripts/gemini_check.py VsichkiKazina/articles/2026-11-07-nba/05b-final-draft.md`
**Exit:** 0

## Verdict (verbatim)
**Shows AI patterns (Likely AI-drafted with human editing), 65% confidence.**
→ Normalized human-likeness = 100 − 65 = **35**. Below GEMINI_TARGET_CONFIDENCE (80) → iterate.

The text features excellent, natural-sounding Bulgarian phrasing in several places (e.g., "няма
бонуси за стил", "се въртиш в онлайн казино", "закован рекорд"), which points to strong human
intervention or a very well-prompted output. However, the underlying *structure* of the
paragraphs—specifically the introduction, the transitions, and the conclusion—relies heavily on
classic LLM rhetorical frameworks. It reads like a human-polished text built on an AI skeleton.

### Flagged passages
1. **"Problem-Solution" thesis** — intro's final sentence „Подредиш ли тези етапи по ред, иначе
   объркващата схема става съвсем логична." Formulaic setup/resolution; tells the reader how to feel.
2. **Over-cautious disclaimer (hedging)** — „Тези числа се менят рядко, но все пак се менят, затова
   винаги си струва да ги сверяваш…" AI over-explains that facts change over time.
3. **Forced thematic bridging** — „Хазартът не носи доходи, колкото и подредена да изглежда една лига
   със своите правила и класирания." Forced „clever" literary bridge to the mandatory RG topic.
4. **"Neat bow" summary** — conclusion's „Научиш ли веднъж как върви фунията от октомври до юни,
   спираш да се чудиш…" mirrors the intro + moralizing wrap-up.

### Recommendations (style-only)
- Intro: delete the final hand-holding sentence.
- Finals: cut the hedging sentence; keep „Към есента на 2026 г." (the date stamp is enough context).
- RG: keep all RG warnings, remove the forced poetic contrast; make the first line a direct, punchy
  statement.
- Conclusion: remove the „learning journey" summary sentence; keep the abrupt final line about
  unpredictability + betting.
- (Note: disclaimers, 18+ markers, affiliate disclosures are perfectly formatted — leave untouched.)

→ Action: apply via a fresh Humaniser pass (step-7b), preserving every untouchable (numbers, links,
RG lines, 18+, disclosures, dates, byline, brand, the „към есента на 2026 г." stamp). Re-check.
