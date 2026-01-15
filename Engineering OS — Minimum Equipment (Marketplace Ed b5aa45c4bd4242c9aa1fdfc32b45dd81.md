# Engineering OS — Minimum Equipment (Marketplace Edition)

<aside>
🧰

**Purpose**: Give a novice a sane, non‑chaotic starter kit for common project archetypes.

**How to use**:

1. Pick the closest archetype.
2. Buy only the MVP kit.
3. Run Risk Kill + micro‑prototypes.
4. Upgrade only when the project proves it needs it.

**Cost notes**: Ranges assume decent hobbyist gear, not pro lab equipment. Costs vary by brand and what you already own.

</aside>

---

## Global rules (read once)

### Buy in this order

1. Tools that enable measurement and safe power‑up.
2. Prototyping consumables.
3. Modules and breakouts to prove function.
4. Only then: custom boards and “fancy” parts.

### Universal “do not buy yet” list (for almost everyone)

- Custom PCB run (until risk‑kill proves the core design).
- Huge component assortments (you will not use most of it).
- Expensive enclosure machining (until fit and interfaces freeze).
- Specialty connectors and crimp tools (until the connector family and pinout are stable).
- Premium scopes and benchtop supplies (unless you already know exactly why).

### Universal minimum consumables

- Wire (solid and stranded), heat shrink, electrical tape.
- Zip ties, labels, Sharpies.
- Small fastener assortment (M3/M4 or #6/#8).
- Flux, solder, IPA, brushes/wipes.
- Breadboard, jumpers, headers.

---

## Archetype 1 — Sensor logger / telemetry device (embedded + data)

**Examples:** CAN logger, temperature/pressure monitor, GPS logger, race telemetry box.

**Core risks:** power integrity resets, timebase/sync, storage corruption, wiring/connectors.

### MVP tools

- DMM (multimeter).
- USB logic analyzer (8‑channel is fine) for SPI/I2C/UART/CAN decode (with software support).
- Soldering iron + basic rework (tips, flux, wick).
- Wire stripper + flush cutters.
- Breadboards + jumper set **or** solderable proto boards (pick one).
- Optional but high value: bench power supply with current limit (or a USB‑C PD trigger + fuse + disciplined measurement).

### MVP parts

- MCU dev board (ESP32/STM32/Teensy‑class) with USB.
- Storage: microSD breakout + quality microSD card.
- RTC module (optional but helpful).
- Primary sensors as breakouts (pressure/temp/IMU/GPS, etc.).
- Power module: known‑good buck converter module (do not start with a custom regulator).
- Protection basics: fuse/polyfuse, TVS diode (if automotive‑ish), reverse polarity protection module or diode.
- Connectors (Rev A): screw terminals or JST‑XH for power/sensors (avoid Dupont for anything that moves).

### What not to buy (yet)

- Custom PCB / 4‑layer stackup.
- “Automotive grade” connector families and crimp tools before pinout is frozen.
- High‑end IMU/GPS modules before proving your timebase/logging pipeline.
- “Ultimate” SD wear‑leveling solutions before you can write reliably.

### Expected cost (incremental)

- If you own nothing: **$150–$450**
- If you already have soldering + DMM: **$60–$200**

---

## Archetype 2 — Controller / actuator driver (PWM, relays, motors, solenoids)

**Examples:** fan controller, pump controller, small motor driver, relay box.

**Core risks:** inductive kickback, brownouts, EMI resetting logic, thermal.

### MVP tools

- DMM.
- Oscilloscope (even basic) or borrowed access (to see kickback/resets).
- Soldering + wire tools.
- Highly recommended: bench PSU with current limiting.

### MVP parts

- MCU dev board.
- Driver module (do not roll your own first): MOSFET driver board / motor driver module / relay module.
- Flyback diodes / snubbers (depends on load).
- Bulk caps + ceramic caps (simple decoupling experiments).
- Separate rails concept: logic rail + load rail (even if both come from the same source).
- Basic thermal: stick‑on heatsinks + thermal tape.

### What not to buy (yet)

- High‑power custom PCB.
- Unknown cheap motor drivers with poor documentation.
- Large motor before the control and protection are proven.
- Random “EMC fixes” (ferrites everywhere) before you can reproduce the failure.

### Expected cost

- **$200–$700** depending on load power and whether you need a scope/PSU.

---

## Archetype 3 — Measurement tool / test fixture (jig, harness tester, lab widget)

**Examples:** breakout box, test jig, automated measurement rig, go/no‑go tester.

**Core risks:** flaky wiring, unclear pass/fail criteria, unrepeatable measurements.

### MVP tools

- DMM.
- Logic analyzer (often more useful than a scope for digital fixtures).
- Soldering + crimping basics (ferrules + screw terminals is fine to start).
- Label maker (or a consistent labeling method).
- Optional: scope if analog is involved.

### MVP parts

- MCU dev board or small SBC (depends on UI/logging needs).
- Terminal blocks or JST connectors for repeatable hookups.
- Known‑good cables and strain relief hardware.
- Simple UI: LEDs + buzzer + small display, or serial console.
- Reference standards if needed (known resistor, reference voltage module, loopback plug).

### What not to buy (yet)

- Custom bed‑of‑nails fixtures.
- Expensive pogo pin arrays before requirements stabilize.
- Full enclosure machining before the fixture proves value.
- Overbuilt UI (touchscreen) before measurement logic is stable.

### Expected cost

- **$100–$500** depending on instrumentation needs.

---

## Archetype 4 — Mechanical bracket / fixture / simple tool (minimal electronics)

**Examples:** mounts, camera brackets, adapters, jigs.

**Core risks:** tolerance stackups, wrong fasteners, poor workholding, misaligned holes.

### MVP tools

- Digital calipers.
- Combination square + steel ruler.
- Center punch + scribe/marker.
- Drill + bits (step bit helps for thin stock).
- Clamps + vise (workholding is non‑negotiable).
- Files + deburring tool.
- Safety gear: eye protection (mandatory).

### MVP parts/materials

- Cheap stock material for prototypes (wood, acrylic, aluminum flat bar).
- Fasteners: M3/M4 (or #6/#8) + washers + nylocs.
- Threadlocker (medium) + paint pen (witness marks).
- If 3D printing: filament + heat‑set inserts kit (optional but powerful).

### What not to buy (yet)

- CNC machine or premium tools to “solve” design uncertainty.
- Expensive material until fit is proven.
- Exotic fasteners before you understand load paths.
- Tight‑tolerance machining before you know which tolerances matter.

### Expected cost

- **$80–$350** depending on what you already have.

---

## Archetype 5 — Enclosure / packaging‑first project (serviceability + fit)

**Examples:** device enclosure, rugged box, sealed‑ish container.

**Core risks:** fitment failures, cable routing, serviceability, sealing.

### MVP tools

- Calipers + ruler + square.
- Basic hand tools (screwdrivers, hex keys).
- Drill + bits + deburring.
- Clamps and/or small vise.
- Optional but huge: 3D printer access.

### MVP parts/materials

- Foam board/cardboard for mockups (this is elite in Rev A).
- 3D‑printed prototypes or laser‑cut panels.
- Common fasteners + inserts/standoffs.
- Cable glands/strain relief (if cables enter).
- Gasket tape or simple sealant for early ingress experiments.

### What not to buy (yet)

- IP‑rated claims or expensive sealing systems before you test ingress paths.
- Premium CNC’d aluminum enclosure until you have at least two prototype iterations.
- Fancy latch hardware before usability and service flow are proven.

### Expected cost

- **$100–$600** depending on whether you print and how rugged you go.

---

## Archetype 6 — IoT / networked device (hardware + cloud/app)

**Examples:** Wi‑Fi sensor, remote monitoring, OTA updates.

**Core risks:** security/secrets, update bricking, privacy, reliability.

### MVP tools

- Same as Sensor Logger.
- Optional: scope.
- A clean dev environment (CI is optional but recommended early).
- Basic network visibility (ability to view logs, ports, etc.).

### MVP parts

- Wi‑Fi/BT MCU dev board (ESP32‑class) or SBC.
- Known‑good power supply.
- Storage if logging locally.
- Minimal UI: LEDs + serial logs first.

### What not to buy (yet)

- Custom mobile app before proving the API and user flow.
- OTA before you have stable boot + rollback (or at least a safe update pattern).
- Fancy cloud infrastructure early. Start local‑first or minimal hosted.

### Expected cost

- **$150–$700** depending on scope and instrumentation.

---

## Archetype 7 — Software‑only tool (no hardware)

**Examples:** analysis tool, workflow app, simulator tooling.

**Core risks:** scope creep, no acceptance criteria, brittle releases.

### MVP tools

- Git + issue tracker.
- Basic CI (even simple).
- Test framework appropriate to the language.
- Logging + profiling basics.

### MVP parts

- N/A (but you do want sample datasets or synthetic test data).

### What not to buy (yet)

- Huge cloud spend.
- Premature microservices.
- Fancy UI frameworks before the core workflow is proven.

### Expected cost

- **$0–$50** (tools are usually free), plus hosting if needed.

---

## Cross‑archetype upgrade triggers (when to spend more)

Upgrade only when one of these is true:

- Micro‑prototypes prove the concept and you are blocked by tool limits.
- You need better measurement fidelity to debug a real failure.
- You are moving from Rev A learning → Rev B shipping.
- Reliability and scale force it (connectors, enclosures, fixture repeatability).

---

## Copy/paste: archetype kit decision block (for your project page)

**Chosen archetype:**

**Path:** Hobbyist / Professional

**MVP tools to acquire (now):**

**MVP parts/modules to acquire (now):**

**What I will NOT buy until after Risk Kill:**

**Expected spend this phase:**

**Top 3 risks this kit helps test:**