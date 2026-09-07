# SMOKE TEST RESULT — executed 07.09.2026 against agents/brand-gate-vsichkikazina.md
# (Run by Claude applying the gate instructions to tests/gate-smoke-test-article.md.
# In production this runs as a fresh-context Stage 5; re-running there should reproduce this.)

BRAND COMPLIANCE SCORECARD — Казино Х ревю — гарантирана печалба за нови играчи
Verdict: FAIL
Total: 14/100
Personality 2/20 | Tone 3/15 | E-E-A-T 2/20 | Trust signals 0/15 | Language&Style 2/15 | RG 5/15

CRITICAL (blocks publish):
- [no НАП licence № anywhere for Казино Х] → fact sweep: "A review missing the operator's НАП licence № → CRITICAL" → add the licence № from the brief/register; without it the review cannot exist.
- "гарантирана печалба за всеки нов играч" → banned promise words (Pillar 5, zero tolerance) → restate as the factual bonus terms with their real cost.
- "стига да действате сега, преди офертата да изтече" → FOMO/urgency mechanics → delete; state the offer's verified expiry date if known, else nothing.
- "превъртане 35x" → Pillar 3: превъртане stated WITHOUT its base → state "35x върху [депозит+бонус / само бонус]" from the brief; if the base is unknown → [DATA NEEDED: превъртане база].
- "**Протокол на тегленето:** ... Заявка: 01.09.2026, 10:00 ..." → FABRICATED EXPERIENCE: the brief supplied no receipts; every timestamp is invented → remove the entire protocol block; replace with [VERIFY: липсва протокол на тегленето]. Not mechanically fixable — requires a real test.
- "се облагат с 10% данък, който се удържа автоматично" → fact sweep: tax asserted as fact with a figure → replace with the [VERIFY]-flagged formulation pointing to счетоводител/НАП. Not mechanically fixable — the human owns tax claims.
- "лицензиран афилиейт оператор с лиценз от НАП № 000099-1234" → fact sweep: claim that the site's own licence has been ISSUED + invented № → replace with the verbatim pending-status footer disclosure.
- Missing verbatim "18+ Хазартът може да пристрасти. Играйте отговорно." → Pillar 4 → insert exactly.
- Missing RG signposting to /otgovorna-igra/ + регистър на уязвимите лица → Pillar 4 → insert per template.
- Em-dash in the opening sentence at publish stage → Pillar 5 → replace with comma/colon/full stop.

MODERATE:
- "Освен това", "Важно е да се отбележи", "В заключение" → banned Bulgarian connectives → delete/restate directly.
- Contrast/subversion opening hook ("Всички познават... но популярността не е гаранция за качество") → open with a finding or number.
- Score 9.8/10 with no six-criteria justification → tie the verdict to the public formula or drop the number.
- Byline, pub/updated dates, About slot, affiliate disclosure slots all absent → insert template slots.

VERIFY QUEUE (route to human): превъртане base for Казино Х; operator НАП licence №; tax formulation sign-off; real withdrawal protocol receipts.

VOICE NOTES (protect during fixes): none to protect — no legitimate Тодоров voice present; the first person here is entirely unsupported.

FAIL rationale per thresholds: score <70 AND two criticals are not mechanically fixable (fabricated protocol, asserted tax) — both require human-supplied facts at Step 6. Per SKILL principle 6, fix at the failing stage (here: the brief itself lacks the operator facts and receipts) and re-run forward; never hand-patch past the gate.

RESULT: all 10 seeded CRITICALs fired, all 4 seeded flags fired. Gate behaves as specified.
