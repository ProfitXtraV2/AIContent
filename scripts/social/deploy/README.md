# The guest: what runs there and how it is installed

The publishing check, the control loop, Postiz, Caddy, Authelia and cloudflared run in one
Ubuntu 24.04 Hyper-V guest on the ProfitXtra Windows host (tech spec, "Host and guest
deployment"). `SOCIAL-SETUP.md` at the repository root is the checklist; this folder holds the
files it uses. Nothing here holds a key: every secret lives in `/etc/px-social/` in the guest.

| File | What it is | Where it goes |
|---|---|---|
| `qualify-host.ps1` | S0: reads the Windows host (edition, Hyper-V, resources, power, updates, BitLocker, every administrator and remote-access tool) | Run elevated on the host; paste the output into `SOCIAL-SETUP.md` |
| `audit-host.ps1` | The monthly host audit (administrators, remote access, BitLocker) | Same, monthly |
| `docker-compose.override.yml` | Postiz pinned by digest, `API_LIMIT=600`, no LAN port; Caddy, Authelia, cloudflared | Next to the official `postiz-docker-compose` file |
| `Caddyfile` | `social.<domain>` behind Authelia (two-step sign-in), `/uploads/*` public, `/api/public/*` answers 403 | `/opt/postiz/Caddyfile` |
| `authelia-configuration.yml` | Two users, `two_factor` for `social.<domain>`, filesystem notifier; secrets from files | `/opt/postiz/authelia/configuration.yml` |
| `cloudflared.yml` | The named tunnel: `social.` and `auth.` to Caddy, everything else 404 | `/etc/px-social/cloudflared/config.yml` |
| `env.example` | The names of the check's settings and secrets (no values) | `/etc/px-social/env` (mode 600, owner `px-social`) |
| `px-social.tmpfiles.conf` | `/run/px-social/` for the shared lock | `/etc/tmpfiles.d/` |
| `px-social-check.service` / `.timer` | The publishing check, minute :10 of every hour, `Persistent=true` | `/etc/systemd/system/` |
| `px-social-control.service` / `.timer` | The control loop, every 5 minutes | `/etc/systemd/system/` |
| `px-social-backup.service` / `.timer`, `backup.sh` | 03:30 UTC: Postiz database, the check's SQLite and `/uploads`, encrypted with `age`, copied off the host, kept 14 days | `/etc/systemd/system/`, `/opt/px-social/backup.sh` |
| `deploy.sh` | Installs a release tag of `scripts/` after `git verify-tag` against the two allowed SSH keys | Run by Nikolay or the setup person over SSH |
| `git-askpass.sh` | Gives git the App installation token of one run, from that run's environment only | Used by `publishing_check.py` |

Both timers wrap their command in `flock -w 240 /run/px-social/lock`, so the check and the
control loop never run at the same time. The report job (`px-social-report`, 05:00 UTC) comes
with Release 2.

The `.sh` files must be executable in the release: when committing them, run
`git update-index --chmod=+x scripts/social/deploy/*.sh` (Windows checkouts do not keep the bit).
