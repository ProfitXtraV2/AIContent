# Social posts — setup and records

Setting up the social posts of the publishing tool, and the records the product relies on: the
host qualification and monthly audits, the identities list, the setup checks V1–V11 and the test
posts. `settings.py` reads the dates recorded here through `settings.md` (`identities_verified`,
`test_post_seen`, `profile_link_set`).

Who does it: **the setup person**, with **Nikolay** confirming where a step says so. Nobody else
gets administrator rights on the host or SSH into the guest.

The design is in the XtraFlow tech spec "AIContent: постове в социалните мрежи". The code is in
`scripts/social/`, the guest's files are in `scripts/social/deploy/` (see its README).

## The simple way: publishing from a team member's computer

Since 2026-11 each person who publishes runs Postiz and the publishing check on their own
computer, instead of the guest below. One brand is published from one computer: the brand's
`publisher` setting names that person's GitHub login, and only that computer hands its posts over.

1. **Once, the person who already publishes** makes the team code from their working Postiz:
   `python scripts/social/local/setup.py team-code --from <their Postiz folder>`. It holds the
   network apps' keys (Meta and others), so it is sent only in private.
2. **Each person** opens PowerShell and pastes one line:
   `irm https://raw.githubusercontent.com/ProfitXtraV2/AIContent/main/scripts/social/local/install.ps1 | iex`.
   It installs Git, Python, GitHub CLI, ngrok and Docker Desktop (a restart, then the same line
   again), signs in to GitHub and runs the setup, which asks in Bulgarian for:
   - the team code;
   - a free ngrok account and its domain;
   - the person's own Postiz account and channels (Add Channel);
   - Postiz's API key.
3. **The setup prints two addresses for the Meta app.** Whoever runs the app adds them once
   (Valid OAuth Redirect URIs) and, while the app is not Live, adds the person's accounts as testers.
4. **The setup links the brands this computer publishes.** It opens the issue
   "social: settings <brand>" with `publisher` and the accounts' channel IDs; merging its PR makes
   it count.
5. **Windows runs it on its own:** the check every hour at :10, the control loop every 5 minutes,
   Postiz and the tunnel at logon (`scripts/social/local/run.py`). The computer must be on when a
   post is due. `python run.py status` shows what it publishes.

Everything personal stays in `%USERPROFILE%\px-social` and is never committed: the keys, Postiz,
and the check's record. A new brand needs no code: the dashboard's Settings tab has
**+ New brand** (name, site, topic, language). Its topic (`social/topics/`: casino, sports
betting, sport, dental, general) gives the brand its rules and first settings; the PR it opens
adds the brand to `social/brands.json` and to the dashboard (`docs/social/`). Every brand is shown
at `docs/social/?brand=<key>`.

---

## Rollout order and gates

Each step starts only when the one before it is done. Record the date and who confirmed it.

| # | Step | Done when | Date / who |
|---|---|---|---|
| 1 | Build R1 code, tests green, library in place | `python3 -m pytest scripts/tests -q` passes; `test_feed_unchanged.py` passes; the publisher's next real run queues nothing new | |
| 2 | Identities | Machine user and GitHub App created; routine account connected as the machine user; old token revoked; `AIContentTokenAll` replaced; identities list below, confirmed by Nikolay | |
| 3 | Host qualified, administrators removed | S0 recorded below; only the two people hold any administrator access on the host; BitLocker on | |
| 4 | Guest, Postiz, tunnel, Authelia | V7, V8 and V11 pass | |
| 5 | Network apps live | Meta app in Live mode with approved permissions; X and LinkedIn access; V1 test post seen by someone without an app role (recorded below) | |
| 6 | Postiz behaviour | V2–V6, V9 and V10 recorded; fallbacks applied where one fails | |
| 7 | Social Gemini billing | Separate Google AI Studio project and billing account; `SOCIAL_GEMINI_API_KEY` in the cloud environment | |
| 8 | Instagram profile link | Profile link set with its tags (below); `profile_link_set` in `settings.md` | |
| 9 | Sandbox walk-through | One `sandbox` pack goes the whole way of flow 0 with `DRY_RUN=1`: PR, checks, merge by Nikolay, go-live, planned hand-over in the audit log | |
| 10 | Settings PR | Nikolay merges `settings.md` with `social: on`, `identities_verified` and active accounts; the setup person adds the brand to `PX_SOCIAL_ENABLED_BRANDS` in the guest | |
| 11 | Legal opinion (Всички Казина only) | Nikolay's go after the opinion | |
| 12 | DentalVia | Its approval wiring, library, live signal and address pattern are settled (product spec, Open question 18) | |

Before step 10 the check may run, but every post stays "Held" and nothing reaches the networks:
`social` is off in `settings.md`, and `DRY_RUN=1` in the guest.

---

## 1. Repository settings (once)

- **Settings → General → Pull requests:** auto-merge **off**, merge queue **off**. With auto-merge,
  `merged_by` would be whoever enabled it, and a later push would be merged unseen (boundary 3).
- **Settings → Code security:** secret scanning and push protection **on**.
- **Branch rules on `main`:** if `main` is ever protected, the App `px-publishing-check` and
  `github-actions[bot]` stay allowed to push the ledger, the audit trail and the dashboard data;
  people still change `main` only through PRs.
- **Issues:** open and pin the issue **"Social control"**. Its number goes into
  `PX_SOCIAL_CONTROL_ISSUE` in the guest. Comments there: `/stop-now vsichkikazina`,
  `/lift vsichkikazina`.

## 2. Identities (step 2)

1. Create the machine user **`profitxtra-agent`** with a ProfitXtra mailbox and two-step sign-in.
   Add it to AIContent with **write**, and to WebPortals with **read** (write only if the publisher
   routine runs on the same Claude account).
2. On a clean shell profile: `gh auth login` as `profitxtra-agent`; then, in Claude Code signed in
   to the Claude account that owns the routines, run `/web-setup`. It replaces the account's
   GitHub connection.
3. In a test cloud session: `gh api user --jq .login` prints `profitxtra-agent`; a test branch
   push and a test PR show the machine user as author.
4. Revoke the token the first `/web-setup` connected (a copy of Nikolay's `gh` token); Nikolay
   signs in to `gh` locally again. Replace the WebPortals secret `AIContentTokenAll` with a
   machine-user token (contents write on AIContent only).
5. Create the GitHub App **`px-publishing-check`**, owned by the organisation, installed on
   AIContent only: contents **write**, pull requests **read**, issues **read**, metadata. Its
   private key goes only into the guest (`/etc/px-social/github-app.pem`, mode 600).
6. Run `GH_TOKEN=$(gh auth token) python3 scripts/social/list_identities.py` and paste the
   output under **Identities** below. Nikolay confirms that none of them acts as Nikolay's account.
   That date is `identities_verified` in `settings.md`.

## 3. The host (step 3)

1. Run `scripts/social/deploy/qualify-host.ps1` elevated on the host; paste the output under
   **Host qualification** below. The host qualifies with Hyper-V, 4 vCPU, 8 GB RAM and 80 GB
   free beyond what it already runs (the outreach app included), no sleep or hibernate, Windows
   Update active hours 09:00–20:00, and BitLocker on the guest's disk.
2. **The removal gate.** Every account other than Nikolay's and the setup person's leaves the
   local Administrators and Hyper-V Administrators groups, remote-management tools and
   remote-support apps; BitLocker recovery keys and physical access stay with the two people.
   This happens **before** the first secret enters the guest. A removal after that point means
   every guest secret is replaced (Postiz API key, App key, tunnel token, Authelia secrets,
   network logins).
3. Monthly: run `audit-host.ps1` and append the output under **Monthly host audits**.

## 4. The guest (step 4)

1. **VM:** Generation 2, Ubuntu 24.04, 4 vCPU, 8 GB fixed memory, 80 GB disk, in a folder only
   Administrators and SYSTEM can read. Automatic start with the host (no sign-in needed),
   clean shutdown with it. External virtual switch on the wired adapter, DHCP reservation.
2. **Guest settings:** SSH on the LAN address only, keys only, the two people's keys. UFW: inbound
   22 from the LAN, nothing else. Unattended security upgrades on. Time: systemd-timesyncd plus
   Hyper-V time sync (slots depend on it).
3. **Postiz:** Docker Engine; the official `postiz-docker-compose` in `/opt/postiz`, with
   `deploy/docker-compose.override.yml` next to it (every image pinned by digest). `.env`:
   `PX_DOMAIN`, `POSTIZ_DISABLE_REGISTRATION=false` until Nikolay has signed up, then `true`.
4. **Domain and tunnel:** a dedicated domain on Cloudflare's free plan (about $10 a year), a named
   tunnel; `deploy/cloudflared.yml` → `/etc/px-social/cloudflared/config.yml`. Zone: Bot Fight
   Mode **off** (Meta fetches `/uploads/*`), Always Use HTTPS **on**.
5. **Caddy and Authelia:** `deploy/Caddyfile` → `/opt/postiz/Caddyfile`;
   `deploy/authelia-configuration.yml` → `/opt/postiz/authelia/configuration.yml` with the domain
   filled in; `users.yml` with Nikolay and the setup person; the three Authelia secrets as files
   in `/etc/px-social/authelia/`.
6. **Keys, only after the removal gate:** Nikolay's Postiz user first, then an invite for the
   setup person; create the Postiz API key; install the App key; connect the network accounts.
7. **The check:** user `px-social` (system, no shell); `/var/lib/px-social` (mode 700) holding a
   clone of AIContent `main` (`AIContent/`) and `state.sqlite`; `/opt/px-social/src` (a clone used
   only to verify tags); `/etc/px-social/env` from `deploy/env.example` (mode 600) with
   `DRY_RUN=1`; `/etc/px-social/allowed_signers` with the two people's SSH keys. The code is
   standard-library Python only (Ubuntu's `python3`); no package is installed for it.
8. **Release:** `sudo /opt/px-social/deploy.sh <tag>` (the first time from the source clone). It
   refuses a tag that neither of the two keys signed (`git tag -s` with `gpg.format=ssh`).
9. **Timers:** `deploy/px-social.tmpfiles.conf` → `/etc/tmpfiles.d/`; the `.service` and `.timer`
   files → `/etc/systemd/system/`; `systemctl enable --now px-social-check.timer
   px-social-control.timer px-social-backup.timer`. Backups: `/etc/px-social/backup.env`
   (`BACKUP_DEST`, off the host), `/etc/px-social/age-recipients.txt` (the two public keys).
10. **Upgrades:** Postiz by changing its pinned digest after reading the release notes; the check
    by a new signed tag. Only the two people do either.

## 5. Day to day: what the banners ask for

| Banner on "Scheduled & published" | Who | What to do |
|---|---|---|
| reconnect account X | setup person | Reconnect the account in Postiz (`https://social.<domain>`) |
| publishing check not running | setup person | Look at the host and the guest: `systemctl status px-social-check.timer`, `journalctl -u px-social-check` |
| the publishing tool could not be reached / refused the API key | setup person | Postiz containers; a refused key is replaced in `/etc/px-social/env` |
| replace the … key | the key's owner | Replace it where it lives (table below); the banner clears after the next check |
| social image credits exhausted / image budget reached | setup person / Nikolay | Top up the social billing account, or raise `image_budget_usd` by a settings PR |
| settings changed without approval | the team | Make the change again from the dashboard's Settings tab (a PR someone with write access merges), or revert it |
| PR #N was merged by @someone, who cannot approve | the team | Its posts are not approved (a bot, or no write access any more); they come back in a fix PR to merge |
| Paused (stop now / tool / settings) | Nikolay | `/lift <brand>` on "Social control", or a settings PR that ends the pause |
| published post breaks a rule | Nikolay | Remove it on the network; it was edited in the tool after hand-over |
| posts not from a pack | Nikolay | Someone posted in the tool directly; check and remove it on the network if needed |

**Where each key lives** (I1): Postiz API key, GitHub App key, WebPortals read token — the guest's
`/etc/px-social/` only. Tunnel token — the guest's cloudflared folder. `SOCIAL_GEMINI_API_KEY` —
the Claude Code cloud environment. The English references need no key: the drafting agent writes them.
Network logins — Postiz. Replacing a key at its home and restarting the timer is enough.

---

## Records

### Host qualification
_Paste the output of `qualify-host.ps1` here, plus who holds the BitLocker recovery keys and who
has physical access._

### Monthly host audits
_Append the output of `audit-host.ps1` each month._

### Identities
_Paste the output of `list_identities.py` here; Nikolay confirms with date and initials._

### Setup checks V1–V11

| # | Check | How | Result (date, who) | Fallback taken |
|---|---|---|---|---|
| V1 | One visible test post per account (D3) | Posted from Postiz; seen by someone without an app role | | |
| V2 | A LinkedIn Page carousel arrives as a document | `post_as_images_carousel: true` test post | | If not: LinkedIn posts use a single image and the PR says so |
| V3 | A disabled channel's queued post does not publish | Disable the channel across a test slot | | Either way the control loop deletes those posts within 5 minutes |
| V4 | The tool gives back exactly the text sent | Compare `content` from `GET /posts` after normalising, for `POSTIZ_CONTENT_FORMAT=html` and `text` | | Keep the format that round-trips |
| V5 | A deleted post never publishes; deleting one post leaves the others of the pack | Two test posts in separate groups, delete one | | |
| V6 | Per-post statistics per network | `GET /analytics/post/{postId}` on a published test post | | R2 shows n/a where empty |
| V7 | No Postiz page, its own password page included, without Authelia's second step | Open the pages from outside, signed out | | |
| V8 | `/api/public/*` answers 403 through the tunnel; the check reaches it on 127.0.0.1; Postiz's server-side calls work | `curl` from outside and inside | | |
| V9 | The flag the API returns for an expired login | Let a test account's login expire, read `GET /integrations` | | The check holds an account for 6 hours after a login error |
| V10 | What happens when Postiz is down at a slot | Stop the containers across a test slot, start them again | | The check's rule handles late, failed and still-queued posts |
| V11 | An Instagram post publishes with its image fetched through the tunnel | Test post with an image | | |

### Test posts seen (D3)
| Account | Date | Seen by (no app role) | How |
|---|---|---|---|
| | | | |

### Instagram profile link (B6)
| Account | Link set | Date |
|---|---|---|
| ig-vsichkikazina | `https://vsichkikazina.bg/blog/?utm_source=instagram&utm_medium=social&utm_campaign=profile&utm_content=ig-vsichkikazina` | |

### Brands switched on in the guest
| Brand | Date | By | After Nikolay's settings merge |
|---|---|---|---|
| | | | |
