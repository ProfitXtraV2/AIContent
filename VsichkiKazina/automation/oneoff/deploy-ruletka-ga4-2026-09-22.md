# Deploy Log: ruletka GA4 events — 2026-09-22

**Status: FAILED — FTP connection timed out on all 3 attempts**

## Pre-flight

- Repo: `profitxtrav2/webportals`
- `git pull origin main` completed successfully
- HEAD confirmed: `400e32f feat(ruletka): GA4 funnel events — start/vertical/type/results/chip/restart/affiliate_click` ✓
- Files targeted: `assets/js/ruletka.js`, `bonus-ruletka/index.html`

## Deploy attempts

| Attempt | Started (UTC) | Result |
|---------|--------------|--------|
| 1 | 15:18:42 | `TimeoutError: [Errno 110] Connection timed out` |
| 2 | 15:21:57 | `TimeoutError: [Errno 110] Connection timed out` |
| 3 | 15:25:12 | `TimeoutError: [Errno 110] Connection timed out` |

60-second wait between each attempt.

## Raw error (identical on all 3 attempts)

```
Traceback (most recent call last):
  File "_publisher/deploy_ftp.py", line 64, in <module>
    sys.exit(upload(files, dry_run=dry))
  File "_publisher/deploy_ftp.py", line 26, in upload
    with ftplib.FTP(host) as ftp:
  File "/usr/lib/python3.11/ftplib.py", line 121, in __init__
    self.connect(host)
  File "/usr/lib/python3.11/ftplib.py", line 158, in connect
    self.sock = socket.create_connection((self.host, self.port), self.timeout, ...)
TimeoutError: [Errno 110] Connection timed out
```

## HTTP verification

Not performed — no files were uploaded.

## Notes

- The morning publisher run deploys fine from this environment; connectivity to the FTP host appears intermittent during this time window.
- Files remain at the state before this run. The GA4 events in `400e32f` are **not yet live** on vsichkikazina.bg.
- Manual re-run or next scheduled publisher run required to complete the deploy.
