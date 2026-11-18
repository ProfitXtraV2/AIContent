# 07 — Gemini text check · pass 1 · vk-0333 · Берое Стара Загора

**Command:** `python3 scripts/gemini_check.py VsichkiKazina/articles/2026-11-13-beroe-stara-zagora/05b-final-draft.md`
**Exit code:** 2

**Verbatim output:**
```
GEMINI_ERROR: HTTP 402 b'{\n  "error": {\n    "code": 402,\n    "message": "Your prepayment credits are depleted. Please go to AI Studio at https://ai.studio/projects to manage your project and billing. Learn more at https://ai.google.dev/gemini-api/docs/billing#prepay. ",\n    "status": "RESOURCE_EXHAUSTED"\n  }\n}\n'
```

**Interpretation:** `GEMINI_UNAVAILABLE` (HTTP 402 RESOURCE_EXHAUSTED — prepayment credits depleted; persistent since 2026-11-10/11/12). Per `automation/daily-run.md` Step 7, the external check is **skipped** (do NOT halt). No Humaniser pass is driven (0 passes applied). Keep-best = the compliant initial 05b (0 em/en-dash body, non-pivot opening, asymmetric close, Brand Gate ~95 PASS 0-critical). `gemini = skipped`.
