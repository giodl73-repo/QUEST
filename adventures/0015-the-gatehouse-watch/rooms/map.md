---
adventure: 0015-the-gatehouse-watch
document: map
author: dungeon-smith
created: 2026-04-21
---

# Map — The Gatehouse Watch

## ASCII Map

```
                                      ╔═══════════╗
                                      ║  R4       ║  UPPER LEVEL
                                      ║ WALL-WALK ║
                                      ╚═══╦═══╦══╝
                              (stairs)    ║   ║ (rope ladder — conditional)
                                          ║   ║
[EXT]══[R1: GATE PASSAGE]══[R2: GUARDROOM]╣   ║   [R5: CHAPEL]══[R6: INNER DOOR]══>[NAVE]
            ║                    ║        ╚═══╝       ╔═══╝
        (low arch,              (grate/              (arch,
         duck to enter)         crawlspace)           open)
            ║                    ║
            ╚══[R3: COLLAPSED]═══╝
                     ║
                  [EXTERNAL — collapsed wall entry]
```

**North is toward the Nave (east in the cathedral's actual orientation; "N" on this map = deeper into the building).**

## Legend

```
══  open passage or doorway
╦╣  stair connection (vertical)
║   secondary connection (arch, crawl, ladder)
>   one-way exit (sealed for this adventure)
[ ] keyed room
```

## Scale note

Each room represents a distinct structural section of the gatehouse. Room dimensions are approximate; the guardroom is the largest (~30 × 20 ft), the gate passage is a corridor (~10 × 20 ft), the collapsed section is irregular (~15 × 15 ft usable).

## Connections Table

| From | To | Direction | Type | Condition |
|---|---|---|---|---|
| External | R1 | W→E | Open gate, portcullis raised | Always open at session start; lowering portcullis (R1 winch) closes it |
| R1 | R2 | E | Open passage | Always passable |
| R1 | R3 | S | Low stone arch (duck to enter — 4 ft clearance) | Always passable; requires crouching; easy to miss (Perception DC 12 to notice from R1) |
| R2 | R3 | Floor | Iron grate, floor-level crawlspace | Accessible from either side; narrow (Medium creatures squeeze, disadvantage on attacks); rat swarm lair |
| R2 | R4 | Up | Stone stairs, no door | Always passable |
| R2 | R5 | E | Open archway (door frame present, no door installed) | Always passable |
| R3 | External | S | Collapsed outer wall, rubble gap | Always passable; the congregation's primary entrance |
| R4 | R3 | Down | Rope ladder, south parapet | **Conditional:** Torva shows it only after party demonstrates peaceful intent; otherwise requires DC 15 Athletics to spot and descend safely |
| R5 | R6 | E | Heavy oak inner door | **Double-locked:** (1) door frame bolts released by portcullis winch in R1; (2) wooden bar from congregation. Both must be cleared to open. |
| R6 | Nave | E | Sealed passage | **Campaign lock:** sealed for adventure 0015; leads to adventure 0016 |

## Congregation Starting Positions

*At session start, before the party enters:*

| NPC | Location | Patrol |
|---|---|---|
| Mig | R2 (near south wall, satchel in hand) | Stationary |
| Grisk | R3 (lookout, watching the collapsed wall approach) | Moves to R2 when party enters R1 |
| Torva | R2 (near stairs, watching the interior) | Moves to R4 if party is large or aggressive |
| 4 unnamed congregation members | R2 (distributed) | Stationary; follow Mig's lead |

*Congregation behavior changes on return visit:* If the party leaves and comes back, Grisk will be watching from R4 (wall-walk) rather than R3. He has moved his lookout higher after the first contact.
