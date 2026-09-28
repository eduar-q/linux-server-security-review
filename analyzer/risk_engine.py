#!/usr/bin/env python3
"""
Risk Engine Module
Evaluates discrepancies and assigns severity levels and remediation steps.
"""

class RiskEngine:
    def __init__(self):
        self.severity_map = {
            "PermitRootLogin": "HIGH",
            "PasswordAuthentication": "MEDIUM",
            "Port": "LOW"
        }

    def evaluate_discrepancies(self, discrepancies):
        """
        Takes a list of discrepancies from the comparator and enriches them
        with risk classifications and remediation advice.
        """
        enriched_findings = []

        for item in discrepancies:
            param_name = item.get("item")
            
            # Limpiamos el nombre por si viene con prefijos como "SSH -> "
            param_clean = param_name.split("->")[-1].strip() if param_name else ""
            
            severity = self.severity_map.get(param_clean, "MEDIUM")
            
            finding = {
                "parameter": param_name,
                "expected": item.get("esperado"),
                "found": item.get("encontrado"),
                "severity": severity,
                "recommendation": self._get_recommendation(param_clean, item.get("esperado"))
            }
            enriched_findings.append(finding)

        return enriched_findings

    def _get_recommendation(self, parameter, expected_value):
        """Provides technical remediation guidelines based on the parameter."""
        recommendations = {
            "PermitRootLogin": f"Edit /etc/ssh/sshd_config and set 'PermitRootLogin {expected_value}' to prevent direct administrative root access over the network.",
            "PasswordAuthentication": f"Edit /etc/ssh/sshd_config and set 'PasswordAuthentication {expected_value}' to enforce robust SSH key-based authentication.",
            "Port": f"Edit /etc/ssh/sshd_config and change the listening port to '{expected_value}' (or a non-standard custom port) to mitigate automated scanning bots."
        }
        return recommendations.get(parameter, "Review configuration against hardening benchmarks.")
