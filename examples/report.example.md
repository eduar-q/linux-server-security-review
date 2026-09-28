# Audit Report Summary - Linux Server Security Review

- **Target System:** `Linux-Lab`
- **OS Release:** `Linux Mint 22.3`
- **Timestamp:** `2026-09-28 00:00:00 UTC`
- **Total Findings:** `2`

---

## Findings Overview

### 1. [HIGH] SSH -> PermitRootLogin
- **Expected:** `no`
- **Found:** `yes`
- **Remediation:** Edit `/etc/ssh/sshd_config` and set `PermitRootLogin no` to prevent direct administrative root access over the network.

### 2. [LOW] SSH -> Port
- **Expected:** `22`
- **Found:** `2222`
- **Remediation:** Edit `/etc/ssh/sshd_config` and change the listening port to `22` (or a custom port) to mitigate automated scanning bots.
