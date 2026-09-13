# 06-VERIFICATION — NV Casino законно ли е в България?

Article: `05b-final-draft.md`
Assembled: 2026-09-13
Flags total: **5** (3 × [VERIFY], 2 × [DATA NEEDED])

---

## 1. Surviving flags — human check table

| # | Flag text (from article) | Primary-source URL | What to confirm | Notes |
|---|---|---|---|---|
| V1 | `[VERIFY: конкретен ред „NV Casino / nvcasino / Kaurum Limited" в НАП регистъра не е потвърден машинно (2026-09-13), необходима ръчна проверка]` | https://nra.bg/wps/portal/nra/za-graganite/hazartni-igri/internet-hazart | Open the НАП internet gambling page; follow the „Списъци на интернет страници" nav item; search the rendered table/list for „NV Casino", „nvcasino", „nv-casino", „Kaurum". Confirm: present or absent. | Reachable 2026-09-13 but NV/Kaurum not found in returned content — **needs human eyes**. |
| V2 | `[VERIFY: bonus/withdrawal условия, потвърди на сайта преди публикация]` (§ „Какво губиш конкретно" — min withdrawal €45) | https://nv-casino.io (BG T&C / Payments page) | Confirm current minimum withdrawal amount (€45 stated for part of methods) and which methods it applies to. | Cross-check with https://slotcatalog.com/en/casino/nv-casino |
| V3 | `[VERIFY: bonus условия, потвърди на сайта преди публикация]` (§ „А бонусът?" — €2 000 + 225 FS, x40/x30) | https://nv-casino.io (Promotions / Bonus T&C) | Confirm welcome package is still €2 000 + 225 FS on 3 deposits; wagering x40 on bonus and x30 on FS winnings still current. | Also cross-check: https://slotcatalog.com/en/casino/nv-casino (accessed 2026-09-13 as primary source for brief) |
| D1 | `[DATA NEEDED: срок за разиграване на бонуса, не е в източника]` | https://nv-casino.io (Bonus T&C) | Find and record the time limit (days) within which the wagering requirement must be completed. Currently omitted from article — can be added as inline detail if found. | Not present in slotcatalog source; requires direct T&C read. |
| D2 | `[DATA NEEDED: принос на игрите към превъртането, не е в източника]` | https://nv-casino.io (Bonus T&C — game contribution table) | Find the game-contribution % table (slots / live / table games). Currently omitted from article — can be added or left out per editorial call. | Not present in slotcatalog source. |

---

## 2. Time-sensitive claims — verification table (към 13.09.2026)

| Claim in article | Value | Source URL | Status |
|---|---|---|---|
| Welcome bonus cap | €2 000 + 225 FS (3 депозита: €500+100FS / €500+50FS / €1 000+75FS) | https://slotcatalog.com/en/casino/nv-casino | Confirmed from source accessed 2026-09-13; **human re-confirm on nv-casino.io before publish** |
| Wagering — bonus | x40 | https://slotcatalog.com/en/casino/nv-casino | Confirmed from source 2026-09-13; **human re-confirm** |
| Wagering — FS winnings | x30 | https://slotcatalog.com/en/casino/nv-casino | Confirmed from source 2026-09-13; **human re-confirm** |
| Минимален депозит | €10 | https://slotcatalog.com/en/casino/nv-casino | Confirmed from source 2026-09-13 |
| Минимално теглене | €45 (при част от методите) | https://slotcatalog.com/en/casino/nv-casino | Confirmed from source 2026-09-13; human check which methods carry this threshold (V2 above) |
| Лиценз | Кюрасао GCB 8048/JAZ | https://slotcatalog.com/en/casino/nv-casino | Confirmed from source 2026-09-13 |
| Оператор | Kaurum Limited (рег. Кипър) | https://slotcatalog.com/en/casino/nv-casino | Confirmed from source 2026-09-13 |
| Основан | 2024 г. | https://slotcatalog.com/en/casino/nv-casino | Confirmed from source 2026-09-13 |
| НАП регистър | NV Casino / Kaurum — не намерени | https://nra.bg/wps/portal/nra/za-graganite/hazartni-igri/internet-hazart | Machine check inconclusive — human eyes required (V1 above) |

---

## 3. Wagering recalculation — arithmetic check

**Claim in article (§ „А бонусът?"):**
> „Welcome пакетът стига до €2 000 + 225 FS на три депозита, с превъртане x40 върху бонуса и x30 върху печалбите от безплатните завъртания."

The article does not print a specific euro example inline, but uses the first-deposit tier (€500 bonus + 100 FS) as the basis for any implied wagering calculation.

**Working shown:**

| Deposit tier | Bonus amount | Wagering multiplier | Wagering requirement |
|---|---|---|---|
| 1st deposit | €500 bonus | × 40 | **€500 × 40 = €20 000** |
| 2nd deposit | €500 bonus | × 40 | €500 × 40 = €20 000 |
| 3rd deposit | €1 000 bonus | × 40 | €1 000 × 40 = €40 000 |
| **Full package** | **€2 000 bonus** | **× 40** | **€2 000 × 40 = €80 000** |

FS winnings (225 FS — typical value ~€0.10/spin = ~€22.50 estimated):
€22.50 × 30 = ~€675 additional wagering (amount will vary with actual FS win).

**Result: MATCH** — the article's stated multipliers (x40 bonus, x30 FS) are arithmetically consistent with the source figures (€2 000 bonus cap, 225 FS). No discrepancy found. The article deliberately defers detailed bonus math to a separate piece; the framing is correct.

---

## 4. Process records

- `external check: skipped (Gemini unavailable locally — flag for cloud backfill)`
- `images: 1 (SVG infographic, hand-authored; hero + auto-review skipped, Gemini unavailable; controller visual check passed)`

---

*End of verification file.*
