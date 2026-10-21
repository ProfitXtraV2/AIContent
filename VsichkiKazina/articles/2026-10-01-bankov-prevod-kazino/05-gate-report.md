# 05 — BRAND GATE REPORT · 2026-10-01-bankov-prevod-kazino

```
BRAND COMPLIANCE SCORECARD — „Банков превод в онлайн казино: срокове, лимити и такси"
Verdict: PASS WITH FIXES
Total: 93/100
Personality 19/20 | Tone 14/15 | E-E-A-T 18/20 | Trust signals 14/15 | Language&Style 14/15 | RG 14/15

CRITICAL (blocks publish): НЯМА.
  - Method-level guide, no operator named → correctly NO Протокол на тегленето, NO НАП №, NO affiliate
    link in body. This is the intended shape, not a missing-element critical.
  - Превъртане не се споменава (payments guide) → N/A, no base-less multiplier to flag.
  - Данъчна тема не се засяга → no unflagged tax claim.
  - Site-affiliate footer present verbatim with „подало заявление … очаква издаването му" (no issued
    licence claimed, no invented №) → compliant.

MODERATE (fixed in Phase 2):
  1. Process/audit notes above the article (SEO AUDIT header съдържа 1 em-dash; INTERNAL-LINK блок) са
     стадийни бележки, не част от публикуемия текст → СТРИПНАТИ в 05b. Публикуемото тяло: 0 em-dash.
  2. Keyword "bank transfer казино" беше вплетен веднъж като етикет в касата (интро) → естествено,
     не stuffing; оставено.

VERIFY QUEUE (route to human):
  - [VERIFY: точната такса за изходящ превод зависи от тарифния план на конкретната банка] — остава
    в текста; банковата тарифа варира по план и не се потвърждава от достъпим общ източник като факт.

VOICE NOTES (protect during fixes):
  - Educational register на Георги Тодоров: първо лице само за собствената му методика („Правя
    верификацията предварително…") — заслужено, не разказан анекдот. НЕ пипай.
  - Асиметричен завършек („…държа банковия превод за случаите, в които сумата го оправдава.") — взема
    страна, не е симетричен both-sides поклон. НЕ изглаждай към баланс.
  - Примерните числа (срокове, €20/€5/€10, десетки хиляди евро) са явно маркирани „примерни" по
    изискване на бранда → НЕ сваляй етикета.

FACT & CLAIM SWEEP:
  - Sourced (OK да се твърди): SEPA ~един работен ден; SEPA Instant за секунди 24/7; SEPA само в евро,
    зона над 40 държави; казиното обикновено не таксува, банката може да начисли; cut-off → следващ
    работен ден; по-големи суми → допълнителна AML проверка.
  - [CONFLICT]: 0. [DATA NEEDED]: 0. Version A/B структура: няма.
  - Em-dash в публикуемото тяло: 0. En-dash само в „10:00–17:00" (RG футър).

RECALC CHECK: няма превъртане/бонус/оценка аритметика за преизчисляване (payments guide). Няма
числова несъгласуваност между 02→05b (примерните прагове и срокове са идентични във всички стадии).
```

## PHASE 2 — FIXES APPLIED
1. Стрипнати всички стадийни бележки (SEO AUDIT ред с единствения em-dash, INTERNAL-LINK suggestions,
   CANON/FLAGS footers) от публикуемия файл 05b. Резултат: 0 em-dash в целия 05b (title, meta, тяло,
   ALT, футър), en-dash само в „10:00–17:00".
2. Потвърдени всички untouchables на място (виж чеклист по-долу).
3. Нищо от гласа/числата/флаговете не е отслабено или премахнато. [VERIFY] флагът остава за човека.

## UNTOUCHABLES CHECKLIST (05b)
- [x] In-body RG touch + verbatim „18+ Хазартът може да пристрасти. Играйте отговорно."
- [x] Byline „**Георги Тодоров**" + „Публикувано: 01.10.2026 · Последна редакция: 01.10.2026"
- [x] „[About Всички Казина boilerplate]" placeholder slot (буквално)
- [x] Пълен „**Отговорна игра.**" футър (регистър на уязвимите лица към НАП + „Солидарност" 0888 99 18 66, 10:00–17:00)
- [x] Пълен „**Разкриване на партньорства.**" футър (1 авг 2026 / ДВ бр. 69 / заявление подадено-очаква-издаване)
- [x] Title tag (≤60) + Meta description (≤160) най-горе, после `---`, после H1
- [x] 0 em-dash; 2–4 whitelisted вътрешни линка (4, вплетени)

Final verdict: PASS WITH FIXES → ready to ship as 05b (human review PR).
