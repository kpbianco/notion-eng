# Artifact 08 — Interface Control Document (ICD)

**What this is**

The contract for how parts/systems talk: fields/pins, units, timing, errors, versioning.

**Artifacts**

- One ICD per interface
- ICD change log

**How to build**

1. For **software/API** interfaces, create a table:
    - Field/Endpoint, Type/Units, Allowed Range/Enums, Direction (in/out), Frequency/Rate, Timeout/Retry, Error Codes, Version.
2. For **hardware/electrical**, create:
    - Signal/Pin, Direction (In/Out), Voltage Level/Current, Pull-up/Down, Timing (setup/hold), Connector, ESD/EMC notes.
3. Add a small **sequence** example (request → response or timing diagram).
4. Add **version** at the top (v0.1) and a **Change Log** block.

**Quality check**

- Someone else could implement the other side using only your ICD.

---

