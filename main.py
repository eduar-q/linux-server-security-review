#!/usr/bin/env python3
"""
Linux Server Security Review
Main orchestrator script for read-only system auditing.
"""

import sys
import os
import json

# Importamos todos los colectores del Día 1 y Día 2
from collectors import system
from collectors import users
from collectors import ssh
from collectors import services  # <-- Nuevo
from collectors import cron      # <-- Nuevo

def print_banner():
    banner = """
    ==================================================
        Linux Server Security Review - Auditor
    ==================================================
    """
    print(banner)

def main():
    print_banner()
    print("[*] Initializing system audit review...")
    
    if os.geteuid() != 0:
        print("[!] Warning: Not running as root. Some collectors may have restricted access.")

    # 1. System Collector
    print("\n[*] Executing System Collector...")
    print(json.dumps(system.collect(), indent=4))
    
    # 2. Users Collector
    print("\n[*] Executing Users Collector...")
    users_data = users.collect()
    print(f"[+] Total users found: {users_data.get('total_users', 0)}")

    # 3. SSH Collector
    print("\n[*] Executing SSH Collector...")
    ssh_data = ssh.collect()
    print(f"[+] SSH config exists: {ssh_data.get('exists', False)}")

    # 4. Services Collector (Nuevo)
    print("\n[*] Executing Services Collector...")
    services_data = services.collect()
    print(f"[+] Total active system services found: {services_data.get('total_active', 0)}")

    # 5. Cron Collector (Nuevo)
    print("\n[*] Executing Cron Collector...")
    cron_data = cron.collect()
    print(f"[+] Total cron/scheduled entries found: {len(cron_data.get('system_crontab_entries', []))}")

    print("\n[+] Day 2 completed successfully! All core collectors integrated.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Audit interrupted by user. Exiting cleanly.")
        sys.exit(0)
