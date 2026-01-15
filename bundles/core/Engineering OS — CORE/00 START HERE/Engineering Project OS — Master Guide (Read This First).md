# Engineering Project OS — Master Guide (Read This First)


## 0) What this is (and why it exists)

You’re going to treat **any serious project** like a product with customers (even if the customer is you). This master guide explains:

- The **philosophy** (why we do things in this order).
- **How to use** the OS (checklists, templates, companion explanations, and the worked example).
- **What “done” looks like** at each step (so you don’t move on half-baked).
- How to keep evidence, trace decisions, and avoid rework.

**Core mindset**

- Plan **before** you buy/build.
- Prove the riskiest assumptions **early** with tiny experiments.
- **Freeze interfaces** so you stop churning.
- March in **milestones** with explicit proofs.
- **Verify** against requirements.
- Capture the **story** so others (and future-you) can use it.

---

## 1) What’s in the OS (components you’ll use)

1. **Master Checklist (1–40)** – A soup-to-nuts sequence from Vision→Verification. This is the **to-do spine**.
2. **Companion Doc (“What/Why/How/Done”)** – A plain-English explainer for each checklist item:
    - **What it is** (definition)
    - **Why it matters** (value)
    - **Inputs** you need
    - **Steps** to do
    - **Outputs** you must produce
    - **Quality bar** (how to know it’s good)
    - **Evidence** to save
3. **Planning + Architecture Templates** – Vision, Requirements, Domain Breakdown, Risk Kill Log, Block Diagram, Pin/Interface Map, Power/Data Flow, Milestone Plan.
4. **Execution + Integration Templates** – Build Log, Issues List (MUST-FIX vs Rev-B), Test Procedures, Verification Matrix, Owner’s Guide, Release Checklist, CCR/ECO forms.
5. **Documentation Standards** – Naming, versioning, traceability, ICD/Interface tables, change control.
6. **Worked Example (Flow Log 1–40)** – A full, **first-person** walk-through of the process on a real project. Use it to see the bar, not to copy specifics.

---

## 1.5) Project Type Router (Pick a Path + Know What to Read)

This OS is intentionally universal. The router prevents “I have 50 pages, what do I do?” Pick **(A) a delivery path** and **(B) a project archetype**. Then follow the recommended reading + gates.

### A) Choose your delivery path

### Path H — Hobbyist (learn + build)

**Use when:** personal project, low consequence failures, no external users, no safety-critical environment.

**Goal:** move fast while still being disciplined.

**Non-negotiable gates (Hobbyist minimum):**

- **Item 1 Vision**, **Item 2 Requirements (lite)**, **Item 3 System Breakdown**, **Item 4 Risk Kill**, **Item 5 Interface Freeze**, **Item 6 Milestones**, **Phase 8 Verification (lite)**
- Evidence capture still required (photos/logs/screenshots).

**Allowed simplifications:**

- Requirements can be **10–20 max** with 1 test each.
- Traceability can be a **single table** (Req → Test → Evidence link).
- Change control can be “Decision Log + Rev bump” instead of formal ECO workflow.

**Hard stop even in hobby mode:**

- High voltage/mains, lithium packs without protections, anything that can injure someone, anything installed in a vehicle in a way that can affect safety systems → treat as **Pro path** or require an SME.

---

### Path P — Professional (ship + support)

**Use when:** external users, safety risks, regulated domains, business claims, warranty/support expectations, meaningful data/privacy/security exposure.

**Professional minimum adds:**

- Stronger **requirements quality bar** (measurable, testable, versioned baseline)
- Formal-ish **change control** (CCR → ECO when needed)
- **Test Strategy Ladder** (unit→integration→system; environmental if relevant)
- **Release packaging** (manifest, hashes, versioning, owner’s guide/runbook)
- **Security/privacy** if data is collected or device is connected
- **Supply chain/DFX** considerations if more than a handful of units

**Rule of thumb:** if you’d feel bad when it fails, you’re in Pro path.

---

### B) Choose your project archetype (what pages to read first)

Use this as your “what to open first” map. You’re not reading everything—just the relevant primers to avoid rookie traps.

### 1) Sensor logger / telemetry device (embedded + data)

**Examples:** CAN logger, environmental monitor, race telemetry box

**Read first:**

- **Engineering OS — Meta Learning** (unknowns → learn tickets; debugging loop)
- **Engineering OS — EE Fundamentals** (power basics, buses, storage, boot/OTA basics)
- **Engineering OS — Software** (data logging schemas, time bases, scripting + plotting)
- **Engineering OS — Testing / Test Strategy** (evidence discipline, verification matrix)
- **Engineering OS — Tooling** + **Tooling Bridges** (instrumentation primer, bench ops)

**High-risk gotchas:** power integrity resets, logging corruption, time sync, connector strain relief.

---

### 2) Motor/actuator controller (PWM, drivers, noise-sensitive)

**Examples:** fan controller, solenoid driver, small BLDC/stepper system

**Read first:**

- EE Fundamentals: **power, transients, ground/returns, EMC/ESD**
- Software: **timing/concurrency basics**, watchdogs
- Tooling: **scope probing + current measurement basics**
- Testing: **fault injection mindset + acceptance tests**

**High-risk gotchas:** inductive kickback, brownouts, EMI coupling into logic.

---

### 3) Battery-powered portable device (power + enclosure + UX)

**Examples:** handheld tool, portable sensor node

**Read first:**

- EE Fundamentals: **regulators, brownout behavior, storage hardening**
- Mechanical: **packaging/mounting, thermal, vibration**
- Compliance: **battery safety fundamentals** (even hobby mode)
- Tooling: **assembly quality + bench infrastructure**

**High-risk gotchas:** charging safety, undervoltage behavior, thermal buildup, connector wear.

---

### 4) IoT / networked product (software-heavy + privacy)

**Examples:** Wi-Fi device, cloud dashboard, remote updates

**Read first:**

- Software: **security & privacy**, local vs cloud decisions, CI/CD basics
- EE Fundamentals: **boot/OTA strategy** (safe updates + rollback)
- Testing: **system tests + reliability lite**
- Compliance: if you transmit RF, **regulatory roadmap awareness**

**High-risk gotchas:** secrets handling, update bricking, data retention, user trust.

---

### 5) Mechanical bracket/fixture/tool (minimal electronics)

**Examples:** mounts, rigs, jigs, adapters

**Read first:**

- Mechanical: **fasteners/tolerancing**, materials/processes
- Tooling: **workholding, metrology, cut/drill/grind**, assembly inspection
- Testing: **fit checks, load checks**, evidence photos + measurements

**High-risk gotchas:** wrong fasteners, tolerance stackups, poor workholding = misaligned holes.

---

### 6) Enclosure / packaging-first project

**Examples:** rugged case, sealed box, serviceable enclosure

**Read first:**

- Mechanical: **packaging/mounting**, ingress, strain relief, serviceability
- Compliance (lite): **safety fundamentals** as relevant
- Tooling: **file formats (STEP/DXF)**, finishing stack, assembly quality

**High-risk gotchas:** cable routing, access for rework, seal failures, fastener stripping.

---

### 7) Test fixture / lab tool

**Examples:** harness tester, jig, automated measurement rig

**Read first:**

- Testing: **fixtures & instrumentation**, measurement uncertainty basics
- Tooling: **bench ops + labeling standards**, assembly inspection
- Software: **scripting for engineers**, plotting/report generation

**High-risk gotchas:** flaky wiring, unclear pass/fail criteria, unrepeatable measurements.

---

### 8) Software-only tool (no hardware)

**Examples:** planner app, data pipeline, analysis tool

**Read first:**

- Meta Learning: trade studies, decision logs, debugging loop
- Software: version control, CI, code quality lite, UX basics, security/privacy if relevant
- Testing: test strategy ladder (unit/integration/system)

**High-risk gotchas:** scope creep, missing acceptance criteria, no release packaging.

---

### C) “Hobby vs Professional” gate overlays (quick rules)

- **Hobby:** Lite requirements + Lite verification + simple decision log; still do risk-kill and freeze interfaces.
- **Professional:** Full traceability mindset; stronger test ladder; change control discipline; release pack; security/privacy.

If you’re torn: start Hobby for Rev A learning, then switch to Pro for Rev B shipping.

---

## 2) How to use this OS (quick start → deep)

### A. 30-minute quick start (get oriented)

- Duplicate the workspace.
- Rename it to your project.
- Open the **Master Checklist (1–40)**.
- Skim the **Companion Doc** for Items 1–8 (Vision → Interface Freeze).
- Open the **Flow Log** to see how a completed path looks.

### B. One-day Planning Sprint (recommended)

1. **Vision & Success** (Item 1): Write the Problem, Outcome, Who Benefits, Success definition.
2. **Requirements** (Item 2): Draft functional, performance, environmental/physical, interface, UX. Make them **measurable**.
3. **System Breakdown** (Item 3): List domains (mech/elec/firmware/software/test/etc.), responsibilities, **open questions**.
4. **Risk Kill Plan** (Item 4): Pick the **3–5 design-killer unknowns** and design micro-prototypes (fast, ugly, focused).
5. **Calendar Milestones** (Item 6): Define M1–M4 with goal, proof, blockers, hours, cost.

> Gate rule: Do not proceed if Vision, Requirements, Domain Breakdown, and Risk-Kill Plan aren’t written.
> 

### C. Weekly cadence (build without chaos)

- Execute next **milestone only**.
- Update **Build Log** and **Issues List** as you go.
- If an interface changes → raise a **CCR** (Item 34) and update artifacts.
- End of week: **Verification against current requirements** touched by the milestone.

---

## 3) Phase gates (what must exist before you move on)

**Phase 1 — Vision & Success**

- Output: Vision Statement (problem, outcome, beneficiary, success).
- Quality bar: A non-technical person can understand what you’re building and why in **60 seconds**.

**Phase 2 — Requirements**

- Output: Requirement list with IDs and measurable criteria.
- Quality bar: Each requirement has a testable PASS/FAIL; no “nice/good/fast”.

**Phase 3 — System Breakdown**

- Output: Domain responsibilities + **open questions**.
- Quality bar: Unknowns are explicit; you can point to 3–5 that would sink the design if wrong.

**Phase 4 — Risk Kill / Pre-Prototypes**

- Output: Risk Kill Log (Question → Experiment → Result → Decision).
- Quality bar: Design-killer unknowns are either resolved or replaced with a clear decision.

**Phase 5 — Interface Freeze**

- Output: Block Diagram, Interface/Pin Map (or equivalent), Power/Data Flow.
- Quality bar: Every connection is labeled (what, voltage/rate, direction). Changing it later = **Rev bump**.

**Phase 6 — Build Plan & Schedule**

- Output: Milestones with goal, proof, blockers, hours, cost.
- Quality bar: Each milestone has an objective **demo condition**.

**Phase 7 — Implementation & Integration**

- Output: Build Log + Issues List (MUST-FIX vs Rev-B) kept current.
- Quality bar: You only build what the **current milestone** needs and prove it immediately.

**Phase 8 — Verification, Handoff, Story**

- Output: Verification Matrix (PASS/FAIL), Owner’s Guide, Next-Rev Notes, optional 1-page pitch.
- Quality bar: A skeptical reviewer can trace each requirement to evidence.

---

## 4) How to fill **any** checklist item using the Companion Doc

For each item (1–40):

1. **Open the Companion Doc entry** for that item.
2. Work top-to-bottom:
    - **What** it is → sanity check you’re doing the right thing.
    - **Why** it matters → focus on value, not ceremony.
    - **Inputs** → gather what’s needed before you start.
    - **Steps** → do them in order (don’t skip).
    - **Outputs** → produce the artifacts; name and file them.
    - **Quality bar** → compare; raise issues if you miss it.
    - **Evidence** → paste links/files so the trail is complete.
3. **Gate**: If outputs aren’t produced to the quality bar, you’re **not done** with that item.

### Concrete example (how you’ll actually write it)

**Item 2 — Requirements (excerpt)**

- **Inputs**: Vision, rough sketches, any constraints you already know (budget, size, interfaces).
- **Steps**: Write 5 categories (functional, performance, environment/physical, interfaces, UX). Add measurable numbers. Assign IDs.
- **Outputs**: `Requirements.md` with R-IDs, and a draft **Verification Matrix** with the test you plan for each.
- **Quality bar**: Every R-ID has a measurable target; a test method exists; nothing is implied.
- **Evidence**: Link to doc; short note in Build Log that requirements were baselined v0.1.

**Item 4 — Risk Kill (excerpt)**

- **Inputs**: Open questions list; top 3–5 design-killers.
- **Steps**: Design **micro-prototypes** (1–4 h each), run them, write what you learned, make a decision.
- **Outputs**: `RiskKill_Log.md` (table).
- **Quality bar**: No design-killer remains untested; each has a decision captured.
- **Evidence**: Photos, scope captures, code snippets, or quick CSVs attached.

> You’ll repeat that pattern for every item. The Companion Doc gives you the exact prompts and acceptance criteria.
> 

---

## 5) Documentation & traceability (the rules of the road)

- **Name files predictably**: `01_Vision/…`, `02_Requirements/…`, … `08_Verification/…`.
- **Version everything**: Docs get dates or minor versions; firmware/hardware follow semantic and Rev naming.
- **ICD / Interface Map** is the source of truth. Changing it requires a **CCR**; approved changes execute via **ECO**.
- **One decision, one place**: Decisions live where they were made (Risk Kill Log, CCR, Milestone review), and are **linked** forward.
- **Evidence or it didn’t happen**: Screenshots, photos, logs, plots. Keep them with the artifact.

---

## 6) How the Worked Example helps you

- The **Flow Log (1–40)** is a **fully applied** run through the process for a real project.
- Use it to benchmark **depth and clarity**.
- When you’re unsure how detailed your artifact should be, open the corresponding step in the Flow Log and match the **quality bar**, not the domain specifics.

---

## 7) Time budgeting (so you finish)

- Expect **30–50%** of total project effort in **planning + risk kill + interface freeze**.
- Milestones should be **days, not months**; each produces visible proof.
- If you’re truly building a throwaway learning prototype, **label it** as such and skip gates intentionally (don’t hide a prototype inside a “product” path).

---

## 8) Adapting across disciplines (solo or small team)

- Swap domain names as needed (e.g., **mechanical packaging** → **content pipeline** for media, **CAN ICD** → **API/contract** for software-only).
- The **gates don’t change**: requirements, risk kill, interface freeze, milestone proofs, verification.
- If you add people, set a lightweight **RACI** per milestone (who owns what; approval = you).

---

## 9) Common failure modes (and the built-in guardrails)

- **Buying parts before requirements** → Guardrail: Gate on Item 2.
- **Infinite architecture churn** → Guardrail: Item 5 (Freeze) with Rev bumps.
- **Hero debugging at 3 a.m.** → Guardrail: Item 6 (Milestone proofs) + Item 7 (Issues List triage).
- **“We’ll document later”** → Guardrail: Evidence attached before you tick “done”.
- **Confusion later** → Guardrail: Owner’s Guide + Verification Matrix in Phase 8.

---

## 10) What “sell-grade” means here

- A new graduate can follow the sequence without prior domain knowledge.
- A senior reviewer can audit requirements → architecture → tests → results and find no gaps.
- Artifacts are **unambiguous**, **measurable**, and **traceable**.
- The package is **publishable**: demo, guide, and verification tell a coherent story.

---

## 11) Your first hour (exact steps)

1. Open **Master Checklist (1–40)** → create a new project instance.
2. Fill **Item 1** using the Companion Doc. Save `01_Vision/Vision.md`.
3. Fill **Item 2**; create `02_Requirements/Requirements.md` + a stub Verification Matrix.
4. Fill **Item 3**; list open questions.
5. Plan **Item 4**; schedule 2–3 micro-prototypes this week.
6. Skim the **Flow Log** for Items 1–6 to internalize the quality bar.
7. Put the next milestone on your calendar.

That’s it. You’re now operating the OS.

---

## 12) FAQ (short)

- **Can I combine steps?** Only if outputs and quality bars are met.
- **When do I change interfaces?** When a CCR is approved; bump Rev and update artifacts.
- **What if I don’t know a term in a step?** Open the **Companion Doc** entry for that item; it defines terms and shows exactly how to do it.
- **What if I’m short on time?** Shrink scope, not gates. Keep the gates; reduce what “Rev A” includes.

---

## 13) Index (where to go next)

- **Pick your path**: Project Type Router (Hobby vs Professional + archetypes)
- **Start here**: Master Checklist (1–40)
- **Use while filling**: Companion Doc (What/Why/How/Done for every item)
- **See the bar**: Worked Example (Flow Log 1–40)
- **When changing things**: CCR/ECO templates
- **When shipping**: Owner’s Guide + Release Checklist
- **When improving**: Metrics Dashboard + Next-Rev Notes
