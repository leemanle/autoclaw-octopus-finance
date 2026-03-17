# 新技能自动打包脚本
# 检查并打包新增技能到桌面

$src = "C:\Users\Administrator\.agents\skills"
$dst = "C:\Users\Administrator\Desktop\新增技能包"
$old = @("backtest-expert-0.1.0","eastmoney-financial-data","finance-news-monitor-1.0.0","aminer-open-academic-1.0.5")

# 获取当前所有技能
$all = Get-ChildItem $src -Directory | Select-Object -ExpandProperty Name

# 找出新增技能
$new = $all | Where-Object { $old -notcontains $_ }

if ($new.Count -eq 0) {
    Write-Host "没有新技能"
    exit 0
}

Write-Host "发现 $($new.Count) 个新技能: $($new -join ', ')"

# 创建目标目录
if (-not (Test-Path $dst)) {
    New-Item -ItemType Directory -Path $dst -Force | Out-Null
}

# 复制每个新技能
foreach ($skill in $new) {
    $srcPath = Join-Path $src $skill
    $dstPath = Join-Path $dst $skill
    if (Test-Path $srcPath) {
        Copy-Item -Path $srcPath -Destination $dstPath -Recurse -Force
        Write-Host "已复制: $skill"
    }
}

Write-Host "打包完成!"

# 更新旧技能列表
$oldFile = "C:\Users\Administrator\.openclaw-autoclaw\workspace\last_skill_backup.txt"
$newList = ($all | Out-String).Trim()
Set-Content -Path $oldFile -Value $newList
Write-Host "技能列表已更新"