# 更新选股定时任务使用正确Python路径
$python = "C:\Users\Administrator\AppData\Local\Programs\Python\Python312\python.exe"
$script = "C:\Users\Administrator\.openclaw-autoclaw\workspace\scripts\stock_picker.py"

# 盘中每30分钟 (9:30-14:30)
$times = @('09:30','10:00','10:30','11:00','11:30','12:00','12:30','13:00','13:30','14:00','14:30')
foreach ($t in $times) {
    $name = "StockPicker_$($t.Replace(':','_'))"
    $trigger = New-ScheduledTaskTrigger -Daily -At $t
    $action = New-ScheduledTaskAction -Execute $python -Argument $script
    Set-ScheduledTask -TaskName $name -Trigger $trigger -Action $action | Out-Null
    Write-Host "Updated: $name"
}

# 收盘后 15:05
$trigger = New-ScheduledTaskTrigger -Daily -At '15:05'
$action = New-ScheduledTaskAction -Execute $python -Argument $script
Set-ScheduledTask -TaskName 'StockPicker_AfterClose' -Trigger $trigger -Action $action | Out-Null
Write-Host "Updated: StockPicker_AfterClose"

Get-ScheduledTask | Where-Object { $_.TaskName -like 'StockPicker*' } | Select-Object TaskName, State