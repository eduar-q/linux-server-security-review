class StateComparator:
    def __init__(self, baseline_data):
        self.baseline = baseline_data
        self.findings = []

    def check_ssh(self, current_ssh):
        # Revisamos clave por clave si el servidor se salió de la raya respecto a lo esperado.
        expected = self.baseline.get("ssh", {})
        
        for param, ideal_val in expected.items():
            real_val = current_ssh.get(param)
            
            if real_val != ideal_val:
                self.findings.append({
                    "item": f"SSH -> {param}",
                    "esperado": ideal_val,
                    "encontrado": real_val,
                    "detalle": "¡Ojo aquí! Configuración desalineada con el estándar."
                })
        
        return self.findings
