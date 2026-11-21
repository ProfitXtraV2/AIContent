# 07 — Gemini external check · pass 3 (after humaniser pass 2) · vk-0341 Етър Велико Търново

**Script:** `python3 scripts/gemini_check.py 05b-final-draft.md` · exit 0 · GEMINI ONLINE
**Verdict (verbatim):** Likely human-written (or heavily human-edited), **85%** confidence → **human-likeness = 85**. **PASS** (≥ 80).

**Keep-best progression (human-likeness):** pass-1 baseline **15** → humaniser p1 → pass-2 **20** → humaniser p2 → pass-3 **85**. Winner = current 05b (humaniser pass 2), **human 85**. No earlier version scored higher, so the current draft is kept. Loop ends on PASS before the cap.

---

**Verdict: Likely human-written (or heavily human-edited), 85% confidence.**

This article reads exceptionally well and contains native, highly contextual Bulgarian idioms that standard LLMs almost never generate organically (e.g., *"отборът вече е чукал на вратата, преди да я избие"*, *"пресен германски шампион"*, *"без да се менят с модата"*). The narrative voice is opinionated and grounded.

However, the article relies on a rigid SEO outline, and in bridging the gaps between these H2 sections, the writer (or the AI assisting them) falls back on a few classic AI-style transitional patterns and signposting.

### Flagged Passages, Patterns, and Recommendations
1. **Formulaic Intro Wrap-up (Summary Signposting)** — *"Заради тези две неща клубът се помни и днес, трийсет и повече години след онова лято."* — immediate "Because of X and Y..." summary halts the opening's momentum; delete or weave in.
2. **Robotic Transition / Filler Opening** — *"Около титлата клубът трупа и други успехи."* — generic zero-information glue sentence; cut and start on the concrete fact (Купа на БФС 1991).
3. **The Generic "Door Opening" Cliché** — *"Титлата отваря вратата към най-силния клубен турнир."* — "opens the door to" default transition; merge into the historical fact.
4. **Didactic / Over-explanatory Comparison** — *"...върши работа, каквато мнозина с по-голям бюджет не вършат."* — slightly preachy budget comparison; tighten to the scale of the achievement.

### Process Note (hard rules respected)
- **[VERIFY] flag:** `[VERIFY: точен капацитет на „Ивайло“...]` noted, NOT touched; stays in text for the human fact-check team.
- **RG / disclosures:** all 18+ markers, affiliate disclosures and responsible-gambling language left entirely intact and un-critiqued, as required.

**Decision:** PASS at human-likeness 85 on the final allowed pass. The four remaining nits above are optional, non-blocking polish and are left for the human editor (applying them risks lowering the score; keep-best mandates holding the 85 version). gemini column → `human 85`.
