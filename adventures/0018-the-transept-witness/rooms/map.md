---
adventure: 0018-the-transept-witness
document: map
author: dungeon-smith
created: 2026-04-21
---

# Map — The Transept Witness

## ASCII Map

```
                              N (toward crypt direction / 0020)
                              ↑
                    ┌─────────┴──────────┐
                    │  R3: SOUTH ARM     │
                    │  (Morren's space)  │
                    └─────────┬──────────┘
                              │ (open arch)
[0016 nave] ──[R1: ENTRY]──[R2: NORTH ARM]──[R6: UNSTABLE]
                              │ (open arch)    (NW corner)
                    ┌─────────┴──────────┐
                    │  R4: ARCADE        │
                    │  PASSAGE (loop)    │
                    └─────────┬──────────┘
                              │ (arch)
                    ┌─────────┴──────────┐
                    │  R5: CROSSING      │──── [toward 0019 Sacristy]
                    │  (center)          │
                    └────────────────────┘
```

**Orientation:** Entry from the west (nave connection). The transept runs north-south. Morren is in R3 (south arm). The crossing (R5) connects toward 0019 (Sacristy) — faction-gated per 0016's topology mandate.

## Connections Table

| From | To | Type | Condition |
|---|---|---|---|
| 0016 nave east arch | R1 | Open passage | Always passable |
| R1 | R2 | Open arch | Always passable |
| R2 | R3 | Open arch (south) | Always passable; Morren visible from R2 |
| R2 | R4 | Side passage | Always passable; DC 11 Perception to notice from R2 |
| R2 | R6 | NW corner | Rope barrier visible; **DC 12 Perception** to notice unstable floor; always physically accessible |
| R3 | R5 | South arch | Always passable |
| R4 | R5 | Arcade arch | Always passable |
| R5 | 0019 | East passage | **Campaign lock:** present but blocked — Nave congregation opened the Sacristy path per Route D of 0016; accessible if party has Nave trust |

## Congregation Positions

| NPC | Location | Notes |
|---|---|---|
| **Morren** | R3 (Morren's chair, north windows) | Stationary; waiting |
| 2-3 congregation observers | R2 (watching quietly) | Have heard the account before; watching the party's faces |
| 1 congregation member | R4 (practicing the account; getting parts wrong) | The imperfect oral transmission visible again |
