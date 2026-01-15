# Example — CCA Rev A — Flow Log (Kian) · Steps 1–10

Got it — here’s the **first-person, fully applied “my work” flow log (Steps 1–10)** for the CAN CCA project. It’s Notion-ready (copy/paste as a single page).

---


> A complete, first-person record of what I decided and did. No placeholders.
> 

---

## 1) Vision & Success

**Why I’m building this**

I want a small, reliable box in my GR86 that shows the critical engine numbers (oil pressure, oil temp, coolant temp, AFR, RPM, gear) clearly while I’m driving and also logs them so I can analyze later. I’ve been winging it on parts in the past; this time I’m planning first so Rev A works and I stop re-spinning.

**Definition of “done”**

I drive a 20-minute session at pace. I glance and can read oil pressure instantly. When I get home, I open one CSV and see time-aligned data for the whole session with no corruption.

**Who benefits**

Me now; later this can be packaged for other owners or generalized for other vehicles.

**Constraints I accept up front**

- No cutting the OEM harness.
- Accessory/switched 12V only.
- Cabin heat and Arizona sun are real; display must be readable.
- Budget for Rev A hardware: ≤ $400 (excl. tools/track time).
- Time box: usable Rev A in ~8 weeks.

---

## 2) Scope Fence (Must-Haves vs Not-Now)

**Must-Haves (Rev A)**

- Live display: oil pressure, oil temp, coolant temp (large, legible digits).
- Logging at ≥10 Hz to a single CSV on microSD.
- Boot-to-first-reading ≤2 s from accessory power on.
- Non-intrusive car connection (OBD-II Y or equivalent) with no bus faults.
- Basic safety: inline fuse, surge protection, tidy harness, strain relief.

**Not-Now (Rev B/Later)**

- Cloud sync, phone app, skins/themes, auto-lap timing, map overlays.
- Fancy enclosure industrialization and injection-molded mounts.
- CAN-FD, secondary MCU, dual-screen layouts.

---

## 3) Context & Constraints (My Operating Envelope)

- **User & Use**: Solo driver; quick glances only at speed; no fiddling while moving.
- **Environment**: Cabin heat (up to ~60 °C), direct sun glare, vibration, power brownouts at crank.
- **Interfaces**: OBD-II for CAN + power (Y-cable) where practical; separate fused accessory tap if needed.
- **Physical**: Compact box; hidden wiring; mount that doesn’t block road view.
- **Budget & Time**: ≤ $400 Rev A BOM; Rev A demo by week 8.
- **Serviceability**: Tool-less SD removal, quick disconnects on harness, labeled connectors.

---

## 4) Requirements (Testable, Numbered)

**Functional**

- R-F1: Show oil pressure/temp and coolant temp live.
- R-F2: Log oil pressure/temp, coolant temp, AFR, RPM, gear to CSV.
- R-F3: Provide a simple page with just “big oil pressure” for at-a-glance checks.

**Performance**

- R-P1: Display refresh ≥10 Hz.
- R-P2: Logging rate ≥10 Hz, time-aligned.
- R-P3: Key-on to first valid reading ≤2.0 s.
- R-P4: 0 CAN errors injected; no MIL/check-engine light caused.
- R-P5: CSV opens in Excel/NumPy without repair and ≤1% dropped samples per 20-min session.

**Interfaces & Power**

- R-I1: Non-destructive vehicle connection (OBD-II Y or add-a-fuse accessory tap + CAN pigtail).
- R-I2: Survive automotive transients and cranking dips (TVS + proper buck).
- R-I3: CAN bitrate matches vehicle (initially 500 kbps) with clean common-mode wiring.

**Environment & Physical**

- R-E1: Sunlight readable at driver eye point (large digits, high contrast).
- R-E2: Operate 0–60 °C cabin; no rattles; all wires strain-relieved.
- R-E3: Install/remove without permanent mods in ≤30 min.

**Usability**

- R-U1: One button/gesture to toggle views; no menu maze.
- R-U2: SD card can be removed with fingers; CSV named with date/time.

---

## 5) Domain Buckets (Responsibilities + My Unknowns)

**Product/UI**

- **Deliver**: Two views (Big OP; Multi-metric). Fonts ≥12 mm cap height.
- **Unknowns I must answer**: Exact digit size readable from seat; best layout for glare.

**Electrical/Power/CAN**

- **Deliver**: 12V→5V buck (2 A), 5V→3.3V LDO, TVS, inline fuse, CAN transceiver, twisted-pair routing.
- **Unknowns**: Which TVS + buck combo keeps me safe on cranking/load-dump? Best CAN transceiver for 3.3 V logic?

**Compute/Comms**

- **Deliver**: MCU with BLE (future), SPI for display + microSD, external CAN controller.
- **Unknowns**: ESP32-S3 + MCP2515 throughput at 500 kbps with 10 Hz logging and full display updates?

**Display**

- **Deliver**: Sunlight-readable SPI TFT (2.4–2.8").
- **Unknowns**: ST7789 vs ILI9341 readability in sun; anti-glare film vs hood.

**Data/Logging**

- **Deliver**: Append-safe CSV, chunked writes, stable file naming.
- **Unknowns**: How often to flush to balance corruption risk vs wear? Do I need a small hold-up cap?

**Mechanical/Mount & Harness**

- **Deliver**: Discrete, rigid mount; labeled harness; service loops; Deutsch/Micro-Fit where sensible.
- **Unknowns**: Exact mount location that avoids glare and line-of-sight blockage.

**Test/Validation**

- **Deliver**: Bench CAN playback, power cut tests, street sanity, track session.
- **Unknowns**: How many random power cuts before I see first corruption with my write scheme?

---

## 6) Risk-Kill Experiments (I ran them fast)

**RK-1 · Sunlight readability**

- **Test**: ST7789 2.4" SPI vs ILI9341 2.8" SPI; show 3-digit “oil pressure” in 7-segment font; noon sun at driver eye point.
- **Result**: ST7789 (IPS) with bold font is readable; ILI9341 washed more at angles.
- **Decision**: **ST7789 SPI** + matte anti-glare film; digit height ≥14 mm.

**RK-2 · Power cut during logging**

- **Test**: ESP32-S3 + microSD (SPI) write 10 lines/s; randomly cut 12 V 30 times during active write.
- **Result**: 2 corruptions out of 30 with naïve writes. With 1 s ring-buffer + “commit index” every 2 s, 0 corruptions; last ≤2 s may truncate but file opens clean.
- **Decision**: **Chunked logging** + periodic index commit; accept ≤2 s tail loss.

**RK-3 · CAN throughput + display + logging concurrency**

- **Test**: MCP2515 + SN65HVD230 at 500 kbps; USB-CAN floods frames; display refresh 10 Hz; log 10 Hz.
- **Result**: Stable at target; SPI bus shared with chip-select discipline works.
- **Decision**: **MCP2515 + SN65HVD230** on shared SPI; hard CS sequencing.

**RK-4 · Non-intrusive vehicle connection**

- **Test**: OBD-II Y-cable: sniff bus; watch for DTCs/oddness.
- **Result**: No MIL; bus clean.
- **Decision**: **OBD-II Y** for Rev A. Keep accessory add-a-fuse as backup for cleaner power if noise appears.

---

## 7) Selections & Rationale (Locked for Rev A)

- **Compute**: ESP32-S3-WROOM-1 (BLE for future; plenty of RAM/flash).
    
    **Why**: Strong dev ecosystem; SPI speed adequate; I already use S3.
    
- **CAN**: MCP2515 (SPI) + SN65HVD230 transceiver.
    
    **Why**: Proven stack; easy breadboard; works at 500 kbps with S3.
    
- **Display**: 2.4" IPS ST7789 SPI + matte film.
    
    **Why**: Readable in sun; small pin count; fonts render crisp.
    
- **Storage**: microSD (SPI) with chunked logger + periodic index commit.
    
    **Why**: CSV compatibility; corruption window bounded; simple to parse.
    
- **Power**: TVS diode (automotive SMBJ-class), inline fuse (1 A), 12V→5V buck (≥2 A, low ripple), 5V→3.3V LDO for logic.
    
    **Why**: Protects from spikes/dips; clean 3.3 V for MCU/SPI.
    
- **Harness**: OBD-II Y for CAN + power (initial). Twisted pair for CAN, 20–22 AWG; power 18–20 AWG. Labels + strain relief.
    
    **Why**: Non-intrusive; serviceable.
    

---

## 8) Connections Freeze (Rev A)

**Block sketch (textual)**

- Vehicle OBD-II (12V ACC + CAN H/L) → **TVS → Fuse → Buck 12→5V → LDO 3.3V** → ESP32-S3
- Vehicle OBD-II CAN H/L → **SN65HVD230** ↔ **MCP2515 (SPI)** ↔ ESP32-S3
- ESP32-S3 (SPI) ↔ **ST7789 TFT** (CS separate)
- ESP32-S3 (SPI) ↔ **microSD** (CS separate)
- Momentary **BTN** → ESP32-S3 GPIO (view toggle)
- Optional analog in → future PX3 oil pressure input (Rev B or parallel test)

**Key pins I’m assigning now**

- SPI: SCK, MOSI shared; CS_TFT, CS_SD, CS_CAN distinct; MISO for SD + MCP2515.
- CAN INT from MCP2515 → dedicated GPIO with ISR.
- BTN → GPIO with pull-up; debounce in software.
- Backlight control (optional) → PWM GPIO.

**Power tree**

12V ACC → TVS → Fuse 1 A → Buck 5 V (2 A) → LDO 3.3 V (500 mA) → S3 + SPI devices.

Ground: single star point in enclosure; CAN transceiver ground tied close to connector; chassis ground bond via harness only.

**Task/data flow**

- **CAN Task** (interrupt-driven): reads frames → updates shared struct (atomic).
- **UI Task** (every 100 ms): copies snapshot → renders big digits.
- **Log Task** (every 100 ms): appends snapshot to ring → flushes chunk + index every 2 s.
- **WD/Sanity**: restarts UI if stale; flags bus-silent >500 ms.

> Any change to these interfaces = Rev B.
> 

---

## 9) Milestones (Proof-oriented)

- **M1 · Table Bring-Up**
    
    Power from bench 12V; show fake numbers changing at 10 Hz; take 10-sec video.
    
    *Proof*: Video of TFT updating smoothly.
    
- **M2 · CAN Loop-Through on Table**
    
    USB-CAN plays frames; I see each target signal parsed correctly at 10 Hz.
    
    *Proof*: Split-screen clip: sender + my display.
    
- **M3 · Logging Sanity + Power-Cut**
    
    Drive a 5-min loop; pull power randomly once; CSV still opens; ≤2 s data truncated max.
    
    *Proof*: CSV opened in Excel + brief note of truncation window.
    
- **M4 · In-Car Street Test**
    
    OBD-II Y connected; no DTCs; display readable from seat in sun.
    
    *Proof*: Driver-eye photo + OBD scan shows no new codes.
    
- **M5 · Track-Session Validation**
    
    20-minute session; one CSV; plot shows continuous, sensible traces.
    
    *Proof*: Single screenshot of overlaid traces; zero corruption.
    
- **M6 · Install Polish & Rev-B Notes**
    
    Tidy harness/mount; 1-page “what to change in Rev B.”
    
    *Proof*: Two photos + Rev-B bullets.
    

---

## 10) Procurement & Setup (What I actually bought / prepped)

**Compute & Comms**

- ESP32-S3-WROOM-1 dev board.
- MCP2515 SPI CAN controller breakout.
- SN65HVD230 (3.3 V) CAN transceiver breakout.

**Display & Storage**

- 2.4" IPS ST7789 SPI TFT + matte anti-glare film.
- microSD (SPI) breakout + 16–32 GB card (FAT32).

**Power & Protection**

- Inline blade fuse holder + 1 A fuses.
- Automotive TVS diode (SMBJ-class).
- 12→5 V buck module (≥2 A) with low ripple.
- 5 V→3.3 V LDO module (≥500 mA).
- Ferrules/bootlace, heat-shrink, braided sleeving.

**Vehicle Connection & Harness**

- OBD-II Y-cable.
- Twisted pair (22 AWG) for CAN.
- 18–20 AWG for power/ground.
- Adhesive labels; zip ties; mounts; strain-relief glands.
- Small project box + panel-mount button.

**Bench Setup**

- Labeled bins: **Power**, **CAN**, **Display**, **Storage**.
- Printed pin map taped to bench.
- “Build Log” page open; I log date, goal, results, issues every session.

**Rules I’m following during bring-up**

- Only buy what unlocks the **next** milestone.
- If the car acts weird: stop; note; back to bench.
- Any architecture/interface change after Step 8 starts **Rev B** on paper.

---

### Status (today)

- Vision, scope, context, and requirements are written and frozen for Rev A.
- Ran 3 risk-kills; all passed with clear decisions (display, logging scheme, CAN stack).
- Connections freeze is set; any change will be Rev B.
- M1/M2 parts are in; bench area labeled and ready.

---

If you want, I can continue this exact “my work” log with **Steps 11–20** (bench bring-up → street test → track validation → Rev-B notes) in the same first-person style.

---

Here’s the **first-person, fully applied “my work” flow log (Steps 11–20)** for the CAN CCA project, in the same style as before. It’s Notion-ready (copy/paste).

---

# CCA Rev A — Flow Log (Kian) · Steps 11–20

> Continuation of the concrete build. No placeholders, just what I actually did and decided.
> 

---

## 11) Bench Power Bring-Up (Safe First Power)

**Goal**

Power the stack safely on the bench and prove my power chain is clean and sized right.

**What I did**

- Set bench supply to **12.5 V**, current limit **0.5 A** to start.
- Wired **TVS → inline 1 A fuse → buck 12→5 V (2 A) → LDO 5→3.3 V**.
- Powered only the ESP32-S3 first (no display, no SD, no CAN).
- Checked 5 V and 3.3 V with a multimeter; touched the regulators after 5 min to check for heat (finger test).
- Added display, then SD, then CAN, **one at a time**; after each add, verified voltage stays in range and nothing gets hot.

**What I saw / learned**

- Idle draw (MCU only): ~70–90 mA at 12.5 V input.
- With display + SD + CAN attached and idle screen: ~180–220 mA.
- No notable heat on buck/LDO at idle; LDO warm but comfortable.

**Decisions**

- Power chain is acceptable for Rev A.
- Keep **1 A fuse** for bench; move to **2 A** for in-car once all loads are known.

**Artifacts saved**

- Photo of bench power setup with labels.
- Note: idle and “everything on” current readings.

**Next**

Wire SPI devices and bring up the display.

---

## 12) Display Bring-Up (Readable Digits at 10 Hz)

**Goal**

Show large oil-pressure digits that update smoothly at ≥10 Hz.

**What I did**

- Connected SPI (shared bus), gave the display its own **CS_TFT** line.
- Rendered a **single big number** (fake OP value) and updated it every 100 ms.
- Tried **two fonts** and sizes; measured digit height with a ruler at driver distance (simulated on the bench ~60 cm).

**What I saw / learned**

- **ST7789** looks crisp; **14 mm digit height** reads clean from ~arm’s length.
- 10 Hz redraw is visually smooth; no flicker.
- Matte anti-glare film reduces reflectivity; contrast remains high.

**Decisions**

- Lock **big-digit view**: 3-char oil pressure centered, with small status row (Hz, log state).
- Secondary “multi-metric” view will trade digit size for more fields.

**Artifacts saved**

- Short video of 10 Hz updates.
- Two screenshots of final fonts/sizes.

**Next**

Add the **CAN** side on the bench and replace fake numbers with parsed values.

---

## 13) CAN Loop-Through on the Bench (Parse Real Signals)

**Goal**

Prove I can parse the frames I care about (OP, OT, CT, AFR, RPM, gear) at the target rate.

**What I did**

- Hooked **USB-CAN** on my laptop to act like the car and replay test frames at **500 kbps**.
- Wired **MCP2515 + SN65HVD230**; gave MCP2515 its own **CS_CAN** and **INT** pin to the S3.
- Subscribed to the expected IDs; mapped fields to human-readable numbers (simple scaling).
- Display: **big OP** view + a tiny row for RPM/AFR to confirm parsing.

**What I saw / learned**

- With 10–15 frames/sec for my IDs, the system keeps up; no visible stutter.
- If I flood the bus, UI stays smooth due to “snapshot then render” approach.

**Decisions**

- **Keep the interrupt-driven CAN read** design.
- Maintain a **single shared struct** of “latest values” that UI/logging copy from.

**Artifacts saved**

- Screen recording: sender (laptop) + my display updating.
- Note with the ID list and field scaling used (for traceability).

**Next**

Bring up the **CSV logger** and test power-cut behavior.

---

## 14) Logging Engine (CSV + Power-Cut Tolerance)

**Goal**

Write clean CSV at ≥10 Hz and survive sudden power loss with only the last couple seconds at risk.

**What I did**

- Implemented **ring-buffer** that collects a snapshot every 100 ms.
- Every **2 s**: write a chunk and update an **index/commit marker**.
- Filenames as **CCA_YYYY-MM-DD_hh-mm-ss.csv**.
- Performed **30 random power cuts** while actively writing.

**What I saw / learned**

- CSVs open instantly in Excel and Python; columns line up.
- With chunked writes + commit marker, I saw **0 corrupt files**; worst case: the last ≤2 s missing.

**Decisions**

- **Lock chunked logging** with 2 s commit interval; document that tail loss is expected on sudden power-off.
- Add a tiny footer row `END_OK=1` when I exit cleanly (helps post-processing).

**Artifacts saved**

- Sample 60-second CSV with headers.
- Note on the power-cut test and results.

**Next**

Sanity-check that the system “keeps up” when everything runs together.

---

## 15) Concurrency Sanity (Everything at Once)

**Goal**

Ensure display updates, CAN parsing, and logging all run together at the target cadence.

**What I did**

- Ran the bench with **busy CAN traffic**, **10 Hz UI refresh**, and **10 Hz logging** simultaneously for **20 min**.
- Watched for missed UI updates, logger hiccups, or delayed button response (view toggle).

**What I saw / learned**

- Display stayed at 10 Hz; logs have ~600 rows per minute as expected.
- Button toggles view immediately; no lag.
- No freezes or watchdog resets.

**Decisions**

- No need to complicate with an RTOS. The simple task model works for Rev A.
- Proceed to the **in-car dry fit**.

**Artifacts saved**

- 20-minute CSV; note on observed behavior.
- Photo of bench running “full blast.”

**Next**

Move to the car: power/noise behavior and packaging.

---

## 16) In-Car Dry Fit & Power Noise Check

**Goal**

Verify non-intrusive power and bus connection, confirm no check-engine lights, and feel out cable routing.

**What I did**

- Plugged **OBD-II Y-cable**; connected my CAN and 12 V accessory.
- Placed the unit with a temporary mount; kept harnesses strain-relieved and away from pedals.
- Keyed accessory on/off several times; started the engine; toggled HVAC, lights, defroster to provoke electrical noise.

**What I saw / learned**

- No DTCs or weird behavior; car happy.
- My unit boots to first reading ~**1.6 s** (passes R-P3).
- No display flicker when big loads switch; power chain looks stable.

**Decisions**

- Keep OBD-II Y for Rev A.
- Add **label sleeves** at each connector; make SD slot finger-accessible from the seat.

**Artifacts saved**

- Photo of the temporary mount and cable routing.
- OBD-scan screenshot showing no new codes.

**Next**

Tune the UI for sunlight and finalize the “Big OP” layout in the real cabin.

---

## 17) Sunlight UI Tuning (Driver-Eye Proof)

**Goal**

Ensure the display is readable in harsh sun at the driver eye point.

**What I did**

- Midday test: parked in open sun; sat in driving position; took **driver-eye photos** of the display.
- Tried **white-on-black** vs **black-on-white**, and two background shades for glare.
- Applied **matte film**; tested with sunglasses.
- Adjusted digit height and spacing until it “reads at a glance.”

**What I saw / learned**

- **White digits on very dark gray** background work best.
- **14–16 mm** digit height is my sweet spot; any smaller slows recognition.
- Matte film helps a lot; sunglasses still fine.

**Decisions**

- Lock the **Big OP** view: giant 3-digit OP, small “OT/CT” under it, tiny status strip at bottom (log Hz, CAN OK).
- Keep the **multi-metric** page but treat it as secondary.

**Artifacts saved**

- Two driver-eye photos (with/without film).
- Final UI screenshots + chosen font/size notes.

**Next**

Do a **15–20 min street drive** to collect a real CSV and check stability.

---

## 18) Street Validation Drive (First Real Data)

**Goal**

Collect a clean CSV on public roads and confirm everything behaves like a product.

**What I did**

- Drove a **20-minute loop** with varied speeds and a few stop/starts.
- Watched the big OP page; tapped the button to switch to the multi-metric page a couple times.
- After parking, removed SD and opened the CSV on my laptop.

**What I saw / learned**

- Display stayed smooth; OP settled to believable values at idle/cruise.
- CSV has **~12,000 rows** (20 min × ~10 Hz); headers intact; timestamps monotonic.
- No corruption; last row has `END_OK=1` because I stopped logging before key-off.

**Requirements check (partial)**

- R-P1 (≥10 Hz UI): **PASS**
- R-P2 (≥10 Hz log): **PASS**
- R-P3 (≤2 s boot-to-first-reading): **PASS (~1.6 s)**
- R-P5 (openable CSV, ≤1% drop): **PASS**

**Decisions**

- Ready for track after enclosure/harness tidy-up.
- Add one **“oil pressure too low”** visual cue for later (Rev B or simple blink in Rev A).

**Artifacts saved**

- The 20-min CSV; quick plot (OP vs time).
- Short cockpit video during drive.

**Next**

Polish install: enclosure, mount, labels, spare fuses/SD — then track.

---

## 19) Track-Day Prep (Install Polish & Spares)

**Goal**

Make the install robust and serviceable for a bumpy day and quick turnarounds.

**What I did**

- Mounted the unit in a **small project box** with strain-relief gland for the harness.
- Secured harness with **adhesive mounts + zip ties**; added labels at each leg.
- Packed **spares**: 2× fuses, 2× SD cards, alcohol wipes (screen), a small screwdriver, tape, zip ties.
- Printed a **1-page quick guide** (boot behavior, button, how to pull SD safely).
- Confirmed I can **remove SD** without tools in <10 s.

**What I saw / learned**

- No rattle; cables have service loops.
- SD slot accessible with seatbelt on; good.

**Decisions**

- Install is “Rev A presentable.”
- Keep the quick guide in glove box.

**Artifacts saved**

- Photos of final mounting and labeled harness.
- PDF of quick guide.

**Next**

Run the **track session** and gather the definitive proof.

---

## 20) Track Session Validation (Rev A “Done/Not Done”)

**Goal**

Drive a full **20-minute** session at pace, then review a **single clean CSV** with continuous, believable data.

**What I did**

- Powered up in the paddock; verified live values before leaving grid.
- Ran one full session; didn’t touch the unit mid-session.
- After cool-down, powered off, removed SD, backed up CSV, and made a quick plot (OP vs RPM vs time).

**What I saw / learned**

- Display readable at speed; I used the **Big OP view** the entire time.
- CSV contained the entire session as **one file**; no corruption; `END_OK=1`.
- OP tracked with RPM as expected; temps rose and plateaued reasonably.

**Requirements check (final)**

- R-F1/F2/F3 (live display + logging + big-OP view): **PASS**
- R-P1/P2/P3 (UI/Log Hz, boot): **PASS**
- R-P4 (no CAN faults/MIL): **PASS** (post-session scan clean)
- R-P5 (CSV integrity, drops): **PASS**
- R-I1/I2/I3 (non-intrusive, transient-safe, correct bitrate): **PASS**
- R-E1/E2/E3 (readability, temp, install/remove): **PASS**
- R-U1/U2 (glanceable, easy SD export): **PASS**

**Decisions**

- **Rev A is complete.**
- Start **Rev B notes**: add visual OP low-threshold alert; consider small holdup cap to further narrow tail loss; evaluate brighter TFT option for midsummer glare.

**Artifacts saved**

- CSV of the full session.
- Two plots (OP vs RPM, OP/OT/CT over time).
- Two paddock photos (install and driver-eye).

**Next**

Write the **Owner’s Guide** and the **Rev B one-pager**. Archive Rev A package (requirements, freeze, milestone proofs, CSVs, photos) so I can hand it to future-me or anyone else.

---

If you want, I’ll continue with **Steps 21–30** (Owner’s Guide, verification report, Rev-B scoping, packaging for others, and turning this into the sellable Notion kit with linked artifacts).

---

Here’s the **first-person, fully applied “my work” flow log (Steps 21–30)** for the CAN CCA project, same format as before. It’s Notion-ready (copy/paste).

---

# CCA Rev A — Flow Log (Kian) · Steps 21–30

> Post-track wrap, proof, packaging, and turning Rev A into repeatable practice.
> 

---

## 21) Requirements Verification Report (PASS/FAIL Table)

**Goal**

Close the loop formally: every requirement gets a verdict with evidence.

**What I did**

- Copied my requirements list into a table with columns: **Req ID | Description | Method | Evidence | Result | Notes**.
- For performance items (Hz, boot time), I pasted **timing logs** and marked the CSV row ranges.
- For usability (readability), I attached **driver-eye photos** and documented test conditions (midday, sunglasses on).
- For bus integrity, I included **OBD scan** screenshots (pre/post session, “no new DTCs”).
- For logging integrity, I linked the **track CSV** and pointed to the `END_OK=1` footer.

**What I saw / learned**

- All Rev A requirements passed; a few I annotated with caveats (e.g., “CSV tail loss ≤2 s when key is cut”).

**Decisions**

- Leave caveats in place and push potential mitigations (holdup cap, chunk size tuning) to Rev B backlog.

**Artifacts saved**

- `Req_Verification_RevA.xlsx` with links to photos/CSVs/screenshots.
- PDF export for immutable record.

**Next**

Draft the **Owner’s Guide** so future-me (and others) can use this without me nearby.

---

## 22) Owner’s Guide (Install, Operate, Retrieve Data, Safety)

**Goal**

Create a one-pager (plus appendix) that a competent driver can follow without me.

**What I did**

- Wrote a **2-page guide**:
    1. **Install**: OBD-II Y cable hookup, fuse rating, device mount location, strain-relief diagram.
    2. **Operate**: Key-on behavior (first reading ~1.6 s), button to toggle views, meaning of status strip (“CAN OK”, “LOG 10 Hz”).
    3. **Retrieve Data**: Stop logging (hold button 2 s or key-off → expect ≤2 s tail loss), eject SD, file naming, CSV columns.
    4. **Safety/Gotchas**: Don’t obstruct airbags/vision; don’t route harness near pedals; no wet cleaning on the display; what blinking OP means (Rev A note).
- Added **appendix**: pinout card, fuse location, spare parts list, and a QR to a folder with sample plots.

**What I saw / learned**

- When I read it cold the next morning, I still knew exactly what to do—no missing steps.

**Decisions**

- Keep to **2 pages** + appendix; laminate one copy for glove box.

**Artifacts saved**

- `CCA_Owners_Guide_RevA.pdf` (+ .md source).
- Laminated print for glove box.

**Next**

Define **maintenance/inspection** so this doesn’t silently degrade.

---

## 23) Serviceability & Maintenance Plan

**Goal**

Prevent slow creep failures; document inspections and consumables.

**What I did**

- Created a **maintenance checklist** with intervals:
    - **Before each event**: harness visual check, connector click test, SD free space check, screen wipe with microfiber.
    - **Quarterly**: open enclosure, dust out; verify gland compression; re-seat SD; confirm logs write and `END_OK=1`.
    - **Annually**: replace inline fuse; replace SD card (cheap insurance); inspect buck/LDO for discoloration.
- Stocked a **spares kit**: 2× fuses, 2× SD cards (pre-formatted), zip ties, alcohol wipes, small screwdriver.
- Logged **service actions** as dated entries in Notion (“what changed, why”).

**What I saw / learned**

- SD lifetime and weirdness cause most field issues; proactive replace is worth it.

**Decisions**

- Treat SD as a consumable: **replace yearly** or **every 100 hours** of logging.

**Artifacts saved**

- `CCA_Maintenance_Checklist.md` and printed copy in the spares pouch.
- Notion “Maintenance Log” database with templates.

**Next**

Capture **lessons learned** (what surprised me vs. what I expected).

---

## 24) Risk Retrospective & Lessons Learned

**Goal**

Compare planning risks vs. real ones; update my mental model.

**What I did**

- Pulled my **Risk Kill Log** from early phases; added a column **“Outcome in Field.”**
- New realities:
    - **Power-cut** strategy worked; tail ≤2 s is acceptable—but I want a future **holdup cap** and **file finalization**.
    - **Glare** manageable with matte film; **digit size** was the bigger deal.
    - **Bus flood** never happened in real car; bench worst-case was still valuable.
- Documented **three surprises**:
    1. Boot-to-first reading was faster than expected after trimming init.
    2. Users naturally stare at **one giant number** (OP) under stress—good validation of UI choice.
    3. Strain-relief was more important than enclosure waterproofing for Rev A.

**Decisions**

- Promote **holdup + finalization** to Rev B priority 1.
- Keep **Big-OP** page as default; multi-metric stays secondary.

**Artifacts saved**

- `Lessons_Learned_RevA.md` linked back to risk log items.
- Slide with “3 Surprises / 3 Confirmations.”

**Next**

Turn observations into a **Rev B backlog** with priorities and acceptance tests.

---

## 25) Rev B Backlog & Prioritization

**Goal**

Convert wants into a ranked list with clear acceptance criteria.

**What I did**

- Built a **backlog table** with columns: **Item | Why | Acceptance Criteria | Effort | Risk | Priority**.
- Top Rev B items:
    1. **OP Low Alert** (visual + optional buzzer). *AC*: triggers reliably at threshold, no false positives at idle blips.
    2. **Holdup Power** (≥500 ms) + **atomic file finalize**. *AC*: 50 random key-offs → 0 missing-footer files.
    3. **Brighter TFT** evaluation for desert summer; same SPI footprint. *AC*: legible at noon sun, sunglasses on.
    4. **EMI sanity** (radiated): AM radio near harness; log any display noise correlation. *AC*: no sustained artifacts.
    5. **Cable/connector** upgrade path (locking connectors). *AC*: survive 10 intentional tugs without fault.
- Prioritized by **safety > data integrity > UX > niceties**.

**What I saw / learned**

- Two items (OP alert, holdup) deliver most of the real value for Rev B.

**Decisions**

- Freeze Rev B scope to top 3 for now; carry others as “nice-to-have.”

**Artifacts saved**

- `RevB_Backlog.xlsx` with scoring (MoSCoW + numeric).

**Next**

Quantify **time & money** spent to assess ROI and plan next round.

---

## 26) Cost/Time Postmortem & ROI

**Goal**

Know what Rev A actually cost and where I burned time.

**What I did**

- Summed parts, tools, expendables (rough but honest).
- Pulled **Build Log** hours and binned by phase (planning vs. bench vs. car vs. docs).
- Calculated **% planning time** vs. implementation.

**What I saw / learned**

- Total out-of-pocket (Rev A): **$XXX** (boards, display, cables, enclosure, spares).
- Total time: **~YY hours**; planning + risk kills were **~35–40%**, which felt right—front-loaded thinking saved me a re-spin.
- Biggest time sink: **UI readability experiments** (worth it).

**Decisions**

- Keep planning time ≥30% for similar projects; it paid off.
- Next time, decide UI font/size faster by pre-baking **A/B printouts** before hardware.

**Artifacts saved**

- `CCA_RevA_Cost_Time_Postmortem.xlsx` with charts.
- One-pager ROI summary.

**Next**

Codify a **QA/Compliance-lite checklist** to stop avoidable regressions.

---

## 27) QA/Compliance-Lite Checklist (Practical, Safety-Oriented)

**Goal**

A lightweight, repeatable gate that makes the build safe and respectable.

**What I did**

- Wrote a **15-item checklist** (each item observable):
    - Harness strain-relief ✓
    - Fuse rating matches BOM ✓
    - No cable near pedals/steering ✓
    - Display does not block sightlines ✓
    - SD ejectable without tools ✓
    - Pin map matches wiring ✓
    - CAN bitrate set correctly ✓
    - Power-on brownout test pass ✓
    - Key-off logging behavior documented ✓
    - No new DTCs post-drive ✓
    - Driver-eye readability at noon ✓
    - Labeling present on each leg ✓
    - Spare fuses/cards present ✓
    - Owner’s Guide in glove box ✓
    - Maintenance log created ✓
- Marked **photos** or **file links** for each item as proof.

**What I saw / learned**

- Having photos for each item makes audits trivial later.

**Decisions**

- Attach this checklist to every future revision’s “go live” gate.

**Artifacts saved**

- `QA_Lite_Checklist_RevA.pdf` and Notion checklist template.

**Next**

Bundle **everything** into a clean handoff package anyone can browse.

---

## 28) Rev A Handoff Package (Clean Bundle)

**Goal**

Single folder a teammate (or future-me) can open and understand in 5 minutes.

**What I did**

- Created a folder structure:
    
    ```
    00_Readme/
    01_Requirements/
    02_Interface_Freeze/
    03_BOM_&_Wiring/
    04_Code_&_Configs/
    05_Test_&_Logs/
    06_Validation/
    07_Owners_Guide/
    08_QA_Checks/
    09_Lessons_RevB/
    
    ```
    
- Dropped a **top-level README.md**: purpose, how to navigate, quickstart.
- Normalized file names and added **timestamps**.
- Included **LICENSE.txt** (personal/non-commercial share) and **version.txt** (“Rev A, build date, commit hash”).

**What I saw / learned**

- With the README and consistent names, I can jump to any artifact in seconds.

**Decisions**

- This structure becomes my default for future projects.

**Artifacts saved**

- Zipped `CCA_RevA_Handoff_Package.zip` (kept local + cloud).

**Next**

Run a small **user acceptance** loop with a trusted friend.

---

## 29) Sharing, Onboarding & Feedback Loop

**Goal**

Prove a fresh set of eyes can install, operate, and retrieve data using only the docs.

**What I did**

- Gave a friend the **Handoff Package** + the **Owner’s Guide**; watched silently as they installed in my car.
- Timed how long it took to: power up, confirm live OP, toggle views, run a 5-minute log, retrieve CSV.
- Captured feedback in a **UAT log** (“what was confusing, what felt great”).

**What I saw / learned**

- They succeeded without me stepping in.
- Two doc tweaks: clarify **button hold** vs. **short press**; add a picture of the **status strip** with labels.

**Decisions**

- Updated Owner’s Guide images; added a “buttons cheatsheet” in the appendix.

**Artifacts saved**

- `UAT_Session_Notes.md`, timings, and two annotated screenshots.
- Owner’s Guide v1.1 with clarified button behavior.

**Next**

Extract the generic **Notion templates** and link back to the concrete Rev A artifacts.

---

## 30) Template Extraction (Sell-Grade Notion Kit)

**Goal**

Turn my concrete Rev A artifacts into reusable, general templates anyone can follow.

**What I did**

- For each artifact, built a **blank template** with locked sections, hints, and examples hidden behind toggles:
    - **Vision & Success** page with examples under collapses.
    - **Requirements DB** with PASS/FAIL linking model.
    - **Interface Freeze Pack** (Block Diagram placeholder, Pin Map table, Power Tree sketch block, Task Model outline).
    - **Milestone Plan** with sample acceptance criteria.
    - **Risk Kill Log** template with “design-killer” tagging.
    - **QA-Lite Checklist** with photo-evidence slots.
    - **Owner’s Guide** template with “where to add images” callouts.
    - **Handoff Package README** boilerplate.
- Added **cross-links** (e.g., each requirement has a “Proof” relation to test logs).
- Wrote a **“Start Here”** page that explains the flow in the order I actually used (not corporate-speak).
- Included a **“Scale Up/Scale Down”** toggle: how to shrink the process for tiny projects or expand for team projects.

**What I saw / learned**

- With all templates wired together, the process reads like a guided tour—no blank-page anxiety.

**Decisions**

- This becomes my **standard OS** for personal engineering projects; Rev B of the CCA will be built entirely inside these templates.

**Artifacts saved**

- Notion export of the **Engineering Project OS (Solo) — v1.0**.
- Screenshot of the “Start Here” page with the 8-phase flow and checkboxes.

**Next**

(If desired) publish a sanitized demo package + screenshots to share the approach without exposing private logs.

---

If you want, I’ll continue with **Steps 31–40** (publishing, support SOP, field issue capture, change control for Rev B, and “teaching version” with tutorials).

Here’s the **first-person, fully applied “my work” flow log (Steps 31–40)** for the CAN CCA project, same format as before. It’s Notion-ready (copy/paste).

---

# CCA Rev A — Flow Log (Kian) · Steps 31–40

> Publish it, support it, learn from the field, control changes, and make it teachable and durable.
> 

---

## 31) Publish & Share (Demo + Sanitized Package)

**Goal**

Show the project crisply without exposing private data; make it easy for someone to “get it” in 2–5 minutes.

**What I did**

- Cut a **90-second demo video**: power-on → OP big number screen → status strip → brief drive clip → CSV open on laptop with a quick plot.
- Created a **sanitized demo pack** (no plate numbers, no personal GPS):
    - 1 short CSV with benign sample values
    - 3 screenshots (device UI, wiring overview, sample plot)
    - a one-pager “What this is / Why it matters / How it works”.
- Exported a **read-only PDF** of the Owner’s Guide with personal info removed.
- Wrote the **README_lite.md** for the demo folder: what’s inside, how to view it, how to contact me.

**What I saw / learned**

- People understand it fastest when they see **OP changing in real time** and a **before/after** (no data vs. clean chart).

**Decisions**

- Keep a public **/demo** folder separate from the full Handoff Package.

**Artifacts saved**

- `demo/CCA_90s_Demo.mp4`, `demo/sample_log.csv`, `demo/README_lite.md`, `demo/guide_excerpt.pdf`.

**Next**

Stand up a minimal **support/ops** routine so issues don’t get lost.

---

## 32) Support & Ops SOP (Triage → Fix → Learn)

**Goal**

Have a tiny, repeatable process for questions and issues so I don’t firefight ad-hoc.

**What I did**

- Made a **Support Inbox** (single email/Notion form) that drops entries into a **Support DB** with: Type, Severity (S0–S3), Status, Owner, Links to evidence.
- Defined **Severity levels** with examples:
    - **S0**: Safety risk (e.g., harness interferes with pedals)
    - **S1**: Major function broken (no display, no logs)
    - **S2**: Degraded (logs work but status strip wrong)
    - **S3**: Cosmetic/docs tweak
- Wrote **SOP**:
    - Acknowledge within **24 h**; triage; request evidence (photo, CSV, brief description).
    - For S0/S1, reproduce on bench same day if possible; otherwise schedule a test.
    - After fix, **log root cause** + **preventive** in “Lessons” and consider CCR (Step 34).
- Added **3 canned replies** with checklists (No Display, No Log Files, Weird Values).

**What I saw / learned**

- Most issues are solved by “check the SD is FAT32 and seated” and “confirm the Y-cable click”.

**Decisions**

- Even for solo projects, treat support as a **mini-kanban** to avoid forgotten DM threads.

**Artifacts saved**

- `SOP_Support_RevA.md`, Notion Support DB template, canned replies.

**Next**

Formalize a clean **field issue intake** so the evidence is usable.

---

## 33) Field Issue Intake & Feedback System

**Goal**

Capture issues with enough context to reproduce them, plus insights for product improvement.

**What I did**

- Built a **Field Report Form** (public link) that posts to a DB with required fields:
    - Vehicle basics, ambient temp, **exact conditions** (idle, cruise, WOT), steps to reproduce
    - Attach **photo/video**, **last CSV**, and **event timestamp**
    - Checkbox for **safety concern**
- Added **auto-acknowledge** with a ticket number (Support DB ID).
- Created **tags** to cluster feedback (Readability, Wiring, Logging, Power, UI, Docs).
- Set weekly **review ritual**: newest → oldest, pick 1 improvement to move into backlog (Step 35/39).

**What I saw / learned**

- Short smartphone clips of key-on + first 5 seconds are pure gold for debugging.

**Decisions**

- Make attaching the **latest CSV** mandatory unless the problem is physical/mechanical.

**Artifacts saved**

- `Field_Report_Form` link, `Field_Issues_DB` with views by tag and severity.

**Next**

When changes are needed, do it under **change control** (not vibe-based tinkering).

---

## 34) Change Control & Versioning (Rev B and beyond)

**Goal**

Stop “mystery builds.” Every change is deliberate, reviewable, and traceable.

**What I did**

- Adopted a **versioning scheme**:
    - **Hardware**: Rev A, Rev B, etc.
    - **Firmware**: `MAJOR.MINOR.PATCH` (e.g., 1.2.0); PATCH = bugfix only; MINOR = new feature compatible; MAJOR = breaking.
- Created a **CCR (Change Control Request)** template: Problem → Options considered → Decision → Impact (reqs, tests, docs) → Rollback.
- Defined **ECO** (engineering change order) to implement an approved CCR with checkboxes: BOM update, Pin Map, Power Tree, Owner’s Guide, QA checklist update.
- Made a **Release Checklist**: build tag, changelog, regression tests run, docs updated, demo assets refreshed.

**What I saw / learned**

- Having a CCR forces me to write down **options considered**, which prevents tunnel vision.

**Decisions**

- No shipping firmware change without **changelog + Owner’s Guide delta** noted.

**Artifacts saved**

- `CCR_Template.md`, `ECO_Checklist.md`, `Release_Checklist.md`, `Changelog.md`.

**Next**

Package a **teaching track** so others can replicate the process quickly.

---

## 35) Teaching & Training Version (Tutorials + Labs)

**Goal**

Turn my process into a guided course: install, operate, interpret, and improve.

**What I did**

- Wrote **3 short tutorials** (with screenshots):
    1. **Install in 10 minutes** (Y-cable, mount, power, first boot).
    2. **Log & Retrieve** (run a 5-minute session, transfer CSV, open in spreadsheet).
    3. **Plot & Decide** (make a 2-axis chart, annotate “normal vs. concern”).
- Created **two “labs”**:
    - **Lab A**: Simulate a low OP event using bench frames, verify alert threshold behavior (for Rev B).
    - **Lab B**: A/B test two display fonts in sun, record readability rating.
- Added **quizzes** (3–5 questions each) to force comprehension without jargon.

**What I saw / learned**

- The “plot & decide” tutorial nudges people to **act** on data, not just collect it.

**Decisions**

- Keep tutorials **under 5 minutes** each; everything else goes to appendices.

**Artifacts saved**

- `Tutorials/01_install.md`, `02_logging.md`, `03_plots.md`, `Labs/LabA.md`, `Labs/LabB.md`.

**Next**

Write a **case study** so someone skimming can still grasp the value.

---

## 36) Portfolio Case Study (Problem → Solution → Proof → Impact)

**Goal**

Condense the story for hiring managers, sponsors, or collaborators.

**What I did**

- Built a **one-page case study**:
    - **Problem**: No trustworthy real-time OP and logs at track pace.
    - **Solution**: Compact CAN display/logger with “Big-OP” UX, 10 Hz logs, ≤2 s boot.
    - **Process**: 8-phase flow, risk kills (CAN+display concurrency, SD integrity), interface freeze.
    - **Proof**: Track CSV + plot + requirement PASS table (links).
    - **Impact**: Safety awareness improved; setup iterations based on real data; captured Rev B path.
- Embedded **three images**: product in situ, UI in sun, annotated plot.

**What I saw / learned**

- The PASS table screenshot builds immediate credibility.

**Decisions**

- Keep a public copy **without** car ID details.

**Artifacts saved**

- `Case_Study_1Pager.pdf` (+ .md), three compressed images.

**Next**

Clarify **IP/licensing** and basic compliance (so sharing is safe).

---

## 37) IP, Licensing & Compliance Notes

**Goal**

Be explicit about what’s mine, what’s reused, and how others can (or can’t) use it.

**What I did**

- Declared **code license**: MIT (simple, permissive, include copyright).
- Declared **hardware docs license**: CERN OHL-P (documentation permissive) for schematics/placement drawings.
- Stated **disclaimers**: hobby/track use, not a safety-critical automotive system; user responsible for installation choices.
- Collected **third-party attributions** (fonts, libraries) in `ATTRIBUTIONS.md`.
- Wrote a **“Trademark/Brand”** note for my marks/logos (no reuse without permission).

**What I saw / learned**

- Having an ATTRIBUTIONS file avoids last-minute hunts when publishing.

**Decisions**

- Keep personal logs private; demo logs only in the share pack.

**Artifacts saved**

- `LICENSE_CODE`, `LICENSE_HW_DOCS`, `ATTRIBUTIONS.md`, `DISCLAIMER.txt`.

**Next**

Plan for **sustainment/obsolescence** so Rev B doesn’t get stuck by parts.

---

## 38) Sustainment & Obsolescence Plan

**Goal**

Avoid being surprised by parts going EOL or supply hiccups.

**What I did**

- Added **BOM lifecycle columns**: Manufacturer status, Last Time Buy rumor, Second Source, Drop-in Alternative.
- Saved **alternates** for display, SD, connectors, and buck: same footprints/ratings where possible.
- Set **quarterly check**: scan key parts for status changes; update alternates list.
- Pre-bought **two years of consumables**: fuses, SD cards, cable glands.

**What I saw / learned**

- Displays and SD cards churn most; keeping a pin-compatible display option saves a lot of grief.

**Decisions**

- In Rev B, favor parts with **≥3 reputable vendors** and long lifecycles.

**Artifacts saved**

- `BOM_RevA.xlsx` (lifecycle columns), `Alternates.md`, `Sustainment_Policy.md`.

**Next**

Instrument **metrics** that tell me if quality and usefulness are trending up.

---

## 39) Metrics & Continuous Improvement

**Goal**

Have objective signals that the product/process is getting better.

**What I did**

- Defined **leading metrics**:
    - % sessions with **`END_OK=1`** (data integrity)
    - **Boot-to-first-reading** median and 95th percentile
    - **Readability score** (1–5) from quick post-drive note
    - **Support rate** (tickets per 10 sessions)
- Created a **monthly dashboard** (Notion/Sheets) that pulls from Support DB and my logs summary.
- Scheduled a **monthly mini-retro**: 30 min to pick **one** Rev B backlog item to advance.

**What I saw / learned**

- A single integrity metric (`END_OK`) is the best early warning.

**Decisions**

- Don’t vanity-graph everything; pick 3–5 metrics that influence action.

**Artifacts saved**

- `Metrics_Dashboard.xlsx`, `Monthly_Retro_Agenda.md`.

**Next**

Prepare for the bad day: loss, failure, or data corruption.

---

## 40) Disaster Recovery & Reproducibility

**Goal**

If hardware dies or files vanish, I can restore quickly and build again exactly.

**What I did**

- Kept **offsite backups** of: Handoff Package, BOM, schematics, firmware repo, Owner’s Guide, demo pack.
- Created a **“fresh SD” image** with correct folders, a readme, and a known-good config; stored the image and a how-to write it.
- Pinned firmware toolchain versions in `toolchain.lock` with a simple **rebuild script** (`build.sh`); tested rebuild on a clean machine.
- Wrote a **Recovery Playbook**:
    1. Replace fuse/SD (quick test)
    2. Swap enclosure with spare (if needed)
    3. Flash known-good firmware tag
    4. Run the **bench smoke test** (CAN sim + display + logging 60 s)
    5. Road sanity check (idle → cruise)

**What I saw / learned**

- The **fresh SD** image eliminates half of the “it won’t log” situations after a card swap.

**Decisions**

- Store **one zip** with everything needed to rebuild Rev A; keep a printed “Recovery Quick Card” in the spares pouch.

**Artifacts saved**

- `CCA_RevA_Restore.zip` (repo tag, docs, SD image, build script), `Recovery_Playbook.md`, laminated Quick Card.

**Next**

Rev B planning can now proceed with confidence (alerts + holdup + brighter TFT), powered by the same OS and templates.

---

If you want, I can bundle **31–40** into a clean Notion page structure (headers, toggles, checklists) that drops right into your OS.

---

## B) DfX Pack (DFM/DFA/DFT/DFR/DFCost/DFService)

**What I’m optimizing**

I’m designing Rev A so it’s easy to manufacture, assemble, test, survive heat/vibration, cost what I expect, and be serviceable between sessions.

**Key decisions (Rev A)**

- **DFM/DFA**: 2-layer PCB, 1.6 mm FR-4, common footprints (0603 passives, SOT-223/SOT-23 regulators), single board + standoffs. All connectors on one edge, right-angle where possible.
- **DFT**: Add test pads for 3V3, 5V, GND, CANH/L probe points, SPI-MOSI/MISO/SCLK/CS, and a UART header. Boot mode accessible without disassembly.
- **DFR**: TVS + input fuse on 12 V, buck → 5 V → LDO 3.3 V; electrolytic + ceramic bulk on input; display sun-readability checked; wiring strain-relief.
- **DFCost**: Keep BOM ≤ $400 Rev A. Prefer commonly stocked parts with alternates.
- **DFService**: SD card and fuse accessible without removing the enclosure. Connectors keyed; harness labeled both ends.

**Constraints I’m designing to**

- Cabin temps up to ~60 °C in AZ sun, road vibration, no cutting OEM harness, quick swap at the track.

**Evidence I will produce**

- Assembly drawing with callouts, test-point map, torque/strain notes, and a 10-min “bench test script” anyone can run.

**Rev B notes**

- Consider 4-layer for better EMC/thermals if needed; consolidate connectors into a small panel; add pogo-pin bed-of-nails if volumes increase.

---

## C) Supply Chain & Lifecycle (AVL + alternates)

**My policy**

For every critical part I keep a primary **manufacturer PN** and at least one **second source/alternate**. I track lifecycle (Active/NRND/EOL), lead time, and RoHS. If a part flips to NRND/EOL, I switch to the alternate at the next ECO.

**Critical parts (Rev A AVL extract)**

```
Item,Function,ManufacturerPN,VendorSKU,Status,Alt1,Alt2,Notes
MCU,Controller,ESP32-S3-WROOM-1-N8R2,Digi-Key1965-ESP32S3WROOM1N8R2CT-ND,Active,ESP32-WROOM-32E,RP2040+MCP2515,"Keep SPI free for display & SD; BLE optional"
CANXCVR,Businterface,MCP2562FD-E/SN,Digi-KeyMCP2562FD-E/SN-ND,Active,SN65HVD230,TCAN337,"Classic CAN 500 kbps; verify standby pin logic"
Buck,12V→5V,LM2596S-5.0/NOPB,Digi-KeyLM2596S-5.0/NOPB-ND,Active,MP1584EN,LMR33630,"Use input TVS + fuse; validate ripple @ 1A"
LDO,5V→3.3V,TLV1117-33CDCYR,Digi-Key296-14506-1-ND,Active,AP2112K-3.3,AZ1117-3.3,"Derate for 60°C cabin"
TVS,12Vsurge,SMAJ58A,Digi-KeySMAJ58A-TPMSCT-ND,Active,SMBJ58A,SMBJ36A,"Place at input before buck"
Display,SPITFT2.4in,ILI9341-basedgeneric,Adafruit1480orsimilar,Active,ST7789SPITFT,NextionUART,"Pick one library; sun test results attached"
Storage,MicroSD(HE),SanDiskHighEndurance32GB,AmazonB0829,Active,KingstonEndurance,TranscendEndurance,"Cycle testing; FAT handling"
Conn(car),OBD-IIpass-through,Molex/aftermarket,Amazon/OBDSolutions,Active,ASconnectorharness,DeutschDT,"No OEM cuts; ensure strain relief"
Conn(board),PowerI/O,Micro-Fit3.043025-0400,Digi-KeyWM3703-ND,Active,Mini-FitJr,XT30,"Keyed; vibration-safe"

```

**Procurement play**

- Buy two of each critical module for A/B testing.
- Store datasheets + invoices with the BOM.
- On receipt, perform **incoming QA**: visual, part number match, quick electrical sanity (no-load current, buck output, etc.). Log results.

**Rev B notes**

- If display supply gets shaky, lock an equivalent by controller (ILI9341/ST7789) and confirm pinout compatibility.
- Add a “sudden-short spare kit” (buck, TVS, LDO, fuses, connectors).

---

## D) Security & Privacy Mini-Spec (threat model, SBOM, data handling)

**What I’m protecting**

- **Assets**: Firmware image, configuration, logs (laps, temps, pressures), car bus integrity.
- **Adversaries**: Curious friend at the paddock, opportunistic local attacker, me (operator error).
- **Surfaces**: SD card, UART console, BLE (if enabled), connectors.

**Decisions (Rev A)**

- **Data scope**: No PII; logs are technical telemetry only.
- **Default posture**: BLE **off** by default; UART requires physical access.
- **Firmware**: Versioned build artifacts; SHA256 recorded in release notes; reproducible build notes in repo.
- **SBOM**: Keep a simple SBOM of libraries (display driver, FAT FS, CAN stack) with licenses (MIT/BSD/etc.) in the repo.
- **Data handling**: CSV with headers & units; user can delete SD contents; no hidden retention.
- **Integrity**: Append-only logging with periodic flush; a journal/index to survive power loss.

**Proof I’ll keep**

- SBOM.md committed with license tags, release hash, and build command.
- Screenshot of menu/config showing BLE disabled.
- Log format spec (fields/units) and sample CSV.

**Rev B notes**

- Consider firmware signing and a PIN-guarded BLE UI if we ever enable wireless controls.
- Add a tamper-evident sticker on the enclosure if shipping.

---

## F) Test Strategy & Evidence Pack (levels, criteria, coverage)

**Levels I’m running**

- **Unit**: Parsing, scaling, min/max clamp, CSV row writer, ring buffer.
- **Integration**: CAN-in → parse → display; CAN-in → log; display + log concurrency.
- **System (bench)**: Full chain on bench with fake CAN; power cycling during logging.
- **Vehicle**: Accessory-on timing, no DTCs, driving at city speeds, then track session.
- **Environmental**: Cabin heat soak, sunlight readability, vibration (hand/road), endurance (60-min continuous log).
- **Fault-injection**: Pull SD mid-write, kill power at random intervals, pull CAN, short display CS (briefly).

**Acceptance criteria (examples)**

- **A-P1** Display ≥10 Hz updates; **A-P2** Logging ≥10 Hz sustained 60 min; **A-P3** Boot-to-first-value ≤2 s; **A-P4** No CAN faults/DTCs; **A-E1** CSV survives 10 power pulls with ≤1 partial row; **A-H1** Readable under noon sun.

**Coverage map (excerpt)**

```
Requirement,Test ID,Method,Pass Bar,Evidence
R-P1 (10 Hz display),T-011,Timedloop @ bench,≥10 Hzfor10 min,video_011.mp4 + timestamps
R-P2 (10 Hz logging),T-021,Row count vstime,≥600rows/60 sfor10 cycles,log_021.csv + check_021.py
R-P3 (≤2 sto firstvalue),T-031,Power-on timer,≤2.0 s median,boot_031_scope.png
R-I1 (no OEM cuts),T-041,Install inspection,Pass (photo proof),install_041.jpg
R-U1 (glanceable),T-051,Readabilitytable,<1 s recognition @70 mph sim,read_test_051.pdf
R-E* (heat),T-061,Cabin soak @60°C,No crash;tempwithin spec,temp_061_log.csv

```

**Evidence discipline**

Every test gets a folder `tests/T-xxx/` with a 1-page procedure, raw artifact (CSV/scope), and a PASS/FAIL. I’ll tag a “RevA-Ready” when all A-level items pass.

**Rev B notes**

- Automate unit tests in CI; add scripted CAN replays; add simple display screenshot diffing.

---

## G) Reliability & Safety (FMEA, fault injection, derating)

**Ground rules**

“Safe” = The box never perturbs CAN, never draws more than fused limits, never blocks driver vision, and survives losing power or SD without bricking itself.

**FMEA (top items excerpt)**

```
Function,FailureMode,Effect,Severity,Occur,Detect,RPN,Mitigation,Owner
12Vinput,Surgespikekillsbuck,Devicedies;couldshort,S=8,O=3,D=4,96,TVS+fuse+layout;validatesurge,Me
Logging,Powercutmid-write,Corruptfile;dataloss,S=6,O=5,D=5,150,Chunkedwrites+index;endurancetest,Me
CANinterface,Transceiverlatch-up,Buserrors,CEL,S=9,O=2,D=4,72,ChooserobustXCVR;ESD;isolationclearances,Me
Display,Unreadableinsun,Drivercan’tglance,S=7,O=4,D=3,84,Suntest;largefont/highcontrast,Me
Thermal,LDOoverheats,Thermalshutdown,S=6,O=3,D=4,72,Derate;heatsinking;swaptobuckifneeded,Me

```

**Fault-injection I will run**

- Kill power at random during logging (10×) → Expect intact CSV with at most final partial row.
- Pull SD during logging → Expect log gracefully pauses and resumes.
- Short display CS for 100 ms → Expect recover without reboot.
- Disconnect CAN → Expect “no data” state without bus error.

**Derating & environment**

- Regulators derated to ≤70% of max current at 60 °C.
- Electrolytics 105 °C rated, ≥2× ripple margin.
- Cable bend radius ≥5× diameter; no sharp-edge contact.

**Safety confirmations**

- Fuse sized appropriately; no ground loops to chassis; harness secured; display mounting doesn’t obstruct field of view.

**Rev B notes**

- Consider 4-layer for improved EMC; add conformal coat if long-term heat cycles demand; add watchdog-tunable thresholds for brown-out behavior.

---

## H) Ops Pack (Owner’s Guide v2, Runbook, Service Notes)

**What I’m operating and supporting**

A small in-cabin telemetry box that reads CAN, displays key values glanceably, and logs to CSV without corrupting on power loss.

### Owner’s Guide v2 (for “future me” or a friend)

**What’s in the box**

- CCA unit (Rev A1), labeled with serial + firmware hash
- Vehicle harness (OBD-II pass-through → fused 12 V accessory + CAN)
- SD card (High-Endurance, pre-formatted FAT32)
- Quick-start sheet (QR to full guide + firmware repo)

**Install (10–15 min)**

1. Turn car OFF.
2. Plug pass-through at OBD-II; route harness along trim; secure with two zip ties.
3. Mount unit with VHB + bracket under dash (doesn’t obstruct airbag/leg space).
4. Insert SD (click until latched).
5. Turn ignition to ACC; verify splash screen → values within 2 s.
6. If screen is blank: see “Troubleshooting” below.

**Operate**

- **Glance pattern**: Oil pressure (big), oil temp, coolant temp, AFR, RPM, gear.
- **Buttons**: ▲/▼ page, ◼ start/stop logging (status LED).
- **Logging**: Starts automatically when CAN frames present; file rolls every 20 min.
- **Power loss**: Safe—files are chunked. Last line may be partial only.

**Data offload**

- Power OFF → remove SD → copy `/logs/YYYY-MM-DD/*.csv`.
- Each row: `ts_ms, rpm, oil_p_kpa, oil_t_C, clt_C, afr, gear, …`.
- Keep raw files; analyze in Python/Excel as needed.

**Safety + Warnings**

- Do not obstruct driver view.
- Do not modify harness while connected.
- Fused at input; replace only with same rating.
- Not a substitute for factory gauges/ECU protection.

---

### Ops Runbook (what I do every time)

**Pre-Session (2 min)**

- SD present (LED heartbeat 1 Hz).
- Values live on screen; no DTCs.
- Harness seated; no chafe points.

**During Session**

- Glance oil pressure on long corners.
- If screen flags “No CAN” or “Over-temp,” pit in.

**Post-Session (3 min)**

- Stop log → ignition OFF.
- Pull SD → copy latest CSV → tag with session, ambient temp, notes.
- Scan “issues list” row in Notion (vibe, readability, boot time) and add any observations.

**Firmware Update (5 min)**

1. Download release zip with SHA noted.
2. Flash via UART header (FTDI) using `flash.sh`.
3. Power cycle; splash shows new version + hash.
4. Record version in “Installed Firmware” DB.
5. Run 2-minute bench self-test script.

**Spare/Swap Plan**

- I keep one spare pre-flashed unit and one spare harness in my track bin.
- If a unit fails at the track: swap entire unit → debug at home.

---

### Service Notes (maintenance & replacement)

**Intervals**

- SD (high-endurance): replace every 12 months or 100 hours of logging.
- Visual: connectors, strain relief, enclosure screws—every 3 months.
- Thermal pad/paste (if used): inspect annually.
- Firmware: update only on a “need” basis (bug fix/new feature), not reflexively.

**Field Replaceables**

- SD card, input fuse, enclosure screws, external harness.
- Internal board not field-serviceable at the track; swap whole unit.

**Labels & Versioning**

- Exterior label: `CCA Rev A1 / FW v0.7.3 / SHA: 9f3d2e`
- Inside label (small): assembly date + tester initials.

---

### Troubleshooting Matrix (quick reference)

```
Symptom                    Likely CauseCheck                              Fix
No display at ACCNo power / fuse blown12V at harness; fuse continuity    Replace fuse; reseat harness
“NO CAN” banner            Wrong bus / loose conn       OBD pass-through seating           Reseat;check CANH/L at pins
Boot >2 s                 SD slow init / bad card      Trywithout SD; swap SD            Replace SD (HEtype)
CSV corrupt                Power cut mid-commit         Count partialrowsonly            Accept partial lastrow;update FWif frequent
Unreadablein sun          Display brightness/font       Sun test; angle glare             Increase font; anti-glare film; re-aim
Device hotto touch        Poor airflow / derating      Cabintemp; regulatortempAdd vents; heatsink;limit backlight

```

---

## I) Business Lite (unit economics, IP/licensing, ethics, export)

**What I’m evaluating**

If I decided to offer a small batch to other owners, does it make sense? What safeguards, costs, and policies do I need so I don’t create a support nightmare or legal mess?

### Value Proposition (one-liner)

“Drop-in, glanceable telemetry and robust logging for track days—no OEM cuts, no bricking logs on power loss.”

**Ideal customer**

Track-day/HPDE drivers who want health monitoring + logs without a laptop or race dash.

**Positioning**

Not a race ECU, not a hacky dev board lash-up; a tidy accessory focused on safety-relevant numbers and reliable logs.

---

### Unit Economics (Rev A small-batch estimate)

```
COGS (1–20 units)                     Est. $
PCB & assembly (2-layer, hand SMD)55
Enclosure + hardware18
Display module20
Harness + connectors28
Power (buck/LDO/TVS/fuse)12
MCU module10
SD + slot7
Testtime (0.5 h @ $35/h)17.5
Packaging + insert4
QC scrap reserve (5%)8
------------------------------------------
Estimated COGS                        ~$179

```

**Retail target**

- Hobby kit (no harness): ~$229
- Fully assembled + harness: ~$349

**Margin sanity**

At $349 retail on ~$179 COGS → ~49% gross before overhead. For tiny batches, that margin covers my time, returns, and inevitable “help me flash firmware” emails.

**Sensitivity**

- If I switch to contract assembly + test jig, test time drops → COGS improves by ~$10–15/unit at volume 50+.
- Display cost volatility: ±$5–10; lock alternates in AVL.

---

### Build & Fulfillment Plan (tiny-batch)

- **Flow**: Order kits → bench assemble → run 10-min automated test → burn QC sticker → pack with QR link.
- **Test jig**: Bed-of-nails (or pogo cable) checks 3V3/5V, CAN loopback, SD R/W, display pattern, RTC (if used).
- **Traceability**: Serial + firmware hash logged against test results and buyer email.
- **Packaging**: ESD bag for unit; harness in separate pouch; card with safety notes and QR.

**Warranty + Returns (draft)**

- 90-day limited warranty for manufacturing defects on the unit/harness; excludes misuse or vehicle damage.
- 30-day no-questions return if undamaged.
- Firmware is provided “as-is”; logs are user responsibility.

---

### Legal/IP/Licensing (keep it clean)

- **Firmware**: I’ll release under MIT (or keep private per decision later); include third-party licenses bundled; SBOM lists versions.
- **Hardware**: I can choose to publish schematics under a permissive license (e.g., CERN OHL-S) or keep proprietary; pick one and state it clearly.
- **Trademarks/Brand**: Use my brand name and logo; avoid OEM marks/logos anywhere.
- **Vehicle disclaimers**: “Not an OEM product; not a safety device; for off-highway or track use at owner’s discretion.”
- **Protocols**: Reading CAN data only; no commands to vehicle; explicitly state “no control frames.”
- **Privacy**: Logs contain no PII; user owns their data; no telemetry is uploaded by default.

---

### Compliance, Ethics, Export

- **RoHS/REACH**: Prefer compliant parts; note status in BOM; don’t claim certification unless lab-tested.
- **EMC**: No claim of formal certification (it’s an in-cabin accessory). Keep emissions low via layout/filters; provide install guidance.
- **Safety Ethic**: Never market as a substitute for OEM warnings or gauges; keep UI conservative (no distraction).
- **Export**: Likely **EAR99** (general purpose). Avoid shipping to sanctioned regions.
- **Right-to-Repair**: Provide pinout and basic service notes so users aren’t locked out of maintenance.

---

### Support & Release Management

- **SLA (best-effort)**: Email reply ≤72 h; bugs triaged in GitHub Issues; critical fixes within 2 weeks when feasible.
- **Releases**: Semantic versioning; release notes include SHA, changes, migration notes, and rollback steps.
- **Recall Plan**: If a critical defect is found, email buyers, publish mitigation/workaround, and offer replacement or refund.

---

### Risk Register (business)

```
Risk                          Impact          Mitigation
Display supply swings         COGS ↑          Two alternates; parametric by controller (ILI9341/ST7789)
User installs poorly          Returns ↑Clear install guide; pre-terminated harness; strain relief
CSV corruption complaints     Reputation       Chunked writes; endurance tests;clear power-off guidance
Feature creep (BLE UI)        Schedule slip    Stickto RevA scope; defer UIto RevB
Support load >margin         Burnout          Priceto include support; publish self-help docs/videos

```

---

# 1) Configuration Management Plan — *My Worked Example*

**What I set up**

I put the whole project in a single Git repo with a predictable layout, version labels, baselines, and reproducible releases. I also keep a Notion “Baselines” and “Releases” table that mirrors what’s in git so I can see status at a glance.

**Repo layout I use**

```
/docs# Reqs, ICD, ADRs, specs (markdown + exported PDFs)
/hardware# CAD, schematics, PCB, gerbers, drawings
/firmware# source, build scripts, compiled .bin
/software# log viewer scripts, tools
/test# plans, procedures, raw logs, screenshots, reports
/ops# owner’s guide, runbook, service notes
/release# as-built packs per release (zip + manifest)
/evidence# stable copies of plots/photos used in test reports

```

**Naming + versioning rules I actually follow**

- Documents: `Reqs_vA1.md`, `ICD_vA1.md`, `BOM_vA1.csv`, `TestPlan_vA1.md`
- Firmware binary: `cca_revA_fw_v1.0.bin`
- Git tags: `Rel-A1.0`, `Rel-A1.1` (hotfix), etc.
- Baseline labels in Notion (and inside docs): `BR-A1`, `BR-A2`

**How I locked my first baseline (BR-A1)**

- I finished and reviewed: `Reqs_vA1`, `ICD_vA1`, `BOM_vA1`, `TestPlan_vA1`.
- I recorded the exact commit (`abc1234`) and froze those versions as **BR-A1**.
- I added a Baseline row:

```
Baseline ID,Included Artifacts,Rationale,Approver,Date,Tag/Hash
BR-A1,"Reqs_vA1;ICD_vA1;BOM_vA1;TestPlan_vA1","Freeze Rev A design inputs","Kian",2025-12-28,git:abc1234

```

**How I cut my first release (Rel-A1.0)**

1. Built the firmware from a clean clone: `git checkout abc1234`, then build script.
2. Executed the verification tests from `TestPlan_vA1`; saved evidence under `/evidence/Rel-A1.0/*`.
3. Created an **as-built pack**:

```
/release/Rel-A1.0/
  manifest.txt
  docs/Reqs_vA1.pdf, ICD_vA1.pdf, TestReport_A1.pdf
  hardware/gerbers_A1.zip, BOM_vA1.csv, drawings_A1.pdf
  firmware/cca_revA_fw_v1.0.bin  (commit def5678)
  evidence/ (plots, photos, raw logs referenced by report)

```

1. Wrote the manifest with file hashes:

```
Release: Rel-A1.0
Docs:
  Reqs_vA1.pdf (sha256:...)
  ICD_vA1.pdf (sha256:...)
Firmware:
  cca_revA_fw_v1.0.bin (commit def5678, sha256:...)
Hardware:
  gerbers_A1.zip (sha256:...), BOM_vA1.csv (sha256:...)
Evidence:
  links enumerated in TestReport_A1.pdf

```

1. Tagged the repo: `git tag -s Rel-A1.0 def5678` (signed tag).
2. Added a Release row:

```
Release Tag,Purpose,Included Baselines,Build Hash/Binaries,Evidence,Approver,Date,Pack Link
Rel-A1.0,"First usable Rev A","BR-A1","fw.bin (git:def5678)","/release/Rel-A1.0/TestReport_A1.pdf","Kian",2026-01-02,/release/Rel-A1.0.zip

```

**Snags I hit + how I fixed them**

- *Snag:* I initially forgot to copy screenshots into `/release/Rel-A1.0/evidence`.
    
    *Fix:* I updated the test SOP: every plot/photo must be exported to `evidence/` and paths locked in the report *before* I tag a release.
    
- *Snag:* Firmware commit in the manifest didn’t match the tag once.
    
    *Fix:* I added a pre-release checklist step: “Rebuild from tag in a **fresh clone**, then re-export evidence.”
    

**Proof my CM works**

I asked a friend to clone `Rel-A1.0`, follow `manifest.txt`, and rebuild the firmware and report. He reproduced the same hashes and screenshots. CM passed.

**Next time**

Automate the pack with a CI job that assembles the zip, computes hashes, and posts the release notes.

---

# 1) Configuration Management Plan — *My Worked Example*

**What I set up**

I put the whole project in a single Git repo with a predictable layout, version labels, baselines, and reproducible releases. I also keep a Notion “Baselines” and “Releases” table that mirrors what’s in git so I can see status at a glance.

**Repo layout I use**

```
/docs# Reqs, ICD, ADRs, specs (markdown + exported PDFs)
/hardware# CAD, schematics, PCB, gerbers, drawings
/firmware# source, build scripts, compiled .bin
/software# log viewer scripts, tools
/test# plans, procedures, raw logs, screenshots, reports
/ops# owner’s guide, runbook, service notes
/release# as-built packs per release (zip + manifest)
/evidence# stable copies of plots/photos used in test reports

```

**Naming + versioning rules I actually follow**

- Documents: `Reqs_vA1.md`, `ICD_vA1.md`, `BOM_vA1.csv`, `TestPlan_vA1.md`
- Firmware binary: `cca_revA_fw_v1.0.bin`
- Git tags: `Rel-A1.0`, `Rel-A1.1` (hotfix), etc.
- Baseline labels in Notion (and inside docs): `BR-A1`, `BR-A2`

**How I locked my first baseline (BR-A1)**

- I finished and reviewed: `Reqs_vA1`, `ICD_vA1`, `BOM_vA1`, `TestPlan_vA1`.
- I recorded the exact commit (`abc1234`) and froze those versions as **BR-A1**.
- I added a Baseline row:

```
Baseline ID,Included Artifacts,Rationale,Approver,Date,Tag/Hash
BR-A1,"Reqs_vA1;ICD_vA1;BOM_vA1;TestPlan_vA1","Freeze Rev A design inputs","Kian",2025-12-28,git:abc1234

```

**How I cut my first release (Rel-A1.0)**

1. Built the firmware from a clean clone: `git checkout abc1234`, then build script.
2. Executed the verification tests from `TestPlan_vA1`; saved evidence under `/evidence/Rel-A1.0/*`.
3. Created an **as-built pack**:

```
/release/Rel-A1.0/
  manifest.txt
  docs/Reqs_vA1.pdf, ICD_vA1.pdf, TestReport_A1.pdf
  hardware/gerbers_A1.zip, BOM_vA1.csv, drawings_A1.pdf
  firmware/cca_revA_fw_v1.0.bin  (commit def5678)
  evidence/ (plots, photos, raw logs referenced by report)

```

1. Wrote the manifest with file hashes:

```
Release: Rel-A1.0
Docs:
  Reqs_vA1.pdf (sha256:...)
  ICD_vA1.pdf (sha256:...)
Firmware:
  cca_revA_fw_v1.0.bin (commit def5678, sha256:...)
Hardware:
  gerbers_A1.zip (sha256:...), BOM_vA1.csv (sha256:...)
Evidence:
  links enumerated in TestReport_A1.pdf

```

1. Tagged the repo: `git tag -s Rel-A1.0 def5678` (signed tag).
2. Added a Release row:

```
Release Tag,Purpose,Included Baselines,Build Hash/Binaries,Evidence,Approver,Date,Pack Link
Rel-A1.0,"First usable Rev A","BR-A1","fw.bin (git:def5678)","/release/Rel-A1.0/TestReport_A1.pdf","Kian",2026-01-02,/release/Rel-A1.0.zip

```

**Snags I hit + how I fixed them**

- *Snag:* I initially forgot to copy screenshots into `/release/Rel-A1.0/evidence`.
    
    *Fix:* I updated the test SOP: every plot/photo must be exported to `evidence/` and paths locked in the report *before* I tag a release.
    
- *Snag:* Firmware commit in the manifest didn’t match the tag once.
    
    *Fix:* I added a pre-release checklist step: “Rebuild from tag in a **fresh clone**, then re-export evidence.”
    

**Proof my CM works**

I asked a friend to clone `Rel-A1.0`, follow `manifest.txt`, and rebuild the firmware and report. He reproduced the same hashes and screenshots. CM passed.

**Next time**

Automate the pack with a CI job that assembles the zip, computes hashes, and posts the release notes.

---

# 3) Calibration & Metrology — *My Worked Example*

**What I decided to calibrate for Rev A**

- **Oil pressure** (critical)
- **Supply/logic voltage readings** (important for power sanity)
- **Temperature** (useful; I did a basic check)
- (Display luminance is a UX topic; I measured qualitatively and deferred full luminance calibration to Rev B.)

**My references**

- Pressure: a shop reference gauge (recent cert) → treated as traceable.
- Voltage: bench supply with recent calibration sticker.
- Temperature: ice bath (0 °C) and a reliable digital thermometer for room temp.

**Acceptance criteria I used**

- Pressure: within **±2%** of reading across 0–700 kPa.
- Voltage: within **±1%** at 5 V and 12 V points.
- Temperature: within **±2 °C** at two points (0 °C, ~25 °C) for Rev A.

**Procedure I actually ran (pressure sensor)**

1. Warmed the board and the pressure rig for 10 minutes.
2. Applied 0/100/300/500/700 kPa; held each point ≥30 s; logged 10 samples per point.
3. Computed average error at each point; fit a linear offset (Rev A assumption).
4. Stored the offset in config; re-checked 300 kPa to confirm within ±2%.
5. Saved the record and labeled the unit with **Cal date** and **Next due** (6 months).

**My calibration record row**

```
Unit ID,Sensor,Range,Importance,Reference,Points,Criteria,Avg Error,Offset,Uncertainty,Pass/Fail,Cal Date,Next Due,By,Evidence
U-023,Oil Pressure,0-700 kPa,Critical,"Gauge 0.1% SN123 (valid to 2026-03)","0/100/300/500/700","±2%",+0.8%,-1.9 kPa,±0.5%,PASS,2025-12-28,2026-06-28,Kian,/release/Rel-A1.0/evidence/cal/U-023.pdf

```

**Voltage check (abbreviated)**

- 5.00 V and 12.00 V set on bench supply; ADC readings after scaling matched within **±0.7%**. Logged in the same CSV (separate row).

**Temperature sanity**

- Ice bath yielded 0.6 °C indicated (offset −0.6 °C). Room measured 24.2 °C indicated vs 24.8 °C reference (−0.6 °C). I stored a simple offset and marked full multi-point calibration for Rev B.

**Snags I hit + fixes**

- *Snag:* Temperature readings were noisier than expected.
    
    *Fix:* I re-checked the pull-up value and sampling time; adding a small moving average stabilized results; documented as an ADR note for Rev B improvements.
    
- *Snag:* I almost skipped re-verifying at the mid-point after applying the pressure offset.
    
    *Fix:* I added a hard step in the procedure: “Re-test mid-point and record.”
    

**What “done” looked like for me**

- Every **critical** channel has a current, passing calibration record.
- Offsets are stored and referenced by the firmware version in the release manifest.
- The unit has a calibration label; next due date is on my calendar.

**Next time**

Move to a 5-point temp calibration with uncertainty, and block releases if any critical calibration is expired.

---

### Go-to-Market (if I proceed)

- **Validation**: 10 beta units to local HPDE community with feedback form.
- **Docs site**: Simple landing page + full docs + downloads; no fluff.
- **Sales**: Small storefront (Gumroad/Shopify) with clear disclaimers.
- **Content**: Short video: install (3 min), use (2 min), data export (2 min).
