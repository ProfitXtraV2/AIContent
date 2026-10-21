# Gemini Step-7 external check — pass 1 (2026-10-02)

Model: gemini-3.1-pro-preview. Ran on initial 05b (humaniser pass 0).

## Normalized score
Verdict phrased as "Shows AI patterns, 80%" -> human-likeness = 100 - 80 = **20** -> below GEMINI_TARGET_CONFIDENCE (80), iterate.

## Full verbatim verdict + recommendations

**Verdict: Shows AI patterns, 80% confidence.**

While this is a high-quality, well-prompted text that successfully avoids the most egregious AI clichés (like "В днешния дигитален свят" / "In today's digital world"), its underlying skeleton is unmistakably AI-generated. The text relies heavily on didactic hand-holding, explicit scope-setting (signposting), forced staccato rhythms for emphasis, and a highly symmetrical, metaphor-heavy structure. It reads like a very polished textbook rather than an engaging, human-authored web article.

Here is the breakdown of the specific patterns that triggered this assessment, along with actionable recommendations to humanize the text.

---

### 1. Explicit Signposting & Scope-Setting
**The Pattern:** LLMs are programmed to be helpful and precise, which often results in them explicitly announcing what they are going to talk about and what they are *not* going to talk about before actually making their point.
**The Flagged Passage:** 
> "Две съседни теми нарочно остават настрани. Как се криптира самото плащане и дали връзката е защитена е въпрос на сигурност на транзакцията; какви права имате върху личните си данни е въпрос на защита на данните. Тук говорим единствено за достъпа до акаунта, тоест кой може да влезе като вас."
**The Recommendation:** Delete this entire paragraph. Human writers rarely spend 50 words explaining what an article *isn't* about right in the introduction. Let the H2s naturally guide the scope of the article. 

### 2. Didactic Transitions & Hand-Holding
**The Pattern:** AI frequently uses conversational filler to tell the reader *how* to think about the upcoming information, treating the reader a bit like a student in a classroom. 
**The Flagged Passages:**
> * "Разделението е лесно за запомняне." (The division is easy to remember.)
> * "Няколко навика свалят риска близо до нулата." (A few habits drop the risk close to zero.)
**The Recommendation:** Remove these meta-commentary transitions. Start the paragraphs directly with the substantive information. For example, instead of "Разделението е лесно за запомняне. Операторът отговаря за...", just start with "Операторът отговаря за...". 

### 3. Over-Reliance on Physical Security Metaphors
**The Pattern:** When discussing digital concepts, LLMs lean heavily on a cohesive web of physical metaphors (doors, fences, keys) to make the text feel "creative." When overused, it feels engineered.
**The Flagged Passages:**
> * "Вашата страна на оградата е една..." (Your side of the fence...)
> * "...е резервният ключ към казино акаунта." (...is the backup key...)
> * "Устройството е другата отворена врата." (The device is the other open door.)
> * "...не тя държи вратата затворена." (...it doesn't keep the door closed.)
**The Recommendation:** Keep one metaphor if you like, but strip out the rest. Change "Вашата страна на оградата е една" to a direct statement about user responsibility (e.g., "Вашата отговорност е една"). Remove the "door" metaphor in the final paragraph entirely—just state that the other steps are secondary.

### 4. Forced Staccato Rhythm & Manufactured Drama
**The Pattern:** To simulate human emotion or urgency, AI often breaks sentences into short, punchy, staccato fragments. It feels overly dramatic for a standard informational guide.
**The Flagged Passages:**
> * "Бързината е номерът. Целта е да натиснете, преди да спрете да помислите."
> * "Усетите ли нещо такова, бързината работи за вас."
**The Recommendation:** Combine these short bursts into more fluid, natural sentences. For example, merge the first passage into something like: "Целта на фишинга е да ви накара да действате прибързано, преди да сте обмислили ситуацията."

### 5. AI Platitudes / Aphorisms
**The Pattern:** LLMs love to wrap up paragraphs with a fortune-cookie-style platitude that sounds wise but adds zero informational value.
**The Flagged Passage:**
> "Дребните неща помагат колкото големите: заключен екран, редовни обновления..."
**The Recommendation:** Cut the aphorism ("Дребните неща помагат колкото големите"). Start the sentence directly with the actionable advice: "Заключеният екран, редовните обновления и излизането от профила са задължителни за устройства, които не са само ваши."

---

*Note on Hard Rules: The responsible gambling boilerplate, 18+ markers, affiliate disclosures, and legal citations at the bottom of the text are perfectly formatted and must remain exactly as they are. Do not alter them during your editing process.*
