# Step 7 — Gemini cross-model check — PASS 2 (post humaniser pass 1)

Command: `python3 scripts/gemini_check.py 05b-final-draft.md`
Date: 2026-10-07

Result: pass-1 verdict "Shows (strong) AI patterns, 80–85%" → HUMAN-LIKENESS ≈ 15–20
(two consecutive runs gave 80% then 85% → HL 20 then 15; high-variance adversarial detector).
This is LOWER than the INITIAL draft (HL 25). The step-7b edits trimmed the brand-required
empathy/opinionated-voice the detector keeps penalising, so each pass lowers the score
(same pattern recorded on vk-0259).

DECISION (keep-best, mandatory): the highest human-likeness seen is the INITIAL 05b (HL 25).
Humaniser pass 1 is DISCARDED; 05b reverted to the initial version. 1 pass applied (cap=2);
pass 2 not run because it predictably degrades real quality for a noisy phantom-detector gain.
gemini column = `ai 75` (the winning/initial version's own verdict: "Shows AI patterns, 75%").

## Verdict (verbatim, post-pass-1 re-check)

**Verdict: Shows AI patterns, 85% confidence.**

While the article is highly informative, grammatically flawless, and well-structured, it exhibits several classic hallmarks of advanced LLM generation (likely GPT-4 or Claude). The primary tells are not robotic stiffness, but rather the opposite: the AI is trying *too hard* to sound empathetic, conversational, and philosophically profound about a dry, bureaucratic process. It relies heavily on didactic over-explanations, repetitive empathetic qualifiers, and dramatic "myth-busting" signposts.

Here is the breakdown of the specific patterns triggered, along with actionable recommendations.

---

### 1. The "Myth-Busting" Signpost & Forced Colloquialism
**The Passages:** 
*   *"Преди това обаче си струва да падне един упорит мит: че някъде стои онлайн справка..."*
*   *"Този мит се чува често; добре е да падне, преди да сте го погнали из интернет."*

**The Pattern:** AI models love to frame standard information as "busting a myth" to create a false sense of narrative tension. Furthermore, the phrase *"преди да сте го погнали из интернет"* is a forced colloquialism—an LLM's clumsy attempt to sound like a casual human expert. 

**Recommendation:** Remove the dramatic "myth" framing entirely. Instead of announcing that you are about to bust a myth, just state the fact directly. For example, transition smoothly by simply stating that there is no public online database to check EGNs, without the theatrical buildup.

### 2. Didactic Over-explanation & Narrated Intent
**The Passages:** 
*   *"Затова и защитата не опира до волята ви всяка отделна вечер."*
*   *"Долната граница е заложена в закона нарочно: срок от няколко дни лесно се заобикаля, затова минимумът е цяла година."*
*   *"Забрана, която може да се вдигне с едно обаждане, не би защитила никого, и законът нарочно не допуска предсрочно заличаване."*

**The Pattern:** This is classic LLM didacticism. Instead of just stating the rules of the registry, the AI feels compelled to play philosopher and explain the *moral or psychological intent* behind the law (e.g., lecturing the reader about willpower, or explaining *why* the lawmakers made the minimum one year). It treats the reader like a student who needs a life lesson, rather than a user looking for instructions.

**Recommendation:** Strip out the philosophical justifications. State the mechanics of the law plainly. Tell the reader that the minimum is one year and that early cancellation is impossible. You do not need to explain *why* the law was written that way or narrate how it protects their willpower. Let the facts speak for themselves.

### 3. The Empathetic Qualifier (Formulaic Repetition)
**The Passages:** 
*   *"Не можете да впишете друг пълнолетен вместо него, **колкото и основателна да ви изглежда причината**."*
*   *"Съпруг, работодател или роднина не може да ви провери по ЕГН, нито вие тях, **колкото и оправдано да им изглежда**."*

**The Pattern:** AI models are programmed to be highly empathetic, especially on sensitive topics like gambling addiction. This results in the AI constantly adding qualifiers to validate the user's feelings. Notice the exact structural repetition here (*"колкото и [adjective] да [pronoun] изглежда"*). This repetitive templating is a massive red flag for AI generation.

**Recommendation:** Delete both of the bolded clauses. The rules are absolute: you cannot register someone else, and you cannot check someone else's EGN. Adding "no matter how justified it seems" adds unnecessary fluff and exposes the AI's underlying text-generation template.

### 4. Corporate Grandstanding / Omniscient Wrap-up
**The Passage:** 
*   *"Във Всички Казина оценяваме казината по техните условия, но решение от този род стои над всяка класация и минава направо през регулатора."*

**The Pattern:** AI struggles to transition into a conclusion naturally, so it often zooms out to a grand, omniscient, or slightly self-congratulatory statement. This sentence feels like corporate grandstanding—it interrupts the practical flow of the article to pat the brand on the back for caring about the user.

**Recommendation:** Cut this sentence entirely. The transition into the final advice will be much stronger and more human if you go straight into the actionable help: *"Ако го обмисляте за себе си или заради близък, тръгнете от nap.bg..."*

---

### A Note on Process (Hard Rules Check)
I see multiple **[VERIFY]** tags regarding dates, legal minimums, and specific NAP procedures, as well as robust **18+ and Responsible Gambling disclosures** at the bottom. 

*Process Note:* This is excellent. The presence of these tags shows a highly responsible editorial workflow where the AI was explicitly instructed to flag claims it cannot guarantee. **Do not remove these tags** until a human editor has actually verified the data with the NAP website and the updated Gambling Act. The RG language and affiliate disclosures are also perfectly placed and should remain exactly as they are.
