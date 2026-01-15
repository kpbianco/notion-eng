# Tooling & Shop Skills (Marketplace Edition)

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
