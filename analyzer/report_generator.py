#!/usr/bin/env python3
"""
Report Generator Module
Compiles audit results and risk findings into a structured technical report.
"""

import json
import os
from datetime import datetime

class ReportGenerator:
    def __init__(self, findings, system_info=None):
        self.findings = findings
        self.system_info = system_info or {}
        self.timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    def generate_json_report(self, output_path="examples/latest_audit_report.json"):
        """Generates a structured JSON report containing the audit summary and risks."""
        report = {
            "metadata": {
                "audit_timestamp": self.timestamp,
                "target_system": self.system_info.get("hostname", "Unknown"),
                "os_release": self.system_info.get("os_release", "Unknown"),
                "total_findings": len(self.findings)
            },
            "findings": self.findings
        }

        # Aseguramos que la carpeta examples exista
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        with open(output_path, "w") as f:
            json.dump(report, f, indent=4)
        
        return output_path
