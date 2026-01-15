# Artifact 20 — Data Flow / Task Model

**What this is**

Who produces/consumes data, at what rate, with what buffers/time budgets.

**Artifacts**

- Data-Flow Diagram
- Timing Budget per stage

**How to build**

1. ASCII diagram:
    
    ```
    [Ingest Task @10Hz] -> (Queue Q1 size=100) -> [Parser 2ms]
                          -> (Queue Q2 size=50) -> [Processor 5ms]
                          -> (Buffer B 1s) -> [Writer batch/100ms]
    
    ```
    
2. Notion table “Timing Budget”:
    - Stage, Trigger/Rate, Avg Time, Worst-Case Time, Deadline/Period, Slack (computed), Failure Strategy (drop/retry/back-pressure).
3. Define back-pressure rules (what happens when queues fill) and error paths.

**Quality check**

- For each stage, **Worst-Case Time ≤ Deadline**, queues sized so bursts don’t cause loss (unless allowed).

---

## Tips for Using This in Notion

- Make each section a **template page** you can duplicate per project.
- For tables, start with properties exactly as listed; you can always add columns later.
- Use **“Quality check”** as a toggle block under each section and don’t progress until it passes.
- Link artifacts together (e.g., each FR links to its acceptance test in §26/§27 when you build those).

If you want, I can split this into **40 separate Notion page templates** with pre-built databases and formulas (RPN, Weighted Totals, Slack) so you can duplicate the whole OS in one shot.

---

Awesome—here’s the **Notion-ready, step-by-step “how to build every artifact” guide for Items 21–40**. Copy-paste directly into Notion. Keep each section as its own page or a long page with toggles. It’s written for a motivated beginner but rigorous enough for pros.

---

