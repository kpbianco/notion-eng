# Starter Guide (Marketplace Edition)

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
