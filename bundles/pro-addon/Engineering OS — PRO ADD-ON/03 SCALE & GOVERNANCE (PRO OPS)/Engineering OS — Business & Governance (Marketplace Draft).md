# Business & Governance (Marketplace Draft)

### What this page is

A compact, practical set of operating systems for **business-side execution** in an Engineering OS.

It defines three databases (21–23), each with:

- **Purpose** and **Definition of Done**
- Suggested **Fields** (schema)
- A **CSV Starter** for quick import
- A lightweight **SOP** and **Gate criteria**
- Clear **Relations** for traceability

### How to use

1. Treat each section (21–23) as its own database.
2. Create the database using the **Fields** list.
3. Optional: copy the **CSV Starter** into a `.csv` and import it.
4. Wire the **Relations** so cost, changes, releases, and comms stay connected.

---

## Engineering OS — Business & Governance (21–23)

## 21) Change Control (ECR/ECO/Deviation/Waiver)

**Purpose**: Control changes after baselines to prevent scope and quality drift, while preserving traceability.

**Definition of Done**: Each change includes impact analysis, approvals, updated artifacts and baselines, a verification plan, and a communication record.

**Fields**

- Change ID (title)
- Type (select: ECR – request, ECO – order, Deviation, Waiver)
- Affected Items (relations: Requirements, ICDs, ADRs, BOM items, Tests, Releases, Baselines)
- Reason/Problem Statement (text)
- Impact Analysis
    - Multi-select: Safety, Quality, Cost, Schedule, Compliance
    - Notes (text)
- Risk Level (select: Low, Medium, High)
- Proposed Change (text)
- Verification Needed (relation or links to Tests/Procedures)
- Approvals (people)
- Approval Date(s) (date)
- Status (select: Proposed, Under Review, Approved, Implemented, Verified, Closed)
- Effective Version/Date (text/date)
- Backout/Rollback Plan (text)
- Communications Done (checkbox)
- Comms Link (url or relation to announcement/runbook)

**CSV Starter**

```
Change ID,Type,Affected Items,Reason/Problem Statement,Impact Analysis,Risk Level,Proposed Change,Verification Needed,Approvals,Status,Effective Version/Date,Backout/Rollback Plan,Communications Done
ECR-0001,ECR,"R-F-002; ICD:Primary Bus","Display glitches in sun","Quality; Schedule","Medium","Switch to high-nit panel; update ICD","T-012 daylight readability; T-013 thermal soak","PM; Tech Lead","Under Review",,"Revert to prior panel; ICD v1.2","FALSE"

```

**SOP**

1. Submit an **ECR** with a clear reason and affected items. Attach evidence (defects, test results).
2. Perform **impact analysis** (cost, schedule, quality, safety, compliance). Assign a risk level and list impacted stakeholders.
3. Run a review (can be a solo + 1 reviewer board). Record the decision: Approve, Reject, or Revise.
4. If approved, convert to **ECO** and update artifacts (ICD, drawings, code, BOM). Re-baseline if needed.
5. Link required tests and execute verification. Attach evidence.
6. Communicate to downstream consumers. Update runbooks. Mark **Communications Done**.
7. Close only when implemented and verified. Capture lessons in a knowledge base (optional).

**Gates**

- **Entrance**: Problem statement + evidence + affected artifacts listed.
- **Exit**: Baseline updated. Verification passed. Rollback plan documented. Stakeholders notified.

**Relations**: Requirements, ICDs, ADRs, BOM, Tests, Releases, Baselines, Runbooks.

---

## 22) Budget & Cost Model (NRE, Unit Economics, Forecast)

**Purpose**: Keep feasibility grounded. Track NRE, CapEx/OpEx, unit cost, margins, and variance vs plan.

**Definition of Done**: A baseline budget exists, a live forecast is maintained, and unit economics are validated at CDR and PRR.

**Fields**

- Line Item (title)
- Category (select: NRE, CapEx, OpEx, Unit BOM, Tooling, Test, Travel, Contingency)
- Project/Phase (select: Idea, Planning, Build, V&V, Release, Ops)
- Amount – Planned (number, currency)
- Amount – Actual (number, currency)
- Variance (formula: Actual − Planned)
- Assumptions (text)
- Vendor/PO (text or relation to Procurement)
- Funding Source (select or text: self, angel, grant, internal)
- Unit Cost Model (relation to “Unit Economics” DB, or inline fields below)
- Last Updated (date)

**Optional Unit Cost Fields** (same DB or a related “Unit Economics” DB)

- Target MSRP (number)
- Target Margin % (number)
- Target Unit Cost (number)
- BOM Cost (rollup from BOM)
- Assembly Labor (number)
- Overhead/Allocated (number)
- Current Estimated Unit Cost (formula)
- Delta vs Target (formula)

**CSV Starter**

```
Line Item,Category,Project/Phase,Amount – Planned,Amount – Actual,Assumptions,Vendor/PO,Funding Source,Last Updated
Prototype PCBs,NRE,Build,600,0,"Qty 10, 4-layer, std lead","JLC-PO-1023",Self,2025-01-10
Displays (10x),Unit BOM,Build,350,0,"$35 each","PO-1004",Self,2025-01-10
Enclosure Tooling,Tooling,Build,1200,0,"Single-cavity, 3D print pilot","Vendor TBD",Self,2025-01-10

```

**SOP**

1. Baseline the budget at PDR. Include NRE, materials, and a contingency (10–20% is typical).
2. Forecast monthly. Link Procurement POs. Update actuals and variance.
3. At CDR, validate unit economics (target unit cost vs BOM + labor + overhead).
4. At PRR, confirm burn vs plan and document funding coverage for the next phase.
5. When scope changes via ECO, update the budget and unit economics. Record the delta and rationale.

**Gates**

- **CDR Exit**: Unit cost within target ±X%. Contingency ≥ threshold. Funding secured.
- **PRR Exit**: Variance within tolerance. Re-forecast approved. Release fully costed.

**Relations**: Procurement, BOM, Releases, Projects, Change Control.

---

## 23) Go-To-Market (GTM) & Stakeholder Communications

**Purpose**: Ensure adoption with clear value propositions, launch assets, and feedback loops for users, stakeholders, support, and ops.

**Definition of Done**: Persona map, messaging, assets, launch checklist, success metrics, and a post-launch review are in place.

**Fields**

- Campaign/Launch Name (title)
- Audience Persona (multi-select: End User, Exec/VC, Ops/Support, Integrator, QA/Compliance)
- Core Message / Value Prop (text)
- Proof/Evidence (links: test data, demos, case studies)
- Channels (multi-select: Email, Deck, README/Docs, Video, Blog, In-App, Social)
- Assets (relations/links: Owner’s Guide, Deck, One-Pager, Demo Script, FAQ)
- Launch Date / Window (date)
- Success Metrics
    - Multi-select: Adoption, Activation, Retention, NPS, MTTR
    - Targets (text)
- Risks/Dependencies (text)
- Owner (person)
- Status (select: Planned, Ready, Launched, Closed)
- Post-Launch Review (text; link defects/feedback)

**CSV Starter**

```
Campaign/Launch Name,Audience Persona,Core Message / Value Prop,Proof/Evidence,Channels,Assets,Launch Date / Window,Success Metrics,Risks/Dependencies,Owner,Status
Rev A Launch,"End User; Exec/VC","Trustworthy telemetry with simple install","/verif-report.pdf; /[demo-video.mp](http://demo-video.mp)4","Deck; Docs; Video; Blog","/[owners-guide.md](http://owners-guide.md); /one-pager.pdf; /pitch-deck.pptx",2025-02-20,"Adoption; Activation","Supply for displays; firmware freeze","Kian","Planned"

```

**SOP**

1. Build a persona map. For each audience, define jobs-to-be-done, objections, and win conditions.
2. Write the message and attach proof: verification plots, demos, and case studies.
3. Produce the core assets: Owner’s Guide, one-pager, deck, demo script, FAQ. Assign owners.
4. Plan channels and calendar. Align with the release version and runbooks. Dry-run the demo.
5. Launch and monitor success metrics. Route issues into Defects. Collect feedback.
6. Run a post-launch review. Update assets. Feed learning into Requirements and ADRs for Rev B.

**Gates**

- **PRR Entrance**: Assets ready. Demo rehearsed. Success metrics and targets set.
- **Launch Exit**: Metrics captured. Issues logged. Stakeholder comms complete. Post-launch review done.

**Relations**: Releases, Owner’s Guide/Docs, Tests (evidence), Defects, Projects.

---

## Cross-links to add (wire once)

- **Change Control** ↔ Requirements, ICDs, ADRs, BOM, Tests, Releases, Baselines.
- **Budget & Cost Model** ↔ Procurement, BOM, Releases, Projects, Change Control.
- **GTM & Stakeholder Comms** ↔ Releases, Docs (Owner’s Guide/FAQ), Tests (evidence), Defects.
