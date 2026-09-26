# 08 — Image review, pass 1 (Monopoly Live)

Command: python3 scripts/gemini_image_review.py VsichkiKazina/articles/2026-09-26-monopoly-live/05b-final-draft.md \
         VsichkiKazina/articles/2026-09-26-monopoly-live/images/monopoly-live-koleloto-i-rtp-infografika.svg

RESULT: GEMINI_UNAVAILABLE (HTTP 402). gemini_image_gen.py also 402 → AI hero SKIPPED.
Per daily-run.md Step 8: image review skipped (Gemini unavailable) — DO NOT halt, keep the image.

Manual integrity self-check (author):
- Numbers trace to 05b VERBATIM: 54 полета; 22/15/7/4 (числа) + 2 Chance + 3 „2 Rolls" + 1 „4 Rolls"; 48/6;
  RTP най-добър ≈96,2%; таван 500 000 € на залог. ✓
- No fabricated figure; NO per-bet RTP table shown (sources disagree → only headline max + "връщат по-малко"); multipliers marked примерни. ✓
- No operator logos/names; Evolution named only as maker (matches 05b); no fake screenshots, no invented bonus/licence. ✓
- No people/faces, no glamorised winning; carries „18+ Играйте отговорно" + „процентите зависят от версията" note. ✓
- XML-valid (viewBox 0 0 720 410, card #0f172a, Arial, headers #93c5fd, right-anchored values, note box). Text-extent check
  per formula (chars × font-size × 0,62): right sub-column label „Числови / специални" @13px ends ~537, value „48 / 6" right-anchored
  x688 → no overlap; „500 000 € на залог" right-anchored value starts ~543, label „Таван на печалбата" ends ~193 → clear; note-box
  text within its rect; ≥16px inner margin. No overlap/clip. ✓
Decision: KEEP (1 infographic). images: 1 (infographic, review skipped — API down).
