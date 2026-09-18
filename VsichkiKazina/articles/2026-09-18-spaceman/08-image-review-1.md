# 08 — Gemini image review, pass 1

Command: `python3 scripts/gemini_image_review.py VsichkiKazina/articles/2026-09-18-spaceman/05b-final-draft.md images/spaceman-hero.svg images/spaceman-cash-out.svg`

Verbatim output:

```
GEMINI_ERROR: HTTP 429 b'{\n  "error": {\n    "code": 429,\n    "message": "Your prepayment credits are depleted. Please go to AI Studio at https://ai.studio/projects to manage your project and billing. Learn more at https://ai.google.dev/gemini-api/docs/billing#prepay. ",\n    "status": "RESOURCE_EXHAUSTED"\n  }\n}\n'
```

Gemini image review unavailable: HTTP 429 RESOURCE_EXHAUSTED. Step-8 visual review skipped per runbook. Manual integrity check instead:

- `images/spaceman-hero.svg` — абстрактна векторна метафора (възходяща крива на множител до светеща точка на осребряване, след което червена пунктирана линия пада = срив; звезди на фон). No operator logos/brand names. No fake screenshots/UI. No invented numbers (само „18+ Играйте отговорно"; никакви статистики). No people/faces. No glamorised winning. Валидира с xmllint; рендира чисто чрез cairosvg. INTEGRITY: PASS.
- `images/spaceman-cash-out.svg` — стат карта / ключови числа. No operator logos/brand names. No fake screenshots/UI. Всички числа съвпадат дословно с 05b (RTP 96.50%; алт. версия около 95%; домашно предимство 3.50%; макс. печалба 5000x; €500 000 при €100; залог €1 - €100; crash формат; множител от 1.00x; авто-кешаут 1.01x - 4999.99x; 50% cash-out; Pragmatic Play, 2022). No people/faces. No glamorised winning. Подзаглавието предупреждава, че операторът може да зареди по-нисък RTP, провери в инфо-панела. Рендер проверен (cairosvg, 740px): без overlap, без изрязване на текст, всички етикети и числа четими с чисти полета. Валидира с xmllint. INTEGRITY: PASS.

Kept all images. images: 2. 0 integrity failures. manual integrity: 0 fabrications.
