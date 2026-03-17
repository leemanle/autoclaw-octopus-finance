# ===== 龙虾权限破除脚本 =====
# 作用：彻底解除Windows系统权限限制，让龙虾能自动安装软件

Write-Host "🔧 开始配置系统权限，请稍候..." -ForegroundColor Green

# 1. 启用内置Administrator账户
Write-Host "📌 步骤1：启用内置管理员账户" -ForegroundColor Yellow
net user administrator /active:yes

# 2. 关闭UAC
Write-Host "📌 步骤2：彻底关闭UAC" -ForegroundColor Yellow
Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" -Name "EnableLUA" -Value 0
Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" -Name "ConsentPromptBehaviorAdmin" -Value 0
Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" -Name "PromptOnSecureDesktop" -Value 0
Write-Host "✅ UAC已禁用" -ForegroundColor Green

# 3. 关闭管理员批准模式
Write-Host "📌 步骤3：配置组策略安全选项" -ForegroundColor Yellow
Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" -Name "FilterAdministratorToken" -Value 0

# 4. 禁用SmartScreen
Write-Host "📌 步骤4：禁用SmartScreen" -ForegroundColor Yellow
Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer" -Name "SmartScreenEnabled" -Value "Off"

# 5. 为龙虾目录授权
Write-Host "📌 步骤5：为龙虾程序目录赋予完全控制权限" -ForegroundColor Yellow
$currentUser = [System.Security.Principal.WindowsIdentity]::GetCurrent().Name

$lobsterPaths = @(
    "$env:LOCALAPPDATA\Programs\AutoClaw",
    "$env:ProgramFiles\AutoClaw",
    "$env:USERPROFILE\.openclaw"
)

foreach ($path in $lobsterPaths) {
    if (Test-Path $path) {
        takeown /f "$path" /r /d y 2>$null
        icacls "$path" /grant "${currentUser}:F" /t /c 2>$null
        Write-Host "✅ 已授权: $path" -ForegroundColor Green
    }
}

# 6. 禁用Windows Defender实时防护
Write-Host "📌 步骤6：临时禁用Windows Defender实时防护" -ForegroundColor Yellow
try {
    Set-MpPreference -DisableRealtimeMonitoring $true -ErrorAction SilentlyContinue
    Write-Host "✅ Windows Defender已临时禁用" -ForegroundColor Green
} catch {
    Write-Host "⚠️ 无法禁用Windows Defender" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "🎉 权限配置已完成！" -ForegroundColor Green
Write-Host "⚠️ 需要重启电脑使配置生效" -ForegroundColor Yellow

# 询问是否重启
$response = Read-Host "是否立即重启电脑？(y/n)"
if ($response -eq "y") {
    Restart-Computer -Force
}
