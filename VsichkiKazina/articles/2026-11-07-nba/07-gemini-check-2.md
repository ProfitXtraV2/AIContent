# 07 — Gemini Step-7 external check — pass 2 (after Humaniser pass 1)

**Command:** `python3 scripts/gemini_check.py VsichkiKazina/articles/2026-11-07-nba/05b-final-draft.md`
**Exit:** 0

## Verdict (verbatim)
**Likely human-written, 90% confidence.**
→ Normalized human-likeness = **90**. ≥ GEMINI_TARGET_CONFIDENCE (80) → **PASS**.

This is an exceptionally strong piece of copy. The text lacks almost all the classic LLM tells in
Bulgarian (no „В днешно време", „Важно е да се отбележи", „В заключение"). It uses highly idiomatic,
conversational phrasing that AI struggles to generate naturally in Bulgarian — „уталожено като
формат", „после не се пипа", „няма бонуси за стил", „се въртиш в онлайн казино". Rhythm punchy, tone
authoritative yet accessible.

Minor non-blocking notes Gemini still raised (at PASS, not acted on further):
1. Symmetrical pacing — most H2 sections run ~2 paragraphs of similar length.
2. One slightly staccato explanation („Устроен е на групи. …по пет, тоест шест групи общо.").
3. One textbook transition („Географски всичко е разделено на две половини.").

## Keep-best decision
- Baseline (07-gemini-check-1): HL 35 („Shows AI patterns 65%").
- Humaniser pass 1 → this check: HL **90** („Likely human-written 90%") = PASS.
- Highest human-likeness seen = **90 (pass 1)**. The current `05b` IS that winner → keep as-is.
- Loop ends on PASS at pass 1 of MAX_GEMINI_PASSES (2). No further humaniser pass needed (already
  ≥ 80; a further pass risks lowering HL per keep-best discipline).

**gemini column = `human 90`.** Style-only throughout; 0 facts/numbers/links/RG/dates/byline/brand
touched; „към есента на 2026 г." stamp preserved.
