# Artifact 24 — Configuration Management & Change Control (ECO/CR)

**What this is**

Versioning and controlled changes to specs, ICDs, BOM, code, docs.

**Artifacts**

- CM Plan
- Change Request (CR) / Engineering Change Order (ECO) log

**How to build**

1. Create a page **“CM Plan”**:
    
    ```
    Artifacts under control: (Requirements, ICDs, SDS/SSDS, BOM, Test Plans, Code)
    Versioning rules: (semver, doc revs)
    Baselines: (what gets “frozen” and when)
    Change gates: (who approves, criteria)
    
    ```
    
2. Create a **CR/ECO** database:
    - ID, Title, Artifact(s) impacted, Reason, Risk/Impact, Alternatives, Decision, Approver, Effective Version, Links.
3. Require **CR** for any post-freeze changes (ICD freeze, requirements freeze).

**Quality check**

- There’s a clear **before/after diff** and a decision record for any change.

---

