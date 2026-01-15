# Engineering OS — Document Examples (Marketplace Draft)

### What this page is

A clean, reference-style set of **example artifacts** you can copy into your Engineering OS.

It includes three common, high-leverage documents:

- A **BOM** example (with sourcing + DFX intent)
- An **AVL** example (same schema, vendor-ready)
- An **FMEA** example (risk-prioritized actions with residual risk)

### How to use

1. Duplicate this page into a project.
2. Copy the table you need.
3. Replace the example rows with your real data.
4. Keep the column structure the same so you can sort, filter, and roll up later.

---

## BOM (example)

| Item # | Function | Preferred Mfr | Preferred P/N | Second Source Mfr | Second Source P/N | Qty | Unit Cost | Ext Cost | Lifecycle | RoHS | Lead Time (wk) | Supplier | SKU | DFX Notes | AVL Approved (Y/N) | Notes | Rev |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Main MCU | Espressif | ESP32-WROOM-32E | Espressif | ESP32-WROOM-32U | 1 | 3.90 | 3.90 | Active | Yes | 4 | Mouser | 356-ESP32-WROOM-32E | Check antenna keepout; choose -U if external antenna | Y | Any module OK meeting pin map | A1 |
| 2 | CAN Transceiver | TI | TCAN1042DR | Microchip | MCP2562-E/SN | 1 | 0.90 | 0.90 | Active | Yes | 2 | Digi-Key | 296-43835-1-ND | ISO 11898-2, 5V rail, ESD note | Y | Footprint shared between options | A1 |
| 3 | Buck Converter | TI | LM2596S-5.0 | Monolithic | MP1584EN | 1 | 1.50 | 1.50 | Active | Yes | 2 | Amazon | MP1584-Module | Derate to 60% max; thermal pad under IC | Y | Module acceptable for Rev A | A1 |
| 4 | TVS Diode (Input) | Littelfuse | SMBJ58A | Bourns | SMBJ58A | 1 | 0.28 | 0.28 | Active | Yes | 1 | Digi-Key | SMBJ58ALFCT-ND | Bidirectional? choose per system ground | Y | Protects 12V transients | A1 |
| 5 | Fuse Holder + Fuse | Littlefuse | 0451.250MRL | Littelfuse | 0451.500MRL | 1 | 0.35 | 0.35 | Active | Yes | 1 | Mouser | 576-0451.250MRL | Select rating via inrush/current calc | Y | Inline or PCB mount acceptable | A1 |
| 6 | Display (SPI) | Newhaven | NHD-2.4-240320CF | BuyDisplay | ER-TFT024-3 | 1 | 10.00 | 10.00 | Active | Yes | 3 | Vendor | ER-TFT024-3 | Sunlight check; SPI mode; pin match | Y | Must meet luminance target | A1 |
| 7 | Storage (uSD) | SanDisk | Industrial 16GB | Transcend | High Endurance 16GB | 1 | 6.00 | 6.00 | Active | Yes | 1 | Amazon | SDI-16 | Use high endurance; chunked writes | Y | Test power-cut robustness | A1 |
| 8 | Connector (Main) | Molex | MicroFit 3.0 6pos | TE | MicroMatch 6pos | 1 | 0.75 | 0.75 | Active | Yes | 2 | Mouser | 43025-0600 | Keying; current rating; strain relief | Y | Crimp spec linked | A1 |
| 9 | Enclosure | Hammond | 1591XX | Bud | PN-1324-C | 1 | 8.00 | 8.00 | Active | Yes | 2 | Mouser | 546-1591XX | Ingress; mounting ears; airflow | Y | Labeling spec v1 | A1 |
| 10 | Mounting Kit | Assorted | M3 Standoffs | Assorted | M3 Standoffs | 1 | 2.50 | 2.50 | Active | Yes | 1 | Amazon | ST-M3-KIT | Lock washers; threadlocker where req'd | Y | Spare included | A1 |
| TOTAL |  |  |  |  |  |  |  | 34.18 |  |  |  |  |  |  |  |  | A1 |

---

## AVL (example)

| Item # | Function | Preferred Mfr | Preferred P/N | Second Source Mfr | Second Source P/N | Qty | Unit Cost | Ext Cost | Lifecycle | RoHS | Lead Time (wk) | Supplier | SKU | DFX Notes | AVL Approved (Y/N) | Notes | Rev |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Main MCU | Espressif | ESP32-WROOM-32E | Espressif | ESP32-WROOM-32U | 1 | 3.90 | 3.90 | Active | Yes | 4 | Mouser | 356-ESP32-WROOM-32E | Check antenna keepout; choose -U if external antenna | Y | Any module OK meeting pin map | A1 |
| 2 | CAN Transceiver | TI | TCAN1042DR | Microchip | MCP2562-E/SN | 1 | 0.90 | 0.90 | Active | Yes | 2 | Digi-Key | 296-43835-1-ND | ISO 11898-2, 5V rail, ESD note | Y | Footprint shared between options | A1 |
| 3 | Buck Converter | TI | LM2596S-5.0 | Monolithic | MP1584EN | 1 | 1.50 | 1.50 | Active | Yes | 2 | Amazon | MP1584-Module | Derate to 60% max; thermal pad under IC | Y | Module acceptable for Rev A | A1 |
| 4 | TVS Diode (Input) | Littelfuse | SMBJ58A | Bourns | SMBJ58A | 1 | 0.28 | 0.28 | Active | Yes | 1 | Digi-Key | SMBJ58ALFCT-ND | Bidirectional? choose per system ground | Y | Protects 12V transients | A1 |
| 5 | Fuse Holder + Fuse | Littlefuse | 0451.250MRL | Littelfuse | 0451.500MRL | 1 | 0.35 | 0.35 | Active | Yes | 1 | Mouser | 576-0451.250MRL | Select rating via inrush/current calc | Y | Inline or PCB mount acceptable | A1 |
| 6 | Display (SPI) | Newhaven | NHD-2.4-240320CF | BuyDisplay | ER-TFT024-3 | 1 | 10.00 | 10.00 | Active | Yes | 3 | Vendor | ER-TFT024-3 | Sunlight check; SPI mode; pin match | Y | Must meet luminance target | A1 |
| 7 | Storage (uSD) | SanDisk | Industrial 16GB | Transcend | High Endurance 16GB | 1 | 6.00 | 6.00 | Active | Yes | 1 | Amazon | SDI-16 | Use high endurance; chunked writes | Y | Test power-cut robustness | A1 |
| 8 | Connector (Main) | Molex | MicroFit 3.0 6pos | TE | MicroMatch 6pos | 1 | 0.75 | 0.75 | Active | Yes | 2 | Mouser | 43025-0600 | Keying; current rating; strain relief | Y | Crimp spec linked | A1 |
| 9 | Enclosure | Hammond | 1591XX | Bud | PN-1324-C | 1 | 8.00 | 8.00 | Active | Yes | 2 | Mouser | 546-1591XX | Ingress; mounting ears; airflow | Y | Labeling spec v1 | A1 |
| 10 | Mounting Kit | Assorted | M3 Standoffs | Assorted | M3 Standoffs | 1 | 2.50 | 2.50 | Active | Yes | 1 | Amazon | ST-M3-KIT | Lock washers; threadlocker where req'd | Y | Spare included | A1 |
| TOTAL |  |  |  |  |  |  |  | 34.18 |  |  |  |  |  |  |  |  | A1 |

---

## FMEA (example)

| Function | Failure Mode | Effect | Severity (S) | Cause | Occurrence (O) | Current Controls | Detection (D) | RPN | Recommended Action | Owner | Due | Residual S | Residual O | Residual D | Residual RPN | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Power Input | Overcurrent blows trace | Loss of system power | 8 | Short or surge | 4 | Fuse + TVS | 3 | 96 | Increase fuse selectivity; widen trace; add polyfuse | EE | 2025-01-10 | 6 | 2 | 3 | 36 | Planned |
| Data Logging | File corruption on power cut | Data loss / unusable logs | 7 | Write interrupted | 5 | Chunked writes + pre-alloc | 5 | 175 | Supercap hold-up or double-buffer commit | FW | 2025-01-12 | 5 | 3 | 4 | 60 | In Progress |
| Interface Bus | Wrong voltage on IO | IC damage | 9 | Level mismatch | 3 | Pin map review + IO tests | 4 | 108 | Add level shifting or change part; add series resistors | EE | 2025-01-15 | 7 | 2 | 3 | 42 | Planned |
| Thermals | Regulator overheats | Shutdown / drift | 6 | Inadequate derating | 4 | Heatsinking + 60% derate | 5 | 120 | Thermal pad + airflow cutouts; log temperature | ME | 2025-01-18 | 5 | 2 | 3 | 30 | Planned |
| UX | Glare unreadable display | Safety info missed | 8 | Sunlight glare | 3 | Sunlight test at noon | 4 | 96 | Matte overlay; brighter module; alternate mount | PM | 2025-01-20 | 6 | 2 | 3 | 36 | Planned |