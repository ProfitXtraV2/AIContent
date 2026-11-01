# 06 — Verification — 2026-10-27-shah-pravila (vk-0300)

## Surviving flags
- **None.** 0 [VERIFY], 0 [DATA NEEDED], 0 [CONFLICT]. All content is universal, well-established
  chess rules; no operator-, НАП-, licence-, or tax claim appears, so nothing is flagged.

## Time-sensitive claims
- None. The rules of chess are evergreen (FIDE Laws of Chess, unchanged in substance). The only
  external references are the free platforms chess.com and Lichess (play vs computer) — both long
  stable, named generically, no figures attached.

## Primary sources
- https://www.chess.com/bg/shakh — „Как се играе шахмат | Правила + 7 първи стъпки" (BG), fetched 27.10.2026.
  Covers: setup, piece moves, castling/ан пасан/произвеждане, check/mate/stalemate, draw conditions,
  white moves first, piece values (pawn 1, knight 3, bishop 3, rook 5, queen 9), beginner principles.
- https://bg.wikipedia.org/wiki/Шахмат — corroborating terminology.

## Recalculated figure (working shown)
- Claim in text: „Два коня срещу топ и пешка е равностойна сделка на хартия."
  Working: two knights = 3 + 3 = 6 pawn-units; rook + pawn = 5 + 1 = 6 pawn-units. 6 = 6 → equal
  on the point count, exactly as the article states (it then correctly adds that the real value
  depends on the position). Consistent.
- Infographic bar lengths trace to the same values (scale 44 px per point): pawn 44, knight/bishop
  132 (3×44), rook 220 (5×44), queen 396 (9×44). All proportional and 1:1 with the stated numbers.

## Gemini Step-7 (text)
- Baseline 05b: „Likely human-written, 80% confidence" → human-likeness 80 → **PASS** (≥80).
- Passes applied: 0 (baseline already clears the gate; keep-best = baseline). `gemini` = **human 80**.
- Three style recommendations (wrap-up micro-summaries, the „Пет навика" imperative block, the
  sign-off) left as optional taste notes for the human Step-6 editor; facts/links/RG/disclosures clean.

## Step-8 images
- **images: 2 (infographic 100, hero 100)** — best review score 100, 0 integrity failures.
- Infographic shah-stoynost-figuri.svg (piece values, numbers 1:1 with 05b); decorative hero
  shah-figuri-hero.webp (14.8 KB, flat-vector chess knight on a board, no text/people/gambling).

## Brand Gate
- PASS 95/100, 0 criticals (see 05-gate-report.md). Byline Георги Тодоров, brand „Всички Казина",
  dates 27.10.2026, About + bio + verbatim 18+ RG line + RG signposting + affiliate footer; no
  operator referenced → „Тази статия не съдържа партньорски връзки" (correct). 0 em-dashes in body.

## Status
Publish-ready for human Step-6 review. FLAGS STAY IN THE TEXT (there are none). Do NOT resolve
flags, post, or merge — human owns Step 6.
