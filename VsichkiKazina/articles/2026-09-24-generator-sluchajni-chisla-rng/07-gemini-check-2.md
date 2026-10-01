# 07 — Gemini external check · pass 2 · vk-0167
Model: gemini-3.1-pro-preview. Ran on 05b after Humaniser pass 1 (step-7b: dropped the "behind the curtain" hook, cut meta-discourse and 3 dramatic pivot sentences, broke the "not X but Y" conclusion).

VERDICT (verbatim): "Shows strong AI patterns, 85% confidence."
Normalised human-likeness = 100 − 85 = **15** → below 80 AND lower than pass 1 (25). Detector noisy/adversarial for this explainer shape.

New flags raised (different from pass 1): rule-of-three personification („Барабаните нямат памет, нито сметка да изравнят, нито съчувствие"), staccato "not X, not Y" parallelism, melodramatic framing („Две скъпи илюзии си отиват", „нищо повече"), didactic "doesn't do A, does B" (TRNG не смята. Той измерва). Recs: combine mirrored pairs, strip personification, tone down drama, soften didactic transitions. Compliance/RG/[VERIFY] untouched (Gemini confirmed).
→ One more Humaniser pass applied (pass 2), then re-check (pass 3).
