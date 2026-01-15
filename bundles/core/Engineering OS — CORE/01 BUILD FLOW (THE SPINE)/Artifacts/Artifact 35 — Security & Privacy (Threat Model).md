# Artifact 35 — Security & Privacy (Threat Model)

**What this is**

How you prevent misuse, protect data, and respond to incidents.

**Artifacts**

- Threat Model (STRIDE or similar)
- Security Requirements
- Security Test Plan
- Incident Runbook

**How to build**

1. Diagram trust boundaries; list assets (credentials, keys, PII).
2. Identify threats (Spoofing/Tampering/Repudiation/Info Disclosure/DoS/Elevation).
3. Create **Security Requirements** (e.g., encryption at rest, authN/authZ).
4. Add **security tests** (pen tests, fuzzing, secrets scans).
5. Draft **Incident Runbook**: detect → contain → eradicate → recover → postmortem.

**Quality check**

- Highest-impact threats have concrete mitigations and tests.

---

