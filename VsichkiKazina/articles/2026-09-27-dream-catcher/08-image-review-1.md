# 08 — Image review, pass 1 (Dream Catcher)

Command: python3 scripts/gemini_image_review.py VsichkiKazina/articles/2026-09-27-dream-catcher/05b-final-draft.md \
         VsichkiKazina/articles/2026-09-27-dream-catcher/images/dream-catcher-koleloto-i-rtp-infografika.svg

RESULT: GEMINI_UNAVAILABLE (HTTP 402). gemini_image_gen.py also 402 → AI hero SKIPPED.
Per daily-run.md Step 8: image review skipped (Gemini unavailable) — DO NOT halt, keep the image.

Manual integrity self-check (author):
- Numbers trace to 05b VERBATIM: 54 полета; 1→23, 2→15, 5→7, 10→4, 20→2, 40→1 полета, множители 2x и 7x
  по 1 поле (52 числови + 2 множителни = 54); число „1" плаща 1:1, „40" плаща 40:1; RTP „10" ≈96,58%
  (най-висок), „40" ≈90,81% (най-нисък); таван 500 000 € на залог. ✓
- No fabricated figure; per-bet RTP shown only for the two extremes (10 highest / 40 lowest — the
  cross-source consensus); multipliers примерни. ✓
- No operator logos/names; Evolution named only as maker (matches 05b); no fake screenshots, no invented
  bonus/licence. ✓
- No people/faces, no glamorised winning; carries „18+ Играйте отговорно" + „Процентите зависят от версията" note. ✓
- XML-valid (viewBox 0 0 720 390, card #0f172a, Arial, headers #93c5fd, right-anchored values @ x350/x688,
  note box #111f38). Text-extent check per formula: right sub-column label „Число „40"" @13px ends ~440,
  value „1 поле" right-anchored x688 → no overlap; „500 000 € на залог" value right-anchored, label „Таван на
  печалбата" ends ~185 → clear; „≈ 96,58%" / „≈ 90,81%" right-anchored, labels end ~245 → clear; note-box
  text within its rect; ≥16px margins. ✓
Decision: KEEP (1 infographic). images: 1 (infographic, review skipped — API down).
