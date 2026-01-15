# Engineering OS — Compliance, Safety & Ethics (Marketplace Draft)

### What this page is

A practical, builder-friendly **compliance, safety, and ethics** layer for engineering projects.

It is designed to help you avoid building something:

- Illegal
- Unsafe
- Ethically irresponsible

…and to give you a realistic path from **hobby prototype** to **sellable product** without drowning in standards.

> This is **not legal advice**. When you are near regulated territory, you still use labs, compliance consultants, and attorneys. The goal here is to show up prepared.
> 

---

## 10‑Minute Quickstart (do this before you build more)

Create a Notion page called **Compliance Snapshot** and answer:

1. Where will it be used? (home / vehicle / industrial / medical-like / outdoors)
2. What energy hazards exist? (mains, Li‑ion, heaters, motors, high current)
3. Does it radiate or transmit? (switching regulators, clocks, USB, Wi‑Fi/BLE, cellular, CAN)
4. Does it touch people or critical systems? (wearable, medical-ish, automotive control, safety interlocks)
5. Does it collect data? (PII, location, audio/video, telemetry tied to identity)

Then apply this rule:

- If **mains** OR **radio transmitter** OR **Li‑ion pack** OR **safety‑critical use** → treat compliance as a **Rev A gating risk**, not “later.”

---

## 1) Regulatory Roadmaps

**Scope**: FCC / CE / UKCA / UL, IEC 60601, ISO 26262.

### 1.1 Market access vs product safety

Most regulation falls into one of these buckets:

- EMC / radio (does not interfere, uses spectrum legally)
- Electrical safety (shock, fire, overheating)
- Functional safety (fails safely when electronics/software malfunction)
- Environmental (restricted substances + end of life)
- Privacy/security (increasingly required by customers/regions)

### 1.2 USA: FCC (quick orientation)

If you sell electronics in the US, FCC rules often apply even if you are not “wireless,” because digital electronics can be unintentional radiators (noise emissions). Unintentional radiators generally follow an authorization route such as Supplier’s Declaration of Conformity (SDoC) or Certification, depending on the device category.

Practical triggers:

- No intentional radio (no Wi‑Fi/BLE/cellular) → likely unintentional radiator path.
- Intentional radio → typically certification is involved (and module approvals matter).

What you do in Rev A:

- Decide: unintentional vs intentional radiator.
- Plan: pre‑compliance EMC sniff test + test lab path if selling.

### 1.3 EU: CE marking (EMC/LVD/RED)

CE marking is the manufacturer’s declaration that the product conforms to applicable EU harmonization legislation.

Typical electronics touch:

- EMC Directive
- LVD (electrical safety for certain voltage ranges)
- RED (radio equipment: Wi‑Fi/BLE/cellular/etc.)

Key idea: you usually do not “get CE certified” by a single authority. You build a Technical File and perform conformity assessment, sometimes involving a notified body depending on product/risk.

Document retention: for radio equipment, EU guidance expects technical documentation + declaration kept for ~10 years after placing on the market.

### 1.4 UK: UKCA (and CE acceptance reality check)

UKCA is the UK conformity marking for Great Britain, with timelines and acceptance rules that can vary by product category.

Builder rule: treat UKCA as “CE-like but UK‑specific documentation + marking requirements.” Do not assume your EU plan automatically covers the UK.

### 1.5 UL (and similar marks)

UL is commonly required by retailers, insurers, and buyers even when not explicitly mandated as law.

Builder lens: UL-type certification becomes relevant when you are:

- Plugging into mains
- Shipping to consumers
- Selling into corporate/industrial procurement

### 1.6 Medical-ish: IEC 60601 family

If your product becomes a medical electrical device/system, IEC 60601-1 and related standards become central. Even “wellness” products can drift into regulated territory depending on claims and intended use.

Practical rule: marketing claims can trigger medical device classification. If you are close, treat it as a hard gate and consult experts early.

### 1.7 Automotive functional safety: ISO 26262

ISO 26262 addresses hazards caused by malfunctioning behavior of E/E safety-related systems in road vehicles.

Builder rule: if your product can influence vehicle control/safety outcomes (braking, steering, powertrain control, ADAS inputs), you are in a different universe than a telemetry logger.

### 1.8 Regulatory decision tree (copy into your project)

Q1 — Where will this be sold/used? US / EU / UK / other

Q2 — Is there intentional radio? (Wi‑Fi/BLE/cellular/etc.)

Q3 — Does it connect to mains? (AC input, internal PSU)

Q4 — Safety critical? (harm possible due to malfunction)

Q5 — Medical claims? (diagnosis/therapy/monitoring claims)

Q6 — Environmental obligations? (RoHS/WEEE/REACH expectations)

Q7 — Data/Privacy? (PII/location/audio/video, user accounts)

Output:

- Applicable regimes (FCC / CE directives / UKCA / UL targets / ISO 26262 / IEC 60601)
- Evidence pack requirements (tests + docs + markings)
- Stop-the-line risks

---

## 2) Safety Fundamentals

**Scope**: hazard analysis, labeling, fusing, isolation, fail-safe defaults, interlocks.

### 2.1 Safety hierarchy (use this order)

1. Design it out (remove hazard)
2. Guard it (physical/electrical protection)
3. Detect + shut down safely
4. Warn + instruct (labels/manual)

Warnings alone are the weakest control.

### 2.2 Hazard analysis (builder-friendly)

Create a **Hazard Register** (10–30 rows is enough for most projects).

For each hazard:

- Hazard (shock/fire/burn/cut/chemical/pressure/entanglement/data harm)
- Cause
- Severity (1–5)
- Likelihood (1–5)
- Detectability (1–5)
- Mitigation(s)
- Verification test

Common hazard categories:

- Electrical shock (mains, exposed conductors)
- Fire (overcurrent, shorts, overheating, battery thermal runaway)
- Thermal burns (heaters, hot components)
- Mechanical injury (sharp edges, pinch points, spinning parts)
- Battery/chemical (Li‑ion handling, venting, swelling, electrolyte)
- Data harm (privacy breach, location exposure, unsafe logs)
- Misuse hazards (wrong supply/cable/install)

### 2.3 Fusing, protection, safe power behavior

Minimum safe power checklist (sellable baseline):

- Input protection (fuse or resettable protection where appropriate)
- Overcurrent protection strategy (at least one layer)
- Reverse polarity protection (if user-accessible power)
- Thermal protection (shutdown/derate) if heat can rise dangerously
- Brownout behavior defined (what happens during droop)
- Fail-safe default on boot (outputs start safe)

### 2.4 Isolation, barriers, and “don’t mix domains”

If you have:

- Mains + low voltage logic
- High current motor drivers + sensors
- Automotive power + USB to a laptop

…define isolation and grounding boundaries explicitly.

Builder rule: write down what “safe separation” means in your system before routing wires or designing the enclosure.

### 2.5 Interlocks and fail-safe defaults

Interlocks are “this must be true before energy is enabled.”

Examples:

- Lid closed before motor runs
- Minimum airflow before heater enables
- Valid sensor signal before actuator moves
- Watchdog must be alive or outputs go safe

Fail-safe defaults:

- Outputs off on reset
- Actuators disabled until commanded
- Safe state documented and tested

### 2.6 Labeling and user instructions (lite but real)

If a reasonable user can misuse it, either:

- Design against misuse, or
- Label and guide clearly

Minimum:

- Electrical input rating label
- Polarity label (if applicable)
- Warnings for heat, sharp edges, batteries
- “Approved accessories/cables” statement (if relevant)

---

## 3) Environmental & Sustainability

**Scope**: RoHS/REACH/WEEE, materials disclosure, eco-design.

### 3.1 RoHS

RoHS restricts certain hazardous substances in electrical and electronic equipment.

Builder impact:

- Need supplier/material declarations for parts.
- Need a product compliance statement if selling into RoHS regions.

### 3.2 WEEE

WEEE governs collection/treatment/recovery of electronic waste in the EU.

Builder impact:

- May require producer registration and take-back obligations depending on role/country.
- At minimum: plan end-of-life handling and labeling.

### 3.3 REACH (SVHC)

REACH imposes obligations for substances of very high concern (SVHC) in articles.

Builder impact:

- Track SVHC declarations for plastics, cables, adhesives, housings.
- Store supplier compliance docs per part.

### 3.4 Eco-design heuristics

- Design for disassembly (standard fasteners, accessible screws)
- Avoid permanent adhesives when not necessary
- Reduce part count
- Use recyclable materials where possible
- Provide repair guidance + spare parts where viable
- Choose long-life components (avoid near-EOL parts)

---

## 4) Legal & IP Basics

**Scope**: patents vs trade secrets, copyright, open-source, export controls.

### 4.1 IP decision map

Patents:

- Good when: novel and defensible, and filings are affordable.
- Bad when: value is in execution/speed/community, or hard to enforce.

Trade secrets:

- Good when: you can keep it secret.
- Bad when: it ships in a product and can be reverse engineered.

Copyright:

- Protects expression (code, docs, artwork), not the idea.

Trademarks:

- Protect brand identifiers (names, logos).

Builder rule: decide IP posture in Rev A so you do not accidentally open-source what you meant to protect.

### 4.2 Open-source licenses

If you use third-party code:

- Track licenses (MIT/BSD/Apache/GPL/etc.)
- Keep attribution notices
- Understand copyleft triggers

Minimum practice:

- Maintain a Third-Party Notices file
- Store dependency list + versions
- Record license type per dependency

### 4.3 Export controls (EAR/ITAR)

Export controls can apply to hardware, software, technical data, and even “deemed exports.”

Builder guardrails:

- If your project relates to defense, advanced sensors, encryption, or controlled tech: assume export controls may apply.
- Do not share controlled technical data with foreign persons or store it in uncontrolled systems without understanding implications.
- Maintain an Export Control Log (classification assumptions, access, what was shared).

If you are near ITAR/EAR boundaries, get expert review.

---

## 5) Ethics & Responsible Use

**Scope**: data ethics, user safety, dual-use, disclosure policies.

### 5.1 Ethics is risk management for humans

Ethical failure modes:

- Harm due to foreseeable misuse
- Privacy violations
- Unsafe defaults
- Security negligence
- Dual-use enablement without safeguards
- Misleading claims

### 5.2 Data ethics (minimum viable)

If you collect data:

- Data minimization
- Purpose limitation
- Retention policy
- Access control
- User transparency

### 5.3 Dual-use thinking (quick test)

Ask:

- Could this be used to harm people or enable wrongdoing?
- Does the design lower the skill barrier for misuse?
- What safeguards can you add without ruining the product?

Safeguards can include:

- Rate limits
- Audit logs
- Safe defaults
- Friction for dangerous modes
- Clear acceptable use policy
- Removal of unnecessary dangerous features

### 5.4 Coordinated Vulnerability Disclosure (CVD)

If you ship hardware/software, people may report vulnerabilities.

Minimum CVD elements:

- How to report (email/web form)
- What info to include
- Expected response timeline
- Safe harbor statement (good-faith researchers)
- How you credit reporters (optional)

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

# Engineering OS — Security (Marketplace Draft)

### What this page is

A marketplace-ready, Notion-native **Security & Privacy mini-spec** you can drop into an Engineering OS.

Each section is designed to become a database (or a page + linked database) and includes:

- **Purpose** and **Definition of Done**
- Suggested **Fields** (schema)
- A **CSV Starter** for quick import
- A pragmatic **SOP** and **Gates**
- **Relations** so security stays connected to requirements, releases, and operations

### How to use

1. Treat each section (D1–D7) as its own database.
2. Create the database using the **Fields** list.
3. Optional: copy the **CSV Starter** into a `.csv` and import it.
4. Revisit the gates at every baseline change and before release.

---

## D) Security & Privacy Mini-Spec

## D1) Threat Model (STRIDE-lite)

**Purpose**: Identify what can go wrong by asset and data flow, and define controls before build.

**Definition of Done**: Assets and data flows mapped. Threats enumerated. Likelihood and impact scored. Controls and owners assigned. Residual risk explicitly accepted. Review scheduled.

**Fields**

- Asset / Data Flow (text)
- Threat (select/text: spoofing, tampering, info disclosure, DoS, privilege escalation, repudiation, other)
- Vector (how)
- Impact (select: Low, Medium, High)
- Likelihood (select: Low, Medium, High)
- Control (prevent/detect/respond) (text)
- Owner (person)
- Residual Risk (text)
- Status (select: Open, Mitigated, Accepted)
- Review Date (date)

**CSV Starter**

```
Asset/Data Flow,Threat,Vector,Impact,Likelihood,Control,Owner,Residual Risk,Status,ReviewDate
Firmware update,Tampering,Unsigned update package,High,Med,"Sign + verify updates (Ed25519)",Alex,"Keys stored in HSM",Mitigated,2025-12-28
Telemetry log,Information disclosure,Intercept on Wi-Fi,Med,Med,"TLS + rotate creds",Alex,"User misconfig",Open,2026-01-10

```

**SOP**

1. List assets and flows (firmware, logs, update channel, cloud API).
2. Draw a simple DFD (boxes and arrows) and mark trust boundaries.
3. For each flow, brainstorm STRIDE threats and score impact and likelihood.
4. Choose controls (prevent, detect, respond). Assign owners and deadlines.
5. Record residual risk and acceptance. Schedule review.
6. Re-check at each architecture change and before release.

**Gates**

- **Entrance**: Interfaces frozen (or close).
- **Exit**: All High/High and High/Medium items have implemented controls and owners.

**Relations**: Requirements, ICD, SBOM, Build/Reproducibility, Vulnerability Mgmt, Ops/Runbook.

**Hobby vs Product**

- **Hobby minimum**: One-page table of assets → top five threats → one control each.
- **Product grade**: Full STRIDE by flow, scored risks, control test evidence, sign-offs, re-review on change.

---

## D2) Data Handling & Privacy Spec

**Purpose**: Define what data you collect, why, where it lives, how long, and who can access it.

**Definition of Done**: Data inventory completed. Retention and encryption defined. Roles, consent, and delete/export paths defined. Storage locations documented.

**Fields**

- Data Item (PII/telemetry/keys/config/etc.)
- Source (device/app/cloud/user)
- Purpose (text)
- Storage Location (device/cloud/SaaS + region)
- Retention (duration/condition)
- Access Role(s) (text)
- In-Transit Encryption (Y/N/method)
- At-Rest Encryption (Y/N/method)
- Anonymization/Pseudonymization (Y/N + method)
- Legal/Policy Basis (text, if applicable)
- DSR Process (export/delete path)
- Owner (person)

**CSV Starter**

```
Data Item,Source,Purpose,StorageLocation,Retention,Access Roles,In-Transit,At-Rest,Anonymization,Legal Basis,DSR Process,Owner
Device logs,Device,"Debug + QA","Local SD; Cloud S3 (us-west-2)","90 days","Eng read-only",TLS,AES-256,"Scrub PII","Legitimate interest","Support ticket + script",Alex

```

**SOP**

1. Inventory all data created and processed (including transient and debug).
2. For each item, define purpose, storage location, retention, and access roles.
3. Specify encryption in transit and at rest. Note key storage and rotation.
4. If personal data exists: define consent, policy, and delete/export path.
5. Publish a short privacy note in plain language.

**Gates**

- **Entrance**: Features defined.
- **Exit**: Every data item has retention, encryption, and access role defined.

**Relations**: Threat Model, SBOM, Ops/Runbook, Legal/Policy.

**Hobby vs Product**

- **Hobby minimum**: List what you log and where. Delete after X days.
- **Product grade**: Full data map, RBAC, KMS-managed keys, audit logs, DSR workflow.

---

## D3) SBOM (Software Bill of Materials) & Licenses

**Purpose**: Know every third-party component you ship, its license, and known CVEs.

**Definition of Done**: SBOM generated (SPDX/CycloneDX). Licenses recorded. CVEs triaged. Build hashes pinned.

**Fields**

- Component (name)
- Version (semver/commit)
- License (MIT/Apache-2.0/GPL/etc.)
- Origin (URL/source)
- Integrity (hash)
- Known CVEs (list/severity)
- Use Scope (prod/dev/tooling)
- Replacement Policy (alt/version)
- Owner/Reviewed (person/date)

**CSV Starter**

```
Component,Version,License,Origin,Integrity,Known CVEs,UseScope,Replacement Policy,Owner
lwIP,2.2.0,BSD-3,https://...,sha256:...,None,prod,"Pin minor; update quarterly",Alex

```

**SOP**

1. Generate SBOM from the build (lockfiles/container image).
2. Record licenses and check compatibility with distribution.
3. Scan CVEs and triage High and Critical. Assign remediation.
4. Pin versions and hashes and store SBOM with the release.

**Gates**

- **Entrance**: Build runnable.
- **Exit**: SBOM attached to release. License and CVE checks completed.

**Relations**: Vulnerability Mgmt, Releases, Compliance Docs.

**Hobby vs Product**

- **Hobby minimum**: Manual list of libraries and versions.
- **Product grade**: Automated SBOM per build, license policy checks, CI gating, signed attestation.

---

## D4) Build Reproducibility & Supply-Chain Security

**Purpose**: Ensure builds are deterministic, attestable, and verifiable.

**Definition of Done**: Toolchains pinned. Builds are containerized. Artifacts are signed with attestations. Verification steps documented.

**Fields**

- Build Input (repo/commit)
- Environment (container image digest)
- Reproducible (Y/N + notes)
- Artifact Hash (sha256)
- Signature/Attestation (Y/N + where)
- Dependency Policy (pin/verify/fail)
- SLSA Target (level)
- Verification Steps (doc link)

**CSV Starter**

```
BuildInput,Environment,Reproducible,ArtifactHash,Signature/Attestation,DependencyPolicy,SLSATarget,VerificationSteps
repo@a1b2c3,[ghcr.io/app@sha256:...,Yes,sha256:...,Sigstore](http://ghcr.io/app@sha256:...,Yes,sha256:...,Sigstore) attest,"Pinned + checksum",2,doclink

```

**SOP**

1. Pin compilers, SDKs, and dependencies. Build in a container.
2. Produce hashes. Sign artifacts. Store attestation with the release.
3. Add a [VERIFY.md](http://VERIFY.md) with exact reproduce and verify steps.
4. Fail CI on dependency drift or unsigned artifacts.

**Gates**

- **Entrance**: CI set up.
- **Exit**: Signed, reproducible artifact with verification steps.

**Relations**: SBOM, Releases, Ops/Runbook, Security Policies.

**Hobby vs Product**

- **Hobby minimum**: Document tool versions, keep a Dockerfile, save hashes.
- **Product grade**: Hermetic CI, signature + attestation, dependency verification, promotion gates.

---

## D5) Secrets & Access Control (Keys, Tokens, Roles)

**Purpose**: Prevent credential sprawl and enforce least privilege with rotation.

**Definition of Done**: Central storage in place. Role matrix defined. Rotation policy defined. Audit logs available.

**Fields**

- Secret Name (text)
- Scope (dev/stage/prod/device)
- Storage Method (vault/envfile/HSM)
- Rotation Policy (interval/trigger)
- Access Roles (list)
- Last Rotated (date)
- Audit Log Link (file/url)

**CSV Starter**

```
Secret,Scope,StorageMethod,RotationPolicy,Access Roles,Last Rotated,AuditLog
OTA_SIGN_KEY,prod,HSM,"6 months","Release-mgr; CI",2025-11-01,link

```

**SOP**

1. Inventory all secrets. Move to a central store. Remove from code.
2. Define roles and least-privilege access.
3. Set rotation cadence and document emergency rotation.
4. Enable audit logging and review monthly.

**Gates**

- **Entrance**: Services/features defined.
- **Exit**: No plaintext secrets in repo. Rotation and audit in place.

**Relations**: Threat Model, Build/Reproducibility, Ops/Runbook.

**Hobby vs Product**

- **Hobby minimum**: Password manager + private .env, rotate manually.
- **Product grade**: Vault/HSM, short-lived tokens, audited access, break-glass policy.

---

## D6) Vulnerability Management & Patch Policy

**Purpose**: Discover, triage, fix, and ship security updates continuously.

**Definition of Done**: Scanners scheduled. SLAs defined by severity. Releases include notes. Customer notice path exists.

**Fields**

- Source (scanner/feed/report)
- CVE/Issue (id)
- Affected Component (SBOM link)
- Severity (Low/Med/High/Critical)
- Decision (Fix/Defer/Accept)
- SLA (days)
- Status (Open/In Progress/Fixed/Released)
- Evidence (PR/build/release)

**CSV Starter**

```
Source,CVE/Issue,Affected,Severity,Decision,SLA,Status,Evidence
NVD,CVE-2025-1234,OpenSSL 3.0.14,Critical,Fix,7,In Progress,PR#221

```

**SOP**

1. Enable weekly scans (code, deps, containers).
2. Triage and set decision and SLA. Assign an owner.
3. Patch, test, and release. Publish a customer note if needed.
4. Review backlog monthly. Ensure no overdue criticals.

**Gates**

- **Entrance**: SBOM available.
- **Exit**: No overdue items per SLA. Fixes released or documented.

**Relations**: SBOM, Releases, Test Evidence, Ops/Runbook.

**Hobby vs Product**

- **Hobby minimum**: Occasional library updates.
- **Product grade**: SLA policy, dashboards, release advisories, backport plan.

---

## D7) Incident Response Mini-Runbook

**Purpose**: Respond quickly and consistently to security and privacy events.

**Definition of Done**: Severity ladder defined. First-hour checklist exists. Contacts and comms templates exist. Postmortem format defined. Rehearsal completed.

**Fields**

- Trigger (what happened)
- Severity (S1–S4)
- First-Hour Actions (checklist)
- Forensics/Evidence (what to collect)
- Customer/Regulatory Comms (templates)
- Roles/Contacts (on-call/escalation)
- Postmortem Link

**CSV Starter**

```
Trigger,Severity,First-Hour Actions,Forensics,Comms,Roles/Contacts,Postmortem
Suspected key leak,S2,"Revoke; rotate; disable pipeline","Audit logs; repo history","Customer advisory draft","Second on-call; Eng mgr",link

```

**SOP**

1. Define severity levels and examples.
2. Write first-hour steps including revoke, rotate, and isolate.
3. Prepare comms templates and a contact list.
4. Run a blameless postmortem and track follow-up actions.

**Gates**

- **Entrance**: Threat model done.
- **Exit**: On-call reachable. Templates stored. Rehearsal completed.

**Relations**: Threat Model, Secrets, Ops/Runbook, Comms.

**Hobby vs Product**

- **Hobby minimum**: One page: who to call, how to rotate, where backups live.
- **Product grade**: Paging, on-call schedule, templated advisories, regulator timelines, drills.

# Engineering OS — Security, Compliance, Ops & Ethics (36–40) (Marketplace Draft)

### What this page is

A marketplace-ready, Notion-native spec for **Security, Compliance, Ops & Ethics (36–40)** inside an Engineering OS.

Each section is intended to become a dedicated database (or page + linked database), and includes:

- **Purpose** and **Definition of Done**
- Suggested **Fields** (schema)
- A **CSV Starter** for quick import
- A pragmatic **SOP** and **Gates**
- **Relations** to keep traceability intact across risk, releases, and operations

### How to use

1. Treat each section (36–40) as its own database.
2. Create the database using the **Fields** list.
3. Optional: copy the **CSV Starter** into a `.csv` and import it.
4. Wire the cross-links once (bottom). Reuse them for every project.

---

## Engineering OS — Security, Compliance, Ops & Ethics (36–40)

## 36) Security, Privacy & Data Protection

**Purpose**: Identify assets and data, model threats, and implement controls so the product and its users stay safe.

**Definition of Done**: Asset and data inventory complete. Threat model documented. Controls implemented and tested (authN/Z, crypto, logging). SBOM published. Incident response plan exercised. Privacy assessment approved.

**Fields**

- Asset / Module (title)
- Data Classification (select: None, Public, Internal, Confidential, PII, PHI)
- Threat Model ID (relation)
- Controls (authN/Z, encryption at rest/in transit, hardening) (text)
- Key Management (KMS/HSM, rotation policy) (text)
- SBOM (file/link + hash)
- Third-Party Dependencies (list + versions)
- Vulnerability Status (select: Open, Patched, Exception)
- Patching Cadence (text)
- Logging & Audit Plan (text)
- Privacy Assessment (LIA/DPIA) (file/link)
- IR Playbook Link (relation)
- Owner (person)
- Status (select: Draft, In Review, Implemented, Verified)
- Evidence (links/files)

**CSV Starter**

```
Asset / Module,Data Classification,Threat Model ID,Controls,Key Management,SBOM,Third-Party Dependencies,Vulnerability Status,Patching Cadence,Logging & Audit Plan,Privacy Assessment,IR Playbook Link,Owner,Status,Evidence
Mobile App,PII,TM-APP-01,"OAuth2, TLS1.3, cert pinning","KMS-managed keys; 90-day rotation",/sbom/app_1.0.spdx.json,"OkHttp 4.12; Moshi 1.15",Patched,"Monthly + out-of-band critical","Event IDs, minimal PII, 30-day retention",/privacy/dpia_[app.md](http://app.md),/ir/ir_[playbook.md](http://playbook.md),Owner A,Implemented,/pentest/q1_report.pdf

```

**SOP**

1. Inventory assets and data. Classify sensitivity and retention.
2. Threat model (STRIDE/LINDDUN) per asset. Capture abuse and misuse cases.
3. Select controls: authN/Z, crypto, hardening, segmentation, secure boot/TPM, least privilege.
4. Produce an SBOM. Set vulnerability scanning and patch cadence (including vendors).
5. Define logging (events, retention, redaction) and privacy posture (DPIA/LIA where needed).
6. Run pen tests or security review. Fix findings or document exceptions with expiry.
7. Incident response: roles, severities, comms templates. Run a tabletop and record outcomes.

**Gates**

- **Pre-pilot**: Threat model + baseline controls + logging + SBOM complete.
- **Pre-release**: Pen test passed. Privacy review approved. IR playbook exercised.

**Relations**: Risk Register, Requirements (safety/privacy), Ops/IR, Legal/Compliance, Releases, Change Control.

---

## 37) Regulatory, Standards & Certification

**Purpose**: Determine applicable regulations and standards, plan compliance, and capture evidence or certifications.

**Definition of Done**: Applicability matrix approved. Gaps closed. Pre-tests complete. Accredited testing passed (if required). Technical file and declarations stored.

**Fields**

- Reg/Std (title) (e.g., CE, FCC, UL, IEC-62368, ISO-27001, SOC2, GDPR/CCPA, RoHS, WEEE, ITAR/EAR)
- Product Scope / Variant (text)
- Applicability (select: Yes, No, N.A.) + Rationale (text)
- Gap Assessment (file/link)
- Test/Assessment Plan (file/link)
- Lab / Assessor (text)
- Evidence Items (reports, photos, schematics, BOM, risk analysis) (files/links)
- Declarations/Marks (DoC, SDoC, labels) (files/links)
- Owner (person)
- Status (select: Planned, In Progress, Passed, Failed)
- Renewal/Surveillance Due (date)

**CSV Starter**

```
Reg/Std,Product Scope / Variant,Applicability,Gap Assessment,Test/Assessment Plan,Lab / Assessor,Evidence Items,Declarations/Marks,Owner,Status,Renewal/Surveillance Due
FCC Part 15B,"Base unit RevB","Yes – unintentional radiator","/compliance/gap_fcc15b.xlsx","/compliance/plan_[fcc15b.md](http://fcc15b.md)","Alpha Labs","/reports/fcc_emissions.pdf","/declarations/sdoc_revB.pdf",Owner B,Passed,2027-06-01

```

**SOP**

1. Map applicability by market and product type. Capture rationale.
2. Run gap analysis and create remediation plan (design tweaks, tests, documentation).
3. Pre-test internally or via pre-compliance labs. Fix issues.
4. Book accredited tests and audits. Assemble the technical file (drawings, BOM, risk, test results).
5. Record outcomes. Publish declarations and markings. Schedule renewals and surveillance.

**Gates**

- **CDR**: Applicability and plan approved.
- **Release**: Evidence uploaded. Declarations issued. Labels and markings verified.

**Relations**: Reliability, DFM/DFA/DFS, Risk, Legal, Docs, Procurement (material declarations), Releases.

---

## 38) Operations, SRE & Customer Support

**Purpose**: Define how the product is run and supported (cloud or field), with SLOs, runbooks, incidents, and RMA loops.

**Definition of Done**: SLO/SLIs defined. Monitoring and telemetry live. Runbooks published. On-call and response matrix active. Support and RMA workflows ready. Postmortem process established.

**Fields**

- Service/Component (title)
- SLOs (availability, latency, error rate) (text)
- SLIs (definitions/queries) (text)
- Error Budget Policy (text)
- Monitors & Alerts (links/IDs)
- Runbooks (relations/files)
- On-Call Schedule / Escalation (file/link)
- Incident Severity Matrix (file/link)
- Ticketing Queues (Support/Engineering) (text)
- RMA/Return Policy (file/link)
- Spare Pool / Stock Levels (numbers/locations)
- Metrics (MTTA, MTTR, CSAT/NPS)
- Status (select: Ready, Live, Tuning)

**CSV Starter**

```
Service/Component,SLOs,SLIs,Error Budget Policy,Monitors & Alerts,Runbooks,On-Call Schedule / Escalation,Incident Severity Matrix,Ticketing Queues,RMA/Return Policy,Spare Pool / Stock Levels,Metrics,Status
Data API,"99.9% monthly; p95 < 300ms","uptime_sli; latency_p95","Freeze deploys if >25% budget burned","/grafana/dash/12","/runbooks/api_[outage.md](http://outage.md)","/oncall/schedule.ics","/ir/severity_[matrix.md](http://matrix.md)","Zendesk L2; Jira ENG","/support/rma_policy.pdf","Hubs: 20 units total","MTTA 8m; MTTR 42m; CSAT 4.6",Live

```

**SOP**

1. Define SLOs and SLIs and the error budget policy.
2. Instrument monitoring with actionable alerts and link each to a runbook.
3. Set on-call and escalation. Train using game days.
4. Support workflow: intake, triage, escalation, knowledge base, SLA targets.
5. RMA and spares: define criteria and ensure closed-loop feedback to Quality and Engineering.
6. Postmortems: blameless format, tracked actions, and regression checks.

**Gates**

- **Go-live**: SLOs signed. Monitors and runbooks active. Support trained.
- **Quarterly ops review**: SLO adherence, incident trends, backlog burn-down.

**Relations**: Releases, Reliability, Metrics/Analytics, Security/IR, Quality/CAPA, EOL.

---

## 39) Product Analytics, Experimentation & Voice of Customer

**Purpose**: Measure value, learn from users, and run disciplined experiments to guide decisions.

**Definition of Done**: North-star metric and KPIs defined. Tracking plan implemented and QA’d. Event dictionary maintained. VOC channels active. Experiments run and decisions captured.

**Fields**

- North-Star Metric (title)
- KPIs (activation, retention, reliability, cost) (text)
- Tracking Plan (file/link)
- Event Dictionary (file/link)
- Data Retention/Privacy Rules (text)
- Experiment ID (relation)
- Hypothesis (text)
- Variant Design (A/B, multivariate) (text)
- Success Criteria & Stats Plan (text)
- Results (file/link)
- Decisions & Next Steps (text)
- Owner (person)
- Status (select: Planned, Running, Complete)

**CSV Starter**

```
North-Star Metric,KPIs,Tracking Plan,Event Dictionary,Data Retention/Privacy Rules,Experiment ID,Hypothesis,Variant Design,Success Criteria & Stats Plan,Results,Decisions & Next Steps,Owner,Status
Weekly Active Analyzers,"DAU/WAU; feature adoption; crash-free sessions","/analytics/tracking_[plan.md](http://plan.md)","/analytics/event_dict.csv","PII removed; 90-day retention",EXP-27,"Simplified setup increases activation 15%","A/B (n≈5k users)","p<0.05; uplift ≥15%; guardrail: crash rate","/results/exp27.html","Ship Variant B; update onboarding",Owner C,Complete

```

**SOP**

1. Define NSM and KPIs tied to user value, with reliability and cost guardrails.
2. Author tracking plan. Implement and QA events in staging and production.
3. Run VOC channels (surveys, interviews, telemetry feedback). Tag themes.
4. Design experiments with hypothesis and stats plan. Run, analyze, decide.
5. Close the loop into roadmap, docs, and support.

**Gates**

- **Beta start**: Tracking plan complete and QA’d. VOC intake live.
- **Quarterly PM review**: Experiments shipped, decisions logged, metric movement reviewed.

**Relations**: Requirements, Roadmap, Security/Privacy, Ops, Docs, Pilot/Beta.

---

## 40) Ethics, Safety & Responsible Use

**Purpose**: Prevent harm and unethical outcomes by designing for safe, accessible, and responsible use, including misuse cases.

**Definition of Done**: Hazard and misuse analyses documented. Mitigations implemented. Residual risks accepted. Accessibility and fairness checks complete. Safety labeling and comms ready.

**Fields**

- Hazard/Abuse Case (title)
- Context (user, environment, jurisdiction) (text)
- Severity (S) / Probability (P) (scales)
- Risk Priority (computed)
- Mitigations (design, process, warnings) (text)
- Residual Risk & Rationale (text)
- Accessibility Review (WCAG/Section 508 or physical equivalents) (file/link)
- Fairness/Bias Review (if ML/data involved) (file/link)
- Safety Notices/Labeling (file/link)
- Review Board / Approvers (people)
- Status (select: Open, Mitigated, Accepted, Deferred)
- Re-review Date (date)

**CSV Starter**

```
Hazard/Abuse Case,Context,Severity,Probability,Risk Priority,Mitigations,Residual Risk & Rationale,Accessibility Review,Fairness/Bias Review,Safety Notices/Labeling,Review Board / Approvers,Status,Re-review Date
Unintended misuse in vehicle,"Single operator, high-speed",High,Medium,High,"Lockouts; clear warnings; non-distracting UI","Residual medium; documented in IFU","/accessibility/a11y_[checklist.md](http://checklist.md)",,"/labels/safety_card.pdf","Safety Lead; PM; Legal",Mitigated,2026-04-01

```

**SOP**

1. Identify hazards and abuse scenarios, including bystanders and downstream impacts.
2. Analyze risk (FMEA/HARA): score S×P and define mitigations. Avoid warning-only mitigations where feasible.
3. Accessibility: evaluate visual, motor, and cognitive access. Provide alternatives.
4. Ethics and fairness (if ML/data): provenance, bias checks, explainability, opt-outs.
5. Document labels and comms. Train support. Re-review after incidents and major changes.

**Gates**

- **Pre-release**: Safety and ethics sign-off with residual risks and justifications.
- **Post-incident**: Mandatory re-review. Corrective actions tracked to closure.

**Relations**: Requirements (safety/privacy), Legal/Compliance, Docs (Owner’s Guide), Ops/IR, Reliability, Support.

---

## Cross-links to wire (once)

- **Security/Privacy** ↔ Risk, SBOM, Ops/IR, Legal, Releases.
- **Regulatory** ↔ Reliability, DFM, Risk, Docs, Procurement.
- **Ops/SRE/Support** ↔ Releases, Metrics, Quality/CAPA, EOL.
- **Analytics/VOC** ↔ Requirements, Roadmap, Privacy, Pilot/Beta.
- **Ethics/Safety** ↔ Requirements, Legal, Docs, Ops, Reliability.

# Engineering OS — Test Strategy & Evidence Pack (Marketplace Draft)

### What this page is

A marketplace-ready, Notion-native **Test Strategy & Evidence Pack** spec for an Engineering OS.

It’s structured as a set of databases (or page + linked DBs) you can implement immediately. Each section includes:

- **Purpose** and **Definition of Done**
- Suggested **Fields** (schema)
- A **CSV Starter** for quick import
- A pragmatic **SOP** and **Gates**
- **Relations** so requirements, tests, defects, and evidence stay traceable

### How to use

1. Treat each section (E1–E10 + Traceability Matrix) as its own database.
2. Create the database using the **Fields** list.
3. Optional: copy the **CSV Starter** into a `.csv` and import it.
4. Enforce the gates at milestone boundaries (PDR/CDR/TRR/PRR).

---

## E) Test Strategy & Evidence Pack

## E1) Test Strategy Charter

**Purpose**: Define test levels, scope, exit criteria, environments, and responsibilities.

**Definition of Done**: Test levels are documented (unit/integration/system/field). Environments are defined. Entry/exit gates are explicit. Ownership is assigned.

**Fields**

- Levels (unit/integration/system/field/etc.)
- Scope per Level (text)
- Environments (sim/bench/stage/prod-like)
- Entry/Exit Criteria (per level)
- Roles/Owners
- Risks & Assumptions
- Schedule/Milestones

**CSV Starter**

```
Level,Scope,Environment,Entry Criteria,Exit Criteria,Owner
System,"End-to-end scenarios",Bench rig,"HW/FW stable","All P1 pass; no P0 defects",QA

```

**SOP**

1. Pick the levels you will run and define what each proves.
2. Specify environments and required tooling/fixtures.
3. Set entry/exit gates and align them with release milestones.
4. Assign owners and publish.

**Gates**

- **Entrance**: Requirements and architecture known.
- **Exit**: Charter approved. Levels cover all risk areas.

**Relations**: Requirements, Risk Log, Fixtures, Release Plan.

**Hobby vs Product**

- **Hobby minimum**: One page listing tests you will run and when you are “done.”
- **Product grade**: Formal test plan tied to milestones with sign-offs.

---

## E2) Requirements ↔ Test Coverage Matrix

**Purpose**: Ensure every requirement has at least one test and every test maps back to a requirement.

**Definition of Done**: 100% coverage with traceability to results and evidence.

**Fields**

- Requirement ID (relation)
- Test ID(s) (relation)
- Level (unit/integration/system)
- Status (Not Planned/Planned/Executed/Pass/Fail)
- Evidence (log/report/screenshot)
- Defect ID (if failed)

**CSV Starter**

```
Requirement ID,Test ID,Level,Status,Evidence,Defect ID
R-P1,T-011,System,Pass,report_link,

```

**SOP**

1. List requirements and create at least one test per requirement.
2. Record test level and expected evidence.
3. As tests run, attach evidence and log defects for failures.
4. Review until coverage is 100%.

**Gates**

- **Entrance**: Requirements frozen.
- **Exit**: No orphan requirements or tests. All items executed or dispositioned.

**Relations**: Requirements, Test Cases, Evidence Pack, Defects.

**Hobby vs Product**

- **Hobby minimum**: Simple table mapping reqs → tests with pass/fail.
- **Product grade**: Full traceability with CI-driven status and signed reports.

---

## E3) Unit Test Spec (Code/Module Level)

**Purpose**: Validate functions and components in isolation.

**Definition of Done**: Critical logic has tests. Coverage goals set and met. Results automated in CI.

**Fields**

- Module/Function
- Test Case ID
- Inputs/Mocks
- Expected Output/Behavior
- Coverage (line/branch)
- Result (Pass/Fail)
- Evidence (CI run link)

**CSV Starter**

```
Module,TestCase ID,Inputs,Expected,Coverage,Result,Evidence
parser.c,UT-03,"frame X","value Y parsed","85% lines",Pass,ci_link

```

**SOP**

1. Identify critical code paths and write tests for them first.
2. Add mocks and stubs for I/O.
3. Set coverage targets and gate them in CI.

**Gates**

- **Entrance**: Modules defined.
- **Exit**: Critical paths covered. CI green.

**Relations**: CI/CD, Defects, Code Review.

**Hobby vs Product**

- **Hobby minimum**: Tests for tricky parts, run locally.
- **Product grade**: Coverage targets, mutation tests on critical code, CI gating.

---

## E4) Integration Test Spec

**Purpose**: Validate interactions across modules and interfaces.

**Definition of Done**: Interface tests exist. Edge cases and timing covered. Fixtures/jigs defined where needed.

**Fields**

- Interface (A↔B)
- Scenario (text)
- Preconditions (env/data)
- Steps
- Expected Results
- Evidence (logs/plots)
- Status

**CSV Starter**

```
Interface,Scenario,Preconditions,Steps,Expected,Evidence,Status
FW↔Display,"Update @10Hz","Bench PSU; mock data","Start loop","No dropped frames",plot_link,Pass

```

**SOP**

1. Enumerate interfaces and define scenarios, including errors and timeouts.
2. Build or script jigs and mocks.
3. Capture evidence and document retries and recoveries.

**Gates**

- **Entrance**: Modules stable.
- **Exit**: Happy paths and failure paths validated.

**Relations**: ICD, Fixtures, Coverage Matrix.

**Hobby vs Product**

- **Hobby minimum**: A few key end-to-end checks.
- **Product grade**: Systematic scenarios, injected faults, automated replay.

---

## E5) System / End-to-End Acceptance

**Purpose**: Prove the full product meets user-visible requirements.

**Definition of Done**: Primary user journeys have quantitative pass criteria and evidence.

**Fields**

- Journey/Use Case
- Requirement IDs Covered
- Steps
- Metrics (latency, accuracy, rate)
- Pass/Fail Criteria
- Evidence (video/log)
- Status

**CSV Starter**

```
Journey,Requirement IDs,Steps,Metrics,Pass/Fail,Evidence,Status
Live display,"R-F2;R-P1","Power on; drive",">=10Hz; readable",Pass,video_link,Pass

```

**SOP**

1. List critical user journeys and tie each to requirements.
2. Define metrics and gates. Avoid “looks good.”
3. Run in a production-like environment and capture evidence.

**Gates**

- **Entrance**: Integration tests passing.
- **Exit**: All journeys pass, or issues are logged with an action plan.

**Relations**: Requirements, Coverage Matrix, Ops/Owner’s Guide.

**Hobby vs Product**

- **Hobby minimum**: Record a demo and check key numbers.
- **Product grade**: Witnessed acceptance with repeatable scripts and signed report.

---

## E6) Regression & CI Automation

**Purpose**: Prevent regressions and keep quality stable as code changes.

**Definition of Done**: CI runs unit/integration suites on PR. Artifacts saved. Failures block merge.

**Fields**

- Pipeline Stage (lint/unit/integration/e2e)
- Trigger (PR/merge/nightly)
- Duration Target
- Pass Gate (required/optional)
- Artifacts (reports/logs)
- Owner

**CSV Starter**

```
Stage,Trigger,Duration,Pass Gate,Artifacts,Owner
Unit,PR,"<5m",Required,JUnitXML,QA

```

**SOP**

1. Create CI stages and mark critical ones as required.
2. Store artifacts and publish badges.
3. Add flaky-test quarantine policy and track trends.

**Gates**

- **Entrance**: Unit and integration tests exist.
- **Exit**: CI blocks merges on failures. Artifacts retained.

**Relations**: Test Suites, SBOM (scan step), Releases.

**Hobby vs Product**

- **Hobby minimum**: Run tests locally before merge.
- **Product grade**: Full CI with parallelization, dashboards, blocking gates.

---

## E7) Performance / Load / Stress Tests

**Purpose**: Ensure timing, throughput, and resource use meet targets with margin.

**Definition of Done**: Workload models defined. Benchmarks repeatable. Threshold alarms exist.

**Fields**

- Metric (latency/throughput/CPU/RAM/temp)
- Workload Profile
- Tool/Fixture
- Threshold/Target
- Result
- Evidence

**CSV Starter**

```
Metric,Workload,Tool,Target,Result,Evidence
Latency,"10Hz update","Bench script","<=100ms",78ms,report_link

```

**SOP**

1. Define metrics and workloads that match real use.
2. Script tests and capture raw data plus summary.
3. Set thresholds and track trends.

**Gates**

- **Entrance**: Functional pass.
- **Exit**: Meets targets with agreed margin.

**Relations**: Requirements, DfR, Thermal/Power Logs.

**Hobby vs Product**

- **Hobby minimum**: One or two timing checks using logs.
- **Product grade**: Automated benchmarks, trend charts, regression alarms.

---

## E8) Reliability / Soak / Environmental

**Purpose**: Catch flakiness over time and across temperature, voltage, vibration.

**Definition of Done**: Soak and environmental sweeps executed. Failure modes captured. Fixes tracked.

**Fields**

- Test Type (soak/temp/vibe/ESD)
- Profile (duration/range)
- Pass Criteria
- Failures Observed
- Fix/ECO Link
- Status

**CSV Starter**

```
TestType,Profile,Pass Criteria,Failures,Fix/ECO,Status
Thermal sweep,"0–60°C; 24h","No resets; stable rates",None,,Pass

```

**SOP**

1. Choose profiles (time and stress).
2. Monitor with telemetry and log failures.
3. File ECOs for fixes and re-test.

**Gates**

- **Entrance**: System stable.
- **Exit**: Profiles passed, or mitigations planned and owned.

**Relations**: DfR, Risk Log, ECOs.

**Hobby vs Product**

- **Hobby minimum**: Overnight run and basic temperature check.
- **Product grade**: Structured ALT/HALT-style testing with telemetry and failure analysis.

---

## E9) Usability & Accessibility Validation (if applicable)

**Purpose**: Ensure users can operate safely and efficiently.

**Definition of Done**: Key tasks timed. Error rates recorded. Accessibility checks applied.

**Fields**

- Task
- User Profile
- Success Criteria (time/error)
- Observations
- Issues & Severity
- Status

**CSV Starter**

```
Task,User,Success Criteria,Observations,Issues,Status
Change layout,Driver,"<30s; 0 errors","Glare at noon","Increase contrast (P2)",Open

```

**SOP**

1. Define user tasks and success metrics.
2. Run 2–5 users and record times, errors, notes.
3. Log issues and prioritize fixes.

**Gates**

- **Entrance**: UI usable.
- **Exit**: P0 and P1 issues addressed or deferred with rationale.

**Relations**: Requirements (UX), Owner’s Guide, Issues.

**Hobby vs Product**

- **Hobby minimum**: Ask a friend to try tasks and take notes.
- **Product grade**: Scripted sessions, accessibility checklists, signed findings.

---

## E10) Evidence Pack & Test Report

**Purpose**: Package results so a reviewer can verify claims quickly.

**Definition of Done**: Single index links requirements → tests → evidence. Summary and sign-off included.

**Fields**

- Requirement ID
- Test ID(s)
- Result (Pass/Fail/Partial)
- Evidence Link(s)
- Deviation/Waiver (if any)
- Sign-off (name/date)

**CSV Starter**

```
Requirement ID,Test ID,Result,Evidence,Deviation,Sign-off
R-P1,T-011,Pass,report_link,,QA Lead 2026-01-05

```

**SOP**

1. Export coverage matrix with results.
2. Bundle reports, logs, and videos under one folder with an [INDEX.md](http://INDEX.md).
3. Capture sign-offs and store with the release tag.

**Gates**

- **Entrance**: Tests executed.
- **Exit**: Evidence Pack attached to release. Gaps documented.

**Relations**: Coverage Matrix, Releases, Change Control.

**Hobby vs Product**

- **Hobby minimum**: Zip of screenshots/logs plus a checklist.
- **Product grade**: Structured pack with signed summary, traceability, immutable links.

---

## Traceability Matrix — Checklist

**Purpose**: Demonstrate end-to-end coverage from requirement to passing test with archived evidence.

**Definition of Done**: 100% must-have requirements mapped to executed tests. Results are PASS or justified waiver. Matrix stored with the release.

**Fields**

- Req ID
- Requirement Text
- Priority (Must/Nice)
- Design Ref (ICD/ADR)
- Code/Module
- Test ID(s)
- Result
- Evidence Link
- Notes
- Waiver ID (if any)

**CSV Starter**

```
ReqID,Priority,DesignRef,TestID,Result,EvidenceLink,Waiver,Notes
R-F-001,Must,ICD§2.1,T-001,PASS,/release/Rel-A1.0/evidence/T-001.png,,
R-P-002,Must,ADR-LOG-001,T-014,PASS,/release/Rel-A1.0/evidence/T-014.csv,,
R-U-003,Nice,UI_SPEC§4.2,T-030,PARTIAL,/release/Rel-A1.0/evidence/T-030.pdf,WA-002,"Font size under glare"

```

**SOP**

1. Number requirements and freeze IDs.
2. Map each requirement to ≥1 design reference and ≥1 test.
3. Execute tests, collect evidence, update results.
4. Generate coverage summary and resolve orphans.
5. Snapshot and store with the release pack.

**Gates**

- **Entrance**: Requirements and tests are written and ID’d.
- **Exit**: No orphan must-have requirements. Evidence archived. Summary attached.

**R/A/G Gate**

- **Green**: 100% must-have coverage and evidence present.
- **Amber**: 1–2 must-have items partial/waived with risk noted.
- **Red**: Any must-have without a mapped executed test.

**Relations**: Requirements DB, Tests DB, Evidence files, Releases, Waivers, ICDs/ADRs.

**Hobby vs Product**

- **Hobby**: Manual links and relaxed nice-to-have bar.
- **Product**: Automated extraction, signed evidence, formal waiver process, audit trail.

# Engineering OS — Test, Validation & Reliability (Marketplace Draft)

### What this page is

A practical test + evidence operating layer you can drop into an Engineering OS.

It helps you:

- Prove the project works with **measurable tests**, not “it seems fine.”
- Build a test ladder that scales from hobby builds to product work.
- Capture evidence other people (and future-you) can trust.
- Improve reliability without drowning in process.

### How to use

You do not “do all tests.” You build a **test ladder**:

- Start with quick unit-level checks
- Integrate and verify interfaces
- Prove system behavior
- Stress what matters (environment, abuse, long runs)
- Capture evidence with clear pass bars

---

## 10‑Minute Quickstart (apply to your current project)

Create a Notion page called **Test Snapshot** and capture:

- Top five requirements (even if informal)
- Top five failure modes (what you are afraid of)
- Test ladder plan (unit → integration → system → stress)
- Evidence folder link (from your Evidence Vault)
- Entry/exit criteria for the next milestone (Rev A or Rev B)

Then do one test today:

- A single measurable pass/fail check on the scariest interface (power, bus, sensor accuracy, logging integrity).

---

## 1) Test Strategy Ladder (Unit → Integration → System → Environmental → Field)

### What the ladder is

The ladder is the order that keeps you from wasting time:

1. Unit tests: verify individual functions/modules/components
2. Integration tests: verify interfaces between parts
3. System tests: verify full device behavior
4. Environmental tests: verify under heat/vibration/EMI/moisture (as needed)
5. Field acceptance: verify in real use conditions

Rule: do not jump to system tests when a unit-level test could catch the issue in five minutes.

### Entry/Exit criteria (what “ready” means)

Every rung should have:

- Entry criteria (what must be true before you test)
- Exit criteria (what constitutes success)

Example:

- Integration entry: rails stable, firmware flashed, interface wiring verified
- Integration exit: 100 consecutive transactions with zero errors

### Rev A vs Rev B test depth

- Rev A (learn safely): prove basic function, capture evidence, bound risks
- Rev B (refine): improve robustness, add coverage, reduce edge-case failures

If you try to test like Rev B during Rev A, you will stall.

---

## 2) Fixtures & Instrumentation

**Scope**: fixtures, wiring discipline, measurement uncertainty.

### Fixtures: what they are

A fixture is anything that makes tests:

- Repeatable
- Faster
- Safer
- Less error-prone

Even tape and cardboard counts if it standardizes the setup.

### Wiring discipline (so your test is not lying)

Bad wiring creates fake failures:

- Intermittent connections
- Ground loops
- Noise pickup
- Wrong pin mapping

Minimum wiring discipline:

- Label every cable end
- Strain relief on probes
- One ground reference strategy
- Photos of setup (wide + close)

### Instrumentation basics

- Multimeter: voltage/current, slow checks, continuity
- Scope: transients, ripple, timing, ringing
- Logic analyzer: bus decode, transaction proof
- Power supply (current limit): safe bring-up and fault testing
- Thermal camera/temp probe: hotspots, drift
- Load (electronic/resistive): stress, droop

### Measurement uncertainty (lite but essential)

Any measurement has error:

- Instrument accuracy
- Probe loading
- Sampling limitations
- Operator setup

Rule: never claim precision your tools cannot support. If your pass bar is tight, quantify uncertainty.

### Fixture micro‑prototypes

**MP‑FIX‑1: Repeatability check**

Run the same test five times.

Pass bar: results consistent within expected variance.

**MP‑FIX‑2: Setup time reduction**

Measure setup time before/after fixture improvements.

Pass bar: setup time drops measurably.

---

## 3) Coverage & Evidence

**Scope**: requirements mapping, pass/fail vs numeric evidence, waivers.

### Requirements still matter as a hobbyist

A requirement can be informal, but it must be testable, measurable, or clearly observable.

Bad: “Works well.”

Good: “Logs data at 50 Hz continuously for 30 minutes without gaps.”

### Pass/Fail vs numeric evidence

- Pass/fail for binary conditions (boots, connects, writes file)
- Numeric evidence for performance and margins (ripple mVpp, latency ms)

Rule: if it matters, capture numbers and margin.

### Traceability matrix

Traceability maps:

- requirement → test → evidence

Even a simple CSV prevents “we tested a lot but did not test what mattered.”

### Waivers and partials

Shipping with known issues is acceptable when documented:

- What failed
- Why you accept it
- Scope/impact
- Mitigation
- When you will fix it (Rev B trigger)

### Evidence quality standard (minimum)

Evidence is trustworthy if it includes:

- Setup description
- Versions (firmware/software/hardware)
- Procedure
- Results
- Artifact links (screenshots/logs)
- Conclusion and margin

---

## 4) Reliability Lite

**Scope**: FMEA, derating, HALT/HASS, fault injection, MTBF myths.

### Reliability is not MTBF spreadsheets

Practical reliability comes from:

- Identifying failure modes
- Designing mitigations
- Validating under stress
- Adding recovery paths

### FMEA (useful version)

For each subsystem:

- Failure mode
- Effect
- Cause
- Detection
- Mitigation

Prioritize by severity, likelihood, and detectability.

Even a 15-row FMEA catches most real-world issues.

### Derating

Do not run components at their limits.

- Voltage margin
- Current margin
- Thermal margin

Rule of thumb: if you run at 95% rating, you are gambling with variation and environment.

### HALT/HASS (conceptual, pre-chamber)

- HALT: push until it fails to find weak points
- HASS: screen production units for early-life defects

HALT-lite options:

- Heat gun + freezer pack
- Vibration via sander table (carefully)
- Supply variation
- EMI exposure in noisy environments

### Fault injection

Introduce realistic faults:

- Disconnect sensor
- Corrupt packet
- Simulate storage full
- Power dip
- Stall a task
- Force retries/timeouts

Pass bar: system detects and recovers safely, or fails safely.

### Reliability micro‑prototypes

**MP‑REL‑1: Long-run soak**

Run 4–24 hours with logging.

Pass bar: no hangs, no leaks, no corruption, restart behavior understood.

**MP‑REL‑2: Abuse shortlist**

Apply 3–5 realistic abuses.

Pass bar: bounded failure and predictable recovery.

---

## 5) Calibration & Metrology

**Scope**: references, traceability, intervals, uncertainty.

### Calibration in practice

Calibration aligns measurement to a known reference.

Metrology is the discipline of making measurements you can trust.

### When calibration matters

- Comparing to real-world truth
- Repeatability across time/devices
- Threshold-based decisions

### Traceability (lite)

For hobby work:

- Use known references (calibrated DMM, reference sensor, known weights)
- Document reference used and stated accuracy

### Calibration intervals

Pick intervals based on:

- How critical accuracy is
- Environment harshness
- Observed drift

### Recording offsets and uncertainty

Record:

- Date
- Method
- Reference
- Offset/gain values
- Uncertainty estimate
- Applied correction method

### Calibration micro‑prototypes

**MP‑CAL‑1: Two-point calibration**

Pass bar: error reduced and stable.

**MP‑CAL‑2: Temperature drift check**

Pass bar: drift quantified and acceptable or compensated.