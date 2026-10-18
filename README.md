# 🛡️ PC_Sentinel &mdash; Advanced Endpoint Security & Threat Monitoring

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![Security](https://img.shields.io/badge/Type-Endpoint_Security-red?style=for-the-badge)

**PC_Sentinel** is an autonomous endpoint security, threat detection, and system activity monitoring solution designed for Windows environments. It continuously observes running processes, checks system anomalies, manages quarantine protocols, and generates structured security audit logs.

---

## 🌟 Key Features

- **Real-Time Threat Detection:** Scans active processes and filesystem events against defined security rule sets and heuristics.
- **Quarantine Engine:** Safely isolates suspicious files into an encrypted quarantine repository.
- **Silent & Background Monitoring:** Includes silent execution drivers (
un_silent.bat) for background security telemetry without interrupting the user.
- **CLI & Automated Control:** Complete CLI interface (sentinel_cli.py) for manual audits, database lookups, and cache management.
- **Audit Logging:** Structured logging (logs/) and hash caching (scan_cache.json) for performance optimization.

---

## 🚀 Installation & Usage

1. **Clone Repository:**
   `ash
   git clone https://github.com/maalik143/PC_Sentinel.git
   cd PC_Sentinel
   `

2. **Run Sentinel Launcher:**
   `ash
   PC_Sentinel_Launcher.bat
   `
   Or launch via Python CLI:
   `ash
   python sentinel_cli.py
   `

---

## 👤 Author
**Zakaria Dahir Awale** &mdash; [@maalik143](https://github.com/maalik143)
