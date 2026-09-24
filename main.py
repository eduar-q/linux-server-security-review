#!/usr/bin/env python3
"""
Linux Server Security Review
Main orchestrator script for read-only system auditing.
"""

import sys
import os
import json

# Importamos colectores (Día 1 y Día 2)
from collectors import system
from collectors import users
from collectors import ssh  # <-- Nuevo colector SSH

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

    # 3. SSH Collector (Nuevo)
    print("\n[*] Executing SSH Collector...")
    ssh_data = ssh.collect()
    print(json.dumps(ssh_data, indent=4))

    print("\n[+] Day 2 initial target (SSH Collector) integrated successfully!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Audit interrupted by user. Exiting cleanly.")
        sys.exit(0)
