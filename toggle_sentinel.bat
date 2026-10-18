@echo off
:: PC Sentinel V4.0 Fortress Edition — Quick Toggle Script
title PC Sentinel V4.0 — Master Protection Toggle
cd /d "%~dp0"
color 0B

net session >nul 2>&1
if %errorlevel% neq 0 (
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

:MENU
cls
echo.
echo  =======================================================
echo   PC SENTINEL V4.0 — MASTER PROTECTION & HARDENING
echo  =======================================================
echo.
echo  [1] Enable Sentinel (Full Protection ON)
echo  [2] Disable Sentinel (Protection OFF)
echo  [3] Enable Windows Startup Boot (Auto-Start)
echo  [4] Disable Windows Startup Boot
echo  [5] Audit Windows 10 EOL Exploit Armor Posture
echo  [6] Apply Full Fortress Hardening (LSA + SMBv1 + Ports)
echo  [7] Exit
echo.
set /p choice="  Enter choice [1-7]: "

if "%choice%"=="1" (
    python -c "import json; c=json.load(open('config.json')); c['enabled']=True; c['realtime_protection']=True; json.dump(c,open('config.json','w'),indent=2); print('[OK] Master Protection ENABLED.')"
    echo  Protection is now ACTIVE.
    pause
    goto MENU
)
if "%choice%"=="2" (
    python -c "import json; c=json.load(open('config.json')); c['enabled']=False; c['realtime_protection']=False; json.dump(c,open('config.json','w'),indent=2); print('[OK] Master Protection DISABLED.')"
    echo  WARNING: System protection is currently OFF!
    pause
    goto MENU
)
if "%choice%"=="3" (
    python -c "import sentinel; sentinel.SentinelScheduler.register_windows_startup(); print('[OK] Startup registered.')"
    echo  Sentinel will start automatically with Windows.
    pause
    goto MENU
)
if "%choice%"=="4" (
    python -c "import sentinel; sentinel.SentinelScheduler.unregister_windows_startup(); print('[OK] Startup removed.')"
    echo  Sentinel will NOT start with Windows.
    pause
    goto MENU
)
if "%choice%"=="5" (
    echo.
    python sentinel_cli.py --audit-fortress
    pause
    goto MENU
)
if "%choice%"=="6" (
    echo.
    python sentinel_cli.py --harden-fortress
    pause
    goto MENU
)
if "%choice%"=="7" (
    exit /b
)

goto MENU
