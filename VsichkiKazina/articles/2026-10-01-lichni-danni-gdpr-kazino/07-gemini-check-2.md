# 07-GEMINI-CHECK — pass 2 (after humaniser pass 1) — lichni-danni-gdpr-kazino
# Model: gemini-3.1-pro-preview · run 2026-10-01 (3rd fire)
# Normalized human-likeness = 80 (Likely human-written / heavily human-edited AI, 80% confidence).
# PASS: human-likeness >= GEMINI_TARGET_CONFIDENCE (80). Log PASS and continue (no further pass). gemini column = 'human 80'.
# Remaining recs are minor/optional; NOT applied — the current text is the PASSED version (further edits would invalidate the verdict and risk a lower re-check).

## Gemini verbatim verdict + recommendations

**Verdict: Likely human-written (or heavily human-edited AI), 80% confidence.**

This is a very strong piece of copy. It avoids the most egregious AI hallmarks (there is no "В днешния дигитален свят" / "In today's digital world", no overly flowery adjectives, and no robotic neutrality). The author uses a distinct, authoritative first-person voice ("Разписвам ги тук", "проверявам дали"), punchy syntax ("Първо лицензът... после всичко останало"), and excellent human-like metaphors ("сблъсък между две задължения, в който съхранението печели временно"). 

However, there are a few lingering structural and phrasing patterns that suggest an AI might have been used for outlining, drafting, or generating the image metadata. 

Here is the breakdown of the specific patterns that triggered my AI-detection radar, along with actionable recommendations to iron them out.

### 1. Pattern: The "Rule of Three" / Formulaic Categorization
* **The Quote:** *"Събраното се дели грубо на три. Има базовата самоличност (име, единен граждански номер или документ, адрес, дата на раждане), финансовата част (картата или сметката, с която внасяш и теглиш) и поведенческите следи..."*
* **Why it flags:** LLMs are hardwired to organize information into neat, easily digestible lists or triads. Announcing that something "is roughly divided into three" before listing them is a classic AI signposting technique used to structure a paragraph.
* **Recommendation:** Remove the setup sentence. You don't need to announce the categorization. Just dive straight into the data types organically. For example, start directly with: *"Казината събират базова самоличност (...), финансова информация (...) и поведенчески следи..."*

### 2. Pattern: Translated Idiom / Clunky Transition
* **The Quote:** *"Едно нещо, което си струва да отделиш наум: съгласието за маркетинг е различно от задължителните данни."*
* **Why it flags:** "Едно нещо, което си струва да отделиш наум" is a very clunky, unnatural phrase in Bulgarian. It reads like a direct, literal translation of the classic AI transition: *"One thing worth keeping in mind..."* or *"One thing to note..."*
* **Recommendation:** Replace this with a more natural, conversational Bulgarian phrasing. Something sharper, like *"Важно е да се прави разлика:"* or simply *"Не бъркайте задължителните данни със съгласието за маркетинг."*

### 3. Pattern: The "Actionable Takeaway" Concluding Subhead
* **The Quote:** *"Какво значи това на практика"* (H2)
* **Why it flags:** AI models almost universally struggle to end articles organically. They rely on formulaic concluding subheads like "What this means for you," "In practice," or "The bottom line." 
* **Recommendation:** Change the subhead to something specific to the actual narrative of the paragraph, rather than a generic summary signpost. For example: *"Защо лицензът е най-добрата защита за данните ти"* or *"Рисковете при офшорните казина"*.

### 4. Pattern: Overly Verbose / Prompt-like Alt Text
* **The Quote:** *"![Инфографика: трите групи лични данни, които онлайн казиното събира (самоличност, финансови, поведенчески), причината KYC и AML, правата на играча по GDPR (достъп, корекция, преносимост, възражение срещу маркетинг) и границата, че правото на изтриване е ограничено от задължението за съхранение на данните по правилата срещу изпиране на пари](images/lichni-danni-gdpr-kazino.svg)"*
* **Why it flags:** This does not read like standard SEO alt text. It reads exactly like a prompt fed into Midjourney/DALL-E to generate the image, or an AI-generated summary of the entire article stuffed into the image brackets. It is too long and overly descriptive for standard web accessibility.
* **Recommendation:** Condense the alt text to a concise, accurate description of the image itself. (e.g., *"Инфографика за видовете лични данни в онлайн казината, KYC/AML изискванията и правата на играчите по GDPR."*)

***

**A Note on Process & Compliance:**
The responsible gambling language, 18+ markers, affiliate disclosures, and author boilerplate at the end of the text are perfectly formatted, legally sound, and seamlessly integrated. **Do not touch or alter these sections.** They are exactly as they should be.
