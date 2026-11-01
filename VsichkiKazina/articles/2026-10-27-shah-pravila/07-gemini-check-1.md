# Step 7 — Gemini check, pass 1 (baseline 05b) — vk-0300

Script: `python3 scripts/gemini_check.py VsichkiKazina/articles/2026-10-27-shah-pravila/05b-final-draft.md`
Date: 2026-10-27 · Exit: 0

## Normalized result
- Verdict: **Likely human-written, 80% confidence** → **human-likeness = 80**.
- PASS test: human-likeness 80 ≥ GEMINI_TARGET_CONFIDENCE (80) → **PASS**.
- Keep-best: this is the baseline and it passes; no humaniser pass run (a pass can only lower a
  noisy detector that already clears the gate, as seen on prior runs). Final 05b = baseline.
- `gemini` column: **human 80**.

## Gemini verbatim verdict + recommendations

**Verdict: Likely human-written (or heavily human-edited), 80% confidence.**

This article reads very naturally and features excellent, colloquial Bulgarian phrasing that LLMs rarely generate organically (e.g., "спорят на масата", "гола дама", "заварва почти всеки неподготвен"). The transition from chess to the site’s core topic (gambling/casinos) is handled with a deft, human touch.

However, the text still exhibits a few structural "tells" typical of AI generation—specifically in how it opens and closes paragraphs. It feels like a human writer who either used AI for an initial outline/draft and polished it heavily, or a human who has unconsciously adopted some LLM formatting habits.

### 1. Pattern: The "Wrap-up Bow" (Micro-summaries)
- Flagged: "Запомните това и никога няма да объркате коя от двете централни фигури къде е."
- Flagged: "Тази е причината една невзрачна пешка в края на играта често да решава всичко."
- Flagged: "Отдолу стои простото житейско правило: не давайте по-скъпа фигура за по-евтина без ясна причина."
- Rec: delete these micro-summaries; end on the actual rule.

### 2. Pattern: Formulaic Setup & Staccato Imperatives
- Flagged: the „Пет навика" block (Борете се / Извеждайте / Рокирайте / Дръжте …).
- Rec: make it a real list; soften rapid-fire imperatives into descriptive advice.

### 3. Pattern: The Cinematic/Dramatic Sign-off
- Flagged: "Правилата се учат за един следобед… Седнете и играйте."
- Rec: tone down; merge into the preceding paragraph.

Note on hard rules: RG language, 18+ markers, author bio, affiliate disclosures perfectly placed; no changes recommended there.

## Disposition (keep-best, loop ended by PASS)
Loop ends on PASS at the baseline (human 80). The three recommendations are style/taste notes
left for the human Step-6 editor; facts, links, RG and disclosures are clean. No humaniser pass
applied, so the published 05b stays the highest-scoring version seen (baseline, human 80).
