Add-Type -AssemblyName System.Drawing
$bmp = New-Object System.Drawing.Bitmap("C:\Users\Administrator\.openclaw-autoclaw\workspace\temp.png")
Write-Host "Width: $($bmp.Width)"
Write-Host "Height: $($bmp.Height)"
$bmp.Dispose()
