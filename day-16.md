# Day 16 - Sysmon Configuration & Event Tracking

## 1. What is Sysmon?
* **Definition:** Sysmon (System Monitor) is a Windows system service and device driver that deep-dives into system activity beyond standard Windows Event Viewer logs.
* **Key Monitoring Capabilities:** It tracks process creation events, network connections, file creation timestamps, and driver loads.

## 2. Setup & Configuration
* **Installation:** Downloaded from the official Microsoft / Sysinternals website.
* **Configuration File:** Requires an XML configuration file (commonly sourced from trusted repositories like SwiftOnSecurity or Microsoft documentation) to filter noise and capture specific high-value security telemetry.
* **Log Details:** Provides granular, structured logs including precise timestamps, command-line arguments, and parent-child process relationships.dy
