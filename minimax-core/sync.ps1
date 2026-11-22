param(
    [string]$Source = "$env:USERPROFILE\.minimax",
    [string]$Repo   = "D:\gh_sync_work",
    [string]$AssetRoot = "$env:USERPROFILE\Desktop\豆包核心资产_20261122",
    [switch]$NoPush
)

$ErrorActionPreference = "Stop"
$Core = Join-Path $Repo "minimax-core\core"

function Write-Log($m) { Write-Host ("[{0}] {1}" -f (Get-Date -Format "HH:mm:ss"), $m) }

function Copy-Safe($srcRel, $dstRel) {
    $s = Join-Path $Source $srcRel
    $d = Join-Path $Core   $dstRel
    if (-not (Test-Path $s)) { Write-Log "skip missing: $srcRel"; return }
    $null = robocopy $s $d /E /R:1 /W:1 /NFL /NDL /NJH /NJS /NP /XF *.png *.jpg *.jpeg *.webp *.zip *.exe *.dll
    if ($LASTEXITCODE -ge 8) { throw "robocopy failed on $srcRel (code $LASTEXITCODE)" }
    Write-Log "copied: $srcRel -> $dstRel"
}

function Sanitize-Secrets([string]$t) {
    $t = [regex]::Replace($t, '(?<![A-Za-z0-9_\-])sk-[A-Za-z0-9_\-]{16,}', '<REDACTED:API_KEY>')
    $t = [regex]::Replace($t, '(?<![A-Za-z0-9_])ghp_[A-Za-z0-9]{20,}', '<REDACTED:GITHUB_TOKEN>')
    $t = [regex]::Replace($t, 'AKIA[0-9A-Z]{16}', '<REDACTED:AWS_KEY>')
    $t = [regex]::Replace($t, '(?i)(bearer\s+)([A-Za-z0-9_\-\.]{20,})', '${1}<REDACTED:BEARER_TOKEN>')
    $t = [regex]::Replace($t, '(?i)(appSecret\s*[":=]\s*)("[^"<>]{8,}"|[^"<\s,]{8,})', '${1}"<REDACTED:APP_SECRET>"')
    $t = [regex]::Replace($t, '(?i)(accessToken\s*[":=]\s*)("[^"<>]{8,}"|[^"<\s,]{8,})', '${1}"<REDACTED:ACCESS_TOKEN>"')
    $t = [regex]::Replace($t, '(?i)(botToken\s*:\s*)(\S+)', '${1}"<REDACTED:WECHAT_BOT_TOKEN>"')
    $t = [regex]::Replace($t, '(?i)(qrcodeToken\s*:\s*)(\S+)', '${1}"<REDACTED:WECHAT_QRCODE_TOKEN>"')
    return $t
}

function Sanitize-Config([string]$t) {
    $t = Sanitize-Secrets $t
    $t = [regex]::Replace($t, '(?i)(sessionId\s*[":=]\s*)([^",\r\n]{6,})', '${1}"<REDACTED:SESSION_ID>"')
    $t = [regex]::Replace($t, '(?i)(apiKey\s*[":=]\s*)("[^"<>]{8,}"|[^"<\s,]{8,})', '${1}"<REDACTED:API_KEY>"')
    return $t
}

Write-Log "=== sync start ==="

# 1) core data (whitelisted only)
Copy-Safe "memory"          "memory"
Copy-Safe "skills"          "skills"
Copy-Safe "workspace"       "workspace"
Copy-Safe ".builtin-skills" "builtin-skills"

# 2) agents: text assets only, exclude memory/archive heavy snapshots
$agentMap = @("mavis", "worker", "explore", "verifier", "builtin")
foreach ($a in $agentMap) {
    $s = Join-Path $Source "agents\$a"
    $d = Join-Path $Core   "agents\$a"
    if (-not (Test-Path $s)) { continue }
    $excl = Join-Path $s "memory\archive"
    $null = robocopy $s $d /E /R:1 /W:1 /NFL /NDL /NJH /NJS /NP /XF *.png *.jpg *.jpeg *.webp *.log /XD $excl "$($s)sessions" "$($s)tmp" "$($s)cache"
    Write-Log "copied: agents\$a"
}
Copy-Item (Join-Path $Source "agents\mavis\memory\MEMORY.md") (Join-Path $Core "agents\mavis\memory\MEMORY.md") -Force -ErrorAction SilentlyContinue
Write-Log "copied: agents\mavis\memory\MEMORY.md (latest only)"

# 2.7) rules and prompts: the single source of truth the agent obeys.
# Only current versions and text assets; history archives and credentials stay out.
$assetMap = @(
    @{ src = "00_清单与校验";        dst = "rules\00_清单与校验" },
    @{ src = "01_宪法与规则\现行";   dst = "rules\01_宪法与规则\现行" },
    @{ src = "02_定时任务";          dst = "rules\02_定时任务" },
    @{ src = "04_提示词";            dst = "rules\04_提示词" },
    @{ src = "05_记忆与偏好";        dst = "rules\05_记忆与偏好" }
)
foreach ($a in $assetMap) {
    $s = Join-Path $AssetRoot $a.src
    $d = Join-Path $Core     $a.dst
    if (-not (Test-Path $s)) { Write-Log ("skip missing asset: " + $a.src); continue }
    $null = robocopy $s $d /E /R:1 /W:1 /NFL /NDL /NJH /NJS /NP
    if ($LASTEXITCODE -ge 8) { throw ("robocopy failed on " + $a.src) }
    Write-Log ("copied asset: " + $a.src + " -> core\" + $a.dst)
}

# 3) config: sanitize then write
$cfgDir = Join-Path $Core "config"
New-Item -ItemType Directory -Path $cfgDir -Force | Out-Null
$cfgList = @(
    "config.yaml",
    "permission.json",
    "access-control.yaml",
    "channel-bindings.yaml",
    "channel-routes.yaml",
    "wechat-channel.yaml",
    "mcp.json",
    "mcp-runtime-names.json"
)
foreach ($f in $cfgList) {
    $p = Join-Path $Source $f
    if (-not (Test-Path $p)) { continue }
    $raw = Get-Content $p -Raw -Encoding UTF8
    $out = Sanitize-Config $raw
    $dst = Join-Path $cfgDir $f
    [System.IO.File]::WriteAllText($dst, $out, (New-Object System.Text.UTF8Encoding($false)))
    Write-Log "sanitized: $f"
}

# 3.5) defense in depth: scrub secrets from every text asset under core
# Memory files can also contain pasted API keys; they never reach the remote.
$textExt = @(".md", ".txt", ".json", ".yaml", ".yml", ".py", ".ps1", ".js", ".csv")
$scrubbed = 0
Get-ChildItem $Core -Recurse -File -Force -ErrorAction SilentlyContinue |
    Where-Object { $textExt -contains $_.Extension.ToLower() -and $_.Length -lt 5MB } |
    ForEach-Object {
        $raw = Get-Content $_.FullName -Raw -Encoding UTF8 -ErrorAction SilentlyContinue
        if (-not $raw) { return }
        $out = Sanitize-Secrets $raw
        if ($out -ne $raw) {
            [System.IO.File]::WriteAllText($_.FullName, $out, (New-Object System.Text.UTF8Encoding($false)))
            $scrubbed++
            Write-Log ("scrubbed secret: " + $_.FullName.Replace($Core, "core"))
        }
    }
Write-Log ("backfill scrub: $scrubbed files changed")

# 4) never-copy list report (so user knows what stayed out)
$never = @(
    "mx_accounts.json", "local-runtime.auth.json", "codex-auth.json",
    "keys_new_20261026.txt", "keys_backup_20261025\", "auth\", "sessions\", "v2\",
    "tools\", "computer-use\", "background-tasks\", "cache\",
    "豆包核心资产\06_凭据与账号\ (credentials, never uploaded)",
    "豆包核心资产\03_脚本与引擎\ (61MB, belongs in a separate repo)",
    "豆包核心资产\08_技能与经验\ (overlaps .minimax\skills, kept local)",
    "01_宪法与规则\历史留档\ (superseded drafts)"
)
Set-Content -Path (Join-Path $Core "EXCLUDED.txt") -Value ($never -join "`n") -Encoding UTF8

# 5) manifest + verification gate (blocking)
$genScript = Join-Path $Repo "minimax-core\generate-manifest.ps1"
if (Test-Path $genScript) {
    & powershell -NoProfile -ExecutionPolicy Bypass -File $genScript -Root (Join-Path $Repo "minimax-core")
    if ($LASTEXITCODE -ne 0) { throw "manifest generation failed" }
}
$verifyScript = Join-Path $Repo "minimax-core\verify.ps1"
if (Test-Path $verifyScript) {
    & powershell -NoProfile -ExecutionPolicy Bypass -File $verifyScript -Root (Join-Path $Repo "minimax-core") -Quiet
    if ($LASTEXITCODE -ne 0) { throw "verification gate failed: fix FAIL items before committing" }
    Write-Log "verify gate passed"
}

# 6) git
Push-Location $Repo
try {
    if (-not (Test-Path (Join-Path $Repo ".git"))) { throw "repo not initialized: run setup first" }
    git add minimax-core
    $msg = "sync " + (Get-Date -Format "yyyy-MM-dd HH:mm")
    git diff --cached --quiet
    if ($LASTEXITCODE -eq 0) {
        Write-Log "no changes to commit"
    } else {
        git commit -m $msg | Out-Null
        Write-Log "committed: $msg"
    }
    if (-not $NoPush) {
        git push origin HEAD
        if ($LASTEXITCODE -ne 0) { throw "git push failed" }
        Write-Log "pushed to origin"
    }
} finally {
    Pop-Location
}

$stat = Get-ChildItem $Core -Recurse -File -Force | Measure-Object Length -Sum
Write-Log ("=== done: files={0} size={1}MB ===" -f (Get-ChildItem $Core -Recurse -File -Force | Measure-Object).Count, [math]::Round($stat.Sum / 1MB, 2))
