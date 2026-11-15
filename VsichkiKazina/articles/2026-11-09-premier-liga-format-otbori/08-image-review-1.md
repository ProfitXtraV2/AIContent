# 08-IMAGE-REVIEW (pass 1) — Премиер лига

Command: python3 scripts/gemini_image_review.py 05b-final-draft.md images/premier-liga-format-sezon.svg images/premier-liga-struktura-hero.svg
Result: GEMINI_ERROR — HTTP 402 RESOURCE_EXHAUSTED ("prepayment credits are depleted").
Exit code: 2 (non-zero).

Per daily-run.md Step 8: Gemini image review unavailable / non-zero exit → log `image review: skipped (Gemini unavailable)`
and KEEP the image(s). No regenerate loop this fire (no verdict to iterate on).

MANUAL INTEGRITY CHECK (both images):
- No operator logos or names (0 operators depicted/named). PASS
- No fake screenshots. PASS
- No invented numbers — every figure traces VERBATIM to 05b-final-draft.md:
  20 отбора · 38 мача/отбор · 380 общо · 3/1/0 точки · първите 4–5 → Шампионска лига (5-о от коефициента на Англия) ·
  следващи + купите → Лига Европа / Лига на конференциите · последни 3 изпадат · топ 2 директно + плейоф 3–6 · август–май. PASS
- No people/faces. PASS
- No glamorised winning (no money/jackpot/celebration imagery; neutral schematic + data cards only). PASS
- Both rendered in Chromium (deviceScaleFactor 2) — layout clean, no text overflow, valid XML. PASS

Images kept: 2 (both hand-authored SVG, API-free).
- images/premier-liga-struktura-hero.svg — schematic hero (20 dots, 38 кръга, 380 мача, август–май).
- images/premier-liga-format-sezon.svg — data infographic (format + points + table zones).
Best review score: n/a (Gemini unavailable); manual integrity PASS on both.
