$bytes = [System.IO.File]::ReadAllBytes("C:\Users\Administrator\latest.tar.gz")[0..20]
$bytes | ForEach-Object { Write-Host -NoNewline ("{0:X2} " -f $_) }
Write-Host
if ($bytes[0] -eq 0x1f -and $bytes[1] -eq 0x8b) {
    Write-Host "GZIP format detected"
} elseif ($bytes[0] -eq 0x50 -and $bytes[1] -eq 0x4B) {
    Write-Host "ZIP format detected"
} else {
    Write-Host "Unknown format"
}