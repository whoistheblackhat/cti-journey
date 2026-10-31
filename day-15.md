# Day 15 - SOC Log Collection Architecture & ELK Stack Setup

In a Security Operations Center (SOC), determining how logs are collected and centralized is the foundational step. To understand this architecture, we analyze a 3-component setup (typically distributed across Linux environments and a Windows target).

---

## Core Architecture Components

### 1. The ELK Stack (Elasticsearch, Logstash, Kibana)
* **What it is:** A centralized log management and SIEM platform.
* **Kibana:** A browser-based GUI built on a Node.js backend that provides dashboards, charts, and data visualization. Elasticsearch acts as the backend database for storing and searching logs.
* **Configuration & Deployment:**
  * Installed on a Linux server instance.
  * Started as system daemon services using `systemctl` (`daemon-reload`, `enable`, `start`).
  * Configuration files (`.yml`) require proper security settings, generation of required keys/passwords, and token handling.
  * **Important Note:** ELK runs multiple services across various ports; firewall rules (e.g., UFW/iptables) must be properly configured to allow internal communication.

### 2. Fleet Server & Elastic Agents
* **Fleet Server:** Used to centrally manage, configure, and update Elastic Agents across the network.
* **Elastic Agent:** A lightweight agent deployed on target machines to collect multiple types of logs and system telemetry in various formats and stream them back to the central ELK/Fleet server.

### 3. Windows Target Machine
* Acts as the monitored endpoint/target environment where user activity, system events, and security logs (such as Windows Event Logs and Sysmon logs) are generated and shipped via the Elastic Agent to the central server.
