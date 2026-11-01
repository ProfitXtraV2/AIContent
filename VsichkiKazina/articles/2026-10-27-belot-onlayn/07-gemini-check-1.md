# Step 7 — Gemini check (pass 1) · vk-0295
Command: `python3 scripts/gemini_check.py VsichkiKazina/articles/2026-10-27-belot-onlayn/05b-final-draft.md`
Date: 2026-10-27

Normalized human-likeness: **15** (saved verdict Shows AI patterns 85pct -> 100-85=15). Detector high-variance across reads this session: observed 75pct and 85pct (HL 25 and 15). BELOW gate 80 -> iterate (humaniser pass 1 applying the recs below).

## Gemini verbatim verdict + recommendations

**Verdict: Shows AI patterns, 85% confidence.**

While the article is highly informative, factually dense, and grammatically flawless, it suffers from structural and stylistic hallmarks of Large Language Models (specifically ChatGPT/Claude). The text relies heavily on meta-discourse (announcing what it will do), pedantic transitions, paragraph-level wrap-ups, and a classic "neat bow" summary at the end. 

Here is the breakdown of the specific patterns that triggered this assessment, along with actionable recommendations to humanize the copy.

### 1. Signposting / Meta-discourse
**The Flagged Text:** *"Тази страница отговаря на другия въпрос, който хората всъщност търсят: къде се играе и как се започва."*
**The Pattern:** AI models love to announce the purpose of the text rather than just delivering the information. Human writers usually trust the headline and the flow of the text to guide the reader, whereas AI acts like a tour guide pointing at the obvious.
**Recommendation:** Delete this sentence entirely. The transition from mentioning the rules to the next heading ("Безплатно, но с чипове") works perfectly without needing a meta-announcement of what the page is about.

### 2. Filler Transitions / Pedantic Clarifications
**The Flagged Text:** *"„Безплатно" тук значи точно каквото звучи, но си струва да се уточни какво стои зад него."*
**The Pattern:** The "It means exactly what it sounds like, but it's worth clarifying..." trope. AI uses these empty buffer sentences to pad the word count before getting to the actual point. 
**Recommendation:** Cut the fluff. Start the paragraph directly with the hard facts: *"В онлайн белота не залагате и не печелите пари. Масите работят с виртуални чипове..."*

### 3. Paragraph-Level Wrap-ups
**The Flagged Text:** *"Така онлайн белотът си остава социална игра и тренировка за ума; пари в него не влизат и не излизат."*
**The Pattern:** Forced conclusion. AI has a habit of treating every paragraph like a mini-essay, summarizing the point it just made in the preceding sentences using words like "Thus" (*Така*). 
**Recommendation:** Delete this sentence. The reader already knows money doesn't go in or out because you just explained how the virtual chips work. Let the facts speak for themselves without the philosophical summary.

### 4. The "Illusion of Depth" Hook
**The Flagged Text:** *"Разликата е по-голяма, отколкото изглежда."* (Under the heading "Срещу хора или срещу ботове")
**The Pattern:** This is a classic ChatGPT cliché used to introduce a comparison. It creates artificial drama for a very straightforward concept.
**Recommendation:** Remove this sentence. Begin the paragraph directly with the mechanical difference: *"Като гост обикновено играете само срещу ботове; за истинските съперници трябва профил."*

### 5. The "Neat Bow" Conclusion
**The Flagged Text:** *"За повечето хора най-близкото до истинския белот онлайн е безплатната маса в браузъра срещу реални съперници. Чиповете стигат за дълги вечери и за трениране на анонсите; печалба от тях няма и платформите не го крият. Онлайн белотът си остава това, което е и на кухненската маса: игра за вечерта."*
**The Pattern:** The formulaic summary. AI almost always ends articles by summarizing the main points (chips, no profit, real opponents) and repeating a metaphor used earlier in the text (the "kitchen table"). It feels highly robotic and redundant.
**Recommendation:** Delete this entire final paragraph. 
*Important Note:* Do **not** touch the paragraph immediately preceding this one (*"Онлайн белотът е от по-безобидните неща..."*). That paragraph contains vital responsible gambling language, 13+/18+ markers, and behavioral warnings. Let the article end naturally on that strong, responsible note rather than diluting it with an AI-generated summary. 

*(Note: The footer disclosures, author bio, and responsible gambling blocks at the very bottom are perfectly formatted and should remain exactly as they are.)*

