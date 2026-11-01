# 07 — Gemini check · pass 1 (baseline draft)

Model: gemini (cross-model external check) · script: scripts/gemini_check.py
Verdict (verbatim): **Shows AI patterns, 85% confidence.**
Normalized human-likeness = 100 − 85 = **15**. Needs changes (< 80).

## Gemini verbatim assessment + recommendations

### Verdict
Shows AI patterns, 85% confidence.
While the text is factually dense, grammatically flawless, and well-tailored to the Bulgarian context, its narrative structure relies heavily on classic LLM tropes. It uses formulaic transitions, dramatic antithesis (contrasting two ideas for poetic effect), and philosophical "wrap-up" sentences at the end of paragraphs. It reads like a high-quality GPT-4 output that has been prompted for a journalistic tone but still leans on AI-typical narrative crutches.

### Flagged patterns
1. Formulaic transitions (signposting bridges):
   - „Доминацията у дома отвори вратата към Европа."
   - „Успехът остави и съвсем материална следа."
2. The "numbers vs reality" cliché:
   - „Числата са сухи. Подредени едно до друго обаче описват десетилетие..."
   - „Една от трибуните носи име, което обяснява духа на клуба по-добре от всяка статистика."
3. Dramatic antithesis & thematic wrapping:
   - „Това, което за повечето новаци е сезон на оцеляване, при Лудогорец стана начало на цяла епоха."
   - „Този контраст, малкият град срещу големите вечери под прожекторите, държи интереса..."
4. "Philosophical/witty" paragraph closers:
   - „Дебютът се подреди от онези, които се помнят дълго."
   - „...е от онези подробности, които никой маркетинг отдел не би могъл да измисли."
5. "Summary recap" opener before the RG pivot:
   - „Погледнат отстрани, Лудогорец е преди всичко футболна история... Следенето на футбол е едно нещо."

### Recommendations
- Cut the bridge sentences; start those paragraphs directly with the facts.
- Remove the "dry numbers" clichés; let the trophy list speak.
- Flatten the dramatic contrasts into plain statements.
- Kill the "marketing department" quip; end on the penalty-save fact.
- Streamline the gambling transition; start with the practical pivot „Ако гледате мачовете и покрай това залагате…".

(Gemini confirmed the RG/18+/affiliate blocks are compliant and left untouched — style-only recs.)
