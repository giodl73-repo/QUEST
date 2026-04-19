---
name: party-builder
description: Create a D&D 5e party as a directory of character-sheet markdown files. Use when an adventure needs a playable party, or when the user wants to spawn a new party of a given archetype (balanced-classic, grief-themed, all-rogues, etc.). Produces personas/parties/<slug>/README.md + one markdown file per PC with stat block, personality, playstyle heuristics, and a specific grief-hook suitable for Dragonlance.
---

# party-builder

Create a party of player-characters for a D&D 5e adventure in this workshop.

## Preconditions

- A directory under `personas/parties/` will be created (or appended to).
- Target adventure's `premise.md` should be read if the party is being built FOR a specific adventure (so level/tier matches).
- `reference/srd/magic-item-rarity.md` for tier context.
- `reference/dragonlance/` for setting-grounded names, orders, and gods.

## Output

```
personas/parties/<party-slug>/
├── README.md                       # party name, formation, tier, cohesion notes
├── <pc-slug>.md                    # one per PC
├── <pc-slug>.md
├── ...
└── shared-log.md                   # empty stub for session-runner to append to
```

## Procedure

### 1. Clarify the party concept

Required dimensions:
- **Tier** (1-4) and **level** (usually 3 for a tier-1 playtest).
- **Size** (default 4).
- **Archetype** — one of:
  - `balanced-classic` — paladin + rogue + wizard + cleric
  - `grief-themed` — each PC has a specific grief that makes them resonate with cursed artifacts
  - `random-roll` — classes via d12 table; races via setting-consistent distribution
  - custom (user provides)
- **Setting anchor** — where/how did they meet? (defaults to the adventure's starting settlement if tied to one)
- **Cohesion** — why do they travel together? Give the party a reason to stay at the table.

### 2. Write the party README

Required sections:

```markdown
---
party: <party-slug>
tier: <n>
level: <n>
archetype: <name>
setting-anchor: <place/event>
author: party-builder
created: <today>
---

# <Party Name>

## One-line identity
<One sentence. "Four odd-sorts drifted into Varduin-by-the-Pines over the same winter and discovered they had nowhere else to be.">

## Formation
<Paragraph: how they came together. Grounded in the setting.>

## Cohesion
<Why they stay together. A shared obligation, a shared debt, a shared curiosity.>

## Party Composition
| PC | Class / Subclass | Race | Role | Key trait |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

## Group Dynamics
Two-sentence sketch of how they argue and who defers to whom.

## Files
Link to each PC's file.
```

### 3. Write each PC file

Every PC sheet MUST have these sections:

```markdown
---
party: <party-slug>
pc: <pc-slug>
class: <class>
subclass: <subclass>
race: <race>
level: <n>
author: party-builder
created: <today>
---

# <Full Name>, <epithet / role>

## Appearance
One paragraph. Height, build, one distinctive physical detail, how they carry themselves. Nouns over adjectives.

## Background (Dragonlance-grounded)
One paragraph. Where born, who raised them, how they came to their class, which order/faith/guild if any. Cite `reference/dragonlance/` where relevant.

## Motivation
What do they want, *in this adventure*? One sentence. Must be narrower than "adventure." Example: "Aelric wants a Solamnic commendation that will get him considered for the Sword."

## Grief / Loss *(required for this workshop)*
One paragraph. What have they lost? Who? When? This is the memory the Silver Rose (or any memory-eating curse) will target. **Name the person. Give one concrete sensory memory of them.** The player will refer back to this during the curse phase.

## Stat Block

**AC** <n>  ·  **HP** <n>  ·  **Speed** <n> ft.

| Str | Dex | Con | Int | Wis | Cha |
|---|---|---|---|---|---|
| <n> | <n> | <n> | <n> | <n> | <n> |

**Saves:** (proficient in which)
**Skills:** (proficient in which)
**Senses:** passive Perception <n>; darkvision if applicable
**Languages:** Common + 1-2 setting-relevant
**Equipment:** armor, weapons, class kit, ~15 gp pocket coin, one personal item

**Attunement slots:** 3 (empty at start of adventure)

## Class Features (level 3)

Bulleted: the 3-6 things the DM will actually use at the table.
- **Feature name.** Mechanical description, one line.

## Spells (if any)

**Cantrips:** list
**Prepared / known (level 1):** list with save DCs
**Prepared / known (level 2):** list

**Spell save DC:** <n>  ·  **Spell attack:** +<n>

## Personality (5e-style)

- **Traits:** two short lines.
- **Ideals:** one line.
- **Bonds:** one line. Connects to the grief above where possible.
- **Flaws:** one line.

## Playstyle Heuristics *(for solo-DM runs)*

**Decision order when offered a choice** (the DM consults this when playing the PC):

1. <PC's top priority, e.g., "honor the Oath even at personal cost">
2. <second priority>
3. <third>

**Signature moves** (the DM should use these when fitting):
- <A thing this PC does that other PCs don't>
- <Another thing>

**When in doubt** — roll d6, 1-3 <option A>, 4-6 <option B>.

**Voice tags** — 2-3 verbal tics or register notes for the DM to lean on when speaking the PC.

## Secrets

One thing the PC has *not* told the rest of the party. May or may not surface in play.
```

### 4. Playability check

Before declaring done:

- [ ] Each PC has a grief paragraph with a named person and a concrete memory.
- [ ] Playstyle Heuristics are concrete enough that a DM can play the PC without asking the player.
- [ ] At least one PC has a setting-anchor that connects to the starting adventure (e.g., born in Varduin, or pupil of the Red Robes, or a Solamnic initiate).
- [ ] Party composition covers the four essentials: heavy front-liner, skilled rogue/scout, arcane caster, divine caster (for balanced-classic).
- [ ] No two PCs have the same mechanical niche.
- [ ] Cohesion section answers "why are they still traveling together?" in a way the DM can reference under pressure.

### 5. Never overwrite silently

If a party directory already exists with different PCs, write `<party-slug>-v2/` and report.

## Output to user

- Party name + archetype.
- Composition table.
- Grief-hooks (one-line each) — these are the threads the DM will pull on during the adventure.
- Suggested next step: `dice-roller` + `session-runner` for the actual playtest.

## Quality gates

- [ ] Party README + N PC files + shared-log.md stub.
- [ ] Each PC sheet ≥ 600 words (not padded; substantive).
- [ ] All stat blocks balance-check: HP and AC in tier-1 ranges.
- [ ] Spell lists chosen from SRD.
- [ ] Grief-paragraphs are specific, not generic.

## Anti-patterns

- Generic "wanted adventure" motivations.
- Abstract griefs ("lost my village"). Grief must name a *person*.
- PCs whose playstyle is "whatever the player wants." For solo-DM runs, we need explicit heuristics.
- Stat blocks that skip Saves or Skills.
- Stat blocks that don't balance (MAD characters with 18 in their off-stat).
