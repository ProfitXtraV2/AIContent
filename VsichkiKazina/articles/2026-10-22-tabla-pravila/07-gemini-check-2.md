# Step 7 — Gemini external check, pass 2 (after humaniser pass 1)

**Script:** `python3 scripts/gemini_check.py 05b-final-draft.md`
**Normalized human-likeness:** 80 (verdict "Likely human-written, 80% confidence" → HL = 80)
**Result:** PASS — human-likeness 80 ≥ GEMINI_TARGET_CONFIDENCE (80).

## Keep-best decision
- Initial draft (check 1): HL 75
- Humaniser pass 1 (this check): HL 80  ← HIGHEST → KEPT
- Final 05b = humaniser pass 1. Loop ends on PASS at pass 1 (within MAX_GEMINI_PASSES=2).
- `gemini` column: `human 80`.

Remaining pass-2 notes (staccato in board-setup, "по две неща" signpost, one residual
"Оттук нататък", "тоест" over-define, "Защото" paragraph opener) are style suggestions on a
draft that already clears the bar at 80; not applied (loop ends on PASS, and further passes
risk lowering HL below the kept best per keep-best discipline).

## Gemini verbatim verdict + recommendations (pass 2)

### **Verdict: Likely human-written (or heavily human-edited), 80% confidence.**
**Reasoning:** The text contains highly idiomatic, culturally accurate Bulgarian phrasing that LLMs almost never generate organically (e.g., *"колкото и да ти отърва"*, *"за една ракия"*, *"цял живот спориш кой как ги разбира"*). An AI writing in Bulgarian tends to be overly formal or uses literal translations of English idioms. However, while the vocabulary is distinctly human, the **structural pacing and transitions** exhibit several classic AI-like formulaic habits.

#### 1. Pattern: Staccato Rhythm / Monotonous Syntax
> *"Дъската има двайсет и четири полета, подредени в четири групи по шест. По средата минава барът и дели дъската на две половини. Всеки играч има по петнайсет пула и ги мести с хвърлянето на два зара."*
Recommendation: Vary the sentence lengths and structures.

#### 2. Pattern: Mechanical Signposting
> *"Трите игри се различават по две неща: накъде вървят пуловете и какво става, когато срещнеш самотен противников пул."*
Recommendation: Remove the numerical signposting ("по две неща").

#### 3. Pattern: The Robotic Pivot (Meta-announcement)
> *"Оттук нататък говорим за обикновената табла."*
Recommendation: Delete this meta-announcement entirely.

#### 4. Pattern: Mid-Sentence Over-defining
> *"Изваждането, тоест изкарването на пуловете от дъската, започва едва след като..."*
Recommendation: Choose just one term.

#### 5. Pattern: The "Because" Transition
> *"Защото „табла“ не е една игра."*
Recommendation: Connect this thought directly to the previous paragraph.

*Note: The responsible gambling section, affiliate disclosures, and 18+ markers at the bottom are perfectly formatted for compliance. Left entirely unflagged and untouched.*
