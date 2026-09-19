#!/usr/bin/env python3
"""
Linux Server Security Review
Main orchestrator script for read-only system auditing.
"""

import sys
import os
import json

# Importamos nuestros colectores del Día 1
from collectors import system
from collectors import users

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

    # 1. Ejecutar System Collector
    print("\n[*] Executing System Collector...")
    system_data = system.collect()
    print(json.dumps(system_data, indent=4))
    
    # 2. Ejecutar Users Collector
    print("\n[*] Executing Users Collector...")
    users_data = users.collect()
    print(f"[+] Total users found: {users_data.get('total_users', 0)}")
    # Mostramos solo los primeros 5 usuarios para no saturar la terminal en la prueba
    print(json.dumps(users_data.get('users', [])[:5], indent=4))
    print("    (... output truncated for brevity ...)")

    print("\n[+] Day 1 core targets achieved successfully!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Audit interrupted by user. Exiting cleanly.")
        sys.exit(0)
