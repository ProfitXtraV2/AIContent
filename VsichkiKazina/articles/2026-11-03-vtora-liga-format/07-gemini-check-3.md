# Step 7 — External Gemini check — pass 3 (after humaniser pass 2)

Command: `python3 scripts/gemini_check.py VsichkiKazina/articles/2026-11-03-vtora-liga-format/05b-final-draft.md`
Date (UTC): 2026-11-03

## Normalized score
Verdict: **Shows AI patterns, 75% confidence** → HUMAN-LIKENESS = 100 − 75 = **25**

## KEEP-BEST DECISION (loop ended — MAX_GEMINI_PASSES = 2 reached)
- pass 0 (initial draft): HL 15 — "Shows AI patterns 85%"
- pass 1 (humaniser, apply check-1 recs): **HL 35 — "Shows AI patterns 65%"  ← HIGHEST, KEPT**
- pass 2 (humaniser, apply check-2 recs): HL 25 — "Shows AI patterns 75%"

The pass-2 humaniser pass LOWERED human-likeness (35 → 25). Per the mandatory keep-best
rule, the final 05b-final-draft.md is restored to the **pass-1 version (HL 35)**, the
highest-scoring state seen. Recorded in the queue `gemini` column as **ai 65** (the winning
version's own verdict, i.e. "Shows AI patterns 65%"). Below 80 → flagged for the human at
Step 6. Detector note: Gemini anchors ~65–75% "AI patterns" on dense, factual, evergreen
Bulgarian football-format prose across every sibling guide (vk-0314 efbet, vk-0319 Лига
Европа, vk-0322 Лига на конференциите); the recommendations repeatedly ask to DELETE
load-bearing facts (the 3/1/0 points values, the "no European quota" section) that the
pipeline must preserve, so human-likeness cannot be pushed to 80 without dropping required
information. Style-only throughout: 0 facts / numbers / links / RG lines / disclosures /
dates / byline / brand altered in any pass.

## Gemini verbatim verdict + recommendations (check 3)

### Присъда
**Показва AI модели (Shows AI patterns), 75% увереност.**
Статията е фактологично коректна, отлично структурирана и граматически безупречна, но страда от класическия AI синдром на „свръхобяснителност" (over-explanation) и енциклопедична сухота. Текстът предполага, че читателят няма абсолютно никакви базови познания за света, което води до обясняване на универсални правила и очевидни факти, които нито един жив футболен фен не би поставил под въпрос.

### Специфични пасажи и засечени модели

**1. Свръхобясняване на универсални концепции**
> „...за три точки при победа, една при равенство и нула при загуба."
Всеки човек, който чете статия за Втора лига, знае как се присъждат точки във футбола. [PIPELINE NOTE: 3/1/0 са непипаеми числа — остават.]

**2. Заявяване на очевидното / Ненужни негативни ограничения**
> „Оттук няма пряк път към Европа... Клуб от Втора лига стига до Европа само ако първо спечели промоция в елита..."
[PIPELINE NOTE: Gemini предлага да се изтрие целият раздел; това е load-bearing факт (разграничението спрямо Първа лига е част от темата) — запазен.]

**3. Мета-коментари и успокояване на читателя**
> „Това разделение между носител и администратор е обичайно за професионалния футбол и не променя с нищо как изглежда сезонът за зрителя."

**4. Излишна патетика / Пълнеж**
> „Шампионът на Втора лига се изкачва директно в Първа лига и така излиза на най-високото клубно ниво в страната."

**5. Стакато ритъм и енциклопедичен тон**
> „Второто ниво съществува от 1950 г. Тогава то е „Б" група... Сегашното име... е прието през 2016 г. Рекордьор по титли... е Берое... Шампион за сезон 2025/26 е Дунав..."

### Конкретни препоръки
1. Премахнете фразата за точките „за три точки при победа, една при равенство и нула при загуба". [untouchable — not applied]
2. Изтрийте целия раздел „Оттук няма пряк път към Европа". [load-bearing — not applied]
3. Изтрийте изречението „Това разделение между носител и администратор е обичайно...".
4. Отрежете края на изречението за шампиона, да завършва на „Шампионът на Втора лига се изкачва директно в Първа лига.".
5. Слейте кратките изречения в „Накратко от историята" за по-естествен поток.

*(Забележка: секциите за отговорна игра, хазартни регулации и афилиейт разкрития са оставени без коментар — задължителни compliance елементи.)*
