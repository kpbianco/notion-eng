# Engineering OS — Operations & Governance (24–30) (Marketplace Draft)

### What this page is

A marketplace-ready, Notion-native spec for **Operations & Governance (24–30)** inside an Engineering OS.

Each section is intended to become a dedicated database (or page + linked database), and includes:

- **Purpose** and **Definition of Done**
- Suggested **Fields** (schema)
- A **CSV Starter** for quick import
- A pragmatic **SOP** and **Gates**
- **Relations** to keep execution traceable end-to-end

### How to use

1. Treat each section (24–30) as its own database.
2. Create the database using the **Fields** list.
3. Optional: copy the **CSV Starter** into a `.csv` and import it.
4. Wire the **Relations** at the end once, then reuse across projects.

---

## Engineering OS — Operations & Governance (24–30)

## 24) Procurement & Supply Chain

**Purpose**: Source the right parts and services at the right cost and lead time, with alternates and traceability.

**Definition of Done**: RFQs compared, supplier selected, PO issued, tracking active, receipts logged, and links to BOM and budget updated.

**Fields**

- PO ID (title)
- Item / Spec / PN (text; link to BOM item)
- Supplier (relation to “Suppliers” DB)
- Status (select: Draft, RFQ, Ordered, Shipped, Received, Closed)
- Qty (number)
- Unit Cost (currency)
- Extended Cost (formula)
- Lead Time (text)
- MOQ / NCNR (text)
- Alt Sources (text or relations)
- Incoterms/Ship Method (text)
- Expected Receipt (date)
- Tracking / Link (url)
- Received Date (date)
- Receiver / Inspection Lot (relation)
- Notes / Risks (text)

**CSV Starter**

```
PO ID,Item / Spec / PN,Supplier,Status,Qty,Unit Cost,Lead Time,MOQ / NCNR,Alt Sources,Incoterms/Ship Method,Expected Receipt,Tracking / Link,Received Date,Receiver / Inspection Lot,Notes / Risks
PO-0001,"Display, 2.4in, SPI, 400nit",Vendor A,Ordered,10,34.50,"2 wks","MOQ 5; NCNR","Vendor B; Vendor C","DAP; DHL",2025-02-05,[https://tracking.example](https://tracking.example),,,

```

**SOP**

1. RFQ to ≥2 suppliers for critical items. Capture lead time and terms.
2. Compare total landed cost and risk. Choose a primary and an alternate.
3. Issue PO with spec and revision. Link to BOM and budget.
4. Track shipment and keep ETA current.
5. Receive and create an incoming inspection lot. Resolve NCRs.
6. Close PO and update actuals. Record supplier performance notes.

**Gates**

- **Build start**: All critical-path POs placed. Alternates identified.
- **Assembly start**: Critical lots received and dispositioned.

**Relations**: BOM, Budget, Suppliers, Incoming Inspection, Change Control, Schedule.

---

## 25) Supplier Quality & Incoming Inspection

**Purpose**: Ensure received parts meet spec. Track supplier performance and corrective actions.

**Definition of Done**: Every receipt has an inspection record (plan, sample, results) and disposition. Supplier scorecards are maintained.

**Fields (Suppliers)**

- Supplier (title)
- Type (select: Distributor, CM, ODM, Service)
- Approved (checkbox)
- Score – OTD (number)
- Score – Quality (number)
- Audits / Notes (text)
- Contacts / Agreements (files/links)

**Fields (Incoming Inspection Lots)**

- Lot ID (title)
- PO ID (relation)
- Part Number (relation to BOM)
- Supplier (relation)
- Qty Received (number)
- Sample Size / Plan (text)
- Checks / Measurements (text/files)
- Result (select: Pass, Fail)
- NCR # (text)
- Disposition (select: Use as-is, Rework, Return, Scrap)
- CAPA Actions (text; relation to Defects/CAPA)
- Inspector (person)
- Date (date)

**CSV Starter (Lots)**

```
Lot ID,PO ID,Part Number,Supplier,Qty Received,Sample Size / Plan,Checks / Measurements,Result,NCR #,Disposition,CAPA Actions,Inspector / Date
LOT-102,PO-0001,DISP-2.4-SPI,Vendor A,10,"AQL 1.0; n=3","Luminance; SPI ID; Pixel test",Pass,,Use as-is,,2025-02-05

```

**SOP**

1. Define inspection plans by part criticality (visual, dimensional, functional).
2. Receive and quarantine. Inspect per plan. Attach evidence.
3. If failed, issue an NCR. Set disposition. Raise CAPA.
4. Score suppliers monthly (OTD and quality). Update approval status.

**Gates**

- **Approved supplier** required before PO for critical parts.
- **Lot release** only after pass or explicit disposition is recorded.

**Relations**: Procurement/POs, BOM, Defects/CAPA, Budget, Risk Register.

---

## 26) Security, Privacy & Safety (Threats, SBOM, Hazards)

**Purpose**: Identify and mitigate product risks across security, privacy/data handling, and physical safety.

**Definition of Done**: Asset and data map, threat model, SBOM, hazard analysis, mitigations, and verification evidence are baselined at release.

**Fields**

- Risk Item (title)
- Category (select: Security, Privacy, Safety)
- Asset/Data/Hazard (text)
- Context/Assumptions (text)
- Threat/Hazard Method (select/text: STRIDE, FMEA, STPA, etc.)
- Severity (select: Low, Medium, High, Catastrophic)
- Likelihood (select: Low, Medium, High)
- Risk Rating (formula)
- Controls/Mitigations (text)
- Verification (links to tests/reports)
- Owner (person)
- Due (date)
- Residual Risk (text; accept/transfer/mitigate)
- SBOM Link (url/file)
- Status (select: Open, Mitigated, Accepted, Closed)

**CSV Starter**

```
Risk Item,Category,Asset/Data/Hazard,Context/Assumptions,Threat/Hazard Method,Severity,Likelihood,Controls/Mitigations,Verification,Owner / Due,Residual Risk,SBOM Link,Status
Unauthorized data access,Security,"Logs; user IDs","Local storage","STRIDE",High,Med,"Encrypt at rest; access control","Pen test report; unit test",Owner/2025-02-15,"Low (accepted)",[https://repo/sbom.json,Mitigated,Open,Open](https://repo/sbom.json,Mitigated,Open,Open)
Thermal burn,Safety,"Enclosure hot surface","Max 60C cabin","FMEA",Med,Low,"Derate load; vents; warning in guide","Thermal soak test",Owner/2025-02-20,"Very Low",,Open

```

**SOP**

1. Build an asset and data map. Classify sensitivity.
2. Run a threat model (STRIDE) and produce an SBOM. Scan dependencies.
3. Run safety analysis (FMEA/DFMEA/HAZOP). Define controls and labels.
4. Verify mitigations (tests and scans). Record residual risk and sign-off.
5. Track vulns and hazards. Feed into Change Control and Releases.

**Gates**

- **Release**: SBOM published. Critical vulns triaged. Safety controls verified. Privacy notice documented.

**Relations**: Requirements (security/safety), Tests, Releases, Docs/Owner’s Guide, Change Control, Risk Register.

---

## 27) Release & Configuration Management

**Purpose**: Ship reproducible versions with frozen baselines, clear notes, and rollback.

**Definition of Done**: Versioned release includes artifacts, change list (ECOs), verification evidence, instructions, and a rollback plan.

**Fields**

- Release ID / Version (title)
- Date (date)
- Scope / Highlights (text)
- Included Changes (relations to ECR/ECO/Defects)
- Baselines (ICD vX, Drawings vY, Firmware tag, BOM rev)
- Artifacts (files/urls: binaries, Gerbers, STLs, docs)
- Checklists (Pre-Release, Release, Post-Release)
- Verification Evidence (links to tests/reports)
- Rollback Plan (text)
- Approvals (people)
- Status (select: Planned, Released, Deprecated)

**CSV Starter**

```
Release ID / Version,Date,Scope / Highlights,Included Changes,Baselines,Artifacts,Checklists,Verification Evidence,Rollback Plan,Approvals,Status
RevA-1.0,2025-03-01,"Initial GA","ECO-12; DEF-44 closed","ICD v1.2; BOM r3; FW v1.0","/artifacts/[gerbers.zip](http://gerbers.zip); /fw/fw_1.0.bin; /owners_guide.pdf","/checklists/[release.md](http://release.md)","/reports/verif_revA.pdf","Revert to RevA-rc4; notify users","PM; Tech Lead",Released

```

**SOP**

1. Document branch/tag strategy. Freeze scope. Bump version.
2. Run the release checklist. Collect artifacts and evidence. Update baselines.
3. Publish artifacts and notes. Execute comms. Update ops runbooks.
4. Monitor metrics and defects. Decide hotfix vs next minor.

**Gates**

- **PRR**: Checklists complete. Artifacts reproducible. Rollback defined.
- **Post-release**: Issues triaged. Metrics reviewed. Deprecations planned.

**Relations**: Change Control, Tests, Docs, GTM, Ops/Runbooks, Budget, Security/SBOM.

---

## 28) Operations, Support & Incident Response

**Purpose**: Keep the product reliable post-release and make response predictable.

**Definition of Done**: Runbooks, SLOs and alerts, escalation path, incident process, and postmortems are defined and used.

**Fields (Runbooks)**

- Runbook ID (title)
- Service/Subsystem (text)
- Start/Stop/Deploy Procedures (text)
- Dependencies (text/relations)
- SLOs/SLAs (text)
- Health Checks/Monitors (text)
- Escalation (contacts/hours)
- Known Issues / Workarounds (text)
- Last Test (date)

**Fields (Incidents)**

- Incident ID (title)
- Severity (select: SEV1, SEV2, SEV3, SEV4)
- Start (date/time)
- End (date/time)
- Impact / Symptom (text)
- Root Cause (text)
- Fix Applied (text)
- Follow-ups (tasks/owners/dates)
- Status (select: Open, Monitoring, Closed)
- Links (release, defects, metrics)

**CSV Starter (Incidents)**

```
Incident ID,Severity,Start,End,Impact / Symptom,Root Cause,Fix Applied,Follow-ups,Status,Links
INC-0007,SEV2,"2025-03-10 10:22","2025-03-10 11:05","Logging stops intermittently","SD write contention","Buffered writes + retry","Add watchdog test; doc known issue",Closed,"Rel RevA-1.0; DEF-77"

```

**SOP**

1. Write runbooks for normal operations and emergency procedures.
2. Define SLOs and map monitors directly to SLOs.
3. Define on-call coverage (solo still means defined hours and escalation).
4. Handle incidents: declare, mitigate, record, and write a postmortem within 72 hours.
5. Feed learnings into Requirements, ECOs, and test coverage.

**Gates**

- **Before GA**: Runbooks, SLOs, and monitors exist. Dry-run an incident.
- **Close incident**: Root cause found. Follow-ups assigned and tracked.

**Relations**: Releases, Defects, Tests, Docs/Runbooks, Metrics, Change Control.

---

## 29) Metrics, Analytics & Experimentation

**Purpose**: Make decisions with data (adoption, reliability, efficiency) and test changes safely.

**Definition of Done**: North-star plus supporting metrics defined, pipeline documented, dashboards live, experiments logged with decisions.

**Fields (Metrics)**

- Metric (title)
- Type (select: Leading, Lagging)
- Definition (exact formula)
- Source (select/text: log, DB, survey)
- Owner (person)
- Target (number/threshold)
- Cadence (select: Daily, Weekly, Release)
- Dashboard Link (url)

**Fields (Experiments)**

- Experiment ID (title)
- Hypothesis (text)
- Variant(s) (text)
- Primary Metric (relation)
- Guardrails (relations)
- Exposure / Duration (text)
- Result (select: Win, Loss, Inconclusive)
- Decision (select: Ship, Hold, Revisit)
- Notes (text)

**CSV Starter (Metrics)**

```
Metric,Type,Definition,Source,Owner,Target,Cadence,Dashboard Link
Activation Rate,Leading,"Activated/Signups","App telemetry",Owner,0.40,Weekly,[https://dash/activation](https://dash/activation)
MTTR,Lagging,"Mean time to restore (mins)","Incident DB",Owner,30,Monthly,[https://dash/ops](https://dash/ops)

```

**SOP**

1. Define a north-star metric and 3–5 supporting metrics. Write exact formulas.
2. Instrument collection and validate accuracy. Respect privacy.
3. Maintain dashboards on a cadence. Assign owners.
4. Pre-register experiments with hypothesis and metrics. Run, decide, and document.
5. Close the loop: changes → metrics → roadmap updates.

**Gates**

- **Pre-launch**: Minimum metric set is live and validated.
- **Post-launch**: Weekly metric review. Experiments gated on guardrails.

**Relations**: Requirements, Releases, Ops/Incidents, GTM, Security/Privacy.

---

## 30) IP, Legal & Compliance

**Purpose**: Protect IP, honor licenses, and meet regulatory obligations (labels, testing, export, privacy).

**Definition of Done**: IP log, OSS compliance (SBOM + notices), regulatory plan/tests, privacy posture, and export classification are maintained and auditable.

**Fields**

- Item (title)
- Category (select: Patent, Trademark, Copyright, OSS License, Regulatory, Export, Data Privacy)
- Description (text)
- Jurisdiction / Standard (text: USPTO, CE/FCC/UL, ISO, GDPR, CCPA, EAR/ITAR)
- Status (select: Draft, Filed, Approved, Compliant, Not Required)
- Evidence/Links (files/urls)
- Counsel/Contact (text)
- Deadlines/Expiry (date)
- Impacted Artifacts (relations: Releases, Docs, BOM)
- Notes / Obligations (text)

**CSV Starter**

```
Item,Category,Description,Jurisdiction / Standard,Status,Evidence/Links,Counsel/Contact,Deadlines/Expiry,Impacted Artifacts,Notes / Obligations
Product Name,Trademark,"Word mark class 009",USPTO,Draft,,Law Firm TBD,2025-06-01,"RevA-1.0","Clearance search before launch"
Open Source Notices,OSS License,"Notices for bundled libs",SBOM/Notices,Compliant,[https://repo/sbom.json,,,"RevA-1.0](https://repo/sbom.json,,,"RevA-1.0); Docs","Include NOTICE file in distro"
EMC/Radio,Regulatory,"Unintentional radiator test",FCC Part 15,Planned,,Test Lab TBD,2025-05-15,"Hardware RevA","Labeling and user manual statements"

```

**SOP**

1. Run an IP sweep at PDR and CDR. Record patentable items. Run trademark clearance.
2. Maintain OSS compliance: SBOM, license checks, notices, and attributions.
3. Build the regulatory plan (EMC, safety, radio, medical, etc.). Schedule lab testing and archive reports.
4. Privacy: data map, notices, request handling process, retention policy.
5. Export: classify product, restrict where needed, record ECCN.

**Gates**

- **PRR**: OSS and labeling obligations met. Regulatory plan scheduled.
- **Release**: Required labels and manual text included. Compliance reports archived.

**Relations**: Security/SBOM, Releases, Docs, Procurement (licenses), GTM, Risk Register.

---

## Cross-links to add (wire once)

- **Procurement** ↔ BOM, Budget, Suppliers, Inspection, Schedule.
- **Supplier Quality** ↔ Procurement, BOM, Defects/CAPA, Risk.
- **Security/Privacy/Safety** ↔ Requirements, Tests, Releases, Docs, IP/Compliance.
- **Release & Config** ↔ Change Control, Tests, Docs, GTM, Ops.
- **Ops & Incidents** ↔ Releases, Metrics, Runbooks, Defects.
- **Metrics & Experiments** ↔ Requirements, Releases, Ops, GTM.
- **IP/Legal/Compliance** ↔ Security/SBOM, Docs, Releases, Procurement.