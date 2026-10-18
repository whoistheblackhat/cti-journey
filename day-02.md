# Day 2: TCP vs UDP, 3-Way Handshake & Wireshark Deep Dive

## 1. TCP (Transmission Control Protocol)
* **What is TCP?** A Transport Layer (L4) protocol designed for reliable, connection-oriented communication.
* **Is TCP itself secure?** No, TCP provides reliability (retransmission upon packet loss), not encryption. Security (like SSL/TLS) is added on top of it.
* **How is a connection established? (3-Way Handshake):**
  1. **SYN:** Client sends `SYN` flag to Server (asking to connect).
  2. **SYN-ACK:** Server responds with `SYN-ACK` (acknowledging and agreeing).
  3. **ACK:** Client sends `ACK` (connection is now established).

---

## 2. Advanced Packet Concepts (Wireshark Analysis)

### Wireshark Filters
* `tcp.flags.syn == 1` — Filters packets initiating a connection.
* `tcp.analysis.initial_rtt` — Measures initial round-trip time for TCP streams.

### MTU vs MSS
* **MTU (Maximum Transmission Unit):** Total size of a packet at L3 (typically **1500 bytes**).
* **MSS (Maximum Segment Size):** Payload size at L4 (**1460 bytes**).
  * *Calculation:* $\text{MTU (1500 bytes)} - \text{IP Header (20 bytes)} - \text{TCP Header (20 bytes)} = \text{MSS (1460 bytes)}$.

### L2 Decapsulation & Hardware Identification
* **Why start Decapsulation at L2?** L2 handles hardware interactions via MAC addresses.
* **MAC Address OUI (Organizationally Unique Identifier):** The first 3 bytes (pairs) identify the NIC vendor (e.g., `00:50:56` belongs to VMware virtual interfaces).

### TTL (Time to Live)
* **Purpose:** Prevents packets from looping infinitely on the network.
* **Default Values:** Windows = 128, Linux = 64.
* **Hop Calculation:** If a ping response shows `TTL = 58` from a Linux server (default 64), it means the packet traveled through $64 - 58 = 6$ routers/hops.

---

## 3. UDP (User Datagram Protocol)
* **What is UDP?** A connectionless, stateless L4 protocol. It sends packets ("fire and forget") without verifying if they reached the destination.
* **Why use UDP?** Speed over reliability. It has minimal overhead, making it ideal for streaming, online gaming, DNS (Port 53), and VoIP.
