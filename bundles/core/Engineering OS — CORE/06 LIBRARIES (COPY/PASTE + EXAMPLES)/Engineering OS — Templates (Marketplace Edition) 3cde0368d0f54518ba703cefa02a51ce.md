# Engineering OS — Templates (Marketplace Edition)

<aside>
✅

**What this is**: A copy‑and‑fill library of engineering templates that turns an “Engineering OS” into repeatable execution.

**How to use**: Duplicate this page into each project, then duplicate the specific templates you need into that project’s folder.

**Design goals**:

- Fast to fill.
- Works for “hobby” depth or “product” depth.
- Traceable: risks → decisions → tests → evidence → releases.
</aside>

---

### 0) Universal rules (use everywhere)

#### 0.1 Naming + IDs

- IDs:
    - Requirements: `REQ-###`
    - Risks: `RISK-###`
    - Decisions: `ADR-###`
    - Tests: `TEST-###`
    - Evidence: `EVD-###`
    - Calibration: `CAL-###`
    - Changes: `CHG-###`
- Dates: `YYYY-MM-DD`
- Releases:
    - Software: `vMAJOR.MINOR.PATCH`
    - Hardware: `revA` / `revB`

#### 0.2 Standard metadata block (top of every template)

**Owner:**

**Project:**

**Date created:**

**Last updated:**

**Status:** Draft / Active / Deprecated

**Links:** Reqs · Risks · ADRs · Tests · Evidence · Release

---

### 1) Learning pipeline: Unknowns Map → Learn Tickets

#### 1.1 Unknowns Map (page template)

**Purpose:** Capture unknowns, cluster them, rank them, and convert the highest‑value unknowns into learnable tickets.

**Context**

- **Project summary (2–5 lines):**
- **Current phase:** Rev A / Rev B
- **Next milestone + pass bar:**
- **Top constraint(s):** time, cost, safety, size, power, schedule, etc.

**Unknowns inventory (raw list)**

List *everything* unclear. Do not filter.

- U-001:
- U-002:
- U-003:

**Clusters (group the unknowns)**

Examples: Power, Firmware, Signal Integrity, Mechanical Fit, Supply Chain, Compliance, UX.

- Cluster A:
- Cluster B:

**Risk + sequence ranking (per unknown)**

- **Impact if wrong (1–5):**
- **Likelihood (1–5):**
- **Detectability (1–5):**
- **Blocks other work?** Yes / No
- **Priority score:** (Impact × Likelihood × (6 − Detectability)) + “blocks” bonus

**Convert to Learn Tickets (top 3–10)**

For each selected unknown:

- **Ticket title:**
- **Decision this enables:**
- **Artifact that proves it:**
- **Stop rule:** when do you stop learning and return to building?

---

#### 1.2 Learn Ticket (90‑minute) template

**Ticket ID:** LT-###

**Title:**

**Cluster:**

**Priority:**

**Timebox:** 90 min

**Problem statement (1–3 sentences)**

What do you need to learn *to proceed*?

**Pass bar (must be measurable)**

What counts as “I know enough”?

**Plan (90 minutes)**

- (10) Vocabulary/overview
- (15) Read the exact needed spec/datasheet section
- (25) Minimal example / reproduction
- (25) Micro‑practice on the real system
- (15) Capture evidence + teach‑back summary

**Micro‑practice task**

Exactly what you will do (no fluff).

**Artifacts to save**

- screenshot/log/trace:
- notes:
- code snippet:

**Result**

- **Pass/Fail:**
- **Decision impact:** what changed, what is now unblocked?
- **Next action:** build / prototype / escalate / defer

---

### 2) Trade Study (decision template + mini outline)

#### 2.1 Trade Study (template)

**Study ID:** TS-###

**Decision being made:**

**Decision deadline:**

**Owner:**

**Stakeholders/SMEs:**

**Requirements and constraints**

- Must‑haves:
- Nice‑to‑haves:
- Hard constraints (cost/size/power/availability):
- Non‑goals:

**Options considered**

- Option A:
- Option B:
- Option C:

**Screening criteria (go/no‑go)**

- Criteria list:
- Disqualifiers:

**Weighted scoring (1–5)**

Create a table:

**Criteria | Weight | A score | A weighted | B score | B weighted | C score | C weighted**

- Performance
- Reliability
- Complexity
- Cost
- Lead time / lifecycle
- Tooling/support
- Risk

**Sensitivity check**

- What if cost weight doubles?
- What if lead time becomes a hard constraint?
- Which assumptions drive the decision?

**Decision**

- **Chosen option:**
- **Why (2–5 bullets):**
- **Risks introduced:**
- **Mitigations:**
- **Verification plan (tests/evidence):**
- **Revisit trigger:** what would cause a reversal later?

---

#### 2.2 Trade Study (mini example outline)

Decision: choose MCU (Option A/B/C)

Weights: reliability 5, availability 4, dev speed 4, cost 2

Result: Option B wins unless availability weight increases → then Option C

(Keep this as a hint, not a full narrative.)

---

### 3) Risk Kill Log (template + prompt examples)

#### 3.1 Risk Kill Log (template)

**Risk ID:** RISK-###

**Risk statement:** “If  ***then***  causing ___.”

**Category**

Power / Interface / Firmware / Signal Integrity / Mechanical / Supply / Compliance / Data / UX

**Score**

- Severity (1–5):
- Likelihood (1–5):
- Detectability (1–5):
- Priority score:

**Kill strategy**

- How will likelihood be reduced?
- How will detectability be increased?
- What test proves the risk is bounded?

**Kill test (micro‑prototype)**

- Setup:
- Procedure:
- Pass bar:
- Evidence to capture:

**Status history**

- Date: action taken, result, score change

---

#### 3.2 Risk examples (fill‑in prompts)

- “If power droops during TX burst then MCU resets causing corrupted logs.”
- “If bus timing is wrong then sensor config silently fails causing bad data.”

---

### 4) Datasheet Dig‑Sheet (copy fields)

#### Datasheet Dig‑Sheet (template)

**Component:**

**Datasheet link + revision:**

**Errata link:**

**Package(s):**

**Operating range:** temp / voltage

**Quick selection**

- Absolute max ratings (red flags):
- Recommended operating conditions:
- Key electrical characteristics (min/typ/max):
- Typical application circuit notes:

**Interfaces & timing**

- SPI/I2C/UART mode details:
- Timing constraints:
- Power‑up/power‑down sequences:
- Reset behavior:

**Registers / command summary**

- ID register:
- Config registers needed:
- Default values:
- Read/write protocol:

**Layout / PCB guidance**

- Decoupling requirements:
- Placement notes:
- Sensitive traces:
- Thermal pad notes (if any):

**Known pitfalls**

- Common failure modes:
- “Gotchas” from errata:

**Project mapping**

- Which schematic page:
- Which nets/pins:
- Which firmware module uses it:
- Tests required to validate:

---

### 5) ICD Lite (Interface Control Document)

#### ICD Lite (template)

**Interface name:**

**Between:** Subsystem A ↔ Subsystem B

**Version:** ICD-###

**Status:** Draft / Active

**Purpose**

What this interface does (1–3 sentences).

**Physical layer (if applicable)**

- Connector:
- Pinout:
- Voltage levels:
- Grounding/shielding notes:
- Cable length limits:

**Electrical characteristics**

- Pullups/termination:
- Drive strength / current limits:
- ESD/TVS protection:

**Protocol layer**

- Bus type + mode (SPI CPOL/CPHA, I2C addr, UART baud, CAN bitrate):
- Message/frame format:
- Timing expectations:
- Error handling / retries:

**Data layer**

- Fields + units:
- Endianness:
- Scaling:
- Rate/throughput:
- Time base sync method:

**Safety & failure behavior**

- What happens on disconnect?
- Safe defaults:
- Watchdog/timeout behavior:

**Verification**

- Tests that prove compliance:
- Evidence artifacts required:

---

### 6) ADR (Architecture Decision Record)

#### ADR (template)

**ADR ID:** ADR-###

**Title:**

**Date:**

**Status:** Proposed / Accepted / Superseded

**Context**

What situation forced a decision?

**Decision**

What you chose.

**Alternatives considered**

- A:
- B:
- C:

**Rationale**

Why this choice wins (bullets).

**Consequences**

- Good:
- Bad:
- Risks introduced:

**Verification plan**

What tests/evidence prove this decision is correct?

**Revisit trigger**

What new info would change the decision?

---

### 7) Test set: Plan → Procedure → Evidence (Module E compatible)

#### 7.1 Test Plan (template)

**Test ID:** TEST-###

**Stage:** Unit / Integration / System / Env / Field

**Purpose:**

**Related requirements:** REQ-###

**Risks covered:** RISK-###

**Entry criteria**

- 

**Exit criteria (pass bar)**

- 

**Metrics to capture**

- 

**Equipment needed**

- 

---

#### 7.2 Test Procedure (template)

**Procedure ID:** PROC-###

**Linked Test ID:** TEST-###

**Setup**

- wiring diagram/photo required? yes/no
- toolchain versions required

**Steps**

1. 
2. 
3. 

**Data to capture**

- logs:
- screenshots:
- plots:

**Stop rules**

- when to abort to prevent damage
- when to stop because evidence is sufficient

---

#### 7.3 Test Evidence (template)

**Evidence ID:** EVD-###

**Linked Procedure:** PROC-###

**Date:**

**Versions:** HW rev / FW commit / SW version

**Operator:**

**Results**

- Pass/Fail:
- Measured values:
- Margin:

**Artifacts**

- links/files:

**Notes**

- anomalies observed:
- follow‑up:

**Conclusion**

One paragraph: what this proves and what it does not prove.

---

### 8) Traceability Matrix (CSV seed)

#### Traceability Matrix (copy into CSV)

Columns:

- Req ID
- Req description
- Test ID
- Procedure ID
- Evidence ID
- Result
- Notes

Starter rows (examples):

- REQ-001,,,,,,
- REQ-002,,,,,,

---

### 9) Calibration Record Sheet

#### Calibration Record (template)

**Cal ID:** CAL-###

**Instrument/Sensor:**

**Serial/ID:**

**Date:**

**Reference used:** accuracy

**Method**

- 

**Raw readings**

- Point 1:
- Point 2:
- Point 3:

**Correction**

- Offset:
- Gain:
- Curve (if any):

**Residual error + uncertainty**

- 

**Applied in**

- Firmware/software version:
- Config file location:

**Next due date**

- 

---

### 10) FMEA starter grid

#### FMEA Grid (template)

Columns (copy into a Notion table):

- Item/SubSystem
- Function
- Failure Mode
- Effect
- Cause
- Severity (1–5)
- Likelihood (1–5)
- Detectability (1–5)
- Mitigation
- Verification Test ID
- Status

Example row prompts:

- Power rail / “droop under TX burst”
- Storage / “power loss during write”
- Sensor / “saturation or drift”
- Comms / “bus lock”

---

### 11) DFX mini‑checklist (DFM/DFT/DFA/DFR)

#### DFX Mini‑Checklist

**DFM (manufacturing)**

- [ ]  footprints verified with manufacturer datasheets
- [ ]  clearances match fab capabilities
- [ ]  polarity and pin‑1 markings are unambiguous
- [ ]  panelization/assembly notes exist

**DFT (test)**

- [ ]  test points for rails and key signals exist
- [ ]  programming/debug access exists
- [ ]  fixture plan exists (even minimal)
- [ ]  serial numbers/version marking method defined

**DFA (assembly)**

- [ ]  connectors keyed and accessible
- [ ]  screws/fasteners standardized
- [ ]  cable routing path defined
- [ ]  assembly steps documented

**DFR (reliability)**

- [ ]  derating margins considered
- [ ]  thermal hotspots identified
- [ ]  vibration/strain relief considered
- [ ]  ESD protection plan exists

---

### 12) Security & Privacy one‑pager

#### Security & Privacy One‑Pager (template)

**Product:**

**Data collected:**

**Purpose:**

**Retention:**

**Who can access:**

**Threats (top 5)**

1)

2)

**Controls (top 5)**

1)

2)

**Update policy:** how patches ship

**Incident response:** who, what, how users are notified

---

### 13) Owner’s Guide / Runbook shells

#### 13.1 Owner’s Guide (customer‑facing)

- What it is
- What it does (outcomes)
- What’s included
- Setup steps
- Normal operation
- Indicators/states
- Troubleshooting
- Safety notes
- Support contact
- Warranty/returns

#### 13.2 Runbook (operator/internal)

- Deployment checklist
- Known‑good versions
- Monitoring/health checks
- How to collect logs
- Common incidents + playbooks
- Rollback steps
- RMA process (if hardware)

---

### 14) Release Manifest + hash scripts

#### 14.1 Release Manifest (template)

**Release:** vX.Y.Z

**Date:**

**HW rev:**

**FW commit:**

**SW version:**

**Notes:**

**Artifacts included**

- firmware.bin
- config.json
- calibration.json
- docs.pdf
- test_evidence_links.txt

**Checksums file**

- checksums.sha256

**Build environment**

- toolchain versions
- OS details
- container hash (if used)

#### 14.2 Hash generation (copy/paste command block)

```bash
# Generate SHA256 checksums for all files in the release directory
# Run inside the release folder
sha256sum * > checksums.sha256
```

(If on Windows PowerShell:)

```powershell
Get-FileHash *-Algorithm SHA256 |Format-Table-AutoSize |Out-File checksums.sha256
```

---

### 15) Supplier/AVL + lifecycle tracker

#### Supplier/AVL Entry (template)

**Part name:**

**Function:**

**Primary vendor + link:**

**Alternate vendor + link:**

**Lifecycle:** Active / NRND / EOL / Unknown

**Lead time:**

**MOQ:**

**Cost @1/@10/@100:**

**Notes:** counterfeit risk, substitutes, footprint flexibility

---

### 16) Unit economics calculator (BOM → COGS → price)

#### Unit Economics (template)

**BOM total (materials):**

**Assembly labor per unit:** min/unit × $/hr

**Test time per unit:**

**Packaging + shipping materials:**

**Overhead allocation (rough):**

**Scrap/yield assumption:**

**COGS estimate:**

**Target price:**

**Gross margin:**

**NRE total:**

**Breakeven units:** NRE / (Price − COGS)

---

### 17) Postmortem (blameless)

#### Postmortem (template)

**Incident:**

**Date:**

**Impact:** hrs / $ / user harm

**Owner:**

**Timeline**

- 

**Root cause(s)**

- 

**What went well**

- 

**What didn’t**

- 

**Corrective actions (with owners + due dates)**

- Action 1:
- Action 2:

**Regression prevention added?**

- test / checklist / monitor:

**Links**

- Evidence:
- ADR updates:
- Change log entry:

---

### 18) SME outreach email/script

#### SME Ask (template)

**Subject:** Quick help on [topic] (15 min)

**Context (2–3 lines)**

What you’re building and why.

**Constraints (bullets)**

Time, cost, safety, compatibility.

**What I already tried (bullets)**

Show effort.

**My specific question(s) (max 3)**

- 

**What I’m asking for**

15 min call or a pointer to a document.

**Artifacts attached**

Diagram/log/screenshot.

**Thanks + scheduling**

Propose 2 windows.

---

### 19) OS onboarding map (links + “definition of done”)

#### OS Onboarding (template)

**Start here (in order)**

1. Project Control Panel (Module F)
2. Unknowns Map + Learn Tickets (Module A)
3. Test & Evidence Ladder (Module E)
4. Change Log + Releases (Module F/I)

**Where things live**

- Decisions (ADR):
- Interfaces (ICD):
- Tests/Evidence:
- Releases/Manifests:
- Supplier/AVL:
- Risks:

**Definition of done (minimum bar)**

- measurable pass bar
- evidence artifact captured
- decision logged if needed
- release tagged if behavior changes

---

### 20) Depth cards: hobby vs product (side‑by‑side)

#### Depth Card (template)

**Area:** BOM / test evidence / calibration / docs / change control

**Hobby depth (minimum safe)**

- 

**Product depth (sellable)**

- 

**Trigger to upgrade depth**

- 

Example areas:

- BOM tracking
- test evidence
- calibration
- compliance planning
- support docs