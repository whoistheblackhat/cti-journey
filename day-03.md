# Day 3: IP Addressing, Private/Public IPs, NAT & CIDR

## 1. IPv4 vs IPv6
* **IPv4:** The older 32-bit addressing system supporting around 4.3 billion devices. It is running out because modern households and enterprises have countless connected devices.
* **IPv6:** The newer 128-bit addressing system created to solve IPv4 exhaustion, providing more than enough addresses for trillions of devices.

## 2. Ports: The Gateways
* While an IP address connects one device to another globally, **Ports** act as doors/gates that direct traffic to specific services or applications running on that device.

## 3. Types of IP Addresses
* **Private / Local IPs:** Used within a local private network (LAN). They are not routable on the public internet. Divided into 3 classes:
  * **Type A:** `10.0.0.0` to `10.255.255.255`
  * **Type B:** `172.16.0.0` to `172.31.255.255`
  * **Type C:** `192.168.0.0` to `192.168.255.255`
* **Public IPs:** Globally unique IP addresses assigned by ISPs (e.g., `8.8.8.8`). Private IPs cannot talk to the outside world directly without NAT.

## 4. NAT (Network Address Translation) & Its Types
NAT acts as a bridge on routers, allowing private local IPs to communicate with external public services.
1. **Static NAT (1:1):** One private IP maps permanently to one public IP.
2. **Dynamic NAT:** A router assigns an available public IP from a pool to a private device for outbound traffic.
3. **PAT (Port Address Translation / NAT Overload):** Multiple private IPs share a single public IP by using unique port numbers (most common in home routers).

## 5. DHCP & APIPA
* **DHCP (Dynamic Host Configuration Protocol):** Automatically assigns IP addresses to devices on a network.
* **APIPA (Automatic Private IP Addressing):** A fallback mechanism in operating systems (`169.254.x.x` range) that assigns a temporary local IP when no DHCP server is available.

## 6. Subnetting & CIDR
* **Network vs Host Analogy:** Think of a **Network** as a city (e.g., Green Park City) and a **Host** as an individual house inside that city.
* **CIDR (Classless Inter-Domain Routing):** Acts as a marker (e.g., `/24`) attached to an IP to define the network and host portions, helping divide networks efficiently without wasting IP addresses.

## 7. Additional Networking Concepts
* **Loopback Address:** The local address of the machine itself (`127.0.0.1`), used for internal testing and background services.
* **IP Packet Header (Layer 3):** Carries crucial metadata like Source IP, Destination IP, and TTL (Time to Live) to manage packet routing and prevent infinite loops.
