# Beginner On‑Ramp & Skill Bridges (Marketplace Draft)

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

[Engineering OS — EE Fundamentals (Marketplace Draft)](../03 DISCIPLINES (REFERENCE PRIMERS)/Engineering OS — EE Fundamentals (Marketplace Draft).md)

[Engineering OS — Document Examples (Marketplace Draft)](../06 LIBRARIES (COPY/PASTE + EXAMPLES)/Engineering OS — Document Examples (Marketplace Draft).md)
