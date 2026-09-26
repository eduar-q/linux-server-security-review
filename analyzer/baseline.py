import json
import os

class BaselineManager:
    def __init__(self, baseline_path="baselines/baseline.example.json"):
        self.path = baseline_path

    def load(self):
        # Si no existe el archivo base, mejor avisar de una vez antes de que truene por otro lado.
        if not os.path.exists(self.path):
            raise FileNotFoundError(f"Pilas: No encontré el archivo base en {self.path}")
        
        with open(self.path, "r", encoding="utf-8") as f:
            return json.load(f)
