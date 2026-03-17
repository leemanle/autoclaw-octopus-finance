# 创建盘中选股定时任务
$times = @('09:30','10:00','10:30','11:00','11:30','12:00','12:30','13:00','13:30','14:00','14:30')
foreach ($t in $times) {
    $name = "StockPicker_$($t.Replace(':','_'))"
    $trigger = New-ScheduledTaskTrigger -Daily -At $t
    $action = New-ScheduledTaskAction -Execute 'python.exe' -Argument 'C:\Users\Administrator\.openclaw-autoclaw\workspace\scripts\stock_picker.py'
    Register-ScheduledTask -TaskName $name -Trigger $trigger -Action $action -Description "A股盘中选股 $t" -Force
    Write-Host "Created: $name at $t"
}

# 收盘后 15:05
$trigger = New-ScheduledTaskTrigger -Daily -At '15:05'
$action = New-ScheduledTaskAction -Execute 'python.exe' -Argument 'C:\Users\Administrator\.openclaw-autoclaw\workspace\scripts\stock_picker.py'
Register-ScheduledTask -TaskName 'StockPicker_AfterClose' -Trigger $trigger -Action $action -Description '收盘后选股' -Force
Write-Host 'Created: StockPicker_AfterClose at 15:05'

# 列出所有选股任务
Get-ScheduledTask | Where-Object { $_.TaskName -like 'StockPicker*' } | Select-Object TaskName, State