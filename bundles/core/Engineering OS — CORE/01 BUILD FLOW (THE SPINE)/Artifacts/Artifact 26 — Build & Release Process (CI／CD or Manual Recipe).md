# Artifact 26 — Build & Release Process (CI/CD or Manual Recipe)

**What this is**

A deterministic recipe to build, test, package, and publish artifacts.

**Artifacts**

- Build Recipe (local + CI)
- Release Checklist
- Release Notes Template

**How to build**

1. Page **“Build Recipe”** with:
    
    ```
    Prereqs (tools/versions)
    One-liner (e.g., make release)
    Outputs (binaries, gerbers, docs bundle)
    Artifacts location (links)
    
    ```
    
2. **Release Checklist**:
    - Version bump, changelog updated, tests green, ICD/BOM frozen, tag created, artifacts uploaded, hashes recorded, release notes published.
3. **Release Notes** template:
    - New, Fixed, Breaking, Migration steps, Hashes/Artifacts, Known issues.

**Quality check**

- A fresh machine can produce identical artifacts from the recipe.

---

