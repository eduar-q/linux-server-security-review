#!/usr/bin/env python3
"""
Linux Server Security Review
Main orchestrator script for read-only system auditing.
"""

import sys
import os
import json

# Importamos todos los colectores hasta el Día 3
from collectors import system
from collectors import users
from collectors import ssh
from collectors import services
from collectors import cron
from collectors import network
from collectors import permissions
from collectors import suid      # <-- Nuevo Día 3
from collectors import kernel    # <-- Nuevo Día 3

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

    # 4. Services Collector
    print("\n[*] Executing Services Collector...")
    services_data = services.collect()
    print(f"[+] Total active system services found: {services_data.get('total_active', 0)}")

    # 5. Cron Collector
    print("\n[*] Executing Cron Collector...")
    cron_data = cron.collect()
    print(f"[+] Total cron/scheduled entries found: {len(cron_data.get('system_crontab_entries', []))}")

    # 6. Network Collector
    print("\n[*] Executing Network Collector...")
    net_data = network.collect()
    print(f"[+] Total listening ports/sockets found: {net_data.get('total_listening', 0)}")

    # 7. Permissions Collector
    print("\n[*] Executing Permissions Collector...")
    perm_data = permissions.collect()
    print(f"[+] Critical files audited: {len(perm_data.get('critical_files', {}))}")

    # 8. SUID/SGID Collector (Nuevo Día 3)
    print("\n[*] Executing SUID/SGID Binaries Collector...")
    suid_data = suid.collect()
    print(f"[+] Total SUID/SGID binaries found: {suid_data.get('total_found', 0)}")

    # 9. Kernel Modules Collector (Nuevo Día 3)
    print("\n[*] Executing Kernel Modules Collector...")
    kernel_data = kernel.collect()
    print(f"[+] Total loaded kernel modules found: {kernel_data.get('total_modules', 0)}")

    print("\n[+] Day 3 completed successfully! All data collectors are fully operational.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Audit interrupted by user. Exiting cleanly.")
        sys.exit(0)
