# 07 — Gemini check, pass 1 (initial 05b)

Model: gemini (scripts/gemini_check.py) · run 24.10.2026 on 05b-final-draft.md (initial draft).

## Verdict (verbatim)
**Verdict: Shows strong AI patterns, 90% confidence.**

Normalised human-likeness = 100 − 90 = **10**. Below GEMINI_TARGET_CONFIDENCE (80) → iterate (humaniser pass 1 via step-7b).

While the Bulgarian grammar is flawless and the rules are clearly explained, the structural rhythm of the article is a textbook example of LLM generation. The text relies heavily on formulaic signposting, over-dramatized transitions, and "fortune-cookie" aphorisms to string facts together. It reads like a machine trying to inject "engaging human flavor" into a dry rulebook.

### 1. Formulaic Signposting (The "Setup + Colon" Crutch)
AI models love to introduce a concept with a slightly dramatic or summarizing clause, drop a colon, and then deliver the actual information. This article uses this exact syntactic structure in almost every single paragraph.

Flagged Passages:
- "Точкуването стъпва изцяло върху стойността на картите, затова ги запомнете отрано:"
- "Тук се крие и обрат, който често преобръща резултата:"
- "Ходът върви по проста рамка:"
- "Черните тройки са спиращи карти:"
- "Прагът расте заедно със сбора на отбора:"
- "Скритото излизане е по-ефектният вариант:"
- "Сметката за едно раздаване върви в една посока:"
- "Канаста има много лица и маси се спорят точно по тях, затова уговорете правилата, преди да седнете:"

Recommendation: Break this repetitive rhythm. You do not need to announce that you are about to explain a rule before explaining it. State the mechanics directly; remove the filler setups and start those paragraphs with the actual content.

### 2. Narrated Emotion and Over-dramatization
To make dry instructions sound "engaging," LLMs often assign emotions, temptations, or dramatic weight to inanimate objects or basic game mechanics.

Flagged Passages:
- "Купът с изхвърлените карти идва наведнъж и затова примамва, но достъпът до него е ограничен със сериозни условия."
- "Върху това стои и отделен слой, замразяването."
- "Тук се крие и обрат, който често преобръща резултата:"

Recommendation: Strip the artificial drama. The discard pile doesn't need to "tempt"; the rules don't need "serious conditions" or "separate layers." State the mechanics plainly.

### 3. AI Aphorisms and Philosophical Framing
LLMs frequently wrap up sections or introduce topics with balanced, slightly preachy, "profound" statements. They love the "Not just X, but Y" structure and neat little concluding idioms.

Flagged Passages:
- "Целта обаче не е просто да „излезеш“ от раздаването, а..."
- "Нито една от тези версии не е грешна, просто е различна..."
- "Една минута уговорка в началото спестява спора в средата."
- "Канаста по рождение е семейна, социална игра: сяда се за нея заради компанията, не заради залога."

Recommendation: Cut the fortune-cookie wisdom. Remove the idioms entirely; let the content stand on its own; transition directly into the legal/real-money realities without the moralizing preamble.

(Note: The responsible gambling language, 18+ markers, and internal links at the end of the text are properly formatted and should remain exactly as they are. Do not alter them during your edits.)
