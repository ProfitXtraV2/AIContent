# 08 — Image review, pass 1 (Crazy Time)

Command: python3 scripts/gemini_image_review.py VsichkiKazina/articles/2026-09-26-crazy-time/05b-final-draft.md \
         VsichkiKazina/articles/2026-09-26-crazy-time/images/crazy-time-koleloto-i-rtp-infografika.svg

RESULT: GEMINI_UNAVAILABLE (HTTP 402 — prepayment credits depleted; same billing outage as Step 7).
Also gemini_image_gen.py → HTTP 402 (both image models). AI hero SKIPPED.
Per daily-run.md Step 8: image review skipped (Gemini unavailable) — DO NOT halt, keep the image.

Manual integrity self-check (author, since automated review is down):
- Numbers trace to 05b VERBATIM: 54 полета; 21/13/7/4 (числа) + 4/2/2/1 (бонуси); 45 (~83%) / 9 (~17%); RTP число 1 ≈96,08%;
  Pachinko/Crazy Time ≈94,33% / 94,41%; средно ≈95,41%; таван ≈20 000x, рекламиран ≈25 000x; Evolution (2020). ✓
- No fabricated figure; NO per-bonus multiplier table shown (only headline max); multiplier values marked примерни. ✓
- No operator logos/names, no fake screenshots, no invented bonus/licence. Evolution named only as the game maker (matches 05b). ✓
- No people/faces, no glamorised winning; carries „18+ Играйте отговорно" + „числата за множителите са примерни" note. ✓
- Validated as XML (viewBox 0 0 720 450, card #0f172a, Arial, headers #93c5fd, right-anchored stat values, note box). Estimated
  text extents checked per formula (chars × font-size × 0,62): two-column composition (left labels vs value @x350; right labels
  @x384 vs value @x688) — no overlap, ≥16px inner margin on all sides; RTP rows' right-anchored values end ≥16px before edge;
  note-box text within its rect. No overlap/clip. ✓
Decision: KEEP (1 infographic). images: 1 (infographic, review skipped — API down).
