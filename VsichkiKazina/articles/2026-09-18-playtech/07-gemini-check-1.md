# 07 — Gemini external check, pass 1 — Playtech provider-hub profile

Model: gemini (scripts/gemini_check.py) · attempted 18.09.2026

Verbatim script output:

```
GEMINI_ERROR: HTTP 429 b'{\n  "error": {\n    "code": 429,\n    "message": "Your prepayment credits are depleted. Please go to AI Studio at https://ai.studio/projects to manage your project and billing. Learn more at https://ai.google.dev/gemini-api/docs/billing#prepay. ",\n    "status": "RESOURCE_EXHAUSTED"\n  }\n}\n'
```

Exit code: 2 (unavailable).

GEMINI_UNAVAILABLE: HTTP 429 RESOURCE_EXHAUSTED (prepayment credits depleted). Step-7 external check skipped per runbook (do not halt, do not iterate). Kept the Brand-Gate-passed 05b as final. Human-likeness: not scored (external checker down).

content-queue gemini = skipped.
