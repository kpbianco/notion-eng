# Engineering OS — Execution Infrastructure (Marketplace Draft)

### What this page is

This is the **execution infrastructure layer** for an Engineering OS.

Its job is to prevent the most common builder failure:

- The project only works on one machine.
- In one lab.
- With one person’s exact setup.

Use it to make work **repeatable**, **portable**, **safe**, and **findable** for:

- You
- Teammates
- Future customers

### How to use

Treat this as a supplemental system that supports normal project flow.

- Hobby projects: adopt the minimum safe setup.
- Professional projects: adopt full reproducibility and an audit trail.

---

## 10‑Minute Quickstart (do this today)

Create a folder called `ops/` (or a Notion section) and add:

1. **Known‑Good Toolchain** (versions + install steps)
2. **Lab Safety Rules** (power, ESD, batteries)
3. **File/Asset Naming Rules** (one page)
4. **Backup Plan** (what is backed up, where, how often)

Then pick one reproducibility method:

- Devcontainer / Docker (best), or
- “Known good versions” lockfile + scripted install.

If someone cannot clone and build within 30–60 minutes, you do not have infrastructure yet.

---

## 1) Toolchain Setup Guides

**Scope**: ECAD, MCAD, compilers, debuggers, analyzers.

### 1.1 Why the toolchain is a first-class artifact

Toolchains drift:

- Compilers change behavior
- SDKs break builds
- IDEs update silently
- Plugin versions mismatch

Your job is to define **Known Good**:

- Exact versions
- Install steps
- Validation checks

This turns “it broke” into “what changed?”

### 1.2 Toolchain inventory (what to document)

Create a **Toolchain Manifest** with:

**Hardware/Embedded**

- Compiler (GCC/Clang/ARM toolchain)
- SDK + version
- Flash tool + version
- Debugger (J‑Link/OpenOCD/etc.) + version
- Serial tools + drivers
- Python runtime + packages (if used for tooling)
- RTOS version (if applicable)

**Software/App**

- Language runtime version (Node/Python/Java/etc.)
- Package manager versions
- Build tools (CMake, Ninja, etc.)
- Linters/formatters

**ECAD/MCAD**

- CAD tool + version
- Libraries used + source
- Exporters + settings
- CAM outputs + settings

**Test/Analysis**

- Scope model + probe types
- Logic analyzer model
- Power supply model
- Measurement scripts versions

### 1.3 Install checks (the missing step)

Every toolchain guide must include a “verify install” step:

- Build a sample
- Flash a sample
- Run a script
- Generate a plot
- Open CAD and export a file

Rule: if you cannot verify, you cannot trust the install.

### 1.4 Known Good version strategy

Choose one:

**Option A: Simple pinning (fastest)**

- Document exact versions in Notion
- Store installers if allowed
- Disable auto-update where possible

**Option B: Devcontainer/Docker (best for repeatability)**

- Repo contains `Dockerfile` or `.devcontainer`
- One command creates an identical environment

**Option C: Scripted bootstrap**

- [`setup.sh`](http://setup.sh) installs dependencies
- Version checks run automatically

### Toolchain checklist (minimum)

- [ ]  Tool + version recorded for every critical element
- [ ]  Install steps documented
- [ ]  Verification step exists
- [ ]  Updates are controlled (not accidental)

---

## 2) Lab Setup & Safety

**Scope**: ESD, power discipline, fire safety, battery handling, chemicals.

### 2.1 Lab safety is engineering

Most lab incidents come from:

- Wrong supply voltage
- Current not limited
- Exposed conductors
- Li‑ion abuse
- “Just one quick test”

You will build faster and safer with discipline.

### 2.2 ESD basics (minimum viable)

You need:

- ESD mat (grounded properly)
- Wrist strap when handling sensitive ICs
- ESD-safe storage for boards

Rule: if you are touching unprotected boards, assume ESD risk exists.

### 2.3 Power discipline (the bring-up lifesaver)

Bring-up rule set:

- Always start with current limit low
- Increase in small steps
- Measure rails before connecting expensive parts
- Use a fuse or sacrificial bring-up harness where possible
- Know where the emergency off is

Brownout behavior: record what happens when voltage dips and returns.

### 2.4 Fire safety

Minimum:

- Appropriate extinguisher nearby
- Clear bench (no paper piles near hot tools)
- Do not leave high-energy tests unattended

### 2.5 Battery handling

Minimum:

- Charge on non-flammable surface
- Never charge damaged/swollen packs
- Store in safe container if possible
- Do not short leads

### 2.6 Chemicals basics (flux, solvents, adhesives)

Minimum:

- Ventilation
- Gloves when appropriate
- Proper storage
- Avoid mixing unknown solvents

### Lab safety checklist (minimum)

- [ ]  ESD controls exist and are used
- [ ]  Current limit always used for first power
- [ ]  Fire plan exists (extinguisher + clear area)
- [ ]  Battery handling rules written and followed
- [ ]  Hazardous chemicals stored/ventilated properly

---

## 3) File & Asset Hygiene

**Scope**: naming, hashes, manifests, release packs, storage/backup.

### 3.1 Goal: long-term retrievability

If you cannot find the right file six months later, it is not documentation. It is landfill.

This section enforces:

- Naming consistency
- Versioning
- Integrity (hashes)
- Backups

### 3.2 Naming conventions (simple and scalable)

Adopt:

- ISO dates: `YYYY-MM-DD`
- Revisions: `revA`, `revB` or `v0.3.1`
- Descriptive slugs: `power_bringup`, `icd_canbus`

Examples:

- `2026-01-04_revA_enclosure_step_export.step`
- `v0.3.0_fw_release_[notes.md](http://notes.md)`

### 3.3 File integrity (hashes)

Hashes prove a file did not change:

- Generate `sha256` hashes for release artifacts
- Store them in `checksums.sha256`

This protects you from:

- Accidental modifications
- Flashing the wrong file
- “Which file did we send the vendor?”

### 3.4 Manifests (what’s in a release)

A manifest tells you:

- What artifacts exist
- Their versions
- Their hashes
- What they’re for
- Build environment metadata

Rule: every shipped release gets a manifest.

### 3.5 Storage and backup strategy

Define:

- What is backed up (repo, CAD exports, evidence, release packs)
- Where (cloud + local)
- Cadence (daily/weekly)
- Retention policy
- Restore test (you must test restore)

Minimum:

- Git remote for code
- Cloud backup for CAD and evidence
- Local backup for critical exports

### Asset hygiene checklist

- [ ]  Naming convention documented and used
- [ ]  Releases have manifests + hashes
- [ ]  Evidence stored with context (not random screenshots)
- [ ]  Backup plan exists and restore has been tested once

---

## 4) Knowledge Base Patterns

**Scope**: Notion/docs that future-you can actually find.

### 4.1 The failure mode: wiki soup

Most Notion workspaces fail because:

- No structure
- No indexing
- Inconsistent naming
- Stale pages with no owner

You need a pattern:

- Consistent home page
- Consistent databases
- Consistent linking

### 4.2 The three-layer knowledge base model

**Layer 1 — Index (dashboard)**

- Project control panel
- Latest release
- Current risks
- Current milestone
- Quick links

**Layer 2 — Databases (structured truth)**

- Requirements
- Tests/Evidence
- Decisions (ADR)
- Parts/AVL
- Changes (ECO)
- Toolchain manifest

**Layer 3 — Pages (unstructured narrative)**

- Guides
- Deep dives
- Design notes
- Troubleshooting journals

Rule: searchable narrative is useful, but structured truth is what scales.

### 4.3 Page templates (so pages don’t rot)

Every page should include:

- Owner
- Last updated date
- Scope (what this page is for)
- Links to related records

Add a staleness banner:

- If not updated in X days, review.

### 4.4 Decision capture (linking to Module A/F)

Make it easy:

- Any major decision becomes an ADR entry
- ADR links to:
    - Risks it addresses
    - Tests verifying it
    - Release where it shipped

### Knowledge base checklist

- [ ]  One dashboard page per project
- [ ]  Databases for decisions/tests/releases exist
- [ ]  Page templates enforce owner/date/scope
- [ ]  Everything important is linked (no orphan pages)