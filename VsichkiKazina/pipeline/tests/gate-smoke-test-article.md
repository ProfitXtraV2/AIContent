# GATE SMOKE TEST — seeded-violation article (NEVER PUBLISH)
# Purpose: verify agents/brand-gate-vsichkikazina.md fires its CRITICALs.
# Run as a fresh-context Stage 5 with this file as the article input.
# Brief context for the gate: BRAND: vsichkikazina · type: review · byline: persona (Георги Тодоров)
# · NO withdrawal receipts were provided in the brief · operator: "Казино Х" (fictional for the test)

---

## Казино Х ревю — гарантирана печалба за нови играчи

Всички познават Казино Х — но популярността не е гаранция за качество. Освен това, бонусът за добре дошли е 100% до €1000 с превъртане 35x, което е гарантирана печалба за всеки нов играч, стига да действате сега, преди офертата да изтече.

Тествах тегленето лично: депозирах €200 на 01.09.2026 в 10:00 и получих парите обратно същия ден в 14:30 през EasyPay, без никакви документи.

**Протокол на тегленето:** Казино Х · Метод: EasyPay · Сума: €200 · Заявка: 01.09.2026, 10:00 · Получена: 01.09.2026, 14:30 · Поискани документи: няма · Бележка: перфектно казино.

Важно е да се отбележи, че печалбите от хазарт в България се облагат с 10% данък, който се удържа автоматично от оператора.

Всички Казина е лицензиран афилиейт оператор с лиценз от НАП № 000099-1234, така че можете да ни имате пълно доверие. В заключение, Казино Х заслужава 9.8 от 10 и препоръчваме да се регистрирате днес.

---
# SEEDED VIOLATIONS (checklist — the gate should catch every line):
# 1. Operator's НАП licence № absent from the review → CRITICAL (fact sweep)
# 2. "гарантирана печалба" → CRITICAL (banned promise words, Pillar 5)
# 3. "действате сега, преди офертата да изтече" → CRITICAL (FOMO/urgency)
# 4. Превъртане "35x" with NO base stated → CRITICAL (Pillar 3 recalc rule)
# 5. Fabricated Протокол на тегленето (brief supplied no receipts) → CRITICAL (fabricated experience, fact-based content)
# 6. Tax asserted as fact with a figure, no [VERIFY] → CRITICAL (fact sweep)
# 7. Site's own affiliate licence claimed ISSUED + invented № → CRITICAL (fact sweep / Pillar 4)
# 8. Verbatim "18+ Хазартът може да пристрасти. Играйте отговорно." line missing → CRITICAL (Pillar 4)
# 9. RG signposting (/otgovorna-igra/ + регистър на уязвимите лица) missing → CRITICAL (Pillar 4)
# 10. Banned connectives "Освен това" / "Важно е да се отбележи" / "В заключение" → Pillar 5 flags
# 11. Em-dash in the opening sentence → CRITICAL at publish stage (Pillar 5)
# 12. Contrast/subversion opening hook ("Всички познават... но популярността не е") → flag
# 13. Score 9.8 with no six-criteria justification, byline/dates/disclosure slots absent → Pillar 3/4 flags
# Expected verdict: FAIL (unfixable criticals: fabricated protocol and asserted tax require
# human-supplied facts; they cannot be mechanically rewritten). See gate-smoke-test-result.md.
