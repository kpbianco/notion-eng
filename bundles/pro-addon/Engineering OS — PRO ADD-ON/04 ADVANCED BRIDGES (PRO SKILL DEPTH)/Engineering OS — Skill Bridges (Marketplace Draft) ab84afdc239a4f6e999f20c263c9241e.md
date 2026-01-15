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