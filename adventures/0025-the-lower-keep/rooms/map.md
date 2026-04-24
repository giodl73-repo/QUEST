---
adventure: 0025-the-lower-keep
document: map
author: dungeon-smith
created: 2026-04-22
---

# Thorngate Keep — Inner Gate and Lower Keep (Map)

## ASCII Map

```
        NORTHEAST (RECONSTITUTION ASSAULT APPROACH)
                       ↑
    ══════════════════════════════════════════════
    ║  CLIFF FACE                     CLIFF FACE ║
    ║                                            ║
    ║                                            ║
    ║   [01]INNER GATEHOUSE ←── assault approach ║
    ║       │  (outer gate approach;             ║
    ║       │   battering frame target)          ║
    ║       │                                    ║
    ║   [02]THE HALL BREACH                      ║
    ║       │  (garrison scramble;               ║
    ║       │   combat floor)                    ║
    ║       │                                    ║
    ║       ├──────────────────────────[03]       ║
    ║       │                       MAINTENANCE  ║
    ║       │                       DOOR          ║
    ║       │                       (lower east  ║
    ║       │                        wall)        ║
    ║       │                                    ║
    ║   GREAT HALL ──── [05]DENE'S             ║
    ║   (shared)         SUPPLY ALCOVE           ║
    ║       │             (north off hall)        ║
    ║       │                    │               ║
    ║       └──────── [04]FIRST CHAMBER ─────────╯
    ║                 (refugee space;            ║
    ║                  lower east chambers)      ║
    ║                                            ║
    ══════════════════════════════════════════════
                   ↓
           NEEDLE PASS (SAFE SIDE)
```

## Lower Keep Specific Layout

```
    VERTICAL SECTION (lower keep, looking inward from gate)

    [01] INNER GATEHOUSE APPROACH  ← outer face (assault target)
         │  ground level, gate arch, portcullis mechanism
         ↓ passage inward (20 ft corridor)
    [02] HALL BREACH
         │  main garrison hall, ground level
         │  assault spills here if outer gate fails
         │
         ├──── east passage (30 ft) ──── [03] MAINTENANCE DOOR
         │                               (lower east wall alcove;
         │                                "maintenance" sign, plank door)
         │
         ├──── north passage ──── [05] DENE'S SUPPLY ALCOVE
         │                        (locked; ledger inside)
         │
         └──── east descent (6 steps) ──── [04] FIRST CHAMBER
                                            (refugee space; hearth,
                                             pallets, stored food)
```

## Legend

| Symbol | Meaning |
|---|---|
| `[NN]` | Keyed location |
| `─` / `│` | Passage / connection |
| `├` `└` | Branch connection |
| `↓` / `↑` | Vertical change (minor; 6 steps) |
| `════` | Keep wall / cliff face |
| `←──` | Direction of assault approach |

## Connections Table

| From | To | Type | Condition |
|---|---|---|---|
| 01 Inner Gatehouse | 02 Hall Breach | Passage (20 ft corridor) | Gate arch; open during assault |
| 01 Inner Gatehouse | Outside | Gate arch / portcullis | Portcullis can be dropped; DC 14 Athletics to hold open |
| 02 Hall Breach | 01 Inner Gatehouse | Passage north | Open |
| 02 Hall Breach | 03 Maintenance Door | East passage (30 ft) | Door labeled "maintenance"; plank, normally locked |
| 02 Hall Breach | 04 First Chamber | East descent (6 steps) | After door opens; previously blocked |
| 02 Hall Breach | 05 Dene's Supply Alcove | North passage | Iron-banded door; Dene has the key |
| 02 Hall Breach | Great Hall (0022-03) | Door south | Open; standard garrison transit |
| 03 Maintenance Door | 02 Hall Breach | East passage (return) | Open once opened |
| 03 Maintenance Door | 04 First Chamber | Connects directly | Door opens to reveal steps down |
| 04 First Chamber | 03 Maintenance Door | 6 steps up | Open once door opens |
| 04 First Chamber | 05 Dene's Supply Alcove | Connecting passage | Dene uses this; locked from alcove side |
| 05 Dene's Supply Alcove | 04 First Chamber | Connecting passage | Dene opens this; ledger visible |

## Loop

02 Hall Breach → 03 Maintenance Door → 04 First Chamber → 05 Dene's Supply Alcove → 02 Hall Breach (via north passage)

## Vertical connections

- Hall Breach (02) **down 6 steps** to First Chamber (04) after the maintenance door opens
- The descent is minor but meaningful: the refugee chambers are slightly below the main garrison floor

## Scale

One square ≈ 10 feet. Inner Gatehouse approach corridor is 15 feet wide (battering frame can fit). Hall Breach is 30 × 25 feet (combat space; pillars at north and south ends). Maintenance door passage is 30 feet long, 8 feet wide. First Chamber is 40 × 20 feet (47 people; tight but viable). Supply Alcove is 10 × 8 feet.

## DM notes

**Combat terrain (Rooms 01–02):** The gatehouse approach is the assault choke point. Pillars in the Hall Breach provide partial cover. The portcullis mechanism in Room 01 is a tactical option — dropping it costs an action and requires DC 14 Athletics. The party's goal is to break the assault before the battering frame reaches the outer gate face.

**The door geometry:** Room 03's door faces the Hall Breach from the east passage. It is visible from the south end of Room 02 during combat — the party will see it if they look east during the fight. It opens while the fight is ongoing (Round 3 or later, when the assault noise is loudest). The girl's face appears in the doorframe during a lull or break in combat action.

**Refugee chamber access:** Room 04 connects to Room 05 via Dene's passage. The party can find the ledger in Room 05 without going through Room 04, but finding it through Dene (Room 04 → 05 with him) is the designed path.
