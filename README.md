# Linux Server Security Review 🛡️

> **Status:** 🚧 Active Development (Version 0.1 - Prototyping Phase)
> *Professional configuration review and security auditing tool for Linux servers.*

---

## 🇬🇧 English Version

### Overview
**Linux Server Security Review** is a lightweight, read-only Python auditing tool designed to inspect Linux server configurations, verify system hardening, and identify potential misconfigurations or security risks. 

Built specifically for systems administrators, security professionals, and freelance auditors, this tool automates the collection of critical security parameters (such as user accounts, SSH configurations, services, and cron jobs) and produces structured, verifiable technical reports.

> **⚠️ Notice:** This tool operates strictly in **read-only mode**. It does not modify, alter, or compromise the target system in any way. It requires read permissions (ideally executed via temporary SSH access with appropriate privileges) to gather telemetry.

---

### 🚀 Key Features
* **Automated Data Collection:** Gathers deep insights into system info, users, permissions, network services, and cron jobs.
* **Baseline Comparison:** Compares current server configurations against known baselines to detect unexpected drift or changes.
* **Risk & Review Engine:** Classifies findings into clear, actionable priority levels (`LOW`, `MEDIUM`, `HIGH`, `REVIEW`).
* **Professional Deliverables:** Automatically outputs structured reports in both **Markdown (`.md`)** and **JSON (`.json`)** formats.
* **Agentless & Safe:** Runs natively using standard Python and native Linux commands without installing heavy agents.

---

### 📂 Project Architecture
```text
linux-server-security-review/
├── main.py                 # Main orchestrator script
├── collectors/             # System data collection modules
│   ├── system.py           # OS, kernel, and release information
│   ├── users.py            # Local user accounts and shell analysis
│   ├── ssh.py              # SSH daemon and key configurations [Coming Day 2]
│   └── ...                 # Additional security collectors
├── analyzer/               # Processing, comparison, and risk engines
├── baselines/              # Configuration baseline templates
├── examples/               # Sample output reports (.md and .json)
├── docs/                   # Technical documentation and guides
└── tests/                  # Test fixtures and fixtures data
```

### 📋 Deliverables for Clients
When utilized as part of a professional audit service, the tool generates:

Markdown Report: A clean, human-readable summary detailing all discovered configuration items, risks, and hardening recommendations.

JSON Report: Raw structured data for programmatic ingestion, tracking, or archiving.



## 🇪🇸 Versión en Español

Linux Server Security Review es una herramienta de auditoría en Python liviana y de solo lectura, diseñada para inspeccionar la configuración de servidores Linux, verificar el endurecimiento (hardening) del sistema e identificar posibles fallos o riesgos de seguridad.

Creada para administradores de sistemas, profesionales de la seguridad y auditores independientes, esta herramienta automatiza la recolección de parámetros críticos (como cuentas de usuario, configuraciones de SSH, servicios y tareas programadas) generando informes técnicos estructurados y verificables.

### ⚠️ Aviso: Esta herramienta opera estrictamente en modo de solo lectura. No modifica ni altera el sistema del cliente. Requiere permisos de lectura para recopilar la telemetría necesaria.

### 🚀 Características Principales
Recolección Automatizada: Extrae información del sistema operativo, usuarios, permisos, servicios de red y tareas programadas.

Comparación de Línea Base: Contrasta la configuración actual del servidor para detectar cambios o desviaciones imprevistas.

Motor de Riesgos: Clasifica los hallazgos en niveles de prioridad claros y explicables (LOW, MEDIUM, HIGH, REVIEW).

Entregables Profesionales: Genera reportes estructurados listos para entregar al cliente en formatos Markdown y JSON.

### _Developed by Eduar Q. | Designed for Professional Linux Security Auditing Services._




