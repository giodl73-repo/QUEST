---
adventure: 0001-tomb-of-the-silver-rose
tier: 1
author: dungeon-smith
created: 2026-04-18
sources:
  - adventures/0001-tomb-of-the-silver-rose/premise.md
---

# Map — The Rose Cairn

Two levels. Cairn-cap (Level 0, surface barrow) and Tomb (Level -1, cut into the bluff below).

Scale: 1 square ≈ 10 ft.

## Legend

```
[N]     keyed room (N = room number)
=       door (unlocked unless noted)
=?=     secret / sealed door
||      stone wall
--      open passage / archway
/  \    stair (direction indicated)
*       shaft / vertical connection
~       weathered, wind-worn
#       cairn-stone / rubble
```

## Level 0 — Cairn-Cap (Surface)

```
                 (wind / open plain)

                    ~~~~~~~~
                    ~[1]~~~~        Room 1 — The Cairn-Cap
                    ~ # # ~         (weather-scoured, rose carving)
                    ~ | | ~
                      / \
                      \ /           stair down to Level -1
                       |

                 (descent ≈ 15 ft into the bluff)
```

## Level -1 — Tomb

```
                       |                    (stair from 1 arrives here)
                       v
                  +---[2]---+                Room 2 — Antechamber of Tears
                  |         |                (atmospheric; weeping wall; bowl)
                  |  = = =  |
                  |  W   E  |
                  +--|-+-|--+
                     | | |
             +-------+ | +-------+
             |         |         |
          +-[4]-+   (walls)   +-[3]-+       Room 3 — Pillar Hall (east)
          | LEC |             | PIL |       Room 4 — Scriptorium (west)
          | TER |             | LAR |
          |  *  |             |     |
          | (shaft  = = = = = (stair
          |  down               down
          |  to 5   ====?====    to 5)
          |  sealed             |
          |  until              |
          |  puzzle)            |
          +-|---+             +-|---+
            |                   |
            v  (shaft)          v  (stair)
            |                   |
            +----+     +--------+
                 |     |
                +-[5]-+                     Room 5 — The Rose Stair
                |     |                     (both descents land here)
                | === |
                +--|--+
                   |
                   v
                +-[6]-----+                 Room 6 — The Sarcophagus Chamber
                |         |                 (octagonal; Ilendra's rest; the Rose)
                |   SRC   |
                |         |
                +---------+
```

## Connections Table

| From | To | Type | Notes |
|---|---|---|---|
| 1 | 2 | Stair (down, ~15 ft) | Capstone Athletics DC 13 to lever aside |
| 2 | 3 | Open archway (east) | — |
| 2 | 4 | Open archway (west) | — |
| 3 | 5 | Stair (down, ~10 ft) | — |
| 4 | 5 | Shaft (down, ~10 ft) | Sealed; opens when ≥2 of 3 books are read (or DC 17 Arcana / DC 15 Religion) |
| 5 | 6 | Door (unlocked) | Inscription above lintel: *Est Sularus oth Mithas* |

## Topology Summary

- **6 rooms.**
- **Loop:** 2 → 3 → 5 → 4 → 2 (fully connected once the shaft in 4 opens).
- **Vertical element:** 2 stair-descents (1→2 and 3→5) plus the shaft (4→5).
- **Two paths to the artifact (Room 6):** via the fight (Room 3) OR via the puzzle (Room 4).
- **Shortcut that unlocks:** the shaft in Room 4 becomes a fast-descent shortcut after the Scriptorium puzzle is solved — a party that does Room 4 thoroughly bypasses Room 3's combat.
- **Atmospheric (Stuart) room:** Room 2.
- **Multi-solution (Jaquays) room:** Room 4.

## Notes for the DM

The cairn predates the Cataclysm. It is still pre-Cataclysm at the time the party enters. The weather outside is cold mid-spring, winds across the plain.

The party will almost certainly take the stair route (Room 1 → 2 → 3 → 5 → 6) on first descent and may never discover Room 4 at all. **That is fine.** Room 4 is designed as the return-trip shortcut *or* as a puzzle for a careful party. Do not railroad them into the Scriptorium.
