---
name: encounter-balancer
description: Validate CR/XP budgets for a D&D 5e encounter given a party tier and size. Checks action economy (solos vs. swarms), flags instakill threats, checks for meaningful tactical choices, and produces an encounter-balance report. Use during dungeon-smith or when dungeon-smith flags an encounter as unvalidated. Produces encounters/<slug>-balance.md.
---

# encounter-balancer

Validate and tune D&D 5e encounters. Produces a balance report that confirms the encounter is fair, has action economy worth engaging with, and cannot accidentally end the campaign.

## When to use

- During dungeon-smith, when the DM notes says "needs balance check."
- After dungeon-smith, before adventure-lint, for any encounter in a tier 2+ adventure.
- When a module has a combat encounter that affects a spotlight-PC's arc (the arc cannot end early due to an unfair TPK).

## Preconditions

- Party tier (1–4), party size (number of PCs), and average party level are known.
- Encounter file exists at `encounters/<slug>.md` with stat blocks.
- `reference/srd/monsters-tier<N>.md` is available for XP lookup.

## XP Budgets (5e SRD, per PC)

| Difficulty | Tier 1 (L1-4) | Tier 2 (L5-10) | Tier 3 (L11-16) | Tier 4 (L17-20) |
|---|---|---|---|---|
| Easy | 25–49 | 250–449 | 1000–2000 | 3000–5000 |
| Medium | 50–74 | 450–699 | 2001–3000 | 5001–7500 |
| Hard | 75–149 | 700–1099 | 3001–4500 | 7501–11000 |
| Deadly | 150+ | 1100+ | 4500+ | 11000+ |

Multiply per-PC budget by party size for total party budget.

**XP multiplier by enemy count:**

| Enemies | Multiplier |
|---|---|
| 1 | ×1 |
| 2 | ×1.5 |
| 3–6 | ×2 |
| 7–10 | ×2.5 |
| 11–14 | ×3 |
| 15+ | ×4 |

Adjusted XP = (sum of enemy base XP) × multiplier. Compare to party budget.

## Procedure

### 1. Read the encounter

Read `encounters/<slug>.md`. Extract:
- Each enemy: name, CR, XP, AC, HP, attack bonus, damage (avg per round), save DCs, special abilities.
- Party context: tier, level, size, spell slots available (from party sheet or session prep).

### 2. Calculate adjusted XP

```
base_xp = sum of all enemy XP values
adjusted_xp = base_xp × multiplier(enemy_count)
party_budget = difficulty_xp_per_pc × party_size
```

Classify: Easy / Medium / Hard / Deadly.

### 3. Check instakill threats

An encounter has an instakill threat if any single enemy can:
- Deal damage equal to ≥ 60% of a PC's max HP in one round (average, not max roll).
- Force a save at DC ≥ 15 that results in incapacitation or death on a first fail.
- Apply a condition that removes a PC from combat for ≥ 2 rounds (paralyzed, stunned, unconscious).

Flag instakill threats as **orange** (survivable with tactics) or **red** (likely TPK without intervention).

### 4. Check action economy

Count actions per side per round:
- PCs: each PC contributes 1 action + bonus action + reaction potential.
- Enemies: each enemy contributes 1 action (multiattack counts as 1 action).

**Swarm warning:** If enemy action count > party action count × 1.5, the party is likely overwhelmed by action economy even if XP is Medium. Flag.

**Solo warning:** If there is only 1 enemy, check legendary actions and resistances. A solo without legendaries at Hard difficulty is often anticlimactic. Flag if no legendaries and XP is Hard+.

### 5. Check tactical choices

A good encounter gives PCs meaningful choices beyond "attack the closest enemy":
- [ ] Is there a priority target (the healer, the controller)?
- [ ] Is there an environmental factor (terrain, light, hazard)?
- [ ] Is there a non-combat resolution available (bribe, distract, sneak)?
- [ ] Does the encounter change if the party acts in the first round vs. the third?

Flag encounters where all of the above are "no" — they are attrition checks, not encounters.

### 6. Write the balance report

Output to `encounters/<slug>-balance.md`:

```markdown
---
adventure: <slug>
encounter: <slug>
author: encounter-balancer
created: <today>
party-tier: <N>
party-level: <N>
party-size: <N>
---

# Encounter Balance — <Encounter Name>

## XP Calculation

| Enemy | CR | Base XP | Count |
|---|---|---|---|
| <Name> | <CR> | <XP> | <N> |
| **Total base XP** | | **<N>** | |

- **Enemy count multiplier:** ×<N>
- **Adjusted XP:** <N>
- **Party budget (Hard):** <N>
- **Difficulty classification:** [Easy / Medium / Hard / Deadly]

## Instakill Threats

[ None / Orange / Red ]

<If flagged: name the specific ability, average damage, and which PC archetype is most at risk.>

## Action Economy

- PCs: <N> actions/round
- Enemies: <N> actions/round
- Ratio: <N>:<N>
- Flag: [None / Swarm warning / Solo warning]

## Tactical Choices

- Priority target: [Yes / No]
- Environmental factor: [Yes / No]
- Non-combat resolution: [Yes / No]
- Round-1 vs. round-3 divergence: [Yes / No]

**Assessment:** [Rich / Adequate / Thin] — <one sentence>

## Verdict

[PASS / FLAG / FAIL]

- **PASS:** Difficulty is Medium or Hard; no instakill red flags; at least 2 tactical choices.
- **FLAG:** Encounter runs but has orange instakill or thin tactical choices — note in GM Notes.
- **FAIL:** Deadly without justification; red instakill flag; or 0 tactical choices.

## Recommended adjustments (if FLAG or FAIL)

<Specific changes: reduce HP, add legendary saves, remove one enemy, add a terrain feature.>
Prioritize the smallest change that moves the verdict to PASS.
```

### 7. Update the encounter file

If adjustments are recommended and user approves:
- Edit `encounters/<slug>.md` stat blocks with the changes.
- Note the adjustment in the encounter file's GM Notes: "Balance-adjusted: [what changed]."

### 8. Never overwrite silently

If `<slug>-balance.md` exists, write `<slug>-balance.v2.md`.

## Quality gates

- [ ] XP calculation is correct (check multiplier vs. enemy count).
- [ ] Instakill check ran against the party's lowest-HP PC.
- [ ] Action economy check ran.
- [ ] At least one tactical choice documented (or "Thin" flag raised).
- [ ] Verdict is one of PASS / FLAG / FAIL — not "it's fine."

## Integration with dungeon-smith

dungeon-smith quality gates include "Proper encounter count ≥ ⌈room_count / 2⌉." encounter-balancer validates the *quality* of those encounters, not just the count. A dungeon can pass the dungeon-smith encounter-count gate and still fail encounter-balancer if every encounter is a Deadly solo with no tactical choices.

## Anti-patterns

- Calculating XP without the multiplier.
- Flagging Deadly encounters in a finale as "fail" — they may be intentional.
- Ignoring legendary actions when evaluating solo encounters.
- Approving encounters with 0 tactical choices as "adequate."
- Skipping the balance report and just adjusting numbers (the report is the audit trail).
