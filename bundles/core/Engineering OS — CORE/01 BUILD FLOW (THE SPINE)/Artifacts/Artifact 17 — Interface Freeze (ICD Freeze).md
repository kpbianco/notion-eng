# Artifact 17 — Interface Freeze (ICD Freeze)

**What this is**

You lock interfaces and create change control.

**Artifacts**

- “ICD v1.0 Freeze” note/page (date/time)
- Change Request (CR) template

**How to build**

1. Create a short page:
    
    ```
    **ICD Freeze v1.0**
    Date: <YYYY-MM-DD>
    Scope: <List of ICDs/pin maps frozen>
    Rule: Any change requires a CR + version bump
    
    ```
    
2. Add a CR template:
    
    ```
    **CR-###: <Title>**
    Change Summary:
    Rationale:
    Impacted Docs:
    Risks/Alternatives:
    Approval (Names/Dates):
    Outcome (Approved/Rejected):
    
    ```
    
3. Duplicate this for each change post-freeze.

**Quality check**

- Any interface change after this date has a **CR** and a **new version tag**.

---

