# Architecture and Execution Flow - Linux Server Security Review

## Overview
`linux-server-security-review` is a modular, read-only system auditing framework designed for Linux environments. It evaluates critical security parameters against a predefined baseline, scores risks, and generates structured reports for defensive analysis.

## Core Architecture

### 1. Collectors (`collectors/`)
The tool executes independent, non-intrusive collection modules to inspect system state:
- **System & Kernel:** OS release, architecture, and loaded kernel modules.
- **Identity & Access:** Local user accounts, shells, and permission mapping.
- **Daemons & Configuration:** SSH daemon parameters, active systemd services, and cron jobs.
- **Network & Privileges:** Listening sockets, critical file permissions, and SUID/SGID binaries.

### 2. Analysis & Comparison (`analyzer/`)
- **Baseline Manager (`baseline.py`):** Loads the security standard configuration.
- **State Comparator (`comparator.py`):** Cross-references active system configurations against the baseline parameters.
- **Risk Engine (`risk_engine.py`):** Evaluates discrepancies, assigns severities (`HIGH`, `MEDIUM`, `LOW`), and compiles precise remediation steps.
- **Report Generator (`report_generator.py`):** Bundles findings and system metadata into structured JSON reports.

### 3. Execution Flow (`main.py`)
1. Verifies root privileges for comprehensive inspection.
2. Triggers all collection modules sequentially.
3. Compares results against the baseline.
4. Evaluates risks and prints actionable terminal alerts.
5. Exports a standardized JSON audit report to `examples/`.
