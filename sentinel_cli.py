"""
PC SENTINEL V3.5 — ULTRA ENTERPRISE EDR CLI
Command-line interface for headless execution, automated security self-tests, and threat auditing.
"""

import sys
import os
import argparse
import time
from pathlib import Path

# Safe Windows CLI Unicode handling
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import sentinel

def print_banner():
    print("""
 ===========================================================================
        [+] PC SENTINEL V3.5 — ULTRA ENTERPRISE EDR DEFENDER CLI
            Next-Gen Zero-Day Shield & Autonomous Cyber Defense
 ===========================================================================
""")

def main():
    parser = argparse.ArgumentParser(description="PC Sentinel V3.5 Ultra Enterprise EDR CLI")
    parser.add_argument("--scan", action="store_true", help="Run Quick Threat Scan")
    parser.add_argument("--deep", action="store_true", help="Run Deep Zero-Day Full Scan")
    parser.add_argument("--path", type=str, help="Scan a specific custom directory or file")
    parser.add_argument("--self-test", action="store_true", help="Execute 100%% Safe Defense Simulation & Compute Readiness Score")
    parser.add_argument("--audit-masquerade", action="store_true", help="Audit active processes for system binary masquerading")
    parser.add_argument("--audit-network", action="store_true", help="Inspect all live sockets for C2 high-risk ports & DGA connections")
    parser.add_argument("--vaccine", action="store_true", help="Vaccinate and clean all connected USB flash drives")
    parser.add_argument("--ram-boost", action="store_true", help="Purge RAM Working Sets and optimize system memory")
    parser.add_argument("--battery-eco", action="store_true", help="Engage Eco Turbo Saver and throttle background power wasters")
    parser.add_argument("--battery-status", action="store_true", help="Show live battery telemetry and idle wasters")
    parser.add_argument("--clean-junk", action="store_true", help="Clean temp files and system junk")
    parser.add_argument("--audit-rootkit", action="store_true", help="Audit Windows persistence, Run keys and Scheduled Tasks")
    parser.add_argument("--quarantine-list", action="store_true", help="List all quarantined threats")
    parser.add_argument("--audit-fortress", action="store_true", help="Audit Windows 10 EOL Exploit Armor & Hardening Posture")
    parser.add_argument("--harden-fortress", action="store_true", help="Engage Full Fortress Hardening (LSA, SMBv1, LLMNR, WPAD, Ports)")

    args = parser.parse_args()

    config = sentinel.ConfigManager()
    db = sentinel.ThreatDB()
    engine = sentinel.AntivirusEngine(config, db)
    firewall = sentinel.EnterpriseFirewallGuard(config, engine)
    armor = sentinel.WindowsExploitArmorShield(config, engine, firewall)

    if args.self_test:
        print_banner()
        print("[*] Launching Autonomous Defense Self-Test Simulation...")
        print("[*] Running 100% harmless verification vectors across all defense shields...\n")
        tester = sentinel.SecuritySelfTestEngine(config, engine, firewall)
        report = tester.run_all_tests()
        
        print(" +------------------------------------------------------------------------+")
        print(" |                       DEFENSE SIMULATION SCORECARD                     |")
        print(" +-----------------------------------------+--------------+---------------+")
        print(" | Test Vector Name                        | Status       | Score / Detail|")
        print(" +-----------------------------------------+--------------+---------------+")
        for item in report["details"]:
            status_symbol = " [PASS] " if item["passed"] else " [FAIL] "
            print(f" | {item['name']:<39} | {status_symbol:<12} | {item['detail']:<13} |")
        print(" +-----------------------------------------+--------------+---------------+\n")
        
        print(f" ========================================================================")
        print(f"   TOTAL DEFENSE READINESS SCORE: {report['score']:>3}%  —  {report['rating']:<28}")
        print(f" ========================================================================\n")
        print(f"[i] Summary: {report['summary']}\n")

    elif args.audit_masquerade:
        print_banner()
        print("[+] Auditing Running Processes for Binary Masquerading & Impersonation...")
        proc_guard = sentinel.ProcessBehaviorGuard(config, engine)
        masq = proc_guard.audit_process_masquerading()
        if not masq:
            print("[+] All active system binaries verified at legitimate Windows paths. Zero masquerading detected.\n")
        else:
            print(f"[!] WARNING: Found {len(masq)} suspicious masqueraded process(es):")
            for m in masq:
                print(f"    - PID {m['pid']}: {m['name']} -> Path: {m['exe']}")
            print()

    elif args.audit_network:
        print_banner()
        print("[+] Inspecting Active Sockets, High-Risk Ports & C2 Indicators...")
        net_guard = sentinel.NetworkSentinelGuard(config, engine, firewall)
        conns = net_guard.inspect_network()
        print(f"[+] Inspected {len(conns)} active TCP/UDP network connections.")
        for c in conns[:15]:
            print(f"    PID {c['pid']:<6} [{c['process']:<20}] {c['local']:<22} -> {c['remote']:<22} ({c['status']})")
        print()

    elif args.scan or args.deep:
        paths = [args.path] if args.path else config.get("scan_paths", [])
        print_banner()
        print(f"[+] PC Sentinel V3.5 Scanning: {paths}")
        engine.scan_paths(paths, deep=args.deep)
        print(f"\n[+] Scan Complete! Scanned: {engine.stats['files_scanned']} | Threats: {engine.stats['threats_found']}\n")

    elif args.vaccine:
        usb = sentinel.USBSentinelVaccineShield(config, engine)
        drives = usb.get_removable_drives()
        print("\n[+] Checking USB Removable Drives...")
        if not drives:
            print("[!] No USB flash drives detected. Shield is armed for automatic injection.")
        for d in drives:
            usb.scan_usb_drive(d)
            print(f"[+] Vaccinated drive: {d}")

    elif args.ram_boost:
        print("\n[+] Purging Windows Process Working Sets & Relieving Load...")
        ram_reliever = sentinel.AutoRAMLoadRelieverShield(config, engine)
        freed = ram_reliever.purge_ram()
        m = ram_reliever.get_system_metrics()
        print(f"[+] RAM Purged! Freed approx {freed:.1f} MB memory. (Current Usage: {m['ram_percent']:.1f}%)\n")

    elif args.battery_eco:
        print("\n[+] Engaging Smart Battery Eco Turbo Saver...")
        bat = sentinel.BatteryPowerSentinelGuard(config, engine)
        count = bat.activate_eco_mode()
        print(f"[+] Throttled {count} background power-draining processes into Eco Efficiency mode.\n")

    elif args.battery_status:
        bat = sentinel.BatteryPowerSentinelGuard(config, engine)
        info = bat.get_battery_info()
        print(f"\n--- PC Sentinel Battery & Power Telemetry ---")
        print(f"Level:        {info['percent']}%")
        print(f"Power Source: {info['status_str']}")
        print(f"Runtime:      {info['time_str']}")
        print(f"Eco Mode:     {'ACTIVE' if info['eco_active'] else 'STANDBY'}")
        
        wasters = bat.get_power_wasters(limit=10)
        print(f"\n--- Top Background Power Wasters ({len(wasters)}) ---")
        for w in wasters:
            print(f"PID {w['pid']:<6} {w['name']:<25} CPU: {w['cpu_percent']}%  RAM: {w['memory_mb']} MB  [{w['impact']}]")
        print()

    elif args.clean_junk:
        print("\n[+] Shredding temp files and caches...")
        temp_dirs = [Path.home() / "AppData" / "Local" / "Temp", Path("C:/Windows/Temp")]
        freed = 0
        count = 0
        for td in temp_dirs:
            if not td.exists(): continue
            for item in td.glob("*"):
                try:
                    if item.is_file():
                        freed += item.stat().st_size
                        item.unlink()
                        count += 1
                except Exception: pass
        print(f"[+] Shredded {count} junk files. Freed {freed/(1024*1024):.2f} MB disk space.\n")

    elif args.audit_rootkit:
        print("\n[+] Auditing Windows Persistence & Startup...")
        auditor = sentinel.WindowsPersistenceAuditor(config, engine)
        reg_items = auditor.audit_startup_registry()
        print(f"\n--- Startup Registry ({len(reg_items)} items) ---")
        for r in reg_items:
            flag = "[HIGH RISK]" if r["suspicious"] else "[CLEAN]"
            print(f"{flag:12} [{r['location']}] {r['name']:20} -> {r['command']}")
        print("\n[+] Audit Complete.\n")

    elif args.quarantine_list:
        records = db.get_quarantine_records()
        print(f"\n--- Quarantined Threats ({len(records)}) ---")
        for r in records:
            print(f"[{r.get('timestamp','')[:19]}] {r.get('original')} -> {r.get('quarantine')}")
        print()

    elif args.audit_fortress:
        print_banner()
        print("[*] Auditing Windows 10 End-of-Support (EOL) Exploit Armor Posture...\n")
        report = armor.audit_posture()
        print(" +------------------------------------------------------------------------+")
        print(" |                   WINDOWS 10 EOL EXPLOIT ARMOR AUDIT                   |")
        print(" +-----------------------------------------+--------------+---------------+")
        print(" | Hardening Vector                        | Status       | Security Level|")
        print(" +-----------------------------------------+--------------+---------------+")
        for item in report["checks"]:
            status_symbol = " [SECURE] " if item["passed"] else " [EXPOSED] "
            print(f" | {item['name']:<39} | {status_symbol:<12} | {item['status']:<13} |")
        print(" +-----------------------------------------+--------------+---------------+\n")
        print(f"   HARDENING DEFENSE SCORE: {report['score']}%  —  {report['rating']}")
        admin_flag = "ACTIVE (ELEVATED)" if report['admin_mode'] else "USER MODE (Run as Admin to Harden)"
        print(f"   ADMIN PRIVILEGES:        {admin_flag}\n")

    elif args.harden_fortress:
        print_banner()
        print("[*] Engaging Windows 10 Fortress Mode (Anti-Exploit System Hardening)...")
        if not sentinel.is_admin():
            print("\n[!] ERROR: Administrator rights are required to apply Fortress Hardening.")
            print("[!] Please run this console as Administrator.\n")
        else:
            res = armor.apply_fortress_hardening()
            print("\n[+] Hardening Applied Successfully:")
            for k, v in res.items():
                print(f"    - {k:<25}: {v}")
            print("\n[+] System is now armored against unpatched Windows 10 EOL attack vectors.\n")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
