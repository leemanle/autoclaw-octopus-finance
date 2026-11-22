param(
    [string]$Root = "D:\gh_sync_work\minimax-core"
)

$ErrorActionPreference = "Stop"
$verFile = Join-Path $Root "VERSION"
$version = if (Test-Path $verFile) { (Get-Content $verFile -Raw).Trim() } else { "0.0.0" }

$exclude = @("manifest.json")
$files = Get-ChildItem $Root -Recurse -File -Force -ErrorAction SilentlyContinue |
         Where-Object { $exclude -notcontains $_.Name }

$entries = foreach ($f in $files) {
    $rel = $f.FullName.Replace($Root, "").TrimStart("\").Replace("\", "/")
    [pscustomobject]@{
        path   = $rel
        bytes  = $f.Length
        sha256 = (Get-FileHash $f.FullName -Algorithm SHA256).Hash
    }
}

$total = ($files | Measure-Object Length -Sum).Sum

$manifest = [pscustomobject]@{
    version     = $version
    generatedAt = (Get-Date).ToString("yyyy-MM-ddTHH:mm:ssK")
    fileCount   = $files.Count
    totalBytes  = $total
    channel     = "github:leemanle/autoclaw-octopus-finance/minimax-core"
    files       = $entries
}

$json = $manifest | ConvertTo-Json -Depth 4
[System.IO.File]::WriteAllText(
    (Join-Path $Root "manifest.json"),
    $json,
    (New-Object System.Text.UTF8Encoding($false)
))

Write-Host ("manifest: version={0} files={1} total={2}MB" -f $version, $files.Count, [math]::Round($total / 1MB, 2))
