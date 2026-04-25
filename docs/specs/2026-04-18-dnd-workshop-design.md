---
title: D&D Workshop — Design
date: 2026-04-18
status: draft
author: brainstorm session with user
---

# D&D Workshop — Design

A workshop in `marathon` for designing D&D adventures, modules, treasures, and world-lore. Core creative principle: **the treasures are the story**. Each adventure is seeded by an artifact whose history carries the narrative weight; curses and consequences make loot a real decision.

## Anchored Decisions

| Dimension | Decision |
|---|---|
| Ruleset | **D&D 5e (2014) — SRD (CC-BY-4.0)** |
| Treasure philosophy | **Artifact-driven** + **cursed & consequential** |
| Output format | **Markdown-at-the-table** now; YAML/JSON migration deferred until 3+ adventures exist |
| Setting | **Dragonlance** (Ansalon) |
| Audience | **DM prepping for a live table** (human players) |
| Skill roster | 6 skills + 1 for reviews (see below); first 3 built, rest deferred |
| First dungeon scope | **Tiny** — 6 rooms, one session, tier 1 (party of 4, level 3) |
| Rules grounding | **Local SRD cache** (seed minimally, grow on demand) + **curated Dragonlance lore pack** |
| Architecture | **Project template + convention** — one directory per adventure, fixed layout |
| Personas | 5 design-canon voices scoring adventures on an 8-axis rubric |

## Directory Layout

```
marathon/
├── CLAUDE.md                    # repo conventions (layout, frontmatter, naming)
├── docs/
│   └── superpowers/specs/       # design docs (this file)
├── skills/                      # workshop skills (built on demand)
│   ├── dungeon-smith/
│   ├── treasure-forger/
│   ├── module-binder/
│   ├── lore-weaver/             # (deferred)
│   ├── encounter-balancer/      # (deferred)
│   ├── rule-lookup/             # (deferred)
│   └── persona-review/          # (deferred)
├── reference/
│   ├── srd/                     # cached 5e SRD (CC-BY-4.0, attributed)
│   └── dragonlance/             # curated lore pack
├── personas/
│   ├── README.md
│   ├── rubric.md                # shared 8-axis 1-10 rubric
│   ├── gygax.md
│   ├── jaquays.md
│   ├── schick.md
│   ├── moldvay.md
│   └── patrick-stuart.md
└── adventures/
    └── NNNN-<slug>/             # one directory per adventure
        ├── README.md
        ├── premise.md
        ├── rooms/
        │   ├── map.md           # ASCII map
        │   └── NN-<slug>.md
        ├── treasures/
        ├── npcs/
        ├── encounters/
        ├── module.md            # table-ready compiled file
        └── reviews/
            └── <persona>-<date>.md
```

## Component Specs

### The Seven Skills

| Skill | Input | Output | Phase |
|---|---|---|---|
| `dungeon-smith` | premise (tier, theme, artifact-seed, room count) | `rooms/NN-<slug>.md` per room + `rooms/map.md` (ASCII) | 3 |
| `treasure-forger` | concept (material, era, curse hook) + artifact-seed | `treasures/<slug>.md` — stat block, lore, curse, hooks | 3 |
| `module-binder` | an adventure directory | `module.md` — TOC, inlined read-aloud + stat blocks + DM cheatsheet | 3 |
| `lore-weaver` | a treasure or location file | appends `## Lore` grounded in Dragonlance ages, cited | 6 (deferred) |
| `encounter-balancer` | party level/size, difficulty, environment | `encounters/<slug>.md` — SRD creatures, XP math, tactics | 6 (deferred) |
| `rule-lookup` | rules question | cites `reference/srd/` with exact snippet | 6 (deferred) |
| `persona-review` | adventure dir + persona(s) | `reviews/<persona>-<date>.md` — rubric scores + in-character critique | 6 (deferred) |

### Skill Contract (shared)

- Read/write **markdown only** in v1 (YAML migration deferred).
- Every generated file begins with frontmatter:

  ```yaml
  ---
  adventure: 0001-tomb-of-the-silver-rose
  tier: 1
  author: dungeon-smith
  created: 2026-04-18
  sources:
    - reference/srd/monsters-tier1.md
    - reference/dragonlance/ages.md#age-of-might
  ---
  ```

- Skills **never overwrite silently** — append, write new file, or prompt.
- Cross-references use relative markdown links; `module-binder` resolves/inlines them.

### Naming Rules

- Adventure slug: `NNNN-kebab-case`, zero-padded 4 digits (`0001`, `0002`…).
- Room files: `NN-<slug>.md` (2 digits, up to 99 rooms).
- Treasure/encounter/npc files: `<slug>.md`.

### Premise File Contract (`premise.md`)

```markdown
---
adventure: 0001-tomb-of-the-silver-rose
tier: 1
party: 4 characters, level 3
---
# Premise
Hook: ...
Setting: <region of Ansalon, age>
Artifact-seed: <one-line description of the central treasure>
Themes: <list>
Constraints: <room count, session length, tone>
```

## Reference Packs

### `reference/srd/` — seed minimally

Seed files (Phase 1 only):

- `LICENSE.md` — CC-BY-4.0 attribution
- `conditions.md` — blinded, frightened, poisoned, grappled, restrained, etc.
- `attunement.md` — 3-item limit, attunement rules, curse framework
- `magic-item-rarity.md` — rarity tiers, expected levels, value ranges
- `monsters-tier1.md` — ~12 stat blocks usable at tier 1 (expand on demand)

Files deferred until needed: `treasure-tables.md`, `traps-hazards.md`, full monster manual, spells, class rules.

### `reference/dragonlance/` — curated, evolve-with-use

Seed files (Phase 1 only):

- `README.md` — usage, what's canon vs. ours
- `ages.md` — Age of Starbirth → Dreams → Might → Despair → Mortals (dates, vibe, key events)
- `geography-ansalon.md` — Abanasinia-focused for dungeon #1, expand as adventures demand
- `factions.md` — Knights of Solamnia (Rose, Sword, Crown) focused
- `dm-notes.md` — tone: fallen grandeur, gods-returned cycle, treasure-as-history

Files deferred: `pantheon.md`, `key-events.md`, `iconic-artifacts.md` — added when a skill hits a gap. Gap-failure mode: skill reports "no entry for X, want me to draft one?" rather than hallucinating.

## Personas

Five design-canon voices. Selected for substance over performance; overlapping-but-distinct philosophies so scores disagree productively.

| Persona | Lens |
|---|---|
| **Gary Gygax** | Old-school discipline, resource attrition, treasure-as-XP, player skill over character build. Punishes hand-holding. |
| **Jennell Jaquays** | Non-linear dungeon topology, loops / verticality / shortcuts ("Jaquaysing the dungeon"). Dings corridor-and-rooms layouts. |
| **Lawrence Schick** | *White Plume Mountain* author. Signature-treasure rooms, restraint on railroading, gonzo puzzle-dungeons. Closest philosophical match to our treasure-hunt premise. |
| **Tom Moldvay** | *B/X D&D* and *B4: The Lost City*. Procedural clarity, terse keyed-room prose. Brutal on table-readiness. |
| **Patrick Stuart** | *Deep Carbon Observatory*, *Veins of the Earth*. Literary weirdness, haunted atmosphere, treasure-as-cursed-object, prose that earns its page. Fits artifact-plus-curse principle. |

### Rubric (`personas/rubric.md`) — 1-10 per axis, /80 total

1. **Premise clarity** — can a DM pitch the hook in one sentence?
2. **Treasure-as-story** — does the central artifact carry the narrative?
3. **Dungeon integrity** — map logic, room purpose, navigation choices
4. **Encounter craft** — balance, variety, tactical interest
5. **Lore grounding** — setting-consistent, non-hallucinated
6. **Curse/consequence** — real stakes of owning the treasure
7. **Table-readiness** — can the DM run it cold from `module.md`?
8. **Player agency** — meaningful choices on the table

Each persona file defines its **voice guidelines**, **axis weights** (not every persona scores all axes equally), and **critique style** so reviews read as that person and not as generic notes.

## First Adventure: `0001-tomb-of-the-silver-rose`

**Working title:** The Tomb of the Silver Rose.

**Ansalon placement:** A wind-scoured bluff above **Abanasinia**, overlooking the Plains of Dergoth. Locally known as "the Rose Cairn."

**Age:** Mid-to-late **Age of Might**. The tomb predates the Cataclysm (AC 0) by a century — and was untouched by the gods' wrath, which is itself a clue.

**The tomb's owner:** Sir Ilendra Vaenor of the Order of the Rose, a minor Knight of Solamnia who fell to something she should not have picked up.

**Central artifact — the Silver Rose of Vaenor:**

> A rose sculpted from moon-silver, petals hinged and sharp. Originally Ilendra's family sigil, refashioned in secret by a hedge-wizard after her brother died in the Third Dragon War. Intended as a relic of remembrance; became a relic of grief that *asks* to be held. Attunement grants minor benefits; every long rest the bearer loses one memory of someone they loved (replaced by a memory of Ilendra's brother). Three prior owners are traceable; each ended worse than the last.

**Hook:** A Solamnic archivist (NPC in starting town) offers coin for the rose's safe return; the Order wants it buried properly. **The archivist does not mention the curse.** Whether the party sells, keeps, destroys, or returns the rose is the adventure's real choice.

**Incidental loot:**
- A few coins of older Istaran mintage
- A defaced Solamnic signet
- A letter in Ilendra's hand revealing the curse's first victim

**Scope:** 6 rooms, one session, tier 1 (party of 4 at level 3).

**Themes:** Fallen grandeur. Grief weaponized. The price of remembering.

## Build Order (MVP Path)

### Phase 0 — Scaffolding
1. Create top-level dirs: `skills/`, `reference/srd/`, `reference/dragonlance/`, `personas/`, `adventures/`.
2. Write repo `CLAUDE.md` — conventions, directory layout, frontmatter contract, naming rules.
3. `personas/rubric.md` — the 8-axis rubric.

### Phase 1 — Seed reference packs
4. `reference/srd/` — the 5 files listed in the Reference Packs section. CC-BY attribution in `LICENSE.md`.
5. `reference/dragonlance/` — the 5 files listed in the Reference Packs section.

### Phase 2 — Personas
6. Write all 5 persona files (`personas/gygax.md`, `jaquays.md`, `schick.md`, `moldvay.md`, `patrick-stuart.md`) before adventure #1 so we can score it once built.

### Phase 3 — Build the three MVP skills
7. `skills/dungeon-smith/SKILL.md`
8. `skills/treasure-forger/SKILL.md`
9. `skills/module-binder/SKILL.md`

**Defer** `lore-weaver`, `encounter-balancer`, `rule-lookup`, `persona-review`. Hand-do those steps in Phase 4-5 — the experience will tell us what those skills actually need.

### Phase 4 — Adventure #1
10. `adventures/0001-tomb-of-the-silver-rose/premise.md`
11. Run `dungeon-smith` (or hand-draft mirroring the skill's contract) → rooms + ASCII map
12. Run `treasure-forger` → Silver Rose + minor loot files
13. Hand-draft encounters (defer `encounter-balancer`)
14. Run `module-binder` → `module.md`

### Phase 5 — Manual persona review of adventure #1
15. For each of 5 personas, write `reviews/<persona>-<date>.md` using the rubric.
16. Aggregate scores in `reviews/SUMMARY.md`.
17. Retrospective — what did the personas reveal? What does the eventual `persona-review` skill need to capture?

### Phase 6 — Harvest lessons
18. Build `lore-weaver`, `encounter-balancer`, `persona-review` informed by what Phase 4-5 taught us. Begin adventure #2.

## YAGNI Guardrails

- No YAML/JSON migration until we have 3+ adventures in markdown.
- No orchestrator/pipeline skill until the manual pipeline has run end-to-end at least twice.
- No publishing format (PDF, HTML, pretty web view) until someone asks to share externally.
- Reference packs grow on demand — every added file must be justified by a skill needing it.
- No `encounter-balancer`, `lore-weaver`, `persona-review`, `rule-lookup` until adventure #1 is playable and reviewed.

## Open Questions / Notes

- Dragonlance isn't CC-licensed; our lore pack paraphrases public summaries. If we ever publish, we'll need to audit for IP safety (custom names for places/people would be a pre-publish step).
- "Canonical" persona voices (Gygax, Jaquays, Moldvay — deceased) are dramatizations based on their published writing. Reviews are in-voice critique, not impersonation-for-attribution.
- Claude-as-DM (running adventures in chat) is a potential future direction; not in scope for this spec.
