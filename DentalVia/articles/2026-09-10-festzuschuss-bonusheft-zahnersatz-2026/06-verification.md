# 06 — Verification checklist (for the human, Step 6) · Festzuschuss & Bonusheft 2026

STATUS: NOT publishable until every GKV figure is confirmed against a primary source (KZBV/GKV) and the
human resolves the flags. ALL figures are flagged [VERIFY] and stay IN the text. Claude resolves nothing.

## Byline / compliance
- Byline: **Mario Yordanov**, Patientenkoordinator (no clinical credential). Rotation: 2nd article of run (after Georgi Todorov).
- Medical disclaimer verbatim at end ✓ · Mediation-transparency line verbatim in CTA block ✓ · Brand "Dentalvia" ✓.
- Guide (not cost/comparison) → /garantie/ intentionally omitted.

## GKV figures — confirm every one against KZBV/GKV before publish
| Claim | Value (as written) | Primary/secondary source to confirm |
|---|---|---|
| Legal basis | § 55 SGB V [VERIFY] | gesetze-im-internet.de (§ 55 SGB V) ; KZBV |
| Base subsidy | 60 % der Regelversorgung [VERIFY] | kzbv.de/.../bonusheft/ |
| 5 Jahre lückenlos | 70 % [VERIFY] | kzbv.de/.../bonusheft/ |
| 10 Jahre lückenlos | 75 % [VERIFY] | kzbv.de/.../bonusheft/ |
| Härtefall | bis 100 % der Regelversorgung [VERIFY] | verbraucherzentrale.de (Zuschuss Zahnersatz) ; GKV |
| 2026 increase | +4,34 % zum 1.1.2026, KZBV-Beschluss 5.12.2025 [VERIFY] | KZBV-Beschluss / GBA ; zahnkosten-rechner.de |
| Bonusheft-Nachweis | Erwachsene 1×/Jahr; Kinder/Jugendl. (6–17) 2×/Jahr; einmaliges Versäumnis im 10-J.-Zeitraum ggf. folgenlos [VERIFY] | kzbv.de/.../bonusheft/ |
| Beispielbeträge Krone | Regelvers. rund 280 € → 168/196/210 € [VERIFY] | zahnkosten-rechner.de festzuschuss-bonusheft |
| Beispielbeträge Brücke | rund 530 € → 318/371/398 € [VERIFY] | zahnkosten-rechner.de |
| Beispielbeträge Vollprothese | rund 500 € → 300/350/375 € [VERIFY] | zahnkosten-rechner.de |
| Festzuschuss-Spanne | rund 17 € bis ca. 965,93 € [VERIFY] | verbraucherzentrale.de ; Festzuschuss-Tabelle 2026 |
| HKP-Genehmigung vor Behandlungsbeginn | [VERIFY] | KZBV / Krankenkassen |
| EU-Ausland: Festzuschuss gilt auch dort | [VERIFY] | KZBV/GKV ; interner Ratgeber (verlinkt) |

## Recalculated examples (working shown)
- Bonus-% of Regelversorgung (Krone 280 €): 60 % = 168,00 €; 70 % = 196,00 €; 75 % = 210,00 € ✓ (match).
- Brücke 530 €: 60 % = 318,00 €; 70 % = 371,00 €; 75 % = 397,50 ≈ **398 €** (article rounds to 398 €) ✓.
- Vollprothese 500 €: 60 % = 300 €; 70 % = 350 €; 75 % = 375 € ✓.
- Rechenbeispiel Eigenanteil: Implantat 2.200 € − Festzuschuss 398 € = **1.802 €** (article: "rund 1.802 €") ✓.
  Figures themselves stay [VERIFY]; only the arithmetic is confirmed.

## Gemini external check (Step 7)
- Model gemini-3.1-pro-preview. Initial 05b: "shows AI patterns 75%" → human-likeness 25.
- 2 Humaniser passes applied (07-gemini-check-1/2/3.md). All three scored human-likeness 25 (tied); keep-best pass 2.
- Queue `gemini` = **ai 25**. Residual driven mainly by required inline [VERIFY] flags + verbatim compliance
  boilerplate + the didactic explainer rhythm of an insurance guide; style-only, no fact/flag/compliance changed.

## Images (Step 8)
- images: 2 (1 concept hero WebP + 1 data infographic SVG — Festzuschuss Beispielbeträge). Best Gemini
  image-review **95 (PASS)** (infographic; "technically flawless, all numbers match, layout clean"). Hero
  reviewed 72 but the sub-80 was solely a mis-loaded "Bulgarian ALT" requirement from the shared VK review
  prompt; German ALT is correct for this site and the hero has NO integrity/hygiene/layout violation, so it
  is kept (keep-best). Every infographic figure traces verbatim to 05b; German labels + "Stand 2026".

## Brand Gate (Step 5)
- PASS WITH FIXES, total **96/100**; all 8 blocking checks PASS (/garantie/ N/A for a guide); one mechanical
  em-dash fix in a meta placeholder. See 05-gate-report.md.
