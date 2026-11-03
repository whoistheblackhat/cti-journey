# Day 17: CyberDefenders — Emprisa Maldoc Lab Triage

## Overview
Today, I registered on CyberDefenders.org and completed the **Emprisa Maldoc Lab**. This was my first time analyzing a malicious document (RTF file), making it a challenging but rewarding hands-on learning experience. 

The lab required investigating a malicious RTF document to answer 13 specific triage and technical questions.

## Key Investigation Steps & Methodology

1. **Lab Setup & Initial Inspection:**
   - Downloaded and extracted the target laboratory zip file containing the malicious hex/RTF payload.
   - Identified that answer keys regarding vulnerability details, patch numbers, and shellcode artifacts were embedded within the file structure.

2. **Static Analysis & Patch Identification:**
   - Researched the underlying vulnerability details (**CVE-2017-11882**) and mapped the required missing patch parameters (**KB4011279**).
   - Used basic Linux utilities like `strings` to identify readable artifact indicators.

3. **Dynamic Threat Intelligence Sandbox Inspection:**
   - Submitted the malicious file to [Hybrid-Analysis](https://www.hybrid-analysis.com) for automated execution sandbox metrics.
   - Leveraged the **Process** tab within Hybrid-Analysis to extract critical execution paths, spawned processes, and dropped payload URLs.

4. **Stream Extraction & Shellcode Analysis:**
   - Cloned and utilized Didier Stevens' `rtfdump.py` utility to dissect the RTF structure.
   - Isolated and dumped **Stream 7** (containing the embedded shellcode payload) into `shellcode.bin` for deeper inspection.
   - Successfully correlated extracted strings and sandbox analysis output to resolve all 13 lab questions.

---
**Status:** Day 17 Completed 🚀
