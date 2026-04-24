---
adventure: 0016-the-nave-congregation
document: map
author: dungeon-smith
created: 2026-04-21
---

# Map — The Nave Congregation

## ASCII Map

```
         UPPER LEVEL
         ╔═══════════╗
         ║ R6        ║──────→ [0017 BELL TOWER]
         ║ GALLERY   ║
         ╚═══╦═══════╝
    (stairs) ║
             ║
[0015 R6]══[R1]══════════[R2: CENTRAL NAVE]══════[R4: APSE]
   (inner    ║                  ║    ║                ║
    door)    ║             (arch)   (stair base)   (back corridor,
             ║                  ║    ║              narrow)
             ║            [R3: NORTH ══════════════╝
             ╚══(arch,     SIDE AISLE]
              quiet)──────[R3]
```

**Cleaner representation:**

```
                                          ┌────────────────────┐
                                          │ R6: UPPER GALLERY  │──→ [0017]
                                          └──────────┬─────────┘
                                                     │ (stairs up)
                                                     │
[0015]══[R1]════════════[R2]═════════════[R4: APSE]
  ↑      ║              ║  ╲             ╱
inner   (arch,        (arch)  (stairway  (back corridor)
door    quiet)          ║     base R5)       │
         ║              ║                    │
         ╚══════════[R3: N. AISLE]═══════════╝
                    (quiet)
```

**Orientation:** West (entrance from 0015) → East (Apse/cup; deeper into cathedral).

## Legend

```
══   open passage
│    secondary connection (arch, corridor)
─→   directed exit (to next adventure or prior)
```

## Scale note

Approximate dimensions: R2 (Central Nave) ~20×50 ft — the cathedral's largest interior space. R4 (Apse) ~15×20 ft. R3 (North Aisle) ~10×50 ft, running parallel to R2. R6 (Gallery) above R2, ~10×20 ft accessible section.

## Connections Table

| From | To | Type | Condition |
|---|---|---|---|
| 0015 Inner Door | R1 | Open passage | Always; party entered here at end of 0015 |
| R1 | R2 | Open — main nave aisle | Always passable; congregation visible from R1 threshold |
| R1 | R3 | Arch — quiet, north side | Always passable; congregation murmur muffled on entry |
| R2 | R3 | Central arch — midpoint of nave | Always passable |
| R2 | R4 | Open — central aisle continues east | Always passable; cup visible from ~30 ft |
| R2 | R5 | South — stairway base | **Faction-gated:** Gorret challenges here. Opens freely after Nave congregation trusts party OR after Gorret's arc-completion fires. |
| R3 | R4 | Back corridor — narrow, behind the apse | Always passable; DC 12 Perception from R3 to notice the passage; approach from behind rather than directly |
| R5 | R6 | Stairs — ascending | Open once R5 passes; stairway is physically clear |
| R6 | 0017 | East passage — arch to Bell Tower approach | **Campaign lock:** sealed until 0016 resolves; the passage is physically present but blocked by heavy debris the congregation has not cleared (they don't go that way) |

## Congregation Positions at Session Start

*Approximately 25 congregation members in the Nave section. Distributed:*

| NPC/Group | Starting location | Behavior |
|---|---|---|
| **Veth** | R1 threshold | Waiting to meet the party; stationary |
| ~12 congregation members | R2 (morning rite or aftermath) | Moving between rite positions; follow Veth's lead |
| ~6 congregation members | R3 (individual shrines) | Quiet, independent practice; do not approach party unless approached |
| **Gorret** | R5 base (south side near stairs) | Positioned but not blocking; watches party movement |
| 3 recently-arrived members | R4 (imperfect rite practice) | Practicing partial rite; not aware party is present until R4 entered |
| ~4 congregation members | R6 (gallery) | Personal space; startled if party ascends unexpectedly |

*On return visit:* Gorret has moved to R6 if he stepped aside (he is watching from above after allowing ascent). If party was turned away, Gorret remains at R5 and Veth has sent a congregation member to the gatehouse to explain that the party must state their purpose more clearly.
