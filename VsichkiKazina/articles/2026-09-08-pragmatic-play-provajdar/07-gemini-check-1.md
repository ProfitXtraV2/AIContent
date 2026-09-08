# Step 7 — Gemini check, pass 1 (initial 05b)

Model: gemini-3.1-pro-preview
Normalized: **"Shows AI Patterns, 75% confidence"** → human-likeness = **100 − 75 = 25** → below target (80). Iterate: one Humaniser pass on the flagged patterns, then re-check. Keep-best tracked (baseline HL 25).

---

**Verdict: Shows AI Patterns, 75% Confidence.**

Highly readable, factually dense, free of the worst AI fluff, but the skeleton relies on LLM structural tropes: formulaic transitions, signposting and "neat bow" paragraph resolutions.

1. **Signposting / meta-commentary** — *"Този профил обяснява какво всъщност прави тя, кои са познатите ѝ заглавия и какво не се променя..."* → delete; dive in.
2. **Didactic "important to note" variant** — *"Това е важно, но е лесно да се разбере погрешно."* → delete; connect facts directly.
3. **"Neat bow" paragraph resolution** — *"Всичко това променя усещането и темпото, но нито една от тези механики не добавя пари извън RTP..."* → end the mechanics paragraph on a concrete detail (Megaways), not a synthesized summary.
4. **Aphoristic transition** — *"Голямото име на доставчика е удобна отправна точка, не гаранция."* → delete; start with the actionable advice.
5. **Formulaic summary** — the whole "Накратко" recap → cut or replace with a single forward-looking next-step thought (short article needs no recap).

*(Process note: [VERIFY] HQ flag + 18+/RG disclosures present and correct — do not touch.)*

(Applied in Humaniser pass 1 → re-checked in 07-gemini-check-2.md.)
