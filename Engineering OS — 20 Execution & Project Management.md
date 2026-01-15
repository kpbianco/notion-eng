# Engineering OS — Execution Infrastructure (Marketplace Draft)

### What this page is

This is the **execution infrastructure layer** for an Engineering OS.

Its job is to prevent the most common builder failure:

- The project only works on one machine.
- In one lab.
- With one person’s exact setup.

Use it to make work **repeatable**, **portable**, **safe**, and **findable** for:

- You
- Teammates
- Future customers

### How to use

Treat this as a supplemental system that supports normal project flow.

- Hobby projects: adopt the minimum safe setup.
- Professional projects: adopt full reproducibility and an audit trail.

---

## 10‑Minute Quickstart (do this today)

Create a folder called `ops/` (or a Notion section) and add:

1. **Known‑Good Toolchain** (versions + install steps)
2. **Lab Safety Rules** (power, ESD, batteries)
3. **File/Asset Naming Rules** (one page)
4. **Backup Plan** (what is backed up, where, how often)

Then pick one reproducibility method:

- Devcontainer / Docker (best), or
- “Known good versions” lockfile + scripted install.

If someone cannot clone and build within 30–60 minutes, you do not have infrastructure yet.

---

## 1) Toolchain Setup Guides

**Scope**: ECAD, MCAD, compilers, debuggers, analyzers.

### 1.1 Why the toolchain is a first-class artifact

Toolchains drift:

- Compilers change behavior
- SDKs break builds
- IDEs update silently
- Plugin versions mismatch

Your job is to define **Known Good**:

- Exact versions
- Install steps
- Validation checks

This turns “it broke” into “what changed?”

### 1.2 Toolchain inventory (what to document)

Create a **Toolchain Manifest** with:

**Hardware/Embedded**

- Compiler (GCC/Clang/ARM toolchain)
- SDK + version
- Flash tool + version
- Debugger (J‑Link/OpenOCD/etc.) + version
- Serial tools + drivers
- Python runtime + packages (if used for tooling)
- RTOS version (if applicable)

**Software/App**

- Language runtime version (Node/Python/Java/etc.)
- Package manager versions
- Build tools (CMake, Ninja, etc.)
- Linters/formatters

**ECAD/MCAD**

- CAD tool + version
- Libraries used + source
- Exporters + settings
- CAM outputs + settings

**Test/Analysis**

- Scope model + probe types
- Logic analyzer model
- Power supply model
- Measurement scripts versions

### 1.3 Install checks (the missing step)

Every toolchain guide must include a “verify install” step:

- Build a sample
- Flash a sample
- Run a script
- Generate a plot
- Open CAD and export a file

Rule: if you cannot verify, you cannot trust the install.

### 1.4 Known Good version strategy

Choose one:

**Option A: Simple pinning (fastest)**

- Document exact versions in Notion
- Store installers if allowed
- Disable auto-update where possible

**Option B: Devcontainer/Docker (best for repeatability)**

- Repo contains `Dockerfile` or `.devcontainer`
- One command creates an identical environment

**Option C: Scripted bootstrap**

- [`setup.sh`](http://setup.sh) installs dependencies
- Version checks run automatically

### Toolchain checklist (minimum)

- [ ]  Tool + version recorded for every critical element
- [ ]  Install steps documented
- [ ]  Verification step exists
- [ ]  Updates are controlled (not accidental)

---

## 2) Lab Setup & Safety

**Scope**: ESD, power discipline, fire safety, battery handling, chemicals.

### 2.1 Lab safety is engineering

Most lab incidents come from:

- Wrong supply voltage
- Current not limited
- Exposed conductors
- Li‑ion abuse
- “Just one quick test”

You will build faster and safer with discipline.

### 2.2 ESD basics (minimum viable)

You need:

- ESD mat (grounded properly)
- Wrist strap when handling sensitive ICs
- ESD-safe storage for boards

Rule: if you are touching unprotected boards, assume ESD risk exists.

### 2.3 Power discipline (the bring-up lifesaver)

Bring-up rule set:

- Always start with current limit low
- Increase in small steps
- Measure rails before connecting expensive parts
- Use a fuse or sacrificial bring-up harness where possible
- Know where the emergency off is

Brownout behavior: record what happens when voltage dips and returns.

### 2.4 Fire safety

Minimum:

- Appropriate extinguisher nearby
- Clear bench (no paper piles near hot tools)
- Do not leave high-energy tests unattended

### 2.5 Battery handling

Minimum:

- Charge on non-flammable surface
- Never charge damaged/swollen packs
- Store in safe container if possible
- Do not short leads

### 2.6 Chemicals basics (flux, solvents, adhesives)

Minimum:

- Ventilation
- Gloves when appropriate
- Proper storage
- Avoid mixing unknown solvents

### Lab safety checklist (minimum)

- [ ]  ESD controls exist and are used
- [ ]  Current limit always used for first power
- [ ]  Fire plan exists (extinguisher + clear area)
- [ ]  Battery handling rules written and followed
- [ ]  Hazardous chemicals stored/ventilated properly

---

## 3) File & Asset Hygiene

**Scope**: naming, hashes, manifests, release packs, storage/backup.

### 3.1 Goal: long-term retrievability

If you cannot find the right file six months later, it is not documentation. It is landfill.

This section enforces:

- Naming consistency
- Versioning
- Integrity (hashes)
- Backups

### 3.2 Naming conventions (simple and scalable)

Adopt:

- ISO dates: `YYYY-MM-DD`
- Revisions: `revA`, `revB` or `v0.3.1`
- Descriptive slugs: `power_bringup`, `icd_canbus`

Examples:

- `2026-01-04_revA_enclosure_step_export.step`
- `v0.3.0_fw_release_[notes.md](http://notes.md)`

### 3.3 File integrity (hashes)

Hashes prove a file did not change:

- Generate `sha256` hashes for release artifacts
- Store them in `checksums.sha256`

This protects you from:

- Accidental modifications
- Flashing the wrong file
- “Which file did we send the vendor?”

### 3.4 Manifests (what’s in a release)

A manifest tells you:

- What artifacts exist
- Their versions
- Their hashes
- What they’re for
- Build environment metadata

Rule: every shipped release gets a manifest.

### 3.5 Storage and backup strategy

Define:

- What is backed up (repo, CAD exports, evidence, release packs)
- Where (cloud + local)
- Cadence (daily/weekly)
- Retention policy
- Restore test (you must test restore)

Minimum:

- Git remote for code
- Cloud backup for CAD and evidence
- Local backup for critical exports

### Asset hygiene checklist

- [ ]  Naming convention documented and used
- [ ]  Releases have manifests + hashes
- [ ]  Evidence stored with context (not random screenshots)
- [ ]  Backup plan exists and restore has been tested once

---

## 4) Knowledge Base Patterns

**Scope**: Notion/docs that future-you can actually find.

### 4.1 The failure mode: wiki soup

Most Notion workspaces fail because:

- No structure
- No indexing
- Inconsistent naming
- Stale pages with no owner

You need a pattern:

- Consistent home page
- Consistent databases
- Consistent linking

### 4.2 The three-layer knowledge base model

**Layer 1 — Index (dashboard)**

- Project control panel
- Latest release
- Current risks
- Current milestone
- Quick links

**Layer 2 — Databases (structured truth)**

- Requirements
- Tests/Evidence
- Decisions (ADR)
- Parts/AVL
- Changes (ECO)
- Toolchain manifest

**Layer 3 — Pages (unstructured narrative)**

- Guides
- Deep dives
- Design notes
- Troubleshooting journals

Rule: searchable narrative is useful, but structured truth is what scales.

### 4.3 Page templates (so pages don’t rot)

Every page should include:

- Owner
- Last updated date
- Scope (what this page is for)
- Links to related records

Add a staleness banner:

- If not updated in X days, review.

### 4.4 Decision capture (linking to Module A/F)

Make it easy:

- Any major decision becomes an ADR entry
- ADR links to:
    - Risks it addresses
    - Tests verifying it
    - Release where it shipped

### Knowledge base checklist

- [ ]  One dashboard page per project
- [ ]  Databases for decisions/tests/releases exist
- [ ]  Page templates enforce owner/date/scope
- [ ]  Everything important is linked (no orphan pages)

# Engineering OS — Project Management for Builders (Marketplace Draft)

### What this page is

A lightweight execution + control system for engineering projects.

It helps you ship without chaos by providing builder-friendly versions of:

- Scoping and phasing
- Milestones and estimates
- Change control
- Supplier and lead-time risk
- Budgeting and unit economics
- Documentation and release hygiene

**Design goal**: strong enough for professional work, still usable for hobby builds.

---

## 10‑Minute Quickstart (apply today)

Create a Notion page called **Project Control Panel** with links to:

- `Scope & Phases`
- `Milestones & Estimates`
- `Risk Kill Log`
- `Change Log (ECR/ECO Lite)`
- `Supplier & Lead Time Tracker`
- `Budget + Unit Economics`
- `Docs System (ICD/ADR/Test/Release)`

Then write:

- Rev A objective (one sentence)
- Rev B objective (one sentence)
- Your next two-week sprint goal

If you cannot articulate Rev A, you are not ready to start building.

---

## 1) Scoping & Phasing

**Scope**: MVP, Rev A learn safely, Rev B refine, timeboxing, kill criteria.

### The core mistake this prevents

Most builders fail because they mix:

- Exploration
- Product polish
- Long-term architecture

into a single phase. That creates infinite scope.

### Phasing model

**Rev A = Learn Safely**

Goal: prove the concept, uncover scary unknowns, get something demonstrably working.

Rev A outputs (typical):

- Working end-to-end demo
- Evidence that key risks are bounded
- List of limitations and next steps
- Known-good snapshot (tag + release pack)

**Rev B = Refine + Harden**

Goal: make it reliable, manufacturable, maintainable.

Rev B outputs:

- Robustness improvements
- Test coverage expansion
- Packaging and serviceability improvements
- Cost and lead-time cleanup
- Better docs and onboarding

### MVP definition

MVP is the smallest version that:

- Delivers core value
- Can be tested
- Can be demonstrated
- Is safe enough

Bad MVP: “full feature set but buggy.”

Good MVP: “one killer path that works reliably with evidence.”

### Timeboxing

Use fixed time windows:

- Rev A timebox (e.g., 2–6 weeks)
- Spike timeboxes (1–4 hours for micro-prototypes)
- Learning tickets (90 minutes)

Timeboxing forces decisions and prevents “research as procrastination.”

### Kill criteria

Kill criteria are conditions that tell you to stop or pivot.

Examples:

- Cost exceeds limit by >2× with no realistic mitigation
- A key part is unobtainable on reasonable lead time
- Performance requirement is not reachable without full redesign
- Safety risk cannot be mitigated within constraints

If you do not define kill criteria, you will sink time indefinitely.

### Scope & Phasing checklist

- [ ]  Rev A goal is one sentence and testable
- [ ]  Rev B goal is one sentence and testable
- [ ]  MVP path is defined (happy path)
- [ ]  Timeboxes exist for learning and spikes
- [ ]  Kill criteria exist for the top three risks
- [ ]  Deferred items explicitly labeled “Rev B”

---

## 2) Milestones & Estimates

**Scope**: bottom-up hours/cost, buffers, risk-burn charts, kanban.

### Estimating truth

You are estimating uncertainty. Estimates are not promises. They are risk management.

Three estimate types:

- Optimistic: if nothing weird happens
- Most likely: normal friction
- Pessimistic: integration pain happens

If you only estimate “most likely,” you are lying to yourself.

### Bottom-up estimation (builder-friendly)

Break work into tasks that fit 30 minutes to 4 hours.

Estimate each task, then add:

- Integration tax (10–30% minimum)
- Buffer (15–40% depending on novelty)
- Lead-time slack (parts, vendor, shipping)

### Milestones that actually work

A milestone should include:

- Clear deliverable
- Pass criteria
- Evidence expectation

Examples:

- “Power stable under load step” (scope screenshot required)
- “Bus transaction verified” (logic analyzer capture required)
- “End-to-end demo recorded” (video/log required)

### Risk-burn charts (simple version)

Track your top risks and whether they are reduced.

Weekly score (0–5) for:

- Power risk
- Interface risk
- Supply chain risk
- Schedule risk
- Reliability risk

Goal: risk trends downward as milestones complete.

### Kanban for builders

Minimum columns:

- Backlog
- Ready
- Doing
- Blocked
- Done
- Shipped (optional)

Rule: limit Doing to 1–3 items max.

### Milestones & Estimates checklist

- [ ]  Tasks are broken into ≤4-hour chunks
- [ ]  Buffers exist explicitly
- [ ]  Milestones include pass criteria and evidence
- [ ]  Risk reduction tracked weekly
- [ ]  WIP limits exist

---

## 3) Change Control (ECR/ECO)

**Scope**: when to file, impact rubric, approvals, verification, communication.

### Why builders need change control

Without change control you get:

- Endless churn
- Undocumented behavior
- Broken compatibility
- “Why is this different than last week?”

Change control is memory and coordination.

### ECR vs ECO (lite)

- ECR (Change Request): proposal to change something
- ECO (Change Order): approved change to implement

Hobby version: a single database tracks both.

### When to file a change

File a change if it impacts:

- Interfaces (pinouts, connectors, protocols)
- Safety behavior
- BOM/parts
- Test plan requirements
- Mechanical fit
- Any release tagged as known-good

If it is cosmetic or internal refactor with no impact, commit messages are enough.

### Impact rubric

Score the change:

- Compatibility impact: breaks old parts? yes/no
- Rework cost: hours + scrap
- Schedule impact: days
- Risk impact: increases uncertainty?
- Verification impact: what must be re-tested?

If verification is not defined, the change is not approved.

### Change Control checklist

- [ ]  Every major change has an entry
- [ ]  Impact assessed before implementation
- [ ]  Verification steps listed
- [ ]  Changes communicated to stakeholders (including future-you)

---

## 4) Supplier & Lead-Time Risk

**Scope**: AVL, alternates, lifecycle flags, MOQ traps, obsolescence.

### Supply chain is part of engineering

A design that cannot be built is not a design.

### AVL basics

For each critical component, identify:

- Primary source
- At least one alternate
- Lifecycle status (Active/NRND/EOL)
- Lead time + MOQ

### Common traps

- MOQ traps: low unit price, forced large buys
- Lifecycle traps: parts trending toward EOL
- Counterfeit risk: sketchy marketplaces for ICs
- Single-source trap: one vendor, one footprint, no fallback

### Lead-time strategy

For long-lead items:

- Buy early
- Lock alternates
- Design footprints that accept multiple packages where feasible

### Supplier Risk checklist

- [ ]  Critical parts have alternates
- [ ]  Lifecycle status checked for critical parts
- [ ]  Lead times recorded and revisited before each rev
- [ ]  MOQ risks understood
- [ ]  Vendor links stored in the BOM tracker

---

## 5) Budgeting & Unit Economics

**Scope**: BOM vs COGS vs NRE, price breaks, breakeven, cash flow.

### The three costs to distinguish

- BOM: raw parts cost per unit
- COGS: BOM + labor + overhead + scrap + packaging
- NRE: non-recurring engineering (fixtures, tooling, dev time, certification)

Most builders underestimate labor and NRE.

### Price breaks and the volume illusion

Unit cost drops with volume only if:

- Demand exists
- Cash flow supports inventory
- Yield/scrap is managed

Do not optimize for volume economics before proving product value.

### Breakeven (simple)

Breakeven units ≈ NRE / (Price − COGS)

If (Price − COGS) is tiny, you do not have a business. You have a hobby.

### Cash-flow timing

When you pay matters:

- Suppliers often get paid before customers pay you
- Shipping and returns create lag

Track:

- Cash out date
- Cash in date
- Buffer needed

### Budget & Unit Econ checklist

- [ ]  BOM tracked with vendor links
- [ ]  Labor assumptions explicit
- [ ]  NRE listed separately
- [ ]  Breakeven math done (rough is fine)
- [ ]  Cash-flow timing considered

---

## 6) Documentation System

**Scope**: ICD, ADR, test evidence, CM plan, release notes, folder anatomy.

### Documentation is retrieval

Docs exist so:

- Others can build/test/maintain
- You can revisit decisions without churn
- You can ship reliable releases

### Minimum doc set

- ICD Lite: interfaces and assumptions
- ADR/Decision Log: why choices were made
- Test plan + evidence: proof, not claims
- Config management plan (CM Lite): versions and locations
- Release notes: what changed and how to use it

### Folder anatomy (recommended)

```
/docs
  /icd
  /decisions
  /test
  /manufacturing
/release
  /vX.Y.Z
    manifest.json
    checksums.sha256
    [notes.md](http://notes.md)

```

Notion indexes. Repo stores authoritative files.

### Documentation checklist

- [ ]  ICD exists for critical interfaces
- [ ]  Decisions logged (ADR)
- [ ]  Tests have evidence linked
- [ ]  Releases have manifests + notes
- [ ]  Folder structure consistent

# Engineering OS — Ops Pack (Marketplace Draft)

### What this page is

A marketplace-ready, Notion-native **Ops Pack** for an Engineering OS.

It’s designed to be implemented as a set of databases (or page + linked DBs). Each section includes:

- **Purpose** and **Definition of Done**
- Suggested **Fields** (schema)
- A **CSV Starter** for quick import
- A pragmatic **SOP** and **Gates**
- **Relations** so ops stays tied to releases, telemetry, security, and support

### How to use

1. Treat each section (G1–G10) as its own database.
2. Create each database using the **Fields** list.
3. Optional: copy the **CSV Starter** into a `.csv` and import it.
4. Re-run the gates before every release and after major changes.

---

## G) Ops Pack

## G1) Owner’s Guide v2 (User-Facing)

**Purpose**: Teach users to install, operate, and maintain the product safely.

**Definition of Done**: Step-by-step install, operation, troubleshooting, safety notes, and FAQs exist, with photos or screenshots.

**Fields**

- Audience (beginner/advanced)
- Install Steps (numbered)
- Operation (modes, indicators)
- Safety Warnings
- Maintenance (intervals)
- Troubleshooting (symptom → fix)
- FAQ
- Version

**CSV Starter**

```
Audience,Install,Operation,Safety,Maintenance,Troubleshooting,FAQ,Version
Beginner,"1..n","Modes A/B","Heat caution","Check X monthly","No display → check power","How to update?",v1.0

```

**SOP**

1. Write install and operation steps with photos.
2. Add safety warnings, maintenance intervals, and a troubleshooting table.
3. Validate by having a new user follow it end-to-end.

**Gates**

- **Entrance**: Feature set stable.
- **Exit**: A novice completes install and operation without help.

**Relations**: Release Notes, Service Notes, Support.

**Hobby vs Product**

- **Hobby minimum**: One page with key steps and photos.
- **Product grade**: Polished guide with localization readiness and accessibility checks.

---

## G2) Operations Runbook (Internal)

**Purpose**: Guide operators (you or a team) to deploy, monitor, and recover day-to-day.

**Definition of Done**: Start/stop procedures, health checks, alerts, backup/restore, and escalation paths are documented.

**Fields**

- Procedure (start/stop/update)
- Health Checks (what/how)
- Alert Thresholds
- Escalation (who/when)
- Backups/Restore Steps
- Maintenance Windows
- Known Issues
- Version

**CSV Starter**

```
Procedure,Health Checks,Alerts,Escalation,Backups,Maintenance,Known Issues,Version
Deploy v1.2,"Heartbeats; disk","CPU>80% 10m","On-call","Nightly S3","Sun 02:00–03:00","Rare timeout",v1.2

```

**SOP**

1. Document start/stop/update procedures.
2. Define health checks and alert thresholds.
3. Add backup/restore steps and escalation trees.
4. Keep known issues current.

**Gates**

- **Entrance**: Release candidate ready.
- **Exit**: Runbook dry-run succeeds without tribal knowledge.

**Relations**: Owner’s Guide, Telemetry, DR/Backups.

**Hobby vs Product**

- **Hobby minimum**: Personal notes for starting/stopping and quick fixes.
- **Product grade**: Full on-call playbook with paging and recovery drills.

---

## G3) Service & Repair Notes

**Purpose**: Enable repeatable, safe servicing and part replacements.

**Definition of Done**: Disassembly steps, parts list, torque/specs, ESD cautions, and a test-after-service checklist exist.

**Fields**

- Procedure (component)
- Tools/Consumables
- Safety/ESD Notes
- Steps
- Specs (torque/clearances)
- Parts (PNs)
- Test After Service
- Time/Skill Level

**CSV Starter**

```
Procedure,Tools,Safety,Steps,Specs,Parts,TestAfter,Time/Skill
Replace screen,"#0 phillips; spudger","ESD mat","1..n","0.4Nm","LCD-123","Run display test","15m/Basic"

```

**SOP**

1. Write step-by-step instructions with photos.
2. Add specs and parts cross-references.
3. Define post-service tests.

**Gates**

- **Entrance**: Hardware finalized.
- **Exit**: A new tech can perform service unaided.

**Relations**: BOM, Change Control, Owner’s Guide.

**Hobby vs Product**

- **Hobby minimum**: Short notes with key pitfalls.
- **Product grade**: Illustrated procedures with parts kits and QA checks.

---

## G4) Release & Deployment Checklist

**Purpose**: Ship safely and repeatably.

**Definition of Done**: Pre-release gates met. Artifacts signed. Docs updated. Rollback plan ready.

**Fields**

- Release ID/Notes
- Artifacts (hash/signature)
- Test Evidence Pack (link)
- SBOM & Licenses (link)
- Known Issues
- Rollback Plan
- Comms (internal/external)
- Approvals
- Status

**CSV Starter**

```
Release,Artifacts,Evidence,SBOM,Known Issues,Rollback,Comms,Approvals,Status
v1.2,"sha256:...; sig:...",evidence_link,sbom_link,"P3 cosmetic","Revert to v1.1",notes_link,"Eng/QA/PM",Ready

```

**SOP**

1. Verify test, SBOM, and security gates.
2. Publish notes and artifacts with hashes and signatures.
3. Stage rollback and obtain approvals.

**Gates**

- **Entrance**: All test suites green.
- **Exit**: Release published and rollback validated.

**Relations**: Test Pack, SBOM, Build Reproducibility.

**Hobby vs Product**

- **Hobby minimum**: Tag + short notes + backup.
- **Product grade**: Signed artifacts, SBOM, approvals, staged rollback.

---

## G5) Telemetry, Observability & Health

**Purpose**: See system health and detect issues early.

**Definition of Done**: Key metrics and events defined. Dashboards and alerts live. Retention and privacy aligned.

**Fields**

- Metric/Event
- Source
- Frequency
- Threshold/Alert
- Dashboard Link
- Retention
- Owner

**CSV Starter**

```
Metric,Source,Frequency,Threshold,Dashboard,Retention,Owner
Update rate,Device,"10s avg","<10Hz alert",Grafana,30d,Alex

```

**SOP**

1. Choose SLOs and define metrics and events.
2. Build dashboards and alerts. Test with synthetic events.
3. Align retention with privacy/data policy.

**Gates**

- **Entrance**: Core features done.
- **Exit**: On-call can triage using dashboards alone.

**Relations**: Data Handling, Runbook, Incident Response.

**Hobby vs Product**

- **Hobby minimum**: Simple logs plus a couple of graphs.
- **Product grade**: SLOs, dashboards, alert hygiene, audit trail.

---

## G6) Support Process & SLAs (if external users)

**Purpose**: Provide predictable support with clear expectations.

**Definition of Done**: Intake channels, severity levels, response and resolve targets, and knowledge base exist.

**Fields**

- Channel (email/portal)
- Severity (S1–S4)
- Response Target
- Resolve Target
- Ownership
- Escalation
- KB Article (link)
- Status

**CSV Starter**

```
Channel,Severity,Response,Resolve,Owner,Escalation,KB,Status
Portal,S2,8h,3d,Support,"Mgr on 24h",install_guide,Active

```

**SOP**

1. Define severity levels and targets.
2. Set intake and triage. Build the KB.
3. Track metrics and iterate.

**Gates**

- **Entrance**: Users beyond you.
- **Exit**: SLA metrics tracked. Escalations work.

**Relations**: Owner’s Guide, Incident Response, Ops.

**Hobby vs Product**

- **Hobby minimum**: Email plus personal response.
- **Product grade**: Ticketing, SLAs, KB, metrics.

---

## G7) Backups, Restore & Disaster Recovery

**Purpose**: Ensure data and configurations survive failures.

**Definition of Done**: Backup schedules, integrity checks, restore drills, and RPO/RTO targets exist.

**Fields**

- Asset (data/config)
- Backup Method/Schedule
- Retention
- Encryption
- RPO/RTO
- Last Restore Test (date/result)
- Owner

**CSV Starter**

```
Asset,Method,Retention,Encryption,RPO/RTO,Last Restore,Owner
Configs,"S3 nightly",30d,KMS,"24h/4h","2025-12-01 Pass",Alex

```

**SOP**

1. Identify assets and define schedule and encryption.
2. Test restore quarterly and record results.
3. Compare to RPO/RTO and adjust.

**Gates**

- **Entrance**: Data exists you care about.
- **Exit**: Restore drill passed within targets.

**Relations**: Runbook, Data Handling, Security.

**Hobby vs Product**

- **Hobby minimum**: Manual backup to external drive/cloud.
- **Product grade**: Automated encrypted backups plus documented restore drills.

---

## G8) Compatibility & Versioning Policy

**Purpose**: Avoid breaking users. Plan forwards and backwards compatibility.

**Definition of Done**: Versioning scheme, compatibility matrix, migration, and rollback procedures exist.

**Fields**

- Component
- Version (semver)
- Compatible With
- Breaking Changes (Y/N + notes)
- Migration Steps
- Rollback Steps
- Test Ref

**CSV Starter**

```
Component,Version,CompatibleWith,Breaking,Migrate,Rollback,Test
Firmware,1.2,"App>=2.0",N,"OTA steps","Reflash 1.1",TC-compat-03

```

**SOP**

1. Choose semver and publish compatibility matrix.
2. Document migration and rollback.
3. Add compatibility tests to release.

**Gates**

- **Entrance**: Multiple components/versions.
- **Exit**: Users can upgrade safely.

**Relations**: Release Checklist, Owner’s Guide, Test Strategy.

**Hobby vs Product**

- **Hobby minimum**: Note which versions work together.
- **Product grade**: Formal matrix, tests, migration tooling.

---

## G9) Decommissioning & EOL Plan

**Purpose**: Provide a dignified end of life with security and user-data safety.

**Definition of Done**: EOL notice, last supported versions, post-EOL security stance, and export/deletion steps exist.

**Fields**

- Product/Version
- EOL Date
- Final Update
- Support Window
- Security Statement
- Data Export/Deletion Instructions
- Comms Plan

**CSV Starter**

```
Product,EOLDate,FinalUpdate,SupportWindow,Security,Data Export,Comms
Device v1,2027-12-31,"1.3 LTS","12 months","No new CVEs patched","How-to guide","Email + site"

```

**SOP**

1. Announce timeline and provide LTS if applicable.
2. Publish export and deletion guides.
3. Archive docs and disable endpoints as planned.

**Gates**

- **Entrance**: Next gen planned or end decided.
- **Exit**: Users informed. Data handled responsibly.

**Relations**: Privacy, Release Notes, Support.

**Hobby vs Product**

- **Hobby minimum**: Stop using and save your data.
- **Product grade**: Public EOL notice, LTS path, data and security stance.

---

## G10) Knowledge Base & FAQ

**Purpose**: Capture repeat answers and reduce support load.

**Definition of Done**: Top issues have step-by-step resolutions with visuals. Content is searchable and maintained.

**Fields**

- Topic
- Problem Statement
- Resolution Steps
- Screenshots/Video
- Related Articles
- Last Reviewed
- Owner

**CSV Starter**

```
Topic,Problem,Resolution,Media,Related,Last Reviewed,Owner
No boot,"Stuck at logo","1..n steps",video_link,"Power issues",2025-12-28,Alex

```

**SOP**

1. Mine support and telemetry for top problems.
2. Write clear steps with visuals.
3. Review monthly and retire stale items.

**Gates**

- **Entrance**: First release shipped.
- **Exit**: Top issues covered and support hit rate declines.

**Relations**: Support, Owner’s Guide, Runbook.

**Hobby vs Product**

- **Hobby minimum**: Personal notes and fixes.
- **Product grade**: Public KB with analytics, ownership, and update cadence.