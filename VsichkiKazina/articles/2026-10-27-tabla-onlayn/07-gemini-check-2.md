# 07 — Gemini Step-7 check · pass 2 · vk-0296

Model: gemini-3.1-pro-preview (cross-model AI-pattern check)
Verdict: **Likely human-written, 85% confidence** → human-likeness = **85**
PASS test: 85 >= 80 → PASS.

KEEP-BEST ledger (human-likeness):
  baseline / pass-1 check : 25  (Shows AI patterns 75%)
  humaniser pass 1 → pass-2 check : 85  (Likely human-written 85%)  <-- WINNER, kept
MAX_GEMINI_PASSES=2; loop ended by PASS at pass 1 humaniser. Highest HL seen = 85.
Final 05b = the humaniser-pass-1 version (already committed). gemini column: human 85.
Pass-2 recs NOT applied: loop already PASSED at 85; a further humaniser pass risks lowering HL
(keep-best mandates keeping the highest version, not a later lower one).

--- Gemini verbatim output (pass 2) ---

**Verdict: Likely human-written (or heavily human-edited AI), 85% confidence.**

This article is exceptionally well-crafted for the Bulgarian language. It features natural idioms, logical deductions, and a conversational yet authoritative tone that AI rarely achieves natively in Bulgarian (e.g., "Спечелените купчини остават вътре", "докато не свършат, и точно тогава идва изкушението"). It completely avoids the dreaded AI fluff like "В днешния дигитален свят" (In today's digital world). 

However, there are a few lingering structural "tells"—specifically in how the text transitions, summarizes, and wraps up paragraphs—that suggest an LLM might have been used for outlining or drafting before a human heavily polished it.

Here are the specific passages that triggered AI detection patterns, along with actionable recommendations to remove them.

### 1. The "Signposting" Transition
> **Flagged text:** *"Едно нещо е добре да знаете предварително: гостите без регистрация не влизат в стаите за matchmaking и не могат да общуват с другите играчи."*
> **Pattern:** Conversational filler / Signposting. LLMs frequently announce what they are about to tell the reader to create a faux-conversational bridge. 

**Recommendation:** 
Remove the setup phrase entirely. Start the sentence directly with the factual limitation. The information is strong enough to stand on its own without the "Here is something you should know" preamble.

### 2. The Generalized "Therefore" Wrap-Up
> **Flagged text:** *"Затова мнозина тренират първо срещу компютър или в игра сам, а чак после сядат на маса с непознати."*
> **Pattern:** Generalized conclusion. AI models struggle to end paragraphs on a specific point, so they often zoom out to state what "many people" do as a way to tie a neat bow on the thought.

**Recommendation:** 
Delete this sentence. The preceding sentence (*"Срещу жив противник се появяват темпото, натискът на времето и човешките грешки, които ботът така и не имитира докрай."*) is a fantastic, highly human observation. Ending the paragraph on that punchy, insightful note is much stronger than following it up with a generic summary of human behavior.

### 3. Formulaic Instructional Flow
> **Flagged text:** *"Самото започване е кратко. За игра срещу хора се регистрирайте с имейл или Facebook; пробвате ли VIP Games като гост, стаите за истински мачове и чатът остават заключени, докато не си направите профил. За бърза партия в браузъра Poki тръгва веднага, без акаунт. После остава да вземете началните чипове..."*
> **Pattern:** Robotic "How-to" sequencing. The structure ("Starting is short. Do X. If Y, then Z. Then do A.") reads like a compressed step-by-step AI list forced into a paragraph format. 

**Recommendation:** 
Soften the rigid instructional tone. Instead of framing it as a chronological guide ("Самото започване е кратко... После остава да..."), suggest focusing purely on the *friction* of starting. For example, contrast the platforms that require accounts (VIP Games) directly against the ones that don't (Poki), without the "First do this, then do that" framing.

### 4. The "Neat Bow" Synthesis (Checklist Summary)
> **Flagged text:** The entire **"Коя платформа за вас"** section (*"За най-много реални съперници... VIP Games и Джаги са първият избор. Backgammon Tabla online е за хората... Poki остава най-бързият вход... А който вече играе белот в Belot.BG, ще намери..."*)
> **Pattern:** The Checklist Synthesis. This is a classic LLM structural hallmark. At the end of an article, the AI will perfectly categorize every single entity mentioned earlier in the text, assigning exactly one sentence and one specific "use case" to each, ensuring nothing is left out. 

**Recommendation:** 
This section feels redundant because the specific use-cases were already excellently explained in the "Къде се играе" section. To make it read less like an AI checklist, either:
1. Delete the section entirely and let the reader decide based on the previous descriptions.
2. Break the symmetry. Instead of listing every single platform again, group them organically (e.g., just compare the heavy social platforms vs. the quick browser option) without trying to give every single app a dedicated shoutout.

*(Note: The responsible gambling language, 18+ markers, and footer disclosures were reviewed and left entirely untouched as per your hard rules. They are formatted correctly and integrate well with the text.)*
