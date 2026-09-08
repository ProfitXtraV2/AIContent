# 07 — Gemini external check · pass 1 (initial 05b)

Model: gemini-3.1-pro-preview · run 2026-09-08 · article: 2026-09-08-keno-pravila
Verdict normalization: "Likely AI-written, 85%" → **human-likeness = 100 − 85 = 15** → needs changes.
Assessment: these recs are largely legitimate and brand-compliant (the "casino floor" calque, signposting lead-ins, narrated-emotion wrap-ups, and the pros/cons seesaw conclusion are all things the Brand Gate itself flags). Apply the compliant subset via a FRESH Humaniser pass; KEEP the [VERIFY] flags (Gemini agrees they stay).

## Gemini verbatim verdict + recommendations

**Verdict: Likely AI-written (or heavily AI-generated and lightly edited), 85% confidence.**

While the text is highly coherent and does a good job of avoiding the most obvious robotic clichés (like "В днешно време" or "В заключение"), it exhibits several sophisticated LLM writing patterns. The most glaring giveaways are literal translations of English casino idioms, heavy use of conversational signposting, and overly dramatic, "gritty" paragraph wrap-ups that GPT-4 often uses when prompted to write in an engaging or expert tone.

Here is the breakdown of the patterns that triggered this assessment, along with actionable recommendations.

### 1. Literal Translation of English Idioms (AI Localization Quirk)
LLMs process concepts in English and translate them into the target language. Here, the AI has literally translated the English casino term "casino floor" (the main gaming area) into Bulgarian.
*   **Flagged text:** "...цената, а при кено тя е сред най-високите **на целия под**."
*   **Flagged text:** "Сравнението с останалата част **на пода** е това, което боли."
*   **Recommendation:** Change "на целия под" and "на пода" to natural Bulgarian phrasing. Native speakers would say "в цялото казино", "в игралната зала", or "сред всички казино игри".

### 2. AI Signposting and Hand-Holding
LLMs rarely just give an example or explain a concept; they feel the need to announce that they are about to do so. This creates a predictable, pedantic rhythm.
*   **Flagged text:** "Един прост пример. Играеш pick-8 за €1..."
*   **Flagged text:** "Ето какво значи това на практика. Два автомата за кено стоят един до друг..."
*   **Recommendation:** Delete the signposting sentences entirely. Jump straight into the action. For instance, just start with "Ако играеш pick-8 за €1..." and "Представи си два автомата за кено един до друг...". This makes the text punchier and more human.

### 3. Over-Polished, Dramatic Wrap-Ups (Narrated Emotion)
When prompted to write engagingly, AI often ends paragraphs with slightly poetic, philosophical, or overly dramatic summaries. It tries too hard to sound like a gritty, seasoned expert.
*   **Flagged text:** "Затова първото практично нещо при кено е скучно, но спасително..."
*   **Flagged text:** "Една щастлива серия не отменя предимството, тя просто идва преди сметката."
*   **Recommendation:** Tone down the dramatic flair. "Скучно, но спасително" is overly stylized; just state that checking the paytable is essential. The phrase "идва преди сметката" sounds like a line from a movie rather than a casino guide—simplify it to state plainly that short-term luck doesn't negate the long-term mathematical edge.

### 4. Formulaic "Pros vs. Cons" Conclusion Structure
The final section follows the classic LLM summary formula: acknowledge the appeal (Pros), reiterate the danger (Cons), and deliver a final moralizing verdict.
*   **Flagged text:** "Кено е лесно за схващане и може да е забавно заради шанса за голям множител от малка сума. Точно този голям множител го прави притегателно и точно той крие високата цена, защото зад него стои вероятност, близка до нулата."
*   **Recommendation:** Break this formulaic recap. You don't need to summarize the entire article again in the final heading. Convert this section into a direct, practical tip about bankroll management without the "It's fun but expensive" seesaw structure.

### Process Note regarding `[VERIFY]` tags:
*   **Flagged text:** `[VERIFY: диапазонът 60%–95%...]` and `[VERIFY: тези стойности са приблизителни...]`
*   **Observation:** These tags are still present in the text. Per your instructions, I am not suggesting you remove them, but their presence in a "finished, human-verified article" is a major process issue. It indicates that raw AI output (or editor notes) bypassed the final proofreading stage.

## Decision
hl 15 < 80 → iterate. Apply recs 1–4 via a FRESH Humaniser pass (step-7b): fix the "под" calque (→ native BG), delete the two signposting lead-ins, de-dramatize the two wrap-ups, break the seesaw conclusion into a direct bankroll tip. KEEP both [VERIFY] flags in the text (Gemini agrees). Preserve every number/range, link, RG line, 18+, disclosure, date, byline, brand. Then re-check; keep the highest-hl version.
