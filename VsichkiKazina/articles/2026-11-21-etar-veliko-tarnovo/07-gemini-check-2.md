# 07 — Gemini external check · pass 2 (after humaniser pass 1) · vk-0341 Етър Велико Търново

**Script:** `python3 scripts/gemini_check.py 05b-final-draft.md` · exit 0 · GEMINI ONLINE
**Verdict (verbatim):** Shows AI patterns, **80%** confidence → **human-likeness = 20** (100 − 80). Improved from pass-1 baseline (15). Still NEEDS CHANGES (< 80).

---

**Verdict: Shows AI patterns, 80% confidence.**

While the text is grammatically excellent, avoids the most obvious cliché vocabulary, and integrates the responsible gambling/SEO elements quite naturally, its underlying architecture is distinctly AI-generated. It suffers from the "rhythm of constant profoundness"—almost every paragraph ends with a dramatic, philosophical, or poetic takeaway. It also relies heavily on formulaic transitions, forced positive spins on negative facts, and a classic "bow-tie" summary at the end.

### 1. The "Silver Lining" / Forced Positivity
- *"Резултатът е суров, но самото излизане срещу такъв гранд показва, че клубът отдавна не е чужд на европейската сцена."* → Remove the philosophical justification; let the historical fact stand on its own.

### 2. Poetic / Melodramatic Wrap-ups
- *"Титлата от 1991 г. е върхът, но талантът около нея се разпръсква надалеч и оставя следа много след като виолетовата фланелка слиза от елита."*
- *"Голямо съоръжение в град, който не е сред най-големите в страната, казва нещо за мащаба на амбицията зад клуба в добрите му години."* → Delete/trim; end on the factual note.

### 3. Formulaic Hooks and Signposting
- *"Ако трябва да се посочи един сезон за целия клуб, това е 1990/91."* → Cut the hypothetical setup; start directly with the subject.

### 4. The "Bow-Tie" Summary (Recap Conclusion)
- *"Етър остава клубът на едно голямо лято: титлата от 1991 г., поколението... Това е наследството, което Велико Търново пази и днес..."* → Delete this recap; the „На пари, отдалеч" section already closes the page.

### 5. AI Meta-Commentary / Breaking the Fourth Wall
- *"...затова конкретната цифра я оставям за проверка."* → Keep the `[VERIFY: ...]` tag (vital editorial safety mechanism); delete the conversational phrase that talks to the editor.

### 6. The "Not X, but Y" Contrast Pattern
- *"Важното е как се печели: не с късна драма в последния кръг, а със седем точки преднина пред ЦСКА."* → Simplify to direct: "Титлата е спечелена категорично, със седем точки преднина пред ЦСКА, натрупани кръг след кръг."

**Action:** humaniser pass 2 applied to all six (kept every number/link/RG/18+/disclosure/date/byline/brand and the [VERIFY] tag). This is the second and final allowed pass (MAX_GEMINI_PASSES=2); re-check follows, then keep-best.
