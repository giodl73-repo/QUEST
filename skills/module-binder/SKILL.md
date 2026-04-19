---
name: module-binder
description: Compile an adventure directory into a table-ready module.md with TOC, inlined rooms/stat-blocks/treasures, and a DM cheatsheet with critical SRD rules inlined (not linked). Use when an adventure has premise, rooms, treasures, encounters, NPCs, and any wandering-pressure table written. Produces adventures/<slug>/module.md.
---

# module-binder

Compile the contents of an adventure directory into a single `module.md` that a DM can open at the table and run cold.

## Preconditions

- `premise.md` exists.
- `rooms/map.md` and at least one `rooms/NN-<slug>.md` exist.
- `treasures/` has at least one item file.
- `encounters/` has files for every encounter-bearing room, OR the rooms self-contain their encounter inline.
- `npcs/<slug>.md` exists for every named NPC in `premise.md`.
- Cross-references use relative paths.
- Ideally: `adventure-lint` has been run and passed.

## Procedure

### 1. Read the directory
- `premise.md`
- `rooms/map.md`
- All `rooms/NN-*.md` in numeric order
- All `treasures/*.md` (exclude `*-manifest.md` — those are for `dungeon-smith`, not players)
- All `encounters/*.md` including `wandering-pressure.md` if present
- All `npcs/*.md`

### 2. Resolve cross-references
For every relative markdown link in a room's Treasure / Encounter / NPC / Connections sections:
- Follow the link.
- Inline the content at that location.
- Preserve source link as HTML comment (`<!-- from treasures/silver-rose.md -->`).

### 3. Inline critical SRD rules
**New invariant.** For every SRD reference used anywhere in the module (attunement, cursed-item rules, specific conditions, exhaustion effects, XP budgets), **inline the relevant 1-3 sentences into the DM Cheatsheet** — do not link out to `reference/srd/*`. A DM at the table should never have to open a second file for rules referenced in the module.

Specifically, the cheatsheet should inline:
- Any condition referenced in encounters (paralyzed, frightened, poisoned, etc.).
- Attunement rules (3-item limit, short-rest attunement, curse-on-attunement).
- Exhaustion levels if any trigger.
- XP budget table for the adventure's tier.

### 4. Assemble `module.md`

Template:

```markdown
---
<frontmatter with compiled-from list>
---
# <Adventure Title> — DM Module

*<Logline.>*

**Tier:** <n>  |  **Party:** <size, level>  |  **Expected playtime:** <sessions>

## Table of Contents
1. Summary
2. Hook
3. Setting & Background
4. Map
5. Rooms (numeric order)
6. Treasures
7. NPCs
8. Encounters Appendix
9. Wandering Pressure (if applicable)
10. DM Cheatsheet

---

<sections per template>

## Rooms
<For each room:>
### Room NN — <Name>
**Read-aloud:** (verbatim from source)
**Features:**
**Connections:**
**Encounter:** <FULLY INLINED — stat block, tactics, XP. No "see appendix" stubs.>
**Treasure:** <INLINED — what the players find when they grab it. Full lore goes to Treasures section.>
**GM Notes:**
**Memory Fragment (optional):** (if the room file has one)

---

## Treasures
<Full content of each treasure: appearance, presence, provenance, properties, curse, ending, hooks, GM notes.>

## NPCs
<Full content of each NPC file.>

## Encounters Appendix
<Stat blocks + tactics, alphabetized. Redundant with Rooms section; intentional.>

## Wandering Pressure (if `wandering-pressure.md` exists)
<Inline the Cold Pulse and Wandering Encounter tables verbatim.>

## DM Cheatsheet

### Quick References
- **Key DCs** (sorted by room)
- **Key saves** (with consequences inline)
- **Attunement rules (inline):** Short rest (1 hour) to attune. 3 items per character. Curse revealed on attunement unless otherwise specified.
- **Conditions used in this adventure (inline):** <e.g., "Paralyzed: incapacitated; can't move/speak; auto-fails Str/Dex saves; attacks have advantage; crit from within 5 ft.">
- **XP budget (tier <n>, party of <size> level <lvl>):** Easy/Medium/Hard/Deadly (inline numbers).

### Scene Triggers
"If the party does X..." → how to handle, one line each.
```

### 5. Invariants to enforce

- **Self-containment.** A DM with only `module.md` + the SRD reference pack they already know can run the adventure.
- **No "see X" stubs in rooms section.** Inline.
- **Room order matches map.**
- **Read-aloud preserved verbatim.**
- **Stat blocks fully inlined in rooms and redundantly in appendix.**
- **DCs visible in-place AND in cheatsheet.**
- **Critical SRD rules inlined in cheatsheet.** (New.)
- **Page-breakability:** `---` between rooms so print-cuts fall cleanly.

### 6. Consistency warnings

After compilation, report:
- Broken cross-references.
- Encounter rooms without inlined stat blocks OR encounter files.
- Treasure references without corresponding treasure file.
- Map rooms with no room file (or vice versa).
- NPCs referenced in body without `npcs/` file.
- Read-aloud over 60 words.
- Any SRD reference not inlined in the cheatsheet.

### 7. Never overwrite silently
Existing `module.md` → write `module.v2.md` and report.

## Quality Gates

### Self-containment (Moldvay)
- [ ] No "see file X" stubs in the rooms section.
- [ ] Every stat block used is inlined at point-of-use.
- [ ] Every SRD reference in the body is inlined in the cheatsheet.

### Integrity (all personas)
- [ ] No broken cross-references.
- [ ] Map rooms ↔ room files 1:1.
- [ ] Every named NPC has an inlined NPCs section entry.
- [ ] Wandering pressure table included if the adventure directory has one.

### Reviewer-ready (Stuart + Schick)
- [ ] Treasures section preserves Presence / Desire language.
- [ ] Every Memory Fragment from room GM Notes is preserved in the compiled body.

## Output to user

- Word count of final module.
- Counts of rooms, treasures, encounters, NPCs compiled.
- Consistency warnings (see Step 6).
- Suggested next step: `persona-review` (when built) OR manual persona reviews.

## Anti-patterns (will be flagged)

- "See treasures/silver-rose.md" in the rooms section.
- Stat blocks only in appendix.
- Missing cheatsheet.
- Critical SRD rules linked out instead of inlined.
- Missing wandering-pressure inline.
- Rooms out of order.
- Read-aloud paraphrased.
