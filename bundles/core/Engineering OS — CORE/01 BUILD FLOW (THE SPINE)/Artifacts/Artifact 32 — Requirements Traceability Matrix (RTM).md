# Artifact 32 — Requirements Traceability Matrix (RTM)

**What this is**

A many-to-many map: requirements ↔ design ↔ tests ↔ results.

**Artifacts**

- RTM view (Notion rollups)
- Coverage report

**How to build**

1. Ensure **Requirements** (from §6/§7), **Design Artifacts**, and **Test Cases** are databases.
2. Add relation fields so each requirement links to:
    - Design specs/ICDs that implement it
    - Test cases that verify it
    - Defects found against it (optional)
3. Create a view “**Coverage**” with formulas:
    - Has Design? (Y/N)
    - Has Test? (Y/N)
    - Latest Result (PASS/FAIL/PENDING)

**Quality check**

- No **Must** requirement is without design & passing test.

---

