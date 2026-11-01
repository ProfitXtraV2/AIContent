# Step 7 — Gemini external check, pass 1 (initial draft)

**Script:** `python3 scripts/gemini_check.py 05b-final-draft.md`
**Normalized human-likeness:** 75 (verdict "Likely human-written, 75% confidence" → HL = 75)
**Result:** BELOW target (GEMINI_TARGET_CONFIDENCE = 80) → iterate with a humaniser pass.

## Gemini verbatim verdict + recommendations

**Verdict: Likely human-written (or heavily human-edited), 75% confidence.**

This text is highly idiomatic and contains cultural nuances that LLMs rarely generate organically in Bulgarian (e.g., „цял живот спориш кой как ги разбира“, „колкото и да ти отърва“, „за една ракия“). The vocabulary is rich and natural („другояче“, „похлупваш“).

However, the structural scaffolding of the article—how it transitions between paragraphs and introduces topics—retains several classic AI copywriting habits. It reads like a human expert wrote it, but perhaps relied on an AI-generated outline, or a human writer who has unconsciously adopted SEO/AI writing patterns.

Here are the specific patterns that trigger AI detection filters, along with actionable recommendations to smooth them out.

### 1. Signposting (Announcing the structure)
AI models struggle with organic transitions, so they constantly tell the reader what they are about to do before doing it.
*   **Flagged text:** *"По-долу минаваме първо обикновената табла изцяло, а след нея двата варианта."*
*   **Flagged text:** *"Оттук нататък говорим за обикновената табла."*
*   **Recommendation:** Delete these meta-sentences entirely. Your H2 subheadings already do the heavy lifting of guiding the reader. You don't need to announce the structure; just let the text flow directly into the explanations.

### 2. Translated Idioms (Anglicisms)
LLMs often translate English idioms literally into Bulgarian, creating phrases that are grammatically correct but stylistically awkward.
*   **Flagged text:** *"Думата е чадър за няколко."* (A literal translation of the English "umbrella term").
*   **Recommendation:** Replace this with a natural Bulgarian equivalent. Suggestion: use „събирателно понятие“ or rephrase to something like „Под това име се крият няколко различни игри.“

### 3. The "Bow-Tie" Wrap-Up (Summarizing the obvious)
AI hates leaving a paragraph without a concluding thought. It frequently tacks on a dramatic summary sentence at the end of a section to tie it up with a neat little bow.
*   **Flagged text:** *"Затова изложеният пул е постоянен риск: едно хвърляне отсреща и той се връща чак в началото на пътя."* (At the end of the "Удряне, блот и бар" section).
*   **Recommendation:** Remove this sentence. The previous sentences already perfectly explain the mechanics of hitting a blot and going to the bar. The reader understands the risk; you don't need to summarize it for them.

### 4. Narrated Emotion / Exaggerated Engagement
To make dry instructional text sound "engaging," AI often injects artificial drama or tells the reader how they should feel about a specific rule.
*   **Flagged text:** *"И тук идва правилото, което обърква начинаещите повече от всичко друго: длъжен си да изиграеш всички ходове..."*
*   **Recommendation:** Soften the dramatic setup. Instead of narrating the confusion of beginners, just state the rule directly with a slight emphasis.

### 5. Staccato Rhythm in Definitions
AI sometimes defaults to overly short, robotic sentences when defining win conditions or basic rules, breaking the otherwise conversational flow.
*   **Flagged text:** *"Пръв извадил всичките петнайсет пула печели. Обикновено една точка. Марс е двойна игра."*
*   **Recommendation:** Combine these fragmented thoughts into a more fluid, human sentence.

***

**A note on the disclosures and Responsible Gambling language:**
The author bio, affiliate disclosures, and 18+ warnings at the bottom are perfectly formatted, legally compliant, and appropriately placed. Do not touch or alter these sections in any way.
