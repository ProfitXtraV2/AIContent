# 07 — Gemini external check, pass 1

Command: `python3 scripts/gemini_check.py VsichkiKazina/articles/2026-09-18-spaceman/05b-final-draft.md`

Verbatim output:

```
GEMINI_ERROR: HTTP 429 b'{\n  "error": {\n    "code": 429,\n    "message": "Your prepayment credits are depleted. Please go to AI Studio at https://ai.studio/projects to manage your project and billing. Learn more at https://ai.google.dev/gemini-api/docs/billing#prepay. ",\n    "status": "RESOURCE_EXHAUSTED"\n  }\n}\n'
```

GEMINI_UNAVAILABLE: HTTP 429 RESOURCE_EXHAUSTED (prepayment credits depleted). Step-7 external check skipped per runbook (do not halt, do not iterate). Kept the Brand-Gate-passed 05b as final. Human-likeness: not scored (external checker down).

## Keep-best ledger
- initial draft: Brand Gate PASS 94/100; anti-AI applied proactively at draft (0 em-dash, no banned connectives, asymmetric close, varied rhythm, no „не A, а B" mic-drop habit, no counting signposts) → KEPT as final (only version).
- content-queue gemini = skipped.
- All untouchables preserved (byline Георги Тодоров, brand Всички Казина, verbatim 18+ body+footer, RG signposting, affiliate footer).
