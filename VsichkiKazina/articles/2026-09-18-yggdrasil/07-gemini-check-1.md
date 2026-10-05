# 07 — Gemini text check · pass 1 (initial 05b)

Command: `python3 scripts/gemini_check.py VsichkiKazina/articles/2026-09-18-yggdrasil/05b-final-draft.md`
Exit: 0

Normalized human-likeness: verdict "Likely AI-written, 85% confidence" = AI patterns @ 85% -> human-likeness = 100 - 85 = **15**. Below target 80 -> apply recs via fresh Humaniser (step-7b), re-run.

## Gemini verdict (verbatim)

**Verdict: Likely AI-written (or heavily AI-edited), 85% confidence.**

While this is a very high-quality, well-prompted text that avoids the worst AI clichés (like "In the ever-evolving world of online gaming..."), its underlying skeleton is unmistakably algorithmic. The text suffers from a highly predictable rhythm: almost every paragraph introduces a concept, explains it, and then ties it off with a neat, philosophical summary sentence. It relies heavily on signposting and parallel sentence structures, which are classic hallmarks of Large Language Models organizing information.

Here is the breakdown of the specific patterns that triggered this assessment, along with actionable recommendations to humanize the copy.

---

### 1. The "Roadmap" Signposting
**The Pattern:** AI models love to tell the reader exactly what they are about to read before they actually say it. It feels like a high school essay introduction.
**The Evidence:** 
> *"Тук ще намерите кой стои зад студиото, кои са фирмените му функции и, по-важно за банката ви, докъде стигат тези функции и къде спира ефектът им."*

**Recommendation:** 
Delete this sentence entirely. The headings already do the job of guiding the reader. You don't need a meta-sentence explaining the structure of the article. 

### 2. The "Neat Bow" (Paragraph Wrap-ups)
**The Pattern:** LLMs struggle to just let a fact sit there. They feel compelled to end almost *every single paragraph* with a summarizing "takeaway" sentence that tells the reader how to feel or what it all means. 
**The Evidence:**
> * "...Тази история обяснява защо студиото се държи повече като технологична компания, отколкото като работилница за една игра." (End of section 1)
> * "...Затова днес марката значи технология поне толкова, колкото име на конкретен екип." (End of section 2)
> * "...но същината е една: студиото продава механика, не поредна тема." (End of section 3)
> * "...Ако сравните тези тавани, се вижда, че Yggdrasil държи и класики със спокойни числа, и модерни високоволатилни заглавия с петцифрени множители." (End of section 5)

**Recommendation:** 
Cut at least half of these concluding sentences. Human writers don't summarize their own points every 100 words. Let the facts (like the transition to private equity, or the licensing of GATI) speak for themselves without the forced "moral of the story" at the end of each block.

### 3. Robotic, Parallel Sentence Structure (The "Listicle in a Paragraph")
**The Pattern:** When asked to list items without using bullet points, AI will often use the exact same syntax repeatedly. Subject + "is" + Description. It creates a monotonous, staccato rhythm.
**The Evidence:** 
> *"Valley of the Gods (2017) **е** египетското заглавие... Temple Stacks: Splitz (2020) **е** витрината на Splitz... Lucky Neko: Gigablox (2020) **е** първото заглавие... Vikings Go Berzerk Reloaded (2021) **е** модерната глава..."*

**Recommendation:** 
Vary the sentence structure in the "Топ слотове" section. Combine some of the games into a single sentence, use active verbs instead of "е" (is), and break the repetitive rhythm. For example, start one sentence with the mechanic rather than the game title, or group the high-volatility games together.

### 4. Forced Conversational Transitions & Meta-Commentary
**The Pattern:** AI tries to sound conversational by using artificial transition phrases that announce the tone of the next sentence.
**The Evidence:** 
> *"За вас това означава практична подробност..."*
> *"Тук е трезвата уговорка."*

**Recommendation:** 
Remove the meta-commentary. Instead of saying "Here is the sober caveat," just state the caveat directly (e.g., start directly with "Splitz с неговите стотици хиляди начини..."). Instead of "For you this means a practical detail," just say "Игра с логото на Yggdrasil невинаги е правена...".

### 5. The "In Conclusion" Grand Finale
**The Pattern:** AI almost always ends articles by zooming out to offer a perfectly balanced, slightly preachy final thought that summarizes the entire thesis of the text.
**The Evidence:** 
> *"За българския играч решаващото остава едно: лицензът на казиното пред НАП, не лицензът на студиото зад играта. Yggdrasil е студио за играчи, които ценят механиката и технологията повече от познатата плодова класика, а за банката ви по-полезно е да го мерите през числата му, отколкото през банера с рекордния таван."*

**Recommendation:** 
This is too perfectly packaged. Keep the practical advice about the NAP license, but delete the final sentence ("Yggdrasil е студио за играчи..."). Ending on the practical, regulatory note is much punchier and reads like a human expert giving advice, rather than an AI writing a concluding essay paragraph.

---
*Note on Compliance:* The responsible gambling language (18+ markers), the boilerplate, the affiliate disclosures, and the NAP licensing references are perfectly placed and formatted. Do not touch or alter any of this text during your edits.
