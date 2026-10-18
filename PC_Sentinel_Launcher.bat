@echo off
:: ==============================================================================
:: PC SENTINEL V3.5 — ULTRA ENTERPRISE EDR DEFENDER MASTER LAUNCHER
:: Next-Gen Multi-Layer AI Heuristics, USB Shield, Battery Eco & Auto-RAM Suite
:: ==============================================================================
title PC Sentinel V3.5 — Master Security Console
color 0B
setlocal enabledelayedexpansion

:: Force Admin Elevation
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo  ====================================================================
    echo   [!] REQUESTING ELEVATED ADMINISTRATOR PRIVILEGES...
    echo   PC Sentinel requires Admin rights for Kernel ^& Process Shielding.
    echo  ====================================================================
    echo.
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

cd /d "%~dp0"

:MENU
cls
color 0B
echo.
echo  ====================================================================
echo  ======= PC SENTINEL V4.0 — ULTRA ENTERPRISE FORTRESS EDR DEFENDER =======
echo  ====================================================================
echo    [Status: ACTIVE ZERO-DAY SHIELD]       [Mode: ELEVATED ADMIN]
echo    [Architecture: MULTI-THREADED AI]      [Protection: REAL-TIME]
echo    [EOL Exploit Armor: INTEGRATED]        [Battery Eco Guard: ACTIVE]
echo  ====================================================================
echo.
echo    [1]  Launch PC Sentinel V4.0 Cyberpunk GUI Dashboard
echo    [2]  Execute Autonomous Cyber Defense Self-Test (Scorecard 0-100%%)
echo    [3]  Start Silent Background Guardian Daemon (Elevated Windowless)
echo    [4]  Run Quick Turbo Threat Scan
echo    [5]  Run Deep Zero-Day Full System Scan (PE + Macros + Heuristics)
echo    [6]  Audit Running Processes for System Binary Masquerading
echo    [7]  Inspect Active Sockets, High-Risk C2 Ports ^& Network Traffic
echo    [8]  Boost ^& Purge System RAM Memory Working Sets
echo    [9]  Activate Smart Battery Eco Turbo Saver (Throttle Idle Wasters)
echo   [10]  View Live Battery Telemetry ^& Power Wasters
echo   [11]  Vaccinate ^& Immunize All USB Flash Drives
echo   [12]  Audit Windows Persistence ^& Rootkit Startup Integrity
echo   [13]  Deploy / Verify Anti-Ransomware Canary Honeypots
echo   [14]  Run System Junk Shredder ^& Temp Purge
echo   [15]  Open Isolated Threat Quarantine Vault
echo   [16]  Audit Windows 10 EOL Exploit Armor ^& Hardening Posture
echo   [17]  Activate Full Fortress Hardening (LSA + SMBv1 + LLMNR + Ports)
echo   [18]  Exit Console
echo.
echo  ====================================================================
set /p choice="  Enter choice [1-18]: "

if "%choice%"=="1" (
    echo.
    echo  [+] Launching PC Sentinel V4.0 GUI Dashboard...
    start "" python sentinel.py
    timeout /t 2 >nul
    goto MENU
)

if "%choice%"=="2" (
    echo.
    python sentinel_cli.py --self-test
    echo.
    pause
    goto MENU
)

if "%choice%"=="3" (
    echo.
    echo  [+] Starting Silent Background Protection...
    start /min pythonw sentinel.py --minimized
    echo  [OK] PC Sentinel V3.5 is running in the background.
    pause
    goto MENU
)

if "%choice%"=="4" (
    echo.
    echo  [+] Initiating Quick Turbo Threat Scan...
    python sentinel_cli.py --scan
    echo.
    pause
    goto MENU
)

if "%choice%"=="5" (
    echo.
    echo  [+] Initiating Deep Zero-Day Full System Scan...
    python sentinel_cli.py --deep
    echo.
    pause
    goto MENU
)

if "%choice%"=="6" (
    echo.
    python sentinel_cli.py --audit-masquerade
    echo.
    pause
    goto MENU
)

if "%choice%"=="7" (
    echo.
    python sentinel_cli.py --audit-network
    echo.
    pause
    goto MENU
)

if "%choice%"=="8" (
    echo.
    echo  [+] Purging RAM Working Sets ^& Relieving System Load...
    python sentinel_cli.py --ram-boost
    echo.
    pause
    goto MENU
)

if "%choice%"=="9" (
    echo.
    echo  [+] Activating Smart Battery Eco Turbo Saver...
    python sentinel_cli.py --battery-eco
    echo.
    pause
    goto MENU
)

if "%choice%"=="10" (
    echo.
    echo  [+] Inspecting Live Battery ^& Power Telemetry...
    python sentinel_cli.py --battery-status
    echo.
    pause
    goto MENU
)

if "%choice%"=="11" (
    echo.
    echo  [+] Running USB Sentinel Auto-Vaccine...
    python sentinel_cli.py --vaccine
    echo.
    pause
    goto MENU
)

if "%choice%"=="12" (
    echo.
    echo  [+] Auditing Windows Persistence ^& Rootkits...
    python sentinel_cli.py --audit-rootkit
    echo.
    pause
    goto MENU
)

if "%choice%"=="13" (
    echo.
    echo  [+] Deploying Anti-Ransomware Honeypot Canaries...
    python -c "import sentinel; c=sentinel.ConfigManager(); db=sentinel.ThreatDB(); e=sentinel.AntivirusEngine(c,db); cs=sentinel.AntiRansomwareCanaryShield(c,e); print('[OK] Canary Honey-pot active.')"
    echo.
    pause
    goto MENU
)

if "%choice%"=="14" (
    echo.
    echo  [+] Running System Junk Shredder...
    python sentinel_cli.py --clean-junk
    echo.
    pause
    goto MENU
)

if "%choice%"=="15" (
    echo.
    echo  [+] Opening Quarantine Vault...
    start "" "%~dp0quarantine"
    goto MENU
)

if "%choice%"=="16" (
    echo.
    python sentinel_cli.py --audit-fortress
    echo.
    pause
    goto MENU
)

if "%choice%"=="17" (
    echo.
    python sentinel_cli.py --harden-fortress
    echo.
    pause
    goto MENU
)

if "%choice%"=="18" (
    exit /b
)

goto MENU
