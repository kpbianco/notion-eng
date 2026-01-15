# Artifact 11 — Architecture Overview / Block Diagram

**What this is**

Your internal boxes and how they connect.

**Artifacts**

- Block Diagram
- Responsibility paragraph per block

**How to build**

1. Identify **5–9** blocks (modules/subsystems).
2. Sketch ASCII:
    
    ```
    [Input Adapter] -> [Parser] -> [Core Logic] -> [Storage]
                                -> [UI/Display]
                       [Health Monitor] -> [Alerts]
    
    ```
    
3. For each block, add a short paragraph:
    - Inputs, Outputs, Key responsibilities, What must never happen (invariant).

**Quality check**

- If you remove a block, you can say exactly what breaks.

---

