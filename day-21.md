# Day 21: Weekly CTI & SOC Review — SIEM, ELK, Logs & Phishing Triage

## 1. Overview of the Week
This week focused heavily on core Blue Teaming fundamentals, log monitoring, event management, SIEM architectures, and practical phishing analysis methodologies.

## 2. Core Components & Architecture
- **ELK Stack (Elasticsearch, Logstash, Kibana):** 
  - **Elasticsearch:** The backend database and search engine used to store and query logs in detail.
  - **Setup:** Installed from official sources, configured to run as a background service following standard documentation.
- **Log Classification:**
  - **Host-Centric Logs:** Detail application behavior, timestamps, dates, and file operations on endpoints.
  - **Network-Centric Logs:** Capture network telemetry including IPs, ports, and VPN traffic.
- **SIEM (Security Information and Event Management):**
  - A tool and technique used for centralized log investigation.
  - **SI (Security Information):** Focuses on log visualization and insights.
  - **EM (Event Management):** Tracks exact attack situations, such as failed login attempts and network triggers via Windows Event IDs.

## 3. Phishing Email Investigation Methodology (3-Step Framework)
1. **Inspection:** Open raw email sources in editors to uncover hidden details, attacker IPs, phishing links, and attached threats.
2. **Threat Intelligence Enrichment:** Search extracted indicators on threat databases (e.g., VirusTotal) to uncover malware types, server details, and campaign context.
3. **Reporting Structure:**
   - **Title / Heading:** Clear investigation subject.
   - **Target Context:** Origin of the sample and identified threat nature.
   - **Identification Definition:** Proof and reasoning explaining why the email is classified as phishing.
   - **IOCs & Artifacts:** Listed links, target IPs, server details, and requested payloads.

---
**Status:** Day 21 Weekly Summary & Deliverable Completed 🚀
