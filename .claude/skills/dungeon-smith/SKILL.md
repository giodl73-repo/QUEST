---
name: dungeon-smith
description: Given an adventure premise, generate a keyed dungeon — room files plus an ASCII map. Use when a premise.md exists and rooms/ is empty. Produces rooms/NN-<slug>.md for each keyed location and rooms/map.md with a legible ASCII dungeon map. Enforces quality gates tied to persona lenses (Jaquays topology, Stuart atmosphere, Schick treasure-framing, Moldvay table-readiness, Gygax attrition).
---

# dungeon-smith

Generate a keyed dungeon for a D&D 5e adventure in this workshop. Produces:

1. `rooms/map.md` — ASCII map with room numbers and connections.
2. `rooms/NN-<slug>.md` — one file per keyed location.
3. `encounters/wandering-pressure.md` if the dungeon is a tomb, crypt, or similar sealed space.

## Preconditions

- `adventures/<slug>/premise.md` exists and has: tier, party, hook, setting, artifact-seed, themes, constraints (including room count).
- `adventures/<slug>/rooms/` is empty or nonexistent.
- If any `treasures/<slug>-manifest.md` files exist (produced by `treasure-forger`), read them as **required inputs** — they specify curse symptoms the dungeon must show.

## Cross-Skill Contract

When a cursed artifact is forged by `treasure-forger`, the forger MUST emit a **Curse Symptoms Manifest** at `treasures/<artifact-slug>-manifest.md` listing the symptoms the dungeon is obligated to express. `dungeon-smith` reads these manifests and MUST honor at least **3 symptoms** distributed across the dungeon's rooms (visual, textual, auditory, or sensory). A dungeon that contains a cursed artifact but shows no symptoms of it violates the contract.

## Procedure

### 1. Read context
- `premise.md`
- All `treasures/*-manifest.md` (if any)
- `reference/dragonlance/dm-notes.md` (tone)
- `reference/dragonlance/ages.md` and `geography-ansalon.md` (setting accuracy)
- `CLAUDE.md` (file/frontmatter conventions + campaign-continuity)
- `personas/rubric.md` (the axes you're being scored on)
- **Campaign spine (if any): `docs/campaign/<slug>.md`** — find this adventure's brief; read its Spotlight, Seeds-Retrieved list, Seeds-To-Plant list, Hints scheduled here.
- **Seed-tracker: `campaign/seed-tracker.md`** — confirm seeds-to-retrieve are `active`; confirm seeds-to-plant don't duplicate existing ones.

### 1a. Campaign-awareness obligations *(new — if a campaign spine exists)*

Before designing rooms, commit to:
- **Spotlight:** which PC's arc centers this adventure. Every keyed scene should give the spotlight-PC at least one moment (not necessarily combat — often a recognition or decision).
- **Seeds-retrieved:** each planted seed from prior adventures gets an activation in this one. For each seed, note which room/scene hosts the retrieval.
- **Seeds-to-plant:** each seed scheduled to be planted here needs a concrete in-fiction placement (an NPC mentions it, a document references it, an object bears its mark).
- **Hints scheduled:** if the spine schedules a hint-unlock here, the module MUST include the unlocking scene (see rubric v1.2 — hints have recovery paths, but the scheduled scene is the primary route).
- **Hint structure mandate:** Every cross-session hint requires all three components: (1) **Plant** — where and how it enters the world; (2) **Delivery mechanism** — the specific roll, passive check, or auto-deliver condition that makes it available; (3) **Convergence point** — which scene in which future adventure this hint is designed to land. A hint with only a plant and no delivery mechanism will fail silently.
- **Three-route outcomes (A/C/D):** Name the three possible session outcomes explicitly before designing rooms — Route A (charter/fallback: the goal is achieved conventionally), Route C (destruction/default: the artifact is spent; the grief discharged without release), Route D (inversion/optimal: the emotional core is named and released; full closure). Every scene's GM Notes should note which route(s) it supports and whether missing the scene closes off a route.

These obligations are cross-checked at `adventure-lint` time.

### 2. Design the map FIRST
Sketch topology before writing any room. **Non-linear is mandatory**:
- At least one loop (two rooms connected in ≥2 ways).
- At least one vertical element (stairs, pit, trapdoor, ledge).
- At least two paths to the central artifact.
- An optional shortcut that opens after a condition.
- **Each branch must have a distinguishing sensory cue at its entrance** — a draft, a sound, a smell — so curious parties are rewarded and non-curious parties still get a chance to notice the interesting branch.

### 3. Write the ASCII map
Output to `rooms/map.md`. Required: ASCII with room numbers and connections; a legend; scale note; a Connections table mapping room → rooms with notes on locks/conditions. Frontmatter per `CLAUDE.md`.

### 4. Write each room
Create `rooms/NN-<slug>.md` per keyed location. Required sections in order:

```markdown
---
<frontmatter>
---
# Room NN — <Short Name>

## Read-aloud
> Under 60 words. Spatial first, atmospheric second. Never tell players how they feel.

## Features
Bulleted interactables with DCs inline.

## Encounter
Link to `encounters/<slug>.md` if a fight happens here. Otherwise "None" or a social/exploration block.

## Treasure
Link to `treasures/<slug>.md` if loot is here. Include retrieval conditions.

## Connections
Directional list with lock DC / door type.

## GM Notes
DM-facing guidance that should NOT appear in read-aloud.

### Memory Fragment (optional — read only if the party lingers)
One-sentence atmospheric beat, ideally from a prior bearer's perspective. No mechanical effect. Optional.
```

### 5. Invariants to enforce

- Every room has a reason to exist. Cut filler.
- At least one room is purely atmospheric/lore-bearing (Stuart room).
- At least one room has multiple valid solutions (Jaquays room).
- Final artifact room includes a **reaction moment** when the artifact is taken (something heals, shifts, reveals, weeps).
- Read-aloud ≤ 60 words.
- Treasure placement foreshadowed.
- **Every named corpse / body gets a name + one sentence of backstory.** Unnamed remains are placeholder; flag them.
- **Every non-statted entity** (echo, voice, ghost, presence) has at least one sentence: "what happens if players try to interact with it?"
- **Retrieval/solution options that differ only in a single flag (loud vs. quiet) should be consolidated** into one option with a modifier, not listed as two options.

### 6. Temporal-pressure table

For any tomb, crypt, sealed vault, or otherwise isolating dungeon: write `encounters/wandering-pressure.md` containing **both** a Cold Pulse table (atmospheric, d6 per 10 min) and a Wandering Encounter table (mechanical, d6 per 30 min). A dungeon without temporal pressure fails the Gygax and Stuart gates simultaneously.

If the dungeon's setting honestly rules out temporal pressure (e.g., frozen-in-time pocket dimension), say so in the GM Notes with justification — skipping requires explicit rationale, not silent omission.

### 7. NPCs manifest

Every NPC named in `premise.md` or in any room/treasure/encounter file MUST have `npcs/<slug>.md`. Skill creates skeletons for missing NPCs and flags them for the human to flesh out. Skeleton must include: appearance, stat block (or "non-combatant"), public vs. private knowledge, behavior matrix (what they do in 5-6 likely party interactions), private motive.

**NPC arc-completion:** For any NPC with an emotional arc (grief, shame, longing, pride, rage), identify the specific thing they are capable of saying or doing that closes their arc. Write it under `## Arc-Completion` in their `npcs/<slug>.md`: the exact line or act, and the conditions under which it fires (what the party must have done or said; what scene structure must be present). This is designable — do not leave it to improvisation. When an NPC fires their arc-completion moment by character logic rather than DM scripting, it produces the highest-quality atmospheric landing in the session. See `skills/npc-architect/SKILL.md` for the full arc-completion design procedure.

**NPC-as-information-holder:** Design some NPCs to hold intelligence rather than objects. They know something and will give the information when the party demonstrates they can use it correctly. Write a specific "information readiness condition" — not "if the party is trustworthy" but "what specific act demonstrates the party can receive this information correctly." *Example: Vorn Haleth knew a shard's location for 8 months and withheld it until she witnessed the party performing the accountability the compact requires.* Information-holder NPCs are distinct from artifact-holder NPCs; their arc-completion is a transfer of knowledge, not a transfer of an object.

**Give the archivist something they cannot document.** If a PC on the party sheet has "systematic documentation" as their primary heuristic, design one scene per session that exceeds their current vocabulary — an experience they cannot categorize. The arc resolves across sessions as they find vocabulary. This produces a reliable 3-session character arc without any scripting: documentation-suspension → vocabulary found → forward-looking design.

### 8. Map ↔ rooms consistency check
Before declaring done:
- Every room number on the map has a corresponding `NN-<slug>.md` file.
- Every `NN-<slug>.md` appears on the map.
- Connections declared in each room match the map.
Report mismatches; don't silent-fix.

### 9. P0 self-review — run before asking for persona review

Two checks that every persona will converge on. Catching them yourself saves a full review round.

**Decision-point fallback check:** For every scene where a PC must make a meaningful decision (attune/refuse; speak/stay; open/destroy; confess/stay silent):
- [ ] A fallback path exists if the PC declines the obvious choice.
- [ ] The scene does not stall if the PC freezes or chooses the unexpected option.
- [ ] At least one scaffold is written for what the PC might say (short/medium versions; the player overrides if they want to go longer).

**Critical-roll failure state check:** For every scene with a critical roll (the roll that determines which route A/C/D is taken):
- [ ] A graceful failure path is written — what happens if the roll fails? (The campaign must still continue; failure changes texture/route, not access.)
- [ ] The failure state is written in the GM Notes, not merely implied by "the DC is accessible."

A design that passes both checks will survive playtesting. One that fails them will produce a stall or dead end at the worst possible moment.

### 10. Never overwrite silently
If a file exists, write `<name>.v2.md` and report.

## Quality Gates (RUN BEFORE DECLARING DONE)

Scored against the 5-persona rubric. Each gate maps to at least one persona.

### Topology (Jaquays)
- [ ] Map has ≥ 1 loop.
- [ ] Map has ≥ 1 vertical connection.
- [ ] ≥ 2 paths to the central artifact.
- [ ] ≥ 1 shortcut that unlocks through play.
- [ ] At least one inhabitant has behavior that changes between party visits (patrol, reposition, react).
- [ ] Every branch has a distinguishing sensory cue at its entrance.

### Temporal pressure (Gygax + Stuart)
- [ ] `encounters/wandering-pressure.md` exists (OR explicit justification in DM Notes).
- [ ] Proper encounter count ≥ ⌈room_count / 2⌉ (e.g., 6 rooms → ≥ 3 encounters; conditional ones count as half).

### Atmosphere (Stuart)
- [ ] Every room's GM Notes includes a Memory Fragment beat (optional-to-read).
- [ ] If a cursed artifact is present: ≥ 3 "dungeon-forgets-itself" sensory details distributed across rooms (from the Curse Symptoms Manifest).
- [ ] If the artifact has a Presence / Desire (per `treasure-forger`): ≥ 1 room expresses that presence in prose.

### Signature treasure (Schick)
- [ ] Every non-trivial treasure sits in a room whose architecture expresses it.
- [ ] Reaction moment when the central artifact is taken (heals / shifts / reveals).
- [ ] Every incidental item has a job (evidence, key, clue, roleplay trigger). Flag purely decorative items.

### Table-readiness (Moldvay)
- [ ] Every read-aloud ≤ 60 words.
- [ ] Every DC inline with the hazard that demands it.
- [ ] Every NPC named in premise has `npcs/<slug>.md`.
- [ ] Every non-statted entity has an interaction rule.
- [ ] No retrieval-option duplicates.

### Player agency (Gygax)
- [ ] Central artifact has ≥ 2 meaningfully different retrieval paths.
- [ ] Adventure's post-recovery decision has ≥ 3 valid outcomes (return / keep / destroy / sell-to-worse pattern).

## Output to user

- Rooms created and map topology summary.
- Quality Gate scorecard: each gate marked ✓ / ✗ with file references for any failures.
- Any Curse Symptoms Manifest obligations honored (and any left undone).
- Suggested next step: `treasure-forger` for any missing treasures; `adventure-lint` before `module-binder`.

## Anti-patterns (will be flagged in review)

- Linear corridor.
- Every room has a fight.
- Read-aloud > 60 words.
- Treasure with no foreshadowing.
- Generic rooms that could appear in any dungeon.
- Retrieval options that differ only in noise level.
- Cursed artifact with no dungeon-level symptoms.
- Named NPC in premise with no `npcs/` file.
