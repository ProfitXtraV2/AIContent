# 07 — Gemini external check · pass 1 (baseline) · vk-0341 Етър Велико Търново

**Script:** `python3 scripts/gemini_check.py 05b-final-draft.md` · exit 0 · GEMINI ONLINE
**Verdict (verbatim):** Shows AI patterns, **85%** confidence → **human-likeness = 15** (100 − 85). NEEDS CHANGES (< 80).

---

### Verdict
**Shows AI patterns, 85% confidence.**
While the article is factually dense, grammatically flawless, and clearly human-verified (as evidenced by the surviving `[VERIFY]` tag), the stylistic skeleton is heavily reliant on classic generative AI cadences. It suffers from philosophical padding, predictable paragraph structures (opening with a sweeping statement, ending with a poetic summary), and formulaic transitions.

### Specific Passages and Patterns Flagged
1. **The "Roadmap" Signposting** — *"Ето откъде идва името на клуба от Велико Търново, как се роди онази титла и защо хората около нея се помнят и до днес."* — LLMs end an intro by explicitly listing the next sections.
2. **Philosophical/Cliché Openings (Narrated Emotion)** — *"В българския футбол столичните клубове обикновено пишат заглавията, а провинцията гледа отстрани."* · *"Клуб се помни през хората, носили фланелката..."* · *"Върхът не трае вечно."* — warming up with universal truths instead of a hard fact.
3. **The "Not Just X" / "Doesn't Come From Nowhere" Formula** — *"Големият сезон не идва от нищото."* · *"Това не е просто съвпадение на биографии."* — artificial contrast/tension crutch.
4. **Sweeping, Poetic Conclusions (Over-moralizing)** — *"...който се помни не с пари, а с един сезон на достойнство срещу по-богати противници."* · *"Следващата глава на търновския футбол никой не я е обещал предварително, но тази, старата, вече е написана и заслужено стои в разказа за България."* — textbook LLM grand finale.
5. **Process Issue: Surviving Editor Tags** — `[VERIFY: точен капацитет на „Ивайло“...]` flagged as a process leak (NOT asked to remove; stays per our rules).

### Concrete Recommendations
- **Kill the roadmap:** delete *"Ето откъде идва името на клуба..."*.
- **Cut the philosophical warm-ups:** in the intro remove the capital-vs-provincial thesis and start on Etar's 1991 achievement; in „Златното поколение" start directly on *"През онзи период през Велико Търново минават..."*; in „Какво стана после" delete *"Върхът не трае вечно."* and open on the hard fact.
- **Flatten artificial transitions:** remove *"Големият сезон не идва от нищото."* and *"Това не е просто съвпадение на биографии."*; let the facts speak.
- **Ground the conclusion:** replace the "next chapter / story of Bulgaria" metaphor with a grounded factual close.
- **VERIFY tag:** route to a human to resolve (kept in text). RG language + 18+ markers are perfectly integrated and should remain exactly as they are.

**Action:** apply a fresh Humaniser pass (step-7b) addressing 1–4; preserve every number, link, RG line, 18+, disclosure, date, byline, brand; keep the [VERIFY] flag. Record human-likeness per pass and keep the best.
