# Day 25: CTI Automation — URLhaus API & Authentication Setup

## Overview
Explored URLhaus (abuse.ch) as a crowdsourced threat intelligence database for malicious URLs and malware payloads, and mastered its API endpoint authentication and query methods.

## Key Learnings & Practical Implementation
- **URLhaus Platform:** A repository where security researchers and systems submit malicious records, files, and URLs.
- **API Protection & Response Policies (RZP):** Endpoints are protected to maintain platform stability and security, requiring authentication via an **Auth Key** generated from user profiles.
- **HTTP Methods & Request Structure:**
  - **GET Requests:** Used for retrieving data and fetching feeds (e.g., recent URLs), passed along with the Auth Key in the headers (`-H "Auth-Key: <token>"`).
  - **POST Requests:** Used for submitting data, querying specific hashes, or checking malicious targets.
- **Terminal Testing (`curl`):** Successfully verified API connectivity, resolved `http_get_expected` handling errors, and fetched live threat intelligence feeds securely.

---
**Status:** Day 25 Completed 🚀
