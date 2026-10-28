# Day 12 - Network Reconnaissance & Port Scanning via Nmap

## 📌 Summary
Today focused on network reconnaissance and attack surface discovery using Nmap. Explored key scan flags, TCP handshake dynamics, port states (Open vs Filtered), and how threat actors leverage version detection for CVE mapping during active reconnaissance.

---

## 🛠️ Key Concepts & Nmap Command Flags

### 1. Default TCP Connect Scan (`nmap <ip>`)
- Automatically defaults to `-sT` when executed without administrative (root) privileges.
- Completes the full 3-way handshake (`SYN` → `SYN-ACK` → `ACK`).
- **CTI Note:** Easily logged by target firewalls and IDS/IPS due to full connection establishment.

### 2. Stealth SYN Scan (`nmap -sS <ip>`)
- Sends a `SYN` packet and waits for `SYN-ACK`. Once received, it immediately responds with a `RST` (Reset) packet to tear down the connection before completion.
- Prevents connection logging on simpler network appliances while identifying open ports.

### 3. Full Port Range Scanning (`nmap -p-`)
- Bypasses Nmap's default scan of the top 1,000 common ports by scanning all **65,535** TCP ports.
- Useful for detecting non-standard or hidden services running on high-numbered ports.

### 4. Service Version Detection (`nmap -sV <ip>`)
- Probes open ports to determine the exact service name and version running.
- **CTI Relevance:** Service versions are mapped directly against vulnerability databases (NVD, CVE, Exploit-DB) to evaluate risk exposure.

### 5. Aggressive Scan (`nmap -A <ip>`)
Combines multiple modules into a single scan:
- `-O`: Operating System detection.
- `-sV`: Service version fingerprinting.
- `-sC`: Default Nse (Nmap Scripting Engine) script execution for common vulnerabilities.

---

## 📊 Sample Scan Analysis & Output Breakdown

```text
PORT        STATE     SERVICE       VERSION
80/tcp      open      http          Python httpd Werkzeug 3.14
9050/tcp    filtered  tor-socks     Tor SOCKS proxy
