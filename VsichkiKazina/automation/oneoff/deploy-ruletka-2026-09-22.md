# Deploy Log — Бонус Рулетка — 2026-09-22

**Status:** FAILED — FTP network unreachable from remote execution environment  
**Commit deployed:** 42aaa01 (fix: apply ruletka integration to linii-na-pechalba)  
**Source range:** 0833a6f..42aaa01 (HEAD)  
**File count:** 104 (sanity check: PASS — within 90–120 expected range)  
**Run date:** 2026-09-22  

---

## Pre-flight checks

| Check | Result |
|-------|--------|
| `git pull origin main` | Already up to date |
| HEAD commit ≥ 42aaa01 | ✅ HEAD = 42aaa01 |
| Changed-file count (90–120) | ✅ 104 files |
| FTP env vars present | ✅ FTP_HOST, FTP_USER, FTP_PASS, FTP_DIR all set |
| Dry-run (all 104 files found locally) | ✅ All 104 confirmed |

---

## Dry-run plan (all 104 files confirmed present)

```
DRY-RUN would upload: 404.html
DRY-RUN would upload: assets/css/ruletka.css
DRY-RUN would upload: assets/css/style.css
DRY-RUN would upload: assets/data/README.md
DRY-RUN would upload: assets/data/bonuses.json
DRY-RUN would upload: assets/img/og/linii-na-pechalba.webp
DRY-RUN would upload: assets/js/ruletka.js
DRY-RUN would upload: blog/20-super-hot/index.html
DRY-RUN would upload: blog/40-super-hot/index.html
DRY-RUN would upload: blog/amusnet-egt-provajdar/index.html
DRY-RUN would upload: blog/bakara-pravila/index.html
DRY-RUN would upload: blog/bezplatni-kazino-igri/index.html
DRY-RUN would upload: blog/bonus-bez-depozit-2026/index.html
DRY-RUN would upload: blog/bonus-pri-registraciya/index.html
DRY-RUN would upload: blog/bonuses-vip/index.html
DRY-RUN would upload: blog/burning-hot/index.html
DRY-RUN would upload: blog/casino-payments/index.html
DRY-RUN would upload: blog/comparisons-news/index.html
DRY-RUN would upload: blog/danaci-pechalbi-onlajn-kazino/index.html
DRY-RUN would upload: blog/evro-hazart-depoziti/index.html
DRY-RUN would upload: blog/games-providers/index.html
DRY-RUN would upload: blog/gates-of-olympus/index.html
DRY-RUN would upload: blog/index.html
DRY-RUN would upload: blog/kak-raboti-razigravaneto/index.html
DRY-RUN would upload: blog/kak-se-igrae-poker-kazino/index.html
DRY-RUN would upload: blog/keno-pravila/index.html
DRY-RUN would upload: blog/koe-kazino-da-izberete/index.html
DRY-RUN would upload: blog/krash-igri-aviator/index.html
DRY-RUN would upload: blog/licenzirane-afiliejt-sajtove-2026/index.html
DRY-RUN would upload: blog/linii-na-pechalba/images/linii-na-pechalba-rotativki-hero.webp
DRY-RUN would upload: blog/linii-na-pechalba/images/linii-zalog-na-zavarshtane.svg
DRY-RUN would upload: blog/linii-na-pechalba/images/nachinite-za-pechalba-243-1024-117649.svg
DRY-RUN would upload: blog/linii-na-pechalba/index.html
DRY-RUN would upload: blog/novi-kazino-igri-2026/index.html
DRY-RUN would upload: blog/novo-onlajn-kazino/index.html
DRY-RUN would upload: blog/nv-casino-bonus-usloviya/index.html
DRY-RUN would upload: blog/nv-casino-zakonno-li-e/index.html
DRY-RUN would upload: blog/pragmatic-play-provajdar/index.html
DRY-RUN would upload: blog/progresivni-dzhakpoti/index.html
DRY-RUN would upload: blog/proverka-licenz-kazino/index.html
DRY-RUN would upload: blog/rechnik-kazino-termini/index.html
DRY-RUN would upload: blog/regulations-taxes/index.html
DRY-RUN would upload: blog/responsible-gambling/index.html
DRY-RUN would upload: blog/rotativki-s-plodove/index.html
DRY-RUN would upload: blog/shining-crown/index.html
DRY-RUN would upload: blog/sugar-rush/index.html
DRY-RUN would upload: blog/sweet-bonanza/index.html
DRY-RUN would upload: blog/the-dog-house/index.html
DRY-RUN would upload: bonus-category/welcome-bonus/index.html
DRY-RUN would upload: bonus-ruletka/index.html
DRY-RUN would upload: bonusi/betano-200-bezplatni-zavartania/index.html
DRY-RUN would upload: bonusi/bez-depozit/index.html
DRY-RUN would upload: bonusi/bezplatni-zavartania/index.html
DRY-RUN would upload: bonusi/mrbit-nachalen-bonus/index.html
DRY-RUN would upload: casino/8888/index.html
DRY-RUN would upload: casino/admiralbet/index.html
DRY-RUN would upload: casino/alphawin/index.html
DRY-RUN would upload: casino/bet365/index.html
DRY-RUN would upload: casino/betano/index.html
DRY-RUN would upload: casino/elitbet/index.html
DRY-RUN would upload: casino/everbet/index.html
DRY-RUN would upload: casino/inbet/index.html
DRY-RUN would upload: casino/livescorebet/index.html
DRY-RUN would upload: casino/magicbet/index.html
DRY-RUN would upload: casino/mrbit/index.html
DRY-RUN would upload: casino/nv-casino/index.html
DRY-RUN would upload: casino/palmsbet/index.html
DRY-RUN would upload: casino/sesame/index.html
DRY-RUN would upload: casino/slotino/index.html
DRY-RUN would upload: casino/winbet/index.html
DRY-RUN would upload: depoziti-i-teglenia/index.html
DRY-RUN would upload: faq/index.html
DRY-RUN would upload: go/8888-kazino/index.html
DRY-RUN would upload: go/8888-sport/index.html
DRY-RUN would upload: go/betano-200fs/index.html
DRY-RUN would upload: go/betano-multi/index.html
DRY-RUN would upload: go/betano-sport/index.html
DRY-RUN would upload: go/elitbet-100fs/index.html
DRY-RUN would upload: go/elitbet-kazino/index.html
DRY-RUN would upload: go/elitbet-sport/index.html
DRY-RUN would upload: go/palmsbet-kazino/index.html
DRY-RUN would upload: go/palmsbet-sport/index.html
DRY-RUN would upload: index.html
DRY-RUN would upload: kak-ocenyavame/index.html
DRY-RUN would upload: kazino-igri/blakdzhak/index.html
DRY-RUN would upload: kazino-igri/index.html
DRY-RUN would upload: kazino-igri/kazino-na-zhivo/index.html
DRY-RUN would upload: kazino-igri/rotativki/index.html
DRY-RUN would upload: kazino-igri/ruletka/index.html
DRY-RUN would upload: kazino-nisak-depozit/index.html
DRY-RUN would upload: kontakti/index.html
DRY-RUN would upload: mobilni-kazina/index.html
DRY-RUN would upload: novi-kazina/index.html
DRY-RUN would upload: obshti-usloviya/index.html
DRY-RUN would upload: otgovorna-igra/index.html
DRY-RUN would upload: politika-za-poveritelnost/index.html
DRY-RUN would upload: sitemap.xml
DRY-RUN would upload: slot-igri/index.html
DRY-RUN would upload: slot-igri/novi/index.html
DRY-RUN would upload: slot-igri/visok-rtp/index.html
DRY-RUN would upload: sravni-kazina/index.html
DRY-RUN would upload: za-nas/index.html
DRY-RUN would upload: zakonno-li-e/index.html
DRY-RUN would upload: zhalbi/index.html
```

---

## Deploy error output

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
TimeoutError: [Errno 110] Connection timed out
```

**Root cause:** The remote execution environment's network policy does not permit direct outbound FTP (port 21) connections. The HTTPS proxy is configured but FTP traffic is blocked/timed-out. All pre-flight checks and the dry-run passed — the 104-file upload plan is valid and ready to execute. The deploy needs to be re-run from an environment with unrestricted outbound FTP access (e.g., a local machine or a runner with the FTP_HOST whitelisted).
