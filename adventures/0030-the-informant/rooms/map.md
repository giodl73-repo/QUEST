---
adventure: 0030-the-informant
document: map
author: dungeon-smith
created: 2026-04-21
---

# Havenmere Watch House — South Station Map

## ASCII Map

```
        MERCER LANE (STREET)
              ↓
    ══════════════════════════════
    ║  [01] DUTY DESK / ENTRANCE  ║   Sergeant asleep; key rack on wall
    ║         │                   ║
    ║  [02] RECORDS ROOM (side)   ║   Files; locked cabinet; no occupant
    ║         │                   ║
    ═════════════════════════════
              │  corridor
    ══════════════════════════════
    ║  [03] CELLS CORRIDOR        ║   Three cells; oil lamp (low)
    ║    Cell 1 — empty           ║
    ║    Cell 2 — ALDRAS          ║   Target
    ║    Cell 3 — drunk detainee  ║   Asleep; snoring
    ══════════════════════════════
              │
    ══════════════════════════════
    ║  [04] SERGEANT'S OFFICE     ║   Officer from main gaol sleeping
    ║  (end of corridor)          ║
    ══════════════════════════════
    ║  [05] SERVICE DOOR (rear)   ║   Back alley exit; standard ward lock
    ══════════════════════════════

        BACK ALLEY (WEST FACE)
```

## Legend

| Symbol | Meaning |
|---|---|
| `[NN]` | Keyed location |
| `│` | Passage |
| `════` | Exterior wall |

## Connections Table

| From | To | Type | Condition |
|---|---|---|---|
| Street | 01 Duty Desk | Front door | Unlocked (Watch house; always open) — but sergeant is at desk |
| 01 Duty Desk | 02 Records Room | Side door | Unlocked |
| 01 Duty Desk | 03 Cells Corridor | Corridor | Open; visible from desk |
| 03 Cells Corridor | 04 Sergeant's Office | Door | **Unlatched** (Perception DC 13 to hear breathing) |
| Back Alley | 05 Service Door | Ward lock | **DC 13** Thieves' Tools (Darro DC 9) |
| 05 Service Door | 03 Cells Corridor | Direct | Preferred entry — bypasses duty desk |

## Two paths to the cells

- **Path A (front):** Street → Duty Desk → Cells Corridor (risks waking sergeant)
- **Path B (rear):** Back Alley → Service Door → Cells Corridor (preferred; bypasses desk)

## Noise economy

- Front door entry: automatic sergeant awareness (Perception 8 for any noise)
- Service door (lockpicked quietly): no alert
- Cell bar via slot: no noise (if using the slot technique)
- Key retrieval from duty rack: Stealth DC 12 (past sleeping sergeant)
- Sergeant's office door fully opening: officer stirs (Perception DC 10 for her)

## DM notes

The station is designed for a quiet extraction — Path B to the service door, Darro opens the cell slot, Aldras moves. Combat is possible but costly (reinforcements from the constable's exterior circuit, then from the main station). A fight here burns resources the party needs for later sessions.
