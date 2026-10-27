# Day 11 - OverTheWire Bandit (Levels 18 to 20) & Linux Permissions

## 📌 Summary
Today I covered Bandit Levels 18 through 20. Focused on bypassing modified SSH login environments, analyzing SUID (SetUID) executable permissions, and establishing local connection bridges using Netcat (`nc`).

---

## 🛠️ Key Concepts & Commands Learned

### 1. SSH Shell Evasion (Level 18)
- **Concept:** When a remote user's `.bashrc` or shell is configured to log out immediately upon connection, commands can be passed directly through the SSH connection string to bypass the interactive shell.
- **Command:**
  ```bash
  ssh bandit18@bandit.labs.overthewire.org -p 2220 "cat readme"
