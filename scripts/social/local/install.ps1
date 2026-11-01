# Social posts on this computer: installs what is missing, gets the code and starts the setup.
# Run it in PowerShell (the same line again after a restart is safe: every step is skipped once done):
#
#   irm https://raw.githubusercontent.com/ProfitXtraV2/AIContent/main/scripts/social/local/install.ps1 | iex
#
# A test repository: set $env:PX_SOCIAL_REPO = "owner/name" before the line.
$ErrorActionPreference = "Stop"
$Repo = if ($env:PX_SOCIAL_REPO) { $env:PX_SOCIAL_REPO } else { "ProfitXtraV2/AIContent" }
$Home2 = if ($env:PX_SOCIAL_HOME) { $env:PX_SOCIAL_HOME } else { Join-Path $HOME "px-social" }

function Say($text) { Write-Host ""; Write-Host "== $text" -ForegroundColor Cyan }
function Have($cmd) {
  if (-not (Get-Command $cmd -ErrorAction SilentlyContinue)) { return $false }
  if ($cmd -eq "python") {                       # the Microsoft Store shortcut is a python.exe that only opens the Store
    python --version *> $null
    return ($LASTEXITCODE -eq 0)
  }
  return $true
}
function Refresh-Path {
  $env:Path = [Environment]::GetEnvironmentVariable("Path", "Machine") + ";" + [Environment]::GetEnvironmentVariable("Path", "User")
}

Say "Постове в социалните мрежи: инсталация на този компютър"
if (-not (Have "winget")) {
  Write-Host "Липсва winget (App Installer). Инсталирай го от Microsoft Store и пусни реда отново." -ForegroundColor Yellow
  return
}

$tools = @(
  @{ cmd = "git";    id = "Git.Git";                name = "Git" },
  @{ cmd = "python"; id = "Python.Python.3.12";     name = "Python 3.12" },
  @{ cmd = "gh";     id = "GitHub.cli";             name = "GitHub CLI" },
  @{ cmd = "ngrok";  id = "Ngrok.Ngrok";            name = "ngrok" },
  @{ cmd = "docker"; id = "Docker.DockerDesktop";   name = "Docker Desktop" }
)
$installed = @()
foreach ($t in $tools) {
  if (Have $t.cmd) { Write-Host ("  OK " + $t.name); continue }
  Write-Host ("  … инсталирам " + $t.name)
  winget install -e --id $t.id --accept-source-agreements --accept-package-agreements --silent | Out-Null
  $installed += $t.name
}
Refresh-Path

if ($installed -contains "Docker Desktop" -or -not (Have "docker")) {
  Write-Host ""
  Write-Host "Docker Desktop е инсталиран. Рестартирай компютъра, пусни Docker Desktop веднъж (приеми условията)" -ForegroundColor Yellow
  Write-Host "и после пусни същия ред отново." -ForegroundColor Yellow
  return
}
docker info *> $null
if ($LASTEXITCODE -ne 0) {
  Write-Host "Docker Desktop не е пуснат. Пусни го (иконата с китчето), изчакай да пише „Engine running“ и пусни реда отново." -ForegroundColor Yellow
  return
}

Say "GitHub"
gh auth status *> $null
if ($LASTEXITCODE -ne 0) {
  Write-Host "Ще се отвори браузърът: влез в GitHub и потвърди кода, който виждаш тук."
  gh auth login --web -h github.com -p https
}

Say "Кодът"
$Code = Join-Path $Home2 "code"
New-Item -ItemType Directory -Force $Home2 | Out-Null
if (-not (Test-Path (Join-Path $Code ".git"))) {
  gh repo clone $Repo $Code -- --depth 1 -c core.autocrlf=false -c core.eol=lf
} else {
  git -C $Code fetch -q origin main; git -C $Code reset -q --hard origin/main
}

Say "Настройка"
$env:PX_SOCIAL_REPO = $Repo
$env:PX_SOCIAL_HOME = $Home2
python (Join-Path $Code "scripts\social\local\setup.py")
