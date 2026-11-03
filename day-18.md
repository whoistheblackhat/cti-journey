# Day 18: Linux Auth Logs & Windows Event ID Analysis

## 1. Linux Systemd Journal Logs
On systemd-based Linux systems (like Kali Linux), traditional `/var/log/auth.log` is replaced/handled by `systemd-journald`.
- **Read Authentication Logs:** `sudo journalctl _COMM=sudo` or `sudo journalctl _COMM=sshd`
- **Filter Priority Log Levels:** `sudo journalctl -p err..alert`

## 2. Windows Authentication Event IDs
- **Event ID 4624 (Successful Logon):** Indicates successful user authentication. Important field: `Logon Type` (Type 2: Local Keyboard, Type 3: Network, Type 10: Remote Desktop).
- **Event ID 4625 (Failed Logon):** Indicates authentication failure. High volume of Event ID 4625 in short intervals is a primary indicator of Brute-Force/Password Spraying activity.
