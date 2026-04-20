---
name: lore-weaver
description: Weave Dragonlance setting lore into an adventure premise and room files. Enforces the accessibility policy (first-use glossing of setting-specific terms), checks for canon contradictions against reference/dragonlance/, and seeds workshop-canon.md with newly invented names. Use during or after dungeon-smith, before adventure-lint.
---

# lore-weaver

Weave Dragonlance lore into an adventure. The goal is not to write a history lesson — it is to make the setting feel lived-in and specific while remaining accessible to a reader who has never heard of Krynn.

## Core principle

**Marathon is Dragonlance-native, not Dragonlance-adjacent.** We invent where Dragonlance is silent. We do not contradict canon where canon speaks.

**The accessibility policy (from CLAUDE.md):** First use of any setting-specific term (Solamnic, Krynn, Cataclysm, High Sorcery, Test, Portent, Oath, Order of the Rose, etc.) must be glossed in-fiction — a line of dialogue, a character's internal note, or a narrator's aside. Returning uses can assume the gloss landed.

## When to use

- After dungeon-smith produces room files but before adventure-lint.
- When a premise references Dragonlance factions, ages, or geography that have not been glossed.
- When a newly invented NPC, location, or item needs to be registered in workshop-canon.md.

## Preconditions

- `adventures/<slug>/premise.md` exists.
- `adventures/<slug>/rooms/` has at least one room file.
- `reference/dragonlance/` exists with: `ages.md`, `geography-ansalon.md`, `factions.md`, `workshop-canon.md`.
- `CLAUDE.md` campaign-continuity section is readable (for campaign-permanent facts that constrain narration).

## Procedure

### 1. Read the setting references

- `reference/dragonlance/ages.md` — which age is this adventure set in? What events are active?
- `reference/dragonlance/geography-ansalon.md` — is the location canon? What is known about it?
- `reference/dragonlance/factions.md` — which factions are in play? What are their current-age relationships?
- `reference/dragonlance/workshop-canon.md` — what names have already been invented for this campaign?
- `CLAUDE.md` — campaign-permanent facts that cannot be contradicted.

### 2. Term audit

Read every room file and the premise. Extract every setting-specific term:
- Proper nouns (faction names, age names, location names, god names, artifact names).
- Concepts specific to Dragonlance (the Test, the Measure, the Oath, High Sorcery, the Orders, the Cataclysm).
- Any term a reader unfamiliar with Dragonlance would not recognize.

For each term, determine:
- **First use?** → requires an in-fiction gloss.
- **Already glossed elsewhere in this module?** → no action needed.
- **Campaign-permanent fact?** → verify narration is consistent.

### 3. Write the glosses

For each first-use term, write a gloss. Glosses go in the room's Read-aloud or GM Notes — never as an aside-from-narrator in brackets.

**Gloss formats:**

- **Dialogue:** *"The Measure," Aelric said — my honor is my life, the Solamnic code that governed every action a knight could take.*
- **Internal note:** *She had spent three years studying under the Orders of High Sorcery, the three mage-guilds that had divided Krynn's arcane power since the Age of Dreams.*
- **Narrator aside (within description):** *The Cataclysm — the gods' punishment three hundred years ago that had reshaped the continent's coastlines — had left this harbor shallower than any chart recorded.*

Glosses must be:
- In-fiction (not parenthetical).
- ≤ 2 sentences.
- Accurate to the current age of the adventure.

### 4. Canon check

For every canon element referenced (named location, historical event, faction relationship, deity):
- Verify it appears in `reference/dragonlance/ages.md` or `geography-ansalon.md`.
- Verify it is consistent with the age of the adventure.
- If it contradicts canon: flag the contradiction and propose a fix (rename the location, adjust the date, use a different faction).

**Never contradict canon where canon speaks.** Where Dragonlance is silent, invent freely — but register the invention.

### 5. Register inventions

Every newly invented name (character, location, item, event, organization) goes into `reference/dragonlance/workshop-canon.md`:

```markdown
### <Name>
- **Type:** [character / location / item / event / organization]
- **Adventure:** <slug>
- **Age:** <age>
- **Description:** 1 sentence.
- **Canon basis:** [canon-consistent / canon-silent (invented) / canon-adjacent]
```

If `workshop-canon.md` does not exist, create it with this header:

```markdown
# Workshop Canon

Invented names and details for the Marathon campaign. Every invented element in this file is tracked so future adventures do not accidentally contradict it.

*Canon policy: we invent where Dragonlance is silent; we never contradict where canon speaks.*
```

### 6. Write the lore report

After all glosses and registrations are written, output a brief report:

```
Lore report — <Adventure Title>

Terms glossed (first use): N
  - <term>: glossed in <room/scene> (<format: dialogue/internal/narrator>)

Canon checks: N passed, N flagged
  - FLAGGED: <term> — <issue> — <proposed fix>

Inventions registered: N
  - <name>: <type>, registered in workshop-canon.md

Accessibility policy status: [COMPLIANT / VIOLATIONS FOUND]
  - Any violations: <list with location>
```

### 7. Never overwrite silently

If a room file already has a gloss for a term, do not replace it — add only where missing. If a `workshop-canon.md` entry already exists for an invented name, update it rather than duplicate.

## Quality gates

- [ ] Every setting-specific term has a first-use gloss in this module.
- [ ] No canon contradiction found (or all flagged and proposed-fix written).
- [ ] Every invented name registered in workshop-canon.md.
- [ ] All glosses are in-fiction (no brackets, no parentheticals, no narrator meta-commentary).
- [ ] Gloss for the Oath (*Est Sularus oth Mithas*) includes the translation (*"my honor is my life"*) on first appearance in this module.

## Dragonlance glossing quick reference

| Term | Standard in-fiction gloss |
|---|---|
| Solamnic | "the Solamnic knights — the chivalric order that had held the continent's northern roads for five centuries" |
| The Measure | "the Measure, the Solamnic code that governed every action a knight could take" |
| The Oath | "*Est Sularus oth Mithas* — my honor is my life, the knight's oath spoken at investiture" |
| High Sorcery | "the Orders of High Sorcery, the three mage-guilds that had divided Krynn's arcane power since the Age of Dreams" |
| The Test | "the Test of High Sorcery, the ordeal every wizard must survive to join the Orders" |
| The Cataclysm | "the Cataclysm, the gods' punishment three centuries ago that had remade the continent's coastlines" |
| Reorx | "Reorx, the Dwarven god of forge and craft" |
| The Orders | "the three Orders of High Sorcery — White Robes, Red Robes, Black Robes — aligned to the three moons" |

These are suggestions. Every gloss should fit naturally into its sentence context — do not paste verbatim if it breaks the prose rhythm.

## Anti-patterns

- Glosses that are longer than 2 sentences (stop explaining, trust the reader).
- Glosses that break the read-aloud voice (a gloss in a read-aloud must sound like description, not a history lesson).
- Inventing names that contradict or overwrite existing workshop-canon entries.
- Checking canon against the wrong age (Dragonlance has multiple ages; the gloss must match).
- Skipping the lore report (the audit trail matters for future adventures in the same campaign).
