# Deploy SEO Fixes — 2026-09-23

**Triggered:** scheduled one-shot task  
**Repo HEAD:** 7912a4d (feat(seo): IndexNow — site-root key file + stdlib submitter) — ≥ required d1b5bd0 ✓

---

## Step 1 — WebPortals git pull

```
From https://github.com/ProfitXtraV2/WebPortals
 * branch            main       -> FETCH_HEAD
   42aaa01..7912a4d  main       -> origin/main
Already up to date.
```

HEAD: `7912a4d feat(seo): IndexNow — site-root key file + stdlib submitter`  
Required minimum: `d1b5bd0` — satisfied ✓

---

## Step 2 — FTP Deploy attempt

**Command:** `python3 _publisher/deploy_ftp.py .htaccess bonus-ruletka/index.html bonus-ruletka/kazino/bez-depozit/index.html bonus-ruletka/kazino/bezplatni-zavartania/index.html bonus-ruletka/kazino/procenten-bonus/index.html bonus-ruletka/kazino/vsichki/index.html bonus-ruletka/sport/free-bet/index.html bonus-ruletka/sport/procenten-bonus/index.html bonus-ruletka/sport/bez-depozit/index.html bonus-ruletka/sport/vsichki/index.html bonusi/bez-depozit/index.html bonusi/bezplatni-zavartania/index.html bonusi/betano-200-bezplatni-zavartania/index.html bonusi/mrbit-nachalen-bonus/index.html bonus-category/welcome-bonus/index.html kontakti/index.html obshti-usloviya/index.html`

**Script output (exit 1):**
```
Traceback (most recent call last):
  File ".../deploy_ftp.py", line 64, in <module>
    sys.exit(upload(files, dry_run=dry))
  File ".../deploy_ftp.py", line 26, in upload
    with ftplib.FTP(host) as ftp:
  File ".../ftplib.py", line 121, in __init__
    self.connect(host)
TimeoutError: [Errno 110] Connection timed out
```

**Diagnosis:** Outbound TCP port 21 (FTP) is blocked by this cloud environment's network policy. Port 21 and port 22 both unreachable from container (`nc -zv ftp.vsichkikazina.bg 21` timed out). This is a network-level block, not an FTP server issue. Re-run was not attempted (re-run cannot overcome a network block; HTTP verification used as per task instructions).

**FTP_HOST:** ftp.vsichkikazina.bg  
**FTP_USER:** aicontent@vsichkikazina.bg  
**FTP_DIR:** public_html

---

## Step 3 — HTTP Verification

Per task instructions, HTTP checks are the authoritative measure of success.

### Check 1 — bonus-ruletka page content
```
curl -s https://vsichkikazina.bg/bonus-ruletka/ | grep -c 'Направо към офертите'
```
**Result:** `1`  
**Required:** ≥ 1  
**Status: PASS ✓**

### Check 2 — /software/netent/ redirect
```
curl -s -o /dev/null -w '%{http_code} %{redirect_url}' https://vsichkikazina.bg/software/netent/
```
**Result:** `301 https://vsichkikazina.bg/blog/games-providers/`  
**Required:** 301, redirect_url ending `/blog/games-providers/`  
**Status: PASS ✓**

### Check 3 — /deposit-method/visa/ redirect
```
curl -s -o /dev/null -w '%{http_code} %{redirect_url}' https://vsichkikazina.bg/deposit-method/visa/
```
**Result:** `301 https://vsichkikazina.bg/depoziti-i-teglenia/`  
**Required:** 301, redirect_url ending `/depoziti-i-teglenia/`  
**Status: PASS ✓**

---

## Overall Verdict

| Criterion | Result |
|---|---|
| HEAD ≥ d1b5bd0 | ✓ PASS (7912a4d) |
| FTP upload script exit code | ✗ FAIL (port 21 blocked in container) |
| HTTP check 1 (bonus-ruletka content) | ✓ PASS |
| HTTP check 2 (netent 301 redirect) | ✓ PASS |
| HTTP check 3 (visa 301 redirect) | ✓ PASS |

**HTTP VERDICT: ALL CHECKS PASS** — content and redirects live on vsichkikazina.bg as expected. FTP transport was blocked by the container network policy; files appear to already be deployed (possibly from a prior run or manual deploy outside this session).

**Action required:** To enable FTP deploys from cloud container sessions, the environment network policy needs to permit outbound TCP port 21 to `ftp.vsichkikazina.bg`. For subsequent scheduled deploys, consider switching to SFTP (port 22) or HTTPS-based deployment if the host supports it.
