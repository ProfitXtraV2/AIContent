# Step 7 — Gemini check, pass 2 (after Humaniser pass 1) — FINAL

Model: gemini-3.1-pro-preview (scripts/gemini_check.py) · verbatim output below.
Normalized: **"Likely human-written (or heavily human-edited), 85%"** → human-likeness = **85** → **PASS** (≥80).

Keep-best: initial 25 → pass 1 revision **85**. Kept pass 1. content-queue gemini = **human 85**.

---

**Verdict: Likely human-written (or heavily human-edited), 85% confidence.**

This article reads exceptionally well and avoids the most egregious AI hallmarks (fluffy introductions, overly flowery adjectives, robotic neutrality). It possesses a slightly cynical, realistic tone ("някакъв VIP връх", "тихомълком") that AI rarely achieves without highly specific prompting. The writer understands the subject matter deeply. 

However, there are a few structural quirks and repetitive motifs that mimic AI writing patterns—specifically, the tendency to latch onto a single metaphor and beat it to death, and a forced "punchy" rhythm at the end. 

Here are the specific patterns that triggered my assessment and how to fix them.

### 1. Motif Overuse (The "Banner" Metaphor)
**The Pattern:** AI models often latch onto a clever metaphor or phrase early in a text and recycle it in almost every paragraph to create artificial "cohesion." Here, the word "банер" (banner) is used as a stand-in for "marketing promises" seven times across the article.
**Flagged Passages:**
*   "...рядко стоят на **банера**..."
*   "...макар **банерът** да ги нарича..."
*   "Едно нещо, което **банерът** не подчертава..."
*   "...изглеждат еднакво на **банера**..."
*   "...водещият процент на **банера**..."
*   "...между две числа на **банерите**..."
*   "...**банерът** обещава повече от договора."

**Recommendation:** Keep the "banner" metaphor in the introduction and the conclusion, as it works well there. In the middle sections, replace it with natural synonyms like "рекламата" (the ad), "офертата" (the offer), "промоцията" (the promo), or "заглавието" (the headline) so it doesn't sound like a machine looping a keyword.

### 2. Staccato Rhythm (Forced Punchiness)
**The Pattern:** When prompted to be "concise" or "punchy," AI often generates a string of very short, fragmented sentences. This creates a robotic, machine-gun rhythm that lacks human flow and breathability. 
**Flagged Passage:** 
> "Три реда в условията решават дали програмата струва. Върху каква база се смята кешбекът. Носи ли превъртане и с каква база. Кога изтичат точките и самият кешбек. Намериш ли ги ясни и в твоя полза, стойността е реална, макар играта да си остава платено забавление. Заровени ли са, банерът обещава повече от договора. Статусът е приятен, но се плаща от твоя оборот."

**Recommendation:** Break up this staccato rhythm by combining the three fragmented condition sentences ("Върху каква база...", "Носи ли...", "Кога изтичат...") into a single, fluid sentence using commas or bullet points. Connect the final two sentences to create a smoother, more natural concluding thought. 

### 3. Formulaic Transitioning (The Didactic Pivot)
**The Pattern:** AI loves to explain a simple concept, pat the reader on the back, and then use a formulaic pivot to introduce a complication. It reads a bit like a textbook.
**Flagged Passage:** 
> "...тоест заложеното минус спечеленото за периода. **Дотук просто. Проблемът започва, когато** базата се смени тихомълком."

**Recommendation:** Remove the artificial bridge ("Дотук просто. Проблемът започва, когато..."). You can make it read more naturally by simply connecting the definition of net loss directly to the complication of the base changing quietly, perhaps using a contrasting conjunction.

### 4. Over-explaining the Obvious (AI "Helpful" Syndrome)
**The Pattern:** AI has a habit of explaining a concept perfectly well, but then adding a "That is to say..." (Тоест...) sentence to spoon-feed a hypothetical scenario to the reader, just to be absolutely sure they understood.
**Flagged Passage:** 
> "Ротативките обикновено дават пълен принос, докъм 100% от залога, докато игрите на маса и казиното на живо често се броят наполовина или изобщо не се броят. **Тоест двама играчи с еднакъв бюджет може да трупат точки с много различна скорост само защото единият върти слот игри, а другият играе блекджек.**"

**Recommendation:** Consider deleting the bolded sentence entirely. The preceding sentence already explains game contribution clearly and effectively. Trust the reader's intelligence; you don't need the hypothetical scenario to drive the point home. 

*(Note: All responsible gambling language, 18+ markers, and affiliate disclosures at the end of the text are perfectly placed and should remain exactly as they are.)*
