@echo off
chcp 65001 >nul
echo [%date% %time%] 财经快报任务开始 >> "%~dp0cron.log"

cd /d "%USERPROFILE%\.openclaw-autoclaw\workspace"

REM 获取当前时间
for /f "tokens=1-2 delims=:" %%a in ("%time%") do (
    set hour=%%a
    set minute=%%b
)

REM 去除前导零
set hour=%hour: =0%
set minute=%minute:~0,2%

echo 当前时间: %hour%:%minute%

REM 根据时间执行不同任务
if "%hour%"=="09" (
    echo 执行早盘快报...
    python finance_news_fetcher_v2.py
    python finance_report.py 早盘
    echo 早盘任务完成 >> "%~dp0cron.log"
)

if "%hour%"=="12" (
    echo 执行午间快报...
    python finance_news_fetcher_v2.py
    python finance_report.py 午间
    echo 午间任务完成 >> "%~dp0cron.log"
)

if "%hour%"=="15" (
    echo 执行收盘快报...
    python finance_news_fetcher_v2.py
    python finance_report.py 收盘
    echo 收盘任务完成 >> "%~dp0cron.log"
)

if "%hour%"=="18" (
    echo 执行晚间快报...
    python finance_news_fetcher_v2.py
    python finance_report.py 晚间
    echo 晚间任务完成 >> "%~dp0cron.log"
)

if "%hour%"=="21" (
    echo 执行夜盘快报...
    python finance_news_fetcher_v2.py
    python finance_report.py 夜盘
    echo 夜盘任务完成 >> "%~dp0cron.log"
)

echo [%date% %time%] 任务结束 >> "%~dp0cron.log"
echo.
