"""
Services collector.
Inspects active systemd services to review what is running on the server.
"""

import subprocess

def collect():
    services_data = {
        "active_services": [],
        "total_active": 0,
        "error": None
    }
    
    try:
        # Usamos systemctl para listar servicios activos de forma rápida y limpia
        # -t service: solo servicios
        # --state=active: solo los que están corriendo
        # --no-pager: evita que la salida se pause en la terminal
        cmd = ["systemctl", "list-units", "-t", "service", "--state=active", "--no-pager", "--plain"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        services_list = []
        for line in result.stdout.splitlines():
            line = line.strip()
            # Ignoramos líneas vacías o cabeceras de systemctl
            if not line or line.startswith("UNIT") or line.startswith("LOAD") or line.startswith("SUB") or line.startswith("--"):
                continue
            
            parts = line.split(None, 3)
            if len(parts) >= 1:
                service_name = parts[0]
                services_list.append(service_name)
                
        services_data["active_services"] = services_list
        services_data["total_active"] = len(services_list)
        
    except Exception as e:
        services_data["error"] = str(e)
        
    return services_data

if __name__ == "__main__":
    import json
    print(json.dumps(collect(), indent=4))
