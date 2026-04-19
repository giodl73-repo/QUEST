---
adventure: 0004-the-wrath-coin
tier: 1
author: dungeon-smith
created: 2026-04-19
campaign: moon-silver-cycle
---

# Map — The Wrath-Coin

Three-zone adventure: **Kharolis road** (Scene 1) → **Gavrek's Anvil shrine + east slope** (Scenes 2-4) → **Lower Ore-Shaft** (Scene 5) → **Kruntharrak mine-hold** (Scene 6) → **back to shrine** (Scene 7).

## Legend

```
[N]     keyed scene
=       door
=L=     locked door
||      wall
/  \    stair (up)
\  /    stair (down)
~       path / road
#       building / structure
+       crossroads
*       trapdoor / shaft-head
```

## Regional Map (zoomed out)

```
              (Varduin, 7 days NE)
                       |
                       ~
                       |
                    [1] Road ambush
                       |
                       ~
                       |
            +---Gavrek's Anvil---+
            |   (shrine + forge) |
            |   [2][3][4]        |
            +---------+----------+
                      |
                (east slope ~3 hrs)
                      |
                   [6] Kruntharrak
                       (Krun's mine-hold)
```

## Gavrek's Anvil (Shrine + Grave + Shaft)

```
                  ~~ road from north
                       |
              +--------+--------+
              |   [2] Courtyard |
              |   (well + gate) |
              +----+--------+---+
                   |        |
               (shrine)  (forge-hall)
                  #         #
                  ||        ||
              +---+---+ +---+---+
              | Nave  | | Forge |
              +---+---+ +---+---+
                  |        |
                  +---+----+
                      |
                (east slope path)
                      |
                    [3] Duren's grave
                    (on the slope)
                      |
                (slope continues down)
                      |
                     \ /
                   [5] Lower Ore-Shaft
                   (mine entrance + descent)
```

**[4] Forge-records archive** is inside the forge-hall building (accessed via Scene 2 or Scene 3 backtrack).

## Kruntharrak (Krun's mine-hold)

```
                         (road from shrine, ~3 hrs east)
                              |
                     +--------+--------+
                     |   Gate (wardens) |
                     +--------+--------+
                              |
                     +--------+--------+
                     |   Outer Hall    |
                     |  (servants)     |
                     +----+---------+--+
                          |         |
              (guard barracks)    (council room)
                     #                   #
                     ||                  ||
                          +--------+
                          |
                     +---[6]--+
                     | Krun's |
                     |  Hall   |
                     |(vault)  |
                     +--------+
```

## Connections Table

| From | To | Type | Notes |
|---|---|---|---|
| (road north) | [1] | Road | Kharolis-road ambush point |
| [1] | [2] Shrine courtyard | Walk | ~6 hrs after ambush |
| [2] | Shrine-nave | Door | Open daily |
| [2] | Forge-hall | Door | Door stays open; smoke |
| Forge-hall | [4] Forge archive | Locked door (Sigga's key) | Investigation DC 13 w/o key |
| [2] | [3] Grave slope | Trail | ~5 min walk |
| [3] | [5] Lower Ore-Shaft | Trail down | ~15 min descent path |
| [5] Shaft entrance | Shaft-floor | Descent (rope or stair) | 120 ft down |
| Shrine | [6] Kruntharrak | Road east | ~3 hrs |
| [6] gate | Outer Hall | Wardens | 4 guards |
| Outer Hall | Krun's Hall | Archway | Jarek's post |
| [6] | [7] back to shrine | Return | Post-confrontation |

## Scene → location mapping

| Scene | Location | Notes |
|---|---|---|
| 01 Road Ambush | [1] Kharolis road | Conditional combat with Jarek's ambush |
| 02 Gavrek's Anvil Arrival | [2] Courtyard + shrine-nave + forge-hall | Meeting Sigga; Krun's visit |
| 03 Duren's Grave / Reorx-rite | [3] East slope | Hint 2 unlock + Hint 3 plant |
| 04 Forge Records | [4] Forge archive | Krun's commissions; Aelwen fragment |
| 05 Lower Ore-Shaft | [5] Mine descent | Murder evidence |
| 06 Thane Krun's Hall | [6] Kruntharrak | Coin + Krun decision |
| 07 Aftermath | [2] back at shrine | Duren's re-interment; Sigga's confession |

## Topology Summary

- **7 keyed scenes across 5 locations** (the Anvil cluster hosts Scenes 2, 3, 4 + returns at 7).
- **Loop:** shrine ↔ grave ↔ shaft, with Kruntharrak a spur.
- **Vertical:** Lower Ore-Shaft 120 ft descent; Duren's grave at mid-slope; shrine at slope-top.
- **Branches:**
  - Scene 1 can be skipped if party arrives late at night or takes alternate route (Deception DC 14 to divert).
  - Scene 4 (archive) can be done before OR after Scene 3 (rite); order depends on party priority. Both before Scene 5.
  - Scene 5 (shaft) can be skipped if party already knows about the murder (Jarek surrenders in Scene 1 or Scene 6 with kinship pressure).
- **Stealth path to [6]:** approach Kruntharrak at night; Stealth DC 15 avoids gate-wardens; enters via service-door into outer-hall. Thera can scout.

## DM notes

- **Gavrek's Anvil is a real shrine, not a dungeon.** Named priests + a forge + a nave + a graveyard on the slope. Multiple NPCs present: Sigga; a young ordained priest named **Vell** (non-combatant, background flavor); two traveling pilgrim dwarves unrelated to plot.
- **Kruntharrak is a functioning mine-hold.** Krun has ~20 retainers (household staff + 8 guards + 4 wardens). Full assault is possible but complicated; diplomatic approach is preferred.
- **The Lower Ore-Shaft is not currently operational.** Closed "for safety" after Duren's death. Nobody has been down in three years. Jarek visits monthly to make sure nothing has surfaced.
- **Rubric v1.3 positional-redundancy:** the manifest symptoms (coin weight, rage-glyph cool, Aelwen fragment) have multi-scene placement per v1.3 requirement. See `treasures/wrath-coin-manifest.md`.
