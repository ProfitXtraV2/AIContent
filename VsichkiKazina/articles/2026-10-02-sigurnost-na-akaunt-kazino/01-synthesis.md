# 01 — Synthesis · vk-0235 · Сигурност на акаунта в онлайн казино

QUERY: Сигурност на акаунта в онлайн казино: силна парола, двуфакторна автентикация и фишинг
MARKET: bg · BYLINE: editorial (signature Георги Тодоров)
INTENT: A player wants to know how to keep their own casino account from being stolen: what a strong password looks like, whether/how to use 2FA, how to spot phishing, and what to do if the account is already breached.

## ENTITY / TERM UNION (to cover)
сигурност на акаунт, силна парола, уникална парола, повторно използвана парола, мениджър на пароли, двуфакторна автентикация (2FA), приложение за автентикация (TOTP), SMS код, SIM swap, резервни кодове, фишинг, смишинг (SMS), огледален/фалшив сайт, фалшива страница за вход, подател/адрес на линка, спешност/urgency, превземане на акаунт (account takeover), възстановяване на парола, имейл като резервен ключ, устройство/заключен екран, публична Wi-Fi, прекратяване на сесии („излез от всички устройства"), поддръжка, временно заключване, нова верификация (KYC).

## VERIFIED FACTS (from security best-practice sources — see 00-brief)
1. Reused passwords are the dominant account-takeover vector (credential stuffing after an unrelated breach). Unique-per-site passwords contain the damage. [IC3; Kaspersky]
2. Length (a long passphrase) beats exotic characters for human-memorable, machine-resistant passwords. A password manager generates + stores unique passwords and autofills only on the correct domain. [general best-practice]
3. 2FA adds a second factor (one-time code). Authenticator app (TOTP) > SMS: app codes are generated locally and not transmitted (cannot be intercepted); SMS is exposed to SIM swap and to codes phished on a fake page. Save backup codes offline. [Keeper Security]
4. Phishing manufactures urgency ("account frozen", "verify now", "bonus expires in an hour") and routes to a lookalike/mirror domain whose login page harvests credentials (and sometimes the live 2FA code). Defences: operators never ask for your password by email; don't log in via links in messages; navigate via bookmark/typed address; check the real sender/link domain. [Kaspersky; Microsoft]
5. The recovery email is the backstage key: compromise it and the attacker resets the casino password. Secure the email with its own strong password + 2FA. Device hygiene (lock screen, updates, avoid shared/public machines, caution on public Wi-Fi, log out) matters. [general best-practice]
6. If compromised: change password (and email password), revoke active sessions ("log out all devices"), enable 2FA, contact support to temporarily lock the account; operators freeze withdrawals and re-run KYC on suspected fraud. [general best-practice]

## CONFLICTS: none.
## EXCLUDED CLAIMS
- Specific statistics (SIM-swap loss totals, % of breaches from reused credentials) excluded to keep the piece concept-level and flag-free; mechanism stated instead. Any figure would be [VERIFY].
- Payment-transaction security (SSL/PCI/3DS/tokenization) → out of scope (vk-0231), one-sentence reference only.
- Data-privacy/GDPR rights → out of scope (vk-0234), one-sentence reference only.
- No operator named; no НАП register data; no affiliate link (no recommendation).

## SUGGESTED PERSONA: Editorial (neutral „ние"/second person), signature Георги Тодоров. Guide register = patient teacher, consumer-protection, dry edge.

## DRAFT (original BG, facts-in-expression-out) — carried to Step 2
[Full prose drafted at Step 2 against the Step 1.5 outline; see 02-draft.md. All six fact clusters covered; one „не A, а B" antithesis allowed; ZERO em-dashes; asymmetric ending.]

## FLAGS: [VERIFY] 0 · [CONFLICT] 0 · [DATA NEEDED] 0 (concept-level piece, mechanism over cited figures).
