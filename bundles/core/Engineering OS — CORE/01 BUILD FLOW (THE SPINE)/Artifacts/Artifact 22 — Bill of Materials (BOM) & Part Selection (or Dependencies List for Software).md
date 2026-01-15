# Artifact 22 — Bill of Materials (BOM) & Part Selection (or Dependencies List for Software)

**What this is**

A controlled list of everything you’ll use—parts or software packages—with rationale.

**Artifacts**

- Controlled BOM (or Software Dependency List)
- Part Selection Notes (Trade links)

**How to build**

1. Create a Notion database **“BOM / Dependencies”** with columns:
    - Item ID, Description/Version, Qty, Unit Cost, Ext. Cost (formula), Supplier/Repo, Lead Time, Lifecycle (Active/NRND/EOL), Alt/2nd source, Criticality (A/B/C), Selection Rationale (link to Trade Study), Compliance (RoHS/License), Notes.
2. For each item, attach **datasheet or package docs** (or LICENSE for software).
3. Mark **Criticality A** items (high risk if swapped).
4. Add a “**BOM v0.1 (Frozen)**” view for release builds.

**Quality check**

- No “mystery parts.” Every critical item has at least one vetted alternate.

---

