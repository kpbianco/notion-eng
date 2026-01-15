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