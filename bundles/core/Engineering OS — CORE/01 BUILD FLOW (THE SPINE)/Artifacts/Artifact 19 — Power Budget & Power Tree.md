# Artifact 19 — Power Budget & Power Tree

*(Software-only alt: “Resource Budget & Resource Tree”)*

**Artifacts**

- Power Tree diagram
- Power Budget table
    
    *(or Resource Tree + CPU/RAM/IO/Throughput budget for software)*
    

**How to build**

- **Hardware**
    1. Table: Rail/Source, Nominal Voltage, Typical Current, Peak/Inrush, Regulator/Converter, Protection (fuse/TVS/OVP), Margin (%).
    2. ASCII tree:
        
        ```
        Source → Fuse → Surge/TVS → Buck (5V, 2A) → LDO (3.3V, 500mA)
                                     ↘ 5V Peripherals (max 800mA)
        
        ```
        
    3. Add worst-case scenarios (startup, hot/cold).
- **Software**
    1. Table: Component, CPU% at load, RAM (MB), Disk (MB/s), Network (Mb/s), Peak Burst, Margin.
    2. ASCII “Resource Tree” (who consumes what).

**Quality check**

- Worst-case usage stays **within margin** (≥30% slack is a good default).

---

