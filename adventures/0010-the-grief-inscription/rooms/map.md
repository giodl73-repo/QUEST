---
adventure: 0010-the-grief-inscription
author: dungeon-smith
created: 2026-04-20
---

# Map — The Grief Inscription

## Topology

The adventure moves from road to chapel. The chapel is a single-building location with interior and exterior elements. The ruins behind the chapel provide an alternate entry and a fallback position.

```
ROAD ENCOUNTER (non-optional, before arrival)
        |
        v
[01 CHAPEL APPROACH] ←—— back ruins path ——→ [05 CHAPEL RUINS (optional)]
        |                                            |
        v                                            |
[02 CHAPEL EXTERIOR]                                 |
        |                 ←————————————————————————→|
        v
[03 CHAPEL INTERIOR — where Lenne holds the shard]
        |
        v
[04 THE SANCTUARY — Morreth + stone box + arc-completion]
```

**Loop:** Chapel approach (01) → exterior (02) → interior (03) → ruins (05) → back to approach (01). The party can circle the chapel.

**Vertical:** None — single-story ruin. The partially collapsed roof provides a high point: Sera can reach a wall-top (Athletics DC 10) for a sniper position during any combat at the chapel.

**Two paths to the shard:** Front (01 → 02 → 03 → 04) or ruins bypass (01 → 05 → 04 via the collapsed east wall). The ruins path is stealth-viable (Stealth DC 12 to approach 05 without Morreth noticing); it reaches the sanctuary from the back.

**Shortcut:** If Morreth trusts the party (chapel exterior goes well), he escorts them directly to the sanctuary (03 skipped).

## Connections table

| Room | Connects to | Notes |
|---|---|---|
| Road | Chapel approach | Non-optional combat |
| 01 Approach | 02 Exterior; 05 Ruins (path around east wall) | Two entry paths |
| 02 Exterior | 01 Approach; 03 Interior (main door, unlatched) | Morreth works here sometimes |
| 03 Interior | 02 Exterior; 04 Sanctuary (short corridor) | Where Lenne holds the shard |
| 04 Sanctuary | 03 Interior; 05 Ruins (collapsed east wall) | Stone box location; arc-completion |
| 05 Ruins | 01 Approach; 04 Sanctuary (collapsed wall) | Optional; stealth path; Sera's high ground |
