---
name: treasure-forger
description: Forge a D&D 5e artifact with full stat block, lore, curse, presence, and plot hooks. Use when an adventure needs a central or incidental treasure. Produces treasures/<slug>.md AND treasures/<slug>-manifest.md (cross-skill handshake listing symptoms the dungeon must show). Enforces quality gates tied to persona lenses.
---

# treasure-forger

Create a D&D 5e magic item — usually a central artifact with curse — for the workshop. The item is the narrative anchor of the adventure. **Also produces a Curse Symptoms Manifest** that `dungeon-smith` is required to honor.

## Preconditions

- Either a **concept** (material, era, owner archetype, curse hook) OR an **artifact-seed** from a `premise.md`.
- Access to `reference/srd/attunement.md` and `reference/srd/magic-item-rarity.md`.
- Access to `reference/dragonlance/` for setting-grounded lore.

## Outputs

1. `treasures/<slug>.md` — the artifact itself.
2. `treasures/<slug>-manifest.md` — the Curse Symptoms Manifest (only if the item is cursed). This is the **cross-skill contract** with `dungeon-smith`.

## Procedure

### 1. Clarify the concept if needed
Ask yourself:
- What does the item *look* like? One concrete sensory line.
- What was it *originally* for? (Almost always different from what it ended up doing.)
- Who made it? Who last held it? What did they do wrong with it?
- What's the curse and what's the **creeping cost**?
- **What does the item want?** (New — the Presence / Desire axis.)

If any of these can't be answered from the seed + premise + Dragonlance refs, ask the user.

### 2. Write `treasures/<slug>.md`

Required sections in order:

```markdown
---
<frontmatter>
---
# <Full Artifact Name>

*<Evocative one-line description — what the players see when they first behold it.>*

## Appearance
Paragraph. Concrete sensory detail. Avoid adjective pile-ups.

## Presence / Desire
**REQUIRED for any attunement-required item.** One paragraph. What does this item *want*? How does it express wanting — does it warm when held, grow heavier for some hands than others, drift toward one character's shadow, chime in a particular room, go still in another? This is not a mechanic — it is *temperament*. The DM should feel comfortable improvising the item's reactions. Example: *"The rose is drawn to the hand of whoever has lost the most. It grows colder in the hands of those who have not yet grieved, and it fits — too well — the hand of those who have."*

## Provenance
A chain of prior owners — at least 3, starting from the creator. Each entry:
- **Name, era, fate.** One line of fate. Each worse than the last.
- Optional one-sentence vignette.

## Properties (Mechanical)

### Rarity
<tier>. Attunement: <required / not required>. Attunement prerequisites: <if any>.

### Benefits (while attuned)
Clear, bulleted. Tier-appropriate per `reference/srd/magic-item-rarity.md`.

### Curse (while attuned)
One hidden mechanic. Required three:
1. A **creeping cost** (not instantaneous).
2. A **narrative symptom** (felt in fiction before seen mechanically).
3. A **mechanical expression** (what the DM rolls).
Also specify: when the curse **first reveals** (typical: third long rest).

### Ending the Curse
Required and playable. No "a wizard of sufficient level."

## Hooks
≥ 3 plot hooks seeded by this artifact:
- Hunters.
- Witnesses.
- Moral / character cost.

## GM Notes
DM-facing paragraph. How to reveal the curse, pacing, what to do if party tries to destroy early.
```

### 3. Write `treasures/<slug>-manifest.md` (cross-skill handshake)

**For any cursed artifact**, produce:

```markdown
---
adventure: <slug>
artifact: <name>
author: treasure-forger
created: <today>
---
# Curse Symptoms Manifest — <Artifact Name>

The dungeon housing this artifact MUST express the curse in at least 3 of the following ways, distributed across its rooms. `dungeon-smith` reads this file and honors it.

## Required (≥3, distributed across ≥2 rooms)

- [ ] **Visual symptom:** <e.g., carvings scored rose-petal-shaped from inside>
- [ ] **Textual symptom (attribution drift):** <e.g., a quote attributed to X in one room and to no one in another>
- [ ] **Textual symptom (orthographic drift):** <e.g., Vaenor spelled Vanor on one inscription>
- [ ] **Auditory symptom:** <e.g., a phrase repeated across rooms the DM reads without commentary>
- [ ] **Sensory symptom:** <e.g., the tomb is always dry even where it should be wet>
- [ ] **Reaction moment:** when the artifact is taken, <something heals / shifts / reveals>

## Required (always)

- [ ] At least one room's architecture expresses the curse's *mechanism* (e.g., memory-erosion → walls whose carvings are being edited).
- [ ] At least one earlier room foreshadows a later reveal (e.g., a letter mentioning the creator's madness).

## Suggested (optional)

- Per-room memory fragments from prior bearers' perspectives (DM reads if party lingers).
- An NPC in the adventure's starting settlement who has met a prior bearer.
- An incidental item that the curse has touched (a secondary, non-attuning object).
```

### 4. Invariants to enforce

- **Mechanical benefit real.** A curse with no benefit is a curse no one falls for.
- **Creeping cost, not cliff.** First session upside; cost emerges across play.
- **Setting-grounded provenance.** Names/dates/events cite `reference/dragonlance/`. Flag gaps; don't silently invent.
- **Curse dispellable in principle.** No unbreakable curses.
- **One curse, not two.** Don't layer.
- **Item has temperament.** The Presence / Desire section is non-negotiable for attuning items.

### 5. Never overwrite silently

If `treasures/<slug>.md` or its manifest exists, write `<slug>.v2.md` and report.

## Quality Gates

### Required sections (Moldvay + Schick)
- [ ] Appearance, Presence / Desire, Provenance (≥3 owners), Properties, Benefits, Curse, Ending, Hooks, GM Notes all present.
- [ ] Presence / Desire section is prose-evocative, not mechanic-spec.

### Curse design (Schick + Stuart)
- [ ] Creeping cost, narrative symptom, mechanical expression all specified.
- [ ] Ending the curse is specific and playable.
- [ ] Curse reveal timing is specified.
- [ ] Manifest file emitted for dungeon-smith.

### Setting (Stuart)
- [ ] Provenance cites ≥3 Dragonlance refs (ages, factions, geography).
- [ ] Any lore gaps flagged (not hallucinated).

### Player stakes (Gygax)
- [ ] Attunement has a clear benefit worth falling for.
- [ ] Hooks include ≥1 future-adventure seed.

## Output to user

- Rarity + attunement summary.
- Curse one-liner.
- Manifest symptoms required of `dungeon-smith` (listed).
- Any `reference/dragonlance/` gaps you'd like filled.
- Suggested room numbers in an existing `rooms/` dir where foreshadowing belongs.

## Anti-patterns (will be flagged)

- Curse is just HP loss per rest.
- Curse with no narrative symptom.
- Provenance < 3 owners.
- Appearance all adjectives, no concrete detail.
- Rarity mismatched to tier without explanation.
- Alignment-only attunement gate.
- Item named after its effect.
- **No Presence / Desire section.**
- **No manifest emitted** for a cursed item.
