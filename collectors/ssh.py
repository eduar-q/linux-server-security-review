"""
SSH configuration collector.
Inspects sshd_config safely to review security hardening parameters.
"""

import os

def collect():
    ssh_data = {
        "config_path": "/etc/ssh/sshd_config",
        "exists": False,
        "parameters": {}
    }
    
    # Parámetros clave de seguridad SSH que nos interesa auditar
    key_params_to_check = [
        "Port",
        "PermitRootLogin",
        "PasswordAuthentication",
        "PubkeyAuthentication",
        "X11Forwarding",
        "MaxAuthTries",
        "PermitEmptyPasswords"
    ]
    
    try:
        if os.path.exists(ssh_data["config_path"]):
            ssh_data["exists"] = True
            
            # Inicializamos los parámetros por defecto como no encontrados
            for param in key_params_to_check:
                ssh_data["parameters"][param] = "Not Specified / Default"
                
            with open(ssh_data["config_path"], "r") as f:
                for line in f:
                    line = line.strip()
                    # Ignorar comentarios y líneas vacías
                    if not line or line.startswith("#"):
                        continue
                    
                    # Separar clave y valor (asumiendo formato Key Value o Key SpacedValue)
                    parts = line.split(None, 1)
                    if len(parts) == 2:
                        param_key, param_val = parts[0], parts[1]
                        # Limpiar posibles comentarios al final de la línea
                        param_val = param_val.split("#")[0].strip()
                        
                        if param_key in key_params_to_check:
                            ssh_data["parameters"][param_key] = param_val
        else:
            ssh_data["error"] = "sshd_config file not found."
            
    except Exception as e:
        ssh_data["error"] = str(e)
        
    return ssh_data

if __name__ == "__main__":
    import json
    print(json.dumps(collect(), indent=4))
