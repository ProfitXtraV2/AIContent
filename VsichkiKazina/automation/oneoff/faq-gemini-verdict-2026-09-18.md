# Gemini FAQ check — model: gemini_check.py (Google Gemini), run date: 2026-09-18

## Result: SCRIPT FAILED — Gemini API unavailable (exit code 2)

```
GEMINI_ERROR: HTTP 429 b'{\n  "error": {\n    "code": 429,\n    "message": "Your prepayment credits are depleted. Please go to AI Studio at https://ai.studio/projects to manage your project and billing. Learn more at https://ai.google.dev/gemini-api/docs/billing#prepay. ",\n    "status": "RESOURCE_EXHAUSTED"\n  }\n}\n'
```

The Gemini API returned HTTP 429 RESOURCE_EXHAUSTED — prepayment credits are depleted.
No verdict, confidence score, flagged passages, or recommendations were produced.

**Action required:** Top up Gemini API credits at https://ai.studio/projects, then re-run:
```bash
python3 scripts/gemini_check.py VsichkiKazina/automation/oneoff/faq-live-2026-09-18.md --brand vsichkikazina
```
and write the output to this file (replacing the error above with the actual verdict).
