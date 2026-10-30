# Week 1 Summary & Foundations: Networking, OSI Model, & Protocols

This document summarizes the core networking fundamentals covered during Week 1 of the CTI journey, including the OSI model, transport layer protocols, IP addressing, subnetting, and DNS reconnaissance.

---

## 1. The OSI Model (Open Systems Interconnection)
The OSI model is the core architecture of networking. Understanding network attacks requires knowing which layer they target. It consists of 7 layers:

* **[7] Application Layer:** Interacts directly with software applications, managing ports and services (e.g., HTTP `80`, HTTPS `443`, FTP `21`, SSH `22`).
* **[6] Presentation Layer:** Handles data translation, formatting, encryption/decryption, and compression/decompression so the OS can process it.
* **[5] Session Layer:** Establishes, maintains, and terminates communication sessions. Controls dialog types (Simplex, Half-Duplex, Full-Duplex).
* **[4] Transport Layer:** Breaks data down into **segments**. Acts as a bridge between upper application layers and lower network layers. Manages reliable delivery via **TCP** or fast delivery via **UDP**, including error detection and retransmission.
* **[3] Network Layer:** Encapsulates segments into **packets**, adding IP headers (Source IP, Destination IP, and TTL). Handles routing via protocols like OSPF (Open Shortest Path First).
* **[2] Data Link Layer:** Encapsulates packets into **frames**. Divided into two sublayers:
  * *MAC (Media Access Control):* Hardware device identification.
  * *LLC (Logical Link Control):* Frame synchronization and error checking via FCS/CRC.
* **[1] Physical Layer:** Converts frames into raw binary **bits** transmitted across physical media, cables, and electrical/optical signals.

---

## 2. Wireshark & Packet Analysis
* **Wireshark** is used to capture and inspect live network traffic (frames, packets, MTU, source/destination IPs).
* **Filters:** Used to isolate specific traffic patterns, such as TCP SYN packets (`tcp.flags.syn == 1`) to analyze handshakes.

---

## 3. TCP vs. UDP & The 3-Way Handshake
* **TCP (Transmission Control Protocol):** Connection-oriented, reliable protocol. Uses a **3-Way Handshake** to establish secure communication:
  1. Client sends `SYN`.
  2. Server responds with `SYN-ACK`.
  3. Client acknowledges with `ACK`.
* **UDP (User Datagram Protocol):** Connectionless protocol. Fast, but provides no delivery guarantee or handshake mechanism (fire-and-forget).

---

## 4. IP Addressing & NAT (Network Address Translation)
* **Private IP Address Ranges (RFC 1918):**
  * *Class A:* `10.0.0.0` to `10.255.255.255`
  * *Class B:* `172.16.0.0` to `172.31.255.255`
  * *Class C:* `192.168.0.0` to `192.168.255.255`
* **NAT Types:**
  * *Static NAT:* Maps one private IP to one unique public IP.
  * *Dynamic NAT:* Allocates public IPs dynamically from a pool.
  * *PAT (Port Address Translation / NAT Overload):* Maps multiple private IPs to a single public IP using unique source ports.

---

## 5. Subnetting & CIDR Notation
* Every subnet reserves the **first IP** as the Network ID and the **last IP** as the Broadcast address.
* **IPv4 Structure:** 32 bits total, divided into 4 octets (8 bits each).
* **Example Calculation (`/26` CIDR):**
  * Total bits: `32`. Host bits remaining: `32 - 26 = 6 bits`.
  * Total IPs: $2^6 = 64$ total addresses.
  * Usable Host IPs: $64 - 2 (Network + Broadcast) = 62$ usable hosts.
  * *Example Range:* For `10.0.0.0/26`, `10.0.0.0` is the Network ID, `10.0.0.63` is the Broadcast address, and hosts range from `10.0.0.1` to `10.0.0.62`.

---

## 6. DNS Resolution & Record Types
DNS translates human-readable domain names into IP addresses. Key record types include:
* **A Record:** Maps a hostname to its IPv4 address.
* **MX Record:** Mail Exchange records for email routing.
* **TXT / SPF Records:** Domain verification and security policies.

### Useful Reconnaissance Tools:
* **`dig`:** Advanced command-line tool to query specific DNS records.
* **`nslookup`:** Used to resolve target domain names and retrieve server IP addresses.
