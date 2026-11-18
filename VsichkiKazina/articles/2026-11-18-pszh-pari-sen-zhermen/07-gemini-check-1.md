# 07 — Gemini check, pass 1 (vk-0338 · ПСЖ)

Script: scripts/gemini_check.py 05b-final-draft.md · GEMINI_API_KEY online · 2026-11-18T07:28:17Z

## Verbatim Gemini verdict + recommendations
```
**Verdict: Shows AI patterns, 80% confidence.**

While this article is highly polished, factually dense, and strictly adheres to its SEO and responsible gambling constraints, its underlying architecture is a textbook example of Large Language Model (LLM) generation. It suffers from "AI neatness"—every paragraph is perfectly symmetrical, transitions are heavily telegraphed, and the narrative relies on classic AI thematic bookending (introducing a "theme" in the intro and resolving it with a philosophical cliché in the conclusion). 

Here is the breakdown of the specific patterns that triggered this assessment, along with actionable recommendations to humanize the text.

### 1. Thematic Bookending & Cliché Sign-offs
**The Pattern:** LLMs love to frame articles around a central "thesis" or "paradox" and then wrap up the conclusion by referencing that exact theme, usually ending on a forward-looking cliché. 
**The Flagged Text:** 
*   *Intro:* "Историята му се върти около това чакане и около върха, който дойде едва когато клубът спря да го гони на части."
*   *Conclusion:* "Историята на Пари Сен Жермен се подрежда около един дълъг парадокс... Следващата глава ще се пише на терена, не в прогноза."
**Recommendation:** Delete the final paragraph entirely, or strip it of the "paradox" framing and the "next chapter will be written on the pitch" cliché (which is one of the most common AI sports-writing tropes). Let the article end naturally on the responsible gambling note in the preceding paragraph, or end with a hard, un-narrated fact about their current status.

### 2. Paragraph-Level Summarization (The "Bow on Top")
**The Pattern:** AI struggles to end a paragraph on a raw fact. It almost always appends a concluding sentence that summarizes the emotional or historical weight of the preceding facts.
**The Flagged Text:**
*   "...но спираше преди последната крачка в Европа." (End of section 3)
*   "Зад тях стои един факт: повече от десетилетие ПСЖ е отборът, който другите във Франция гонят." (End of section 4)
*   "Върхът, който парите гонеха от 2011 г., беше покорен два пъти в рамките на една година." (End of section 5)
**Recommendation:** Trim these summary sentences. Human journalists often let the data speak for itself. For example, in the "Трофеите у дома" section, just list the trophies and end the paragraph. You don't need to tell the reader that "behind them stands a fact." 

### 3. Robotic Topic Sentences & Transitions
**The Pattern:** AI uses highly formulaic, slightly unnatural transitional sentences to move from one H2 to the next, often stating the obvious to introduce a list.
**The Flagged Text:** 
*   "Големият футбол дойде на вълни."
*   "Обрат от друг порядък настъпи през 2011 г..."
*   "Силата на клуба личи и в рекордните му списъци."
**Recommendation:** Cut the filler transitions and jump straight into the substance. Instead of "Силата на клуба личи и в рекордните му списъци," start the paragraph directly with the subject: "Килиан Мбапе е голмайстор номер едно в историята на ПСЖ..."

### 4. Over-explained Meta-Commentary
**The Pattern:** When prompted to write about a specific point in time (in this case, the future date of 2026), AI often breaks the fourth wall to awkwardly explain its own temporal constraints to the reader.
**The Flagged Text:** "Числата се менят със следващите сезони, затова ги четете като моментна снимка от края на 2026 г."
**Recommendation:** Remove this sentence. The phrase "Към 2026 г. колекцията във Франция е внушителна..." at the start of the paragraph already establishes the timeline perfectly. The meta-commentary is redundant and sounds like a machine explaining its prompt parameters.

### 5. Forced Brand Signposting
**The Pattern:** When instructed to mention a brand or website, AI often does so with a clunky, overly literal justification that disrupts the narrative flow.
**The Flagged Text:** "Парижкият клуб е една от редовните теми, когато у нас се говори за европейски футбол, и затова има място сред профилите, които Всички Казина поддържа."
**Recommendation:** Soften the integration. Instead of explicitly justifying *why* the site has a profile on PSG, just weave the internal links naturally into the text. For example: "Като една от най-обсъжданите теми в европейския футбол у нас, ПСЖ заема важно място в нашия [раздел за футбол]..."

***

*Note on Hard Rules: All facts, dates (including the 2025/2026 Champions League claims), names, and figures have been accepted as-is without question. The responsible gambling disclosures, 18+ markers, and affiliate text in the footer are excellent, compliant, and have been entirely excluded from the critique as requested.*
```

## Normalization
- Verdict: "Shows AI patterns, 80% confidence" → human-likeness = 100 − 80 = **20**. Below target 80.
- Action: apply flagged style recs via fresh Humaniser pass (step-7b), preserve ALL untouchables (numbers/links/dates/RG/18+/disclosures/byline/brand). Then re-check.
