# Engineering Project OS — Master Guide (Read This First)

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

# Engineering OS — Starter Guide (Marketplace Edition)

<aside>
🧭

**Purpose**: Prevent overwhelm and avoid unsafe, too‑large projects.

This guide gives you a Day 0 → Day 7 runway, a simple triage flow to pick a winnable project, and clear “stop and ask for help” gates.

**Who this is for**: Anyone willing to follow instructions and learn. No engineering background required.

**Outcome**: A working project *or* an evidence‑backed decision to re‑scope before you burn weeks.

</aside>

---

### 1) The big idea (read once)

Most projects fail for one of three reasons:

1. **Scope is too big.** You tried to build a “platform.”
2. **Unknowns are unmanaged.** You do not know what you do not know.
3. **No pass bars, no evidence.** You cannot tell whether you are making progress.

This Engineering OS solves those problems *if you start with a safe project class and follow the runway*.

---

### 2) Project triage wizard (pick a safe, winnable project)

#### Step 1 — Choose your project class

Pick the *highest* class that matches. If multiple apply, assume the **highest risk**.

**Class 0 — Software‑only**

- Examples: automation script, dashboard, data parser
- Risk: low
- Best for beginners

**Class 1 — Low‑power electronics (USB / ≤ 12V, no big motors, no large batteries)**

- Examples: sensor logger, BLE telemetry, small controller
- Risk: moderate‑low
- Strong “first hardware” class

**Class 2 — Moderate power / actuators**

- Examples: small motor control, automotive accessory (non‑control), higher current
- Risk: moderate‑high
- Requires stronger safety and test discipline

**Class 3 — High‑risk / regulated**

- Examples: mains AC, medical claims, safety‑critical automotive control, aviation, high‑power batteries, certified RF end‑products
- Risk: high
- **Requires SME review and/or test lab involvement at gates**

**Hard rule:** If you are new and your project is Class 3, do not start there. Re‑design into Class 0–1 first as a “safe pilot.”

---

#### Step 2 — Red‑flag gate (instant stop / re‑scope triggers)

If any of these are true, you must either downscope to a safe pilot or bring in an SME.

**Stop triggers**

- plugs into a wall outlet (mains)
- lithium battery pack bigger than a “small gadget battery”
- can cause physical harm if it fails (heat, motion, vehicle control)
- collects sensitive personal data (location, audio/video tied to identity)
- claims anything medical, diagnostic, or therapeutic
- radio transmitter in a sellable product and you do not understand certification pathways

If you hit a stop trigger, the next task is not “build.” It is “risk plan + safety gate.”

---

#### Step 3 — Pick a starter archetype (do not invent a new category)

Choose **one** archetype. These are designed to teach skills without forcing a death‑march.

**A) Data Logger**

- Input: sensor data
- Output: file/log/plot
- Teaches: buses, timing, storage, evidence

**B) Simple Controller**

- Input: buttons/sensor
- Output: actuator/LED/display
- Teaches: state machines, timing, safe defaults

**C) Measurement Tool**

- Input: signal
- Output: measurement report
- Teaches: instrumentation, uncertainty, test discipline

**D) Software Utility**

- Input: files/data
- Output: transformed output/dashboard
- Teaches: automation, packaging, UX

Pick one. Resist “A + B + C” until Rev B.

---

### 3) Difficulty ladder (what you are allowed to attempt)

**Level 1 — Safe starter (recommended)**

- Allowed:
    - USB power or ≤ 12V wall adapter
    - no high‑current loads
    - no mains
    - no safety‑critical control
    - small datasets, local storage
- Goal:
    - working prototype + evidence pack

**Level 2 — Builder**

- Allowed:
    - moderate power (careful)
    - more complex integrations
    - vehicle accessory *non‑control* (telemetry only)
- Goal:
    - Rev A stable + basic reliability checks

**Level 3 — Advanced / pro gates**

- Allowed:
    - mains, high‑power battery, safety‑critical, regulated markets
- Goal:
    - compliance roadmap + formal test plan + SME reviews

---

### 4) The Day 0 → Day 7 runway

#### Day 0 (60–90 minutes) — Define the build so it cannot sprawl

Create a **Project Control Panel** and fill:

- One‑sentence goal: “This project will ___.”
- Non‑goals: “It will NOT ___.”
- Success criteria (3 bullets): measurable outputs
- Constraints: budget, time, tools
- Project class + difficulty level
- Starter archetype selected

**Pass bar (Day 0):** you can explain what you are building in 30 seconds and what you are *not* building.

---

#### Day 1 (90 minutes) — Unknowns Map → top Learn Tickets

Create an **Unknowns Map**:

- list 20 unknowns (do not filter)
- cluster them
- rank top 5 by “blocks progress” + risk
- convert top 3 into 90‑minute Learn Tickets

**Pass bar (Day 1):** top 3 Learn Tickets exist with measurable pass bars.

---

#### Day 2 (90 minutes) — Risk Kill Log → choose one scary question to answer

Create **Risk Kill Log** entries for the top 3 risks.

Pick **one** risk and design a micro‑test that answers it in under 4 hours.

**Pass bar (Day 2):** one micro‑test is defined with setup, procedure, and evidence plan.

---

#### Day 3–4 (2–4 hours) — Build the smallest end‑to‑end slice

Build a “thin vertical slice”: input → process → output.

Examples:

- read one sensor register → log to console
- button press → state change → LED indicator
- parse one file → produce one chart

**Pass bar (Day 3–4):** the end‑to‑end slice runs once and is captured in evidence.

---

#### Day 5–7 — Stabilize and package

- Add one test (unit or integration)
- Add one failure test (power drop, disconnect, corrupted file, invalid input)
- Create a Release Manifest + hashes
- Write a one‑page Quickstart

**Pass bar (Day 5–7):** someone else could reproduce the result from your docs.

---

### 5) “Stop and ask for help” gates (avoid dangerous confidence)

#### Gate S1 — Power safety

Stop if:

- you do not understand your power source limits
- rails droop or reset unpredictably
- components get hot and you do not know why

Ask for help with:

- power tree review, protection, thermal

#### Gate S2 — Interface mismatch

Stop if:

- bus decode shows corrupted frames
- timing margins are not proven
- you are guessing at CPOL/CPHA/addressing

Ask for help with:

- logic analyzer trace review, timing table interpretation

#### Gate S3 — Data corruption / integrity

Stop if:

- logs are missing, duplicated, or time‑warped
- SD writes fail on power loss

Ask for help with:

- file system strategy, journaling patterns, power‑loss hardening

#### Gate S4 — user/hazard risk

Stop if:

- failure could cause injury or damage

Ask for help with:

- hazard analysis + failsafe design

**Rule:** Asking for help is not weakness. It is project control.

---

### 6) Beginner defaults (so you do not have to decide everything)

**Default build choices (when unsure)**

- prefer wired, simple interfaces over wireless early
- prefer logging over real‑time dashboards at first
- prefer known modules/dev boards over custom PCBs in Rev A
- prefer one sensor over “multi‑sensor fusion”
- prefer local‑first (SD/file) over cloud‑first

**Default definition of “done” for Rev A**

- it works 10 times in a row
- you can reproduce it after a day away
- evidence exists (logs/screenshots/plots)
- failure mode is known and bounded

---

### 7) Minimum template set (use these, skip the rest)

For a first project, use only:

1. Project Control Panel
2. Unknowns Map + Learn Tickets
3. Risk Kill Log
4. ICD Lite (if any interface exists)
5. Test Plan/Procedure/Evidence for at least one test
6. Release Manifest + hashes

Everything else is optional until Rev B.

---

### 8) What “success” looks like (especially for new builders)

Success is not “perfect.”

Success is:

- you built something real
- you learned the right skills at the right time
- you did not get hurt
- your work is reproducible and documentable

If you followed the runway and chose to re‑scope, that is also success because it saved you weeks.

---

### 9) Starter checklist (copy/paste)

- [ ]  Project Class chosen (0–3)
- [ ]  Starter Archetype chosen
- [ ]  One‑sentence goal + non‑goals written
- [ ]  Success criteria are measurable
- [ ]  Top 3 risks logged
- [ ]  Top 3 Learn Tickets created
- [ ]  One micro‑test designed and executed
- [ ]  One end‑to‑end slice working
- [ ]  One test evidence pack captured
- [ ]  Release manifest created

---

### 10) Optional: “choose your first project” suggestions (safe + educational)

If you want maximum learning with minimal danger:

- software‑only tool that parses data and generates a report
- USB‑powered sensor logger with serial output + saved log file
- simple UI dashboard for a local dataset (no accounts, no cloud)

Avoid as first projects:

- anything mains‑powered
- anything with large batteries
- anything that moves with force
- anything with medical or safety‑critical claims

# Engineering OS — Beginner On‑Ramp & Skill Bridges (Marketplace Draft)

### What this page is

A practical onboarding system for technical builds: when a term or interface blocks progress, you **pause**, learn the minimum, prove it with a **micro‑practice**, and resume with confidence.

This page is intentionally designed for solo builders and small teams:

- **90‑minute learning ramps**
- An objective **Done‑When** bar
- A lightweight **Learn Ticket** loop when you fail
- A **Skill Log** to keep competence visible over time

### How to use

1. When you hit a term or skill you do not know, use **⌘/CTRL‑F** to find the relevant **Skill Ramp**.
2. Follow the **90‑minute learning path**.
3. Complete the **micro‑practice** and meet the **Done‑When** bar.
4. If you fail, create a **Learn Ticket**, schedule it, and do not proceed until you pass.
5. Log passes in the **Skill Log**.

---

## Templates

### Learn Ticket (drop‑in)

```
## Learn Ticket: <Skill>
- Why now (1 line):
- What blocks me (1 line):
- Chosen Skill Ramp: <link/section>
- Timebox: 90 minutes today (+ one 60-minute retry if needed)
- Pass bar (copy the Done-When):
- Scheduled at:
- Result (PASS/RETRY/ESCALATE):
- Next action (if RETRY or ESCALATE):

```

### Skill Log (CSV starter)

```
Date,Skill,Context (Task/Checklist#),Pass? (Y/N),Evidence (file/link),Gaps Noted,Next Review
2025-12-28,SPI basics,InterfaceFreeze #5,Y,logic_trace.png,"CPOL/CPHA notes",2026-01-15

```

### Each Skill Ramp includes

- **What to know** (five lines)
- **90‑minute learning path** (three blocks)
- **Micro‑practice** (one tiny task)
- **Done‑When** (objective pass bar)
- **Common mistakes & debug**

---

## Fast‑Start Route (recommended)

If you are new, do these first:

1. Requirements Writing
2. Block Diagram & Interfaces
3. BOM Basics
4. Version Control (Git)
5. SPI or I²C (pick one)
6. Test Plan & Evidence
7. Change Control (ECR/ECO)

Everything else can be learned on demand using the ramps below.

---

## Skill Ramps

> Each ramp is intentionally practical. No prior background assumed.
> 

---

## 1) Requirements Writing (clear, testable)

**What to know (in 5 lines)**

- Requirements are **criteria**, not solutions.
- Each requirement must be **testable** (number, threshold, pass/fail).
- Common types: Functional, Performance, Environmental/Physical, Interfaces, UX.
- Use IDs so you can verify each later.
- If you cannot test it, it is not a requirement.

**90‑minute learning path**

- 0–30 min: Rewrite your idea as 8–15 bullet requirements. Ban vague adjectives (“good”, “fast”).
- 30–60 min: Add numbers (Hz, seconds, °C, volts, mm, error %).
- 60–90 min: Add a one‑sentence test method for each requirement.

**Micro‑practice**

- Produce a one‑page “Requirements v0” with IDs (R‑F‑001 etc.), each with a test sentence.

**Done‑When**

- A neutral reader can point to a numeric test or explicit pass condition for every requirement.

**Common mistakes & debug**

- Vague words → replace with numbers.
- Solution statements (“use ESP32”) → move to design, not requirements.

---

## 2) Block Diagram & Interfaces (Interface Freeze starter)

**What to know (in 5 lines)**

- Boxes = subsystems. Arrows = connections.
- Every arrow must be labeled (name, voltage, speed/protocol).
- This becomes your Interface Freeze reference.
- Simple beats fancy.
- Unlabeled arrows usually mean unknowns.

**90‑minute learning path**

- 0–30 min: Draw 6–12 boxes (power, controller, sensors, display, storage).
- 30–60 min: Label arrows (SPI 10 MHz, 12V→5V buck, CAN 500 kbps).
- 60–90 min: Draft a rough controller pin map (assign pins per interface).

**Micro‑practice**

- One diagram (image or Notion diagram) plus a 10‑row pin map table.

**Done‑When**

- Someone else could wire the demo without asking voltage or protocol questions.

**Common mistakes & debug**

- Unlabeled arrows → add voltage and protocol.
- Pin collisions → resolve early.

---

## 3) BOM Basics (Bill of Materials)

**What to know (in 5 lines)**

- A BOM lists every part with source, cost, and alternates.
- Include manufacturer PN and vendor SKU.
- Plan at least one alternate for critical parts.
- Track lifecycle (Active/NRND/EOL).
- Keep it versioned.

**90‑minute learning path**

- 0–30 min: Create BOM columns (Item, Function, Mfr PN, Vendor SKU, Qty, Cost, Alternate).
- 30–60 min: Add links and lead time for five critical parts.
- 60–90 min: Add alternates and compute rough total cost.

**Micro‑practice**

- Populate 10+ real BOM rows and include one alternate per critical part.

**Done‑When**

- You can place an order today without ambiguity.

**Common mistakes & debug**

- Missing Mfr PN → add it immediately.
- No alternates → add at least one.

---

## 4) Version Control (Git) for Files & Firmware

**What to know (in 5 lines)**

- Git tracks changes and makes rollback possible.
- You need a remote (GitHub/GitLab/private).
- Commit small, logical changes with readable messages.
- Use branches for features.
- Tag releases (v1.0).

**90‑minute learning path**

- 0–30 min: Initialize repo. Commit docs (requirements, block diagram).
- 30–60 min: Create a branch (feature‑test‑spi). Add a placeholder driver.
- 60–90 min: Open PR/MR, merge, and tag v0.1.

**Micro‑practice**

- Repo with main + feature branch + a tag + readable commits.

**Done‑When**

- You can clone from scratch and reproduce the same state.

**Common mistakes & debug**

- Giant commits → split them.
- No tags → tag per milestone.

---

## 5) SPI Basics (pick SPI or I²C first)

**What to know (in 5 lines)**

- SPI uses MOSI/MISO/SCLK/CS.
- Mode = CPOL/CPHA. Both sides must match.
- Master sets the speed. Slaves have max limits.
- Typically one CS per device.
- Verify with a logic analyzer if possible.

**90‑minute learning path**

- 0–30 min: Identify MOSI/MISO/SCLK/CS. Confirm slave max speed and mode.
- 30–60 min: Write a tiny read of a known ID register.
- 60–90 min: Capture a transaction and confirm bytes.

**Micro‑practice**

- Print the slave ID byte to serial once per second.

**Done‑When**

- After power‑cycling, it reads reliably 10 times in a row.

**Common mistakes & debug**

- Wrong CPOL/CPHA → try all four modes.
- Adding pull‑ups out of habit → SPI does not need pull‑ups.

---

## 6) I²C Basics (if sensors use I²C)

**What to know (in 5 lines)**

- I²C uses SDA/SCL with pull‑ups.
- Devices have 7‑bit addresses. Use a bus scan.
- Slower than SPI but simple.
- Bus length/capacitance matters.
- Mixed 3.3V/5V may need level shifting.

**90‑minute learning path**

- 0–30 min: Verify pull‑ups (2.2–4.7 kΩ typical).
- 30–60 min: Run an address scanner.
- 60–90 min: Read one register repeatedly.

**Micro‑practice**

- Print a temperature or ID register every second.

**Done‑When**

- Scan shows the expected device and reads are stable.

**Common mistakes & debug**

- Missing pull‑ups → add them.
- Wrong address → check 7‑bit vs 8‑bit notation.

---

## 7) UART Basics (logs, simple links)

**What to know (in 5 lines)**

- UART is TX/RX at a set baud.
- Cross lines TX→RX and RX→TX.
- Voltage levels must match.
- Great for debugging.
- Long wires increase noise risk.

**90‑minute learning path**

- 0–30 min: Wire USB‑UART and confirm voltage levels.
- 30–60 min: Print a heartbeat. Open serial monitor.
- 60–90 min: Echo back received characters.

**Micro‑practice**

- Terminal shows heartbeat and echoes input.

**Done‑When**

- Reset does not break output. Reconnection works.

**Common mistakes & debug**

- Wrong baud → try 9600 and 115200.
- Missing ground → connect GND.

---

## 8) CAN Bus Fundamentals (if relevant)

**What to know (in 5 lines)**

- CAN uses CAN‑H/CAN‑L with 120Ω termination at both ends.
- Speed must match the bus.
- It is message‑based (IDs + payload).
- Use pass‑through adapters. Do not disturb OEM wiring.
- Verify with a CAN tool if possible.

**90‑minute learning path**

- 0–30 min: Confirm termination and speed.
- 30–60 min: Receive frames and print ID + first byte.
- 60–90 min: Filter one ID and prove stability for five minutes.

**Micro‑practice**

- Log 10 seconds of frames to CSV.

**Done‑When**

- No bus errors and frames match expectations.

**Common mistakes & debug**

- Missing/extra terminators → terminate at the ends only.
- Wrong speed → match bus setting.

---

## 9) Test Plan & Evidence (prove “done”)

**What to know (in 5 lines)**

- Tests map directly to requirements.
- Each test has setup, steps, expected result.
- Evidence is a photo, log, or measurement.
- Keep pass/fail visible.
- Automate later. Define now.

**90‑minute learning path**

- 0–30 min: Create mapping table (Requirement ID → Test ID).
- 30–60 min: Write three short test procedures.
- 60–90 min: Run one test and attach evidence.

**Micro‑practice**

- One complete test with evidence stored in your repo.

**Done‑When**

- Anyone can re-run and get the same result.

**Common mistakes & debug**

- “Check it works” → replace with numbers.
- No evidence → add a photo/log.

---

## 10) Change Control (ECR/ECO)

**What to know (in 5 lines)**

- ECR requests a change. ECO is the approved order.
- Every change needs impact analysis (cost, schedule, quality, safety).
- Update artifacts (BOM, ICD, code) when approved.
- Link to tests that re‑verify.
- Changes after a baseline must be tracked.

**90‑minute learning path**

- 0–30 min: Create a simple Change Log table.
- 30–60 min: Write one sample ECR (what/why/impact).
- 60–90 min: Convert to ECO and update one artifact.

**Micro‑practice**

- One ECR→ECO pair with an updated doc and a test reference.

**Done‑When**

- You can point to before vs after states and the reason.

**Common mistakes & debug**

- Silent changes → outlaw them.
- Missing re‑verification → add tests.

---

## 11) ICD (Interface Control Document) Basics

**What to know (in 5 lines)**

- ICD defines exact signals/messages between blocks.
- Software: IDs, fields, units, endianness, rates.
- Hardware: pins, voltage, timing, connector.
- ICD changes are major. Control them.
- You should be able to build against an ICD without seeing the other side.

**90‑minute learning path**

- 0–30 min: List one interface and its signals.
- 30–60 min: Define message format or pin/level table.
- 60–90 min: Validate by writing a mock on the other side.

**Micro‑practice**

- One‑page ICD used by a mock to pass a ping test.

**Done‑When**

- Both mock and real block obey the ICD without tweaks.

**Common mistakes & debug**

- Ambiguous units/endian → specify explicitly.
- “TBD” fields → decide now or remove.

---

## 12) FMEA (Failure Modes & Effects)

**What to know (in 5 lines)**

- List how parts/functions can fail and the effect.
- Score Severity, Occurrence, Detection.
- Focus on top RPN items first.
- Define concrete actions.
- Review after major changes.

**90‑minute learning path**

- 0–30 min: List five critical items and one failure mode each.
- 30–60 min: Score S/O/D and compute RPN.
- 60–90 min: Pick top two and write actions.

**Micro‑practice**

- Mini‑FMEA table with actions assigned.

**Done‑When**

- Actions reduce or close the top risks.

**Common mistakes & debug**

- Hand‑wavy actions → write exact design/test changes.
- Ignored RPNs → sort and act.

---

## 13) Power & Protection Basics

**What to know (in 5 lines)**

- Convert supply safely and meet current needs.
- Protect against spikes, reverse, shorts.
- Thermal dissipation matters.
- Layout affects stability.
- Verify under load.

**90‑minute learning path**

- 0–30 min: Sketch a power tree.
- 30–60 min: Calculate currents and select converters.
- 60–90 min: Bench test with dummy load and log volts/temps.

**Micro‑practice**

- Power tree plus photo of stable output under load.

**Done‑When**

- No dropouts at expected load and temps are in spec.

**Common mistakes & debug**

- Undersized regulator → pick higher current.
- No input protection → add TVS/fuse as needed.

---

## 14) Wiring & Connectors (physical reliability)

**What to know (in 5 lines)**

- Choose gauge/connector for current and environment.
- Strain relief matters.
- Route away from noise and heat.
- Label both ends.
- Verify with continuity and wiggle tests.

**90‑minute learning path**

- 0–30 min: Choose connectors and gauge from datasheets.
- 30–60 min: Crimp and assemble a short harness.
- 60–90 min: Pull test, continuity test, label.

**Micro‑practice**

- Labeled harness that survives a gentle tug test.

**Done‑When**

- Wiggle tests do not cause dropouts.

**Common mistakes & debug**

- Mixed gauges in a crimp → redo.
- No strain relief → add clamp/boot.

---

## 15) Oscilloscope & Logic Analyzer (essential probing)

**What to know (in 5 lines)**

- Multimeter for DC. Scope/LA for signals.
- Ground placement matters.
- Trigger on CS/SCLK or I²C start.
- Avoid loading signals.
- Save screenshots as evidence.

**90‑minute learning path**

- 0–30 min: Measure a DC rail and log it.
- 30–60 min: Capture one SPI/I²C transaction.
- 60–90 min: Annotate and save the capture in repo.

**Micro‑practice**

- One clean capture matching datasheet timing.

**Done‑When**

- You can point to CPOL/CPHA or I²C address in the capture.

**Common mistakes & debug**

- Wrong ground → move ground.
- Too much probe capacitance → adjust probe.

---

## 16) Task Model & Scheduling (firmware basics)

**What to know (in 5 lines)**

- Break work into tasks (receive, parse, display, log).
- Use timers and avoid blocking.
- Queue between tasks.
- Worst-case time must fit the period.
- Watchdog resets hung code.

**90‑minute learning path**

- 0–30 min: Write a 3‑task sketch (RX→PARSE→DISPLAY).
- 30–60 min: Add a queue and publish rates.
- 60–90 min: Prove it runs 10 minutes without overruns.

**Micro‑practice**

- Print each task timestamp and show stable periods.

**Done‑When**

- Jitter is within target and no missed cycles.

**Common mistakes & debug**

- Blocking I/O in fast loop → move to slower task.
- No watchdog → add one.

---

## 17) Data Logging & CSV Hygiene

**What to know (in 5 lines)**

- Choose sampling rate and stick to it.
- Timestamp every record.
- CSV with headers and units.
- Handle power-loss.
- Keep file sizes manageable.

**90‑minute learning path**

- 0–30 min: Define fields and units.
- 30–60 min: Log dummy values at fixed rate.
- 60–90 min: Pull file into a spreadsheet and verify.

**Micro‑practice**

- 60‑second CSV with headers and consistent rows.

**Done‑When**

- No corrupt files and values make sense.

**Common mistakes & debug**

- Writing every byte → buffer writes.
- No headers → add them.

---

## 18) Fault Injection & Safe State (minimum)

**What to know (in 5 lines)**

- Define what “safe” means.
- Simulate common faults.
- Observe behavior and log it.
- Add detection and fallback.
- Retest after fixes.

**90‑minute learning path**

- 0–30 min: Define three faults and expected safe state.
- 30–60 min: Induce one fault and observe.
- 60–90 min: Add a detector and retry.

**Micro‑practice**

- One fault demonstrates expected safe behavior.

**Done‑When**

- Fault no longer crashes the system.

**Common mistakes & debug**

- Over-scoping tests → start simple.
- No evidence → record video/logs.

---

## 19) Mechanical Mounting & Tolerance

**What to know (in 5 lines)**

- Secure mounting prevents vibration failures.
- Manage clearance, airflow, heat.
- Use threadlock/locknuts where needed.
- Avoid cable strain at edges.
- Validate with a shake test.

**90‑minute learning path**

- 0–30 min: Choose mounting location and constraints.
- 30–60 min: Mock with cardboard/3D print.
- 60–90 min: Install and shake test.

**Micro‑practice**

- Mock mount that holds steady and does not pinch cables.

**Done‑When**

- No rattle and serviceable in under five minutes.

**Common mistakes & debug**

- Sharp edges → add grommets.
- Hot zones → relocate or add standoffs.

---

## 20) Documentation “Minimum Set”

**What to know (in 5 lines)**

- Minimum set: Vision/Success, Requirements, Block Diagram, BOM v0, Test Plan v0.
- Keep them in version control.
- Update after ECOs.
- Include evidence screenshots.
- Write for your future self.

**90‑minute learning path**

- 0–30 min: Create five docs as stubs.
- 30–60 min: Fill key content (ramps 1–3 and 9).
- 60–90 min: Commit and tag v0.1.

**Micro‑practice**

- Repo contains the five files. Another person can understand the plan.

**Done‑When**

- Someone can state the goal, interfaces, first parts to buy, and first test to run.

**Common mistakes & debug**

- Docs outside VC → move into repo.
- No IDs → add IDs.

---

## Optional Ramps (add when needed)

- Basic Thermal (power dissipation & temp rise)
- Safety Goals & HARA‑lite
- SBOM & License Hygiene
- Unit Economics Lite (if selling)
- Privacy & Data Handling Basics

---

## Guardrails

- **Timebox**: 90 minutes per ramp, max one 60‑minute retry.
- **Pass bar**: Done‑When must be met with evidence.
- **No silent skips**: If you cannot pass, log a Learn Ticket and escalate.
- **Traceability**: Reference checklist item numbers or requirement IDs in the Skill Log.

---

## Where this plugs into your system

- Use these ramps alongside your checklists and companion docs.
- Each checklist artifact should point to at least one ramp (e.g., ICD → #11, Test Plan → #9, Interface Freeze → #2 and #16).

[Engineering OS — Meta-Learning (Module A)](Engineering%20OS%20%E2%80%94%20Beginner%20On%E2%80%91Ramp%20&%20Skill%20Bridges%20/Engineering%20OS%20%E2%80%94%20Meta-Learning%20(Module%20A)%202dacfa84f4fc8019a7ecc44d73087b35.md)

[Engineering OS — EE Fundamentals (Marketplace Draft)](Engineering%20OS%20%E2%80%94%20Beginner%20On%E2%80%91Ramp%20&%20Skill%20Bridges%20/Engineering%20OS%20%E2%80%94%20EE%20Fundamentals%20(Marketplace%20Draf%2010b11bcf1e17413bb8a82731380d555e.md)

[Engineering OS — Document Examples (Marketplace Draft)](Engineering%20OS%20%E2%80%94%20Beginner%20On%E2%80%91Ramp%20&%20Skill%20Bridges%20/Engineering%20OS%20%E2%80%94%20Document%20Examples%20(Marketplace%20Dr%208f7594161c45434285565853551a5985.md)

# Engineering OS — Meta-Learning (Module A)

<aside>
🧠

**Module A — Meta-Learning Playbook: Unknowns → Knowns**

**Purpose:** A lightweight operating system for learning inside engineering projects. Use it alongside your build plan to surface unknowns, de-risk in the right order, and make decisions backed by evidence.

**Who it’s for:** hobbyists through professionals, including beginners.

**What you get:** repeatable workflows, templates, and “minimum viable rigor” standards.

</aside>

---

## How to use this page

### The core loop

1. **List unknowns**
2. **Rank by risk and sequencing**
3. **Convert top unknowns into 90-minute Learn Tickets**
4. **Run micro-prototypes** (1–4 hour tests)
5. **Capture evidence**
6. **Log decisions**

Repeat until things are “known enough” to move forward safely.

### 15-minute quickstart

Create four items in Notion:

- **Database:** `Unknowns Map`
- **Database:** `Learn Tickets`
- **Database:** `Decision Log (ADR Lite)`
- **Page/Folder:** `Evidence Vault` (links + file structure)

Then pick **one** real project and run **one** Learn Ticket today.

<aside>
⏱️

If you try to build the entire system up front, you’ll end up with a “productivity museum.” Optimize for momentum and evidence, not perfect documentation.

</aside>

---

## Operating principles

- **Unknowns are normal.** The gap between juniors and seniors is speed and discipline in turning unknowns into decisions with evidence.
- **Learning is a project activity.** Don’t “learn everything.” Learn **just enough** to reduce the highest risks first.
- **Evidence beats confidence.** If you cannot point to a test, measurement, or primary reference, treat it as unverified.
- **One scary question at a time.** Micro-prototypes exist to answer *one* risk quickly.
- **Keep decisions reversible by default.** When you choose irreversibility, log it and name the point of no return.

---

# 1) Unknowns Map & Learning Plan

## 1.1 Definitions (keep it simple)

- **Known known:** you can explain it and apply it.
- **Known unknown:** you know what you don’t know (example: “I don’t know SPI timing margins”).
- **Unknown unknown:** you do not yet realize it exists (common integration failures).
- **Assumption:** you are acting as if something is true, but you have not verified it.

**Goal:** Move items from Unknown/Assumption → Verified Known (or “Known enough”) with minimal time.

---

## 1.2 Generate unknowns (without missing the important ones)

### The 10-surface sweep

List unknowns under each heading:

1. **Requirements & success criteria**
2. **Interfaces** (electrical, mechanical, data, human)
3. **Power & energy** (startup, transients, brownout)
4. **Timing & performance** (latency, throughput, deadlines)
5. **Environment** (temperature, vibration, EMI, moisture, abuse)
6. **Failure modes** (what breaks, how it breaks, consequences)
7. **Manufacturing & assembly** (tolerances, tools, yield)
8. **Software/firmware behavior** (states, recovery, updates)
9. **Supply chain** (availability, alternates, lead time)
10. **Compliance / safety / ethics** (even if “not now,” note it)

<aside>
🧩

**Beginner check:** If you cannot write at least two unknowns per surface, you are probably not scanning wide enough yet.

</aside>

---

## 1.3 Cluster (turn a list into a map)

Once you have ~30–150 unknowns, group them. Useful clustering schemes:

- **By subsystem:** Power, Sensors, MCU, Comms, Enclosure, UI, Test
- **By risk type:** Safety, Integration, Performance, Cost, Schedule, Reliability
- **By phase:** Prototype, EVT, DVT, Production (or Rev A/Rev B)

**Target:** 6–12 clusters. If you have 25 clusters, merge until it behaves like a system.

---

## 1.4 Rank (learn in the right order)

### Practical scoring model

Score each unknown 1–5:

- **Impact:** if wrong, how bad?
- **Likelihood:** how likely are you wrong?
- **Sequence:** does it gate other work?
- **Lead time:** will it take weeks to fix or procure?
- **Detectability:** will you notice quickly if it is wrong?

### Heuristics

- **High impact + high sequence goes first.**
- **High lead time gets pulled earlier than you want.**

<aside>
🛑

“I’ll figure it out later” is usually untracked schedule risk.

</aside>

---

## 1.5 Convert unknowns into Learn Tickets

### What a Learn Ticket is

A **Learn Ticket** is a timeboxed learning unit that produces a **deliverable**, not just reading.

Every ticket ends with one of:

- a decision,
- a micro-prototype plan,
- a written summary with specific next actions,
- or a clarified question you can hand to an SME.

### 90-minute ticket structure

- **0–10 min:** define the exact question + pass bar
- **10–35 min:** read targeted sources (avoid general browsing)
- **35–65 min:** produce an artifact (notes, diagram, margin calculation, snippet, checklist)
- **65–80 min:** write a teach-back summary (as if explaining to a smart 16-year-old)
- **80–90 min:** decide next step + link evidence in Notion

---

## 1.6 Schedule learning without burnout

Use **Learning Sprints** (1–2 weeks).

A realistic cadence for builders with a job or school:

- **2–5 Learn Tickets per week** (90 minutes each)
- **1 weekly review** (30–60 minutes)
- **1 micro-prototype block** (2–4 hours)

### Weekly review agenda

- What unknowns turned into knowns?
- Which assumptions remain unverified?
- What are the next three gating unknowns?
- What decisions are pending evidence?
- What changed in requirements?

---

# 2) Reading Specs Like an Engineer (datasheets, standards, tables, errata)

## 2.1 Reading order (do not start at page 1)

1. **Overview + feature list:** what is it supposed to do?
2. **Block diagram:** what are the internal subsystems?
3. **Absolute maximum ratings:** what kills it (even briefly)?
4. **Recommended operating conditions:** where it is meant to live
5. **Electrical characteristics:** what is guaranteed (min/max) vs typical (typ)
6. **Timing characteristics:** what you must satisfy to communicate reliably
7. **Application info + layout guidelines:** what actually matters on a PCB
8. **Package / pinout / mechanical:** physical integration
9. **Errata + app notes:** where reality deviates from the main document

<aside>
⚠️

If you skip absolute max ratings and timing characteristics, you will eventually get punished.

</aside>

---

## 2.2 Min / typ / max (without fooling yourself)

- **Min/Max:** often guaranteed limits (under specified conditions).
- **Typ:** statistical center, not a promise.

**Rule:** If failure matters, design to worst case (min/max) unless you explicitly accept the risk.

---

## 2.3 Timing tables (how to apply them)

Your job is to:

1. Identify the **signal names** (SCLK, CS, MOSI, MISO, etc.).
2. Find the **reference points** (rising edge, falling edge, valid window).
3. Extract **setup and hold** requirements.
4. Translate into **your clocking and firmware constraints**.
5. Compute **margin**.

### Margin (conceptual)

- If a device requires **data setup ≥ X ns** and your design provides **Y ns**, margin is **Y − X**.
- If margin is small or negative: slow the clock, change edge timing, or redesign.

<aside>
🧪

Common pitfall: “it worked on my dev board” is not timing closure.

</aside>

---

## 2.4 Errata mining (find landmines early)

Errata is where products admit their sins.

**Method:**

- Search your **exact part number + silicon revision**.
- Look for language like “may,” “unexpected,” “undefined,” “intermittent,” “rare.”
- Pay attention to reset quirks, boot/clock anomalies, peripheral misbehavior.
- Copy relevant items into your **Unknowns Map** and decide mitigation.

---

## 2.5 The “dig-sheet” method (extract only what you need)

Instead of highlighting everything, extract a one-page summary:

- Power limits and sequencing
- IO voltage levels
- Timing minima/maxima
- Required external components
- Layout constraints
- Known issues and errata references

---

# 3) Trade Study 101 (options → decision you can defend)

## 3.1 Definition

A trade study is a structured comparison that turns opinions into a decision with rationale.

## 3.2 When to do one

Do a trade study when the choice affects:

- **Safety**
- **Budget**
- **Timeline**
- **Architecture lock-in** (MCU, bus, battery, regulator)
- **Anything expensive to undo** (PCB spins, enclosure tooling)

---

## 3.3 Workflow

1. **Problem statement** (1–3 sentences)
2. **Options** (aim for 3+)
3. **Screening criteria** (hard musts)
4. **Weighted criteria** (soft wants)
5. **Score + justify** (no unexplained numbers)
6. **Sensitivity check** (how stable is the winner?)
7. **Decision + next steps**
8. **Decision log entry** (link evidence)

---

## 3.4 Screening criteria (examples)

- Must be available in < 4 weeks
- Must operate at 3.3V logic
- Must support required temperature range
- Must have an acceptable license
- Must have a second source (if product)

---

## 3.5 Weighted scoring (avoid fake precision)

Use **1–5 scores** and **weights that sum to 100**.

Rules:

- Every score has a one-sentence justification.
- Use no more than eight criteria.
- If two options are within ~5–10% total, the decision is likely not robust → run a micro-prototype.

---

## 3.6 Sensitivity check

Move your top two weights up and down by ~20%.

If the winner changes easily:

- the criteria are wrong,
- the weights reflect bias,
- or you need evidence to separate options.

---

## 3.7 Decision write-up (defensible format)

Include:

- what you chose
- why you chose it
- what you rejected and why
- risks you accept
- how you will validate in the next phase

---

# 4) Micro-Prototype Design (1–4 hour tests for one scary question)

## 4.1 Definition

A micro-prototype is a small experiment that answers a single gating question fast.

Examples:

- Will this sensor saturate in my use case?
- Can I meet SPI timing at 10 MHz with this wiring length?
- Does this regulator survive load transients without brownout?
- Does the boot sequence recover after power loss?

---

## 4.2 The 6-part micro-prototype spec

1. **Scary question** (one sentence)
2. **Hypothesis** (“I think X will work because Y”)
3. **Success criteria** (numeric if possible)
4. **Test setup** (wiring, tools, versions, conditions)
5. **Procedure** (step-by-step)
6. **Stop rules** (when to stop and decide)

---

## 4.3 Designing minimum-sufficient tests

Use the smallest test that can fail honestly.

Patterns:

- Use a **dev kit** before PCB spin.
- Use a **breakout board** before schematic lock.
- Use **known-good libraries** before writing drivers.
- Stub everything except the risky interface.

---

## 4.4 Stop rules

Stop when:

- success criteria is met with margin,
- failure is clearly reproducible and explained,
- further work will not change the decision without redesign,
- you learned enough to update the Unknowns Map and next actions.

**Do not** keep iterating because you want it perfect. That is a different phase.

---

# 5) How to Ask for Help (SME Ops)

## 5.1 Why most help requests fail

They are vague, missing constraints, or provide a wall of text without a clear question.

People respond when you:

- show you tried,
- make it easy to answer,
- provide artifacts,
- ask a specific thing.

---

## 5.2 The SME Ask (copy/paste)

- **Context:** what you’re building, why it matters
- **Constraints:** voltage, timing, cost, tools, deadline
- **What I tried:** 2–5 bullets + results
- **Artifacts:** links, screenshots, logs
- **Exact question:** one sentence
- **Ask:** 10–15 minutes, or a “sanity check,” or “which of these two is less wrong?”

---

## 5.3 Where to find SMEs

- Internal: team leads, adjacent teams, lab staff, test engineers
- External: vendor FAEs, product forums, GitHub issues, Discord, Stack Overflow, local maker groups
- Paid: consults, office hours, contractors (often worth it for schedule-critical issues)

---

## 5.4 Office-hours playbook

- Send the SME Ask **before** the meeting.
- Open with: “Here’s the scary question and the pass bar.”
- Share artifacts immediately.
- Close with next steps: “I’ll do X, then validate with Y by Friday.”

---

# 6) “Good Enough” Bars (hobby vs product depth)

## 6.1 Core idea

Choose a depth level explicitly or you will oscillate forever.

### Build types

- **Hobby one-off:** “works for me” + basic safety checks
- **Serious hobby / portfolio:** repeatable + documented + basic validation
- **Internal tool / prototype:** reproducible + evidence + defined constraints
- **Product:** robust + tested + change-controlled + supportable

---

## 6.2 Rev A vs Rev B

- **Rev A:** prove the concept safely and learn the scary parts.
- **Rev B:** improve reliability, packaging, usability, and documentation.

Common trap: dragging Rev B behaviors into Rev A and stalling.

---

## 6.3 “Good enough” checklist

Before you move on:

- Do you have **one proof** it works (test, measurement, demo)?
- Did you capture **evidence**?
- Did you write down **known limitations**?
- Did you decide what you are deferring to Rev B?

If yes → ship Rev A.

---

# 7) Retention (so you keep the knowledge)

## 7.1 Why you forget

Reading once feels productive, but retention requires retrieval and use.

Retention is built by:

- spaced repetition,
- retrieval practice,
- application.

---

## 7.2 Lightweight retention stack

1. **Fast notes** (during the ticket)
2. **Reference card** (one page max per topic)
3. **Teach-back** (3–8 sentences)
4. **Micro-practice** (tiny applied task)
5. **Spaced review** (1 day, 1 week, 1 month)

---

## 7.3 Teach-back drills

After every ticket, write:

- Explain this to a beginner in eight sentences.
- List three failure modes.
- List three design rules.
- What would you measure to prove it works?

If you cannot do that, you do not own the knowledge yet.

---

# 8) Debugging Mindset (hypotheses → experiments → evidence)

## 8.1 The rule

Debugging is science, not emotion. The goal is to reduce uncertainty.

---

## 8.2 The debug loop

1. **Observe:** what exactly happened?
2. **Define expected behavior:** what should happen?
3. **Generate hypotheses:** ranked
4. **Design a test:** change one variable
5. **Run test + capture evidence**
6. **Update model:** what is now true?
7. **Repeat**

---

## 8.3 Binary search (fast isolation)

When something fails:

- split the system in half conceptually,
- test at the boundary,
- isolate the half containing the fault,
- repeat until local.

Works well for firmware states, signal chains, packets, power rails, and mechanical fit issues.

---

## 8.4 Five-Why and fault trees

- **Five-Why:** root causes for process failures and recurring bugs.
- **Fault trees:** multiple plausible causes for a single failure event.

Use fault trees when symptoms are shared across subsystems, reproduction is inconsistent, or interactions are suspected (timing, power, EMI).

---

# 9) Evidence Hygiene (make it trustworthy)

## 9.1 Standard: reproducible enough

Your evidence should allow someone else, or future you, to understand what you did, rerun it, and agree with the conclusion.

---

## 9.2 Minimum viable evidence

- Photos of setup and wiring (wide + close)
- Scope or logic screenshots with labels
- Raw logs (CSV/JSON)
- Conditions + versions + procedure
- Result summary: pass/fail + margin

---

## 9.3 Screenshot annotation rules

Every screenshot should include:

- what signal or metric it is,
- instrument settings (time/div, volts/div, sampling rate),
- trigger condition,
- test conditions (voltage, load, temperature if relevant),
- a filename tying it back to a ticket + date.

---

## 9.4 Hashing (optional, pro-level)

For artifacts that matter (release zips, results):

- generate a SHA256 hash,
- store it in the evidence record,
- you can now prove the file did not change later.

---

## 9.5 Folder anatomy

```
/evidence
  /YYYY-MM-DD_ticket-XYZ_short-title
     README.md   (setup, versions, steps, conclusion)
     photos/
     screenshots/
     logs/
     plots/
     artifacts/  (firmware builds, configs)

```

Notion stores the *index*. The filesystem stores the *truth*.

---

# 10) Decision Journaling (ADR Lite)

## 10.1 Why log decisions

If you do not log decisions, you will re-litigate old choices and forget why constraints existed. Decision logs protect you from your future self.

---

## 10.2 ADR Lite fields

- **Decision:** what you chose
- **Context:** what problem you were solving
- **Options considered:** 2–5 options
- **Criteria:** what mattered
- **Evidence:** links to tests/specs
- **Consequences:** tradeoffs + risks accepted
- **Follow-ups:** what must be validated next
- **Revisit triggers:** what would reopen this decision?

---

## 10.3 Anti-churn rule

You may reopen a decision only if:

- a requirement changed,
- evidence disproved an assumption,
- or a new option materially improves constraints.

Not: “I saw a cool post online.”

# Engineering OS — Skill Bridges (Marketplace Draft)

### What this page is

A library of modular **Skill Bridges**: short, practical learning modules that turn “I’ve heard of it” into “I can use it on my project.”

Each bridge is designed to:

- Fit in ~90 minutes
- Produce a micro‑artifact you can reuse
- End with an objective pass bar (so you can move on)

### How to use

When your project hits a topic you do not know:

1. Add the bridge as a Learn Ticket (Module A).
2. Run the 90‑minute path.
3. Do the micro‑practice on real hardware/code (or a tiny sandbox).
4. Save artifacts into Evidence Vault (Module A/E).
5. Mark pass/fail and continue.

### Design rules

- One bridge = one skill = one measurable outcome
- The goal is functional competence, not mastery
- Every bridge ends with an artifact you can reuse later

---

## Bridge Template (copy/paste)

### [SKILL #] Skill Name

**5-line “what to know”**

- What it is:
- Where it shows up:
- Why it fails in real life:
- The one mental model:
- The one tool you’ll use most:

**Prereqs (max 3):**

**Inputs**

- Datasheet / docs:
- Hardware/tools:
- Repo/examples:

**90-minute learning path**

1. (10 min) Vocabulary + why it exists
2. (15 min) Minimal working example concept
3. (25 min) Failure modes + debugging hooks
4. (25 min) Micro-practice build
5. (15 min) Evidence capture + teach-back

**Micro-practice (1–4 tasks)**

**Pass bar**

**Artifacts to save**

**Common traps**

**Where to go deeper (optional)**

---

## 63) SPI in Practice

**5-line “what to know”**

- What it is: synchronous serial bus with clock, separate MOSI/MISO, chip select per device.
- Where it shows up: sensors, flash, ADCs, displays.
- Why it fails: wrong mode (CPOL/CPHA), CS timing, bit order, clock too fast, ground noise.
- Mental model: “A shift register on both ends clocked by SCLK while CS selects who’s listening.”
- Tool you’ll use: logic analyzer with SPI decode.

**Prereqs:** basic binary/hex, timing diagrams, GPIO.

**Inputs:** device datasheet SPI timing + command format; logic analyzer.

**90-minute path**

1. Read mode (CPOL/CPHA), frame format, max SCLK.
2. Identify command packet structure from datasheet (read/write/address/data).
3. Learn failure signatures (off-by-1 bit, wrong endian, wrong mode).
4. Implement one read and one write (or simulate).
5. Capture LA trace proving correct transaction.

**Micro-practice**

- Read a known ID register (WHOAMI).
- Write a config register and read back to verify.
- Sweep SCLK rates until failure boundary appears (optional).

**Pass bar**

- You can show a decoded SPI transaction that reads the correct ID 3 times in a row and write+readback matches.

**Artifacts**

- LA capture screenshot with decode
- a “SPI transaction worksheet” for that device (commands, timing constraints)
- code snippet (or pseudo-code) showing read/write

**Common traps**

- Sampling on wrong edge (CPHA)
- CS not held for full frame
- MISO floating without pull-ups
- Sharing bus without tri-state awareness

---

## 64) I²C in Practice

**5-line “what to know”**

- What it is: 2-wire shared bus (SDA, SCL) with addressing and open-drain lines.
- Where it shows up: sensors, EEPROMs, RTCs, power monitors.
- Why it fails: missing pull-ups, address confusion (7-bit vs 8-bit), clock stretching, bus lock.
- Mental model: “Everyone can pull the line low; nobody drives it high—resistors do.”
- Tool: logic analyzer with I²C decode.

**Prereqs:** pull-ups concept, basic digital IO.

**Inputs:** device address, register map, timing/pull-up requirements.

**90-minute path**

1. Understand open-drain + pull-ups + rise time.
2. Identify device address and register read/write procedure.
3. Learn ACK/NACK meaning and bus lock symptoms.
4. Perform a register read and confirm ACKs.
5. Capture a trace with start/addr/ack/data/stop.

**Micro-practice**

- Scan bus for devices.
- Read one stable register.
- Force an error (wrong address) and recognize NACK signature.

**Pass bar**

- Successful read with ACK sequence documented; bus scan finds expected address.

**Artifacts**

- LA capture, bus scan output, pull-up calculation note (rough)

**Common traps**

- No pull-ups / too-weak pull-ups
- Address shifted wrong
- Stuck-low SDA due to crash

---

## 65) UART in Practice

**5-line “what to know”**

- What it is: asynchronous serial (TX/RX) with agreed baud/format.
- Where it shows up: debugging, GPS, BLE modules, bootloaders.
- Why it fails: baud mismatch, wrong voltage level, swapped TX/RX, ground reference missing.
- Mental model: “Timed bits with start/stop framing; no clock line.”
- Tool: serial terminal + scope/LA if needed.

**Prereqs:** voltage levels (3.3V vs 5V), baud.

**Inputs:** baud rate, parity, stop bits.

**90-minute path**

1. Understand framing: start bit, 8N1 etc.
2. Confirm logic levels and common ground.
3. Validate baud with known message.
4. Send command, receive response.
5. Save a log proving communication.

**Micro-practice**

- Echo test (loopback).
- Connect to a module and parse one sentence/line (e.g., GPS NMEA).
- Intentionally mis-set baud and observe garbage.

**Pass bar**

- Clean bidirectional exchange with correct parsing and saved log.

**Artifacts**

- terminal log, configuration notes, pinout diagram

**Common traps**

- Level shifting required but missing
- Wrong ground
- Inverted UART (some devices)

---

## 66) CAN in Practice

**5-line “what to know”**

- What it is: differential multi-drop bus with arbitration and robust error handling.
- Where it shows up: automotive, industrial networks.
- Why it fails: wrong bitrate, missing termination, bad wiring/stubs, ID/filter confusion.
- Mental model: “Messages win arbitration by dominant bits; everyone hears everything.”
- Tool: CAN interface + logger + termination check.

**Prereqs:** differential signaling basics, bitrates.

**Inputs:** bitrate, termination expectations (typically 120Ω ends), IDs.

**90-minute path**

1. Learn physical layer (CANH/CANL, termination).
2. Understand frames (ID, DLC, data, CRC).
3. Bring up bus: confirm ~60Ω total across CANH/CANL when properly terminated.
4. Send one frame; receive/ack.
5. Log frames and filter by ID.

**Micro-practice**

- Measure termination (expect ~60Ω across H/L on a properly terminated bus).
- Send a heartbeat frame at 10 Hz.
- Decode one real message and graph a signal (optional).

**Pass bar**

- Verified termination + stable message TX/RX with logs.

**Artifacts**

- wiring diagram, termination measurement note, log file, ID list

**Common traps**

- Only one termination or too many
- Long stubs
- Wrong bitrate (silent bus)

---

## 67) PWM/Timers in Practice

**5-line “what to know”**

- What it is: toggling output with controlled duty cycle and frequency using timers.
- Where it shows up: motors, LEDs, servos, audio, control loops.
- Why it fails: wrong timer prescaler, jitter, resolution limits, bad filtering.
- Mental model: “Timer counts; compare match flips pin.”
- Tool: scope.

**Prereqs:** frequency, duty cycle.

**90-minute path:** configure timer, generate PWM, measure on scope, change duty/freq, validate resolution.

**Micro-practice**

- Generate 1 kHz PWM, sweep duty 10–90%.
- Measure freq stability and duty accuracy.

**Pass bar**

- Scope evidence showing correct frequency and duty across sweep.

---

## 68) ADC/DAC Basics

**5-line “what to know”**

- ADC converts voltage to code; DAC converts code to voltage.
- Key tradeoffs: resolution, sample rate, noise, reference stability.
- Failures: wrong reference, aliasing, noisy ground, input impedance.
- Mental model: “Quantization + sampling + reference define truth.”
- Tool: scope + known reference source.

**Micro-practice**

- Read a stable voltage divider; compute expected code and compare.
- Add averaging; see noise reduction.
- Change reference (if possible) and observe.

**Pass bar**

- ADC reading matches expected within computed tolerance; noise characterized.

---

## 69) RTOS Tasks & Queues

**5-line “what to know”**

- RTOS schedules tasks; queues pass data safely; priorities can break you.
- Failures: priority inversion, stack overflow, deadlocks, starvation.
- Mental model: “Many loops sharing time; priority decides who runs.”
- Tool: RTOS trace/logging if available.

**Micro-practice**

- Create 2 tasks + a queue: producer sends sensor samples, consumer logs.
- Add a watchdog and prove recovery from a stalled task.

**Pass bar**

- Stable runtime with no missed deadlines in a short stress test; logs show task timing.

---

## 70) Debugging with a Logic Analyzer

**5-line “what to know”**

- LA shows digital timing across many channels; decode protocols.
- Failures: wrong sampling rate, wrong thresholds, ground lead issues.
- Mental model: “Capture edges, then annotate meaning.”
- Tool: LA software decoders.

**Micro-practice**

- Capture SPI/I²C/UART transaction and label phases.
- Prove timing margins vs datasheet requirement.

**Pass bar**

- Saved capture demonstrates correct timing and data.

---

## 71) Oscilloscope Essentials

**5-line “what to know”**

- Scope shows voltage over time; reveals noise, transients, timing.
- Failures: probe grounding artifacts, bandwidth limits, aliasing, wrong coupling.
- Mental model: “The probe is part of the circuit.”
- Tool: scope with proper probing.

**Micro-practice**

- Measure ripple on a rail with good probing.
- Compare long ground lead vs spring ground artifact.

**Pass bar**

- You can capture a clean rail measurement and explain probe effects.

---

## 72) Power Integrity with a Multimeter + Scope

**5-line “what to know”**

- PI = the rail stays within limits during dynamic load.
- Failures: droop, ringing, brownout resets, noise coupling.
- Mental model: “Load step response is the truth.”
- Tool: scope + load step (even crude).

**Micro-practice**

- Apply load changes; measure droop and recovery time.
- Trigger on reset line if available.

**Pass bar**

- Evidence includes droop magnitude and confirms no unintended resets (or explains them).

---

## 73) Basic 3D CAD & 3DP

**5-line “what to know”**

- CAD defines geometry; prints have shrink, warping, tolerance.
- Failures: wrong clearances, weak orientation, stress risers.
- Mental model: “Model nominal, design tolerance.”
- Tool: parametric CAD + calipers.

**Micro-practice**

- Design a calibration coupon (holes, slots, fits).
- Print, measure, update clearance rules.

**Pass bar**

- You produce a clearance table that matches your printer/material.

---

## 74) Soldering & Rework

**5-line “what to know”**

- Heat + flux + wetting = good joints.
- Failures: cold joints, lifted pads, bridges, thermal damage.
- Mental model: “You’re cleaning and controlling heat, not melting metal.”
- Tool: iron + flux + wick + microscope.

**Micro-practice**

- Solder headers cleanly, inspect under magnification.
- Rework a component using wick; no pad damage.

**Pass bar**

- Joint quality meets visual standard; continuity verified; no bridges.

---

## 75) Python for Lab Automation

**5-line “what to know”**

- Python turns tests into repeatable scripts: capture → analyze → report.
- Failures: timebase mismatch, missing metadata, non-reproducible notebooks.
- Mental model: “Your script is a test instrument.”
- Tool: Jupyter + matplotlib.

**Micro-practice**

- Parse a log, compute summary stats, plot one graph.
- Auto-generate a PDF/HTML report (optional).

**Pass bar**

- One-button script reproduces plot + summary.

---

## 76) Basic Control Loops (PID)

**5-line “what to know”**

- PID corrects error using proportional, integral, derivative terms.
- Failures: instability, windup, noise amplification.
- Mental model: “P reacts now, I fixes bias, D predicts change.”
- Tool: plotting step response.

**Micro-practice**

- Implement PID on a simulated plant or simple physical system (fan speed/LED).
- Tune to reduce overshoot and settle time.

**Pass bar**

- Step response meets defined overshoot/settle targets.

---

## 77) Statistics for Testing (mean, stdev, CI)

**5-line “what to know”**

- Mean/stdev describe variation; CI bounds uncertainty.
- Failures: small sample false confidence, mixing populations, ignoring outliers.
- Mental model: “Variation is signal about your process.”
- Tool: spreadsheet or Python.

**Micro-practice**

- Take 30 samples; compute mean/stdev/95% CI.
- Plot histogram and identify outliers.

**Pass bar**

- You can state performance with CI and justify sample size.

---

## 78) DOE Micro-Intro (A/B and 2-factor)

**5-line “what to know”**

- DOE finds what factors matter with minimal runs.
- Failures: changing multiple things without tracking, confounding.
- Mental model: “Change intentionally, measure consistently.”
- Tool: simple matrix + plots.

**Micro-practice**

- Run A/B test (two settings) and measure effect.
- Run 2-factor (2×2) test and compute main effects.

**Pass bar**

- You can name which factor drives outcome and show data.

---

## 79) EMC Pre-Checks (probe + radio hacks)

**5-line “what to know”**

- Pre-checks find noisy offenders before lab testing.
- Failures: noisy DC/DC, bad return paths, cable emissions.
- Mental model: “High dI/dt loops radiate.”
- Tool: near-field probe + cheap radio/SDR (as available).

**Micro-practice**

- Scan near DC/DC and clocks; identify hotspots.
- Try mitigation (loop area reduction, shielding, ferrite) and compare.

**Pass bar**

- Before/after evidence shows reduced emissions at key frequencies.

---

## 80) Threat Modeling Lite

**5-line “what to know”**

- Threat modeling identifies attackers, assets, and attack paths.
- Failures: secrets in code, no auth, insecure updates, weak defaults.
- Mental model: “What do we protect, from whom, and how could it fail?”
- Tool: simple STRIDE-ish checklist.

**Micro-practice**

- Identify assets + threats + mitigations.
- Add one mitigation (rate limiting, secure storage, signed update).

**Pass bar**

- Threat model written + at least one mitigation implemented and tested.

---

## 81) UX for Readability (layout, type, contrast)

**5-line “what to know”**

- Good UX makes correct use the default and errors obvious.
- Failures: low contrast, unclear states, hidden actions, jargon labels.
- Mental model: “UI is a control panel, not a brochure.”
- Tool: quick prototypes + user observation.

**Micro-practice**

- Redesign one screen for glanceability (status first).
- Run a 5-minute usability test with 2 people.

**Pass bar**

- Users complete top task without help; misclick rate reduced.

# Engineering OS — Companion Guide (Expanded, Actionable)

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