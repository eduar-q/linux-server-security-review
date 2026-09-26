"""
SUID/SGID Binaries collector.
Scans critical system directories for files with SUID or SGID permissions set.
"""

import os

def collect():
    suid_data = {
        "suid_sgid_files": [],
        "total_found": 0,
        "error": None
    }
    
    # Directorios habituales donde buscar binarios de sistema privilegiados
    search_dirs = ["/usr/bin", "/usr/sbin", "/bin", "/sbin"]
    
    try:
        found_files = []
        for directory in search_dirs:
            if not os.path.exists(directory):
                continue
                
            for root, dirs, files in os.walk(directory):
                for file in files:
                    filepath = os.path.join(root, file)
                    try:
                        # Omitir enlaces simbólicos para evitar duplicados o errores
                        if os.path.islink(filepath):
                            continue
                            
                        file_stat = os.stat(filepath)
                        mode = file_stat.st_mode
                        
                        # Verificamos si el bit SUID (0o4000) o SGID (0o2000) está activo
                        is_suid = bool(mode & 0o4000)
                        is_sgid = bool(mode & 0o2000)
                        
                        if is_suid or is_sgid:
                            perms_octal = oct(mode & 0o7777)
                            found_files.append({
                                "path": filepath,
                                "permissions": perms_octal,
                                "suid": is_suid,
                                "sgid": is_sgid
                            })
                    except (PermissionError, FileNotFoundError):
                        # Ignoramos archivos sin permisos de lectura en la ruta
                        continue
                        
        suid_data["suid_sgid_files"] = found_files
        suid_data["total_found"] = len(found_files)
        
    except Exception as e:
        suid_data["error"] = str(e)
        
    return suid_data

if __name__ == "__main__":
    import json
    print(json.dumps(collect(), indent=4))
