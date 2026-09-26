"""
Permissions collector.
Inspects critical system files permissions to detect potential exposure.
"""

import os

def collect():
    perm_data = {
        "critical_files": {},
        "error": None
    }
    
    # Archivos críticos del sistema operativo que requieren auditoría de permisos
    files_to_check = [
        "/etc/passwd",
        "/etc/shadow",
        "/etc/sudoers",
        "/etc/ssh/sshd_config"
    ]
    
    try:
        for filepath in files_to_check:
            if os.path.exists(filepath):
                file_stat = os.stat(filepath)
                # Extraemos los permisos en formato octal (ej. '0644', '0600')
                permissions_octal = oct(file_stat.st_mode & 0o777)
                
                perm_data["critical_files"][filepath] = {
                    "exists": True,
                    "permissions": permissions_octal,
                    "uid": file_stat.st_uid,
                    "gid": file_stat.st_gid
                }
            else:
                perm_data["critical_files"][filepath] = {
                    "exists": False
                }
                
    except Exception as e:
        perm_data["error"] = str(e)
        
    return perm_data

if __name__ == "__main__":
    import json
    print(json.dumps(collect(), indent=4))
