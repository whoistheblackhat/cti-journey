# Day 4: Subnetting, Binary Conversions & CIDR

## 1. Introduction to Subnetting & IP Structure
* **IPv4 Address:** Consists of 32 bits divided into 4 pairs or octets (8 bits each).
* **Network ID vs Host ID:** In any subnet, 2 IPs are always reserved:
  1. **Network ID** (The first IP of the subnet range).
  2. **Broadcast Address** (The last IP used to reach all devices in that subnet).
* **Subnet Mask:** Looks like an IP address (e.g., `255.255.255.0`) and helps separate the network portion from the host portion.

---

## 2. Binary to Decimal Conversion
To convert binary to decimal, we use the standard power-of-2 chart:
`128 | 64 | 32 | 16 | 8 | 4 | 2 | 1`

* **Example:** Converting binary `10100000` to decimal:
  * Active bits: `128` (has 1) and `32` (has 1).
  * Calculation: $128 + 32 = 160$.

---

## 3. Decimal to Binary Conversion
To convert decimal to binary, use the subtraction method against the chart values.

* **Example:** Converting the first octet of `192.168.1.10` (`192`):
  * `192 - 128 = 64` (Bit 128 is `1`)
  * `64 - 64 = 0` (Bit 64 is `1`)
  * Remaining bits are `0`.
  * Result: `11000000`.

---

## 4. CIDR (Classless Inter-Domain Routing)
* CIDR uses a slash notation (e.g., `/24`) to tell routers how many bits are reserved for the network versus hosts.
* **Example (`/24`):** Means the first 24 bits (3 octets) are reserved for the **Network**, and the remaining 8 bits (last octet) are available for **Hosts**.
