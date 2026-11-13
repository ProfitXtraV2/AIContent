# 08 — Gemini image review · pass 1 · vk-0333 · Берое Стара Загора

**Command:** `python3 scripts/gemini_image_review.py VsichkiKazina/articles/2026-11-13-beroe-stara-zagora/05b-final-draft.md VsichkiKazina/articles/2026-11-13-beroe-stara-zagora/images/beroe-fakti.svg`
**Exit code:** 2

**Verbatim output:**
```
GEMINI_ERROR: HTTP 402 b'{\n  "error": {\n    "code": 402,\n    "message": "Your prepayment credits are depleted. Please go to AI Studio at https://ai.studio/projects to manage your project and billing. Learn more at https://ai.google.dev/gemini-api/docs/billing#prepay. ",\n    "status": "RESOURCE_EXHAUSTED"\n  }\n}\n'
```

**Interpretation:** `GEMINI_UNAVAILABLE` (HTTP 402 RESOURCE_EXHAUSTED — prepayment credits depleted). Per `automation/daily-run.md` Step 8, the image review is **skipped** (do NOT halt) and the image is kept. The optional AI hero was also skipped (same depleted key) → shipped the infographic alone.

## Manual integrity check (fallback when Gemini is down) — PASS
- **Numbers trace 1:1 to 05b:** 1986 (шампион), 2010 · 2013 (Купа, 2 пъти), 2013 (Суперкупа), 4 (Балкански купи, рекорд), 9 (Втора лига, рекорд), „Берое" (стадион), 1959 / 4 април (открит), 12 128 (капацитет), 144 (Петко Петков), 341 (Евгени Янчовски). Every figure is stated verbatim in `05b-final-draft.md`.
- **No integrity failures:** 0 operator logos/names, 0 fake screenshots, 0 fabricated bonus/RTP/licence numbers, 0 people/faces, 0 glamorised winning.
- **Render:** Chromium (deviceScaleFactor 2) — layout clean, 0 overlap/clipping after the date-row fix (big value shortened to „1959", date moved to the label).
- **Best review score:** manual integrity PASS (Gemini numeric score unavailable).

**images: 1** (infographic `beroe-fakti.svg`).
