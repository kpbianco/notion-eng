# Companion Guide (Expanded, Actionable)

> Each section includes: Purpose, Do this, Artifacts to produce, Process & checklist, Pitfalls, and a Quality gate you must pass before moving on.
> 

---

## 1) Vision & Success Criteria

**Purpose**

Align on *why* the project exists and what “done” objectively means.

**Do this**

Draft a one-page vision that a non-engineer can understand. Convert vision to 3–7 measurable success criteria.

**Artifacts**

- Vision Statement (Problem, Outcome, Who benefits, Success definition)
- Success Metrics (quantified, time-bound)

**Process & checklist**

- Write a 4-block vision: Problem → Outcome → Who → Success.
- Translate Outcome into measurable metrics (e.g., “≤ 2s startup,” “≥ 95% satisfaction,” “≤ $X unit cost”).
- Add a North-Star metric (the one number you’d present to leadership).

**Pitfalls**

Vague words (“better,” “robust”), confusing solution with problem.

**Quality gate**

A neutral reviewer can restate your success in one sentence *with numbers*.

---

## 2) Stakeholders & Personas

**Purpose**

Make design tradeoffs explicit by knowing who uses, buys, maintains, and signs off.

**Do this**

Create brief personas and capture their goals, constraints, and success measures.

**Artifacts**

- Persona Cards (primary user, buyer, maintainer, operator)
- Stakeholder Map (influence vs interest)

**Process & checklist**

- For each persona: job-to-be-done, pains, environment, must-haves.
- Add an anti-persona (who you won’t optimize for) to prevent scope creep.
- Map who approves what.

**Pitfalls**

Designing for “everyone,” ignoring maintainers/operators.

**Quality gate**

You can explain a tricky tradeoff by pointing to a persona’s need.

---

## 3) Problem Statement & Value Proposition

**Purpose**

Center decisions on value, not features.

**Do this**

Write a one-sentence value prop and quantify value (time saved, revenue, risk).

**Artifacts**

- Problem Statement
- Value Prop with quantified impact

**Process & checklist**

- Template: “For [persona], who struggles with [pain], our solution [does X] leading to [measurable value].”
- Add 3–5 proof points or benchmarks you can later validate.

**Pitfalls**

Listing features as value; no numbers.

**Quality gate**

Value can be estimated in dollars/time/risk.

---

## 4) Constraints & Assumptions

**Purpose**

Expose hard limits and bets that could break the plan.

**Do this**

List non-negotiable constraints and top assumptions with owners to validate.

**Artifacts**

- Constraint List (legal, physical, budget, timeline)
- Assumption Log (with validation dates/owners)

**Process & checklist**

- Capture top 10 constraints.
- For each assumption, define a validation task (links to risk-kill prototypes in §15).

**Pitfalls**

Treating assumptions as facts; no owners.

**Quality gate**

Every assumption has a scheduled validation (who/when/how).

---

## 5) Glossary & Context

**Purpose**

Eliminate ambiguity.

**Do this**

Define acronyms/terms; draw a high-level context diagram.

**Artifacts**

- Glossary (top 20 terms)
- System Context Diagram (actors, external systems, arrows with protocols/units)

**Process & checklist**

- Write 1–2 line definitions without jargon.
- Add trust boundaries and data sensitivity tags where relevant.

**Pitfalls**

Undefined terms; burying internals in the context view.

**Quality gate**

A newcomer can read this page and correctly name the parts in a meeting.

---

## 6) Functional Requirements

**Purpose**

Specify *what* must happen.

**Do this**

Write numbered “shall” statements that are testable.

**Artifacts**

- Functional Requirements (FR-001 …) with acceptance tests linked

**Process & checklist**

- 8–15 must-haves.
- Each FR includes: trigger, behavior, exceptions.
- Tag priority (Must/Should/Could).

**Pitfalls**

Design baked into requirements; vague verbs.

**Quality gate**

Each FR can be unambiguously tested and judged pass/fail.

---

## 7) Non-Functional Requirements (Performance/Reliability/Quality)

**Purpose**

Make quality attributes concrete.

**Do this**

Set numeric targets for latency, throughput, accuracy, availability, MTTR, etc.

**Artifacts**

- NFR Table (attribute, target, method of measure)
- Workload profiles (typical/peak/worst case)

**Process & checklist**

- Choose 5–10 attributes; define target and test method.
- Define error budgets and consequences for violation.

**Pitfalls**

“Fast,” “reliable,” “secure” with no numbers.

**Quality gate**

Targets are realistic and testable with an outlined method.

---

## 8) Interface Requirements (ICD)

**Purpose**

Prevent integration by guesswork.

**Do this**

Document every interface’s schema/pins/timing/units/error handling/versioning.

**Artifacts**

- ICD per interface (tables/diagrams)
- Versioned change log

**Process & checklist**

- For each interface: endpoints, fields/pins, units/ranges, timing/handshake, errors/timeouts, versioning.
- Define backward compatibility policy.

**Pitfalls**

Implicit defaults; “TBD” left in a freeze.

**Quality gate**

Another team could implement the other side using only the ICD.

---

## 9) Environmental & Physical Requirements

**Purpose**

Ensure it survives the real world.

**Do this**

Set environmental limits and reference applicable standards.

**Artifacts**

- Environment Spec (temperature, humidity, shock/vibe, ingress, EMC)
- Test reference (e.g., IEC/ISO methods)

**Process & checklist**

- Write numeric limits; note derating.
- Identify required tests and evidence to store.

**Pitfalls**

Over-assuming benign conditions; no test plan.

**Quality gate**

Environment tests are traceable to specific requirements.

---

## 10) System Context Diagram

**Purpose**

Shared mental model of boundaries and interactions.

**Do this**

Draw external actors/systems; label flows with protocols/units/frequencies.

**Artifacts**

- Context Diagram (v1.0)

**Process & checklist**

- 5–10 nodes; arrows named; trust/data boundaries marked.

**Pitfalls**

Over-detailed internals; unlabeled arrows.

**Quality gate**

A reviewer can point to any arrow and say what moves and how often.

---

## 11) Architecture Overview / Block Diagram

**Purpose**

Guide decomposition and ownership.

**Do this**

Define subsystems, responsibilities, and key interfaces.

**Artifacts**

- Block Diagram
- One-paragraph “responsibility brief” per subsystem

**Process & checklist**

- 5–9 boxes; arrows map to ICDs.
- For each box: inputs, outputs, invariants, major NFR drivers.

**Pitfalls**

Hand-wavy boxes; missing invariants.

**Quality gate**

If you removed a box, you could state what breaks and why.

---

## 12) Subsystem Responsibilities

**Purpose**

Set contracts inside the system.

**Do this**

Write a card per subsystem detailing inputs/outputs/invariants/failure modes.

**Artifacts**

- Responsibility Cards (one per subsystem)

**Process & checklist**

- Include: assumptions, failure containment, owner.
- Define observable health signals (for Ops/SRE).

**Pitfalls**

“Magic” cross-cutting behavior; no failure boundaries.

**Quality gate**

You can test a subsystem in isolation using its contract.

---

## 13) Trade Study Method

**Purpose**

Make choices defensible and repeatable.

**Do this**

Compare candidates with weighted criteria and sensitivity analysis.

**Artifacts**

- Trade Matrix (criteria, weights, scores, notes)
- Decision Record (why chosen, why not others)

**Process & checklist**

- Define criteria: performance, cost, schedule risk, supply, ecosystem, learning curve.
- Score 3–5 options; run sensitivity (does winner change if weights shift?).

**Pitfalls**

Hidden criteria; no alternates; “pet” choices.

**Quality gate**

A skeptic agrees your winner is reasonable given the weights.

---

## 14) Risk Register & FMEA

**Purpose**

Focus on what can sink the project.

**Do this**

Log risks with severity/likelihood/detectability and mitigation owners.

**Artifacts**

- Risk Register (ID, cause, S/L/D, RPN, owner)
- Mitigation Plan & review cadence

**Process & checklist**

- Identify top 10; assign owners/dates.
- Elevate “design-killers” to §15 prototypes.

**Pitfalls**

Parking risks with no action; stale register.

**Quality gate**

Every high RPN risk has a concrete mitigation or experiment scheduled.

---

## 15) Risk-Kill Prototypes (Design-Killers)

**Purpose**

Answer scary unknowns *fast* before you cement design.

**Do this**

Run 1–4 hour micro-experiments; log question, method, threshold, result, decision.

**Artifacts**

- Risk-Kill Log (Question → Method → Threshold → Result → Decision)
- Raw evidence (data, photos, code snippets)

**Process & checklist**

- Define pass/fail threshold *before* testing.
- Build the ugliest thing that isolates the variable.
- Decide immediately: proceed, change, or drop.

**Pitfalls**

Gold-plating experiments; no thresholds; no decision.

**Quality gate**

You can point to each design-critical assumption and show its proof.

---

## 16) Prototype Findings & Decisions

**Purpose**

Translate learning into design changes.

**Do this**

Write “Finding → Implication → Change” summaries; update affected docs.

**Artifacts**

- Findings Digest
- Updated Architecture/ICDs/BOM where applicable

**Process & checklist**

- For each finding, note the decision, doc links updated, and who approved.

**Pitfalls**

Learn but don’t change; orphaned knowledge.

**Quality gate**

No discrepancy between findings and the latest design docs.

---

## 17) Interface Freeze (ICD Freeze)

**Purpose**

Stop churn and enable parallel work.

**Do this**

Version and freeze ICDs/pin maps/protocols; establish change control.

**Artifacts**

- “ICD v1.0 Freeze” note with date
- Change Request (CR) template and approvers

**Process & checklist**

- Tag versions, export read-only PDFs, store in repo.
- Any change after freeze = CR + version bump.

**Pitfalls**

Silent edits; “just one more tweak.”

**Quality gate**

All downstream work references the frozen version tag.

---

## 18) Pin Map / Electrical Interfaces

**Purpose**

Remove ambiguity around signals and electrical behavior.

**Do this**

Map every pin: function, direction, voltage, pull-ups, boot state, tolerances.

**Artifacts**

- Pin Map Table
- Electrical Characteristics Notes

**Process & checklist**

- Include default/boot states and safe states on error.
- Indicate reserved pins and alternates.

**Pitfalls**

Leaving “TBD”; undocumented pulls/defaults.

**Quality gate**

A board/firmware person can wire/route without asking you questions.

---

## 19) Power Budget & Power Tree

**Purpose**

Ensure safe, stable power under all conditions.

**Do this**

Diagram sources, conversion, protection; table worst-case current, margins.

**Artifacts**

- Power Tree Diagram
- Power Budget Table (typical/peak/inrush, margin ≥30%)

**Process & checklist**

- Include protection (fusing, TVS, OVP/OCP), ground strategy, isolation.
- Validate with stress cases (startup, brownout, hot/cold).

**Pitfalls**

Ignoring peak/inrush; no derating; ground loops.

**Quality gate**

Power system tolerates worst case without violating specs.

---

## 20) Data Flow / Task Model

**Purpose**

Make runtime behavior explicit.

**Do this**

Define producers/consumers, queues/pipelines, rates, back-pressure, time budgets.

**Artifacts**

- Data-Flow Diagram
- Timing Budget (per stage)

**Process & checklist**

- Name each task, its trigger, rate, and outputs.
- Define failure behavior (drop, retry, circuit-break).

**Pitfalls**

Hidden blocking calls; contention; unbounded queues.

**Quality gate**

You can predict throughput and identify the bottleneck by inspection.

---

## 21) BOM & Part Selection

**Purpose**

Control cost, availability, and performance.

**Do this**

Create a structured BOM with key specs, lifecycle status, alternates, and supply risk.

**Artifacts**

- BOM (part, spec, primary/alternate PNs, lifecycle, lead time, cost, MOQ)
- Supply Risk Notes (single-source, obsolescence flags)

**Process & checklist**

- For each critical part: list 1–2 alternates meeting requirements.
- Capture datasheets and compliance (RoHS/REACH/etc.).
- Note validation/qualification status.

**Pitfalls**

Single-source with no backup; ignoring lifecycle.

**Quality gate**

Every critical line has at least one validated alternate or a mitigation plan.

---

## 22) Procurement & Vendor Management

**Purpose**

Make buying auditable, repeatable, and resilient to supply shocks.

**Do this**

Build a **procurement database** tied to your BOM that tracks approved vendors, quotes, POs, receipts, inspections/QA results, and vendor performance over time. This becomes your traceable history to resolve discrepancies, manage obsolescence, and support audits.

**Artifacts**

- Approved Vendor List (AVL) mapped to BOM lines
- Quotes (dated, quantities, price breaks, lead times)
- Purchase Orders (POs) + revisions
- Receiving logs (date, qty, lot/serials, CoC/CoA)
- Incoming QA check records (visual, measurements, electrical fit, regulatory docs)
- Non-conformance reports (NCRs), returns, corrective actions
- Vendor scorecards (quality, on-time, responsiveness)

**Process & checklist**

- For each BOM line, add at least one **approved vendor** with quote, plus alternates.
- Issue PO referencing BOM rev and spec; include quality clauses (CoC, date codes, packaging).
- On receipt: log lot/serial, perform incoming inspection (per AQL plan), attach CoC/CoA.
- Record any deviations, initiate NCRs/returns with photos and test evidence.
- Quarterly: review vendor scorecards; upgrade/downgrade status; note risks (capacity, geopolitical).
- Maintain a live **obsolescence watch** (PCNs/PDNs) and replacement path.

**Pitfalls**

Buying via ad-hoc carts; no receipt/lot trace; accepting substitutions without review.

**Quality gate**

You can answer: “For BOM item X in build Y, which lot did we use, from which vendor, under which spec, and did it pass incoming QA?”

---

## 23) DFM/DFA/DFS (Design for X)

**Purpose**

Reduce cost, errors, and delays in build, assembly, and service.

**Do this**

Run DFX reviews and fix flagged issues before release.

**Artifacts**

- DFX Checklist & Review Minutes
- Action Log with owners/dates

**Process & checklist**

- Walk through build steps (jigs, tools, tolerances).
- Assess assembly (orientation, clearances, fasteners, sequence).
- Plan serviceability (access to wear parts, diagnostics).
- Re-review after fixes.

**Pitfalls**

Ignoring jigs/fixtures, test points, or service access.

**Quality gate**

A technician can build/assemble/test/repair following your instructions without improvisation.

---

## 24) Configuration Management (Repos/Assets)

**Purpose**

Make everything reproducible and traceable.

**Do this**

Define repo structure, naming/versioning, branch strategy, artifact storage.

**Artifacts**

- CM Plan (folders, naming, tagging)
- Repos with READMEs, LICENSE, CI setup

**Process & checklist**

- Separate design/docs/code/test/data.
- Tag releases, store immutable artifacts (e.g., release bundle with BOM, ICDs, binaries).
- Access controls and backups.

**Pitfalls**

Blob files scattered in chats; no tags; single local copy.

**Quality gate**

You can recreate build “1.2.0” from tags alone.

---

## 25) Coding & Style Standards

**Purpose**

Reduce defects and friction.

**Do this**

Adopt linters/formatters, code review checklist, and static analysis as required.

**Artifacts**

- Style Guide links
- CI jobs (lint, format, unit tests)
- PR Checklist

**Process & checklist**

- Enforce via CI gates.
- Define exception process (who can approve and why).
- Add secure coding and dependency scanning.

**Pitfalls**

Standards that aren’t enforced; silent exceptions.

**Quality gate**

No PR merges with red CI; exceptions are documented.

---

## 26) Test Strategy & V&V Plan

**Purpose**

Decide *how* you’ll prove it works.

**Do this**

Define levels (unit/integration/system/acceptance), environments, data, and pass/fail criteria.

**Artifacts**

- Test Strategy (scope, levels, environments)
- Acceptance Criteria mapped to requirements

**Process & checklist**

- For each test level, define entry/exit criteria.
- Include real-world scenarios and negative cases.
- Plan test data/generators; define evidence to save.

**Pitfalls**

Only happy-path; no negative or stress tests.

**Quality gate**

A requirement picked at random has at least one planned test that would fail if the requirement weren’t met.

---

## 27) Test Cases & Traceability Matrix

**Purpose**

Prove coverage and support audits.

**Do this**

Map every requirement to test cases and record results with evidence links.

**Artifacts**

- RTM (Req ID → Test ID → Status → Evidence)
- Test Case Specs & Results (with logs/screenshots/data)

**Process & checklist**

- Write deterministic tests with clear assertions.
- Store evidence in a stable location; link in RTM.
- Automate report generation where possible.

**Pitfalls**

Non-asserting tests; evidence missing or ephemeral.

**Quality gate**

You can answer: “Which tests validate R-NFR-004, and where’s the evidence for build 1.1?”

---

## 28) Build Plan & Milestones/Schedule

**Purpose**

Sequence work to reduce risk, with proof checkpoints.

**Do this**

Define milestones with demonstration criteria, estimates, and blockers.

**Artifacts**

- Milestone Plan (M1..Mn)
- Integrated schedule (Gantt/Kanban) with buffers

**Process & checklist**

- For each milestone: Goal → Demo → Proof/Evidence → Blockers → Hours/Cost.
- Protect critical chain with buffers; flag cross-dependencies.

**Pitfalls**

Calendar art without proof conditions; optimistic estimates.

**Quality gate**

Every milestone has an objective “demo condition” that proves completion.

---

## 29) Budget & Cost Model

**Purpose**

Align scope with resources.

**Do this**

Model NRE (non-recurring), per-unit, tools, infra, and contingency.

**Artifacts**

- Cost Model (baseline and scenarios)
- Buy-vs-build notes

**Process & checklist**

- Capture all costs: parts, labor, fixtures, licenses, cloud, shipping, taxes.
- Add 20–30% contingency; run best/base/worst cases.
- Tie trade-offs to performance/requirements.

**Pitfalls**

Ignoring tools/overhead; no contingency.

**Quality gate**

Leadership can see cost drivers and what changes them.

---

## 30) Quality Management & CAPA

**Purpose**

Prevent repeat failures.

**Do this**

Log defects; perform RCA; implement corrective and preventive actions; verify.

**Artifacts**

- Defect Log (severity, impact, status)
- RCA (5-Whys/Fishbone)
- CAPA plan and verification records

**Process & checklist**

- Triage by severity; time-bound fixes.
- Verify fixes; add prevention (tests, checks, training).
- Trend defects; review regularly.

**Pitfalls**

Fix symptoms; forget verification; no trend analysis.

**Quality gate**

High-severity issues show both a fix and a prevention that would have caught it earlier.

---

## 31) Documentation Plan & Templates

**Purpose**

Make docs discoverable, current, and useful.

**Do this**

Define what’s documented, where it lives, owners, and update cadence. Provide templates.

**Artifacts**

- Doc Index (ICD, Owner’s Guide, Release Notes, Runbooks, Training, FAQs)
- Templates (requirement spec, test case, RFC, release)

**Process & checklist**

- Link each doc to its source of truth (repo path).
- Set review cadence; archive superseded versions.

**Pitfalls**

Docs detached from code/data; stale content.

**Quality gate**

A new teammate can onboard using the docs alone.

---

## 32) Change Control & Release Management

**Purpose**

Control change; ship safely.

**Do this**

Use RFCs for non-trivial changes; tag versions; produce release bundles with notes and checksums.

**Artifacts**

- RFCs with decisions
- Version tags and Release Notes
- Release bundle (artifacts, BOM, ICDs, test report)

**Process & checklist**

- Submit RFC → review → approval → implement → test → tag → release.
- Stage/roll out with rollback plan.
- Keep a human-readable changelog.

**Pitfalls**

Hotfixes outside process; missing rollback.

**Quality gate**

Any release can be reproduced and rolled back cleanly.

---

## 33) Deployment/Installation Plan

**Purpose**

Ensure reliable, repeatable installs.

**Do this**

Write step-by-step procedures, pre-reqs, validation checks, and rollback.

**Artifacts**

- Installation Guide (operator-friendly)
- Validation checklist
- Rollback procedure

**Process & checklist**

- Dry-run on a clean environment; time the process.
- Define post-install health checks and acceptance criteria.

**Pitfalls**

Hidden pre-reqs; no validation or rollback.

**Quality gate**

A non-author can deploy successfully on first attempt.

---

## 34) Pilot/Beta Plan & Feedback Loop

**Purpose**

Learn safely before scaling.

**Do this**

Pick a small cohort, define goals and exit criteria, capture feedback and defects.

**Artifacts**

- Pilot Plan (cohort, goals, metrics, timeline)
- Feedback Log + actions
- Exit report (go/no-go, changes)

**Process & checklist**

- Instrument to capture metrics; run structured debriefs.
- Convert findings to backlog with owners/dates.

**Pitfalls**

“Soft” pilots with no exit criteria; feedback lost in chats.

**Quality gate**

Pilot yields at least 3 prioritized changes with owners.

---

## 35) Maintenance & End-of-Life (EOL)

**Purpose**

Plan longevity and predictability.

**Do this**

Define support windows, update cadence, spares, migration/EOL policy.

**Artifacts**

- Maintenance Policy (cadence, windows)
- EOL Plan and communication templates
- Spare/repair strategy

**Process & checklist**

- Publish support timelines and compatibility guarantees.
- Maintain SBOM and patch policies.

**Pitfalls**

Surprise deprecations; no migration path.

**Quality gate**

Users know how long they’re supported and how to migrate.

---

## 36) Security, Privacy & Data Protection

**Purpose**

Prevent/limit incidents and protect users.

**Do this**

Threat model, implement controls, maintain SBOM, test, and prepare incident response.

**Artifacts**

- Threat Model (assets, threats, mitigations)
- Security Controls Matrix (authN/Z, transport, storage, key mgmt)
- SBOM / dependency scan reports
- Incident Response Plan (roles, runbooks)

**Process & checklist**

- Least privilege, secure defaults, logging without secrets, key rotation.
- Run pen tests; fix high/critical findings before release.

**Pitfalls**

Over-collecting data; logging secrets; no IR practice.

**Quality gate**

You can show how a top threat is mitigated and tested.

---

## 37) Regulatory, Standards & Certification

**Purpose**

Legal access to markets and compliance.

**Do this**

Map applicable regulations/standards; plan pre-tests; collect evidence; certify.

**Artifacts**

- Applicability Matrix (regs/standards and sections)
- Test Plans & Reports
- Declarations/Certificates

**Process & checklist**

- Confirm versions/editions; plan labs; keep a compliance binder.
- Track surveillance/audits.

**Pitfalls**

Wrong standard revision; missing evidence retention.

**Quality gate**

An auditor can trace requirement → test → evidence.

---

## 38) Operations, SRE & Support

**Purpose**

Keep it healthy in the real world.

**Do this**

Define SLOs/SLIs, monitoring/alerts, runbooks, on-call, RMA/support workflows.

**Artifacts**

- SLOs & Alert Policies
- Runbooks (common incidents)
- On-call rotation; RMA/support SOPs

**Process & checklist**

- Tie alerts to user impact; test pages; do postmortems with actions.
- Track MTTR/MTBF trends.

**Pitfalls**

No error budgets; alerts no one actionably owns.

**Quality gate**

A simulated incident is resolved by on-call using runbooks.

---

## 39) Analytics, Experimentation & Voice of Customer

**Purpose**

Close the loop between usage and roadmap.

**Do this**

Define key metrics, implement tracking, collect feedback, run experiments, decide.

**Artifacts**

- Metric Dictionary & Tracking Plan
- VOC Repository (tickets, interviews, surveys)
- Experiment Plans & Results

**Process & checklist**

- Pick a North-Star + 3–5 guardrails; instrument ethically.
- Schedule VOC reviews; convert to prioritized backlog.

**Pitfalls**

Vanity metrics; feedback with no owner.

**Quality gate**

You can show a roadmap change justified by data/VOC.

---

## 40) Ethics, Safety & Responsible Use

**Purpose**

Reduce harm and ensure responsible outcomes.

**Do this**

Identify hazards/abuse cases, design mitigations, document residual risk, check accessibility.

**Artifacts**

- Hazard/Abuse Case Register
- Mitigation & Warning Matrix
- Accessibility checklist/results

**Process & checklist**

- Rate severity/probability; prefer design mitigations over warnings.
- Review with diverse users; document residual risk.

**Pitfalls**

Relying on disclaimers; ignoring a11y.

**Quality gate**

Top hazards have design mitigations and user-tested warnings where needed.

---

# Configuration Management Plan (CM) — Companion

**What this is**

A simple, enforceable system so there’s **one source of truth** for every artifact (docs, code, CAD, tests), with **baselines** and **releases** that anyone can reproduce.

**Why it matters**

Prevents “which version did we test?”, allows rollbacks, and lets a new person build the exact **as-built** unit from a tagged release.

**Artifacts to produce**

- **CM Plan (this page)**
- **Repo layout** (folders + naming convention)
- **Baseline register** (frozen snapshots of key docs)
- **Release register** (tagged, buildable drops)
- **As-Built Pack** (zip per release with evidence)

**How to build (step-by-step)**

1. **Create repo layout** (one repo or mono-repo):
    
    ```
    /docs
    /hardware      (CAD, gerbers, drawings)
    /firmware      (source, build scripts, binaries)
    /software      (apps, tools)
    /test          (plans, procedures, results/evidence)
    /ops           (runbooks, owner’s guides)
    /release       (as-built zips, manifests)
    
    ```
    
2. **Adopt naming/version rules** (semantic & readable):
    - Documents: `Reqs_vA1.md`, `ICD_vA1.md`, `TestPlan_vA1.md`, `BOM_vA1.csv`
    - Baseline label: `BR-A1` (links to exact doc versions included)
    - Release tag: `Rel-A1.0` (git tag), mirrors `/release/Rel-A1.0.zip`
3. **Define roles & permissions** (solo? still write it):
    - Who can **propose** changes vs. **approve** baselines/releases
    - Branch model: `main` (protected), `feat/*`, PR with review
4. **Create Baseline Register** (Notion database or CSV):
    - Fields: Baseline ID, Included Artifacts (refs), Rationale, Approver, Date, Hash/Tag
5. **Create Release Register**:
    - Fields: Release ID/Tag, Purpose, Included Baselines, Build Hash(es), Binaries, Test Evidence, Approver, Date
6. **Define As-Built Pack content** (zip per release):
    
    ```
    /docs  (PDFs of Reqs, ICD, Test Report)
    /hardware (gerbers, BOM CSV, drawings PDF)
    /firmware (bin/hex + commithash)
    /test (final report + key evidence)
    /manifest.txt (versions + hashes)
    
    ```
    
7. **Write the CM SOP** (how you’ll use it daily): see checklist’s SOP.

**Templates**

- **Baseline Register (CSV)**
    
    ```
    Baseline ID,Included Artifacts,Rationale,Approver,Date,Hash/Tag
    BR-A1,"Reqs_vA1; ICD_vA1; BOM_vA1; TestPlan_vA1",Freezefor Rev A design,"Tech Lead",2025-12-28,git:abc1234
    
    ```
    
- **Release Register (CSV)**
    
    ```
    ReleaseTag,Purpose,IncludedBaselines,BuildHash/Bin,TestEvidence,Approver,Date
    Rel-A1.0,"Rev A first usable","BR-A1","fw.bin (git:def5678)","/test/Report_A1.pdf","Owner",2026-01-02
    
    ```
    
- **Manifest (text)**
    
    ```
    Release: Rel-A1.0
    Docs: Reqs_vA1.md (sha256:...), ICD_vA1.md (...), TestReport_A1.pdf (...)
    Firmware: fw.bin (commit def5678, sha256:...)
    Hardware: BOM_vA1.csv (sha256:...), gerbers/ (zip sha256:...)
    
    ```
    

**Quality checks (don’t skip)**

- Repro test: clone → `git checkout Rel-XX` → rebuild artifacts **without edits**.
- Every release has a **Test Report** and **Trace Matrix** snapshot.
- No mutable links: evidence copied into `/release/Rel-XX/…` or content-addressed.

**Dual-Track callout (Hobby vs Product)**

- **Hobby minimum:** One repo; manual zip for each release; simple manifest; single approver (=you).
- **Product grade:** Protected branches; mandatory reviews; signed tags; artifact hashing; as-built pack; retention policy; offsite backup.

**Done-when**

- A stranger can rebuild the exact released unit from the **release tag** + **as-built pack**, and your **baseline register** explains what was frozen and why.

---

# Traceability Matrix — Companion

**What this is**

A living table linking **Requirements → Design/ICD/ADRs → Tests → Results/Evidence → Release**.

**Why it matters**

Proves you built **the right thing** and tested **every must-have**. Finds orphans (untested requirements, useless tests).

**Artifacts to produce**

- **Traceability Matrix** (Notion table or CSV under version control)
- **Coverage dashboard** (counts of PASS/FAIL/ORPHAN)
- **Exception/Waiver list** (with rationale & risk)

**How to build (step-by-step)**

1. **Freeze requirement IDs** (R-F-001…); keep them stable.
2. **Identify design anchors**: ICD sections, ADRs, code modules, schematics.
3. **Create/ID tests** (T-###) that **verify** each requirement (functional, performance, environmental, UX, interface).
4. **Define evidence**: file path to log, photo, plot, bin hash, etc.
5. **Build the matrix** (one row per requirement):
    
    ```
    Req ID, Requirement Text, DesignRef, Test ID,Result, Evidence, Notes
    
    ```
    
6. **Fill results** after execution; attach evidence; mark **PASS/FAIL/PARTIAL/WAIVED**.
7. **Add coverage metrics** (Hobby ≥ 90% must-haves; Product = 100% must-haves).
8. **Snapshot** the matrix for each release; store with the as-built pack.

**Templates**

- **Matrix (CSV)**
    
    ```
    Req ID,Requirement Text,Design Ref,Code/Module,Test ID,Result,Evidence Link,Notes
    R-F-001,"Shall display oil pressure",ICD §2.1,ui_display.c,T-001,PASS,/evidence/T-001.png,"10Hz verified"
    R-P-002,"Log ≥ 10Hz",ADR-LOG-001,logger.c,T-014,PASS,/evidence/T-014.csv,"Avg 14.8Hz"
    R-I-003,"No CAN faults",ICD §3.2,can_if.c,T-020,PASS,/evidence/T-020.log,"No DTCs"
    
    ```
    
- **Coverage summary (Markdown)**
    
    ```
    ## Coverage
    Must-have: 24/24 PASS (100%)
    Nice-to-have: 6/8 PASS (75%), 2 WAIVED
    Orphans: 0 requirements without tests; 0 tests without requirements
    
    ```
    

**Quality checks**

- No requirement without at least one verifying test.
- No test that maps to **zero** requirements (delete or relabel as exploratory).
- Evidence links resolve and are immutable in the release pack.

**Dual-Track callout (Hobby vs Product)**

- **Hobby:** One table; screenshots/logs stored in repo; **must-haves ≥ 90% PASS**, no safety WAIVED.
- **Product:** 100% **must-have** PASS; every waiver has hazard/risk note; automated coverage report.

**Done-when**

- For a release, every **must** requirement has **PASS** with evidence, and the matrix is included in the as-built pack.

---

# Calibration & Metrology — Companion

**What this is**

A repeatable way to align measurements (sensors/instruments) to a **known reference**, record offsets/uncertainty, and set **re-calibration intervals**.

**Why it matters**

If numbers drive decisions (safety, performance), they must be **trustworthy**. Calibration is how you prove it.

**Artifacts to produce**

- **Calibration Plan** (what gets calibrated, how often, by what method)
- **Calibration Procedures** (step-by-step per sensor/instrument)
- **Calibration Records** (unit-level results, offsets, uncertainty, next due)
- **Reference Log** (what standards you used, traceability info)

**How to build (step-by-step)**

1. **Inventory measurands**: what you read (e.g., pressure, temperature, voltage).
2. **Classify criticality**: safety-critical vs. informative (drives interval rigor).
3. **Pick reference**:
    - External standard (lab cert) or **golden unit** you trust (document why).
4. **Define acceptance criteria**:
    - Tolerance (e.g., ±2%), linearity, hysteresis, repeatability.
5. **Write procedure** (per sensor):
    - Stabilize, apply N points across range, record readings, compute error/offset, store calibration constants.
6. **Record results**:
    - Unit serial, date, environment, equipment, raw vs. corrected readings, calculated offsets, uncertainty, **next due date**.
7. **Update firmware/config** with new calibration constants; mark unit as **Calibrated**.
8. **Label** the unit (sticker: date, due date, by whom).
9. **Schedule re-cal** (calendar reminder) based on drift/usage.

**Templates**

- **Calibration Record (CSV)**
    
    ```
    UnitID,Sensor,Range,RefEquipment,Points,AvgError,Offset,Uncertainty,Pass/Fail,CalDate,NextDue,By,Evidence
    U-023,OilPressure,0-700kPa,RefGaugeSN123,0/100/300/500/700,"+0.8%","-1.9 kPa","±0.5%",PASS,2025-12-28,2026-06-28,AB,"/evidence/cal/U-023.pdf"
    
    ```
    
- **Procedure (Markdown)**
    
    ```
    ## Sensor: Oil Pressure
    1) Warm-up10 min; ambientstable.
    2) Apply0/100/300/500/700 kPausing reference gauge.
    3) Holdeachpoint ≥30s;log10 samples; compute mean.
    4) Calculate error vs reference; fit linearoffset.
    5) Storeoffsetin config; re-run300 kPato confirmwithin ±2%.
    6)Recordin CalibrationRecord; label unit.
    
    ```
    

**Quality checks**

- Reference device is within its own calibration date or justified as a golden unit.
- Post-cal verification point **passes** acceptance.
- Evidence (plots/logs) stored in release/evidence folder.

**Dual-Track callout (Hobby vs Product)**

- **Hobby:** Golden unit reference; 3-point check; offsets stored in a config file; **due date ~6–12 months**.
- **Product:** Traceable reference with certs; 5+ points with uncertainty; MSA optional; calibration stickers; system enforces **block on expired**.

**Done-when**

- Every **critical** sensor has a current, passing calibration record, and units carry applied offsets + next due date.

## Using This Guide

- Treat each **Quality gate** as non-negotiable.
- Keep everything **versioned** and **traceable**.
- Depth scales with novelty/risk: new domains → heavier §13–16 and §26–27.
- If you’re solo, these artifacts still save time and prevent rework; if you scale to a team, they become your onboarding and operating system.

If you want this split into **individual Notion templates** (one per section with pre-built tables and checklists), say the word and I’ll output them as drop-in pages.
