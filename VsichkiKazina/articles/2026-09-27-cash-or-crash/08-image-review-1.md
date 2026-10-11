# 08 — Image review, pass 1 (Cash or Crash)

Command: python3 scripts/gemini_image_review.py VsichkiKazina/articles/2026-09-27-cash-or-crash/05b-final-draft.md \
         VsichkiKazina/articles/2026-09-27-cash-or-crash/images/cash-or-crash-staldata-i-rtp-infografika.svg

RESULT: GEMINI_UNAVAILABLE (HTTP 402). gemini_image_gen.py also 402 → AI hero SKIPPED.
Per daily-run.md Step 8: image review skipped (Gemini unavailable) — DO NOT halt, keep the image.

Manual integrity self-check (author):
- Numbers trace to 05b VERBATIM: 28 топки; 19 зелени / 8 червени / 1 златна; стълба 20 нива; връх 18 000x без
  златна, до 50 000x със златна; RTP ≈ 99,59% (ранен кешаут) и ≈ 94,51% (гонене на върха); домашно предимство
  ≈ 0,41% до 5,49%; трите решения Вземи всичко / Вземи половината / Продължи. All present in 05b. ✓
- No fabricated figure; per-strategy RTP shown only for the two extremes + edge; multipliers примерни. ✓
- No operator logos/names; Evolution named only as maker (matches 05b); no fake screenshots, no invented
  bonus/licence, no euro max-win cap invented. ✓
- No people/faces, no glamorised winning; carries „18+ Играйте отговорно" + „Стойностите зависят от версията" note. ✓
- XML-valid (checked with xml.dom.minidom: OK). viewBox 0 0 720 390, card #0f172a, Arial, headers #93c5fd,
  right-anchored values, note box #111f38. Two subcolumns in the composition block (left labels x48 → values
  x350; right labels x384 → values x688); RTP block three rows with separators at y244/272/300, values right-
  anchored x688; note-box text within its rect; ≥16px side margin. Longest right value „до 50 000x" @13px right-
  anchored x688 vs label „Връх със златна" ending ~495 → no overlap; „≈ 0,41% до 5,49%" starts ~600, label ends
  ~205 → clear. ✓
Decision: KEEP (1 infographic). images: 1 (infographic, review skipped — API down).
