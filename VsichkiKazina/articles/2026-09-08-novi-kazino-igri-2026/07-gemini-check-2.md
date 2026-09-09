# 07 — Gemini external check · pass 2 (after Humaniser pass 1)

Model: gemini-3.1-pro-preview · run 2026-09-08 · article: 2026-09-08-novi-kazino-igri-2026
Verdict normalization: "Shows strong AI patterns, 85%" → **human-likeness = 100 − 85 = 15**.
NOTE: this is LOWER than the initial draft (hl 25). Gemini is high-variance on this piece (cf. vk-0008 reads 25–90). Several pass-2 recs CONFLICT with mandatory brand rules and will NOT be applied: bullet-point/bolded-inline-subhead formatting (brand bans bullet lists for prose facts), removing the worked €-example (guides REQUIRE a worked € example), and removing the `[VERIFY]` flag (flags MUST stay in the text for the human — Gemini misreads the flag as a missed placeholder). Only the brand-compliant subset is applied in Humaniser pass 2: break the dense mechanics info-dump into shorter paragraphs, trim the checklist recap, soften clinical psychology phrasing, and de-cliché the RTP example toward micro-stakes framing (still a worked illustrative € example, RTP concept preserved).

## Gemini verbatim verdict + recommendations

**Verdict: Shows strong AI patterns, 85% confidence.**

While the article is grammatically flawless, highly informative, and contains excellent localized legal/compliance footers (which were clearly human-added or heavily human-prompted), the core body text relies heavily on classic LLM structural tropes. It uses textbook examples, compressed encyclopedic definitions, a slightly didactic tone regarding psychology, and a classic "bow-tie" summary conclusion.

Here is the breakdown of the specific patterns that triggered this assessment, along with actionable recommendations to humanize the copy.

### 1. The "Textbook RTP" Cliché
**The Pattern:** AI models almost universally explain RTP using a hypothetical €100 (or $100) bet, breaking it down into exactly €96 returned and €4 kept by the house. It is the most common AI casino-writing trope in existence.
**The Quote:** *"Заложите ли хипотетични €100 на заглавие с около 96% RTP, средно за много завъртания се връщат около €96, а около €4 остават предимство за казиното."*
**The Recommendation:** Ditch the €100/€96/€4 example entirely. Human experts usually explain RTP by contrasting it with volatility or by explaining that it's a mathematical baseline calculated over billions of simulated spins, rather than breaking down a €100 bill. If you must use an example, use a micro-bet scenario (e.g., thousands of €0.20 spins) to illustrate how long-term math works, which feels much more authentic to actual slot play.

### 2. Compressed Encyclopedic Definitions
**The Pattern:** When asked to explain mechanics, AI tends to cram dictionary-style definitions of multiple concepts into a single, dense paragraph without formatting breaks. It reads like a glossary rather than an engaging article.
**The Quote:** *"Megaways, механика, въведена от Big Time Gaming, променя броя символи... Съвсем различно се държи cluster pays: там линии няма... При „задръж и завърти“ (hold-and-win) специални символи се заключват..."*
**The Recommendation:** Break this dense paragraph apart. Use bullet points or bolded inline subheads for **Megaways**, **Cluster Pays**, and **Hold-and-Win**. To make it sound less like Wikipedia, shift the focus from *how they are programmed* to *how they feel to the player* (e.g., the visual chaos of Megaways vs. the slow-build tension of Hold-and-Win).

### 3. The Didactic / Parental Tone
**The Pattern:** When discussing gambling psychology or risks, AI often shifts into a highly clinical, cautionary tone that sounds like a psychology textbook rather than a peer giving advice.
**The Quote:** *"Подтикът „пробвай най-новото“ работи като поведенчески капан, защото свежата графика и усещането, че изпускате нещо, тласкат към по-бързи и по-едри залози."*
**The Recommendation:** Soften the clinical language ("поведенчески капан" / behavioral trap). Rephrase this to sound like a seasoned player sharing a warning. For example, frame it around the "shiny object syndrome" of new releases—how the flashy animations are specifically designed to make you forget your budget, rather than diagnosing the reader's psychological triggers.

### 4. The "Bow-Tie" Summary Conclusion
**The Pattern:** LLMs are hardwired to conclude articles by summarizing every point they just made. The final paragraph here is a perfect checklist recap of the article's subheadings (demo, volatility, developer).
**The Quote:** *"Форматът се сменя, математиката остава същата. „Ново“ е маркетингов етикет, не по-добър шанс. Пуснете новото заглавие първо в демо, прочетете тавана и волатилността, проверете кой го е направил, и чак тогава решете струва ли развлечението парите му."*
**The Recommendation:** Cut the recap. You don't need to remind the reader to check the demo, volatility, and developer—they just read that 30 seconds ago. Keep the strong opening sentence ("Форматът се сменя, математиката остава същата. „Ново“ е маркетингов етикет, не по-добър шанс."), and then immediately transition to your internal link call-to-action.

### 5. Process Issue: Surviving Editor Tags
**The Pattern:** AI-generated or AI-assisted drafts often include bracketed placeholders that get missed during human review.
**The Quote:** *"[VERIFY: допустимост на bonus buy при лицензирани BG оператори]"*
**The Recommendation:** This is a workflow/process issue. The tag survived the final human verification stage. You need to actually verify the legal status of bonus buys in Bulgaria, integrate that fact into the sentence, and delete the bracketed flag before publishing. (Do not remove the responsible gambling boilerplate or affiliate disclosures at the bottom—those are excellent and necessary).

## Decision
hl 15 (< initial hl 25). Apply ONLY the brand-compliant subset in a FINAL Humaniser pass 2 (cap): #2 (break the info-dump into shorter prose paragraphs, feel-not-spec framing), #3 (soften clinical tone), #4 (trim checklist recap), and #1 reframed as a micro-stakes illustrative € example (NOT removed — guides require a worked example; RTP 96% concept preserved). REJECTED as non-compliant: bullets/inline-subhead formatting; removing the worked example; removing the [VERIFY] flag (flags stay — the human resolves at Step 6, this is not a missed placeholder). Then re-check and KEEP THE HIGHEST-hl version across initial (25) / pass1 (15) / pass2.
