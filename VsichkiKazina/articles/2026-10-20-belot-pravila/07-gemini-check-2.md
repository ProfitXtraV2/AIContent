# 07 — Gemini external check, pass 2 (after Humaniser pass 1)

Command: `python3 scripts/gemini_check.py VsichkiKazina/articles/2026-10-20-belot-pravila/05b-final-draft.md`
Date: 2026-10-20

**Normalized human-likeness = 90** (verdict "Highly likely human-written, 90% confidence" → 90). ABOVE target 80 → **PASS**.

## KEEP-BEST DECISION
- Initial draft (check 1): HL **15** ("Likely AI-generated, 85%").
- Humaniser pass 1 (this check): HL **90** ("Highly likely human-written, 90%").
- Highest human-likeness seen = **pass 1 = 90**. Loop ends by PASS (no pass 2 needed; well inside MAX_GEMINI_PASSES=2).
- FINAL 05b = the Humaniser-pass-1 version (already the committed state). Recorded in content-queue as `human 90`.
- The micro-pattern recommendations below are optional polish only (we are at PASS 90); NOT applied — keeping the best-scoring version per keep-best discipline, and avoiding a further pass that could lower the score.

## Gemini verbatim verdict + recommendations

**Verdict: Highly likely human-written, 90% confidence.**

This is an exceptionally strong piece of Bulgarian copywriting. It completely avoids the standard traps of AI-generated Bulgarian (which usually suffers from clunky literal translations, passive voice, and repetitive transitional adverbs like "Освен това" or "Важно е да се отбележи").

The text uses rich, highly idiomatic phrasing that LLMs rarely generate organically in Bulgarian—phrases like "минава на две порции", "щом паднат три последователни паса", "точките висят", and "отгоре идват анонсите". The rhythm is varied, and the tone is authoritative yet conversational.

However, if we are looking through a microscope, there are a few micro-patterns that carry a faint "AI scent" or feel like forced SEO copywriting. Here is what triggered my radar and how to tighten it up.

### Flagged Passages & Recommendations

**1. Pattern: Forced SEO Signposting / Cross-linking**
- The Quote: "Същата логика на последователни карти важи и при [комбинации в покера](/blog/poker-kombinacii/), където подреждането е разписано по-подробно."
- The Issue: This is a classic SEO-driven insertion. While grammatically perfect, it breaks the reader's immersion. Right in the middle of explaining a Belot-specific rule (квинта/сто), the text suddenly pivots to poker just to satisfy an internal linking requirement.
- Recommendation: Move this cross-link to the end of the paragraph as a standalone "Вижте също", or weave it in without the explanatory "където подреждането е разписано по-подробно".

**2. Pattern: Literal Translation / Unnatural Terminology**
- The Quote: "Разпръсната ръка, богата на аса и десетки, клони към „Без коз" или „Всичко коз"."
- The Issue: "Разпръсната ръка" reads like a direct translation of "scattered hand". Not authentic Belot slang.
- Recommendation: Use "шарена ръка" or a hand "без дълга боя".

**3. Pattern: The "Academic" Descriptor**
- The Quote: "Без коз редът е интуитивният: Асо, десятка, Поп..."
- The Issue: LLMs love "интуитивен" to describe standard processes; stiff in a casual card-game guide.
- Recommendation: Swap "интуитивният" for "стандартният" / "обичайният" / "нормалният".

**4. Pattern: The Mini-Conclusion (Summarizing Wrap-up)**
- The Quote: "Една ръка с голямо каре и терца може да стигне прага по-бързо от няколко редови ръце, така че анонсите решават изхода също толкова, колкото редовната игра."
- The Issue: The "така че..." construction is a classic wrap-up pattern that over-explains.
- Recommendation: Delete the "така че..." clause; let the first half stand.

*(Note: The responsible gambling section, legal disclosures, and dates at the bottom were reviewed but left untouched as per your hard rules. They are perfectly formatted for compliance.)*
