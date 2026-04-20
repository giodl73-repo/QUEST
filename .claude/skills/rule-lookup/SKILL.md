---
name: rule-lookup
description: Fast SRD reference during session play or adventure design. Given a rule keyword, condition, mechanic, or spell name, returns the exact 5e text inlined (not linked), plus any Dragonlance-specific modifications. Used by session-runner when a rule question arises mid-scene. Never halts the session — returns the rule and continues.
---

# rule-lookup

Fast, inline rule resolution. The session does not stop for a rule lookup — this skill runs, returns the answer, and the session continues.

## When to use

- During session-runner's PLAY stage when a rule question arises.
- During encounter-balancer when a special ability's mechanics need confirmation.
- During dungeon-smith when a trap or hazard needs accurate DC/damage reference.
- During module-binder when the DM Cheatsheet needs SRD text inlined.

**Never** during a social/narrative scene — if no dice are being rolled, no rule lookup is needed.

## Preconditions

- `reference/srd/` exists with at minimum: `conditions.md`, `combat.md`, `spells-tier<N>.md`, `monsters-tier<N>.md`.
- `reference/dragonlance/factions.md` and `ages.md` available for setting-specific modifications.

## Procedure

### 1. Identify the query type

| Query | Source | Format |
|---|---|---|
| Condition (paralyzed, frightened, stunned, etc.) | `reference/srd/conditions.md` | Bullet list of effects |
| Combat mechanic (grapple, shove, disengage, hide) | `reference/srd/combat.md` | Action description + resolution |
| Spell (by name) | `reference/srd/spells-tier<N>.md` | Full spell block |
| Monster ability (by ability name or monster) | `reference/srd/monsters-tier<N>.md` | Ability block |
| Attunement / curse rules | `reference/srd/magic-items.md` | Rule paragraph |
| Exhaustion levels | `reference/srd/conditions.md#exhaustion` | Level table |
| XP budgets | `reference/srd/encounter-building.md` | Table |

### 2. Retrieve and inline

Read the relevant SRD file. Extract only the relevant rule text. Do not link — inline it.

Format the response:

```
RULE: <keyword queried>
SOURCE: reference/srd/<file>.md

<exact SRD text, verbatim, ≤ 150 words>

DRAGONLANCE MODIFICATION (if any):
<any setting-specific adjustment — e.g., Solamnic knights are proficient with X; High Sorcery
wizards must belong to an Order; Reorx clerics use Y channel divinity>
```

If no Dragonlance modification exists, omit that section.

### 3. Answer the session's specific question

After the raw rule, add one line resolving the specific question that prompted the lookup:

```
APPLIED: <one sentence — e.g., "Aelric's grapple attempt uses Athletics vs. the bandit's Athletics or Acrobatics (bandit's choice); bandit is Medium, so no size restriction applies.">
```

### 4. Continue the session

Return the rule answer and immediately continue. Rule-lookup does not produce a file — it produces inline text only. If the rule needs to be added to the module's DM Cheatsheet, note it for module-binder.

## Common rules quick-reference (inline — do not look up if you know these)

### Conditions

**Paralyzed:** Incapacitated (can't act or react); can't move or speak; auto-fails Str and Dex saves; attacks against have advantage; attacks from within 5 ft. are critical hits.

**Frightened:** Disadvantage on ability checks and attack rolls while the source of fear is in sight; can't willingly move closer to the source.

**Stunned:** Incapacitated; can't move; can speak only falteringly; auto-fails Str and Dex saves; attacks against have advantage.

**Poisoned:** Disadvantage on attack rolls and ability checks.

**Charmed:** Can't attack the charmer or target them with harmful abilities or magical effects; charmer has advantage on social ability checks against the charmed creature.

**Grappled:** Speed becomes 0. Ends if the grappler is incapacitated or the target is moved out of reach.

### Attunement

A creature can be attuned to no more than 3 magic items at a time. Attunement requires a short rest (1 hour) spent focused on the item. Cursed items: the curse is revealed on attunement (unless specified otherwise); the curse persists until dispelled, even if the character removes the item.

### Death saves

On your turn when at 0 HP: roll 1d20. On a 10 or higher: success. On a 9 or lower: failure. 3 successes: stable. 3 failures: dead. A natural 1 counts as 2 failures. A natural 20 restores 1 HP. Damage at 0 HP adds 1 failure (2 if from a critical hit).

### Advantage/disadvantage

When you have advantage: roll 2d20, take higher. When you have disadvantage: roll 2d20, take lower. If you have both advantage and disadvantage from any sources, they cancel — roll 1d20.

### Concentration

Casting a concentration spell while already concentrating on one ends the first spell. If you take damage while concentrating: Constitution saving throw DC = max(10, half damage taken). On a fail: concentration ends.

## Dragonlance-specific rule modifications

### Solamnic knights

- Proficiency in heavy armor regardless of class proficiencies (per Order).
- The Oath (*Est Sularus oth Mithas*) is a binding commitment enforced by campaign-permanent honor mechanics (see CLAUDE.md).
- Knights of the Crown: Sworn to justice. Knights of the Sword: Sworn to service. Knights of the Rose: Sworn to wisdom.

### High Sorcery wizards

- Must belong to one of the three Orders (White Robes / Red Robes / Black Robes) after passing the Test.
- Spells cast with a component tied to their moon alignment are cast at +1 spell level (when that moon is full).

### Reorx clerics (Dwarven forge-priests)

- Channel Divinity: "Thou'rt seen" — as an action, the cleric may speak this phrase to a forge, hearth, or crafted object to sense its spiritual state (as Detect Magic, but restricted to crafted objects and their emotional provenance). Once per short rest.
- Sacred craft ritual: touching the inside-curve of a forge or anvil as a bonus action grants the cleric proficiency on the next Religion check made in connection with craft or grief.

## Anti-patterns

- Looking up rules that are in the quick-reference section above (waste of time).
- Paraphrasing the SRD instead of quoting it (paraphrases introduce errors).
- Stopping the session to deliver a 3-paragraph rule explanation (inline only; ≤ 150 words).
- Adding Dragonlance modifications that are not in `reference/dragonlance/` (invent only when the setting is silent, and register the invention).
- Using this skill for social/narrative questions that have no mechanical resolution.
