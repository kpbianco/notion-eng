# Engineering OS — Reliability & Safety (Marketplace Draft)

### What this page is

A marketplace-ready, Notion-native **Reliability & Safety** spec for an Engineering OS.

It is designed to be implemented as a set of databases (or page + linked DBs). Each section includes:

- **Purpose** and **Definition of Done**
- Suggested **Fields** (schema)
- A **CSV Starter** for quick import
- A pragmatic **SOP** and **Gates**
- **Relations** so safety and reliability stay tied to requirements, tests, releases, and operations

### How to use

1. Treat each section (F1–F8 + the checklists) as its own database.
2. Create the database using the **Fields** list.
3. Optional: copy the **CSV Starter** into a `.csv` and import it.
4. Use the R/A/G gates as review criteria before release.

---

## F) Reliability & Safety

## F1) Hazard Analysis & Safety Goals (HARA-lite)

**Purpose**: Identify hazards, assess risk (severity × exposure × controllability), and set safety goals.

**Definition of Done**: Hazards listed. Risk ranked. Safety goals and top-level safety requirements defined. Owners assigned.

**Fields**

- Hazard (text)
- Context/Mode (when it arises)
- Severity (S1–S3)
- Exposure (E1–E3)
- Controllability (C1–C3)
- Risk Priority (calc/score)
- Safety Goal (text)
- Safety Requirement(s) (IDs)
- Owner
- Status (Open/Mitigated/Accepted)
- Evidence

**CSV Starter**

```
Hazard,Context,Severity,Exposure,Controllability,Risk Priority,Safety Goal,Safety Requirements,Owner,Status,Evidence
Loss of display,"High temp cabin",S2,E2,C2,Med,"Must alert or fail-safe","SR-01 audible alert; SR-02 fallback LED",Alex,Open,link

```

**SOP**

1. List operating contexts (startup, normal, extreme, shutdown).
2. Brainstorm hazards. Assign S/E/C and compute risk.
3. Define safety goals for High and Medium risks. Derive safety requirements.
4. Assign owners and link to verification.

**Gates**

- **Entrance**: Requirements draft.
- **Exit**: All High and Medium risks mapped to safety goals and requirements.

**Relations**: Requirements, Fault Injection, Test Evidence, Change Control.

**Hobby vs Product**

- **Hobby minimum**: One table of top hazards with simple mitigations.
- **Product grade**: Formal HARA scoring with sign-offs and traceability to tests and release gates.

---

## F2) FMEA (Failure Modes & Effects Analysis)

**Purpose**: Anticipate how parts and functions can fail and prevent the most critical ones.

**Definition of Done**: Functions/components listed. Failure modes, causes, effects, and controls documented. Priority (RPN or equivalent) drives actions.

**Fields**

- Item/Function
- Failure Mode
- Cause
- Effect
- Severity (1–10)
- Occurrence (1–10)
- Detection (1–10)
- RPN (=S×O×D) or Priority
- Current Controls
- Recommended Action
- Owner/Date
- Status

**CSV Starter**

```
Item,FailureMode,Cause,Effect,Severity,Occurrence,Detection,RPN,CurrentControls,Action,Owner,Status
Buck reg,Overheat,Derating too low,Device resets,8,3,4,96,Thermal pad,"Increase copper; temp cutback",Alex,Open

```

**SOP**

1. List items/functions. Brainstorm failure modes.
2. Fill S/O/D. Compute RPN. Sort by priority.
3. Define actions (design/process/test) and track to closure.

**Gates**

- **Entrance**: Architecture frozen.
- **Exit**: Top risks mitigated or accepted with rationale.

**Relations**: Derating, Reliability Testing, Change Control.

**Hobby vs Product**

- **Hobby minimum**: Top 10 rows with actions.
- **Product grade**: Full FMEA per subsystem, periodic reviews, gated actions before release.

---

## F3) Component Derating & Stress Analysis

**Purpose**: Ensure components operate within safe margins across temperature, voltage, and current.

**Definition of Done**: Worst-case conditions identified. Derating rules applied. Stress is within allowed margin. Exceptions documented.

**Fields**

- Component (PN)
- Parameter (V/I/P/T)
- Worst-Case Value
- Rating
- Derating Rule (e.g., 50% electrolytic ripple)
- Margin (%)
- Pass/Fail
- Action/Note

**CSV Starter**

```
Component,Parameter,Worst-Case,Rating,Rule,Margin,Pass/Fail,Action
Electrolytic cap,Temp,60°C,105°C,"<=70% rating",57%,Pass,—

```

**SOP**

1. Define worst-case conditions (Tmin/Tmax, load, supply tolerance).
2. Apply derating rules per component class.
3. Compute margins and implement layout/heatsinking changes as needed.
4. Log exceptions and track via ECO.

**Gates**

- **Entrance**: Power/thermal model.
- **Exit**: All critical parts meet derating targets or have an ECO plan.

**Relations**: Thermal, BOM, FMEA, Environmental Tests.

**Hobby vs Product**

- **Hobby minimum**: Check big-ticket parts (regulators, caps, displays).
- **Product grade**: Full spreadsheet with rules by class, cross-checked with thermal and chamber data.

---

## F4) Fault Injection & Safe State Plan

**Purpose**: Prove the system fails safely under realistic faults.

**Definition of Done**: Fault list defined. Injection methods scripted. Safe-state behavior verified with evidence.

**Fields**

- Fault (what)
- Injection Method (how)
- Expected Safe State
- Monitor/Detection
- Pass Criteria
- Evidence
- Status

**CSV Starter**

```
Fault,Injection,Expected Safe State,Detection,Pass Criteria,Evidence,Status
Brownout,"PSU dip to 8V","Graceful shutdown; no data loss","Voltage monitor","No crash; log flush",video_link,Pass

```

**SOP**

1. List faults (power dips, comm loss, sensor stuck, over-temp).
2. Define safe state and detection. Script injection.
3. Run tests, capture evidence, file ECOs as needed.

**Gates**

- **Entrance**: System bench-ready.
- **Exit**: All critical faults demonstrate safe behavior.

**Relations**: HARA, Diagnostics, Test Evidence.

**Hobby vs Product**

- **Hobby minimum**: Manually try 3–5 likely faults.
- **Product grade**: Automated campaign with coverage metrics and release gating.

---

## F5) Diagnostics & Coverage (Detect/Report/Recover)

**Purpose**: Ensure critical faults are detected and acted upon.

**Definition of Done**: Diagnostic monitors defined. Thresholds and actions set. Coverage measured.

**Fields**

- Monitor (what)
- Threshold/Rule
- Action (alert/shutdown/fallback)
- Coverage Target (%)
- Test Reference
- Status

**CSV Starter**

```
Monitor,Threshold,Action,CoverageTarget,TestRef,Status
Temp,>70°C,"Throttle update rate",95%,FI-04,Open

```

**SOP**

1. Define monitors for critical metrics and set thresholds.
2. Define actions and user feedback.
3. Measure coverage via fault injection. Iterate until target met.

**Gates**

- **Entrance**: Fault list available.
- **Exit**: Coverage target met. Docs updated.

**Relations**: Fault Injection, Owner’s Guide, Runbook.

**Hobby vs Product**

- **Hobby minimum**: A few checks with simple alerts.
- **Product grade**: Comprehensive monitors with metric-based coverage and tests.

---

## F6) Environmental & Reliability Plan (ALT/HALT-lite)

**Purpose**: Validate reliability across temperature, vibration, humidity, ESD, and time.

**Definition of Done**: Profiles and acceptance criteria set. Tests executed. Failures analyzed and addressed.

**Fields**

- Stress Type (temp/vibe/humidity/ESD/soak)
- Profile (range, duration)
- Acceptance Criteria
- Failures
- Corrective Action (ECO)
- Status

**CSV Starter**

```
Stress,Profile,Criteria,Failures,Action,Status
Vibration,"5–200 Hz 1 hr/axis","No resets; conn intact",Loose header,"Locking connector",Open

```

**SOP**

1. Define profiles that reflect real use plus margin.
2. Execute tests and log telemetry and failures.
3. Run FA/5-Whys. File ECOs. Retest.

**Gates**

- **Entrance**: Assembly stable.
- **Exit**: P0/P1 reliability issues resolved or deferred with rationale.

**Relations**: Derating, FMEA, Change Control.

**Hobby vs Product**

- **Hobby minimum**: Simple soak plus temperature spot checks.
- **Product grade**: Structured plan with FA loop and documentation.

---

## F7) Safety Case & Evidence Bundle

**Purpose**: Make a concise, evidence-backed argument that the product is acceptably safe.

**Definition of Done**: Safety goals, mitigations, test evidence, and residual risks compiled with sign-offs.

**Fields**

- Safety Goal (ID/text)
- Mitigations (links)
- Tests & Results
- Residual Risks
- Sign-off (name/date)

**CSV Starter**

```
Goal,Mitigations,Tests,Residual Risks,Sign-off
No dangerous fault,"FMEA actions; diagnostics","FI-01..05: Pass","Single transient reset risk","Lead 2026-01-10"

```

**SOP**

1. Summarize goals and mitigations.
2. Link tests and results and list residual risks.
3. Obtain sign-offs and store with the release.

**Gates**

- **Entrance**: All F-tests done.
- **Exit**: Safety case approved for release.

**Relations**: Test Evidence, HARA, Change Control.

**Hobby vs Product**

- **Hobby minimum**: One-page summary with links to tests.
- **Product grade**: Structured reviewed bundle included in release checklist.

---

## F8) Field Monitoring & Feedback Loop

**Purpose**: Capture real-world failures and improve future revisions.

**Definition of Done**: Telemetry or feedback channel exists. Issues triaged. Fixes looped into the roadmap.

**Fields**

- Source (support/telemetry/forum)
- Issue Summary
- Severity (P0–P3)
- Repro Rate
- Owner
- Fix/Decision
- Release Tag

**CSV Starter**

```
Source,Issue,Severity,Repro,Owner,Decision,Release
Telemetry,"Occasional reset",P2,"1/200h",Alex,"Fix in 1.1",r1.1

```

**SOP**

1. Define intake and severity tagging.
2. Analyze clusters and route into ECOs and roadmap.
3. Communicate fixes in release notes.

**Gates**

- **Entrance**: Initial release shipped.
- **Exit**: Feedback reviewed on cadence and actions tracked.

**Relations**: Ops/Runbook, Releases, Issues.

**Hobby vs Product**

- **Hobby minimum**: Personal log of issues and ad-hoc fixes.
- **Product grade**: Formal intake, triage SLA, tracked fixes by release.

---

## Configuration Management Plan (CM) — Checklist

**Purpose**: Single source of truth, reproducible builds, traceable changes.

**Definition of Done**: Repo layout, naming, baseline and release registers, SOP, and an as-built pack for the latest release, verified by a dry-run rebuild.

**Fields (Notion DBs)**

- **Baselines DB**: Baseline ID, Artifacts, Rationale, Approver, Date, Tag/Hash, Links
- **Releases DB**: Release Tag, Purpose, Baselines, Build Hash/Binaries, Evidence, Approver, Date, Pack Link

**CSV starters**

```
Baselines:
BaselineID,Artifacts,Rationale,Approver,Date,Tag/Hash,Notes
BR-A1,"Reqs_vA1;ICD_vA1;BOM_vA1;TestPlan_vA1","Rev A freeze","Owner",2025-12-28,git:abc1234,

Releases:
ReleaseTag,Purpose,Baselines,BuildHash/Binaries,Evidence,Approver,Date,PackLink
Rel-A1.0,"First usable A","BR-A1","fw.bin (git:def5678)","/test/Report_A1.pdf","Owner",2026-01-02,/release/[Rel-A1.0.zip](http://Rel-A1.0.zip)

```

**SOP**

1. Propose change via PR. Reference impacted artifacts/IDs.
2. Review and merge. Update affected docs with new minor versions.
3. When the architecture and doc set stabilizes, create a baseline (freeze IDs/versions).
4. When tested and shippable, tag a release (Rel-X.Y) and build an as-built pack.
5. Store the pack, update the release register, and verify reproducibility.
6. Communicate release notes and archive evidence.

**Gates**

- **Entrance**: Repo layout and naming in place.
- **Exit**: Reproducible release with manifest and evidence. Baselines recorded.

**R/A/G Gate**

- **Green**: Baseline and release registers exist and last release is reproducible.
- **Amber**: Registers exist but last release missing one artifact.
- **Red**: No registers or no reproducible release.

**Relations**: Requirements, ICDs, Test Reports, Trace Matrix, BOM, Firmware, Releases.

**Hobby vs Product**

- **Hobby**: Manual zip, one approver, Drive backup.
- **Product**: Signed tags, CI artifact store, retention/backups, formal approvals, immutable evidence.

---

## Calibration & Metrology — Checklist

**Purpose**: Ensure measurements are accurate enough for decisions. Record offsets and due dates.

**Definition of Done**: For each critical measurand, there is a passing, dated calibration record, applied correction, a label on device, and a scheduled next due.

**Fields**

- Unit ID
- Sensor/Instrument
- Range
- Importance (Critical/Info)
- Reference (Model/SN/Cert)
- Points
- Criteria
- Error/Offset
- Uncertainty
- Pass/Fail
- Cal Date
- Next Due
- Technician
- Evidence Link

**CSV Starter**

```
UnitID,Sensor,Range,Importance,Reference,Points,Criteria,AvgError,Offset,Uncertainty,Pass/Fail,CalDate,NextDue,By,Evidence
U-023,OilPressure,0-700kPa,Critical,"Gauge 0.1% SN123 (valid to 2026-03)","0/100/300/500/700","±2%",+0.8%,-1.9kPa,±0.5%,PASS,2025-12-28,2026-06-28,AB,/evidence/cal/U-023.pdf

```

**SOP**

1. Identify critical sensors and instruments. Set intervals.
2. Verify reference validity. Warm up and stabilize the environment.
3. Execute calibration and compute offsets and uncertainty.
4. Apply corrections in config/firmware and verify.
5. Record results, label devices, schedule next due, archive evidence.

**Gates**

- **Entrance**: Sensor list, criteria, and reference ready.
- **Exit**: Record saved, corrections applied, label placed, next due set.

**R/A/G Gate**

- **Green**: All critical sensors in date with passing records.
- **Amber**: One item due within 14 days and plan scheduled.
- **Red**: Any critical sensor expired or failed without mitigation.

**Relations**: Test Plan, Trace Matrix, Releases, Ops.

**Hobby vs Product**

- **Hobby**: Golden unit and simple offset record.
- **Product**: Lab certs, uncertainty budget, enforced due dates, NCR/CAPA for failures.