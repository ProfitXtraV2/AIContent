# 07 — Gemini check — pass 2 (after humaniser pass 1)

**Verdict: Shows AI patterns, 75% confidence.**
**Normalized human-likeness = 100 − 75 = 25.** Up from pass-1 HL 15. Still below 80 → one more humaniser pass (pass 2).

Gemini's verbatim verdict + recommendations (style-only; facts/numbers/links/RG untouched):

---

This article is actually quite good and avoids the most egregious AI clichés. It has a strong, punchy opening and a distinct voice. However, beneath the surface polish, it relies on classic LLM structural formulas: forced balance, tidy paragraph wrap-ups, and a pseudo-profound ending. Additionally, there is a workflow artifact: the image alt-text is a literal generative AI prompt.

### 1. Workflow Artifact: The Generative AI Prompt Leak
*   Passage: `![Плоска илюстрация на футболен трофей на тъмен фон с меко златисто сияние, в топли тонове; без клубни гербове, без лога, без хора](images/kupa-na-balgariya-trofej-hero.webp)`
*   Pattern: Prompt leakage — the alt-text is a direct copy of a generation prompt, not SEO/accessibility text.
*   Recommendation: Replace with a standard descriptive phrase (e.g. „Илюстрация на трофея от Купата на България по футбол").

### 2. Forced Balance / „Both are Valid" Trope
*   Passage: „…в които всяка грешка може да е последна. Затова и двата трофея се ценят, но по различни причини."
*   Recommendation: Delete the final sentence. The contrast is strong enough on its own.

### 3. The Tidy Wrap-Up (Bow-Tying)
*   Passage: „…колко тима влизат от долните дивизии. Именно този микс ражда изненадите, при които по-скромен отбор елиминира фаворит на собствения си терен."
*   Recommendation: Drop the „Именно този микс…" summarising frame; integrate the surprises point or let the facts stand.

### 4. The Pseudo-Profound Sign-Off
*   Passage: „Миналите финали в Купата на България вече имат имена и дати. Следващият мач още няма, и никой залог не го гарантира."
*   Recommendation: Ground the ending; remove the poetic past-vs-future contrast; a dry practical close is better.

### Note on Process (Hard Rules Observed)
`[VERIFY: 27]` / `[VERIFY: 22]`, RG disclosures and 18+ markers left untouched per instructions; [VERIFY] tags to be resolved and brackets removed by the fact-checker before publication.

---

**Action:** apply recs 1–4 via step-7b humaniser (ALT-text fix is a real improvement kept regardless of HL; hygiene constraints move into the image-gen prompt, not the ALT). Preserve every number, link, RG line, 18+, disclosure, date, byline, brand, and the two [VERIFY] tags. Re-check (pass 3). If still < 80 at the cap, KEEP BEST.
