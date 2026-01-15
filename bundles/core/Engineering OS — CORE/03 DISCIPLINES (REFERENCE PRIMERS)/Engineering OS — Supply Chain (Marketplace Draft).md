# Supply Chain (Marketplace Draft)

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
