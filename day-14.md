# Week 2 Summary & Cheat-Sheet: Linux CLI & Network Reconnaissance

This cheat-sheet summarizes the essential Linux commands and network reconnaissance tools covered during Week 2 of the CTI journey.

---

## 1. Linux File & Text Manipulation Commands

* **`cat`**: Prints the content of a file directly to the terminal.
* **`ls -la`**: Lists all files and folders (including hidden ones starting with `.`), displaying permissions, modification dates, file sizes, owners, and groups.
* **`grep` (Global Regular Expression Print):** Searches for specific text patterns inside files.
  * `-e`: Matches specific text lines. (Note: `grep` is case-sensitive by default).
  * `-E`: Enables extended regular expressions, allowing multiple text search using the OR (`|`) operator.
  * `-i`: Ignores case sensitivity during searches.
* **`find`**: A powerful utility to search for files and directories based on specific attributes.
  * `-size`: Filters files by size (bytes, blocks).
  * `-user`: Finds files owned by a specific user.
  * `-type`: Filters by file type (e.g., file, directory).
* **`xxd`**: A tool to create a hex dump of a file or reverse a hex dump back to binary.

---

## 2. Network & Connectivity Commands

* **`ssh`**: Connects securely to a remote server using a specified server address and port.
* **`curl`**: Interacts with web servers, checks server status, inspects security headers (`-I`), downloads files, and tests endpoints.
* **`whois`**: Retrieves domain registration details, registrar information, creation/expiry dates, and abuse contact emails/phones.
* **`nslookup`**: Resolves domain names to find public IP addresses and DNS records.
* **`ss` (Socket Statistics):** Displays active network socket details, process IDs, and services.
  * `-t`: Filters for TCP connections.
  * `-u`: Filters for UDP connections.
  * `-l`: Shows only listening services.s
  * `-p`: Displays the Process ID (PID) associated with the socket.
  * `-n`: Shows numeric addresses and ports instead of resolving names.

---

## 3. Network Mapping & Reconnaissance (Nmap)

**Nmap** is a powerful tool used for network discovery, port scanning, and attack surface mapping. 

### Port States:
* **Open:** The target service is actively accepting connections on this port.
* **Closed:** The port is accessible, but no service is listening on it.
* **Filtered:** Firewalls, routers, or network filters are blocking probes, making it unclear if the port is open.

### Important Nmap Flags:
* **Default Scan (`nmap <ip>`):** Automatically performs a TCP connect scan if administrative privileges are absent, scanning the top 1,000 common ports.
* **`-sS` (TCP SYN / Stealth Scan):** Sends a `SYN` packet. If the target returns `SYN-ACK`, Nmap immediately replies with an `RST` (Reset) packet to abort the connection. This leaves fewer traces in standard connection logs.
* **`-sT` (TCP Connect Scan):** Completes the full 3-way handshake (`SYN` -> `SYN-ACK` -> `ACK`), which logs the connection on the target.
* **`-sV`:** Probes open ports to determine exact service names and software versions (vital for CVE mapping).
* **`-A`:** Aggressive scan mode (includes OS detection `-O`, version detection `-sV`, script scanning `-sC`, and traceroute).
* **`-p` / `-p-`:** Specifies custom port ranges (e.g., `-p-` scans all 65,535 ports).
