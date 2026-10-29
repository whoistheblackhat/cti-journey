```markdown
# Day 13 - Command-Line Web Probing, Domain Intelligence & Socket Inspection

## 📌 Summary
Today focused on command-line reconnaissance tools: `curl` for HTTP response header inspection, `whois` for domain registrar intelligence, and `ss` for local active socket/process tracking.

---

## 🛠️ Key Tools & Technical Breakdown

### 1. `curl` (Headless Web Probing)
Acts as a headless browser to inspect server infrastructure, HTTP protocols, redirection flows, and security policies without executing client-side scripts.

- **HTTP Status Codes:**
  - `2xx` (Success): Server processed the request successfully (e.g., `200 OK`).
  - `3xx` (Redirection): Resource moved temporarily/permanently (e.g., `301 Moved Permanently`).
  - `4xx` (Client Errors): Bad request or resource not found on client end (e.g., `404 Not Found`).
  - `5xx` (Server Errors): Server failed to fulfill a valid request.

- **Key Security Headers Inspected:**
  - `X-Frame-Options`: Prevents Clickjacking attacks by controlling whether the site can be rendered inside `<frame>`, `<iframe>`, or `<embed>` tags.
  - `Content-Security-Policy (CSP)`: Specifies trusted domains for loading scripts, images, and resources to mitigate XSS and data injection attacks.

- **Usage:**
  ```bash
  curl -I [https://linkpc.net](https://linkpc.net)

```

---

### 2. `whois` (Domain Registration Reconnaissance)

Used to gather domain ownership metadata, infrastructure details, creation/expiration dates, and Name Servers (NS records).

* **Usage:**
```bash
whois linkpc.net
whois jo3.org

```



---

### 3. `ss` (Socket Statistics & Active Connections)

An advanced alternative to `netstat` for inspecting running network sockets, listening ports, and associated Process IDs (PID).

* **Flag Breakdown (`-tulpn`):**
* `-t`: Show TCP sockets.
* `-u`: Show UDP sockets.
* `-l`: Filter and display only listening sockets.
* `-p`: Show the process name and PID associated with the socket.
* `-n`: Display numeric port numbers instead of resolving service names.


* **Usage:**
```bash
ss -tulpn

```



---

## 📋 Command Cheat-Sheet Matrix

| Command | Purpose | Primary Flags |
| --- | --- | --- |
| `curl` | Web probing & header analysis | `-I` (Headers only), `-v` (Verbose) |
| `whois` | Domain registrar & NS lookup | None (Direct target domain) |
| `ss` | Active network socket inspection | `-tulpn` (TCP/UDP, Listening, PID, Numeric) |

```

```
