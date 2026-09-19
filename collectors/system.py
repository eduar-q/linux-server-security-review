"""
System information collector.
Gathers basic OS details, kernel version, and hostname safely.
"""

import platform
import os

def collect():
    system_info = {}
    
    try:
        system_info["hostname"] = platform.node()
        system_info["system"] = platform.system()
        system_info["release"] = platform.release()
        system_info["version"] = platform.version()
        system_info["machine"] = platform.machine()
        
        # Intentar leer la versión de la distribución desde /etc/os-release si existe
        if os.path.exists("/etc/os-release"):
            os_release = {}
            with open("/etc/os-release", "r") as f:
                for line in f:
                    if "=" in line:
                        k, v = line.strip().split("=", 1)
                        os_release[k] = v.strip('"')
            system_info["os_release"] = os_release.get("PRETTY_NAME", "Unknown Linux")
        else:
            system_info["os_release"] = "Unknown"
            
    except Exception as e:
        system_info["error"] = str(e)
        
    return system_info

if __name__ == "__main__":
    # Prueba rápida individual del colector
    import json
    print(json.dumps(collect(), indent=4))
