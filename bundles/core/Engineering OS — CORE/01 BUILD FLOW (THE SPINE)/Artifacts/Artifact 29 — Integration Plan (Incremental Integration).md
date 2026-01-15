# Artifact 29 — Integration Plan (Incremental Integration)

**What this is**

A plan to integrate subsystems in the least-risk order.

**Artifacts**

- Integration Sequence
- Interface Mocks/Stubs
- “Done” Criteria per integration step

**How to build**

1. List the **lowest-risk chain** from inputs → outputs.
2. For unavailable pieces, specify **mocks/stubs/simulators**.
3. For each step:
    - Inputs provided by (real/mocked), Expected outputs, Telemetry to confirm, Issues to watch, “Done when …”.

**Quality check**

- You can show progress at every step (observable signals, logs, plots).

---

