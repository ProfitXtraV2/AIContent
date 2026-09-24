# 07 — Gemini Step-7 external check · pass 1 (INITIAL DRAFT)

Model: gemini-3.1-pro-preview. Brand: vsichkikazina.

**Detector variance note:** two back-to-back identical calls on the initial 05b returned
**85%** then **75%** confidence of human authorship (same draft, noisy detector). Highest
human-likeness seen for the initial draft = **85** (recorded for keep-best). Both readings
flag the SAME real tells (signposting crutches, conditional hook, binary parallelism,
link-dump), so a single Humaniser pass to remove them is warranted regardless of which
reading is canonical. Verbatim verdict from the captured (75%) call below.

---

**Verdict: Heavily Human-Edited AI or Highly Competent Human (75% Confidence of Human Authorship)**

This is a very strong piece of copy. If an LLM generated this, it was guided by an exceptional prompt and heavily edited by a human who understands the casino niche deeply. It successfully avoids the worst AI clichés (no "In conclusion," no "Delve into," no overly enthusiastic marketing fluff). The tone is refreshingly cynical and realistic, especially regarding casino math ("обикновено те изяжда по-бързо", "не поредната фабрика за бързи заглавия").

However, there are lingering structural tells—specifically in how the text transitions between ideas and how it handles SEO requirements—that still trigger AI/content-mill detection patterns.

### 1. The Formulaic "If X, then Y" Hook
Passage: *"Ако въртиш плодови барабани или тръгваш след съкровище в българско онлайн казино, има шанс зад играта да стои Belatra."*
Recommendation: Drop the conditional setup. State Belatra's prevalence as a fact.

### 2. Conversational Signposting (Hand-holding)
Passages: *"Дотук добре."* · *"И още нещо, което лесно се обърква."* · *"Ето кое лесно се пропуска."*
Recommendation: Delete these micro-transitions entirely; let the facts connect themselves.

### 3. The "Two Sides" Parallelism
Passage: *"Стилово Belatra живее на два адреса. Единият е... Другият са..."*
Recommendation: Soften the rigid Address 1 / Address 2 structure; blend the contrast.

### 4. The SEO Link-Dump Paragraph
Passage: the demo/RTP/провайдъри cluster before the RG block.
Recommendation: Break it up so the links breathe; separate gameplay advice from site navigation. (Do NOT alter the RG sentences that follow.)

### Process Note
`[VERIFY: точната държава и седалище днес...]` left in text under the first H2 — untouched, flagged for the human editorial workflow.

**Verdict → human-likeness: 85 (best of 85/75). PASS threshold is 80. Applying one Humaniser pass anyway to remove the flagged crutches, then re-check and keep-best.**
