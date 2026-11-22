param(
    [string]$Root = "D:\gh_sync_work\minimax-core",
    [switch]$Quiet
)

$ErrorActionPreference = "Stop"
$fail = 0
$warn = 0
$out  = @()

function Emit($level, $msg) {
    $script:out += ("[{0}] {1}" -f $level, $msg)
    if ($level -eq "FAIL") { $script:fail++ }
    if ($level -eq "WARN") { $script:warn++ }
}

# ---- 1. forbidden paths must not exist ----
$forbiddenNames = @(
    "auth", "sessions", "v2", "tools", "computer-use", "background-tasks", "cache",
    "mx_accounts.json", "local-runtime.auth.json", "codex-auth.json"
)
foreach ($n in $forbiddenNames) {
    $p = Join-Path $Root ("core\" + $n)
    if (Test-Path $p) { Emit "FAIL" ("forbidden path present: core/" + $n) }
}
$keys = Get-ChildItem $Root -Recurse -Directory -Force -ErrorAction SilentlyContinue |
        Where-Object { $_.Name -match '^keys_(backup|new)' }
foreach ($k in $keys) { Emit "FAIL" ("forbidden keys dir: " + $k.FullName.Replace($Root, "")) }

# ---- 2. required assets must exist ----
$required = @(
    "README.md", "sync.ps1", "restore.ps1", "verify.ps1", "manifest.json",
    "core\memory\user.md",
    "core\agents\mavis\memory\MEMORY.md",
    "core\skills",
    "core\builtin-skills",
    "core\config\config.yaml"
)
foreach ($r in $required) {
    if (-not (Test-Path (Join-Path $Root $r))) { Emit "FAIL" ("missing required: " + $r) }
}

# ---- 3. file size limits (GitHub hard limit 100MiB, warn 50MiB) ----
$bigFiles = Get-ChildItem $Root -Recurse -File -Force -ErrorAction SilentlyContinue |
            Where-Object { $_.Length -gt 50MB }
foreach ($b in $bigFiles) {
    $mb = [math]::Round($b.Length / 1MB, 1)
    if ($b.Length -gt 100MB) { Emit "FAIL" ("file >100MiB: $($b.Name) $mb MB") }
    else { Emit "WARN" ("file >50MiB: $($b.Name) $mb MB") }
}

# ---- 4. secret scan (anything real, not the REDACTED placeholder) ----
$secretPatterns = @(
    '(?<![A-Za-z0-9_\-])sk-[A-Za-z0-9_\-]{16,}',
    '(?<![A-Za-z0-9_])ghp_[A-Za-z0-9]{20,}',
    'AKIA[0-9A-Z]{16}',
    '(?i)(bearer\s+)([A-Za-z0-9_\-\.]{20,})',
    '(?i)(appSecret|accessToken|botToken|qrcodeToken)\s*[":=]\s*"[^"<]{12,}'
)
$scanned = Get-ChildItem $Root -Recurse -File -Force -ErrorAction SilentlyContinue |
           Where-Object { $_.Length -lt 5MB -and $_.Extension -in '.md','.json','.yaml','.yml','.py','.ps1','.txt','.js','' }
foreach ($f in $scanned) {
    $txt = Get-Content $f.FullName -Raw -Encoding UTF8 -ErrorAction SilentlyContinue
    if (-not $txt) { continue }
    foreach ($pt in $secretPatterns) {
        $m = [regex]::Matches($txt, $pt)
        foreach ($hit in $m) {
            if ($hit.Value -match 'REDACTED') { continue }
            $rel = $f.FullName.Replace($Root, "")
            Emit "FAIL" ("secret-like value in $rel : " + $hit.Value.Substring(0, [Math]::Min(12, $hit.Value.Length)) + "...")
        }
    }
}

# ---- 5. manifest integrity ----
$mfPath = Join-Path $Root "manifest.json"
if (Test-Path $mfPath) {
    $manifest = Get-Content $mfPath -Raw -Encoding UTF8 | ConvertFrom-Json
    $missing = 0; $changed = 0
    foreach ($e in $manifest.files) {
        $fp = Join-Path $Root ($e.path -replace '/', '\')
        if (-not (Test-Path $fp)) { $missing++; continue }
        $h = (Get-FileHash $fp -Algorithm SHA256).Hash
        if ($h -ne $e.sha256) { $changed++ }
    }
    if ($missing -gt 0) { Emit "FAIL" ("manifest: $missing files missing on disk") }
    if ($changed -gt 0) { Emit "WARN" ("manifest: $changed files changed since last snapshot (run sync.ps1)") }
    Emit "INFO" ("manifest version " + $manifest.version + ", files " + $manifest.fileCount)
}

# ---- 6. total size ----
$all = Get-ChildItem $Root -Recurse -File -Force -ErrorAction SilentlyContinue | Measure-Object Length -Sum
$totalMB = [math]::Round($all.Sum / 1MB, 2)
if ($totalMB -gt 900) { Emit "FAIL" ("repo size $totalMB MB exceeds 900MB budget") }
else { Emit "INFO" ("size $totalMB MB, files " + $all.Count) }

# ---- report ----
if (-not $Quiet) { $out | ForEach-Object { Write-Host $_ } }
Write-Host ""
Write-Host ("RESULT: {0} fail, {1} warn" -f $fail, $warn)
if ($fail -gt 0) { exit 1 } else { exit 0 }
