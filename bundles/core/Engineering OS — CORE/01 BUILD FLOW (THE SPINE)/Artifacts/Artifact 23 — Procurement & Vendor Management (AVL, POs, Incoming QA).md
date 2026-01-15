# Artifact 23 — Procurement & Vendor Management (AVL, POs, Incoming QA)

**What this is**

How you source, buy, receive, and verify components/software.

**Artifacts**

- AVL (Approved Vendor List)
- PO & Receipt Log
- Incoming QA Checklist

**How to build**

1. Create **AVL** table:
    - Vendor, Category, Approved Items, Contact, Terms, Risk Notes, Performance (A/B/C).
2. Create **PO/Receipts** table:
    - PO #, Item ID, Qty Ordered/Received, Date, Price, Invoice, Receipt link, Discrepancies (Y/N).
3. Create **Incoming QA checklist** (toggle template):
    
    ```
    - Verify part number & rev against BOM
    - Visual inspection (damage/packaging)
    - Quantity match
    - Certificates/COC or license present
    - Basic functional/fit check (if applicable)
    - Record lot/serial for traceability
    
    ```
    
4. Link received items back to **BOM rows**.

**Quality check**

- You can reconstruct **who supplied what, when, and why** for any item.

---

