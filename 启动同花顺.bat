@echo off
chcp 65001 >nul
echo ========================================
echo 正在启动同花顺...
echo ========================================

REM 尝试多个可能的路径
if exist "C:\new_tdx\同花顺.exe" (
    echo 找到: C:\new_tdx\同花顺.exe
    start "" "C:\new_tdx\同花顺.exe"
    goto :success
)

if exist "D:\new_tdx\同花顺.exe" (
    echo 找到: D:\new_tdx\同花顺.exe
    start "" "D:\new_tdx\同花顺.exe"
    goto :success
)

if exist "C:\Program Files\同花顺\同花顺.exe" (
    echo 找到: C:\Program Files\同花顺\同花顺.exe
    start "" "C:\Program Files\同花顺\同花顺.exe"
    goto :success
)

if exist "D:\Program Files\同花顺\同花顺.exe" (
    echo 找到: D:\Program Files\同花顺\同花顺.exe
    start "" "D:\Program Files\同花顺\同花顺.exe"
    goto :success
)

echo ========================================
echo 未找到同花顺.exe！
echo ========================================
echo.
echo 请手动启动同花顺，然后在软件中：
echo 1. 按F6打开自选股
echo 2. 查看已添加的3只股票：
echo    - 000890 法尔胜
echo    - 000596 古井贡酒
echo    - 002384 东山精密
echo.
pause
goto :end

:success
echo.
echo ========================================
echo 同花顺已启动！
echo ========================================
echo.
echo 请按F6查看自选股，已添加：
echo    - 000890 法尔胜
echo    - 000596 古井贡酒
echo    - 002384 东山精密
echo.
timeout /t 3 >nul
goto :end

:end
