# Day 1: OSI Model & Wireshark Packet Analysis

## 1. OSI Model (Open Systems Interconnection)
OSI is a framework designed to perform internet connectivity, routing signals, and various other functions. It has 7 layers:

* **(Data) Application Layer (L7):** Designed to interact the user with the interface. Functionally uses protocols and ports like HTTP (port 80), HTTPS (port 443) for web, FTP (port 20), SFTP (port 21) for files, etc. Ensures application-to-application communication.
* **(Data) Presentation Layer (L6):** Plays roles like encoding, decoding, protecting data, and compressing data for faster transmission (e.g., zip formats). Ensures data is readable for networks and computers using standards like ASCII, UTF-8/16.
* **(Data) Session Layer (L5):** Handles connection establishing, maintaining, and termination. Also handles error checking and transmission modes (simplex like radio, half-duplex, full-duplex). Has unique features like synchronization (checkpointing)—for example, downloading a 100MB file with a marker every 10MB so a dropped connection resumes from the last marker instead of the beginning.
* **(Segment) Transport Layer (L4):** The most important layer, deciding how segments travel on the internet. It breaks data into pieces called segments. It has two main sub-protocols: TCP (Transmission Control Protocol - uses 3-way handshake, reliable, secure, but slower) and UDP (User Datagram Protocol - works without confirmation, faster, unreliable).
* **(Packet) Network Layer (L3):** Assigns IPs to segments and adds headers with source IP and destination IP, turning segments into *packets*. Ensures smooth data transmission and network management.
* **(Frame) Data Link Layer (L2):** Uses packets and adds physical addresses (MAC). Has two sublayers: MAC (Media Access Control - manages how devices connect for identification) and LLC (Logical Link Control - handles framing methods and communication flow).
* **(Bits) Physical Layer (L1):** Converts frames into raw bits so they can travel across physical wires, wireless networks, and other media.

---

## 2. Wireshark Practical Lab
Wireshark is designed to capture web and network traffic. 

* **How to run:** Run `sudo wireshark` in the Kali Linux terminal.
* **DNS Capture:** Opened another terminal, ran `nslookup google.com`, went back to Wireshark, and filtered by `dns`.
* **Packet Breakdown observed:**
  * **Frame (L2):** Shows frame size (max size typically 1500 bytes) and source MAC. Running as root in VMware shows ID 0 and VMware-specific address columns.
  * **Internet Protocol (L3):** Network layer providing source and destination IPs.
  * **UDP (L4):** Transport layer running on port 53 (DNS), showing source port, destination port, and **checksum** (which provides an extra integrity/security layer).
  * **Application (L7):** Domain Name System details showing transaction rates and query info.
