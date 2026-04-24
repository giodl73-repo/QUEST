---
adventure: 0035-the-final-job
document: map
author: dungeon-smith
created: 2026-04-21
---

# Pale's Operations Building — Map

## ASCII Map

```
        MERCHANT QUARTER (STREET)
              ↓
    ══════════════════════════════
    ║  [01] SHIPPING CONCERN      ║   Ground floor — public facade
    ║  (closed overnight)         ║
    ║         │ counting-room     ║
    ║         │ corridor          ║
    ══════════════════════════════
              │
    ══════════════════════════════
    ║  [02] COUNTING-ROOM         ║   Adjacent to service stair
    ║  CORRIDOR                   ║
    ║  (guard rotation 25 min)    ║
    ║         │ service stair↓    ║
    ══════════════════════════════
              ↓
    ══════════════════════════════
    ║  [03] VAULT CORRIDOR        ║   Sub-level; no windows
    ║  (service stair arrives)    ║
    ════════════════════════════════
    ║  [04] VAULT DOOR            ║   DC 15 (Darro: DC 11)
    ══════════════════════════════
    ║  [05] VAULT INTERIOR        ║   Dossiers by operation code
    ║  (shelves; lockbox)         ║   Party's file + RI correspondence
    ══════════════════════════════

        ALLEY (WEST FACE)
    ══════════════════════════════
    ║  [00] ALLEY DOOR            ║   DC 12 (Darro DC 8) — entry point
    ══════════════════════════════
```

## Connections Table

| From | To | Type | Condition |
|---|---|---|---|
| Alley | 00 Alley Door | Service entry | **DC 12** Thieves' Tools (Darro DC 8) |
| 00 Alley Door | 02 Counting-room Corridor | Service stair | Direct access; bypass ground floor |
| 02 Corridor | 03 Vault Corridor | Service stair down | Open; 15 ft descent |
| 03 Vault Corridor | 04 Vault Door | Direct | **DC 15** Thieves' Tools (Darro DC 11) |
| 04 Vault Door | 05 Vault Interior | Open once unlocked | Dossiers on shelves |

## Two paths out

- **Path A (clean):** Vault → Vault Corridor → Service Stair → Counting-room Corridor → Alley Door → Street
- **Path B (alternate):** If guard is at far end of corridor on return, Darro takes lower service corridor to street-level drain exit (DC 12 Athletics to squeeze; alternative if corridor is blocked)

## Noise economy

- Alley door (lockpicked): no noise
- Vault door (lockpicked): no noise (Darro's expertise)
- Vault interior movement: no noise if careful (Stealth DC 8 in vault — very quiet environment)
- Route E (incendiary): immediate noise; smoke visible in 4 minutes

## Guard rotation (25-minute circuit)

The guard walks: Corridor → Far Office → Back Corridor → Vault Corridor → Return to Corridor. Full circuit: 25 minutes. Optimal entry: immediately after guard passes the vault corridor heading toward the far office. Party has ~20 minutes in the sub-level.

## DM notes

The vault infiltration is Darro's dungeon — it is physically straightforward (his Thieves' Tools expertise reduces every lock to manageable DC) and the complexity is temporal (the guard circuit). The vault interior rewards Investigation briefly (the dossiers are organizational evidence) but the party should not linger. In and out is the professional standard.
