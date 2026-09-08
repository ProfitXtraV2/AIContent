# Step 7 — Gemini check, pass 1 (initial 05b)

Model: gemini-3.1-pro-preview
Normalized: **"Shows AI patterns, 85% confidence"** → human-likeness = **100 − 85 = 15** → below target (80). Iterate: one Humaniser pass on the flagged patterns, then re-check. Keep-best tracked (baseline HL 15).

---

**Verdict: Shows AI patterns, 85% confidence.**

Disciplined and factual, but relies on structural AI tropes plus one literal-translation anglicism.

1. **Anglicism (dead giveaway)** — „**подписната** прогресивна система" is a literal calque of "signature progressive system"; „подписна" means a document signature in Bulgarian. → replace with „емблематичната" / „запазената марка на" / drop the adjective.
2. **Didactic signposting** — „...математика, **която си струва да разбереш, преди да завъртиш.**" and „**Тук е важно да си наясно** откъде идват тези пари." → strip meta-commentary; deliver the fact directly.
3. **Formulaic summary conclusion** — „20 Super Hot дава семпло, бързо забавление... **подсладено**..." + „Под визията стоят под-среден RTP..." → delete the recap sentences; start the final section on the actionable advice.
4. **Forced contrast / narrated emotion** — „...лесно се пропуска зад носталгичната визия." and „...точно затова е примамлив и опасен едновременно." → cut the philosophical contrasts; let the mechanics speak.

*(Process note: [VERIFY] release-year flag + 18+/RG left untouched — flags stay in text for the human.)*

(Applied in Humaniser pass 1 → re-checked in 07-gemini-check-2.md.)
