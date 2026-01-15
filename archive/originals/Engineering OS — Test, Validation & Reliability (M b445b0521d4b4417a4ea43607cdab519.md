# Engineering OS — Test, Validation & Reliability (Marketplace Draft)

### What this page is

A practical test + evidence operating layer you can drop into an Engineering OS.

It helps you:

- Prove the project works with **measurable tests**, not “it seems fine.”
- Build a test ladder that scales from hobby builds to product work.
- Capture evidence other people (and future-you) can trust.
- Improve reliability without drowning in process.

### How to use

You do not “do all tests.” You build a **test ladder**:

- Start with quick unit-level checks
- Integrate and verify interfaces
- Prove system behavior
- Stress what matters (environment, abuse, long runs)
- Capture evidence with clear pass bars

---

## 10‑Minute Quickstart (apply to your current project)

Create a Notion page called **Test Snapshot** and capture:

- Top five requirements (even if informal)
- Top five failure modes (what you are afraid of)
- Test ladder plan (unit → integration → system → stress)
- Evidence folder link (from your Evidence Vault)
- Entry/exit criteria for the next milestone (Rev A or Rev B)

Then do one test today:

- A single measurable pass/fail check on the scariest interface (power, bus, sensor accuracy, logging integrity).

---

## 1) Test Strategy Ladder (Unit → Integration → System → Environmental → Field)

### What the ladder is

The ladder is the order that keeps you from wasting time:

1. Unit tests: verify individual functions/modules/components
2. Integration tests: verify interfaces between parts
3. System tests: verify full device behavior
4. Environmental tests: verify under heat/vibration/EMI/moisture (as needed)
5. Field acceptance: verify in real use conditions

Rule: do not jump to system tests when a unit-level test could catch the issue in five minutes.

### Entry/Exit criteria (what “ready” means)

Every rung should have:

- Entry criteria (what must be true before you test)
- Exit criteria (what constitutes success)

Example:

- Integration entry: rails stable, firmware flashed, interface wiring verified
- Integration exit: 100 consecutive transactions with zero errors

### Rev A vs Rev B test depth

- Rev A (learn safely): prove basic function, capture evidence, bound risks
- Rev B (refine): improve robustness, add coverage, reduce edge-case failures

If you try to test like Rev B during Rev A, you will stall.

---

## 2) Fixtures & Instrumentation

**Scope**: fixtures, wiring discipline, measurement uncertainty.

### Fixtures: what they are

A fixture is anything that makes tests:

- Repeatable
- Faster
- Safer
- Less error-prone

Even tape and cardboard counts if it standardizes the setup.

### Wiring discipline (so your test is not lying)

Bad wiring creates fake failures:

- Intermittent connections
- Ground loops
- Noise pickup
- Wrong pin mapping

Minimum wiring discipline:

- Label every cable end
- Strain relief on probes
- One ground reference strategy
- Photos of setup (wide + close)

### Instrumentation basics

- Multimeter: voltage/current, slow checks, continuity
- Scope: transients, ripple, timing, ringing
- Logic analyzer: bus decode, transaction proof
- Power supply (current limit): safe bring-up and fault testing
- Thermal camera/temp probe: hotspots, drift
- Load (electronic/resistive): stress, droop

### Measurement uncertainty (lite but essential)

Any measurement has error:

- Instrument accuracy
- Probe loading
- Sampling limitations
- Operator setup

Rule: never claim precision your tools cannot support. If your pass bar is tight, quantify uncertainty.

### Fixture micro‑prototypes

**MP‑FIX‑1: Repeatability check**

Run the same test five times.

Pass bar: results consistent within expected variance.

**MP‑FIX‑2: Setup time reduction**

Measure setup time before/after fixture improvements.

Pass bar: setup time drops measurably.

---

## 3) Coverage & Evidence

**Scope**: requirements mapping, pass/fail vs numeric evidence, waivers.

### Requirements still matter as a hobbyist

A requirement can be informal, but it must be testable, measurable, or clearly observable.

Bad: “Works well.”

Good: “Logs data at 50 Hz continuously for 30 minutes without gaps.”

### Pass/Fail vs numeric evidence

- Pass/fail for binary conditions (boots, connects, writes file)
- Numeric evidence for performance and margins (ripple mVpp, latency ms)

Rule: if it matters, capture numbers and margin.

### Traceability matrix

Traceability maps:

- requirement → test → evidence

Even a simple CSV prevents “we tested a lot but did not test what mattered.”

### Waivers and partials

Shipping with known issues is acceptable when documented:

- What failed
- Why you accept it
- Scope/impact
- Mitigation
- When you will fix it (Rev B trigger)

### Evidence quality standard (minimum)

Evidence is trustworthy if it includes:

- Setup description
- Versions (firmware/software/hardware)
- Procedure
- Results
- Artifact links (screenshots/logs)
- Conclusion and margin

---

## 4) Reliability Lite

**Scope**: FMEA, derating, HALT/HASS, fault injection, MTBF myths.

### Reliability is not MTBF spreadsheets

Practical reliability comes from:

- Identifying failure modes
- Designing mitigations
- Validating under stress
- Adding recovery paths

### FMEA (useful version)

For each subsystem:

- Failure mode
- Effect
- Cause
- Detection
- Mitigation

Prioritize by severity, likelihood, and detectability.

Even a 15-row FMEA catches most real-world issues.

### Derating

Do not run components at their limits.

- Voltage margin
- Current margin
- Thermal margin

Rule of thumb: if you run at 95% rating, you are gambling with variation and environment.

### HALT/HASS (conceptual, pre-chamber)

- HALT: push until it fails to find weak points
- HASS: screen production units for early-life defects

HALT-lite options:

- Heat gun + freezer pack
- Vibration via sander table (carefully)
- Supply variation
- EMI exposure in noisy environments

### Fault injection

Introduce realistic faults:

- Disconnect sensor
- Corrupt packet
- Simulate storage full
- Power dip
- Stall a task
- Force retries/timeouts

Pass bar: system detects and recovers safely, or fails safely.

### Reliability micro‑prototypes

**MP‑REL‑1: Long-run soak**

Run 4–24 hours with logging.

Pass bar: no hangs, no leaks, no corruption, restart behavior understood.

**MP‑REL‑2: Abuse shortlist**

Apply 3–5 realistic abuses.

Pass bar: bounded failure and predictable recovery.

---

## 5) Calibration & Metrology

**Scope**: references, traceability, intervals, uncertainty.

### Calibration in practice

Calibration aligns measurement to a known reference.

Metrology is the discipline of making measurements you can trust.

### When calibration matters

- Comparing to real-world truth
- Repeatability across time/devices
- Threshold-based decisions

### Traceability (lite)

For hobby work:

- Use known references (calibrated DMM, reference sensor, known weights)
- Document reference used and stated accuracy

### Calibration intervals

Pick intervals based on:

- How critical accuracy is
- Environment harshness
- Observed drift

### Recording offsets and uncertainty

Record:

- Date
- Method
- Reference
- Offset/gain values
- Uncertainty estimate
- Applied correction method

### Calibration micro‑prototypes

**MP‑CAL‑1: Two-point calibration**

Pass bar: error reduced and stable.

**MP‑CAL‑2: Temperature drift check**

Pass bar: drift quantified and acceptable or compensated.