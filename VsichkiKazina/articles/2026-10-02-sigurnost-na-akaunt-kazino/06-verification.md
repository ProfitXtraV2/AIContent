# 06 — Verification · vk-0235 · Сигурност на акаунта в онлайн казино

## SURVIVING FLAGS IN 05b: none.
[VERIFY] = 0 · [DATA NEEDED] = 0 · [CONFLICT] = 0 · [LINK NEEDED] = 0.
The piece is concept-level player education. No operator, no НАП register data, no quoted statistic, no tax claim, no affiliate link. Mechanisms are stated instead of cited figures, which is why nothing needs human verification before publish.

## TIME-SENSITIVE / EXTERNAL-STAT CLAIMS: none in the text.
Deliberately excluded (would have been [VERIFY]): SIM-swap loss totals, "% of account takeovers from reused passwords". The brief required any specific external statistic to be flagged; the cleaner route for a concept guide was to describe the mechanism and omit the number. The best-practice claims that remain are standard and sourceable:
- Authenticator app (TOTP) safer than SMS; SMS exposed to SIM swap; save backup codes offline; pair with a unique password from a manager — Keeper Security: https://www.keepersecurity.com/blog/2024/02/15/authenticator-app-vs-sms-authentication-which-is-safer/
- Phishing red flags (urgency, lookalike sender/domain, password requests), fake login pages, navigate via bookmark/typed address — Kaspersky: https://www.kaspersky.com/resource-center/preemptive-safety/phishing-prevention-tips ; Microsoft: https://support.microsoft.com/en-us/security/protect-yourself-from-phishing
- Account takeover rides weak/reused passwords + missing MFA; unique passwords limit blast radius; go directly to the official site to check alerts — FBI IC3: https://www.ic3.gov/CrimeInfo/AccountTakeover

## PASSWORD-LENGTH GUIDANCE ("Дванайсет знака са разумен минимум")
Treated as standard general advice, not a cited external statistic, so left unflagged. If an editor prefers a hard source, NIST SP 800-63B (memorized-secret length) is the conventional reference. Not required for publish.

## ANTI-CANNIBALIZATION (confirmed DISTINCT)
- Payment-transaction security (SSL/TLS, PCI DSS, 3-D Secure, tokenization) = vk-0231. Referenced here in ONE sentence only ("сигурност на транзакцията"), not re-explained.
- Data privacy / GDPR rights = vk-0234. Referenced here in ONE sentence only ("защита на данните"), not re-explained.
- This page stays strictly on LOGIN/ACCOUNT access. No overlap beyond the two one-sentence pointers.

## INFOGRAPHIC SPEC — images/sigurnost-akaunt-sloeve.svg
Concept: a clean conceptual diagram of the FOUR defence layers that stand between an attacker and the account (stacked bands, or concentric rings around a core). Conceptual only. NO hard numbers anywhere in the graphic except the layer COUNT of four, which is carried by the words „няколко слоя … четири" in the body and „Четирите слоя" in the caption. No percentages, no odds, no money figures.

Core being protected (center / innermost):
- Label: „Акаунтът" with sub-line „баланс · документи · метод на плащане"
- Traces to 05b intro sentence: „Акаунтът в онлайн казино събира на едно място пари, сканирани документи от верификацията и често запазена банкова карта или портфейл."

The four layers, outer → inner (or top → bottom), each a labelled band:
1. „Уникална парола (в мениджър)" — traces to S3 „Паролата: дълга, уникална и скрита в мениджър" / closing „уникална парола в мениджър".
2. „Двуфакторна автентикация (приложение)" — traces to S4 „Двуфакторна автентикация: приложение или SMS" / closing „двуфакторна автентикация през приложение".
3. „Разпознаване на фишинг" — traces to S5 „Как изглежда фишингът при казино".
4. „Сигурно устройство и имейл" — traces to S6-intro paragraph „Устройството и имейлът ви са част от акаунта".

Optional one-line footer inside the SVG (no number): „Падне ли един слой, следващият печели време." — verbatim idea from S2 closing sentence („Падне ли един слой, следващият печели време и често спира превземането на акаунта, преди да стигне до баланса.").

Colour/style: brand-neutral, legible in light and dark, no emoji, no checkmarks. ALT text and caption already in 05b (zero em-dashes).

NUMBER TRACEABILITY (every graphic number → a 05b sentence):
- „4" (четири layers) → body „няколко слоя, които се подпират взаимно: силна и уникална парола, втори фактор при влизане, око за фалшиви съобщения и чисти устройство и имейл" (four items) + caption „Четирите слоя на защита на акаунта". CONFIRMED. No other numbers in the graphic.

## SANITY-CHECKED FIGURE (the only count in the piece)
Four layers = four proactive defence sections of the article:
S3 парола + S4 2FA + S5 фишинг + S6 устройство/имейл = 4. The frame section (S1) introduces them; the recovery section ("Ако акаунтът ви вече е компрометиран") and the closing verdict are not layers. Count re-derived independently: 4. Matches „четири/четирите слоя" in ALT, caption and the roadmap sentence. CONFIRMED.

## COMPLIANCE SPOT-CHECK (05b whole file)
- Em-dashes (—): 0. · En-dash (–): only in verbatim RG footer time range 10:00–17:00 (from exemplar).
- Byline „Георги Тодоров": present (not a team byline). Brand „Всички Казина": exact, no transliteration.
- Dates 02.10.2026 (публикувано + последна редакция): present.
- Verbatim „18+ Хазартът може да пристрасти. Играйте отговорно.": present inline + in RG footer.
- RG signposting /otgovorna-igra/ + регистър на уязвимите лица (НАП) + Солидарност 0888 99 18 66: present.
- Verbatim affiliate-licensing footer (1 август 2026, ДВ бр. 69 от 31.07.2026, „подало заявление … очаква издаването му", no issued-licence claim): present.
- Internal links (approved set): /zakonno-li-e/, /depoziti-i-teglenia/, /otgovorna-igra/ = 3 distinct in body.
- Banned AI connectives / promise / hype words: 0.
- Title 43 chars (≤60) · Meta 141 chars (≤155) · Body ~1122 words (target 1000–1400).

## HUMAN-ACTION LIST
- Author the SVG per the spec above (orchestrator) + optional hero.
- Fill the [About Всички Казина boilerplate] slot with the standard boilerplate at Step 8.
- Nothing to resolve: 0 [VERIFY] / 0 [DATA NEEDED].

---

## Автопилот финализация — Step-7 + Step-8 (2026-10-02)

- **Gemini Step-7 (текст):** human-likeness по пасове (шумен детектор): initial 20 → humaniser-1 **30 (BEST)** → humaniser-2 20. KEEP-BEST възстанови humaniser пас 1. Финален вердикт на запазената версия: „Shows AI patterns 70%" → **ai 70**. Остатъчни [VERIFY]/[DATA NEEDED]: **0**.
- **Step-8 изображения:** 2 (инфографика `sigurnost-akaunt-sloeve.svg` — Gemini review **100 PASS**, всички етикети проследени към 05b, 0 integrity; hero `sigurnost-akaunt-hero.webp` 16.5 KB WebP — Gemini review **100 PASS**, абстрактна метафора, без лица/лого/UI/текст). images: 2 (infographic 100, hero 100).
- **0 em-dash** в целия 05b. Byline Георги Тодоров; brand „Всички Казина"; 3 вътрешни връзки (/zakonno-li-e/, /depoziti-i-teglenia/, /otgovorna-igra/). Без назован оператор → без affiliate връзка.
