# Artifact 25 — Source Control & Branch Strategy

**What this is**

How you structure repos/branches/tags to keep work stable and reproducible.

**Artifacts**

- Repo Map
- Branch/Tag Policy
- PR Template

**How to build**

1. Page **“Repo & Branch Strategy”** with:
    
    ```
    Repos: <list, purpose, link>
    Branches: main (protected), develop, feature/<name>, release/<ver>, hotfix/<ver>
    Tagging: vA.B.C ties to doc/BOM/Test baselines
    
    ```
    
2. Add **PR Template**:
    
    ```
    Summary
    Linked requirements/tests
    Risk/rollback
    Screenshots/logs
    Checklist (lint/tests/docs updated)
    
    ```
    
3. Protect main/release; require review + status checks.

**Quality check**

- You can checkout a **tag** and reproduce the build + artifacts exactly.

---

