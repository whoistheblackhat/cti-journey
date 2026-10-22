# Day 6: DNS, DNS Records & Advanced Threat Concepts (DGA & Tunneling)

## 1. What is DNS?
* **Domain Name System (DNS):** Acts like the phone book of the internet. It maps human-readable domain names to computer-readable IP addresses. When a browser makes a request, DNS resolves it to the correct server IP.

---

## 2. Common DNS Record Types
* **A Record (Host Record):** Maps a domain name directly to an IPv4 address. Usually sufficient for basic website configuration.
* **MX Record (Mail Exchange):** Directs email traffic to the correct mail servers for email forwarding and handling.
* **TXT & SPF Records:** Used for domain ownership verification and email security (Sender Policy Framework to prevent domain spoofing).

---

## 3. Advanced CTI Concepts: Threat Analysis
* **DGA (Domain Generation Algorithm):** A technique used by malware and threat actors to automatically generate a large number of pseudo-random domain names. This helps attackers bypass static domain blacklists for Command and Control (C2) communication.
* **DNS Tunneling:** A data exfiltration method where attackers abuse **Port 53** (which is almost always open for DNS traffic). They smuggle non-DNS data or malicious code out of a network by encoding it (often using Base64) inside standard DNS queries and TXT records.
