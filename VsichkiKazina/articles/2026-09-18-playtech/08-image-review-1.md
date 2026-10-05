# 08 — Gemini image review, pass 1 — Playtech provider-hub profile

Model: gemini (scripts/gemini_image_review.py) · attempted 18.09.2026

Verbatim script output:

```
GEMINI_ERROR: HTTP 429 b'{\n  "error": {\n    "code": 429,\n    "message": "Your prepayment credits are depleted. Please go to AI Studio at https://ai.studio/projects to manage your project and billing. Learn more at https://ai.google.dev/gemini-api/docs/billing#prepay. ",\n    "status": "RESOURCE_EXHAUSTED"\n  }\n}\n'
```

Exit code: 2 (unavailable).

Gemini image review unavailable: HTTP 429 RESOURCE_EXHAUSTED. Step-8 visual review skipped per runbook (do not halt). Manual integrity check performed instead:

- **images/playtech-hero.svg** (concept hero, abstract interconnected product panels + four-tier jackpot ladder): no operator or provider logos, no brand marks; no fake screenshot or real casino UI; no invented numbers (only the studio name „Playtech", generic product labels казино/живо/покер/бинго and the allowed „18+ Играйте отговорно" line, no RTP/max-win figures); no people or faces; no glamorised winning (abstract vector metaphor only). Well-formed (xmllint). KEPT.
- **images/playtech-age-of-the-gods-niva.svg** (jackpot-tier ladder): shows only the four tier NAMES (Power, Extra Power, Super Power, Ultimate Power) and the concept of a shared network pool; bar sizes explicitly labelled „примерни (мрежов прогресив, променлив)" so no jackpot amount is asserted; the only figures are 95.02% RTP and the ~0.99% jackpot contribution, both present verbatim in 05b; no logos, no people/faces, no glamorised winning. Well-formed (xmllint). KEPT.
- **images/playtech-top-slotove.svg** (top-slots data infographic): no logos or brand marks; no fake screenshot; every number matches 05b verbatim (Age of the Gods 95.02% / 10 000x / 2016; Gladiator: Road to Rome 95.05% / 150 000x / 2019; Jackpot Giant 94.22% / 50 000x / 2014; Great Blue 94.30% / 10 000x / 2013; Buffalo Blitz 95.96% / 300x / 2016); source (racingpost) and the multi-build + max-win-varies caveats noted; the Buffalo Blitz max-win disagreement (300x vs up to 10 000x) surfaced honestly; max win labelled a theoretical ceiling, not a promise; no people/faces, no glamorised winning. Well-formed (xmllint). KEPT.

manual integrity: 0 fabrications. Kept all images.
