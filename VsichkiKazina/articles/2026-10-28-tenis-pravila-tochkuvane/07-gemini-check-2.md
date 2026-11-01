# 07 — Gemini check, pass 2 (after humaniser pass 1)

Command: `python3 scripts/gemini_check.py VsichkiKazina/articles/2026-10-28-tenis-pravila-tochkuvane/05b-final-draft.md`

Normalized human-likeness: **90** ("Likely human-written, 90% confidence") → **PASS** (≥ 80).

## Gemini verbatim verdict + recommendations

**Verdict: Likely human-written, 90% confidence.**

### 1. The "Demystification" Hook
> Quote: "Звучи странно, докато не схванеш стълбицата; щом тя ти е ясна, цялата система се нарежда сама, от първата топка до последния сет."
> Pattern: Over-promising setup / Meta-commentary. Recommendation: delete the meta-commentary, start directly with the scoring system.

### 2. Explicit Signposting & Forced Pivots
> Quote: "Дотук е просто броене с необичайни имена. Усложнението идва при 40-40..."
> Quote: "Проблемът е, когато двамата стигнат 6-6 и никой не може да откъсне нужните два гейма. Тогава идва тайбрекът."
> Pattern: Problem-Solution transition glue. Recommendation: let the H2s carry the pivots; state the rule plainly.

### 3. Narrated Emotion / Faux Relatability
> Quote: "В тайбрека броенето най-сетне става нормално: 1, 2, 3 и нагоре."
> Pattern: forced "finally" (най-сетне). Recommendation: "В тайбрека точките се броят стандартно: 1, 2, 3..."

### 4. The Neat Philosophical Bow
> Quote: "Приятно предание, но точният произход не е документиран със сигурност."
> Quote: "Сигурна печалба от залог върху когото и да било няма, и точно това е единствената гаранция в цялата схема."
> Pattern: AI wrap-up / summarising bow. Recommendation: trim the closing flourishes.

**Compliance note (Gemini):** the money section + footer (За Всички Казина / Отговорна игра /
Разкриване на партньорства, НАП, 18+, Aug-2026 affiliate law) are excellent; per hard rules do
NOT touch any of it.

## KEEP-BEST decision
- Human-likeness by state: initial draft (pass 1) = **85**; after humaniser pass 1 (current 05b)
  = **90**. Both PASS (≥ 80).
- Winner = **pass 2 state (HL 90)** — the current 05b. Keep it.
- STOP here (MAX_GEMINI_PASSES = 2 reached; score is already 90 and rising). Pass-2 recs are the
  detector relocating goalposts on an already-passing, rising draft (same whack-a-mole pattern
  documented on prior articles). Over-applying them risks lowering HL and stripping genuine voice;
  per keep-best + never-pad/never-over-humanise, the HL-90 version stands.
- `gemini` column: **human 90**.
- Every number, internal link, RG line, 18+, disclosure, date, byline and brand preserved verbatim
  across both passes (verified: 0 em-dashes, scoring numbers identical to 02/03/04).
