@echo off
:: PC Sentinel V4.0 Fortress Edition — Elevated Silent Background Launcher
cd /d "%~dp0"

net session >nul 2>&1
if %errorlevel% neq 0 (
    powershell -Command "Start-Process pythonw -ArgumentList 'sentinel.py --minimized' -Verb RunAs -WindowStyle Hidden"
    exit /b
)

start /min pythonw sentinel.py --minimized
