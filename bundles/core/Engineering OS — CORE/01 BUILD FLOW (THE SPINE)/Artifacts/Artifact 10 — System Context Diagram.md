# Artifact 10 — System Context Diagram

**What this is**

Visual of external actors/systems around you (big picture).

**Artifact**

- Context Diagram (can be ASCII now; later you can attach a draw.io image)

**How to build**

1. List external **actors/systems/services** (3–8).
2. Draft an ASCII diagram:
    
    ```
    [Customer/User] ──uses──> [Your Product] ──exports──> [Reports/DB]
           │                         │
           └──support/ops──> [Support Tools/Telemetry]
    [Upstream Data Source] ──feeds──> [Your Product] ──calls──> [3rd-Party API]
    
    ```
    
3. Label arrows with **what** (data/command) and **how often** (rate, schedule).

**Quality check**

- Each arrow clearly states **what moves** and **how often**.

---

