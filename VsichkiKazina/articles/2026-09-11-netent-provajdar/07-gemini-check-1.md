# 07 — Gemini external check, pass 1 (gemini-3.1-pro-preview)

Verdict: **Shows AI patterns, 85% confidence** → human-likeness = 100 − 85 = **15**.

## Flagged patterns (verbatim summary)
1. "X, not Y" didactic conclusion appended to ~every paragraph (robotic expectation management):
   - „...не че връщат повече." / „...а не предимство за сметката ти." / „...не по-щедро." /
     „...не че тези правила са в твоя полза." / „...не игра, която накрая ти връща повече." /
     „...отколкото за шансовете ти." / „...не ти връща повече..." / „...не за твоята вечер."
   Fix: keep the RG/boilerplate to do that job; strip ~70% of these micro-disclaimers; keep the
   „X, not Y" contrast only where it fits best (RTP or License), delete elsewhere.
2. Forced relatability / presumptuous „you": „дори да не си забелязал логото" / „приемаш за
   даденост" / „За теб като играч тази биография не значи нищо магическо". Fix: state impact
   objectively; drop the conversational padding.
3. Formulaic rhythm premise→elaboration→warning; Sections 3 & 5 both list exactly four items then
   end on the same wallet warning. Fix: vary paragraph endings (cultural impact of Gonzo's Quest,
   volatility of Dead or Alive, how Avalanche changed slot design industry-wide).

Note (Gemini): RG language, 18+, affiliate disclosures are correct — do NOT alter; recs apply to
descriptive body only.

Decision: below 80 → apply recs via fresh Humaniser pass (step-7b), preserve every untouchable
(numbers, links, RG, 18+, dates, byline, brand), then re-check. Record HL 15 for keep-best.
