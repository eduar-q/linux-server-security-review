"""
Cron jobs collector.
Inspects system-wide scheduled tasks and crontab configurations.
"""

import os

def collect():
    cron_data = {
        "crontab_paths_checked": [
            "/etc/crontab",
            "/etc/cron.d"
        ],
        "system_crontab_entries": [],
        "error": None
    }
    
    try:
        # Leemos el archivo global /etc/crontab si existe
        if os.path.exists("/etc/crontab"):
            with open("/etc/crontab", "r") as f:
                for line in f:
                    line = line.strip()
                    # Ignorar comentarios, líneas vacías o variables de entorno (como SHELL=, PATH=)
                    if not line or line.startswith("#") or "=" in line and not line.startswith("@"):
                        continue
                    cron_data["system_crontab_entries"].append(line)
                    
        # Revisamos también si hay archivos dentro de /etc/cron.d
        if os.path.exists("/etc/cron.d"):
            for filename in os.listdir("/etc/cron.d"):
                filepath = os.path.join("/etc/cron.d", filename)
                if os.path.isfile(filepath):
                    with open(filepath, "r") as f:
                        for line in f:
                            line = line.strip()
                            if not line or line.startswith("#"):
                                continue
                            cron_data["system_crontab_entries"].append(f"{filename}: {line}")
                            
    except Exception as e:
        cron_data["error"] = str(e)
        
    return cron_data

if __name__ == "__main__":
    import json
    print(json.dumps(collect(), indent=4))
