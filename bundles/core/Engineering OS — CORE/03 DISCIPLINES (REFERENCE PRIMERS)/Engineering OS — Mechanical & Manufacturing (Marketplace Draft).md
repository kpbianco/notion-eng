# Mechanical & Manufacturing (Marketplace Draft)

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
