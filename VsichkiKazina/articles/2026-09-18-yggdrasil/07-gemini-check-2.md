# 07 — Gemini text check · pass 2 (after humaniser pass 1)

Command: `python3 scripts/gemini_check.py VsichkiKazina/articles/2026-09-18-yggdrasil/05b-final-draft.md`
Exit: 0

Normalized human-likeness: verdict "Shows AI patterns, 75% confidence" -> human-likeness = 100 - 75 = **25** (up from 15). Below target 80 -> one more Humaniser pass (2 of max 2), then keep-best.

Note on rec #4: Gemini suggests converting the top-slots prose to a bulleted list. DECLINED - the Brand Gate treats such an enumeration list as an AI "clean categorisation" tell (Pillar 5) and the scannable data view is already the SVG infographic; a bullet list would duplicate it. Applied the rec's underlying goal (break the robotic rhythm) by varying the prose openers instead. All other recs applied.

## Gemini verdict (verbatim)

**Verdict: Shows AI patterns, 75% confidence**

While this article is highly factual, well-researched, and avoids the worst AI hallucinations, its structural skeleton is heavily reliant on classic Large Language Model (LLM) writing tropes. It reads like a very well-prompted AI or a human writer who leans heavily on formulaic transitions, "neat bow" summaries, and poetic metaphors to explain technical concepts. 

Here is the breakdown of the specific patterns that triggered this assessment, along with actionable recommendations to humanize the text.

### 1. The "What Sets It Apart" Hook (Formulaic Openings)
AI models struggle to start paragraphs organically, often relying on a formula where they explicitly state that the subject is unique or different before explaining *why*. 
*   **Flagged text:** *"Yggdrasil (игдрасил) се различава от повечето студиа по едно нещо: то е колкото производител на игри, толкова и технологична платформа."*
*   **Flagged text:** *"Онова, което отличава Yggdrasil от съседите му по рафт, е GATI..."*
*   **Recommendation:** Remove the artificial setup. For the intro, start directly with the fact that Yggdrasil operates as both a game producer and a tech platform. For the GATI section, drop the "neighbors on the shelf" idiom and simply introduce GATI as the studio's standardized development toolkit.

### 2. The Poetic/Philosophical Wrap-Up (Narrated Metaphor)
When explaining math or technical concepts, AI often concludes the paragraph with a slightly dramatic, metaphorical summary to make it sound "engaging."
*   **Flagged text:** *"Множителите и разцепените символи правят пътя по-бурен, но крайната точка си остава там, където я определя математиката."*
*   **Recommendation:** Strip the metaphor ("бурен път", "крайна точка"). Replace it with a dry, direct statement explaining that visual mechanics increase variance but do not alter the programmed Return to Player (RTP). 

### 3. The "Neat Bow" Conclusion (Over-summarization)
AI hates leaving a section without a concluding sentence that summarizes exactly what was just said. This leads to redundancy.
*   **Flagged text:** *"За българския играч решаващото остава едно: лицензът на казиното пред НАП, не лицензът на студиото зад играта."* (This appears at the very end of the article).
*   **Recommendation:** Delete this final sentence entirely. You already made this exact point clearly in the first paragraph of that same section (*"За вас като играч в България значение има лицензът на самия оператор пред НАП..."*). Trust the reader to remember what they read two paragraphs ago.

### 4. The Cataloging Paragraph (Formulaic Structure)
When tasked with listing examples, AI often writes dense paragraphs where every sentence follows the exact same rhythm: *[Game Name] does [Feature] with [Stats]*. 
*   **Flagged text:** *"Египетското Valley of the Gods (2017) залага на... Splitz двигателят получи витрината си в Temple Stacks... GigaBlox дебютира в Lucky Neko... Модерната глава на серията Vikings..."*
*   **Recommendation:** Break this dense block of text into a bulleted list. Not only will this break up the robotic rhythm of the sentences, but it will also make the heavy statistical data (RTPs, max wins, release years) much easier for a human to scan.

### 5. Signposting (Filler Transitions)
AI frequently uses "signpost" sentences that contain no actual information other than telling the reader what they are about to look at.
*   **Flagged text:** *"Няколко заглавия държат името на Yggdrasil живо, а числата им показват къде играе студиото на скалата."*
*   **Recommendation:** Cut this sentence entirely. The heading "Топ слотове и техните числа" followed immediately by the table and the data is perfectly sufficient. You don't need to announce the data before showing it.

### A Note on Process and Compliance:
The responsible gambling language (18+ warnings), the affiliate disclosure, and the specific references to Bulgarian licensing (НАП) are excellently placed. **Do not touch or alter any of the boilerplate text, dates, or legal disclosures at the bottom of the article.** They are functionally perfect and necessary for compliance.
