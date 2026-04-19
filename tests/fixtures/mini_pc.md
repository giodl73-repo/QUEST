---
party: test-party
pc: test-fighter
class: fighter
level: 3
heuristics:
  doubt_die:
    "1-3": "attack"
    "4-6": "defend"
  decision_order:
    - key: survival
      condition: "any_pc_below_half_hp"
    - key: offense
      condition: "always"
  signature_moves:
    - id: "power-attack"
      trigger: "always"
      mechanical_effect: null
  voice_tags:
    - "terse"
---

# Test Fighter

## Stat Block

**AC** 16 (chain mail)  ·  **HP** 28  ·  **Speed** 30 ft.

| Str | Dex | Con | Int | Wis | Cha |
|---|---|---|---|---|---|
| 16 | 12 | 14 | 10 | 12 | 10 |

**Saves (proficient):** Strength +5, Constitution +4
**Skills (proficient):** Athletics +5, Perception +3
**Senses:** passive Perception 13
**Languages:** Common
**Equipment:** chain mail, longsword, shield, 15 gp

**Attunement slots:** 3 (empty)

**Proficiency:** +2. **Initiative:** +1.
