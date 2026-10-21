# 08 — Image review, pass 1 (Evolution)

Command: python3 scripts/gemini_image_review.py VsichkiKazina/articles/2026-09-27-evolution-provajdar/05b-final-draft.md \
         VsichkiKazina/articles/2026-09-27-evolution-provajdar/images/evolution-portfolio-i-rtp-infografika.svg

RESULT: GEMINI_UNAVAILABLE (HTTP 402). gemini_image_gen.py also 402 → AI hero SKIPPED.
Per daily-run.md Step 8: image review skipped (Gemini unavailable) — DO NOT halt, keep the image.

Manual integrity self-check (author):
- Numbers trace to 05b VERBATIM: основана 2006; живо блекджек ≈ 99,29%; живо бакара ≈ 98,94%; рулетка на живо ≈ 97,30%;
  game show формати ≈ 95–96% (Crazy Time 96,08%, Funky Time 95,99%, Mega Ball 95,40% all in body); flagship names
  (Crazy Time, Monopoly Live, Lightning Roulette, Funky Time, Dream Catcher, Mega Ball) all named in 05b. ✓
- No fabricated figure; RTP shown as представителни/примерни ranges by category, all present in body; „Швеция" and 2006 sourced. ✓
- No operator logos/names; Evolution named only as the maker (matches 05b); no fake screenshots, no invented bonus/licence №. ✓
- No people/faces, no glamorised winning; carries „18+ Играйте отговорно" + „Стойностите са примерни и зависят от версията и играта" note. ✓
- XML-valid (checked with xml.dom.minidom; viewBox 0 0 720 390, card #0f172a, Arial, headers #93c5fd, right-anchored values at x688, note box). Text-extent check:
  longest left label „Game show формати (най-нисък RTP)" @13px ends ~ x360; right-anchored value „≈ 95–96%" starts ~ x648 → no overlap; „2006, Швеция" value fits within right margin; note-box text within its 656px rect; ≥16px side margins on all rows. Green (#4ade80) = higher RTP, amber (#fbbf24) = lower, aids the honest hierarchy. ✓
Decision: KEEP (1 infographic). images: 1 (infographic, review skipped — API down). AI hero not produced (402).
