"""
Users information collector.
Gathers local system users by parsing /etc/passwd safely.
"""

def collect():
    users_list = []
    
    try:
        with open("/etc/passwd", "r") as f:
            for line in f:
                # Omitir comentarios o líneas vacías
                if line.startswith("#") or not line.strip():
                    continue
                
                parts = line.strip().split(":")
                if len(parts) >= 7:
                    user_info = {
                        "username": parts[0],
                        "uid": parts[2],
                        "gid": parts[3],
                        "home": parts[5],
                        "shell": parts[6]
                    }
                    users_list.append(user_info)
                    
    except Exception as e:
        return {"error": str(e)}
        
    return {"total_users": len(users_list), "users": users_list}

if __name__ == "__main__":
    import json
    print(json.dumps(collect(), indent=4))
