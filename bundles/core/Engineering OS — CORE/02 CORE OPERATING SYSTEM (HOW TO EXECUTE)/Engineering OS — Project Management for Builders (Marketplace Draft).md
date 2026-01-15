# Project Management for Builders (Marketplace Draft)

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
