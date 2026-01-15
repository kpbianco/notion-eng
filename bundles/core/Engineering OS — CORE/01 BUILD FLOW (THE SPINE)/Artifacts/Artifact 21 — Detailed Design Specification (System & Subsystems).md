# Artifact 21 — Detailed Design Specification (System & Subsystems)

**What this is**

A precise, testable description of how each subsystem works internally.

**Artifacts**

- System Design Spec (SDS)
- Subsystem Design Specs (SSDS) linked from SDS

**How to build**

1. Create a page **“System Design Spec (v0.1)”** with sections:
    
    ```
    ## Overview
    Scope, assumptions, references
    
    ## Decomposition
    List of subsystems and their responsibilities (link to each SSDS)
    
    ## Key Scenarios
    3–5 sequence flows (startup, steady-state, error, shutdown, update)
    
    ## Cross-Cutting Concerns
    timing, concurrency, error handling, logging/telemetry, safety/security
    
    ## Constraints
    performance ceilings, environmental limits, platform constraints
    
    ```
    
2. Create one **Subsystem Design Spec** per block:
    
    ```
    ### <Subsystem Name>
    Purpose & responsibilities
    Inputs/Outputs (link to ICD fields or APIs)
    Internal data structures & algorithms (high level)
    Timing model (periodic vs event-driven, budgets)
    Error handling (fail-safe states, retries, escalation)
    Diagnostics (health signals, counters, logs)
    Dependencies & configuration
    
    ```
    
3. Link to **ICDs, NFRs, Risk-Kills** where relevant.

**Quality check**

- Every claim is verifiable by a test or traceable to a requirement.

---

