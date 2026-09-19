# Linux Server Security Review 🛡️

> **Status:** 🚧 Active Development — Version 0.1
> *Lightweight, read-only security and configuration review tool for Linux servers.*

---

## 🇬🇧 English Version

### Overview

**Linux Server Security Review** is a lightweight, read-only Python tool designed to inspect security-relevant configuration and system state on Linux servers.

The project focuses on collecting verifiable technical information about areas such as user accounts, SSH configuration, services, scheduled tasks, networking, permissions, and kernel-related settings.

The collected information can then be analyzed, compared against an optional baseline, and used to generate structured technical reports.

> **⚠️ Notice:** This tool operates strictly in **read-only mode**. It does not modify system configuration, install software, or execute remediation actions. Appropriate authorization is required before running it on any system.

---

### 🚀 Key Features

* **Automated Collection:** Collects security-relevant information from the Linux system.
* **Configuration Review:** Examines users, SSH, services, scheduled tasks, networking, permissions, and other security-related areas.
* **Baseline Comparison:** Compares observed system state against a defined baseline when available.
* **Risk & Review Engine:** Classifies findings into clear and explainable levels such as `LOW`, `MEDIUM`, `HIGH`, and `REVIEW`.
* **Structured Reports:** Generates human-readable Markdown reports and machine-readable JSON output.
* **Read-Only by Design:** The tool is intended to inspect systems without modifying their configuration.

---

### 📂 Project Architecture

```text
linux-server-security-review/
├── main.py                 # Main orchestrator
├── collectors/             # System data collection modules
│   ├── system.py           # OS, kernel, and release information
│   ├── users.py            # Local users and shell analysis
│   ├── ssh.py              # SSH configuration and access settings
│   └── ...                 # Additional security collectors
├── analyzer/               # Analysis, comparison, and risk logic
├── baselines/              # Baseline definitions
├── examples/               # Example reports and output
├── docs/                   # Technical documentation
└── tests/                  # Test fixtures and test data


```
---

📋 Output

The project is designed to produce two main report formats:

Markdown Report

A human-readable report containing observed configuration, findings, evidence, risk levels, and recommended areas for review.

JSON Report

Structured output containing the collected and analyzed information for programmatic processing, archiving, or future integrations.


---

⚠️ Scope

This project is intended to assist with Linux security and configuration reviews.

It does not automatically determine whether a system has been compromised, nor does it replace a complete security audit, penetration test, or human investigation.

Findings should be interpreted together with the available system context and supporting evidence.


---

## 🇪🇸 Versión en Español

Descripción

Linux Server Security Review es una herramienta ligera desarrollada en Python para realizar revisiones de configuración y seguridad en servidores Linux.

El proyecto recopila información técnica verificable sobre áreas como usuarios, configuración de SSH, servicios, tareas programadas, red, permisos y otros elementos relevantes para la seguridad del sistema.

La información recopilada puede ser analizada, comparada con una línea base opcional y utilizada para generar informes técnicos estructurados.

> ⚠️ Aviso: La herramienta funciona estrictamente en modo de solo lectura. No modifica la configuración del sistema, instala software ni ejecuta acciones de remediación. Se requiere autorización apropiada antes de utilizarla sobre cualquier sistema.




---

🚀 Características Principales

Recolección Automatizada: Obtiene información relevante del sistema Linux.

Revisión de Configuración: Analiza usuarios, SSH, servicios, tareas programadas, red, permisos y otros componentes relacionados con la seguridad.

Comparación con Línea Base: Permite comparar el estado observado con una línea base definida cuando está disponible.

Motor de Riesgos y Revisión: Clasifica los hallazgos mediante niveles claros y explicables como LOW, MEDIUM, HIGH y REVIEW.

Informes Estructurados: Genera informes en Markdown y datos estructurados en JSON.

Diseño de Solo Lectura: El objetivo es inspeccionar el sistema sin modificar su configuración.



---

📋 Alcance

El proyecto está orientado a apoyar revisiones de seguridad y configuración de servidores Linux.

No determina automáticamente si un sistema ha sido comprometido ni sustituye una auditoría de seguridad completa, una prueba de penetración o una investigación humana.

Los hallazgos deben interpretarse considerando el contexto del sistema y la evidencia disponible.


---

👨‍💻 Author

Eduar Q.

Linux · Python · System Administration · Defensive Security
