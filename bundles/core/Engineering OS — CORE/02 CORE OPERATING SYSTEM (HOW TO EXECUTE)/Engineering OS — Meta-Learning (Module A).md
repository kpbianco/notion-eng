# Meta-Learning (Module A)

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
