# Day 09 - OverTheWire Bandit (Levels 8 to 13) & Advanced Linux Recon

## 📌 Summary
Today I covered Bandit Levels 8 to 13, focusing on text manipulation, binary inspection, data decoding, cipher translation, and SSH key-based authentication.

---

## 🛠️ Key Commands & Concepts Learned

1. **`file` Command:**
   - Used to inspect file types and format signatures (magic numbers) regardless of file extensions.

2. **`strings` Command:**
   - Filters out non-printable binary characters to extract human-readable text strings from raw binary files.

3. **`base64` Decoding:**
   - Decoded Base64 encoded streams using the `-d` flag:
     ```bash
     base64 -d data.txt
     ```

4. **`tr` (Translate) Command:**
   - Used for character-by-character translation/replacement, such as decoding ROT13 ciphers:
     ```bash
     cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
     ```

5. **`xxd` Command:**
   - Converts binary data into hex dumps or reverses hex back to binary (`xxd -r`).

6. **SSH Key-Based Authentication:**
   - Learned the fundamental difference between SSH key pairs:
     - **Public Key:** Shared with remote servers to allow access.
     - **Private Key:** Stored securely on the local system (never shared) to verify identity during connection (`ssh -i key.private user@host`).

---

## 🎯 Bandit Progress
- **Levels Completed:** Bandit 8 through 13.
- **Key Takeaway for CTI:** Binary analysis (`strings`, `file`, `xxd`) and decoding (`base64`, `tr`) are essential skills when analyzing obfuscated malware payloads and inspecting raw network captures.
