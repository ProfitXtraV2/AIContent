# 07 — Gemini external check · pass 1 (INITIAL draft) · vk-0036

Model: gemini-3.1-pro-preview · Date: 2026-09-10

## Verdict (verbatim)
**Shows AI patterns (Advanced LLM / Claude-style), 65% confidence.** → HUMAN-LIKENESS = 100 − 65 = **35**.

High-quality, idiomatic vocabulary ("защото таванът е таван", "издържа на четене"), but the structural skeleton relies on classic AI tropes: explicit signposting, forced staccato parallelism, dramatic two-part subheadings, and the "Not X, but Y" philosophical wrap-up. [VERIFY] + RG/affiliate disclosures noted as present, not touched (per hard rules).

## Flagged patterns
1. **Signposting intro** — "Тази статия разглобява механиката, за да знаете какво подписвате, преди да натиснете „Депозирай"." → announces purpose at end of intro.
2. **Forced parallelism / staccato** — "Внасяте €100 … балансът ви става €200. Внасяте €600, бонусът пак спира на €500…"; "Същият множител, двойно изискване." → too rhythmic/engineered.
3. **Over-polished dramatic subheadings** — "Превъртането е истинската цена, а базата решава всичко"; "Тихите ограничения: макс. залог и таван на тегленето" → two-part hook+function shape.
4. **Antithesis summary** — "Бонусът при регистрация не е подарък и не е капан; той е сделка…" → the "not X, not Y; ultimately Z" AI close (the single most recurring BG tell).

## Recommendations (to apply via Humaniser pass 1)
- Delete the signpost sentence; let "Договорът е в общите условия…" be the hook.
- Merge the €100/€600 staccato into one flowing sentence.
- Make subheadings functional (drop the dramatic second clause).
- Remove the "не е подарък и не е капан" antithesis; open the closer with the actionable advice directly.

## Decision
HL 35 < 80 → NOT PASS. Apply recommendations through fresh Humaniser pass (step-7b), preserve every untouchable, re-run gemini_check → 07-gemini-check-2.md.
