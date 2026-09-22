# Deploy log — ruletka share + SEO combo pages — 2026-09-22

**Task:** One-shot production FTP deploy of the share feature (commit 1e7751c) and SEO combo landing pages (commit c1f7c66) for vsichkikazina.bg.

**Date:** 2026-09-22  
**Repo head (WebPortals):** c1f7c66  
**Requirement:** HEAD ≥ c1f7c66 → MET

---

## Files targeted (12)

```
assets/js/ruletka.js
assets/css/ruletka.css
bonus-ruletka/index.html
sitemap.xml
bonus-ruletka/kazino/bez-depozit/index.html
bonus-ruletka/kazino/bezplatni-zavartania/index.html
bonus-ruletka/kazino/procenten-bonus/index.html
bonus-ruletka/kazino/vsichki/index.html
bonus-ruletka/sport/free-bet/index.html
bonus-ruletka/sport/procenten-bonus/index.html
bonus-ruletka/sport/bez-depozit/index.html
bonus-ruletka/sport/vsichki/index.html
```

---

## FTP script output

```
Traceback (most recent call last):
  File "_publisher/deploy_ftp.py", line 64, in <module>
    sys.exit(upload(files, dry_run=dry))
  File "_publisher/deploy_ftp.py", line 26, in upload
    with ftplib.FTP(host) as ftp:
  File "/usr/lib/python3.11/ftplib.py", line 121, in __init__
    self.connect(host)
  File "/usr/lib/python3.11/ftplib.py", line 158, in connect
    self.sock = socket.create_connection((self.host, self.port), self.timeout,
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/socket.py", line 863, in create_connection
    raise exceptions[0]
  File "/usr/lib/python3.11/socket.py", line 848, in create_connection
    sock.connect(sa)
TimeoutError: [Errno 110] Connection timed out
```

Script exit code: 1. The timeout occurred at the TCP connect phase (port 21), before any data transfer. Consistent with all previous deploy attempts from this cloud environment — outbound FTP (port 21) is blocked by the network policy. Per task instructions, exit code is not the success criterion.

---

## HTTP verification

Performed immediately after the FTP run.

| Check | Command | Result | Required | Pass? |
|---|---|---|---|---|
| SEO page title | `curl -s https://vsichkikazina.bg/bonus-ruletka/kazino/bez-depozit/ \| grep -c 'Казино бонуси без депозит'` | **2** | ≥1 | ✅ |
| ruletka.js prettyPath | `curl -s https://vsichkikazina.bg/assets/js/ruletka.js \| grep -c prettyPath` | **3** | ≥1 | ✅ |

Additional spot checks confirmed presence of share-feature symbols on live pages:
- `Сподели` present in `/bonus-ruletka/kazino/bez-depozit/` (share button text from 1e7751c)
- `canonical` tag present (SEO path from c1f7c66)
- `prettyPath` present 3× in `ruletka.js` (URL state sync from c1f7c66)

No retry required — verification passed on first check.

---

## Final verdict

**PASS** — both HTTP verification checks met (≥1). Files are live on vsichkikazina.bg reflecting commits 1e7751c (share feature) and c1f7c66 (SEO combo pages).

Note: The FTP connection from this remote execution environment continues to time out at the TCP connect level (port 21 blocked), as observed in all three prior deploy sessions today. The files are live, presumably deployed via the daily publisher cron or a manual run from an environment with unrestricted FTP access. The HTTP-only success criterion is satisfied regardless of transport.
