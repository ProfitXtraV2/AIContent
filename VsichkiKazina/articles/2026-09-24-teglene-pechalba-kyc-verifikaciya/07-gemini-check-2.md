# Step 7 — Gemini cross-model check · PASS 2
Model: gemini-3.1-pro-preview · run 24.09.2026 · input: 05b after Humaniser pass 1.

## VERDICT
**Shows AI patterns, 85% confidence** → normalized human-likeness = 100 − 85 = **15** → below 80. Detector noisier/harsher than pass 1 (25). One more Humaniser pass allowed (cap = 2); keep-best across versions.

## Flagged patterns (verbatim from Gemini)
1. „Contrast / not just" hooks: „...не са едно и също нещо. Между тях стои една процедура..."; „Верификацията не е прищявка на казиното." → start from the practical/legal reality directly.
2. Dramatic signposting / artificial tension: „Едно нещо бави хората повече от всичко друго."; „Има и по-незабележим капан." → flatten, merge setup into the fact.
3. „Neat bow" resolutions: „Всяка от тях се решава по един и същ начин: изряден комплект документи..."; „Изрядните документи и съвпадащите данни свалят точно онези дни забавяне..." → delete/soften the summarizing closers.
4. Staccato list-intro rhythm: „Пътят изглежда така:"; „Повечето забавяния идват от няколко ясни причини:" → vary/integrate.
Process note: two [VERIFY] tags present — Gemini correctly does NOT touch them.

## Recommendations to apply (fresh Humaniser pass 2, untouchables preserved)
- Rewrite intro to open on the practical reality (withdrawal needs a KYC check before money moves), not the balance-vs-account contrast.
- Open the KYC section on the AML/legal requirement directly, drop „не е прищявка".
- Replace „Едно нещо бави хората..." with the direct fact (mismatched name/address is the most common delay).
- Merge the pending-reversal warning into a plain factual sentence, drop „по-незабележим капан" setup.
- Cut the two neat-bow closers.
- Vary the two list-intro lead-ins.
- PRESERVE: numbers, both [VERIFY] flags, verbatim 18+ RG line + block, byline/brand, 4 internal links.
