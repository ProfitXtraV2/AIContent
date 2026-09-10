# Step 7 — Gemini check, pass 4 (this run's baseline, MAX_GEMINI_PASSES=5)

Model: gemini-3.1-pro-preview (scripts/gemini_check.py) · temp 0.2 · recommendations only.
Article checked: `05b-final-draft.md` as inherited from the prior run (Humaniser pass 2).

## Normalized score
Official first read of this run: **"Highly likely human-written (90% confidence)"** → human-likeness = **90**.

## Stability note (important — the score is noisy on this draft)
Three back-to-back reads of the SAME file returned:
- Read A (official): "Highly likely human-written, 90%" → **90**
- Read B: "Shows AI patterns, 75%" → **25**
- Read C: "Likely human-written (or heavily human-edited), 85%" → **85**

The draft sits right on the detection threshold: 2 of 3 reads clear 80, one falls to 25.
Consensus recommendation is therefore to strengthen the recurring structural tells so the
distribution moves reliably above 80, rather than banking a single lucky read.

## Consensus flags across the reads (safe to fix, no untouchables affected)
1. **Info-dump inline list** — the 10 hand rankings crammed into one comma-wall sentence
   ("От най-слабото към най-силното: висока карта, чифт …"). Break into a scannable
   enumeration (genuine 6+ item list — endorsed by humaniser.md list rule).
2. **Mid-article mini-conclusion** — "Разликата между форматите опира до това колко решения
   искат от теб …" prematurely summarises ALL formats at the end of the Три-карти section.
   Relocate its substance into the final buyer's-guide section.
3. **Textbook glossary phrasing** — the two back-to-back dictionary definitions of RTP and
   домашно предимство ("X е Y. Z е обратното на X: A"). Dissolve into a causal sequence.
4. **Didactic signpost / block-glue** — "Тази стълбица важи еднакво във всеки от форматите
   по-долу". Scrub the "по-долу" transition.
5. **"Matchmaker" close** — the symmetric persona-matching in "Кое да пробваш първо".
   Rebuild as an asymmetric, opinion-led recommendation (brand voice requires an opinionated
   close; keep the opinion, drop the template symmetry).
6. Softened the intro house-edge over-explanation ("публично изчислимо число" textbook cadence).

Plus the UPDATED BG AI-TELL targets: kill "не A, а B" paragraph-closers, demonstrative
amplifiers ("именно тази"), везни symmetry, translated idioms, reveal-before-explain.

Kept deliberately: the closing line "една таблица, която не се интересува колко силно ти се
играе" — flagged once as a mic-drop but praised in two reads as "brilliant, distinctly human";
it is an asymmetric opinionated close, brand-appropriate. Removing it would reduce human signal.

## Untouchables verified present and preserved (unchanged)
Numbers (RTP 98%, edge 2%, €100/€2), the illustrative-numbers parenthetical, links
(/kazino-igri/, /otgovorna-igra/ ×2, /kak-ocenyavame/), RG lines, 18+ markers, disclosures,
dates (07.09.2026), byline Георги Тодоров, brand Всички Казина.
