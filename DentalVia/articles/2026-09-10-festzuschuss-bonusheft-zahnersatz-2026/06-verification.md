# 06 — Verification checklist (for the human, Step 6) · Festzuschuss & Bonusheft 2026

Reprocessed under the tiered verification policy (`DentalVia/pipeline/reference/verification-policy.md`,
approved 2026-09-11) by the verify-assist pass on 2026-09-11. Example-framed euro amounts (Tier A) had their
markers removed; the legal-rate claims were checked against the primary statute (§ 55 SGB V) and resolved
where the source confirms them verbatim; current-year/administrative figures the primary source did not
confirm stay for the human. Nothing was resolved by reasoning or a secondary source, and no claim or number
was altered.

STATUS: still NOT publishable until the REMAINING flags are confirmed by the human. Merge = approve stays human.

## Count summary
**Was 28 flags (28 [VERIFY]) → resolved 20 (Tier A: 16, Tier B: 4), remaining 8 for human.**

## RESOLVED

### Tier B — confirmed against a fetched primary source (marker removed)
| Claim in article | Source (fetched 2026-09-11) | Exact quote | Result |
|---|---|---|---|
| Der befundorientierte Festzuschuss ist geregelt in **§ 55 SGB V** | § 55 SGB V — gesetze-im-internet.de/sgb_5/__55.html | „Versicherte haben … Anspruch auf **befundbezogene Festzuschüsse** bei einer medizinisch notwendigen Versorgung mit Zahnersatz" | CONFIRMED → resolved |
| Basiszuschuss **60 %** der Regelversorgung | § 55 Abs. 1 SGB V — same URL | „Die Festzuschüsse umfassen **60 Prozent** der … festgesetzten Beträge" | CONFIRMED → resolved |
| **70 %** nach 5 Jahren lückenlosem Bonusheft | § 55 Abs. 1 SGB V — same URL | „erhöhen sich die Festzuschüsse nach Satz 2 auf **70 Prozent**" (fünf Kalenderjahre) | CONFIRMED → resolved |
| **75 %** nach 10 Jahren lückenlosem Bonusheft | § 55 Abs. 1 SGB V — same URL | „Die Festzuschüsse nach Satz 2 erhöhen sich auf **75 Prozent**, wenn der Versicherte … in den letzten zehn Kalenderjahren …" | CONFIRMED → resolved |

### Tier A — example-framed euro amounts (marker removed; framing is the guard, no source needed)
The whole Beispielbeträge block is framed „Beispielwerte (Stand 2026)" (section heading + intro sentence +
figure caption), and the worked example is framed „Beispielwert Stand 2026" inline. Per policy Tier A the
inline [VERIFY] markers were removed; the numbers were NOT changed.

| Figure (as written) | Framing present |
|---|---|
| Einzelkrone Regelversorgung rund 280 € → 168 / 196 / 210 € | „Beispielwerte (Stand 2026)" table |
| Dreigliedrige Brücke rund 530 € → 318 / 371 / 398 € | „Beispielwerte (Stand 2026)" table |
| Vollprothese je Kiefer rund 500 € → 300 / 350 / 375 € | „Beispielwerte (Stand 2026)" table |
| Beispiel-Festzuschuss 398 € (75 %) | „Beispielwert Stand 2026" inline |
| „er bleibt bei 398 €" (andersartige Versorgung) | same worked example (Beispielwert Stand 2026) |
| Implantat samt Krone 2.200 € | „beispielsweise … (Beispielwert Stand 2026)" |
| Eigenanteil rund 1.802 € (= 2.200 − 398) | derived from the framed example; arithmetic checked below |

## REMAINING FOR HUMAN (flags stay in the text)

| Claim in article | Flag | Best source found / pre-fetched quote | What the human must check |
|---|---|---|---|
| Festzuschuss zum 1.1.2026 um **+4,34 %** gestiegen (intro) | [VERIFY] | KZBV / GKV-Spitzenverband Festzuschuss-Beschluss 2026; kzbv.de patient-info page returned HTTP 404 on fetch 2026-09-11 — no primary source reached | Confirm the +4,34 % 2026 uplift against the KZBV/GKV-Spitzenverband Beschluss (Bundesanzeiger). Source unreachable → flag stays. |
| KZBV hob die Festzuschüsse um **+4,34 %** an, **beschlossen am 5.12.2025** | [VERIFY] | same as above — KZBV-Beschluss vom 5.12.2025 | Confirm both the +4,34 % figure and the 5.12.2025 decision date against the KZBV/GKV primary publication. |
| Härtefall: „Der Festzuschuss **verdoppelt sich** und kann **bis zu 100 %** der Regelversorgung erreichen" | [VERIFY] | § 55 Abs. 2/3 SGB V — gesetze-im-internet.de/sgb_5/__55.html, fetched 2026-09-11: Abs. 2 „einen Betrag in Höhe von **40 Prozent** … für die … Regelversorgung … höchstens … in Höhe der tatsächlich entstandenen Kosten"; Abs. 3 caps the total at Festzuschuss (Abs.1) + Betrag (Abs.2). | **100 % cap is confirmed** (60 % + 40 % = max 100 %, capped at actual cost). BUT the statute frames it as **+40 Prozentpunkte**, NOT a literal „Verdoppelung". Human: confirm/reword „verdoppelt sich" (mechanically base 60 % + 40 pp = 100 %; „doppelter Festzuschuss" is the colloquial term). Flag kept because the wording is not verbatim-supported. |
| Bonus: „einmaliges Versäumnis im Zehnjahreszeitraum … **sofern Sie es gegenüber der Kasse ausreichend begründen** können" | [VERIFY] | § 55 Abs. 1 SGB V — same URL, fetched 2026-09-11: „… nur mit **einer einmaligen Unterbrechung** in Anspruch genommen hat" | Statute confirms a **single interruption** is tolerated for the 75 % level; it does NOT condition this on a justification („begründen"). Human: confirm whether the „begründen"-Voraussetzung reflects actual Kassen-Praxis, or reword to match the statute. |
| Festzuschuss-Spanne **rund 17 € bis etwa 965,93 €** über alle Befunde | [VERIFY] ×2 | KZBV Festzuschuss-Tabelle 2026 (befundbezogene Festzuschüsse) — not fetched; not example-framed, so NOT Tier A | Confirm the min/max against the official Festzuschuss-Tabelle 2026. Specific current-law figures, not examples → human. |
| HKP muss **vor Behandlungsbeginn** von der Kasse **genehmigt** werden | [VERIFY] | Zahnersatz-Richtlinie (G-BA) / § 87 SGB V, BEMA — not fetched | Confirm the mandatory prior-approval rule against the Zahnersatz-Richtlinie / BEMA. |
| Festzuschuss gilt auch für Zahnersatz im **EU-Ausland**, sofern GKV-abrechenbar und HKP vorab genehmigt | [VERIFY] | § 13 Abs. 4 SGB V — gesetze-im-internet.de/sgb_5/__13.html, fetched 2026-09-11: „Versicherte sind berechtigt, auch Leistungserbringer in einem anderen Mitgliedstaat der Europäischen Union … im Wege der **Kostenerstattung** in Anspruch zu nehmen" (begrenzt auf inländische Vergütung) | **Core confirmed** (EU-Ausland Kostenerstattung bis zur Höhe der Inlandsvergütung). BUT § 13 Abs. 4 is generally „ohne vorherige Genehmigung" for non-hospital care; the article's „HKP vorab genehmigt" prerequisite is a Zahnersatz-specific rule not shown by § 13. Human: confirm the HKP-Genehmigung requirement for the cross-border Festzuschuss (KZBV/Kasse). Flag kept. |

## Recalculated examples (working shown — figures stay as dated examples)
- Bonus-% of Regelversorgung (Krone 280 €): 60 % = 168 €; 70 % = 196 €; 75 % = 210 € ✓
- Brücke 530 €: 60 % = 318 €; 70 % = 371 €; 75 % = 397,50 ≈ **398 €** (article rounds to 398 €) ✓
- Vollprothese 500 €: 60 % = 300 €; 70 % = 350 €; 75 % = 375 € ✓
- Eigenanteil: Implantat 2.200 € − Festzuschuss 398 € = **1.802 €** (article: „rund 1.802 €") ✓
  Arithmetic confirmed; the underlying example euro amounts remain dated examples (Tier A).

## Byline / compliance (verify present, do not change)
- Byline: **Mario Yordanov**, Patientenkoordinator (no clinical credential). Rotation: 2nd article of run.
- Medical disclaimer verbatim at end ✓ · Mediation-transparency line verbatim in CTA block ✓ · Brand "Dentalvia" ✓.
- Guide (not cost/comparison) → /garantie/ intentionally omitted. Compliance/risk/framing untouched by verify-assist.

## Gemini external check (Step 7)
- gemini-3.1-pro-preview: initial "shows AI patterns 75%" → human-likeness 25; 2 passes (25/25/25), keep-best pass 2.
  Queue `gemini` = ai 25. Style-only; no fact/flag/compliance touched. (Unchanged by verify-assist.)

## Images (Step 8)
- 2 images (concept hero WebP + Festzuschuss-Beispielbeträge SVG). Infographic Gemini review 95 (PASS,
  "all numbers match"); hero 72 kept (sub-80 was solely the mis-loaded VK "Bulgarian ALT" requirement — German
  ALT correct, no integrity/layout violation). Every figure traces verbatim to 05b. Not touched by verify-assist.

## Brand Gate (Step 5)
- PASS WITH FIXES, total 96/100; all 8 blocking checks PASS (/garantie/ N/A for a guide). See 05-gate-report.md.
