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