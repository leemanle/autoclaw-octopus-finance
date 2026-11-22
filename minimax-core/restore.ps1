param(
    [string]$Repo   = "D:\agent-core-sync",
    [string]$Target = "$env:USERPROFILE\.minimax",
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"
$Core = Join-Path $Repo "core"

function Write-Log($m) { Write-Host ("[{0}] {1}" -f (Get-Date -Format "HH:mm:ss"), $m) }

if (-not (Test-Path $Core)) { throw "core dir not found in $Repo" }

$stamp = Get-Date -Format "yyyyMMdd_HHmmss"
$bak   = Join-Path $env:USERPROFILE (".minimax_backup_" + $stamp)

Write-Log "=== restore start ==="
Write-Log "source: $Core"
Write-Log "target: $Target"

if ($DryRun) {
    Write-Log "DRY RUN: planned mapping"
    Get-ChildItem $Core -Directory | ForEach-Object { Write-Log ("  {0} -> {1}" -f $_.Name, (Join-Path $Target $_.Name)) }
    Write-Log "config/* -> per-file copy into $Target (manual review required)"
    return
}

# 1) snapshot current state before overwrite
foreach ($d in @("memory", "skills", "workspace")) {
    $cur = Join-Path $Target $d
    if (Test-Path $cur) {
        New-Item -ItemType Directory -Path $bak -Force | Out-Null
        $null = robocopy $cur (Join-Path $bak $d) /E /R:1 /W:1 /NFL /NDL /NJH /NJS /NP
        Write-Log "backed up existing: $d"
    }
}

# 2) restore core dirs
foreach ($d in @("memory", "skills", "workspace")) {
    $s = Join-Path $Core $d
    if (-not (Test-Path $s)) { continue }
    $null = robocopy $s (Join-Path $Target $d) /E /R:1 /W:1 /NFL /NDL /NJH /NJS /NP
    Write-Log "restored: $d"
}

# 3) builtin skills -> .builtin-skills
$bs = Join-Path $Core "builtin-skills"
if (Test-Path $bs) {
    $null = robocopy $bs (Join-Path $Target ".builtin-skills") /E /R:1 /W:1 /NFL /NDL /NJH /NJS /NP
    Write-Log "restored: .builtin-skills"
}

# 4) agents
$ag = Join-Path $Core "agents"
if (Test-Path $ag) {
    Get-ChildItem $ag -Directory | ForEach-Object {
        $dst = Join-Path (Join-Path $Target "agents") $_.Name
        $null = robocopy $_.FullName $dst /E /R:1 /W:1 /NFL /NDL /NJH /NJS /NP
        Write-Log ("restored: agents\" + $_.Name)
    }
    # restore latest MEMORY.md over archive default
    $mem = Join-Path $ag "mavis\memory\MEMORY.md"
    if (Test-Path $mem) {
        $dstMem = Join-Path $Target "agents\mavis\memory"
        New-Item -ItemType Directory -Path $dstMem -Force | Out-Null
        Copy-Item $mem (Join-Path $dstMem "MEMORY.md") -Force
        Write-Log "restored: agents\mavis\memory\MEMORY.md"
    }
}

# 5) config: copy sanitized versions aside, never silently overwrite live creds
$cfgSrc = Join-Path $Core "config"
if (Test-Path $cfgSrc) {
    $cfgOut = Join-Path $Target "_restored_config"
    New-Item -ItemType Directory -Path $cfgOut -Force | Out-Null
    Get-ChildItem $cfgSrc -File | ForEach-Object {
        Copy-Item $_.FullName (Join-Path $cfgOut $_.Name) -Force
        Write-Log ("staged for manual merge: config\" + $_.Name)
    }
}

Write-Log ""
Write-Log "=== MANUAL STEPS REQUIRED ==="
Write-Log "1. Fill real secrets inside $cfgOut (values marked <REDACTED:...>)"
Write-Log "2. Merge them into $Target (do NOT overwrite auth/ or keys_* dirs)"
Write-Log "3. Old state backup: $bak"
Write-Log "=== restore finished ==="
