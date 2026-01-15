# Security (Marketplace Draft)

### What this page is

A marketplace-ready, Notion-native **Security & Privacy mini-spec** you can drop into an Engineering OS.

Each section is designed to become a database (or a page + linked database) and includes:

- **Purpose** and **Definition of Done**
- Suggested **Fields** (schema)
- A **CSV Starter** for quick import
- A pragmatic **SOP** and **Gates**
- **Relations** so security stays connected to requirements, releases, and operations

### How to use

1. Treat each section (D1–D7) as its own database.
2. Create the database using the **Fields** list.
3. Optional: copy the **CSV Starter** into a `.csv` and import it.
4. Revisit the gates at every baseline change and before release.

---

## D) Security & Privacy Mini-Spec

## D1) Threat Model (STRIDE-lite)

**Purpose**: Identify what can go wrong by asset and data flow, and define controls before build.

**Definition of Done**: Assets and data flows mapped. Threats enumerated. Likelihood and impact scored. Controls and owners assigned. Residual risk explicitly accepted. Review scheduled.

**Fields**

- Asset / Data Flow (text)
- Threat (select/text: spoofing, tampering, info disclosure, DoS, privilege escalation, repudiation, other)
- Vector (how)
- Impact (select: Low, Medium, High)
- Likelihood (select: Low, Medium, High)
- Control (prevent/detect/respond) (text)
- Owner (person)
- Residual Risk (text)
- Status (select: Open, Mitigated, Accepted)
- Review Date (date)

**CSV Starter**

```
Asset/Data Flow,Threat,Vector,Impact,Likelihood,Control,Owner,Residual Risk,Status,ReviewDate
Firmware update,Tampering,Unsigned update package,High,Med,"Sign + verify updates (Ed25519)",Alex,"Keys stored in HSM",Mitigated,2025-12-28
Telemetry log,Information disclosure,Intercept on Wi-Fi,Med,Med,"TLS + rotate creds",Alex,"User misconfig",Open,2026-01-10

```

**SOP**

1. List assets and flows (firmware, logs, update channel, cloud API).
2. Draw a simple DFD (boxes and arrows) and mark trust boundaries.
3. For each flow, brainstorm STRIDE threats and score impact and likelihood.
4. Choose controls (prevent, detect, respond). Assign owners and deadlines.
5. Record residual risk and acceptance. Schedule review.
6. Re-check at each architecture change and before release.

**Gates**

- **Entrance**: Interfaces frozen (or close).
- **Exit**: All High/High and High/Medium items have implemented controls and owners.

**Relations**: Requirements, ICD, SBOM, Build/Reproducibility, Vulnerability Mgmt, Ops/Runbook.

**Hobby vs Product**

- **Hobby minimum**: One-page table of assets → top five threats → one control each.
- **Product grade**: Full STRIDE by flow, scored risks, control test evidence, sign-offs, re-review on change.

---

## D2) Data Handling & Privacy Spec

**Purpose**: Define what data you collect, why, where it lives, how long, and who can access it.

**Definition of Done**: Data inventory completed. Retention and encryption defined. Roles, consent, and delete/export paths defined. Storage locations documented.

**Fields**

- Data Item (PII/telemetry/keys/config/etc.)
- Source (device/app/cloud/user)
- Purpose (text)
- Storage Location (device/cloud/SaaS + region)
- Retention (duration/condition)
- Access Role(s) (text)
- In-Transit Encryption (Y/N/method)
- At-Rest Encryption (Y/N/method)
- Anonymization/Pseudonymization (Y/N + method)
- Legal/Policy Basis (text, if applicable)
- DSR Process (export/delete path)
- Owner (person)

**CSV Starter**

```
Data Item,Source,Purpose,StorageLocation,Retention,Access Roles,In-Transit,At-Rest,Anonymization,Legal Basis,DSR Process,Owner
Device logs,Device,"Debug + QA","Local SD; Cloud S3 (us-west-2)","90 days","Eng read-only",TLS,AES-256,"Scrub PII","Legitimate interest","Support ticket + script",Alex

```

**SOP**

1. Inventory all data created and processed (including transient and debug).
2. For each item, define purpose, storage location, retention, and access roles.
3. Specify encryption in transit and at rest. Note key storage and rotation.
4. If personal data exists: define consent, policy, and delete/export path.
5. Publish a short privacy note in plain language.

**Gates**

- **Entrance**: Features defined.
- **Exit**: Every data item has retention, encryption, and access role defined.

**Relations**: Threat Model, SBOM, Ops/Runbook, Legal/Policy.

**Hobby vs Product**

- **Hobby minimum**: List what you log and where. Delete after X days.
- **Product grade**: Full data map, RBAC, KMS-managed keys, audit logs, DSR workflow.

---

## D3) SBOM (Software Bill of Materials) & Licenses

**Purpose**: Know every third-party component you ship, its license, and known CVEs.

**Definition of Done**: SBOM generated (SPDX/CycloneDX). Licenses recorded. CVEs triaged. Build hashes pinned.

**Fields**

- Component (name)
- Version (semver/commit)
- License (MIT/Apache-2.0/GPL/etc.)
- Origin (URL/source)
- Integrity (hash)
- Known CVEs (list/severity)
- Use Scope (prod/dev/tooling)
- Replacement Policy (alt/version)
- Owner/Reviewed (person/date)

**CSV Starter**

```
Component,Version,License,Origin,Integrity,Known CVEs,UseScope,Replacement Policy,Owner
lwIP,2.2.0,BSD-3,https://...,sha256:...,None,prod,"Pin minor; update quarterly",Alex

```

**SOP**

1. Generate SBOM from the build (lockfiles/container image).
2. Record licenses and check compatibility with distribution.
3. Scan CVEs and triage High and Critical. Assign remediation.
4. Pin versions and hashes and store SBOM with the release.

**Gates**

- **Entrance**: Build runnable.
- **Exit**: SBOM attached to release. License and CVE checks completed.

**Relations**: Vulnerability Mgmt, Releases, Compliance Docs.

**Hobby vs Product**

- **Hobby minimum**: Manual list of libraries and versions.
- **Product grade**: Automated SBOM per build, license policy checks, CI gating, signed attestation.

---

## D4) Build Reproducibility & Supply-Chain Security

**Purpose**: Ensure builds are deterministic, attestable, and verifiable.

**Definition of Done**: Toolchains pinned. Builds are containerized. Artifacts are signed with attestations. Verification steps documented.

**Fields**

- Build Input (repo/commit)
- Environment (container image digest)
- Reproducible (Y/N + notes)
- Artifact Hash (sha256)
- Signature/Attestation (Y/N + where)
- Dependency Policy (pin/verify/fail)
- SLSA Target (level)
- Verification Steps (doc link)

**CSV Starter**

```
BuildInput,Environment,Reproducible,ArtifactHash,Signature/Attestation,DependencyPolicy,SLSATarget,VerificationSteps
repo@a1b2c3,[ghcr.io/app@sha256:...,Yes,sha256:...,Sigstore](http://ghcr.io/app@sha256:...,Yes,sha256:...,Sigstore) attest,"Pinned + checksum",2,doclink

```

**SOP**

1. Pin compilers, SDKs, and dependencies. Build in a container.
2. Produce hashes. Sign artifacts. Store attestation with the release.
3. Add a [VERIFY.md](http://VERIFY.md) with exact reproduce and verify steps.
4. Fail CI on dependency drift or unsigned artifacts.

**Gates**

- **Entrance**: CI set up.
- **Exit**: Signed, reproducible artifact with verification steps.

**Relations**: SBOM, Releases, Ops/Runbook, Security Policies.

**Hobby vs Product**

- **Hobby minimum**: Document tool versions, keep a Dockerfile, save hashes.
- **Product grade**: Hermetic CI, signature + attestation, dependency verification, promotion gates.

---

## D5) Secrets & Access Control (Keys, Tokens, Roles)

**Purpose**: Prevent credential sprawl and enforce least privilege with rotation.

**Definition of Done**: Central storage in place. Role matrix defined. Rotation policy defined. Audit logs available.

**Fields**

- Secret Name (text)
- Scope (dev/stage/prod/device)
- Storage Method (vault/envfile/HSM)
- Rotation Policy (interval/trigger)
- Access Roles (list)
- Last Rotated (date)
- Audit Log Link (file/url)

**CSV Starter**

```
Secret,Scope,StorageMethod,RotationPolicy,Access Roles,Last Rotated,AuditLog
OTA_SIGN_KEY,prod,HSM,"6 months","Release-mgr; CI",2025-11-01,link

```

**SOP**

1. Inventory all secrets. Move to a central store. Remove from code.
2. Define roles and least-privilege access.
3. Set rotation cadence and document emergency rotation.
4. Enable audit logging and review monthly.

**Gates**

- **Entrance**: Services/features defined.
- **Exit**: No plaintext secrets in repo. Rotation and audit in place.

**Relations**: Threat Model, Build/Reproducibility, Ops/Runbook.

**Hobby vs Product**

- **Hobby minimum**: Password manager + private .env, rotate manually.
- **Product grade**: Vault/HSM, short-lived tokens, audited access, break-glass policy.

---

## D6) Vulnerability Management & Patch Policy

**Purpose**: Discover, triage, fix, and ship security updates continuously.

**Definition of Done**: Scanners scheduled. SLAs defined by severity. Releases include notes. Customer notice path exists.

**Fields**

- Source (scanner/feed/report)
- CVE/Issue (id)
- Affected Component (SBOM link)
- Severity (Low/Med/High/Critical)
- Decision (Fix/Defer/Accept)
- SLA (days)
- Status (Open/In Progress/Fixed/Released)
- Evidence (PR/build/release)

**CSV Starter**

```
Source,CVE/Issue,Affected,Severity,Decision,SLA,Status,Evidence
NVD,CVE-2025-1234,OpenSSL 3.0.14,Critical,Fix,7,In Progress,PR#221

```

**SOP**

1. Enable weekly scans (code, deps, containers).
2. Triage and set decision and SLA. Assign an owner.
3. Patch, test, and release. Publish a customer note if needed.
4. Review backlog monthly. Ensure no overdue criticals.

**Gates**

- **Entrance**: SBOM available.
- **Exit**: No overdue items per SLA. Fixes released or documented.

**Relations**: SBOM, Releases, Test Evidence, Ops/Runbook.

**Hobby vs Product**

- **Hobby minimum**: Occasional library updates.
- **Product grade**: SLA policy, dashboards, release advisories, backport plan.

---

## D7) Incident Response Mini-Runbook

**Purpose**: Respond quickly and consistently to security and privacy events.

**Definition of Done**: Severity ladder defined. First-hour checklist exists. Contacts and comms templates exist. Postmortem format defined. Rehearsal completed.

**Fields**

- Trigger (what happened)
- Severity (S1–S4)
- First-Hour Actions (checklist)
- Forensics/Evidence (what to collect)
- Customer/Regulatory Comms (templates)
- Roles/Contacts (on-call/escalation)
- Postmortem Link

**CSV Starter**

```
Trigger,Severity,First-Hour Actions,Forensics,Comms,Roles/Contacts,Postmortem
Suspected key leak,S2,"Revoke; rotate; disable pipeline","Audit logs; repo history","Customer advisory draft","Second on-call; Eng mgr",link

```

**SOP**

1. Define severity levels and examples.
2. Write first-hour steps including revoke, rotate, and isolate.
3. Prepare comms templates and a contact list.
4. Run a blameless postmortem and track follow-up actions.

**Gates**

- **Entrance**: Threat model done.
- **Exit**: On-call reachable. Templates stored. Rehearsal completed.

**Relations**: Threat Model, Secrets, Ops/Runbook, Comms.

**Hobby vs Product**

- **Hobby minimum**: One page: who to call, how to rotate, where backups live.
- **Product grade**: Paging, on-call schedule, templated advisories, regulator timelines, drills.
