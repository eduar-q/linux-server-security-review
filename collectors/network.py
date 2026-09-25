"""
Network collector.
Inspects active listening ports and network configuration safely.
"""

import subprocess

def collect():
    net_data = {
        "listening_ports": [],
        "total_listening": 0,
        "error": None
    }
    
    try:
        # Usamos 'ss' para listar puertos en escucha de forma rápida y limpia
        # -t: TCP, -u: UDP, -l: Listening, -n: Numérico (sin resolver nombres)
        cmd = ["ss", "-tulpn"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        ports_list = []
        for line in result.stdout.splitlines():
            line = line.strip()
            # Ignoramos la cabecera del comando
            if not line or line.startswith("Netid") or line.startswith("State"):
                continue
            ports_list.append(line)
            
        net_data["listening_ports"] = ports_list
        net_data["total_listening"] = len(ports_list)
        
    except Exception as e:
        net_data["error"] = str(e)
        
    return net_data

if __name__ == "__main__":
    import json
    print(json.dumps(collect(), indent=4))
