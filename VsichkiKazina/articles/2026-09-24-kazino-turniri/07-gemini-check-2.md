# Gemini Step-7 external check — pass 2 (after Humaniser pass 1)

Command: `python3 scripts/gemini_check.py 05b-final-draft.md`

**Verdict: (mid) reads like a solid AI draft that has received a light human edit.** Improved from pass 1 (human-likeness 15). New flags for pass 2 humaniser:
1. Formulaic signposting in "Капаните" section ("Започни с…", "Гледай и…", "Не подценявай и…", "Отвъд всичко това стои едно просто нещо:") → strip, start paragraphs directly.
2. Personification / forced metaphors ("бюджет не обича", "тих начин", "витрината, която прави турнира състезание") → literal ("изпразва бюджета", "скрит начин", drop showcase metaphor).
3. Narrated emotion "Тази динамика е и част от притегателната му сила…" → delete.
4. AI throat-clearing "Един пример с примерни числа." → "Например (числата са примерни):".

All untouchables preserved; „примерни" labels + all numbers kept verbatim; em-dash 0. → apply Humaniser pass 2 (final, MAX_GEMINI_PASSES=2).
