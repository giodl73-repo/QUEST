---
adventure: 0001-tomb-of-the-silver-rose
tier: 1
party: 4 characters, level 3
author: human
created: 2026-04-18
revision: 2 (trimmed per Moldvay gate; detail spun to npcs/ and treasures/)
sources:
  - reference/dragonlance/ages.md
  - reference/dragonlance/geography-ansalon.md
  - reference/dragonlance/factions.md
  - reference/dragonlance/dm-notes.md
---

# Premise — The Tomb of the Silver Rose

**Logline:** A buried rose that remembers the dead for you — and forgets the living on your behalf.

## Setting

**Place:** The Rose Cairn, a weather-scoured barrow on the northern edge of the Plains of Dergoth, Abanasinia. Eight miles from the hill-village of **Varduin-by-the-Pines.** A carved stone rose set into the capstone.

**Time:** Late **Age of Might**, roughly **PC 20-80**. The tomb was sealed in **PC 100**. The Cataclysm (AC 0) has not yet come. The characters do not know it will.

## Hook

A Solamnic archivist, **Brother Laen** (full file: `npcs/brother-laen.md`), offers the party 80 gp plus a letter of Solamnic service to retrieve a "sigil of the fallen Vaenor line" from the Rose Cairn and return it unopened. The Order wishes to retire it with honors.

**He does not mention the curse.** See `npcs/brother-laen.md` for his private knowledge and behavior matrix.

## Central Artifact (seed)

The **Silver Rose of Vaenor** — a rose of moon-silver, petals hinged, made by a hedge-wizard for a grieving Knight of the Rose. It erodes the bearer's memory of loved ones over long rests, replacing their memories with fragments of its prior owners' griefs.

Full artifact file: `treasures/silver-rose.md` (appearance, presence, provenance, mechanics, curse, ending-the-curse, hooks).

Cross-skill manifest: `treasures/silver-rose-manifest.md` (symptoms the dungeon must express).

## Themes

- Fallen grandeur
- Grief weaponized
- The price of remembering
- A place the Cataclysm did not touch (and why)

## Constraints

- 6 rooms, one session (3-4 hours)
- Tier 1; party of 4 at level 3
- Non-linear map (loops + vertical element + multiple paths to the artifact)
- At least one purely atmospheric room (Stuart room)
- At least one room with multiple valid solutions (Jaquays room)
- Temporal pressure table (Cold Pulse + Wandering) for attrition (Gygax gate)
- Curse symptoms distributed across ≥3 rooms (Stuart gate)
- Read-aloud ≤ 60 words per room (Moldvay gate)
- Every named NPC has an `npcs/<slug>.md` file (Moldvay gate)

## The Real Decision

After learning what the rose does, what do the players do?

1. **Return it to Brother Laen.** Take the 80 gp (or 300 with Aelwen's Letter), walk away. No curse. Institutional cover-up confirmed.
2. **Keep it.** Attunement, creeping cost over sessions. Rose is useful. Memories go.
3. **Destroy it.** Return to the tomb under Paladine's first light; surrender the memory of their most-beloved person; a witness speaks *Caen Vaenor* aloud. The cure is its own cost.
4. **Sell it to someone worse.** Bone-Collectors of Neraka pay ~500 gp, with debt attached. Seeds adventure #0002.

## Key Files in This Adventure

- `npcs/brother-laen.md` — patron
- `treasures/silver-rose.md` — central artifact
- `treasures/silver-rose-manifest.md` — curse-symptom obligations
- `treasures/minor-loot.md` — incidental items + purpose tags
- `encounters/03-pillar-hall-attendants.md` — 4 skeletons
- `encounters/06-ilendras-armor.md` — 1 animated armor
- `encounters/wandering-pressure.md` — Cold Pulse + Wandering tables
- `rooms/map.md` — two-level ASCII map
- `rooms/01-cairn-cap.md` through `rooms/06-sarcophagus-chamber.md`

## Prior Bearers (summary)

Full provenance in `treasures/silver-rose.md`. In brief:
1. **Aelwen the Silversmith (PC 180)** — forger. Died of grief.
2. **Baron Edric of Vaenshold (PC 145)** — gifted it to Ilendra. Died two winters later.
3. **Sir Ilendra Vaenor (received PC 145, buried PC 100)** — Knight of the Rose. Stopped aging at 50.

A fourth victim died in the tomb three weeks before the adventure begins: **Vesk of the Bone-Collectors**, whose daughter **Pella** is mentioned in Room 05. See `rooms/05-rose-stair.md`.
