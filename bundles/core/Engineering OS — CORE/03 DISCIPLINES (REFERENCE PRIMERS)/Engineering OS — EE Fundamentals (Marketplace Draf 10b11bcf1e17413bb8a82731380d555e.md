# Engineering OS — EE Fundamentals (Marketplace Draft)

### What this page is

A practical electrical + embedded “support manual” that sits next to an Engineering OS checklist.

Use it to:

- Make correct design choices in power, timing, noise, and storage.
- Turn unknowns into **validated decisions** using measurement and micro‑prototypes.
- Avoid the most common failure modes that look like “software bugs,” but are actually hardware and system issues.

**Audience**: beginner → pro. Hobby builds → product work.

### How to use

Treat each section as a toolbox:

- **Rules of thumb** (act immediately)
- **What to measure** (verify, do not hope)
- **Micro‑prototypes** (1–4 hour tests)
- **Checklists** (avoid landmines)
- **Pass bars** (know when to stop)

---

## 10‑Minute Quickstart (apply to your current project)

1. Create a Notion page called **Electrical Snapshot** and capture:
    - Supply voltages and max currents
    - Battery/adapter type
    - Buses used (SPI/I²C/UART/CAN/etc.)
    - Storage type (SD/NAND/etc.)
    - Sensors list and ranges
    - “Scary unknowns” list (link to your Unknowns Map)
2. Run two micro-checks today:
    - **Power**: measure rail droop during a load step.
    - **Signal**: verify one bus transaction on a logic analyzer (or scope).

If you cannot measure these, you are not blocked. You are missing instrumentation.

---

## 1) Power Basics (PI)

**Scope**: regulators, decoupling, transients, grounds, brownout.

### What PI is (plain language)

**Power Integrity** means every chip gets the voltage it expects at the moment it needs it, across load changes, noise, startup, and faults.

**Reality check**: Most embedded “weird bugs” are power bugs wearing a software mask.

### Minimum mental model (no math required)

Power delivery is a chain:

**Source → protection → regulator → planes/traces → decoupling → IC pins**

Failures happen when:

- Current demand changes faster than the supply can respond.
- Impedance is too high (long traces, thin wires, poor returns).
- Ground reference moves (ground bounce).
- Startup/reset sequencing is wrong.

### Regulator selection (quick decision framework)

**Choose topology**

- **LDO**: simple, low noise, wastes power as heat (Vin–Vout drop).
- **Buck**: efficient, noisier, layout-sensitive.
- **Buck‑boost**: handles wide input ranges (battery), more complex.

**Non‑negotiable spec checks**

- Max load current (with margin)
- Dropout/headroom (LDO)
- Transient response (load steps)
- Stability requirements (output capacitor type/ESR)
- Quiescent current (battery life)
- Thermal (worst‑case dissipation)

**Beginner trap**

Choosing a regulator by “rated current” alone. Transient response, layout, and stability are the real killers.

### Decoupling (what it actually does)

Decoupling capacitors are local energy buckets that supply fast current spikes while the regulator catches up.

**Placement order (practical)**

1. 0.1 µF near each VDD pin
2. 1–10 µF per IC or per rail region
3. Bulk (10–100+ µF) near power entry or regulator output
4. Any datasheet‑required caps (for stability)

**Layout rule**

A decap loop must be tiny:

VDD pin → cap → ground → back to pin.

If the loop is long, the cap becomes decorative.

### Transient protection (surge, reverse polarity, ESD)

At minimum (depending on source):

- Reverse polarity protection (ideal diode / Schottky / MOSFET)
- TVS diode at power entry for hot‑plug/surge
- Input fuse / PTC if fault current could be dangerous

**Brownout behavior must be designed**

Ask:

- What happens when voltage dips?
- Does the MCU reset cleanly?
- Do peripherals latch into bad states?
- Do you recover automatically?

Minimum: enable BOR, use a watchdog, and design safe defaults.

### Ground / return paths (the actual rule)

Current returns under the path of least impedance, usually right under the signal trace on a ground plane.

**Practical implications**

- Long return paths create noise, crosstalk, and false edges.
- Star ground is often misused:
    - Star can help separate analog currents.
    - For fast digital signals, planes are usually better.

### PI Micro‑prototypes (1–4 hours)

**MP‑PI‑1: Rail droop under load step**

- Question: Does the 3.3V rail stay in spec during current spikes?
- Setup: scope 3.3V at MCU pin (short ground spring)
- Stimulus: toggle load (Wi‑Fi TX burst, motor on/off, GPIO switching, resistor bank)
- Pass bar: Vmin above BOR threshold plus margin, no repeated resets

**MP‑PI‑2: Cold start + hot plug**

- Procedure: 30 plug cycles + 10 rapid cycles
- Pass bar: 100% boots, no latch‑up, no corrupted storage

**MP‑PI‑3: Worst‑case thermal**

- Procedure: max load for 10 minutes, measure temperature
- Pass bar: below safe thermal limit, no throttling/reset

### PI Checklist (minimum safe)

- [ ]  I know my input source range (min/max + transients)
- [ ]  I have reverse polarity + surge strategy (as needed)
- [ ]  I have BOR configured and verified
- [ ]  I have local decoupling at IC pins
- [ ]  I measured rail droop at the load during a real load change
- [ ]  I can explain brownout behavior and recovery

---

## 2) Signal Integrity (SI) Lite

**Scope**: rise/fall, impedance intuition, termination, crosstalk.

### Core truth

SI is about edge speed (rise time), not clock frequency.

### Practical SI triggers (when you should care)

Care if any are true:

- Edge rates are fast (MCU GPIO often is)
- Traces are long relative to edge time
- Cables > ~10–20 cm with fast edges
- Clocks > a few MHz with weak layout
- High‑impedance inputs in noisy environments
- ADC/analog accuracy matters

### Impedance intuition (no equations)

A trace behaves like a transmission line when the transition is fast enough that the wave has not reached the end and returned before the receiver decides.

Mismatch symptoms:

- Ringing (overshoot/undershoot)
- Double‑clocking / false edges
- EMI
- Marginal reliability across temperature and units

### Termination

- Series termination (at source): simplest, good point‑to‑point, slows edge
- Parallel termination (at receiver): stronger, more power
- No termination: ok for short lines/slow edges

Rule of thumb: if ringing crosses logic thresholds, you must act.

### Crosstalk defenses

- Keep spacing (aim ≥3× trace width where possible)
- Route over solid ground
- Avoid long parallel high‑speed runs
- Add series resistors to slow edges if needed

### SI Micro‑prototypes

**MP‑SI‑1: “Is it ringing?”**

Scope a clock/data line at the receiver.

- Pass bar: ringing stays away from thresholds, no double edges.

**MP‑SI‑2: “Does slowing the edge fix it?”**

Add series resistor (start ~22–100Ω) at source.

- Interpretation: if reliability improves, it was SI, not software.

### SI Checklist

- [ ]  I know longest trace/cable lengths for fast signals
- [ ]  Fast signals routed over continuous return
- [ ]  Avoided stubs/branches on clocks
- [ ]  Validated at least one critical edge on scope/LA
- [ ]  Plan exists for termination/edge-rate control

---

## 3) Embedded Buses Primer

**Scope**: SPI, I²C, UART, CAN, LIN, USB, Ethernet.

### The two‑layer view (mandatory)

Every bus has:

- Electrical layer: voltages, wiring, termination, noise
- Protocol layer: framing, addressing, timing, retries

Many failures come from confusing the two.

### Quick selection guide

Point‑to‑point, short distances:

- UART: simplest debug, async, logs/CLI
- SPI: fast, deterministic, more wires

Multi‑drop on PCB/short harness:

- I²C: two wires, many devices, slower, pullups matter

Noisy vehicle/long harness/multi‑node:

- CAN: robust, arbitration, termination matters
- LIN: cheap/simple, slower, single‑master

High throughput:

- USB: strict electrical, good ecosystem
- Ethernet: scalable, tooling rich, PHY complexity

### Tradeoffs table (use in trade studies)

Consider:

- Throughput vs latency
- Wiring complexity
- Distance
- Noise tolerance
- Debug tooling
- Library ecosystem
- Addressing/scaling

Hard truth: “SPI is easy” becomes false once you add cables or awkward CS timing.

### Bus bring‑up sequence

1. Verify electrical: voltages, pullups/termination, wiring order
2. Verify idle states
3. Capture one transaction on logic analyzer
4. Confirm timing mode (SPI mode, I²C speed, CAN bitrate)
5. Confirm error handling (timeouts, retries, recovery)

### Bus Micro‑prototypes

- MP‑BUS‑1: golden transaction capture and annotation
- MP‑BUS‑2: fault injection (unplug, NACK, brief safe short) and recovery proof

---

## 4) Timing & Concurrency

**Scope**: polling vs IRQ vs DMA vs RTOS tasks.

### Core concepts

- Polling: simple, wastes CPU, can miss events
- IRQ: efficient, can become complex
- DMA: high throughput, more complexity
- RTOS tasks: scalable concurrency, scheduling pitfalls

### When to use what

- Polling: timing loose, simplicity wins
- IRQ: sporadic events or tight response needs
- DMA: high throughput (ADC, comms, audio)
- RTOS: 3+ ongoing activities with different priorities

### Priority inversion

Low priority holds a resource needed by high priority.

Mitigation: avoid long locks, use priority inheritance, design lock‑free where practical.

### Watchdogs

- Define “healthy loop”
- Pet watchdog only when system is truly healthy
- Log reset causes

### Timing Micro‑prototypes

- MP‑TIME‑1: instrument worst‑case loop/ISR time (pass: within deadline + margin)
- MP‑TIME‑2: stress concurrency with worst‑case bursts (pass: no missed deadlines, no lockups, no corrupted logs)

---

## 5) Storage & Filesystems

**Scope**: SD/NAND wear, FAT pitfalls, journaling, power‑loss hardening.

### Big risks

- SD cards can corrupt on power loss
- Filesystem metadata updates can brick data
- Flash wears out with small frequent writes

### Rules you can apply immediately

- Buffer and flush in chunks
- Prefer append‑only logs
- Separate critical state from bulk telemetry
- Treat “write interrupted” as normal

### FAT pitfalls

- Metadata updates fragile on power loss
- Sync calls matter
- Corruption can affect more than one file

### Power‑loss hardening patterns

- Double‑buffered config
- Journaled log with checksums
- Log + periodic checkpoints

### Storage Micro‑prototypes

- MP‑FS‑1: repeated controlled power cuts (pass: boots, self‑heals, bounded corruption)
- MP‑FS‑2: endurance estimate via repeated write pattern simulation

---

## 6) Sensors & Actuators

**Scope**: transfer functions, resolution vs accuracy, calibration.

### Definitions you must not mix up

- Resolution, accuracy, precision/repeatability, range, drift

Bits do not equal truth.

### Transfer function

Define:

- Input range
- Scaling and units
- Filtering
- Calibration offsets
- Saturation and failure behavior

### Calibration levels

- None
- Single‑point offset
- Two‑point offset + gain
- Multi‑point nonlinearity
- Temp compensation

### Actuator reality

Actuators create EMI, ground bounce, droop, and coupling into sensors.

Treat actuator power paths as hostile neighbors.

### Sensor Micro‑prototypes

- MP‑SENS‑1: range + saturation test (pass: expected behavior, flags out‑of‑range)
- MP‑SENS‑2: repeatability + drift (pass: within project needs)

---

## 7) Microcontroller Selection

### The selection question

Not “which MCU is best,” but “which MCU satisfies constraints with lowest risk.”

### MCU scorecard

Must‑have:

- Voltage domain compatibility
- Required peripherals
- RAM/flash margin
- Debug support and tooling

Risk reducers:

- Documentation and examples
- Toolchain stability
- Availability/longevity
- Second‑source strategy (product)
- Package you can assemble

### Margin rules

- RAM: ≤60–70% typical
- Flash: ≤70–80%
- CPU: headroom for worst‑case bursts

### MCU Micro‑prototype

MP‑MCU‑1: “Hello, real world”

Bring up one sensor, one comms interface, logging, and a recovery/reset test.

Pass bar: reproducible builds and evidence of stability.

---

## 8) Boot & OTA Strategy

OTA is a reliability problem first. Unsafe OTA is a remote bricking mechanism.

### Minimum safe boot strategy

- Immutable bootloader
- Two image slots (A/B)
- Validate before boot (checksum/signature)
- Rollback on failure
- Version gating if needed

### Recovery behaviors to define

- Power loss during update
- Partial download
- Corrupted image
- Repeated crash on boot

### OTA Micro‑prototype

MP‑OTA‑1: “Brick attempt”

Interrupt update at random points.

Pass bar: device recovers automatically every time.

---

## 9) EMC/ESD Basics

### What it is

- ESD: sudden static discharge that resets or destroys
- EMC: emissions and susceptibility

Common symptoms:

- Random resets
- Sensor glitches
- Comms errors
- Flaky behavior near motors/radios

### Design rules that prevent pain

- TVS on external lines where appropriate
- Series resistors on fast IO leaving the board
- Common‑mode chokes where needed
- Good return paths and ground stitching
- Separate noisy power from sensitive analog

### Pre-check hacks (before a chamber)

- Test near motors/radios/switching supplies
- Careful ESD touch tests on enclosure/ports
- Monitor reset causes and error counters

If failures are non‑deterministic, assume EMI until proven otherwise.

---

## 10) PCB Design Essentials

### Beginner PCB reality

Common failures:

- Wrong footprints
- Missing pullups/decoupling
- Swapped pins
- Poor grounding/returns
- Connector pinout mistakes
- No test points
- Missing power entry/protection

### Placement order

1. Connectors
2. Power entry + protection
3. Regulators
4. MCU / primary IC
5. Critical interfaces
6. Decoupling
7. Remaining passives/indicators
8. Test points + programming header

### Stackup rules

- Solid ground plane adjacent to signal layers
- Route critical signals over continuous reference
- Avoid splits under high‑speed signals
- Stitch ground near connectors and transitions

### Testability essentials

- Test points for every rail
- Programming/debug header access
- Break out bus pins when possible
- Current measurement options when power is tricky

### DRC/DFM handoff checklist (minimum)

- [ ]  Footprints verified (pin 1, pitch, courtyard)
- [ ]  Power net classes correct (width, via size)
- [ ]  All connectors checked with a pinout table
- [ ]  Decoupling placed with tiny loops
- [ ]  Test points for rails + key signals
- [ ]  Mounting holes and keepouts correct
- [ ]  Silkscreen labels for connectors, pin 1, polarity
- [ ]  Assembly notes captured