# Engineering OS — Human Systems & Personal Ops (Marketplace Draft)

### What this page is

A practical **human operating system** for building—solo or with a team—without burning out, thrashing, or becoming the bottleneck.

This is not motivation. It is execution support:

- Time structure that protects deep work
- Collaboration patterns that reduce context hoarding
- Postmortems that prevent repeat failures
- Communication templates that make progress legible

### What this module produces (deliverables)

- A repeatable weekly operating cadence
- A solo-to-team transition kit (handoffs + onboarding)
- A postmortem system that improves reliability over time
- A communication pack (status updates, demos, evidence visuals)
- Personal anti-chaos rules that protect decision quality

---

## 10‑Minute Quickstart (do this today)

Create a Notion page called **Personal Ops Control Panel** with:

1. Weekly Review template (15–30 minutes, recurring)
2. Focus block rules (what counts as deep work, what does not)
3. Current bottleneck (one sentence)
4. Top three risks (from Module A) + what you will do this week to burn them down
5. Status update template (copy/paste ready)

Then adopt one constraint immediately:

- No more than three active tasks at once (WIP limit). If you violate this, your schedule becomes fiction.

---

## 1) Solo‑to‑Team Transition

**Scope**: handoffs, onboarding kits, role slicing, collaboration.

### 1.1 The problem this solves

Solo builders naturally hoard context. When someone joins, everything slows down because:

- They do not know where anything is
- They do not know what “done” means
- They cannot reproduce your setup
- You become the reviewer, tester, and decision-maker for everything

Goal: make yourself replaceable without losing quality.

---

### 1.2 Minimum Onboarding Kit (for any contributor)

This kit lives in Notion and links to repo folders.

Onboarding kit contents:

- Project one-liner + purpose
- Current phase (Rev A/Rev B) + goals
- System overview diagram (block diagram)
- Repo structure + how to build/run/flash
- Toolchain “Known Good” (Module I)
- Top risks + mitigation plan (Module A)
- Current milestone + pass criteria (Module F)
- How to log decisions (ADR) + evidence (Module E)

Rule: if you cannot onboard someone in 60 minutes, your documentation system is not real.

---

### 1.3 Role slicing (how to split work without collisions)

Slice by interfaces and artifacts, not vague “help me.”

Good slices:

- Own the telemetry schema + parser tests
- Own the PCB bring-up procedure + evidence pack
- Own the mechanical enclosure iteration + fit tests
- Own the CI pipeline + release packaging

Bad slice:

- Help with firmware

---

### 1.4 Handoffs (definition of done for collaboration)

Every handoff must include:

- What changed (diff summary)
- How to reproduce
- What remains unknown
- Evidence links
- Next step suggestion

If a handoff does not include reproduction steps, it is not a handoff. It is a message.

---

### 1.5 What good collaboration looks like

- Small PRs (reviewable)
- Evidence for claims (screenshots/logs)
- Decisions recorded (ADR)
- Respectful disagreement with data
- Predictable cadence (weekly review + demo)

### Solo‑to‑Team checklist

- [ ]  Onboarding kit exists and is up to date
- [ ]  Work is sliced into owned artifacts
- [ ]  Handoffs include repro steps + evidence
- [ ]  Decisions are logged, not re-litigated
- [ ]  WIP limits enforced

---

## 2) Time & Energy Management

**Scope**: focus blocks, weekly review, anti-chaos habits.

### 2.1 Bandwidth beats todo lists

Engineering work requires deep focus. If your schedule is meetings + pings, you will work all week and ship nothing.

---

### 2.2 The three-layer time system

**Layer 1 — Deep work blocks (primary)**

- 60–120 minute blocks
- One objective
- One artifact output

**Layer 2 — Shallow work windows**

- Email, messages, admin
- Parts ordering, quick reviews

**Layer 3 — Recovery**

- Breaks, walk, sleep
- Prevents quality collapse

Rule: protect deep work like you protect meetings.

---

### 2.3 Focus block rules (non-negotiable)

- Start with a written objective: “By end of block, X exists.”
- Prep inputs first (docs open, repo ready, instruments ready)
- No multitasking
- End with: result + next step + log/evidence saved

---

### 2.4 Weekly review (15–30 minutes that prevents drift)

Agenda:

1. What shipped last week? (evidence-based)
2. What broke? (root cause)
3. What are the top three risks now?
4. What is the next milestone and pass criteria?
5. What gets deprioritized?

Rule: if you do not deprioritize, you are lying about priorities.

---

### 2.5 Anti-chaos habits

Daily:

- 5 minutes: update Doing/Blocked
- Log decisions that happened
- Capture evidence for progress

Weekly:

- Archive old artifacts
- Check parts lead times
- Run a restore test quarterly (Module I)

### Time & Energy checklist

- [ ]  Deep work blocks exist on the calendar
- [ ]  WIP capped (≤3 active tasks)
- [ ]  Weekly review happens
- [ ]  Each block ends with an artifact + log entry
- [ ]  Shallow work batched, not scattered

---

## 3) Postmortems & Learning Culture

**Scope**: blameless write-ups, actions, regression tracking.

### 3.1 Postmortems prevent repeats

If something fails and you do not learn, you will repeat it.

Blameless means:

- Focus on system causes, not who messed up

But blameless is not consequence-free. You still create corrective actions.

---

### 3.2 When to run a postmortem

Run one when:

- Schedule slipped meaningfully
- A failure required a redesign
- A bug escaped into a demo/customer
- Data was corrupted or lost
- A safety issue occurred
- A week was burned on confusion

Rule: if it cost more than four hours, it deserves a postmortem.

---

### 3.3 Postmortem structure

- What happened (timeline)
- Impact (time/cost/user harm)
- Root causes (not symptoms)
- What went well
- What did not
- Action items (owner + due date)
- Regression test added? (yes/no)
- Decision log updates

Rule: no postmortem ends without at least one prevention mechanism (test, checklist, or process change).

---

### 3.4 Regression tracking (so fixes stick)

Every meaningful fix should create at least one of:

- Test case
- Checklist item
- Design rule
- Monitoring alert

Otherwise the fix is temporary.

### Postmortem checklist

- [ ]  Timeline and impact documented
- [ ]  Root cause identified
- [ ]  Action items assigned with due dates
- [ ]  Regression prevention added
- [ ]  Linked to ADR/test evidence

---

## 4) Communication for Engineers

**Scope**: status updates, demos, evidence, visuals.

### 4.1 Communication is a technical skill

Most engineering communication fails because it is:

- Too detailed without structure, or
- Too vague without evidence

Goal: deliver the right information at the right resolution.

---

### 4.2 Status updates that land

Status = progress + evidence + blockers + ask

Template:

- What shipped (with links)
- Current focus
- Blockers/risks
- Decisions needed (if any)
- Next milestone + ETA range

Rule: done must include evidence, not a claim.

---

### 4.3 Demoing evidence

Best demo pattern:

- Show pass criteria
- Show evidence (plot/log/video)
- Explain what it means
- State remaining risks

Avoid:

- It seems stable
- I think it’s fine

---

### 4.4 Visuals that persuade

Use:

- Block diagrams
- Sequence diagrams for protocols
- One plot per claim
- Labeled screenshots with arrows

Minimum standard:

- Title + date
- Version identifiers
- Measurement context

### Communication checklist

- [ ]  Status updates include evidence links
- [ ]  Claims tied to measurable criteria
- [ ]  Visuals labeled and contextual
- [ ]  Asks explicit (what you need, by when)