# Gemini Step-7 external check — pass 3 (2026-10-02, MAX_GEMINI_PASSES cap)

## Normalized score + KEEP-BEST
"Shows AI patterns, 70%" -> human-likeness = **30**.
HL across versions: pass0 25, pass1 25, pass2 **30 (BEST)**. Current 05b = humaniser pass 2 = the best, so it is KEPT (no revert). 30 < 80 after cap -> final gemini verdict = ai 70.

## Full verbatim verdict (pass 2 draft)

**Verdict: Shows AI patterns, 70% confidence.**

This article is highly polished and avoids the most egregious AI clichés (there is no "In today's fast-paced world" or "Let's dive in"). The tone is appropriately serious and empathetic for a Responsible Gambling (RG) page. However, it reads like a high-quality, heavily prompted LLM output (or a human draft heavily edited by AI) because of its rigid structural symmetry, predictable paragraph pacing, and reliance on neat, summarizing "wrap-up" sentences at the end of sections. 

Here is the breakdown of the specific patterns that triggered this assessment and how to fix them.

### 1. Pattern: The "Signpost" Intro Wrap-Up
**The Quote:** *"Изместването рядко се усеща отвътре, затова си струва да знаеш как изглежда отстрани и какво можеш да направиш, ако го разпознаеш у себе си или у близък човек."*
**Why it flags as AI:** LLMs struggle to transition naturally from an introduction to the main body. They almost always use a "signposting" sentence that explicitly announces what the rest of the article is about (e.g., "therefore it's worth knowing," "here is what to look for"). 
**Recommendation:** Delete the phrase *"затова си струва да знаеш как изглежда отстрани и какво можеш да направиш..."* entirely. End the introduction on the strong, factual observation about the boundary shifting, and let the H2 (*Кога забавлението спира да е забавление*) do the work of transitioning the reader.

### 2. Pattern: Over-Polished, Symmetrical Lists
**The Quote:** 
> - **Гонене на загубите:** след като изгубиш...
> - **Криене и лъжа за играта:** омаловажаваш...
> - **Заемане на пари за игра:** от кредит...
> *(and so on for all 6 bullet points)*

**Why it flags as AI:** The rigid `**Bold Concept:** Explanation` format applied flawlessly across a half-dozen bullet points is a classic ChatGPT formatting quirk. Human writers tend to vary list structures—some points might be full sentences, others might be shorter, or they might not use the exact same bolding syntax for every single line.
**Recommendation:** Break the robotic symmetry. You can do this by removing the bolded prefixes and just writing the bullet points as natural sentences (e.g., instead of "**Заемане на пари за игра:** от кредит...", write "Заемаш пари за игра от кредит, приятели или средства, предвидени за друго."). 

### 3. Pattern: The Platitude / Summary Wrap-Up Sentence
**The Quote:** *"Разпознаването на тези сигнали е първата полезна стъпка."* (Found at the end of the "Признаци, които си струва да разпознаеш" section).
**Why it flags as AI:** AI models are programmed to be helpful and conclusive, which means they rarely just deliver facts and move on. They feel compelled to tie a neat little bow at the end of paragraphs with a mild, slightly preachy platitude.
**Recommendation:** Delete this sentence entirely. End the paragraph on the hard facts (*"...чувство на вина след игра, което бързо отстъпва пред желанието да се играе пак."*). The text will feel much punchier and more human without the unnecessary summary.

### 4. Pattern: Narrated Emotion / Philosophical Conclusion
**The Quote:** *"Разпознаването на проблема рядко е драматичен момент. По-често е просто да забележиш, че играта е престанала да бъде нещо, което избираш."*
**Why it flags as AI:** When concluding an article, AI often shifts into a detached, philosophical, or emotionally narrated tone to create a sense of closure before delivering the final Call to Action. 
**Recommendation:** Cut the philosophical opening. Start that final paragraph directly with the actionable advice. For example, you can merge it straight into the CTA: *"Ако забележиш, че играта е престанала да бъде нещо, което избираш, и се разпознаваш в тези признаци, конкретната следваща стъпка е обаждане на „Солидарност" 0888 99 18 66."* *(Note: Ensure you keep the exact phone number and organization name intact as per the hard rules).*

### 5. Pattern: Formulaic Contrast Framing
**The Quote:** *"Човек с висок доход може да заложи стотици евро за вечер, без това да му създаде проблем, докато друг изпада в затруднение с много по-малко."*
**Why it flags as AI:** AI loves to explain concepts using immediate, perfectly balanced contrasts ("While Person A does X, Person B does Y"). It's not inherently wrong, but it contributes to the "textbook" feel of the writing.
**Recommendation:** Make it slightly more conversational and less perfectly balanced. For example, rephrase to focus on the core issue rather than the hypothetical two people: *"Размерът на залога не е единственият критерий – стотици евро може да са безобидно забавление за един, но минимална сума да създаде сериозно затруднение за друг."*
