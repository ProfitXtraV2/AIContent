# Gemini Step-7 external check — pass 3 (2026-10-02, MAX_GEMINI_PASSES cap)

Ran on humaniser pass 2 05b.

## Normalized score + KEEP-BEST decision
"Shows AI patterns, 80%" -> human-likeness = **20**.

Human-likeness across versions (noisy detector, bounces): initial/pass0 = 20; humaniser pass 1 = **30 (BEST)**; humaniser pass 2 = 20.
KEEP-BEST: restore humaniser **pass 1** (HL 30, highest seen). Cap of 2 humaniser passes reached; 30 < 80, so final gemini verdict = ai 70 (pass-1's own 'Shows AI patterns 70%').

## Full verbatim verdict (pass 2 draft)

**Verdict: Shows AI patterns, 80% confidence**

While the article is highly informative, grammatically flawless, and well-structured, it exhibits several classic hallmarks of LLM generation. The text relies heavily on formulaic transitions, didactic "us vs. them" framing, and slightly unnatural metaphors that occur when AI attempts to translate English idioms into Bulgarian. It reads like a high-quality GPT-4 output that has been given a good prompt but hasn't been fully humanized.

Here is the breakdown of the specific patterns that triggered this assessment, along with actionable recommendations.

### 1. The "Neat Bow" Summary (Formulaic Conclusion)
AI models are trained to summarize everything at the end of an essay, often repeating the exact points made in the subheadings, wrapped up with a philosophical or definitive final thought. 

*   **The Flagged Passage:** *"Уникалната парола в мениджър и двуфакторната автентикация през приложение са минимумът. Те спират огромната част от опитите за превземане, защото повечето кражби залагат точно на повторена парола и липсващ втори фактор. Фалшивите имейли и огледалните сайтове идват после и се разбиват в същите два навика. Останалото е надстройка, полезна, но не тя решава."*
*   **The Recommendation:** Break this formulaic recap. Instead of summarizing the H2s again, end on a single, forward-looking, practical note. Remove the phrase *"се разбиват в същите два навика"* (crash into the same two habits)—this is a very unnatural metaphor in Bulgarian. Replace it with a literal statement about how good habits prevent phishing.

### 2. Unnatural Metaphors / Clunky Idiom Translation
When AI tries to sound conversational or authoritative in Bulgarian, it often translates English structural idioms too literally, resulting in phrasing that a native Bulgarian copywriter wouldn't naturally use.

*   **The Flagged Passage:** *"През него минава възстановяването на парола, затова превземе ли някой пощата ви, казиното идва наготово след нея."*
*   **The Recommendation:** *"идва наготово след нея"* is an awkward personification of the casino account. Change this to a more direct, human phrasing, such as explaining that compromising the email automatically grants access to the casino account.
*   **The Flagged Passage:** *"Падне ли един, следващият печели време и често спира превземането на акаунта..."*
*   **The Recommendation:** The "falling layers buying time" is a classic AI cybersecurity trope. Soften the metaphor. Just state that multiple layers of security make it exponentially harder for unauthorized access.

### 3. The "Even if X, Y" Setup (Signposting)
AI loves to transition between paragraphs by setting up a hypothetical extreme to introduce the next topic. It creates a predictable, rhythmic bounce that feels robotic.

*   **The Flagged Passage:** *"Дори най-силната парола и код не помагат, ако сами дадете достъп. Точно на това залага фишингът: убеждава ви сами да го направите."*
*   **The Recommendation:** Remove the dramatic setup. Start the phishing section directly by stating what phishing is and how it bypasses technical security. For example, start with how phishing tricks users into handing over their credentials, rather than the "Even the strongest password..." contrast.

### 4. Didactic / Preachy Tone
AI often adopts a lecturing tone when discussing security, heavily emphasizing "your responsibility" versus "their responsibility" in a rigid, binary way.

*   **The Flagged Passage:** *"Лицензираното казино пази своята част от системата, но входът към акаунта остава във вашите ръце. Защитата на този вход зависи изцяло от вас."* and *"Вашата отговорност е една: самоличността, с която се влиза."*
*   **The Recommendation:** Soften the lecture. Instead of telling the reader "Your responsibility is one" or "Protection depends entirely on you," frame it as a partnership or simply state the facts of how user credentials work. Make it conversational rather than accusatory.

### 5. Staccato Rhythm in Lists Disguised as Prose
AI frequently writes lists as a series of short, punchy sentences to simulate urgency.

*   **The Flagged Passage:** *"Понякога първият сигнал е известие за влизане, което не сте правили. Друг път са сменени данни за контакт, стопен баланс или заявка за теглене, която не разпознавате. Усетите ли нещо такова, бързината работи за вас."*
*   **The Recommendation:** Combine these sentences to create a more natural, flowing rhythm. The "If you sense X, Y works for you" is another AI-ism. Change *"бързината работи за вас"* to a direct instruction to act immediately.

---

**A Note on Process:**
The responsible gambling language, 18+ markers, author bio, and the affiliate disclosure at the bottom of the text are perfectly placed, highly compliant, and well-formatted. **Do not touch or alter these sections** during your humanization edits, as they are critical for legal and ethical compliance.
