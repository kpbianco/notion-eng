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

# Engineering OS — Tooling & Shop Skills (Marketplace Edition)

<aside>
🛠

**Purpose**: Your Engineering OS covers planning, learning, decisions, testing, and shipping. This add‑on covers the missing execution layer: the bench and fabrication skills that turn designs into safe, repeatable artifacts.

**How to use**:

- Treat each section as a Skill Bridge: 90‑minute ramp → micro‑practice → pass bar → evidence.
- Pick only the skills you need for the current phase.
- Capture evidence so skills compound instead of resetting.
</aside>

---

### What each skill includes

- What it is and when to use it
- Minimum viable kit
- Standard procedure
- Common failure modes
- Micro‑practice
- Pass bar
- Evidence to capture

---

## 0) Safety baseline (read once, follow forever)

### 0.1 PPE defaults

- **Eyes**: safety glasses by default. Add face shield for grinding/cutting.
- **Hearing**: grinders, routers, CNC, shop vacs, air tools.
- **Lungs**: sanding, welding fumes, resin printing, paint, solvents.
- **Hands**: gloves only when appropriate. **Never** near rotating tools.
- **Clothing**: no loose sleeves or jewelry. Tie hair back.

### 0.2 Shop behaviors that prevent injuries

- **Ventilation is a tool.** If you can smell it, you are breathing it.
- **Fire discipline.** Know extinguisher locations. Clear combustibles before sparks.
- **One‑hand rule around unknown power.** Avoid current paths through the chest.
- **Secure the work.** Most injuries start with “I was holding it.”
- **Stop rules.** If tired, rushed, or angry, do not run machines.

---

## 1) Readiness ladder (choose your level)

**Level 0 — No‑shop build**

- Outsource fabrication.
- Use dev boards and off‑the‑shelf enclosures.
- Focus on planning, integration, and testing.

**Level 1 — Basic maker capability (recommended baseline)**

- Hand tools, drilling, deburring
- Soldering
- FDM 3D printing
- Goal: functional prototypes made safely

**Level 2 — Intermediate fabrication**

- Harnessing and crimp systems
- Enclosure finishing
- Light CNC routing
- Goal: small‑batch‑quality assemblies

**Level 3 — Advanced shop**

- Welding
- Precision CNC
- Composite layups
- Surface finishing
- Goal: robust mechanical structures and production fixtures

**Rule:** move up levels because the project requires it, not because it is “cool.”

---

## A) Electronics build skills

### A1) Soldering fundamentals (through‑hole + basics)

**Use when:** prototypes, connectors, headers, repair.

**Minimum kit:** temperature‑controlled iron, tips, flux, solder, wick, tweezers, IPA + brush, fume extraction.

**Standard procedure**

1. Clean pads/leads (especially oxidized surfaces).
2. Flux the joint.
3. Heat pad and lead together.
4. Feed solder into the joint (not the tip).
5. Remove solder, then iron. Do not move the joint while cooling.
6. Inspect (wetting, shape, no cracks). Clean flux if needed.

**Common failure modes**

- Cold joint (dull/grainy)
- Too little heat (solder balls)
- Too much heat (lifted pad)
- No strain relief (wire breaks later)

**Micro‑practice:** Make 10 perfect joints on a header. Inspect under magnification.

**Pass bar:** 10/10 joints are shiny with concave fillets, proper wetting. Continuity verified. No bridges.

**Evidence:** before/after photos under magnification + continuity check log.

---

### A2) SMD soldering (hand solder + drag solder)

**Use when:** assembling small boards, fixing ICs.

**Minimum kit:** fine tip, flux pen, tweezers, microscope, wick. Hot air optional.

**Procedure (drag solder)**

1. Align part. Tack corners.
2. Flood pins with flux.
3. Drag solder across pins with light pressure.
4. Wick bridges. Re‑flux. Re‑touch as needed.
5. Inspect pin‑by‑pin.

**Common traps:** insufficient flux, overheating pads, misalignment.

**Micro‑practice:** Solder a 0.5–0.8 mm pitch IC (practice board preferred).

**Pass bar:** no bridges. All pins wetted. Continuity where expected. No shorts to neighbors.

---

### A3) Hot air rework (remove/replace SMD)

**Use when:** rework, component replacement.

**Minimum kit:** hot air station, nozzles, flux, Kapton, tweezers. Preheater optional.

**Procedure**

- Protect nearby parts (Kapton/foil).
- Preheat when possible.
- Flux. Heat evenly. Lift gently once solder reflows.
- Clean pads (wick). Re‑tin. Place new part. Reflow. Inspect.

**Common traps:** blowing away passives, delaminating pads, overheating ICs.

**Micro‑practice:** Remove and replace a QFN/QFP on a scrap board.

**Pass bar:** board still functional or passes continuity checks. No lifted pads.

---

### A4) Reflow soldering (stencil + paste)

**Use when:** building multiple boards or dense SMD.

**Minimum kit:** stencil, paste, squeegee, alignment jig, hot plate/oven, inspection.

**Procedure**

- Align stencil. Apply paste evenly.
- Place parts (verify polarity).
- Reflow with a controlled profile.
- Inspect and rework defects.

**Common traps:** too much paste (bridges), tombstoning, wrong polarity.

**Micro‑practice:** assemble a small SMD kit board and document defect rate.

**Pass bar:** ≥95% joints acceptable without rework (or defects are understood and corrected).

---

### A5) Wire harnessing and cable management

**Use when:** anything that moves, vibrates, or gets serviced.

**Minimum kit:** wire stripper, crimp tool(s), correct terminals, heat shrink, labels, lacing/zip ties, strain relief boots.

**Procedure**

- Choose wire gauge by current and mechanical needs.
- Use the correct terminal and correct die.
- Add strain relief. Avoid sharp bends. Secure at intervals.
- Label both ends. Document pinout.

**Common traps:** wrong crimp, no strain relief, unlabeled cables, mixed grounds.

**Micro‑practice:** build a 4‑wire harness with connector. Label it. Do a pull test.

**Pass bar:** pull test passes. Continuity is correct. Bend test does not break.

**Evidence:** pinout diagram + photos + test results.

---

### A6) Crimping (open‑barrel + closed‑barrel)

**Use when:** reliable connectors (automotive, industrial).

**Minimum kit:** correct crimper for the terminal series, terminals matched to wire spec.

**Procedure**

- Strip to exact length. Do not nick strands.
- Crimp conductor wings, then insulation wings.
- Inspect: conductor compression, insulation support, no exposed strands.

**Micro‑practice:** 10 crimps. Inspect + pull test.

**Pass bar:** 10/10 visually correct. 0 pull test failures.

---

### A7) Conformal coating / potting (optional reliability layer)

**Use when:** moisture, vibration, corrosion environments.

**Procedure**

- Mask connectors and test points.
- Clean thoroughly.
- Apply per spec. Cure. Inspect coverage.
- Document a rework strategy.

**Pass bar:** coverage is uniform. Connectors remain uncoated. Rework plan is documented.

---

## B) Mechanical hand skills (baseline “I can make parts”)

### B1) Measuring and layout

**Use when:** any fabrication.

**Minimum kit:** calipers, ruler, square, scribe/marker, center punch.

**Procedure**

- Measure twice, mark once.
- Use a square for perpendicularity.
- Center punch before drilling.

**Micro‑practice:** layout and drill a hole pattern on scrap plate. Measure error.

**Pass bar:** hole positions within your tolerance target (e.g., ±0.5 mm hobby).

---

### B2) Drilling

**Minimum kit:** drill press preferred, bits, cutting fluid, clamps.

**Procedure**

- Clamp the work.
- Pilot hole if needed.
- Use correct speed for material.
- Deburr both sides.

**Common traps:** work spinning, wandering bits, oversized holes.

**Pass bar:** holes are round, on‑location, deburred, with no work damage.

---

### B3) Tapping threads

**Procedure**

- Use correct tap drill size.
- Use cutting fluid.
- Keep tap aligned.
- Advance, then back to break chip.
- Clear chips. Do not force.

**Pass bar:** thread engages smoothly. No cross‑threading. No broken tap.

---

### B4) Deburring and edge finishing

**Use when:** everything, especially enclosures and metal parts.

**Pass bar:** no sharp edges. Parts are safe to handle. Surfaces are uniform.

---

### B5) Adhesives and fasteners

**Use when:** joining dissimilar materials, sealing, vibration resistance.

**Procedure**

- Surface prep: clean and roughen.
- Choose adhesive by load type (shear vs peel), temperature, cure.
- Clamp correctly. Respect cure time.

**Pass bar:** joint survives a defined mechanical test (pull, twist, vibration shake).

---

## C) 3D printing (FDM + resin)

### C1) FDM printing (functional prototyping)

**Use when:** fast enclosure prototypes, brackets, fixtures.

**Minimum kit:** FDM printer, calipers, basic filament, slicer profiles.

**Procedure**

- Calibrate first layer, extrusion, bed leveling.
- Print a calibration coupon (dimensions, holes, slots).
- Establish clearance rules (fits and holes).

**Micro‑practice:** print a tolerance coupon. Measure. Build a clearance table.

**Pass bar:** fit outcomes (press vs slip) are predictable for your printer.

**Common traps:** designing to CAD nominal without tolerance, weak orientations, ignoring warp.

---

### C2) Resin printing (detail parts)

**Use when:** small detailed components, molds, cosmetic parts.

**Safety:** ventilation + gloves. Resin handling discipline.

**Pass bar:** parts cure properly (not tacky). Dimensional drift is understood.

---

### C3) Design for 3DP (DFAM‑lite)

**Key rules**

- Add fillets at stress points.
- Avoid long thin cantilevers.
- Design for print orientation.
- Prefer bosses/ribs over solid blocks.

**Micro‑practice:** redesign one bracket twice: “naive” and “print‑aware.” Compare strength.

---

## D) CNC and machining fundamentals

### D1) CNC router basics (wood/plastic/light aluminum)

**Use when:** plates, enclosures, fixtures.

**Minimum kit:** CNC router, workholding, bits, CAM software, dust control.

**Procedure**

- Secure work (workholding is half the battle).
- Define coordinate zero correctly.
- Start conservative on feeds and speeds.
- Run an air cut or simulation.
- Cut, deburr, measure.

**Micro‑practice:** machine a simple pocket + hole pattern. Measure.

**Pass bar:** dimensions within tolerance target. Finish acceptable. No crashes.

---

### D2) Mill basics (precision metalwork)

**Core skills**

- squaring stock
- locating edges
- drilling/reaming
- light facing
- clamping strategy

**Pass bar:** you can produce controlled thickness and repeatable hole spacing.

---

### D3) Lathe basics (shafts, spacers)

**Core skills**

- facing, turning diameter, parting, chamfering
- measuring diameter accurately
- managing chatter

**Pass bar:** you can make a spacer to ±0.05–0.1 mm (setup‑dependent) repeatably.

---

### D4) Feeds and speeds intuition

**Mental model**

- too slow feed or too fast RPM → rubbing and heat
- too fast feed → chatter and tool overload
- chips tell the truth

**Micro‑practice:** run a feeds/speeds sweep on scrap. Document what changes.

---

## E) Welding and metal joining

### E1) MIG welding (fast structural steel)

**Use when:** brackets, frames, thicker steel.

**Minimum kit:** MIG welder, gas, PPE, grinder, clamps.

**Procedure**

- Clean metal to bright.
- Fit‑up and clamp.
- Tack in multiple spots.
- Weld short controlled beads.
- Inspect penetration, bead profile, defects.

**Micro‑practice:** fillet weld coupons. Cut and etch (or do a bend test if appropriate).

**Pass bar:** consistent bead, minimal spatter, no obvious undercut/porosity. Passes a simple destructive test.

**Common traps:** welding dirty metal, poor fit‑up, incorrect heat settings.

---

### E2) TIG welding (precision, thin material)

**Use when:** thin steel, stainless, aluminum, clean aesthetic welds.

**Micro‑practice:** beads on plate → fillet joint → butt joint.

**Pass bar:** consistent bead, controlled heat, no contamination, acceptable penetration.

---

### E3) Stick welding (outdoors, dirty steel)

**Use when:** heavy‑duty work in less controlled environments.

**Pass bar:** acceptable bead with minimal slag inclusions. Joint passes a strength check.

---

### E4) Brazing / silver solder

**Use when:** joining without full fusion, sometimes dissimilar metals.

**Pass bar:** joint survives a defined mechanical test. Clean fillet. No brittle failure.

---

## F) Composites (fiberglass/carbon fiber)

### F1) Fiberglass layup

**Use when:** lightweight panels, enclosures, fairings.

**Safety:** PPE and ventilation. Epoxy sensitization is real.

**Procedure**

- Mold prep.
- Cut cloth. Mix resin by weight.
- Wet‑out. Remove bubbles. Cure.
- Trim, sand, seal/finish.

**Micro‑practice:** flat panel coupon. Compare flex strength vs thickness.

**Pass bar:** consistent laminate, minimal voids, predictable thickness.

---

### F2) Vacuum bagging

**Use when:** better strength‑to‑weight and fewer voids.

**Pass bar:** leak rate acceptable. Laminate measurably improves vs hand layup.

---

## G) Surface finishing (prototype → product)

### G1) Sanding and surface prep

**Use when:** painting, adhesion, appearance.

**Pass bar:** consistent surface, no deep scratches, cleaned before coating.

---

### G2) Painting and clearcoat

**Use when:** corrosion protection and presentation.

**Key idea:** prep is most of the work.

**Pass bar:** even coverage, no runs, adhesion verified (tape test).

---

### G3) Powder coating / anodizing (often outsourced)

**Use when:** durable finishes.

**Skill:** knowing when to outsource and how to specify.

**Pass bar:** correct finish and thickness. Masked interfaces remain functional.

---

## H) Shop workflow skills (the glue between tools)

### H1) Workholding and clamping

**Use when:** drilling, sanding, CNC, welding.

**Pass bar:** work does not shift. Results are predictable.

---

### H2) Fixture building

**Use when:** you do anything more than once.

**Micro‑practice:** build a simple drilling jig or soldering fixture.

**Pass bar:** repeat operation is faster and has less error.

---

### H3) Tool maintenance

- Replace consumables before failure (tips, bits, belts).
- Calibrate printer beds.
- Clean and lubricate where appropriate.

**Pass bar:** maintenance log exists. “Mystery failures” decrease.

---

## 2) Notion implementation (for this tooling add‑on)

### Database — Tooling Skill Bridges Library

**Properties**

- **Skill** (Title): e.g., “MIG Welding — Fillet Welds”
- **Category**: Electronics / Mechanical / Additive / CNC / Welding / Composites / Finish
- **Level**: 1 / 2 / 3
- **Timebox**: 90 min default
- **Minimum Kit**: text
- **Micro‑practice**: text
- **Pass bar**: text
- **Artifacts**: files/links
- **Safety Flags**: Fire / Fumes / High‑speed / High‑current / Chemical
- **Status**: Not started / In progress / Passed / Needs retry
- **Linked Project**: relation
- **Linked Evidence**: relation to EVD entries

**Suggested views**

- Beginner‑safe (Level 1)
- Requires ventilation
- Needed this week (linked project)
- Passed skills

---

## 3) Standard evidence pack for tooling (copy/paste)

Whenever you learn a tooling skill, save:

- Setup photo (workholding and tool settings visible)
- Process photo/video (one key step)
- Result photo (with measurement)
- Measurement log (calipers, continuity, pull test)
- What went wrong + fix (one paragraph)
- Next‑time rule (one bullet)

This makes skill learning cumulative.

---

## 4) Scope guardrails (so this does not balloon)

### What not to do

- Do not turn this into a “master machinist” curriculum.
- Do not buy tools before the project proves the need.
- Do not upgrade difficulty mid‑project unless the risk plan changes.

### What to do instead

- Use micro‑practice and a pass bar.
- Outsource when:
    - safety risk is high (mains, pressure vessels, structural welds for safety)
    - tolerances exceed your tools
    - certified processes are required

---

## 5) Tool purchase mini‑template (use your Trade Study)

When you are tempted to buy a tool:

- **What operation does it unlock?**
- **How many times will it be used in 6 months?**
- **Outsource cost vs buy cost?**
- **Space/ventilation/power needs?**
- **Safety risk?**
- **Minimum acceptable tool specs?**
- **Pass bar after purchase:** what will you produce to justify it?

If you cannot answer these, do not buy yet.

---

## Workholding and fixturing (primer)

**Why this matters:** most shop failures are not “bad cutting.” The part moved. Workholding is the difference between repeatable parts and chaos.

### What it is

Workholding is how you constrain a part so drilling/cutting/grinding forces cannot move it. Fixturing is how you make a setup repeatable.

### When you need it

- precise drilling
- grinding/sanding small parts
- any CNC
- welding/brazing (fit‑up and distortion control)
- assemblies where alignment matters

### Beginner mistake

Holding parts by hand or relying on friction and hope. If it can grab, it will.

### Core mental model

A part has **6 degrees of freedom**: translate X/Y/Z and rotate about X/Y/Z. Your clamps/fixture must block the ones that matter for the operation.

**3‑2‑1 fixturing (lightweight version)**

- 3 points define a plane (base)
- 2 points define an edge
- 1 point defines the last axis

### Minimum viable kit (cheap but real)

- bench vise (or drill‑press vise)
- clamps: F‑style and quick‑grip
- spring clamps (light duty)
- C‑clamps (rigid)
- V‑block (round parts)
- sacrificial board (drilling)
- masking tape + CA glue (flat fixturing)
- spacers/parallels (even scrap bar stock)
- rubber pads (prevent marring)
- wood blocks (soft jaws)

Upgrades:

- soft jaws for vise
- angle plate
- threaded inserts + fixture plate

### Workholding playbook (every time)

1. Identify forces: where will the tool push/pull?
2. Clamp on strong surfaces.
3. Prevent spin (V‑block or trap round stock).
4. Support near the cut (reduce flex).
5. Use a sacrificial layer for through‑drilling.
6. Push hard by hand before cutting. It should not shift.
7. Re‑check after the first operation. Clamps settle.

### Failure modes (and fixes)

- Part spins: chatter, gouges
    - Fix: V‑block, clamp closer, reduce RPM/pressure, pilot hole
- Part lifts: hole drift, asymmetric burrs
    - Fix: add downward force and support points
- Clamp slip: shiny witness marks, shifted location
    - Fix: clean surfaces, pads, better clamp direction
- Crushing/marring: dents, cracked plastic
    - Fix: soft jaws, distribute force, clamp on sacrificial areas
- Welding warp: misalignment
    - Fix: tack sequence, opposing tacks, stitch pattern, allow cooling

### When to build a fixture

Build a fixture if:

- the operation repeats more than twice
- alignment is critical
- the part is small or awkward
- misalignment consequences are high

### Micro‑practice (30–90 minutes)

**Goal:** drill a repeatable hole pattern without drift.

1. Cut a scrap plate (wood or aluminum).
2. Mark a 4‑hole square pattern (e.g., 30 mm × 30 mm).
3. Clamp two ways (bad vs good).
4. Drill both. Measure location error.
5. Write a one‑line rule about what improved it.

**Pass bar:** hole centers within ±0.5 mm by hand (tighter if drill press + good vise). No spinning. Clean deburr.

**Evidence:** setup photo, measurement table, 3 bullets (worked, failed, next time).

---

## Measurement and metrology for builders (primer)

**Why this matters:** measurement is not “read the number.” It is tool + technique + reference + uncertainty.

### What it is

Reliable measurement that supports decisions:

- does it fit?
- is it within tolerance?
- did the change improve it?

### When you need it

- fit and assembly
- fabrication (drilling, 3DP, CNC)
- verification claims (tests must be measurable)

### Core concepts

- Accuracy: closeness to true value
- Precision: repeatability
- Resolution: smallest displayed increment
- Repeatability: will you get the same result again?

If you cannot measure repeatably, you cannot tune anything.

### Minimum viable kit

- digital calipers
- steel ruler
- combination square
- feeler gauges
- center punch + scribe/marker
- known references (optional)

Upgrades:

- micrometer
- dial indicator
- pin gauges
- thread pitch gauge

### Procedures that stop lies

1. Measure the same feature 3 times. If values differ, technique is unstable.
2. Control the part: clean, deburr, consistent jaw pressure.
3. Use the right tool for the feature. Calipers lie on small holes and burrs.
4. Use go/no‑go fit checks when fit matters more than the number.

### Practical fit categories

- Slip fit: easy by hand, minimal wobble
- Snug fit: gentle pressure
- Press fit: force/heat, usually permanent

**3D printing rule:** holes print undersized. Drill/ream when precision matters. Build a clearance table.

### Common traps

- burrs
- temperature
- jaw tilt
- measuring threads with calipers
- believing one number

### Micro‑practice (45–90 minutes)

**Goal:** build tolerance intuition.

1. Pick 5 objects: bolt, nut, printed part, metal bar, drilled hole.
2. Measure each 3 times.
3. Compute max‑min spread.
4. Note where technique was inconsistent.
5. Make one go/no‑go test (e.g., bolt passes hole).

**Pass bar:** for at least 3 objects, measurements are within ±0.1 mm (or your tool’s realistic repeatability). You can state: “My repeatability is about __.”

**Evidence:** measurement table, measurement photo, 3 rules you will follow.

---

## Cut / drill / grind fundamentals (primer)

**Why this matters:** these operations are where beginners get hurt and parts get ruined fast.

### A) Cutting (hand tools → power tools)

**Choose control over speed.**

Common tools and what they are good at:

- utility knife: foam, thin plastics (score + snap)
- hacksaw: metal bar/tube
- jigsaw: rough wood/plastic cuts (can wander)
- circular saw: straight wood cuts (high consequence if misused)
- bandsaw: controlled cuts and repeat work
- angle grinder cutoff wheel: fast metal cutting (high risk)
- rotary tool cutoff: small cuts, slow, easy to overheat

### B) Drilling

**Precision hierarchy (best → worst)**

1. drill press + vise
2. hand drill + guide/jig
3. hand drill freehand

**Standard drilling procedure**

1. Mark location.
2. Center punch.
3. Clamp work.
4. Pilot hole if needed.
5. Correct speed.
6. Cutting fluid for metal when appropriate.
7. Clear chips.
8. Drill into sacrificial board.
9. Deburr both sides.
10. Verify with fastener/gauge.

**Bit selection cheat sheet**

- twist bit: general
- step bit: sheet/thin material
- brad point: wood
- spade bit: rough wood holes
- hole saw: large holes (needs stable setup)
- countersink: chamfer (go slow)

### C) Grinding / sanding

Angle grinders remove material extremely fast. Many errors are irreversible.

**Minimum safety**

- guard installed
- face shield + safety glasses
- secure the work
- stand out of the wheel plane

**Standard grinding procedure**

1. Secure part.
2. Use light passes.
3. Control heat.
4. Finish with file/deburr/sand.
5. Measure repeatedly.

### Failure modes (and fixes)

- bit walks: no punch, poor clamp, dull bit → punch + pilot + clamp
- oversized hole: wobble, forcing → drill press/guide, step bit for thin sheet
- work spins: catastrophic → clamp, V‑block
- chatter: overhang, wrong speed → support close, reduce speed, sharpen
- heat damage: melting/work‑hardening → lower speed, pause, fluid where appropriate
- grinder gouge: too much pressure → lighter passes, switch to file/flap disc

### Micro‑practice (60–90 minutes)

**Goal:** controlled hole‑making and safe finishing.

1. Layout a 3‑hole line (e.g., 20 mm spacing) on scrap.
2. Center punch.
3. Drill pilot, then final size.
4. Deburr.
5. Measure spacing and diameters.
6. Repeat once and compare.

**Pass bar:** holes round and deburred, spacing within ±0.5 mm (tighter with drill press). No work spin incidents.

**Evidence:** setup photo, measurement table, notes on what to change next time.

# Engineering OS — Tooling Bridges (Marketplace Edition)

<aside>
🧩

**Who this is for**: builders who keep getting stuck on the “practical stuff” mid‑project (file exports, prototyping methods, instrumentation, bench ops, quality).

**Purpose**: give you enough grounding to recognize what is coming, avoid common traps, and go deeper only when the project demands it.

**How to use**:

- Jump to the section that matches your blocker (G–K).
- Each section follows the same pattern: what it is → when to use → traps → quick procedures → micro‑practice → pass bar → artifacts.
- Save artifacts. That is how experience becomes reusable capability.
</aside>

---

## G) Fabrication file formats and exports (STL/STEP/DXF/Gerbers)

### Why this matters

Beginners lose days to:

- exporting the wrong format
- unit and coordinate mistakes
- sending shops unusable files
- generating incorrect Gerbers or incomplete manufacturing packages

This section defines a minimum‑viable export pipeline from CAD → fabrication.

---

### G1) File formats: what they are and when to use them

#### STL

**What it is:** a triangle mesh (no true curves, no features).

**Use for:**

- 3D printing (FDM/resin)
- rough visualization
- CAM workflows that accept mesh

**Do not use for:**

- precision machining
- editable CAD handoff
- drawings

**Common trap:** treating STL as “the CAD.” It is a surface approximation.

**Best practice**

- Export high enough mesh resolution for curved surfaces (avoid faceting).
- Verify in slicer before printing.
- Keep STEP or native CAD as the source of truth.

---

#### STEP (.step/.stp)

**What it is:** solid model exchange with real geometry.

**Use for:**

- vendor handoff
- assembly integration
- CAM
- MCAD exchange

**Default choice** for most mechanical exchange.

**Best practice**

- Use STEP for machine shops and integration into other CAD.
- Include correct units and verify by importing into a fresh session or a viewer.

---

#### IGES (.igs/.iges)

**What it is:** older geometry exchange, often surfaces.

**Use for:** legacy systems and specific surface workflows.

**Avoid unless you must.** STEP is usually better.

**Common trap:** IGES imports as broken surfaces, which creates repair work.

---

#### DXF

**What it is:** 2D geometry exchange (lines/arcs).

**Use for:**

- laser / waterjet / router
- flat parts and panels
- gaskets
- engraving
- PCB outlines (sometimes)

**Best practice**

- Confirm the shop’s expectations (layers, units, line types, text).
- Include a reference dimension or scale marker.

---

#### SVG (honorable mention)

**Use for:** laser cutters, UI graphics, some CNC/engraving workflows.

**Common trap:** scaling differences between programs.

---

#### Gerbers + NC Drill (PCB fabrication)

**What they are:** PCB fabrication outputs (copper, mask, silkscreen, outline) plus drill files.

**Use for:** sending boards to PCB fab houses.

**Common traps:** missing layers, wrong outline, wrong drill mapping.

---

#### Pick‑and‑place + BOM + assembly drawings (PCB assembly)

**What they are:** placement coordinates, parts list, and human‑readable assembly notes.

**Use for:** SMT assembly services (PCBA).

**Common traps:** mismatched refdes, wrong rotation/origin, incorrect footprints, missing alternates.

---

### G2) “Choose the export” cheat sheet

- **3D print** → STL (plus STEP for archive)
- **Machine shop / CNC** → STEP + drawing PDF (or STEP + CAM package)
- **Laser / waterjet** → DXF (2D)
- **Sheet metal** → DXF (flat pattern) + drawing + bend notes
- **PCB fab** → Gerbers + NC Drill + fab notes
- **PCB assembly** → Gerbers + BOM + pick‑and‑place + assembly drawing + test notes

---

### G3) DXF rules for laser/waterjet/router (newbie‑safe)

#### Geometry rules

- Use true arcs/circles, not segmented polylines (unless requested).
- Remove duplicate lines and overlaps.
- Close contours for cut profiles (no gaps).
- Put etch/engrave geometry on a separate layer.

#### Layer conventions (simple)

- `CUT_OUTER` (through cut)
- `CUT_INNER` (holes/slots)
- `ETCH` (marking/engraving)
- `BEND` (sheet metal)
- `TEXT` (if allowed)

#### Tabs, kerf, and lead‑ins (conceptual)

- **Kerf** is the material removed by the jet/beam. Shops often compensate.
- **Tabs** hold parts in place to prevent drop‑out.
- If tolerances matter, specify which dimensions are critical and how they will be measured.

#### DXF validation checklist

- [ ]  Units match expectation (mm vs inches)
- [ ]  One closed outer profile per part
- [ ]  No duplicates or overlaps
- [ ]  Critical holes called out in a drawing
- [ ]  Material, thickness, and finish specified

---

### G4) CAM exports: coordinate systems and unit traps (CNC sanity)

#### Common failure modes

- Units: mm vs inches
- Origin confusion: part zero vs machine zero vs CAM zero
- Orientation errors: mirrored top/bottom
- Z‑zero confusion: top of stock vs top of part vs table
- Tool diameter/compensation mistakes

#### Minimum‑viable CAM sanity flow

1. Define stock size and datum surfaces.
2. Set WCS/origin explicitly (corner or center).
3. Simulate toolpaths.
4. Run an air cut (Z above stock).
5. Cut a test piece in cheap material.
6. Measure and adjust offsets.

#### Always include in a CAM package

- Part STEP
- Drawing with critical dimensions
- Setup sheet: origin location, tool list, feeds/speeds (even if rough)
- Notes: which side is up, fixturing assumptions

---

### G5) PCB outputs: what to export and how not to mess it up

#### Minimum PCB fab package

- Gerbers: copper layers, solder mask, silkscreen, paste (if needed), outline
- NC Drill (plated + non‑plated if applicable)
- Readme: thickness, copper weight, solder mask color, surface finish, impedance notes (if any)

#### Minimum PCB assembly package (PCBA)

- BOM (MPNs, alternates, quantities)
- Pick‑and‑place (XY, rotation)
- Assembly drawing (polarity, pin‑1, special parts)
- Programming/test notes (how to verify a good board)
- Stencil file or paste layer confirmation (when relevant)

#### Common PCB output traps

- Board outline missing or on the wrong layer
- Drill files not matching pads
- Paste layer errors (assembly defects)
- Pick‑and‑place origin inconsistent
- Rotation conventions differ between tools and vendors

#### PCB export validation (must do)

- Open Gerbers in a Gerber viewer.
- Verify: outline present, drills align with pads, text readable.
- Confirm polarity marks.
- Check paste apertures for fine‑pitch parts.

---

### G6) Naming and revisioning (traceable fab files)

**Principle:** fab files must be uniquely identifiable and traceable to a design state.

**Simple naming standard**

`PROJECT_SUBASSY_REV_VERSION_DATE_FORMAT`

Examples:

- `CCA_PCB_REV_A_v1.2_2025-12-29_[GERBERS.zip](http://GERBERS.zip)`
- `ENCLOSURE_TOP_REV_A_v0.4_2025-12-29_STEP.step`
- `BRACKET_MOTOR_REV_B_v0.2_2025-12-29_DXF.dxf`

**What goes in every fab zip**

- Fabrication files
- Readme including:
    - revision
    - units
    - material/finish
    - critical dimensions
    - contact for questions
- Hashes/checksums (optional but pro)

---

### G7) Micro‑practice (45–90 min)

Export the same part as STL, STEP, and DXF and validate each.

1. Pick a simple bracket model.
2. Export STL (print), STEP (vendor), DXF (flat face).
3. Open each in a different viewer/tool.
4. Confirm units, orientation, and geometry integrity.

**Pass bar:** you can explain which format is for what, and your DXF cut geometry matches CAD dimensions.

**Artifacts:** exported files + one screenshot per viewer + a 5‑line readme.

---

## H) Electronics prototyping techniques (beyond “breadboard vs PCB”)

### Why this matters

The false choice is:

- messy breadboards (unreliable)
- full custom PCBs (too early, expensive, slow)

There are intermediate methods that let you learn fast and reduce risk.

---

### H1) Prototyping spectrum (when to use what)

#### Breadboard (solderless)

**Use for:** quick logic tests, very low current circuits, basic sensor breakout experiments.

**Avoid for:** high frequency, high current, precision analog, vibration.

**Breadboard limits**

- intermittent connections
- high resistance contacts
- parasitic capacitance/inductance
- ground noise and weird resets

**Rule:** breadboard is for “does this concept work,” not “is this stable.”

---

#### Perfboard / stripboard

**Use for:** robust prototypes, low‑to‑moderate complexity.

**Pros:** stronger than breadboard, custom routing.

**Cons:** time‑consuming and error‑prone without planning.

**Best practice**

- Sketch routing first.
- Use buses for power and ground.
- Add strain relief.

---

#### Dead‑bug / Manhattan style

**Use for:** quick RF/analog hacks.

**Pros:** fast for certain layouts.

**Cons:** hard to reproduce. Can be messy for beginners.

---

#### Breakout boards and modules (default for Rev A)

**Use for:** most early builds.

- MCU dev boards
- sensor breakouts
- power modules/regulators

**Pros:** fast progress, fewer footprint mistakes.

**Cons:** not final form factor. Wiring complexity grows.

**Rule:** modules first, custom PCB later.

---

#### Proto PCB / solderable breadboard

**Use for:** making wiring semi‑permanent without a full PCB design cycle.

---

#### Wire‑wrap

**Use for:** niche digital prototypes.

**Beginner note:** only if you have a specific reason.

---

### H2) The “bring‑up harness” (sacrificial wiring)

**What it is:** a known‑good wiring harness used during bring‑up that you fully expect to replace later.

**Why it works**

- Separates circuit correctness from final cable management.
- Makes probing easy.
- Reduces damage risk to the final assembly.

**Bring‑up harness rules**

- Label both ends.
- Leave extra length for probing.
- Include test points for rails and key signals.
- Use connectors that will not fall apart mid‑test.

---

### H3) Connector habits (Dupont pain points and better defaults)

#### Dupont jumpers (why they fail)

- loose retention
- inconsistent contact
- vibration failures
- easy to mis‑plug

**Use for:** short‑lived lab tests only.

#### Better beginner defaults

- JST‑XH / JST‑PH for low power and signal
- screw terminals for quick power prototypes
- ferrules for stranded wire into screw terminals
- for harsh environments: sealed families (when ready)

**Habit:** choose keyed connectors with strain relief.

---

### H4) Power prototyping rules

- Start with a current‑limited supply.
- Add a fuse or polyfuse for first power‑up.
- Verify rails at the load, not just at the supply.
- Add local decoupling near modules (even in prototypes).

---

### H5) Micro‑practice (60–90 min)

Build the same sensor readout three ways:

1. breadboard
2. breakout + harness
3. perfboard/proto PCB

Compare stability and debug ease.

**Pass bar:** you can explain why breadboard failed (if it did) and what improved with the harness/proto board.

**Artifacts:** photos of each build, logs showing stability, and a short lessons‑learned note.

---

## I) Instrumentation and debug primer (DMM/scope/LA/thermal)

### Why this matters

Owning tools is not the same as making trustworthy measurements. Tools lie when technique is wrong.

---

### I1) DMM fundamentals

**Best uses**

- voltage verification
- continuity checks (with caution)
- resistance spot checks
- current measurement (with setup awareness)

**Continuity lies (common trap)**

- The beep can occur through unexpected paths (ESD diodes, pullups, parallel circuits).
- Beep does not mean “acceptable short.”

Rule: if continuity surprises you, measure resistance and understand the path.

**Diode mode**

- Useful for checking protection diodes, LED polarity, and junction behavior.
- Useful for “is this pin clamped to a rail?”

**Burden voltage (current measurement trap)**

- Series current measurement introduces voltage drop that can change system behavior.
- Symptoms: resets, “wrong” current.

Rule: if the measurement changes behavior, use a shunt resistor or clamp method.

---

### I2) Oscilloscope basics that matter immediately

- Probe compensation matters.
- Grounding matters: long ground leads create ringing that is not real.
    - Use a ground spring for fast edges when possible.
- Bandwidth matters: insufficient bandwidth makes edges look slower.
- Probe at the right location:
    - at the load pin
    - across decoupling capacitors (ripple)
    - across shunts (current waveform)

---

### I3) Logic analyzer (LA) setup

- Sample rate: you need multiple samples per bit.
- Thresholds: set logic thresholds correctly (3.3 V vs 5 V).
- Decode pitfalls:
    - SPI CPOL/CPHA mismatch
    - weak I2C pullups (slow edges)
    - UART baud mismatch

Rule: if decode fails, verify the electrical layer first.

---

### I4) Thermal debugging (IR vs thermocouple)

- IR cameras lie via emissivity (shiny metal reads wrong). Use tape/paint patches.
- Thermocouples are good for spot checks, but placement/contact matters.

Rule: verify “hot” parts with two methods when stakes are high.

---

### I5) Measurement plan template (copy/paste)

**Goal:** what question does this measurement answer?

**Signal/parameter:**

**Where to measure:** exact point

**Tool:** DMM / scope / LA / thermal

**Expected range:** min/typ/max

**Pass bar:** what counts as good

**Procedure:**

**Artifacts to save:** screenshots/logs/photos

**Notes:** grounding, thresholds, pitfalls

---

### I6) Micro‑practice (60–90 min)

Measure a PWM signal three ways:

1. DMM (average voltage)
2. scope (frequency, duty, rise time)
3. LA (frequency, duty, timing)

**Pass bar:** you can explain what each tool tells you and what it cannot tell you.

**Artifacts:** scope screenshot, LA capture, filled measurement plan.

---

## J) Bench setup and shop ops (habits that prevent chaos)

### Why this matters

Many failures come from bench chaos:

- lost parts
- unlabeled wires
- unknown tool state
- no evidence trail

---

### J1) ESD, lighting, and magnification (minimum viable)

**ESD**

- grounded ESD mat
- wrist strap for sensitive parts
- ESD bags/foam for storage

**Lighting**

- bright overhead + adjustable task light
- eliminate shadows

**Magnification**

- microscope or head loupe

Rule: if you cannot see it, you cannot control it.

---

### J2) Labeling standards (wires, connectors, bins)

**Wires**

- label both ends with the same ID
- include voltage or signal name when useful

**Connectors**

- label mating pair
- mark orientation when ambiguous

**Bins**

- part family + value range
- fasteners by size and length

Minimum standard: anything that can be unplugged must be labeled.

---

### J3) Part storage and minimum inventory discipline

**Beginner‑friendly system**

- small bins + labels
- one active project tray
- one incoming parts tray
- one to‑rework tray

**Minimum discipline**

- store leftovers immediately
- keep BOM links in one place
- do not mix similar‑looking parts

---

### J4) Consumables restock checklist (copy/paste)

- [ ]  solder + flux
- [ ]  wick + tips
- [ ]  IPA + wipes/brush
- [ ]  heat shrink + tape
- [ ]  zip ties + labels
- [ ]  spare blades/bits/discs
- [ ]  gloves + eye protection
- [ ]  filament/resin (if applicable)

---

### J5) Evidence capture setup (make it frictionless)

**Minimum setup**

- phone tripod or desk arm
- a default photo area with good lighting
- screenshot hotkeys
- standard folder naming

**File naming default**

`DATE_PROJECT_ARTIFACT_TYPE_ID`

Example: `2025-12-29_CCA_SCOPE_PWR_RAIL_EVD-014.png`

Rule: if capture is annoying, you will not do it.

---

### J6) Micro‑practice (30–60 min)

Set up your bench so you can:

- photograph a setup in 10 seconds
- capture a scope screenshot and file it correctly
- label a cable in 30 seconds

**Pass bar:** you can capture and file evidence without “I will clean it up later.”

**Artifacts:** photo of bench layout + your naming convention.

---

## K) Assembly quality and inspection (what “good” looks like)

### Why this matters

Many builds work once, then fail because:

- solder joints crack
- crimps pull out
- prints delaminate
- bolts loosen
- alignment drifts

This section defines minimal acceptance criteria and low‑tech QC.

---

### K1) Visual acceptance criteria (baseline)

**Solder joints**

- Good: smooth fillet, proper wetting, no cracks, no bridges
- Bad: dull/grainy (cold), balled solder, lifted pad, bridges

**Crimps**

- Good: tight conductor crimp, insulation support, no stray strands
- Bad: crushed insulation, exposed strands, loose pull‑out, wrong die imprint

**3D prints**

- Good: consistent extrusion, strong layer adhesion, no major warp
- Bad: under‑extrusion, delamination, warped mating surfaces

**Weld beads**

- Good: consistent bead, no obvious porosity/undercut, adequate fusion
- Bad: porous, undercut, cold lap, inconsistent penetration

---

### K2) Low‑tech QC tests (high leverage)

- Pull tests (wires/crimps): pull firmly. If it moves, it fails.
- Bend tests: flex near joints and watch for intermittent faults.
- Shake tests: shake assembly, listen for rattles, re‑check connectors.
- Fit checks: assemble/disassemble multiple times; verify nothing degrades.

Rule: if it cannot survive simple abuse, it will not survive real life.

---

### K3) Cosmetic vs functional defects

**Often tolerable in Rev A**

- minor print stringing
- non‑critical scratches

**Must fix**

- cracked solder joints
- loose connectors
- misaligned holes that stress parts
- anything affecting safety, sealing, or electrical reliability

---

### K4) Torque discipline, witness marks, and thread engagement

- Torque critical fasteners consistently.
- Use witness marks (paint pen line across bolt head onto part).
- Ensure adequate thread engagement, especially in soft materials.

---

### K5) Assembly inspection checklist (copy/paste)

- [ ]  no loose fasteners
- [ ]  witness marks on critical bolts
- [ ]  no exposed conductors
- [ ]  strain relief present
- [ ]  connectors fully seated and keyed correctly
- [ ]  no sharp edges cutting cables
- [ ]  functional test passes after light shake/bend

---

### K6) Micro‑practice (60–90 min)

Build a small assembly and run QC:

- solder a connector
- crimp two wires
- mount a bracket or printed part with fasteners

Then:

- pull test wires
- shake test assembly
- run a functional test before and after

**Pass bar:** no functional change after abuse tests, and all joints pass visual criteria.

**Artifacts:** before/after photos + completed checklist + test evidence.

---

## 3) Tooling domain bridges (mini‑modules)

Short primers so a novice can recognize the landscape and dive deeper when needed.

---

### TDB‑01) Laser cutting / waterjet basics

**Key concepts**

- kerf
- heat affected zone (laser)
- tabs
- DXF hygiene (closed profiles, no duplicates)

**Micro‑practice:** design a simple plate with slots/tabs. Order a cheap cut. Measure fit.

**Pass bar:** you can predict kerf/fit issues and produce a mating part.

---

### TDB‑02) Sheet metal basics

**Key concepts**

- bend allowance (K‑factor concept)
- hole placement near bends shifts
- PEM inserts for strong threads
- avoid tiny flanges and impossible bend radii

**Micro‑practice:** make a simple L‑bracket with holes. Compare predicted vs actual alignment.

**Pass bar:** bracket fits without forced assembly. Bend‑induced drift is understood.

---

### TDB‑03) Molding and casting basics

**Key concepts**

- draft angles
- silicone molds for urethane casting
- bubbles/voids (vacuum/pressure helps)
- shrinkage and cure time

**Micro‑practice:** cast a small part. Inspect voids and finish.

**Pass bar:** acceptable surface with minimal voids.

---

### TDB‑04) Thermal interface materials (TIMs) and heat paths

**Key concepts**

- contact quality dominates thermal performance
- pads vs paste vs adhesive trade‑offs
- mounting pressure matters
- air gaps are catastrophic

**Micro‑practice:** compare temperatures with pad vs paste under the same load.

**Pass bar:** peak temperature drops measurably and you can explain why.

---

### TDB‑05) Sealants and ingress protection (IP thinking)

**Key concepts**

- gaskets vs sealant vs potting
- strain relief is part of sealing
- IP ratings are system‑level

**Micro‑practice:** seal an enclosure seam. Do a controlled spray/drip test.

**Pass bar:** no ingress at defined exposure and failure points are documented.

---

### TDB‑06) Fastener systems (real‑world bolts)

**Key concepts**

- metric vs imperial, thread pitch
- grades/strength classes
- torque vs preload
- threadlocker vs anti‑seize
- washers, locking methods, witness marks

**Micro‑practice:** assemble a bracket, torque consistently, witness mark, re‑check after vibration.

**Pass bar:** fasteners stay put and you can justify the locking method.

---

### TDB‑07) Cable and connector ecosystems

**Key concepts**

- connector families (JST, Molex, Deutsch, etc.)
- strain relief and service loops
- ferrules for screw terminals
- correct crimp tools matter

**Micro‑practice:** build a labeled harness with keyed connector. Pull and bend test.

**Pass bar:** harness survives abuse tests and is easy to service.

---

### TDB‑08) Paint and finishing stack

**Key concepts**

- prep is most of the work (clean, scuff, degrease)
- primer selection by material
- cure time matters
- adhesion tests (tape test)

**Micro‑practice:** paint a small part with proper prep. Run a tape adhesion check.

**Pass bar:** coating adheres and finish is consistent.

---

### TDB‑09) Tool maintenance

**Key concepts**

- dull tools create bad parts and increase risk
- printer calibration is maintenance
- bits/discs are consumables
- logs prevent “mystery failures”

**Micro‑practice:** calibrate one tool (printer bed, probe comp, bit replacement) and document improvement.

**Pass bar:** output becomes more consistent and the setup is repeatable.

---

## Standard “Skill Bridge” artifact pack (use everywhere)

- Setup photo (tool + fixturing visible)
- Result photo + measurement
- Completed checklist or measurement plan
- Notes: what went wrong, what changed, what rule you will follow next time

# Engineering OS — Mechanical & Manufacturing (Marketplace Draft)

### What this page is

A practical mechanical + manufacturability support layer that sits next to an Engineering OS checklist.

Use it to avoid the “worked on my desk but not in the real world” failures:

- Loose fasteners
- Cracked prints
- Tolerance stack-ups
- Heat and vibration issues
- Cable strain
- Impossible assembly
- Revision chaos

### How to use

Each section includes:

- **Core concepts** (beginner-readable)
- **Rules of thumb** (act immediately)
- **Micro‑prototypes** (1–4 hour tests)
- **Checklists + pass bars** (stop at “good enough”)

---

## 10‑Minute Quickstart (apply to your current build)

Create a Notion page called **Mechanical Snapshot** and capture:

- Where it mounts (vehicle/desk/enclosure/etc.)
- Loads (push/pull, weight, vibration, shock, heat)
- Assembly constraints (tools, access, service frequency)
- Interfaces (connectors, cable exits, seals, mounting holes)
- Manufacturing method (3DP/CNC/sheet metal/off-the-shelf)

Then do two fast sanity checks today:

1. Identify your service access path (how you will open/remove/replace).
2. Identify the top three tolerance risks (holes, fits, connector alignment).

---

## 1) Fasteners & Tolerancing 101

**Scope**: threads, torque, locking, GD&T lite, stack-ups.

### Fasteners: what matters most (practical truth)

Fasteners are about **clamp force** and **not loosening**, not “tight = good.”

### Key definitions (simple)

- Thread type (metric M3/M4 or imperial #6‑32)
- Pitch
- Engagement length
- Clamp force
- Torque (imprecise, but practical)

### Thread selection (beginner-safe defaults)

- Small electronics/fixtures: **M2.5 / M3**
- General small assemblies: **M4 / M5**
- Vehicle-ish/high load: depends heavily — do not guess; look up spec

Rule: standardize early. A build that uses nine fastener types is a maintenance trap.

### Engagement rules of thumb

Broad heuristics (for critical loads, use proper design references):

- Steel screw into steel nut: ~1× diameter engagement
- Steel screw into aluminum: ~1.5× diameter
- Screw into plastic: use inserts; threads in plastic are fragile unless designed for it

### Torque + locking

Vibration loosens fasteners via micro-slips.

Common locking methods:

- Nyloc nuts
- Threadlocker (blue for removable; avoid on plastics unless compatible)
- Lock washers (often less effective than people think)
- Nord‑lock wedges
- Safety wire

Rule: if it vibrates, assume it will loosen unless proven otherwise.

### GD&T lite (minimum internal model)

You do not need full GD&T to win, but you do need defined geometry.

Key idea:

- Datums define reference surfaces (what “true” is).

Minimum: define which surfaces/edges matter for alignment.

### Tolerance stack-ups

If multiple parts have tolerances, errors add up.

Classic failures:

- Connector does not line up with enclosure cutout
- Holes do not align across layers
- Lid does not close because print shrank or warped

Rule: any alignment that crosses part boundaries should include adjustability or clearance.

### Fastener micro‑prototypes

**MP‑FAST‑1: Vibration loosen test**

Assemble with locking method. Shake/vibrate (vehicle drive, sander table).

Pass bar: no loosening after defined duration; witness marks unchanged.

**MP‑FAST‑2: Serviceability timing**

Time removal and reinstall.

Pass bar: serviceable in < X minutes without damage.

### Fastener checklist

- [ ]  Fasteners standardized where possible
- [ ]  Locking strategy exists for vibration
- [ ]  Fasteners are accessible with real tools
- [ ]  Service removal tested at least once
- [ ]  Not relying on threads cut into plastic unless designed for it

---

## 2) Materials & Processes

**Scope**: plastics vs metals, 3DP vs CNC vs sheet metal vs casting.

### The real decision is process + environment

Material is not “PLA vs aluminum.” It is:

- Loads + impacts + fatigue
- Temperature exposure
- UV exposure
- Moisture/chemicals
- Tolerance needs
- Lead time + cost
- Assembly method (inserts, adhesives, etc.)

### Fast material selection (practical defaults)

**3D printing**

- PLA: easy, stiff, poor heat resistance, can creep
- PETG: tougher, better temp than PLA, can be stringy
- ABS/ASA: better temp, ASA handles UV better, warping risk
- Nylon: tough, fatigue resistant, absorbs moisture, harder to print
- CF-filled: stiff, abrasive, may be brittle

**Metals**

- Aluminum: light, machinable, good brackets/housings
- Steel: strong, heavy, corrosion risk unless coated
- Stainless: corrosion resistant, tougher to machine

### Process selection quick guide

- 3DP: fastest iteration, lower strength/precision
- CNC: strong, accurate, higher cost, slower
- Sheet metal: strong option for enclosures/brackets at scale
- Casting/injection: only when volume justifies tooling

Rule: prototypes are usually 3DP; production tends to move to CNC/sheet as requirements stabilize.

### Material/process micro‑prototypes

**MP‑MAT‑1: Heat soak**

Expose to expected max temp for 1–2 hours.

Pass bar: no warping, fit remains, no creep.

**MP‑MAT‑2: Drop/impact**

Drop from realistic height.

Pass bar: no cracks; function preserved; mounting points survive.

### Materials/process checklist

- [ ]  Material fits temperature and environment
- [ ]  Process can hit required tolerances
- [ ]  Wear surfaces use inserts/bushings/hard materials
- [ ]  Highest-risk feature prototyped in real or close material/process

---

## 3) Thermal & Vibration

**Scope**: heat paths, sinks, airflow hacks, isolation, potting vs conformal.

### Thermal is a path problem

Heat must flow:

**chip → PCB copper → interface → enclosure → air**

If any segment is weak, temperature rises.

### Thermal rules of thumb

- Copper area + thermal vias under hot parts (PCB)
- Thermal interface material when coupling to enclosure
- Do not seal heat sources in dead air unless designed for it
- Measure temperature early

### Vibration is fatigue + loosening

Vibration causes:

- Fastener loosening
- Wire fretting
- Connector failures
- Solder joint fatigue
- Cracked prints near stress risers

Hardening tactics:

- Cable strain relief
- Fillets (avoid sharp internal corners)
- Support heavy components
- Locking connectors
- Foam/grommets strategically (do not trap heat)

### Potting vs conformal

- Conformal coat: moisture protection, serviceable-ish
- Potting: strong protection and isolation, but often kills repairability

Rule: do not pot unless you know why and accept the consequences.

### Thermal/vibration micro‑prototypes

**MP‑TV‑1: Worst‑case run thermal test**

Run full power workload for 15–30 minutes. Measure hotspots.

Pass bar: below derating limits with margin.

**MP‑TV‑2: Cable + connector fatigue**

Wiggle/strain cables repeatedly.

Pass bar: no intermittent connections; strain relief holds.

### Thermal/vibration checklist

- [ ]  Heat sources and heat path identified
- [ ]  Temps measured under realistic load
- [ ]  Strain relief on all external cables
- [ ]  Vibration loosening addressed (locking/inserts/reinforcement)
- [ ]  Stress risers avoided (fillets, ribs)

---

## 4) Packaging & Mounting

**Scope**: ingress, strain relief, cable management, serviceability.

### Packaging is a system

Packaging failures often look like:

- Works until moved
- Connector broke
- Water got in
- Cannot service without destroying

### Ingress protection (IP) basics

You do not need certification to benefit from:

- Gaskets on seams
- Drip loops on cables
- Sealed connectors when exposed
- Breathable vents for pressure equalization

Rule: if it might see moisture, design water paths. Water always wins.

### Strain relief

Every cable leaving a device must have strain relief.

Options:

- Zip‑tie anchors
- Cable glands
- Clamp plates
- Grommets
- Service loops with retention

Rule: never let solder joints or connector pins take mechanical load.

### Serviceability

Ask:

- How do I open it?
- Can I replace the battery?
- Can I reflash firmware?
- Can I replace a connector?

Rule: if you cannot service it, treat it as disposable and decide if that is acceptable.

### Packaging micro‑prototypes

**MP‑PACK‑1: Open/close cycle**

Open and close enclosure 20 times.

Pass bar: threads do not strip; seals survive; alignment holds.

**MP‑PACK‑2: Cable abuse**

Pull, twist, bend cables realistically.

Pass bar: no intermittent behavior; no damage.

### Packaging checklist

- [ ]  Mounting points match real install constraints
- [ ]  Connector clearance and alignment tolerance exists
- [ ]  Strain relief for all external cables
- [ ]  Enclosure opens without damage
- [ ]  Heat can escape or is intentionally managed

---

## 5) Drawings & Rev Control

**Scope**: drawing types, title blocks, ECO impacts, supplier handoff.

### Drawings are communication

If someone else cannot build it from your docs, you do not have manufacturing-ready information.

### Drawing types

- Part drawing
- Assembly drawing
- Exploded view
- Interface drawing (cutouts, connectors, mounting patterns)

Hobby minimum: clean dimensioned sketch + hole pattern + notes.

Product minimum: drawings with revision control.

### Title block essentials

- Part name + number
- Revision
- Material/process
- Units
- Tolerances (general + critical)
- Date + author
- Notes (finish, deburr, inserts)

### Revision control rules

- Every change increments revision (Rev A/B/C or 0.1/0.2)
- Never overwrite old exported manufacturing files
- Archive exports in dated release folders with checksums

### ECO impact thinking

Before changing, ask:

- Does it break compatibility with existing parts?
- Does it require rework of built units?
- Does it change tooling/fixtures?
- Does it change testing?

### Supplier handoff pack (minimum viable)

- Drawing PDFs
- STEP files
- Notes about critical features
- Tolerances and finishes
- Quantity + requested lead time

### Drawings/rev control checklist

- [ ]  Every part has a revision identifier
- [ ]  Exports archived (no regen without rev bump)
- [ ]  Assembly order documented
- [ ]  Critical dimensions explicitly called out
- [ ]  Supplier pack complete enough to quote/build

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

# Engineering OS — Software, Data & Tooling (Marketplace Draft)

### What this page is

A practical software + data operating layer for engineering projects (embedded, hardware-adjacent, robotics, telemetry, apps, internal tooling).

It exists to make work:

- **Reproducible** (builds and results survive “new laptop day”)
- **Reviewable** (decisions and changes are legible)
- **Shippable** (releases are real artifacts, not vibes)

The goal is rigor without bureaucracy.

### How to use

You do not “implement Module C.” You pull the right tools at the right time:

- Solo hobby: minimal workflows (still reproducible)
- Team or product: stronger guardrails (CI, security, release discipline)

---

## 10‑Minute Quickstart (do today)

Create a `/project` repo structure and add these four files now:

1. [`README.md`](http://README.md) (what it is, how to run/build, how to flash/test)
2. [`CHANGELOG.md`](http://CHANGELOG.md) (human-friendly changes by version)
3. `LICENSE` (even if private, pick intentionally later)
4. `docs/decisions/` (ADR Lite entries)

Then create a **Release Pack** template:

- `release/`
    - `manifest.json`
    - `checksums.sha256`
    - `artifacts/` (binaries, configs)
    - [`notes.md`](http://notes.md)

If you do only this, future-you will already be ahead of most builders.

---

## 1) Version Control for Solo & Teams

**Scope**: Git workflows, tags, releases, LFS.

### Why version control is non-negotiable (even solo)

Version control is not backup. It is:

- A time machine
- An audit trail
- A way to ship known-good snapshots

If you are not tagging known-good states, you do not have releases. You have vibes.

### Repo anatomy (works for embedded + app + tooling)

Recommended top-level structure:

```
/docs
  /decisions
  /test
  /architecture
/src
/hw            (schematics, pin maps, board notes)
/scripts
/tools         (formatters,local utilities)
/third_party   (submodules or vendored deps)
/release
[README.md](http://README.md)
[CHANGELOG.md](http://CHANGELOG.md)
LICENSE

```

If you have firmware + host tooling:

- `firmware/`
- `host_tools/`
- `shared/` (schemas, message definitions)

### Branching workflows (choose based on reality)

**Solo or small team (recommended default): trunk-based + tags**

- `main` is always buildable
- Feature branches are short-lived
- Merge frequently
- Release via tags: `v0.3.0`

Pros: simple and fast.

Cons: requires discipline not to merge broken code.

**Larger teams: GitFlow-lite**

- `main` = releases only
- `develop` = integration
- `feature/*`, `release/*`, `hotfix/*`

Pros: clearer separation.

Cons: overhead and merge complexity.

Rule: do not adopt GitFlow because it sounds “pro.” Adopt it because your team needs it.

### Tags + release packaging

Use semantic versioning when possible: `vMAJOR.MINOR.PATCH`

- MAJOR: breaking
- MINOR: features
- PATCH: fixes

Minimum release ritual:

- Tag commit
- Generate artifacts
- Generate checksums
- Write release notes
- Store in `/release/vX.Y.Z/`

### Git LFS (large binaries)

Use Git LFS for:

- Datasets
- Large logs
- Model files
- Binaries you must track

Avoid committing:

- Generated build outputs
- Huge raw logs (store externally, index in Notion)

### VC Checklist (minimum viable)

- [ ]  Repo exists and builds from a clean clone
- [ ]  `.gitignore` excludes build junk and secrets
- [ ]  Tags exist for known-good states
- [ ]  Releases include artifacts and notes, not just code

---

## 2) CI/CD for Hardware‑Adjacent Projects

**Scope**: automated builds, unit tests, artifacts.

### What CI/CD means here

CI/CD is: every change triggers a repeatable pipeline that:

- Builds
- Runs tests
- Produces artifacts
- Makes regressions obvious

Even if you never deploy automatically, CI is still worth it.

### Minimal CI pipeline (start here)

On every push or PR:

1. Lint/format check
2. Build (firmware + host tools)
3. Unit tests
4. Package artifacts (zip)
5. Upload artifacts (CI storage)

Stretch goals:

- Hardware-in-the-loop smoke test
- Static analysis
- Dependency scanning

### Reproducible builds

Reproducible means build outputs do not depend on personal machine state.

Tactics:

- Pin tool versions (compiler, SDK)
- Use devcontainer/Docker when feasible
- Store build metadata (version, commit hash)

### Artifact zips (what they should contain)

- Firmware binary + map file (if applicable)
- Config defaults
- Schema/message definitions
- Flashing instructions
- Version/commit ID

### CI/CD Checklist (minimum)

- [ ]  One-click build in CI passes
- [ ]  Artifacts generated automatically
- [ ]  Version info embedded in binaries/log output
- [ ]  Pipeline documented in README

---

## 3) Code Quality Lite

**Scope**: style, static analysis, review, test pyramid.

### Code quality is risk management

You are reducing:

- Integration bugs
- Regressions
- “Only runs on my machine” failures

### Style guides (pick and enforce)

Pick one and automate:

- C/C++: clang-format + clang-tidy
- Python: ruff + black
- JS/TS: eslint + prettier

Rule: style debates end at the formatter.

### Static analysis (cheap wins)

- Catches null derefs, unused vars, dead code
- Run in CI
- Do not block progress on noisy warnings. Tune gradually.

### Code review checklist (even solo)

Before merging:

- Is behavior tested?
- Are error cases handled?
- Are timeouts present?
- Are resources cleaned up?
- Are logs meaningful?
- Would future-me understand this diff?

Solo tip: do a self-review 30 minutes later before merging.

### Test pyramid (practical)

- Unit tests: fast, many
- Integration tests: fewer, interface-focused
- System tests: minimal but meaningful (“does the device work?”)

Hardware-adjacent reality: fewer unit tests than pure software is fine. Compensate with stronger integration tests + evidence.

### Code Quality Checklist

- [ ]  Formatter + linter enforced
- [ ]  Unit tests exist for critical logic
- [ ]  Integration tests cover interfaces
- [ ]  Failures are logged and actionable

---

## 4) Data Logging & Telemetry

**Scope**: schemas, time bases, sync, compression, missing data, privacy.

### Logging is a product feature

Bad logging makes debugging impossible and can corrupt data.

Four goals:

1. Debuggability
2. Performance insight
3. Auditability
4. User value

### Schema design

Define:

- Message types
- Field names and units
- Data types and ranges
- Versioning strategy

Rule: if you cannot write it as a schema, you do not understand your data.

### Time bases (common failure)

Define:

- What “time” means (monotonic vs wall clock)
- Sync approach (multi-device)
- Timestamp resolution

Best practice:

- Device logs monotonic time
- Optionally also logs wall time
- Include sync events (GPS, NTP, host handshake)

### Compression + storage strategy

- Compress in chunks (not per record)
- Prefer append-only logs
- Include checksums per chunk
- Index files for partial reads

### Missing data handling

Missing data is reality. Make it explicit:

- Missing markers
- Sequence counters
- Drop rate stats
- Reconnection logic for streams

### Privacy implications

Telemetry can contain location, identifiers, behavior patterns.

Minimum:

- Do not log secrets
- Document what you collect
- Provide delete/export path

### Telemetry micro-prototypes

**MP-DATA-1: Logging integrity under stress**

Flood logs, drop packets, reboot mid-write.

Pass bar: logs remain parseable and corruption is bounded.

**MP-DATA-2: Multi-source time alignment**

Log from two sources (MCU + host) and verify alignment.

Pass bar: drift measured and within tolerance.

### Logging Checklist

- [ ]  Schema exists and is versioned
- [ ]  Timestamps defined and consistent
- [ ]  Logs survive reset/power loss reasonably
- [ ]  Missing data represented explicitly
- [ ]  Privacy constraints documented

---

## 5) Scripting for Engineers

**Scope**: notebooks, plotting standards, report automation.

### The goal

Turn repeated manual work into:

- One command
- Consistent outputs
- Shareable evidence

### Notebook discipline

- One notebook = one purpose
- Parameterize inputs
- Export results (plots + CSV)
- Summary at top (“what did we learn?”)

Convert to scripts/pipeline when it matters.

### Plotting standards

Every plot includes:

- Title + date
- Axes labels + units
- Legend when needed
- Sample rate/window when relevant
- Data source reference (file name + hash if needed)

Avoid pretty plots that omit context.

### Auto-generated reports

Generate:

- Test summaries
- KPI tables
- Plots
- PDF/HTML report

### Scripting Checklist

- [ ]  Scripts produce deterministic outputs from given inputs
- [ ]  Plots include units and context
- [ ]  Outputs saved and linked in Evidence Vault

---

## 6) Basic App/Tool UX

**Scope**: affordances, glanceability, accessibility, dark mode pitfalls.

### UX for engineering tools reduces mistakes

Make the right thing easy and the wrong thing hard.

### Glanceability rules

- Show the 3–7 most important values
- Make status obvious (OK/WARN/FAIL)
- Avoid dense text
- Use consistent units and scales

### Accessibility minimums

- Readable font size
- Sufficient contrast
- Do not rely on color alone
- Keyboard navigation for key actions (if applicable)

Dark mode pitfall: low-contrast gray-on-gray dashboards that hide errors.

### UX Micro‑prototype

**MP-UX-1: 30-second usability test**

Give it to someone new:

- Find current status
- Start/stop logging
- Export data

Pass bar: they succeed without explanation.

### UX Checklist

- [ ]  Critical states obvious
- [ ]  Risky actions have confirmation
- [ ]  Errors are actionable
- [ ]  Export/share is easy

---

## 7) Security & Privacy Basics

**Scope**: threat model lite, secrets, SBOM, dependency scanning.

### Security is realistic threat models

Prevent common failures:

- Leaked API keys
- Insecure updates
- Dependency compromise
- Exposed debug ports

### Threat model lite

Answer:

- What are you protecting?
- Who might attack?
- Where are entry points?
- What happens if compromised?

### Secrets handling (non-negotiable)

- Never commit secrets
- Use `.env` locally (ignored)
- Use CI secrets vault
- Rotate keys when leaked

### SBOM + dependency scanning

If you ship:

- Know what you depend on
- Track vulnerabilities
- Have an update plan

### Security Checklist

- [ ]  Debug ports protected/disabled for release (if needed)
- [ ]  Secrets never in repo
- [ ]  OTA/update integrity checks (if used)
- [ ]  Dependency scanning exists for shipped software

---

## 8) Local vs Cloud Decisions

**Scope**: latency, cost, reliability, ops burden.

### The decision is tradeoffs

- Latency
- Cost
- Offline requirements
- Maintenance burden
- Privacy constraints

### Quick guidance

Use local-first when:

- Offline reliability matters
- Low latency matters
- Privacy is critical
- You want fewer failure modes

Use cloud when:

- Multi-device sync is essential
- Shared access matters
- You can tolerate outages
- You can support operations

Hybrid is common:

- Local logging + optional cloud upload

### Local/Cloud Checklist

- [ ]  Offline behavior defined
- [ ]  Data retention policy defined
- [ ]  Failure modes defined (cloud down behavior)
- [ ]  Cost estimated at realistic scale

# Engineering OS — DFX Pack (Marketplace Draft)

### What this page is

A marketplace-ready **DFX Pack (Design-for-X)** you can drop into an Engineering OS.

It’s organized as a set of lightweight “mini-specs” you can implement as pages or databases. Each section includes:

- **What this is** (intent and scope)
- **Artifacts to produce** (minimum outputs)
- **How to build** (step-by-step)
- **Quality check** (a single hard test of readiness)
- **Hobby vs Product** (calibrated rigor)

---

## B) DFX Pack (Design-for-X)

## B1 — DFM (Design for Manufacturability)

**What this is**

A focused check that the design can be built consistently by someone who is not you, using realistic tools and tolerances.

**Artifacts to produce**

- DFM review report (risks, fixes, validated tolerances)
- Vendor or assembler pre-quote or written feedback confirming no blockers

**How to build (step-by-step)**

1. Open “DFX / B1 — DFM” in Notion.
2. List critical features that could block builds (tight tolerances, exotic processes, rare materials).
3. Send the design to a real assembler or fab for a quick pass. Capture constraints and red flags.
4. Update the design or document mitigations. Record a final “go/no-go.”

**Quality check (don’t skip)**

- Could a third party build ≥10 units with the current files and achieve the same result?

**Hobby vs Product**

- *Hobby:* One-page DFM notes plus confirmation from a maker shop or peer builder.
- *Product:* Formal DFM report with tolerance stack-ups, panelization/fixtures (HW), build scripts (SW), and vendor sign-off.

---

## B2 — DFA (Design for Assembly)

**What this is**

Reduce assembly time and errors through clear instructions, keyed parts, and minimal variation.

**Artifacts to produce**

- Illustrated Assembly Work Instructions (WIs)
- Takt-time estimate (minutes per unit) and error-proofing notes

**How to build (step-by-step)**

1. Photograph each assembly step and annotate torque, specs, and part IDs.
2. Remove unique fasteners where possible. Add labels and physical keying.
3. Have someone new assemble from the WIs. Time it, capture failure points, then refine.

**Quality check (don’t skip)**

- Can a novice complete assembly within the expected time without asking questions?

**Hobby vs Product**

- *Hobby:* One page with photos, parts list, and short notes.
- *Product:* Versioned WIs, torque tables, tool list, part bins, and poka-yoke notes with measured takt.

---

## B3 — DFT (Design for Test)

**What this is**

Ensure you can prove functionality quickly and repeatably at build time.

**Artifacts to produce**

- Test-point or diagnostic map (HW) or health-check endpoints (SW)
- “Golden” bring-up script or fixture plan with pass/fail criteria

**How to build (step-by-step)**

1. Define the minimum objective tests for “works vs broken.”
2. Expose probes and logging. Script setup checks.
3. Dry-run on 3+ units or instances. Time it and refine.

**Quality check (don’t skip)**

- Can you reach a definitive pass/fail in < N minutes without deep expertise?

**Hobby vs Product**

- *Hobby:* Manual checklist and a basic smoke test.
- *Product:* Automated or semi-automated fixture/script with versioned pass/fail logs tied to serials.

---

## B4 — DFR (Design for Reliability)

**What this is**

Design margin into parts and code to survive real conditions (power, thermal, noise, duty).

**Artifacts to produce**

- Derating table (key parts/loads) or headroom metrics (SW throughput/memory)
- Thermal/EMI plan and protection strategy

**How to build (step-by-step)**

1. Define worst-case environment and loads.
2. Choose parts and settings with ≥20–50% margin.
3. Measure real temperatures and loads. Update derating and add protections.

**Quality check (don’t skip)**

- Do measured hotspots and stress stay within derating limits during worst-case use?

**Hobby vs Product**

- *Hobby:* Quick stress check plus thermometer or monitor logs.
- *Product:* Formal derating worksheet, measured thermal map, EMI/ESD plan, watchdog and retry paths.

---

## B5 — Design for Service / Maintainability

**What this is**

Make routine maintenance and field repair fast, safe, and low-cost.

**Artifacts to produce**

- Service access map (open points, tools, seals)
- Replaceable modules and spares list with procedures

**How to build (step-by-step)**

1. Identify what fails or wears first and how it is replaced.
2. Add labels, keyed connectors, and tool-less access where possible.
3. Write or film a replacement procedure. Time it and refine.

**Quality check (don’t skip)**

- Can a tech swap a common part within the target time without guesswork?

**Hobby vs Product**

- *Hobby:* Brief notes plus photos describing common fixes.
- *Product:* Illustrated service manual, parts catalog, calibration steps, and time standards.

---

## B6 — DFCost (Cost)

**What this is**

Verify the design meets unit-cost targets across volumes, including test, build, and packaging.

**Artifacts to produce**

- Costed BOM with volume breaks
- Roll-up including assembly, test, packaging, and NRE

**How to build (step-by-step)**

1. Gather quotes and price breaks. Include labor and test time.
2. Build a cost model by volume and run sensitivity (10–20% swings).
3. Identify top cost drivers and alternates.

**Quality check (don’t skip)**

- Does the design still hit cost targets at realistic yields?

**Hobby vs Product**

- *Hobby:* Simple BOM price plus rough labor estimate.
- *Product:* Formal model with sensitivity, alternates, and negotiated supplier terms.

---

## B7 — DFCompliance / Safety Pre-Check

**What this is**

Early check for blockers to certification and safety (materials, creepage/clearance, emissions, labeling).

**Artifacts to produce**

- Applicable standards list (e.g., FCC/CE/UL/IEC/ISO)
- Labeling/marking matrix plus pre-scan and pre-test plan

**How to build (step-by-step)**

1. Identify mandatory standards by market and use.
2. Map design constraints (clearances, shielding, markings).
3. Plan pre-tests, log findings, and adjust.

**Quality check (don’t skip)**

- Are there any obvious blockers to certification (materials, creepage, emissions)?

**Hobby vs Product**

- *Hobby:* List likely regulations and do a quick self-check.
- *Product:* Pre-compliance evidence plus certification plan with test-house notes.

---

## B8 — DFX Summary & Sign-off

**What this is**

A one-page decision log that freezes DFX choices and residual risks before build.

**Artifacts to produce**

- DFX decision log (risks, owners, due dates)
- Sign-off (name/date)

**How to build (step-by-step)**

1. Summarize DFM, DFA, DFT, DFR, service, cost, and compliance.
2. Record accepted risks and deferrals to Rev B.
3. Get explicit sign-off.

**Quality check (don’t skip)**

- Is each residual risk owned by a person and a date?

**Hobby vs Product**

- *Hobby:* Short note capturing major trade-offs.
- *Product:* Formal sign-off with version tie-in to the release gate.

---

## C) Supply Chain & Lifecycle

## C1 — BOM Normalization

**What this is**

Make every BOM line unambiguous and comparable (true Mfr PN plus key parameters).

**Artifacts to produce**

- Normalized BOM (Mfr PN, description, params, lifecycle, RoHS/REACH, MOQ/lead time)

**How to build (step-by-step)**

1. Replace vendor SKUs with true manufacturer part numbers.
2. Add key parameters (value, tolerance, voltage, package).
3. Add lifecycle, compliance, and lead times.

**Quality check (don’t skip)**

- Can a buyer source this BOM without asking you a single question?

**Hobby vs Product**

- *Hobby:* Simple table with Mfr PN and one vendor link.
- *Product:* Full parameterized BOM with compliance and availability fields.

---

## C2 — AVL (Approved Vendor List)

**What this is**

A controlled list of where you’re allowed to buy each line item.

**Artifacts to produce**

- AVL table (primary/secondary vendors, terms, contacts)

**How to build (step-by-step)**

1. For critical lines, add at least one alternate vendor or document exception.
2. Capture rep names, contract terms, and MOQs.
3. Link to quotes.

**Quality check (don’t skip)**

- If your primary vendor disappears, can you still build next month?

**Hobby vs Product**

- *Hobby:* Preferred vendor column.
- *Product:* Multi-source policy with contract details and escalation path.

---

## C3 — Lifecycle & PCN/EOL Watch

**What this is**

A system to hear about obsolescence before it stops production.

**Artifacts to produce**

- Lifecycle tracker plus PCN subscriptions
- Last-time-buy (LTB) policy

**How to build (step-by-step)**

1. Subscribe to PCNs for key components.
2. Run a monthly status check (G/Y/R).
3. Define LTB triggers and buffer.

**Quality check (don’t skip)**

- Will you catch an EOL in time to react?

**Hobby vs Product**

- *Hobby:* Manual once-per-quarter check.
- *Product:* Automated alerts into Notion/Jira with an owner.

---

## C4 — Alternates & Parameter Equivalence

**What this is**

Pre-vetted substitute parts with known verification steps.

**Artifacts to produce**

- Alternates table (param match, layout fit, re-verify steps)

**How to build (step-by-step)**

1. Define acceptable parameter windows for each critical line.
2. Identify alternates and list required re-tests.
3. Validate one alternate now if feasible.

**Quality check (don’t skip)**

- Could you swap to the alternate in a week without a redesign?

**Hobby vs Product**

- *Hobby:* “If out of stock, buy X.”
- *Product:* Formally vetted alternates with re-qualification plan.

---

## C5 — Procurement Plan

**What this is**

Ensure long-lead items arrive before they block milestones.

**Artifacts to produce**

- PO plan by milestone, long-lead list, expedite rules

**How to build (step-by-step)**

1. Back-schedule from build dates using lead times.
2. Place POs for long-leads early and document buffer.
3. Define when to expedite or swap.

**Quality check (don’t skip)**

- Are any milestones at risk solely due to lead time?

**Hobby vs Product**

- *Hobby:* Simple buy list with dates.
- *Product:* Milestone-tied PO calendar and risk flags.

---

## C6 — Traceability (Lots/Receipts/QA)

**What this is**

Link every build to the part lots that went into it.

**Artifacts to produce**

- PO → receipt → QA intake log with lot/batch numbers and photos

**How to build (step-by-step)**

1. Record lot numbers and upload label photos at receipt.
2. Log QA checks (visual and measurement).
3. Tie lot IDs to builds and serials.

**Quality check (don’t skip)**

- Can you identify which units contain a bad lot in < 1 hour?

**Hobby vs Product**

- *Hobby:* Keep invoices plus quick notes.
- *Product:* Structured lot tracking with COAs and QA sign-offs.

---

## C7 — Inventory & Kitting

**What this is**

Keep parts findable and stage builds without surprises.

**Artifacts to produce**

- Bin map, min/max levels, and pre-build kits

**How to build (step-by-step)**

1. Assign bins and labels. Track quantities.
2. Pre-kit parts per batch. Seal and tag.
3. Run cycle counts monthly.

**Quality check (don’t skip)**

- Can you stage a build in one pass with zero surprises?

**Hobby vs Product**

- *Hobby:* Labeled bins plus manual counts.
- *Product:* Lightweight inventory system with reorder triggers.

---

## C8 — Cost Roll-Up & Targets

**What this is**

A live picture of unit cost vs target across volumes.

**Artifacts to produce**

- Cost roll-up by volume with charts and variance to target

**How to build (step-by-step)**

1. Sum BOM, labor, test, packaging, and shipping.
2. Add yield and scrap assumptions.
3. Track variance and improvement actions.

**Quality check (don’t skip)**

- Does current cost meet target at your first real production run?

**Hobby vs Product**

- *Hobby:* BOM plus rough labor.
- *Product:* Full P&L roll-up by volume tier.

---

## C9 — Compliance & Import/Export

**What this is**

Paperwork and declarations to ship legally.

**Artifacts to produce**

- COO, HS codes, ECCN (if any), MSDS, restricted substances data

**How to build (step-by-step)**

1. Request COO, HS, ECCN, and MSDS from suppliers.
2. Add fields to BOM rows.
3. Prepare a shipping packet template.

**Quality check (don’t skip)**

- Can you clear customs without an email volley?

**Hobby vs Product**

- *Hobby:* Basic country and HS.
- *Product:* Full compliance table and shipping pack.

---

## C10 — Obsolescence Plan

**What this is**

A playbook for sudden EOLs and part shortages.

**Artifacts to produce**

- EOL response flow, pre-approved alternates, customer comms template

**How to build (step-by-step)**

1. Define triggers (PCN/EOL alert, backorder > X weeks).
2. Pre-write change notices and internal steps.
3. Keep alternates verified.

**Quality check (don’t skip)**

- Can you execute a swap within one sprint?

**Hobby vs Product**

- *Hobby:* “If part dies, use B.”
- *Product:* Policy with timelines, notices, and verification gates.

---

## D) Security & Privacy Mini-Spec

## D1 — Scope & Data Inventory

**What this is**

A list of what data exists, why, where it goes, and how long it stays.

**Artifacts to produce**

- Data flow map and retention table

**How to build (step-by-step)**

1. List inputs, outputs, logs, and third-party services.
2. Define purpose and retention for each.
3. Mark sensitive items (PII, keys).

**Quality check (don’t skip)**

- Can a non-engineer point to where their data goes?

**Hobby vs Product**

- *Hobby:* Simple table plus basic retention.
- *Product:* Full inventory with owners and lawful basis.

---

## D2 — Threat Model (light STRIDE)

**What this is**

Top risks to assets and how you mitigate them.

**Artifacts to produce**

- Table: asset → threat → mitigation → residual risk

**How to build (step-by-step)**

1. Identify assets (device, API, keys, data).
2. Brainstorm threats (spoofing, tampering, information disclosure, etc.).
3. Assign mitigations and accept or reduce residual risk.

**Quality check (don’t skip)**

- Are the top five risks covered by concrete controls?

**Hobby vs Product**

- *Hobby:* One-page list with simple controls.
- *Product:* Reviewed model with tickets for each control.

---

## D3 — Security Controls & Architecture

**What this is**

Documented controls at each trust boundary.

**Artifacts to produce**

- Architecture diagram
- Control checklist (TLS, authZ, input validation, rate limits)

**How to build (step-by-step)**

1. Draw trust boundaries (user, device, backend, third-party).
2. Assign controls for each boundary.
3. Reference standard libraries and avoid custom crypto.

**Quality check (don’t skip)**

- Is every high-risk path actually controlled?

**Hobby vs Product**

- *Hobby:* Basic TLS/auth and validation.
- *Product:* Defense-in-depth with hardening guides.

---

## D4 — Key & Secret Management

**What this is**

How secrets are created, stored, rotated, and revoked.

**Artifacts to produce**

- Key inventory
- Rotation policy
- Compromise runbook

**How to build (step-by-step)**

1. List all keys and secrets and where they live.
2. Store via secure elements, OS keystores, or secret vaults.
3. Define rotation and incident steps.

**Quality check (don’t skip)**

- Can you rotate a key in production without downtime?

**Hobby vs Product**

- *Hobby:* `.env` with basic hygiene.
- *Product:* Managed secrets, rotation schedules, and no hardcoded keys.

---

## D5 — Secure Update & Reproducible Builds

**What this is**

Guarantee you ship what you built and updates are authentic.

**Artifacts to produce**

- Signed update policy
- Reproducible build instructions
- Hashes per release
- SBOM per release

**How to build (step-by-step)**

1. Pin dependencies and record hashes.
2. Sign releases and verify on install.
3. Generate an SBOM per release.

**Quality check (don’t skip)**

- Can a second machine reproduce the same artifact with the same hash?

**Hobby vs Product**

- *Hobby:* Versioned builds and checksums.
- *Product:* Signed reproducible builds with CI enforcement and SBOM.

---

## D6 — Data Retention & Deletion

**What this is**

How long you keep data and how you delete or export it.

**Artifacts to produce**

- Retention schedule
- Export/delete procedures

**How to build (step-by-step)**

1. Set default retention by data type.
2. Script deletion and export where feasible.
3. Test both on dummy data.

**Quality check (don’t skip)**

- Can you fulfill a delete/export request within your stated time?

**Hobby vs Product**

- *Hobby:* Manual deletion on request.
- *Product:* Automated workflows and audit logs.

---

## D7 — Privacy Notice (Plain Language)

**What this is**

A short, human-readable explanation of data use.

**Artifacts to produce**

- One-page privacy summary

**How to build (step-by-step)**

1. Explain what you collect, why, where it is stored, how long, and user rights.
2. Link it from the UI and docs.
3. Keep jargon out.

**Quality check (don’t skip)**

- Can a teen explain your policy back to you?

**Hobby vs Product**

- *Hobby:* Readable page in repo/site.
- *Product:* Versioned notice with change log and contact.

---

## D8 — Security Testing (Basic)

**What this is**

Automated and manual checks to catch obvious security issues.

**Artifacts to produce**

- Static analysis results
- Dependency scans
- AuthZ tests
- Fuzz or negative-test notes

**How to build (step-by-step)**

1. Add static and dependency scans to CI.
2. Write at least one negative test per sensitive function.
3. Track and fix findings.

**Quality check (don’t skip)**

- CI fails on critical vulnerabilities or forbidden patterns.

**Hobby vs Product**

- *Hobby:* Periodic scans plus manual checks.
- *Product:* CI-enforced gates with remediation SLAs.

---

## D9 — SBOM & Vulnerability Management

**What this is**

A list of components in each release and how you handle CVEs.

**Artifacts to produce**

- SBOM per release
- Vulnerability scan and resolution log

**How to build (step-by-step)**

1. Generate SBOM at build time.
2. Scan against CVE feeds and file tickets.
3. Patch and verify.

**Quality check (don’t skip)**

- No known critical CVEs in the current release.

**Hobby vs Product**

- *Hobby:* SBOM snapshot and occasional scan.
- *Product:* Continuous scanning and tracked remediation.

---

## D10 — Security Sign-off

**What this is**

Checkpoint documenting residual security risk.

**Artifacts to produce**

- Mini-spec with decisions, acceptances, and owner/date

**How to build (step-by-step)**

1. Summarize top risks and mitigations.
2. List residual risks and acceptance.
3. Sign-off before release.

**Quality check (don’t skip)**

- Are residual risks explicit and owned?

**Hobby vs Product**

- *Hobby:* Short note in the release.
- *Product:* Formal gate with approver list.

---

## F) Reliability & Safety

## F1 — Reliability Targets & Environment

**What this is**

Declare reliability goals and real-world conditions.

**Artifacts to produce**

- Targets (e.g., MTBF/mission time)
- Environment table (temp/shock/vibe/EMI/humidity/duty)

**How to build (step-by-step)**

1. Describe typical and worst-case use.
2. Set measurable reliability targets.
3. Tie tests to these targets.

**Quality check (don’t skip)**

- Are targets realistic for the environment?

**Hobby vs Product**

- *Hobby:* Descriptive notes.
- *Product:* Quantified targets bound to verification tests.

---

## F2 — Derating & Thermal Budget

**What this is**

Ensure electrical and thermal margins under worst case.

**Artifacts to produce**

- Derating table
- Thermal measurements and plots

**How to build (step-by-step)**

1. Define worst-case loads and ambient.
2. Apply derating rules and select parts accordingly.
3. Measure hotspots and update the table.

**Quality check (don’t skip)**

- Do measured temperatures and loads stay within limits?

**Hobby vs Product**

- *Hobby:* IR thermometer spot checks.
- *Product:* Instrumented thermal profile with guardbands.

---

## F3 — FMEA (Failure Modes & Effects)

**What this is**

Systematic list of how things fail and how you prevent it.

**Artifacts to produce**

- FMEA table (severity/occurrence/detection, RPN, mitigations)

**How to build (step-by-step)**

1. Break the system into functions.
2. For each, list failure modes and effects.
3. Prioritize by RPN and add mitigations.

**Quality check (don’t skip)**

- Are top-RPN items mitigated or redesigned?

**Hobby vs Product**

- *Hobby:* Short table of top five risks.
- *Product:* Full FMEA with tracked actions.

---

## F4 — Fault Injection Plan

**What this is**

Deliberately trigger faults to verify safe behavior.

**Artifacts to produce**

- Fault matrix
- Expected behavior
- Test logs

**How to build (step-by-step)**

1. List critical faults (power dips, comms loss, sensor stuck).
2. Define expected safe response.
3. Run tests, log results, and fix gaps.

**Quality check (don’t skip)**

- Does the system fail safe or recover gracefully?

**Hobby vs Product**

- *Hobby:* Manual fault tests.
- *Product:* Scripted fault campaigns with evidence.

---

## F5 — Safety Analysis (Hazards & Protections)

**What this is**

Identify hazards and layer protections and warnings.

**Artifacts to produce**

- Hazard table (cause → effect → protection → warning)

**How to build (step-by-step)**

1. Brainstorm misuse and failure hazards.
2. Add protections (limits, interlocks, watchdogs).
3. Add user warnings where needed.

**Quality check (don’t skip)**

- Are severe hazards addressed by ≥2 protections?

**Hobby vs Product**

- *Hobby:* List plus basic mitigations.
- *Product:* Formal safety case linking to test evidence.

---

## F6 — Protection Hardware / Software

**What this is**

The fuses, TVS, limits, and timeouts that protect the system.

**Artifacts to produce**

- Protection list with thresholds and test evidence

**How to build (step-by-step)**

1. Choose protections per risk.
2. Implement thresholds and timeouts.
3. Validate trip and recovery behavior.

**Quality check (don’t skip)**

- Do protections trip predictably at the right thresholds?

**Hobby vs Product**

- *Hobby:* Basic fusing and limits.
- *Product:* Layered protections with certification-minded evidence.

---

## F7 — Life Testing / Burn-In

**What this is**

Run the system long enough to surface early failures.

**Artifacts to produce**

- Burn-in plan
- Acceptance criteria
- Logs

**How to build (step-by-step)**

1. Define soak time and stress profile.
2. Run life tests and monitor metrics.
3. Root-cause failures and retest.

**Quality check (don’t skip)**

- No new failures after the soak window, or failures are root-caused and fixed.

**Hobby vs Product**

- *Hobby:* Overnight run.
- *Product:* Multi-day or accelerated testing with statistics.

---

## F8 — Reliability Evidence Pack

**What this is**

A single place that supports reliability claims.

**Artifacts to produce**

- Plots, tables, and photos
- Procedures
- Verdicts tied to targets

**How to build (step-by-step)**

1. Collect all reliability tests and outcomes.
2. Tie each to a target or hazard.
3. Summarize verdicts and gaps.

**Quality check (don’t skip)**

- Can a reviewer validate reliability without talking to you?

**Hobby vs Product**

- *Hobby:* Short appendix of results.
- *Product:* Structured pack with traceability.

---

## F9 — Field Failure Feedback Loop

**What this is**

Capture real-world issues and convert them into fixes.

**Artifacts to produce**

- Intake form
- Triage flow
- RCA template
- Release gates

**How to build (step-by-step)**

1. Define severity and response targets.
2. Log defects with evidence and run root cause.
3. Gate releases on top-severity closures.

**Quality check (don’t skip)**

- Can a new field issue become a tracked fix within 48 hours?

**Hobby vs Product**

- *Hobby:* GitHub issues and labels.
- *Product:* SLA-based workflow with metrics.

---

## F10 — Safety Sign-off

**What this is**

Formal acceptance of residual safety risk.

**Artifacts to produce**

- Safety memo linking hazards → mitigations → tests
- Signatures

**How to build (step-by-step)**

1. Summarize hazards and protections.
2. Attach test evidence.
3. Obtain sign-off.

**Quality check (don’t skip)**

- Is any severe hazard left unowned?

**Hobby vs Product**

- *Hobby:* Short note acknowledging risks.
- *Product:* Formal gate with approvers and audit trail.

---

## G) Ops Pack (Owner’s Guide v2, Runbook, Service)

## G1 — Owner’s Guide v2 (Illustrated)

**What this is**

A friendly, picture-heavy guide for installation, use, and care.

**Artifacts to produce**

- Illustrated Owner’s Guide
- First-run checklist
- FAQs

**How to build (step-by-step)**

1. Photograph install and first run. Write steps in plain language.
2. Add “what you should see” screenshots.
3. Include safety notes and common mistakes.

**Quality check (don’t skip)**

- Can a first-time user succeed without help?

**Hobby vs Product**

- *Hobby:* One-pager with photos.
- *Product:* Versioned manual with accessibility and localization plan.

---

## G2 — Quick Start / Onboarding

**What this is**

A one-page “do this now” that gets a user from box to success.

**Artifacts to produce**

- Quick Start card or onboarding wizard checklist

**How to build (step-by-step)**

1. Reduce to five to seven steps.
2. Pre-fill defaults and include rollback.
3. Test with a new user.

**Quality check (don’t skip)**

- Setup time meets target on a clean system.

**Hobby vs Product**

- *Hobby:* Simple checklist.
- *Product:* Guided flow with telemetry for success rate.

---

## G3 — Ops Runbook

**What this is**

Daily, weekly, and monthly tasks that keep the system healthy.

**Artifacts to produce**

- Runbook with task frequencies
- Backup, update, and health check procedures

**How to build (step-by-step)**

1. List routine tasks with owners and timing.
2. Script where possible and document results.
3. Review monthly.

**Quality check (don’t skip)**

- Could an ops operator run this without contacting engineering?

**Hobby vs Product**

- *Hobby:* Short maintenance checklist.
- *Product:* Time-boxed SOPs, escalation contacts, and audit logs.

---

## G4 — Service Notes & Maintenance Schedule

**What this is**

When to replace, clean, or calibrate, with parts and tools.

**Artifacts to produce**

- Maintenance table
- Parts list
- Illustrated procedures

**How to build (step-by-step)**

1. Identify consumables and intervals.
2. Write replacement steps with photos.
3. Maintain a spares and tools list.

**Quality check (don’t skip)**

- Can maintenance be done within the budgeted time?

**Hobby vs Product**

- *Hobby:* Simple interval notes.
- *Product:* Versioned schedule with part numbers and service times.

---

## G5 — Troubleshooting Trees

**What this is**

Decision trees for the top user-visible issues.

**Artifacts to produce**

- Symptom → checks → fixes trees
- Error code map

**How to build (step-by-step)**

1. List most common failures.
2. Create short decision trees and test with a novice.
3. Include parts and tools needed per branch.

**Quality check (don’t skip)**

- Does each tree end in a fix or a precise escalation?

**Hobby vs Product**

- *Hobby:* FAQ-style steps.
- *Product:* Formal trees with MTTR targets.

---

## G6 — Support Workflow & SLAs

**What this is**

How issues are logged, prioritized, and resolved on time.

**Artifacts to produce**

- Intake form
- Severity levels
- Response and restore targets
- Escalation path

**How to build (step-by-step)**

1. Define severity and SLA times.
2. Create intake form and triage script.
3. Track and report SLA adherence.

**Quality check (don’t skip)**

- Are high-severity issues consistently resolved within SLA?

**Hobby vs Product**

- *Hobby:* Email plus spreadsheet.
- *Product:* Ticketing with dashboards and on-call rotation.

---

## G7 — RMA / Returns / Warranty

**What this is**

A smooth path for swaps and repairs with data capture.

**Artifacts to produce**

- RMA criteria
- Test-before-swap procedure
- Refurb and disposition steps

**How to build (step-by-step)**

1. Define what qualifies and what does not.
2. Test returned units before replacement.
3. Track outcomes and failure causes.

**Quality check (don’t skip)**

- Is the RMA loop within SLA and producing learnings?

**Hobby vs Product**

- *Hobby:* Email-based process.
- *Product:* Serialized RMAs tied to lots and RCA.

---

## G8 — Versioning & Field Configuration

**What this is**

Know what is deployed and keep it compatible.

**Artifacts to produce**

- Version matrix
- Compatibility rules
- Migration and rollback steps

**How to build (step-by-step)**

1. Adopt semantic versioning.
2. Document upgrade paths and blockers.
3. Provide rollback instructions.

**Quality check (don’t skip)**

- Can support identify version drift in minutes?

**Hobby vs Product**

- *Hobby:* Release notes plus manual tracking.
- *Product:* Central registry and enforced compatibility checks.

---

## G9 — Observability (Logs/Telemetry) & Privacy

**What this is**

Capture health data without violating privacy.

**Artifacts to produce**

- Log and metric list
- Retrieval steps
- Retention and redaction rules

**How to build (step-by-step)**

1. Choose key health metrics and error events.
2. Define where logs live and how to export.
3. Redact or make opt-in for personal data.

**Quality check (don’t skip)**

- Can a support case include objective diagnostics within 10 minutes?

**Hobby vs Product**

- *Hobby:* Local logs plus manual export.
- *Product:* Structured telemetry with consent and retention policy.

---

## G10 — Ops Handoff & Training

**What this is**

Training materials so others can run ops without you.

**Artifacts to produce**

- Training deck or video
- One-page cheat sheet
- Access provisioning checklist

**How to build (step-by-step)**

1. Record a run-through of install, operate, and support.
2. Create a one-page cheat sheet.
3. Gate access on completion.

**Quality check (don’t skip)**

- Can a new operator run solo after training?

**Hobby vs Product**

- *Hobby:* Short video plus notes.
- *Product:* Versioned training with tracked completion.

# Engineering OS — Supply Chain (Marketplace Draft)

### What this page is

A marketplace-ready, Notion-native **Supply Chain & Lifecycle** spec for an Engineering OS.

Each section below is designed to become a database (or page + linked database) and includes:

- **Purpose** and **Definition of Done**
- Suggested **Fields** (schema)
- A **CSV Starter** for quick import
- A pragmatic **SOP** and **Gates**
- **Relations** to preserve traceability across sourcing, quality, and releases

### How to use

1. Treat each section (C1–C10) as its own database.
2. Create the database using the **Fields** list.
3. Optional: copy the **CSV Starter** into a `.csv` and import it.
4. Wire relations once, then reuse across projects.

---

## C) Supply Chain & Lifecycle

## C1) Approved Vendor List (AVL)

**Purpose**: Define qualified suppliers per part category with contacts, terms, and risk context.

**Definition of Done**: Each critical part has at least one approved vendor (preferably two). Contacts and terms are recorded.

**Fields**

- Vendor Name (text)
- Category (PCB/Mech/IC/Cables/etc.)
- Approved For (parts/part families)
- Alt/Second Source (text)
- Contract Terms (lead/MOQ/Incoterms)
- Quality Status (Approved/Probation/Blacklisted)
- Contacts (name/email/phone)
- Notes/Risks (text)
- Review Date (date)

**CSV Starter**

```
Vendor,Category,ApprovedFor,Alt/Second Source,Contract Terms,Quality Status,Contacts,Notes/Risks,ReviewDate
JLCPCB,PCB,4-6 layer FR-4,PCBWay,"10d lead; FOB",Approved,"ops@...","+/- soldermask match",2025-12-28

```

**SOP**

1. List current and target vendors by category.
2. Attach sample orders or references and set quality status.
3. Capture contacts and terms. Add alternates where possible.
4. Review quarterly and update statuses.

**Gates**

- **Entrance**: BOM draft exists.
- **Exit**: All critical categories have at least one approved vendor. Contacts recorded.

**Relations**: BOM, Supplier Scorecards, Procurement Log.

**Hobby vs Product**

- **Hobby minimum**: One trusted vendor per category plus a backup name.
- **Product grade**: Dual-source strategy, signed terms, performance review cadence.

---

## C2) BOM with Lifecycle & Alternates

**Purpose**: Add lifecycle (NRND/EOL), lead time, and vetted alternates to every BOM line.

**Definition of Done**: 100% of BOM lines have lifecycle status. Critical items have at least one evaluated alternate.

**Fields**

- MPN (text)
- Description (text)
- Lifecycle (Active/NRND/EOL)
- Years to EOL (estimate)
- Primary Vendor (relation)
- Alternate MPNs (list)
- Form/Fit/Function Match (Yes/No + notes)
- Compliance (RoHS/REACH)
- Unit Price @ Volumes (1/100/1k)
- Lead Time (weeks)

**CSV Starter**

```
MPN,Description,Lifecycle,Yearsto EOL,Primary Vendor,Alternate MPNs,Form/Fit/Function,Compliance,Unit Price (100),LeadTime
ESP32-S3,MCU,Active,5,MCUdist,"STM32G4; RP2040","Partial (FW port)",RoHS,$3.20,10

```

**SOP**

1. Export the current BOM and add lifecycle and lead time columns.
2. For risky parts, identify alternates and evaluate form/fit/function.
3. Flag compliance and price tiers.
4. Review at each revision and keep current.

**Gates**

- **Entrance**: BOM baseline exists.
- **Exit**: Lifecycle filled. Alternates listed for all critical items.

**Relations**: AVL, Obsolescence Watch, ECOs.

**Hobby vs Product**

- **Hobby minimum**: Note availability and list one alternate.
- **Product grade**: PCN feeds, second-source verified, costed alternates.

---

## C3) Supplier Qualification & Scorecard

**Purpose**: Track supplier performance (quality, delivery, cost, support) to manage risk.

**Definition of Done**: Each active supplier has a scored record with evidence and action items.

**Fields**

- Supplier (relation)
- Metrics (Quality/Delivery/Cost/Support)
- Score (0–5 each)
- Evidence (RMA %, OTD %, quotes)
- Actions/Notes (text)
- Status (Good/Watch/Remediate)
- Review Date (date)

**CSV Starter**

```
Supplier,Quality,Delivery,Cost,Support,Evidence,Actions/Notes,Status,ReviewDate
JLCPCB,4,5,4,4,"OTD 98%; 0.5% scrap","Tighter mask notes",Good,2025-12-28

```

**SOP**

1. Define metric scales and what “3/5” means.
2. Review quarterly with evidence and update status.
3. Create and track actions for low scores.

**Gates**

- **Entrance**: First orders placed.
- **Exit**: Scores filled and actions assigned where needed.

**Relations**: AVL, Procurement Log, Incoming Inspection.

**Hobby vs Product**

- **Hobby minimum**: Thumbs-up/down notes after orders.
- **Product grade**: Threshold-based scorecards tied to sourcing decisions.

---

## C4) Sourcing Strategy & Lead-Time Plan

**Purpose**: Reduce schedule risk with forecast, buffer stock, and alternates.

**Definition of Done**: Lead times known. Buffers set. Buy windows scheduled.

**Fields**

- Part/Family (text)
- Current Lead Time (weeks)
- MOQ/Multiples (numbers)
- Buffer Policy (weeks or qty)
- Buy Window (dates)
- Alternate Trigger (rule)
- Owner (person)

**CSV Starter**

```
Part,LeadTime,MOQ,BufferPolicy,BuyWindow,AlternateTrigger,Owner
MCU,10,500,"8 weeks rolling",2026-Q1,"If LT>12w, switch alt",Alex

```

**SOP**

1. Pull lead times for critical parts and record MOQs.
2. Set buffers based on demand and risk.
3. Schedule buy windows.
4. Define triggers to switch to alternates.

**Gates**

- **Entrance**: Demand or build plan exists.
- **Exit**: All long-lead items have buffers and buy windows.

**Relations**: BOM, Build Plan, Procurement.

**Hobby vs Product**

- **Hobby minimum**: Note long-lead items and order early.
- **Product grade**: Rolling forecast, buffers, alternates with pre-approved ECO path.

---

## C5) Procurement Log & Traceability

**Purpose**: Maintain an audit trail of quotes, POs, receipts, and QA.

**Definition of Done**: Each purchase links vendor, lot/serial info, and receiving QA result.

**Fields**

- PO/Order ID (text)
- Vendor (relation)
- Part/MPN (relation)
- Qty Ordered/Received (numbers)
- Lot/Serial (text)
- Price/Terms (currency/text)
- Receiving QA (Pass/Fail + notes)
- Attachments (quote/receipt/COC)
- Date
- Owner

**CSV Starter**

```
PO/Order ID,Vendor,Part/MPN,Qty Ordered,Qty Received,Lot/Serial,Price,Receiving QA,Attachments,Date,Owner
PO-1021,MCUdist,ESP32-S3,500,500,L2025-12,$1600,Pass,"quote.pdf; coc.pdf",2025-12-28,Alex

```

**SOP**

1. Log every order and attach quotes and receipts.
2. Record lot/serials on receipt and run incoming QA.
3. Link to BOM line and record QA result.
4. Keep all docs searchable.

**Gates**

- **Entrance**: Buying begins.
- **Exit**: 100% traceability for critical parts.

**Relations**: BOM, AVL, Incoming Inspection, Compliance Docs.

**Hobby vs Product**

- **Hobby minimum**: Save receipts and vendor links. Jot lot info when present.
- **Product grade**: COA/COC attached, receiving checks logged, lot-level traceability.

---

## C6) Incoming Inspection Plan

**Purpose**: Verify parts meet spec before entering stock or build.

**Definition of Done**: Sampling plan and checks defined. Reject/return workflow documented.

**Fields**

- Part/Family (text)
- Critical Checks (dimensions, markings, tests)
- Sample Size (AQL or fixed)
- Tools/Fixtures (calipers, multimeter, jigs)
- Pass/Fail Criteria (text)
- Disposition (Accept/Quarantine/Reject)
- Owner
- Date

**CSV Starter**

```
Part,Checks,SampleSize,Tools,Pass/Fail,Disposition,Owner,Date
Sensors,"Marking; output @ 5V","5/lot","PSU;DMM","±2% @ 25°C",Accept,QA,2025-12-28

```

**SOP**

1. For each critical part, define checks and sample size.
2. Build quick jigs if needed.
3. Record results, disposition, and escalation.

**Gates**

- **Entrance**: First deliveries arrive.
- **Exit**: Plan in place, first runs executed, failures addressed.

**Relations**: Procurement Log, Fixtures, Risk Log.

**Hobby vs Product**

- **Hobby minimum**: Spot-check markings and basic function.
- **Product grade**: Documented AQL sampling, calibrated tools, NCR/return process.

---

## C7) Obsolescence Monitoring (PCN/EOL Watch)

**Purpose**: Catch PCN/EOL changes early and react (alternates, last buy).

**Definition of Done**: Subscriptions set. Owners assigned. Action rules defined.

**Fields**

- Part/MPN (relation)
- Watch Source (OEM/distributor alerts)
- Owner (person)
- PCN/EOL Status (None/PCN/EOL)
- Action Plan (Last buy/Alt/ECO)
- Deadline (date)
- Notes

**CSV Starter**

```
Part,WatchSource,Owner,PCN/EOL Status,Action Plan,Deadline,Notes
ESP32-S3,Espressif PCN feed,Alex,None,,,

```

**SOP**

1. Subscribe to vendor and distributor notifications.
2. Assign owners per part family.
3. On PCN/EOL: log, decide action, set deadline, execute.

**Gates**

- **Entrance**: BOM stable.
- **Exit**: All critical parts watched and actioned within deadlines.

**Relations**: BOM, ECOs, Sourcing.

**Hobby vs Product**

- **Hobby minimum**: Manual check before each purchase.
- **Product grade**: Automated feeds, owners, last-buy budgets, ECO path.

---

## C8) Inventory & Lot Tracking

**Purpose**: Know what you have, where it came from, and what was built with it.

**Definition of Done**: Stock levels tracked with lot/serial mapping to builds/units.

**Fields**

- Location (bin/shelf)
- Part/MPN (relation)
- Qty On Hand / Allocated / Available
- Lot/Serial (text)
- Build/WO Links (relations)
- Expiry/Date Codes (text)
- Owner
- Updated (date)

**CSV Starter**

```
Location,Part,QtyOnHand,Allocated,Available,Lot/Serial,BuildLinks,Expiry,Updated
BinA3,ESP32-S3,500,200,300,L2025-12,"WO-1001",2028-Wk12,2025-12-28

```

**SOP**

1. Create bins and label locations.
2. Receive lots with labels and update counts on issue/return.
3. Link lots to work orders and shipped units where applicable.

**Gates**

- **Entrance**: First stock on shelf.
- **Exit**: Real-time view of critical parts with lot linkage.

**Relations**: Procurement Log, Build Orders, RMA/Service.

**Hobby vs Product**

- **Hobby minimum**: Labeled boxes and spreadsheet counts.
- **Product grade**: Lot-level traceability tied to serial numbers and build records.

---

## C9) Compliance Docs (RoHS/REACH/CM/UL/CE as applicable)

**Purpose**: Centralize compliance evidence and declarations.

**Definition of Done**: Each applicable regulation has linked evidence tied to parts and builds.

**Fields**

- Regulation (RoHS/REACH/CM/UL/CE/…)
- Scope (part/product/packaging)
- Evidence Type (CoC/DoC/Test report)
- Link/File (attachment)
- Expiry/Version
- Owner/Reviewer
- Status (Requested/Collected/Validated)

**CSV Starter**

```
Regulation,Scope,EvidenceType,Link/File,Expiry/Version,Owner,Status
RoHS,Product,DoC,doclink,RevA,Alex,Collected

```

**SOP**

1. List applicable regulations by market.
2. Request evidence from vendors or test labs.
3. Store centrally, track versions/expiry, validate.

**Gates**

- **Entrance**: Markets identified and BOM stable.
- **Exit**: Evidence collected/validated, or a documented plan exists (test scheduled).

**Relations**: BOM, DfCompliance, Test Plan, Ops Pack.

**Hobby vs Product**

- **Hobby minimum**: Keep vendor RoHS statements and avoid restricted substances.
- **Product grade**: Controlled doc set with signed DoCs, lab reports, version control.

---

## C10) End-of-Life (EOL) / Sustaining Plan

**Purpose**: Plan spares, last-buy, and customer support beyond active sales.

**Definition of Done**: Spares policy, last-buy triggers, and sustaining support plan are documented.

**Fields**

- EOL Trigger (sales drop, part EOL, etc.)
- Last-Buy List (parts/qty)
- Spares Policy (qty/years)
- Support Window (years)
- Communication Plan (customers/suppliers)
- Owner
- Date
- Status (Draft/Approved)

**CSV Starter**

```
EOLTrigger,Last-Buy List,SparesPolicy,SupportWindow,Communication Plan,Owner,Status
Part EOL on MCU,"MCU 2k; PSU 1k","5% field base/yr","3 years","Email; site notice; distributor brief",PM,Approved

```

**SOP**

1. Define triggers and support window.
2. Calculate spares and last-buy quantities.
3. Draft communication templates and approve the plan.

**Gates**

- **Entrance**: Product in market or pre-launch.
- **Exit**: Approved plan with quantities and budgets.

**Relations**: BOM, Obsolescence Watch, Ops Pack, Business Lite.

**Hobby vs Product**

- **Hobby minimum**: Keep a few spares and document substitutes.
- **Product grade**: Formal sustaining plan with budget, spares, customer comms, deprecation policy.