"""
Kernel Modules collector.
Inspects currently loaded kernel modules in the Linux system.
"""

import subprocess

def collect():
    kernel_data = {
        "loaded_modules": [],
        "total_modules": 0,
        "error": None
    }
    
    try:
        # Usamos el comando 'lsmod' para listar los módulos del kernel cargados de forma limpia
        cmd = ["lsmod"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        modules_list = []
        for line in result.stdout.splitlines():
            line = line.strip()
            # Ignoramos la cabecera 'Module Size Usedby'
            if not line or line.startswith("Module"):
                continue
            
            parts = line.split()
            if parts:
                modules_list.append(parts[0])
                
        kernel_data["loaded_modules"] = modules_list
        kernel_data["total_modules"] = len(modules_list)
        
    except Exception as e:
        kernel_data["error"] = str(e)
        
    return kernel_data

if __name__ == "__main__":
    import json
    print(json.dumps(collect(), indent=4))
