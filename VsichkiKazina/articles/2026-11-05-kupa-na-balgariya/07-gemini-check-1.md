# 07 — Gemini check — pass 1 (baseline draft)

**Verdict: Shows AI patterns, 85% confidence.**
**Normalized human-likeness = 100 − 85 = 15.** Below GEMINI_TARGET_CONFIDENCE (80) → iterate (humaniser pass 1).

Gemini's verbatim verdict + recommendations (style-only; facts/numbers/links/RG untouched):

---

While the article is grammatically flawless and follows a logical structure, it heavily relies on classic Large Language Model (LLM) stylistic tropes. It exhibits the typical AI "balanced antithesis" (perfectly mirrored contrasting sentences), over-explains basic concepts, uses conversational hedging to avoid stating absolutes, and relies on formulaic signposting. The concluding thoughts also drift into the philosophical, preachy tone AI often adopts when handling gambling-related topics.

### 1. Dramatic Parallelism & Antithesis
*   Flagged: „Първенството възнаграждава постоянството през дълъг сезон, купата награждава този, който издържи поредица мачове на живот и смърт."
*   Flagged: „в лигата грешките се поправят до пролетта, в купата втори шанс няма."
*   Recommendation: Tone down the melodrama. Remove the „живот и смърт" cliché. Break the perfect symmetry.

### 2. Didactic Over-explaining
*   Flagged: „Турнирът е на директни елиминации. Който загуби, отпада веднага, а победителят продължава към следващия кръг."
*   Recommendation: Delete the second sentence entirely. Trust the reader's basic sports literacy.

### 3. Conversational Hedging & Meta-Commentary
*   Flagged: „Точният брой участници и двойки се мени от сезон на сезон, затова няма смисъл да се помни наизуст; важното е принципът."
*   Flagged: „...затова за актуалната подредба е по-разумно да се погледне официалният регламент, вместо да се приема за заковано."
*   Recommendation: Strip the conversational filler. State the facts directly: note that the exact number of participants and European quotas fluctuate annually based on UEFA rankings and tournament phases.

### 4. Formulaic Signposting
*   Flagged: „Безспорното е друго."
*   Flagged: „Любопитен детайл е, че..." (the Bulgarian equivalent of „It is worth noting that...").
*   Recommendation: Cut these transitional crutches. Start sentences directly with the subject.

### 5. Philosophical/Robotic Conclusions
*   Flagged: „Миналите финали в Купата на България носят точни дати и имена. Изходът от следващия двубой не се знае предварително и никой залог не го гарантира."
*   Recommendation: Ground the conclusion. Tie unpredictability to the nature of the Cup (eliminations/upsets) and frame as a practical reminder for setting betting limits.

### Process Note: Unresolved Editorial Tags
*   Flagged: `[VERIFY: 27]` and `[VERIFY: 22]` — NOT removed/resolved (per instructions). Workflow note: title-count verification tags to be manually checked/cleared by the editorial team before publication.

---

**Action:** apply style recs 1–5 via step-7b humaniser (preserve every number, link, RG line, 18+, disclosure, date, byline, brand; keep the two [VERIFY] tags). Re-check.
