# 07 — Gemini check, pass 1 (initial draft)

**Verdict: Likely human-written (or heavily human-edited), 80% confidence.**
→ human-likeness = **80** → **PASS** (≥ GEMINI_TARGET_CONFIDENCE 80).

Final RG section reads 100% human. Four stylistic AI-tells flagged in the historical half
(recommendations only; facts/numbers/RG/links untouchable):

1. **"It all started when" crutch** — „Всичко започва на 6 март 1902 г., когато е основан…"
   → lead directly with the date + original name, drop the preamble.
2. **"No coincidence" framing** — „Не е случайно, че през 2000 г. ФИФА обяви…"
   → state the FIFA recognition as a direct, punchy fact.
3. **Universal platitude** — „Списъкът с имена… е дълъг и познат дори на хора, които не следят футбол."
   → cut the generalization, open straight on the players/eras.
4. **"Not only X, but Y" wrap-up** — „Зад тях стои не само спортът, а и дълга история между двата града."
   → replace with a sharper, specific statement.

Decision: PASS already met at 80. Run ONE targeted Humaniser pass (step-7b) applying these
four surgical fixes, re-check, keep the highest human-likeness (keep-best).
