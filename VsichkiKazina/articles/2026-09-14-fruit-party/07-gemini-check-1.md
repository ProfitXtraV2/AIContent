# Step 7 — Gemini check, pass 1 (initial 05b)

Model: gemini (scripts/gemini_check.py, gemini-3.1-pro-preview). Verdict normalized:
**"Likely human-written, 85% confidence"** → human-likeness = **85** → **PASS** (≥ 80 target). Kept pass 1 (baseline HL 85). No Humaniser pass required.

One genuine GRAMMAR slip flagged (item 2) — corrected as a factual/grammar fix, not a style rewrite: heading „Как да го подходиш разумно" → „Как да подходиш разумно" (the pronoun „го" is ungrammatical with intransitive „подходиш"). No numbers, links, RG lines, 18+, dates, byline, brand or [VERIFY] flag touched. Other flagged items (style crutches) left as-is: the piece already PASSED and over-editing strips voice per keep-best.

---

**Verdict: Likely human-written (or heavily human-edited), 85% confidence.**

This text reads exceptionally well for Bulgarian casino content. It avoids the typical AI hype ("thrilling adventure," "endless riches") and instead uses grounded, highly native phrasing that AI rarely generates in Bulgarian (e.g., "разсипва на порции," "карта от петна," "едно завъртане вика следващото," "сухите серии"). The analytical tone regarding math and RTP is sharp and cynical in a very human way ("звучи като обещание, но е връх, който математиката вече е калкулирала").

However, there are a few structural crutches, minor anglicisms, and run-on sentences that occasionally mimic AI writing patterns.

### 1. The "Heart of [Concept]" Trope (Narrated Emotion / Cliché)
- Text: „Случайните множители са сърцето на вариацията" (Heading)
- Pattern: "X is the heart of Y" to introduce core mechanics.
- Recommendation: „Случайните множители диктуват вариацията" or „…са двигателят на вариацията".

### 2. The Direct Translation Anglicism (Awkward Phrasing)
- Text: „Как да го подходиш разумно" (Heading)
- Pattern: direct translation of "How to approach it"; „подхождам" is intransitive here, so „подходиш го" is a grammatical slip.
- Recommendation: remove „го" → „Как да подходиш разумно". [APPLIED — grammar fix]

### 3. The Breathless Didactic Run-On (Over-explained Warning)
- Text: „Задай си лимит за загуба и за време още преди първото завъртане и го спазвай, дори когато мрежата светне от множители, защото струпаните числа създават усещане за близка голяма печалба, а всяко следващо завъртане тръгва от същата математика."
- Pattern: 41-word five-clause sentence weaving RG advice into mechanics.
- Recommendation: keep the RG advice verbatim, break into two or three sentences.

### 4. Repetitive Logical Connectors (Signposting)
- Text: „Заради това" used three times.
- Recommendation: swap at least two („Ето защо", „По тази причина", or restructure).

Note: the [VERIFY] flag (volatility) and the 18+ / RG boilerplate were noted and bypassed per instructions; correctly placed for the editorial process.
