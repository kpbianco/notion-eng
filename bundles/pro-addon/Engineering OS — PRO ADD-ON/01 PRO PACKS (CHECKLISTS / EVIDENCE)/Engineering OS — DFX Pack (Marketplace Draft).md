# Pack — DFX (Marketplace Draft)

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
