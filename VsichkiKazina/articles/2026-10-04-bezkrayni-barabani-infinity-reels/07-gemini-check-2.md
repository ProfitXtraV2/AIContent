# 07 — GEMINI CHECK 2 (Step 7, verbatim) · vk-0255

NORMALIZATION: verdict „Shows AI patterns, 70% confidence" → human-likeness = 100 − 70 = **30**. Improved from HL 25 (pass 1) → 30. Still < 80. Applying humaniser pass 2 (last within MAX_GEMINI_PASSES=2) per recs, then re-check + keep-best. Gemini ONLINE, no 429.

---

**Verdict: Shows AI patterns, 70% confidence.**

While this article is exceptionally well-prompted and uses natural, industry-accurate Bulgarian phrasing (e.g., "да излезе общата сметка", "сухи периоди"), its underlying skeleton reveals classic Large Language Model (LLM) structural habits. It avoids the worst AI clichés, but it relies heavily on rigid parallelism, didactic internal linking, and a preachy, moralizing conclusion. It reads like a human-drafted text that was "polished" by an AI, or a very tightly constrained AI generation.

### 1. Rigid Parallelism / Formulaic Structure
**Flagged:** "При Megaways броят барабани е фиксиран… При каскадните игри… При безкрайните барабани…"
**Pattern:** Three consecutive sentences starting with "При [Mechanic]…" create a robotic, staccato rhythm — a bulleted list forced into a paragraph.
**Recommendation:** Vary the introductory clauses; combine Megaways and cascades in a single fluid sentence contrasting them with Infinity Reels.

### 2. Forced Signposting / Didactic Link Insertion
**Flagged:** "…го намираш в [речника с казино термини] и в правилата на самото заглавие." · "…затова си струва да отвориш [правилата на ротативката], преди да решиш коя точно гледаш."
**Pattern:** Explicitly instructing the reader to click a link ("you can find this in…", "it's worth opening…") breaks the fourth wall and reads like a bot.
**Recommendation:** Weave the links into noun phrases inside the explanation; remove the explicit commands.

### 3. The Preachy Conclusion / Moralizing Wrap-up
**Flagged:** "Избирай слот, защото темпото и волатилността му ти понасят на бюджета, който си заделил, не заради обещанието за безкраен растеж."
**Pattern:** Prescriptive "Do X, not Y" life advice.
**Recommendation:** Frame as an objective observation about which bankroll/playstyle the mechanic suits, rather than commanding the reader. (Do not touch the RG disclosures that follow.)

### 4. Hypothetical Framing (Minor Flag)
**Flagged:** "Да речем, че тръгваш с три барабана и множител едно."
**Pattern:** "Да речем" is a common AI example transition.
**Recommendation:** State the scenario directly/objectively.
