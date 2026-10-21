# Day 5: Subnetting Part 2 — Network IDs, Broadcast Addresses & Usable Ranges

## 1. Subnetting Fundamentals
* **What is Subnetting?** A method to divide a large network into smaller, manageable subnetworks.
* **CIDR Role:** Tells the router how many bits are dedicated to the Network ID versus the Host ID.

---

## 2. Host Formula & Usable IPs
To find out how many devices can fit in a subnet, we use the host bit formula:
* **Total IPs:** `2 ^ host_bits`
* **Usable Host IPs:** `(2 ^ host_bits) - 2`

**Why minus 2?** Because every subnet reserves 2 fixed IPs:
1. **Network ID:** The very first IP of the range (represents the subnet).
2. **Broadcast Address:** The very last IP of the range (used to reach all devices in that subnet simultaneously).

---

## 3. Practical Calculation Example (`/25` Subnet)
* If we have 7 host bits left ($32 - 25 = 7$):
  * Total IPs = $2^7 = 128$ IPs.
  * Usable IPs = $128 - 2 = 126$ usable hosts.

**Range Breakdown:**
* **Network ID:** `192.168.1.0` (First IP)
* **Usable Range:** `192.168.1.1` to `192.168.1.26`
* **Broadcast Address:** `192.168.1.127` (Last IP)

*Note:* Because counting starts at `0`, a total of 128 IPs ends at `127` (`0` to `127` inclusive).
