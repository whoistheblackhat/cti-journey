# Day 24: Python Automation — JSON Parsing & API Data Extraction

## Overview
Focused on learning and implementing JSON parsing techniques to collect and structure threat intelligence data from public APIs programmatically.

## Key Learnings & Practical Implementation
- **API Data Fetching:** Used the `requests` module with custom headers (`User-Agent`) and timeout parameters to query public endpoints (e.g., `ipapi.co` for IP `8.8.8.8`).
- **JSON Parsing:** 
  - Converted raw HTTP responses into usable dictionaries using the `.json()` method.
  - Extracted individual data points (such as IP address, city, country, and organization) into dedicated variables.
- **Data Persistence & Debugging:**
  - Structured data can be directly written to `.csv` or `.txt` files using Python's file handling and `csv` modules.
  - Used `print(data)` or `print(resp)` for inspecting full API response payloads during debugging.

---
**Status:** Day 24 Completed 🚀
