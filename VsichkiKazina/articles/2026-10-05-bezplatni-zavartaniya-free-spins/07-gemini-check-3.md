# 07 — GEMINI CHECK · pass 3 (after humaniser pass 2) · vk-0259
Model: gemini-3.1-pro-preview (ONLINE, exit 0). Target: 05b after humaniser pass 2.

## NORMALIZED SCORE
Verdict: „Shows AI patterns, 85% confidence." → human-likeness = 100 − 85 = **15** (< 80).

## KEEP-BEST DECISION (loop ended — MAX_GEMINI_PASSES = 2 reached)
Human-likeness across the loop: initial **30** → humaniser pass 1 **25** → humaniser pass 2 **15**.
Highest = INITIAL DRAFT (HL 30). Per keep-best, the final 05b is restored to the initial-draft version.
The two humaniser passes LOWERED the score each time: this is the documented high-variance/noisy
detector on a didactic casino topic (queue history: HL swings 15↔85 on identical didactic content,
goalposts relocate each pass). gemini column = `ai 70` (initial verdict „AI patterns 70%" → HL 30).
Note: pass-3 even flagged the brand-REQUIRED illustrative-number hedge („Числата тук са примерни…")
and the brand's reader-question heading style as „tells" — these are brand doctrine and are NOT removed.

## GEMINI VERBATIM VERDICT + RECOMMENDATIONS
**Verdict: Shows AI patterns, 85% confidence.**

While this article is well-structured and contains accurate, responsible gambling information, it exhibits several classic hallmarks of LLM generation. Specifically, it suffers from literal English-to-Bulgarian translation artifacts, conversational signposting in the headings, and the classic "didactic loop"—where the AI repeats the same "moral of the story" multiple times across different paragraphs.

### 1. Translated Idioms & AI Grammar Slips
* "Вървят и срок на валидност от няколко часа до седмица..."
* "Завъртанията без депозит са най-стегнати по всички тези линии наведнъж..."
* "...и точно там се крие цялата оферта."
Recommendation: use "Има и срок на валидност..."; replace "стегнати по всички тези линии" with "имат най-строги условия"; smooth the intro to "и точно там е уловката."

### 2. Didactic Repetition (The "Moral of the Story" Loop)
* Section 2: "...са две различни неща, които нямат много общо."
* Section 5: "...и почти винаги са по-малко щедри, отколкото звучи броят завъртания."
* Section 6: "Тези няколко реда казват повече от броя завъртания в заглавието."
* Section 6: "По-полезно е да провериш условията в дребния шрифт, отколкото да броиш завъртанията в банера."
Recommendation: keep the advice in the final section; trim the redundant warnings in Sections 2 and 5.

### 3. Conversational Signposting in Headings
* "Видовете, които ще срещнеш" / "Печалбата е бонус пари, не твои пари още" / "Таван на теглене: колко реално излиза"
Recommendation: tighten headings, e.g. "Видове безплатни завъртания", "Разликата между печалба и реални пари".

### 4. Over-Hedging
* "Числата тук са примерни; реалните стоят в условията на конкретната оферта..."
Recommendation: delete — the heading and the infographic caption already say the numbers are examples.

*Note on Compliance:* The responsible gambling language, 18+ markers, and affiliate disclosures are perfectly placed. Do not alter or remove them.

## DISPOSITION
Loop ended at the cap. Recommendations NOT applied: rec 4 targets a brand-REQUIRED illustrative-number
hedge (compliance — kept); rec 3 targets the brand's „real reader question" heading style (brand doctrine
— kept); recs 1–2 are plausible polish but applying another pass carries regression risk and the score has
only fallen with each pass. Keep-best restores the initial draft (HL 30). No further edits.
