# Step 7 — Gemini cross-model check — PASS 1 (baseline 05b)

**Date:** 2026-10-27
**Checked file:** 05b-final-draft.md (initial, pre-humaniser-recs)
**Model:** gemini-3.1-pro-preview

## Verdict (verbatim)
**Shows AI patterns, 75% confidence.**

→ Normalized HUMAN-LIKENESS = 100 − 75 = **25**  → below GEMINI_TARGET_CONFIDENCE (80) → iterate.

## Gemini's flagged passages & patterns (verbatim summary)
1. **"Prompted internal link" pattern (repetitive first-person signposting).** The "...съм я описал/събрал/разписал/разгледал в [link]" formula appears 4×, creating a robotic rhythm:
   - „...съм я описал стъпка по стъпка в [как се проверява лицензът на казино]."
   - „...събрал съм ги в [слотове с високо RTP]."
   - „...съм разписал отделно в [линии на печалба]."
   - „...съм разгледал в [прогресивни джакпоти]."
2. **Forced persona / overcompensated authority.** „Това не го приемам на доверие, разбира се. […] За мен, като автор във Всички Казина, одитираното RNG върви в комплект с лиценза…" — classic AI persona injection (announcing job title + brand mid-explanation).
3. **Didactic signposting / textbook transitions.** „Важното свойство тук е независимостта."; „Монетата го показва най-чисто."; „Най-полезно е да гледаш на RTP като на среден разход…"; „Прогресивните джакпоти са отделна история."
4. **"Goldilocks" symmetrical structure.** „Ниската волатилност дава… Високата те държи… Средната е някъде по средата." — the "medium is in the middle" filler sentence.

## Gemini's concrete recommendations (verbatim summary)
- Vary internal-link integration: drop the "I wrote about this here" formula; let the anchor text carry the link inside the educational sentence.
- Tone down the forced persona: remove the explicit self-reference to being an author at the brand; state the standard directly.
- Cut transitional throat-clearing: start paragraphs directly with the core idea (remove „Важното свойство тук е независимостта.", „Прогресивните джакпоти са отделна история.").
- Break the symmetrical volatility explanation: delete „Средната е някъде по средата."; make high/low contrast more fluid.

**Note (Gemini, verbatim):** the responsible-gambling language, 18+ markers, and limits advice are perfectly placed — do NOT alter or remove during edits.

## Decision
HL 25 < 80 → apply these style-only recs via a FRESH Humaniser pass (step-7b), preserving every number/link/RG line/byline/brand, then re-check (pass 2). Keep-best across baseline + passes.
