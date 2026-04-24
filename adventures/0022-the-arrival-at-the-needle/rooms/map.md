---
adventure: 0022-the-arrival-at-the-needle
document: map
author: dungeon-smith
created: 2026-04-21
---

# Thorngate Keep — Map

## ASCII Map

```
        NORTHEAST (RECONSTITUTION SIEGE LINES)
                       ↑
    ══════════════════════════════════════
    ║  CLIFF FACE                        ║  CLIFF FACE
    ║                                    ║
    ║  [07]NORTH TOWER    [08]SOUTH TOWER║
    ║       │  ↑stairs        │  ↑stairs ║
    ║       │  [06]ARROW─WALK─╯          ║
    ║       │  (high; both towers)       ║
    ║       ╰──────────────────╮         ║
    ║  [05] EAST WALL WALK     │         ║
    ║  (outer face; battlements)│        ║
    ║       │                  │         ║
    ║       ╰──────┬───────────╯         ║
    ║         [02] GATEHOUSE             ║
    ║         (passage through wall)     ║
    ║              │                     ║
    ║         [03] GREAT HALL            ║
    ║         (main garrison space)      ║
    ║              │ stairs↓             ║
    ║         [04] LOWER LEVEL DOOR      ║
    ║         (locked; sounds below)     ║
    ║                                    ║
    ║  [01] POSTERN GATE                 ║
    ║  (side entry; safe side)           ║
    ║              │                     ║
    ══════════════════════════════════════
           ↓
    NEEDLE PASS (SAFE SIDE / INTERIOR)
```

## Legend

| Symbol | Meaning |
|---|---|
| `[NN]` | Keyed location |
| `─` / `│` | Passage / connection |
| `╰` `╮` | Corner connection |
| `↑stairs` | Vertical connection (up) |
| `stairs↓` | Vertical connection (down) |
| `════` | Keep wall / cliff face |

## Connections Table

| From | To | Type | Condition |
|---|---|---|---|
| 01 Postern Gate | 03 Great Hall | Door (iron-bound) | Unlocked; garrison watches |
| 01 Postern Gate | 05 East Wall Walk | Exterior stairs (stone) | Open; exposed to NE during day |
| 02 Gatehouse | 03 Great Hall | Door | Open |
| 02 Gatehouse | 05 East Wall Walk | Battlement stairs | Open |
| 03 Great Hall | 04 Lower Level Door | Stairs down | **Locked** (iron bar; DC 18 Str to force; DC 15 Thieves' Tools; Asholt has the key) |
| 03 Great Hall | 02 Gatehouse | Door | Open |
| 03 Great Hall | 08 South Tower (ground) | Door | Open |
| 05 East Wall Walk | 06 Arrow-Walk | Stairs up (north end) | Open |
| 05 East Wall Walk | 06 Arrow-Walk | Stairs up (south end) | Open |
| 06 Arrow-Walk | 07 North Tower | Tower door | **Closed** (convention, not locked; Asholt's quarters; party unwelcome) |
| 06 Arrow-Walk | 08 South Tower | Tower door | Open |
| 08 South Tower | 03 Great Hall | Internal stairs | Open |

## Two paths to the east wall

- **Path A (direct):** 01 Postern Gate → exterior stairs → 05 East Wall Walk
- **Path B (interior):** 01 Postern Gate → 03 Great Hall → 02 Gatehouse → battlement stairs → 05 East Wall Walk

## Loop

05 East Wall Walk → 06 Arrow-Walk → 08 South Tower → 03 Great Hall → 02 Gatehouse → 05 East Wall Walk

## Vertical connections

- Great Hall (03) **down** to Lower Level Door (04) — locked
- East Wall Walk (05) **up** to Arrow-Walk (06) via two stair points
- Arrow-Walk (06) **lateral** at height between 07 and 08

## Shortcut (unlocks through play)

The North Tower (07) door is closed by convention. If Asholt gives the party full trust (final token), this door is opened and the tower's commanding view of the siege lines becomes available — granting Advantage on Perception checks to read Reconstitution troop movements for all future sessions.

## Scale

One square ≈ 10 feet. The East Wall Walk is approximately 60 feet wide (battlement to battlement). The Arrow-Walk is 15 feet above the Wall Walk. The Great Hall is 40 × 30 feet. The Lower Level is unknown dimensions (not keyed this session).

## DM notes

The fortress does not have conventional dungeon rooms — it has positions. Movement between positions during the night assault takes 1 round per connection traversed (e.g., moving from Great Hall to East Wall Walk via Path B costs 2 rounds of movement). This creates meaningful positioning decisions during the assault.
