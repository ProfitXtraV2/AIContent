# 08 — IMAGE REVIEW — pass 1 (infographic)

Command: python3 scripts/gemini_image_review.py 05b-final-draft.md images/poker-bulgaria-zakonno-infografika.svg

**Result: image review SKIPPED (Gemini unavailable).** Two attempts both failed on the generativelanguage endpoint (attempt 1: outer timeout EXIT=124 after 180s; attempt 2: `GEMINI_ERROR: The read operation timed out`, EXIT=2). Per Step 8, a non-zero/unavailable exit does NOT halt — keep the image and proceed. The text Step-7 checks ran on the same endpoint and did return (needed retries), so this is intermittent slowness/overload on the vision call, not a key/config problem.

## Manual integrity check (author-run, since Gemini review unavailable) — PASS
Image: `images/poker-bulgaria-zakonno-infografika.svg` (hand-authored vector, no API). Checked EACH figure/citation against 05b-final-draft.md:
- Покерът = игра в казино, чл. 41, ал. 1, т. 5 (05b: „чл. 41, ал. 1" + „последната група ... рулетка, блекджек, бакара") ✓
- рулетка / блекджек / бакара (05b line 12) ✓
- Онлайн допустим, чл. 41, ал. 2, без томбола/моментна лотария (05b line 18) ✓
- Казино капитал мин. 1 500 000 лв., чл. 4, ал. 2 (05b line 22) ✓
- Глоба от 500 до 2000 лв. ≈ 255,65 до 1022,58 € , чл. 9, ал. 14 + чл. 97а, ал. 2 (05b line 28) ✓
- Блокиране до 24 часа от 01.08.2026, чл. 17, ал. 6; плащанията затворени (чл. 9, ал. 13) (05b line 30) ✓
- 18+ пълнолетни, чл. 2, ал. 3 (05b line 36 + RG footer) ✓
- Brand „Всички Казина" exact; RG line verbatim in footer ✓

Integrity hygiene (automatic-fail triggers — none present):
- No operator logos/names (grep for betano/efbet/winbet/palms/pokerstars/casino = 0) ✓
- No fake screenshots (pure vector) ✓
- No invented bonus/RTP/licence numbers (only ЗХ law figures, all from 05b) ✓
- No people/faces ✓
- No glamorised winning (it is a legal-rules + player-risk card, warns of fines) ✓

VERDICT: KEEP. Manual integrity PASS; no fabrication. Score: review unavailable (manual PASS).
