---
adventure: 0024-the-saboteur
document: map
author: dungeon-smith
created: 2026-04-22
---

# Thorngate Keep — West Wall (Map)

## ASCII Map

```
        NORTHEAST (RECONSTITUTION SIEGE LINES)
                       ↑
    ══════════════════════════════════════════════
    ║  CLIFF FACE                     CLIFF FACE ║
    ║                                            ║
    ║                         [07]NORTH TOWER   ║
    ║                              │ ↑stairs    ║
    ║           [04]WEST WALL──────┤            ║
    ║           UPPER LEDGE        │            ║
    ║           (battlements,   [06]ARROW-WALK  ║
    ║            escape ledge)     │            ║
    ║              ↑stairs      [08]SOUTH TOWER ║
    ║              │               │            ║
    ║           [02]WEST WALL   [05]EAST WALL   ║
    ║           WALK               WALK         ║
    ║           (investigation   (battlements)  ║
    ║            trail, fungal                  ║
    ║            compound)                      ║
    ║              │               │            ║
    ║              ╰───────────────╯            ║
    ║                     │                     ║
    ║              [03]GARRISON QUARTERS        ║
    ║              (Wil's bunk; evidence)       ║
    ║                     │                     ║
    ║              [02]GATEHOUSE ───────────────╯
    ║              (passage through wall)        ║
    ║                     │                     ║
    ║              [03]GREAT HALL               ║
    ║              (main garrison space)        ║
    ║                     │                     ║
    ║  [01]WEST WALL BASE ╯                     ║
    ║  (arrow cache, postern night log)         ║
    ║                     │                     ║
    ══════════════════════════════════════════════
                   ↓
           NEEDLE PASS (SAFE SIDE)
```

**Note on map layout:** Rooms 01–04 are west-wall specific locations. Rooms 02 (Gatehouse), 03 (Great Hall), 05 (East Wall Walk), 06 (Arrow-Walk), 07 (North Tower), 08 (South Tower) are shared Thorngate Keep geography from adventure 0022. The west wall adds four new keyed positions along and above the west-facing wall section not previously keyed.

## West Wall Specific Layout

```
    WALL SECTION (west face, looking inward)

    [04] WEST WALL UPPER LEDGE  ←──── escape ledge (exterior)
         ↕ stairs (DC 12 Athletics; or iron ring ladder)
    [02] WEST WALL WALK
         (middle tier, patrol path)
         ↕ postern stairs (internal)
    [01] WEST WALL BASE
         (ground level; arrow cache alcove; postern night log lectern)

    [03] GARRISON QUARTERS (west wing, off Great Hall, ground level)
         connects via door to [01] and to Great Hall
```

## Legend

| Symbol | Meaning |
|---|---|
| `[NN]` | Keyed location |
| `─` / `│` | Passage / connection |
| `╰` `╮` | Corner connection |
| `↑stairs` / `↕` | Vertical connection |
| `════` | Keep wall / cliff face |

## Connections Table

| From | To | Type | Condition |
|---|---|---|---|
| 01 West Wall Base | 03 Garrison Quarters | Door (plank, west wing) | Unlocked during day; Wil's quarters visible from here |
| 01 West Wall Base | 02 West Wall Walk | Postern stairs (internal) | Open; stone steps, single file |
| 01 West Wall Base | Great Hall (0022-03) | Door (stone arch) | Open; standard garrison transit |
| 02 West Wall Walk | 01 West Wall Base | Postern stairs (down) | Open |
| 02 West Wall Walk | 04 West Wall Upper Ledge | Iron ring ladder + stone steps | Open; **DC 12 Athletics to ascend quickly** |
| 02 West Wall Walk | East Wall Walk (0022-05) | Battlement passage (traverse) | Open; exposed on north face |
| 03 Garrison Quarters | 01 West Wall Base | Door (west) | Open during day |
| 03 Garrison Quarters | Great Hall (0022-03) | Door (east) | Open |
| 04 West Wall Upper Ledge | 02 West Wall Walk | Iron ring ladder + steps (down) | Open |
| 04 West Wall Upper Ledge | Arrow-Walk (0022-06) | Battlement traverse (east) | Open; lateral connection at height |

## Two paths to Room 04 (West Wall Upper Ledge)

- **Path A (west wall direct):** 01 West Wall Base → 02 West Wall Walk → 04 West Wall Upper Ledge
- **Path B (interior–east traverse):** Great Hall (0022-03) → 02 Gatehouse → East Wall Walk (0022-05) → Arrow-Walk (0022-06) → 04 West Wall Upper Ledge (battlement traverse)

## Loop

02 West Wall Walk → 04 West Wall Upper Ledge → Arrow-Walk (0022-06) → East Wall Walk (0022-05) → 02 West Wall Walk

## Vertical connections

- West Wall Base (01) **up** to West Wall Walk (02) via postern stairs
- West Wall Walk (02) **up** to West Wall Upper Ledge (04) via iron ring ladder + steps
- Upper Ledge (04) **lateral** at height to Arrow-Walk (0022-06)

## Scale

One square ≈ 10 feet. West Wall Base alcove is approximately 15 × 20 feet (arrow cache occupies the north half). West Wall Walk is 40 feet long (battlements, west-facing). Upper Ledge is a 10-foot-wide patrol ledge above the outer face — exposed on the west side. Garrison Quarters (west wing) is 20 × 15 feet: eight bunks, personal gear.

## DM notes

The west wall positions are investigation terrain during Scenes 1–2 and combat terrain during Scene 3. The two-path design means the party can split: send Talis up the wall direct while Davan circles via interior. Room 03 (Garrison Quarters) is a deliberate dead-end — you enter, you search, you exit the same way. The loop runs above it.

**Wil's field of view from Room 04:** The upper ledge faces west and northwest. Wil can see anyone approaching via Path A (west wall direct) from Room 02 upward. He cannot see Path B (interior traverse) until the party is already at the Arrow-Walk. Path B gives the party an approach without Wil seeing them coming — relevant if the party wants to close the escape route before the confrontation.
