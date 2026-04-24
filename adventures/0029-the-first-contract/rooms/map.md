---
adventure: 0029-the-first-contract
document: map
author: dungeon-smith
created: 2026-04-21
---

# Fenwick Gale's Counting House — Map

## ASCII Map

```
        ANCHOR ROW (STREET)
              ↓
    ══════════════════════════════
    ║  [01] TRADING FLOOR        ║   Ground floor — public
    ║  (display cases, shut)     ║
    ║         │  stairs↑         ║
    ║  [02] STORE-ROOM (side)    ║   Bessa's cot; candle lit
    ║  (adjacent ground floor)   ║
    ══════════════════════════════
              │ stairs↑
    ══════════════════════════════
    ║  [03] GALE'S OFFICE        ║   First floor — private
    ║  (desk, locked drawer)     ║
    ║         │  door →          ║
    ║  [04] COUNTING ROOM        ║   Iron bar from inside
    ║  (ledger, safe shelf)      ║
    ║  (high narrow window→alley)║
    ══════════════════════════════
              │ stairs↑
    ══════════════════════════════
    ║  [05] GALE'S BEDROOM       ║   Second floor — Gale sleeping
    ══════════════════════════════

        ALLEY (EAST FACE)
    ══════════════════════════════
    Window to [04] — 15 ft up, 8 in wide
```

## Legend

| Symbol | Meaning |
|---|---|
| `[NN]` | Keyed location |
| `│` / `─` | Passage / stairs |
| `→` | Door direction |
| `════` | Exterior wall |

## Connections Table

| From | To | Type | Condition |
|---|---|---|---|
| Street | 01 Trading Floor | Front door | **Locked** (DC 14 Thieves' Tools; Darro: DC 10 with expertise) |
| 01 Trading Floor | 02 Store-Room | Side door | Unlocked (store-room door opens inward) |
| 01 Trading Floor | 03 Gale's Office | Stair | Open |
| 03 Gale's Office | 04 Counting Room | Door | **Iron-barred from inside** (cannot be forced without noise; key held by Bessa) |
| 03 Gale's Office | 05 Gale's Bedroom | Stair | Open |
| Alley | 04 Counting Room | High window | Athletics DC 14 to squeeze through (Darro advantage); 15 ft drop inside |

## Two paths to the ledger

- **Path A (window):** Alley → window → Counting Room (bypasses the bar from inside)
- **Path B (Bessa):** Front door → Store-Room → Bessa → key → Counting Room

## Noise economy

- Front door forced: automatic alert to Gale (2 floors up, sleeping light)
- Counting room bar forced: Perception DC 10 for Gale (ground floor creak carries)
- Bessa's cot disturbed: Gale does not hear if Bessa is cooperative
- Window entry: no noise unless drop landing fails (Athletics DC 12 to land quietly)

## DM notes

The building is designed for a two-approach play — the party can split, with Darro going up the alley while Mira handles the front, or converge on Bessa first. Bessa is the intended resolution path; the window is the backup. Both work. The session does not require combat.

Gale's bedroom (05) is accessible but there is no narrative reason to go there. If the party enters, he is asleep with a light snore. He has a cash box under the bed (15 gp, not the objective). Waking him is the failure condition.
