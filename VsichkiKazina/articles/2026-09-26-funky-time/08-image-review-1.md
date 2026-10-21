# 08 — Image review, pass 1 (Funky Time)

Command: python3 scripts/gemini_image_review.py VsichkiKazina/articles/2026-09-26-funky-time/05b-final-draft.md \
         VsichkiKazina/articles/2026-09-26-funky-time/images/funky-time-koleloto-i-rtp-infografika.svg

RESULT: GEMINI_UNAVAILABLE (HTTP 402). gemini_image_gen.py also 402 → AI hero SKIPPED.
Per daily-run.md Step 8: image review skipped (Gemini unavailable) — DO NOT halt, keep the image.

Manual integrity self-check (author):
- Numbers trace to 05b VERBATIM: 64 полета; 1→28, букви→24, Bar 6/Disco 3/Stayin' Alive 2/VIP Disco 1 (12 бонус);
  1:1 и 25:1; RTP 1 ≈95,99% (най-висок), VIP Disco ≈95,38% (най-нисък); таван 500 000 € на залог. ✓
- No fabricated figure; per-bet RTP shown only for the two extremes (numbers agree across sources); multipliers примерни. ✓
- No operator logos/names; Evolution named only as maker (matches 05b); no fake screenshots, no invented bonus/licence. ✓
- No people/faces, no glamorised winning; carries „18+ Играйте отговорно" + „процентите зависят от версията" note. ✓
- XML-valid (viewBox 0 0 720 390, card #0f172a, Arial, headers #93c5fd, right-anchored values, note box). Text-extent check
  per formula: right sub-column label „Stayin' Alive (бонус)" @13px ends ~490, value „2 полета" right-anchored x688 → no overlap;
  „500 000 € на залог" value starts ~543, label „Таван на печалбата" ends ~193 → clear; note-box text within its rect; ≥16px margin. ✓
Decision: KEEP (1 infographic). images: 1 (infographic, review skipped — API down).
