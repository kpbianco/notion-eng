# Compliance, Safety & Ethics (Marketplace Draft)

### What this page is

A practical, builder-friendly **compliance, safety, and ethics** layer for engineering projects.

It is designed to help you avoid building something:

- Illegal
- Unsafe
- Ethically irresponsible

…and to give you a realistic path from **hobby prototype** to **sellable product** without drowning in standards.

> This is **not legal advice**. When you are near regulated territory, you still use labs, compliance consultants, and attorneys. The goal here is to show up prepared.
> 

---

## 10‑Minute Quickstart (do this before you build more)

Create a Notion page called **Compliance Snapshot** and answer:

1. Where will it be used? (home / vehicle / industrial / medical-like / outdoors)
2. What energy hazards exist? (mains, Li‑ion, heaters, motors, high current)
3. Does it radiate or transmit? (switching regulators, clocks, USB, Wi‑Fi/BLE, cellular, CAN)
4. Does it touch people or critical systems? (wearable, medical-ish, automotive control, safety interlocks)
5. Does it collect data? (PII, location, audio/video, telemetry tied to identity)

Then apply this rule:

- If **mains** OR **radio transmitter** OR **Li‑ion pack** OR **safety‑critical use** → treat compliance as a **Rev A gating risk**, not “later.”

---

## 1) Regulatory Roadmaps

**Scope**: FCC / CE / UKCA / UL, IEC 60601, ISO 26262.

### 1.1 Market access vs product safety

Most regulation falls into one of these buckets:

- EMC / radio (does not interfere, uses spectrum legally)
- Electrical safety (shock, fire, overheating)
- Functional safety (fails safely when electronics/software malfunction)
- Environmental (restricted substances + end of life)
- Privacy/security (increasingly required by customers/regions)

### 1.2 USA: FCC (quick orientation)

If you sell electronics in the US, FCC rules often apply even if you are not “wireless,” because digital electronics can be unintentional radiators (noise emissions). Unintentional radiators generally follow an authorization route such as Supplier’s Declaration of Conformity (SDoC) or Certification, depending on the device category.

Practical triggers:

- No intentional radio (no Wi‑Fi/BLE/cellular) → likely unintentional radiator path.
- Intentional radio → typically certification is involved (and module approvals matter).

What you do in Rev A:

- Decide: unintentional vs intentional radiator.
- Plan: pre‑compliance EMC sniff test + test lab path if selling.

### 1.3 EU: CE marking (EMC/LVD/RED)

CE marking is the manufacturer’s declaration that the product conforms to applicable EU harmonization legislation.

Typical electronics touch:

- EMC Directive
- LVD (electrical safety for certain voltage ranges)
- RED (radio equipment: Wi‑Fi/BLE/cellular/etc.)

Key idea: you usually do not “get CE certified” by a single authority. You build a Technical File and perform conformity assessment, sometimes involving a notified body depending on product/risk.

Document retention: for radio equipment, EU guidance expects technical documentation + declaration kept for ~10 years after placing on the market.

### 1.4 UK: UKCA (and CE acceptance reality check)

UKCA is the UK conformity marking for Great Britain, with timelines and acceptance rules that can vary by product category.

Builder rule: treat UKCA as “CE-like but UK‑specific documentation + marking requirements.” Do not assume your EU plan automatically covers the UK.

### 1.5 UL (and similar marks)

UL is commonly required by retailers, insurers, and buyers even when not explicitly mandated as law.

Builder lens: UL-type certification becomes relevant when you are:

- Plugging into mains
- Shipping to consumers
- Selling into corporate/industrial procurement

### 1.6 Medical-ish: IEC 60601 family

If your product becomes a medical electrical device/system, IEC 60601-1 and related standards become central. Even “wellness” products can drift into regulated territory depending on claims and intended use.

Practical rule: marketing claims can trigger medical device classification. If you are close, treat it as a hard gate and consult experts early.

### 1.7 Automotive functional safety: ISO 26262

ISO 26262 addresses hazards caused by malfunctioning behavior of E/E safety-related systems in road vehicles.

Builder rule: if your product can influence vehicle control/safety outcomes (braking, steering, powertrain control, ADAS inputs), you are in a different universe than a telemetry logger.

### 1.8 Regulatory decision tree (copy into your project)

Q1 — Where will this be sold/used? US / EU / UK / other

Q2 — Is there intentional radio? (Wi‑Fi/BLE/cellular/etc.)

Q3 — Does it connect to mains? (AC input, internal PSU)

Q4 — Safety critical? (harm possible due to malfunction)

Q5 — Medical claims? (diagnosis/therapy/monitoring claims)

Q6 — Environmental obligations? (RoHS/WEEE/REACH expectations)

Q7 — Data/Privacy? (PII/location/audio/video, user accounts)

Output:

- Applicable regimes (FCC / CE directives / UKCA / UL targets / ISO 26262 / IEC 60601)
- Evidence pack requirements (tests + docs + markings)
- Stop-the-line risks

---

## 2) Safety Fundamentals

**Scope**: hazard analysis, labeling, fusing, isolation, fail-safe defaults, interlocks.

### 2.1 Safety hierarchy (use this order)

1. Design it out (remove hazard)
2. Guard it (physical/electrical protection)
3. Detect + shut down safely
4. Warn + instruct (labels/manual)

Warnings alone are the weakest control.

### 2.2 Hazard analysis (builder-friendly)

Create a **Hazard Register** (10–30 rows is enough for most projects).

For each hazard:

- Hazard (shock/fire/burn/cut/chemical/pressure/entanglement/data harm)
- Cause
- Severity (1–5)
- Likelihood (1–5)
- Detectability (1–5)
- Mitigation(s)
- Verification test

Common hazard categories:

- Electrical shock (mains, exposed conductors)
- Fire (overcurrent, shorts, overheating, battery thermal runaway)
- Thermal burns (heaters, hot components)
- Mechanical injury (sharp edges, pinch points, spinning parts)
- Battery/chemical (Li‑ion handling, venting, swelling, electrolyte)
- Data harm (privacy breach, location exposure, unsafe logs)
- Misuse hazards (wrong supply/cable/install)

### 2.3 Fusing, protection, safe power behavior

Minimum safe power checklist (sellable baseline):

- Input protection (fuse or resettable protection where appropriate)
- Overcurrent protection strategy (at least one layer)
- Reverse polarity protection (if user-accessible power)
- Thermal protection (shutdown/derate) if heat can rise dangerously
- Brownout behavior defined (what happens during droop)
- Fail-safe default on boot (outputs start safe)

### 2.4 Isolation, barriers, and “don’t mix domains”

If you have:

- Mains + low voltage logic
- High current motor drivers + sensors
- Automotive power + USB to a laptop

…define isolation and grounding boundaries explicitly.

Builder rule: write down what “safe separation” means in your system before routing wires or designing the enclosure.

### 2.5 Interlocks and fail-safe defaults

Interlocks are “this must be true before energy is enabled.”

Examples:

- Lid closed before motor runs
- Minimum airflow before heater enables
- Valid sensor signal before actuator moves
- Watchdog must be alive or outputs go safe

Fail-safe defaults:

- Outputs off on reset
- Actuators disabled until commanded
- Safe state documented and tested

### 2.6 Labeling and user instructions (lite but real)

If a reasonable user can misuse it, either:

- Design against misuse, or
- Label and guide clearly

Minimum:

- Electrical input rating label
- Polarity label (if applicable)
- Warnings for heat, sharp edges, batteries
- “Approved accessories/cables” statement (if relevant)

---

## 3) Environmental & Sustainability

**Scope**: RoHS/REACH/WEEE, materials disclosure, eco-design.

### 3.1 RoHS

RoHS restricts certain hazardous substances in electrical and electronic equipment.

Builder impact:

- Need supplier/material declarations for parts.
- Need a product compliance statement if selling into RoHS regions.

### 3.2 WEEE

WEEE governs collection/treatment/recovery of electronic waste in the EU.

Builder impact:

- May require producer registration and take-back obligations depending on role/country.
- At minimum: plan end-of-life handling and labeling.

### 3.3 REACH (SVHC)

REACH imposes obligations for substances of very high concern (SVHC) in articles.

Builder impact:

- Track SVHC declarations for plastics, cables, adhesives, housings.
- Store supplier compliance docs per part.

### 3.4 Eco-design heuristics

- Design for disassembly (standard fasteners, accessible screws)
- Avoid permanent adhesives when not necessary
- Reduce part count
- Use recyclable materials where possible
- Provide repair guidance + spare parts where viable
- Choose long-life components (avoid near-EOL parts)

---

## 4) Legal & IP Basics

**Scope**: patents vs trade secrets, copyright, open-source, export controls.

### 4.1 IP decision map

Patents:

- Good when: novel and defensible, and filings are affordable.
- Bad when: value is in execution/speed/community, or hard to enforce.

Trade secrets:

- Good when: you can keep it secret.
- Bad when: it ships in a product and can be reverse engineered.

Copyright:

- Protects expression (code, docs, artwork), not the idea.

Trademarks:

- Protect brand identifiers (names, logos).

Builder rule: decide IP posture in Rev A so you do not accidentally open-source what you meant to protect.

### 4.2 Open-source licenses

If you use third-party code:

- Track licenses (MIT/BSD/Apache/GPL/etc.)
- Keep attribution notices
- Understand copyleft triggers

Minimum practice:

- Maintain a Third-Party Notices file
- Store dependency list + versions
- Record license type per dependency

### 4.3 Export controls (EAR/ITAR)

Export controls can apply to hardware, software, technical data, and even “deemed exports.”

Builder guardrails:

- If your project relates to defense, advanced sensors, encryption, or controlled tech: assume export controls may apply.
- Do not share controlled technical data with foreign persons or store it in uncontrolled systems without understanding implications.
- Maintain an Export Control Log (classification assumptions, access, what was shared).

If you are near ITAR/EAR boundaries, get expert review.

---

## 5) Ethics & Responsible Use

**Scope**: data ethics, user safety, dual-use, disclosure policies.

### 5.1 Ethics is risk management for humans

Ethical failure modes:

- Harm due to foreseeable misuse
- Privacy violations
- Unsafe defaults
- Security negligence
- Dual-use enablement without safeguards
- Misleading claims

### 5.2 Data ethics (minimum viable)

If you collect data:

- Data minimization
- Purpose limitation
- Retention policy
- Access control
- User transparency

### 5.3 Dual-use thinking (quick test)

Ask:

- Could this be used to harm people or enable wrongdoing?
- Does the design lower the skill barrier for misuse?
- What safeguards can you add without ruining the product?

Safeguards can include:

- Rate limits
- Audit logs
- Safe defaults
- Friction for dangerous modes
- Clear acceptable use policy
- Removal of unnecessary dangerous features

### 5.4 Coordinated Vulnerability Disclosure (CVD)

If you ship hardware/software, people may report vulnerabilities.

Minimum CVD elements:

- How to report (email/web form)
- What info to include
- Expected response timeline
- Safe harbor statement (good-faith researchers)
- How you credit reporters (optional)
