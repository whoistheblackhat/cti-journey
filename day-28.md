# Day 28: Phase 1 Checkpoint & Summary

## 1. TCP 3-Way Handshake
- The foundation of connection-oriented network communication.
- **Process:** Client sends a `SYN` flag to the server $\rightarrow$ Server responds with `SYN-ACK` to confirm $\rightarrow$ Client replies with an `ACK` flag to fully establish the connection (`ESTABLISHED`).

## 2. IPv4 Subnetting & CIDR
- Subnetting controls how IP addresses are distributed across devices within a network.
- **IPv4 Structure:** Total 32 bits split into 4 octets (8 bits each).
- **CIDR Notation:** Classless Inter-Domain Routing defines the network and host boundaries (e.g., `/26`).
- **Calculation Example (For ~60 devices):**
  - Chosen CIDR: `/26` (26 network bits, leaving $32 - 26 = 6$ host bits).
  - Total IPs: $2^6 = 64$.
  - Usable IPs: $64 - 2 = 62$ (excluding 1 Network ID and 1 Broadcast address).

## 3. DNS Inspection with `dig`
- A core command-line utility used to query DNS nameservers and inspect domain configurations, resource records (A, MX, TXT), and mail security configurations like SPF records.

## 4. CTI Automation Script (`urlhaus-fetcher.py`)
- A custom command-line intelligence tool built using three core Python modules:
  - **`requests`:** Handles GET/POST communications, custom headers, and API token authentication (`Auth-Key`).
  - **`argparse`:** Implements CLI functionality, allowing dynamic features like custom output file flags (`-o`).
  - **`csv`:** Formats and writes threat feed intelligence into structured reports.
