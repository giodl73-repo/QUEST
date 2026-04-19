---
adventure: 0001-tomb-of-the-silver-rose
tier: 1
author: module-binder
created: 2026-04-18
revision: 2
compiled-from:
  - premise.md
  - rooms/map.md
  - rooms/01-cairn-cap.md
  - rooms/02-antechamber-of-tears.md
  - rooms/03-pillar-hall.md
  - rooms/04-scriptorium.md
  - rooms/05-rose-stair.md
  - rooms/06-sarcophagus-chamber.md
  - treasures/silver-rose.md
  - treasures/silver-rose-manifest.md
  - treasures/minor-loot.md
  - encounters/03-pillar-hall-attendants.md
  - encounters/06-ilendras-armor.md
  - encounters/wandering-pressure.md
  - npcs/brother-laen.md
---

# The Tomb of the Silver Rose — DM Module

*A buried rose that remembers the dead for you — and forgets the living on your behalf.*

**Tier:** 1  |  **Party:** 4 characters, level 3  |  **Expected playtime:** one session, 3-4 hours.

## Table of Contents

1. [Summary](#summary)
2. [Hook](#hook)
3. [Setting & Background](#setting--background)
4. [Map](#map)
5. [Rooms](#rooms)
6. [Treasures](#treasures)
7. [NPCs](#npcs)
8. [Wandering Pressure](#wandering-pressure)
9. [Encounters Appendix](#encounters-appendix)
10. [DM Cheatsheet](#dm-cheatsheet)

---

## Summary

The Rose Cairn sits on a weather-scoured bluff over the Plains of Dergoth, Abanasinia. A century ago, Sir Ilendra Vaenor — a Knight of the Rose — was buried there holding a silver rose that stopped her aging but slowly erased her memory of everyone she ever loved.

A Solamnic archivist, **Brother Laen**, hires the party (80 gp) to retrieve the rose and return it to him. He does **not** mention the curse. What the party does with the rose once they learn what it is — return it, keep it, destroy it, sell it to someone worse — is the real decision of the adventure.

The tomb has two levels (cairn-cap + tomb), six keyed rooms, non-linear topology (a loop, a shaft, a shortcut that opens with curiosity), two fights (a ritual skeleton encounter and an animated armor climax) plus a conditional ghoul, and one purely atmospheric room. A Cold Pulse / Wandering Encounter table gives the tomb temporal pressure. A Curse Symptoms Manifest obliges the tomb to *show its sickness* — attribution drift, a misspelled name, a repeated phrase, a fresco that heals for a heartbeat when the rose is taken.

## Hook

Brother Laen — Knight of the Crown, mid-30s, clerk to the Rose Council — meets the party at a fortified way-house in the hill-village of **Varduin-by-the-Pines**, eight miles from the cairn. Offer:

- **80 gp** and a letter of Solamnic service to any member of the party who wants one.
- The task: retrieve a "sigil of the fallen Vaenor line" from the Rose Cairn and return it, unopened, to him.
- The Order wishes to retire it with honors.

**What he is not saying:** see [NPCs](#npcs) for Brother Laen's private knowledge, behavior matrix, and raised offers (up to 400-500 gp) if the party presents Aelwen's Letter or demands to know the curse.

If pressed hard (DC 16 Insight), he admits: *"It is not a simple sigil. The Council wishes it sealed."*

## Setting & Background

**Era:** Late Age of Might, approximately **PC 20-80**. The Cataclysm has not yet come; the characters do not know it will.

**Region:** Northern edge of the Plains of Dergoth, Abanasinia. Cold spring; wind across short-grass plains; Kharolis peaks visible to the south. Nearest settlement: Varduin-by-the-Pines (where Brother Laen is based; also Laen's mother's village).

**The Cairn:** Built in **PC 100** for Sir Ilendra Vaenor. Sealed since. The Cataclysm, a century later, did not touch it. That is an unusual fact. Something about this cairn repels divine disaster — either Paladine's own protection of a Rose Knight, or the rose's memory-eating grip on Krynn's attention.

**Who Ilendra was:** A minor Knight of the Rose whose brother Caen died in the Third Dragon War. Aelwen the silversmith of Vaenshold forged her a rose of remembrance that became a device of grief. She served with distinction, stopped aging at 50, kept a written list of the living. Asked to be interred holding the rose.

**Who else is interested:** The **Bone-Collectors of Neraka**. One of their scouts — **Vesk** — descended into the cairn three weeks before the adventure opens. The party will find him, living or dead, in Room 05.

---

## Map

Two levels. Cairn-cap (Level 0, surface) and Tomb (Level -1, cut into the bluff). Scale: 1 square ≈ 10 ft.

**Legend:** `[N]` keyed room · `=` door · `=?=` sealed · `||` wall · `/` `\` stair · `*` shaft · `~` wind-worn · `#` cairn-stone.

### Level 0 — Cairn-Cap (Surface)

```
               (wind / open plain)
                  ~~~~~~~~
                  ~[1]~~~~       Room 1 — The Cairn-Cap
                  ~ # # ~
                    / \
                    \ /          stair down (~15 ft)
                     |
```

### Level -1 — Tomb

```
                     |                (stair from 1 arrives here)
                     v
                +---[2]---+          Room 2 — Antechamber of Tears
                |  W   E  |          (weeping wall; bowl; VANOR lintel)
                +--|-+-|--+
                   | | |
           +-------+ | +-------+
           |                   |
        +-[4]-+             +-[3]-+    Room 3 — Pillar Hall (east; click-scrape)
        | LEC |             | PIL |    Room 4 — Scriptorium (west; vellum-smell)
        | TER |             | LAR |
        |  *  |             |     |
        | (shaft  = = = = = (stair
        |  down               down
        |  to 5   =?=          to 5)
        |  sealed)            |
        +-|---+             +-|---+
          |                   |
          v                   v
          +----+     +--------+
               |     |
              +-[5]-+                  Room 5 — The Rose Stair (Vesk)
              | === |
              +--|--+
                 |
                 v
              +-[6]-----+              Room 6 — Sarcophagus Chamber
              |   SRC   |
              +---------+
```

### Connections Table

| From | To | Type | Notes |
|---|---|---|---|
| 1 | 2 | Stair (down, ~15 ft) | Capstone Athletics DC 13 to lever |
| 2 | 3 | Open archway (east; click-scrape) | — |
| 2 | 4 | Open archway (west; vellum-smell; VANOR lintel) | — |
| 3 | 5 | Stair (down, ~10 ft) | — |
| 4 | 5 | Shaft (down, ~10 ft) | Sealed until 2+ books read, OR DC 17 Arcana, OR DC 15 Religion, OR DC 20 Athletics |
| 5 | 6 | Door (unlocked) | Inscribed: *Est Sularus oth Mithas* |

**Topology summary:** 6 rooms, 1 loop (2→3→5→4→2 once shaft opens), 3 vertical elements, 2 paths to the artifact, 1 earned shortcut.

---

## Rooms

### Room 01 — The Cairn-Cap

**Read-aloud:**
> A shoulder of stone-and-turf crowns the bluff. Black pines lean from the wind. At the cairn's center, a flat capstone — carved with a rose so worn you could miss it. Cold air rises from around its edge: the stone is not flush. Something is beneath it.

**Features:**
- **Capstone:** Athletics DC 13 to lever; two cooperating characters auto-succeed. Reveals stair down (~15 ft) to Room 02.
- **Rose carving:** Investigation DC 13 — re-carved over an earlier defaced sigil. DC 15: the older line reads *"Sister of Caen."*
- **Wind:** Survival DC 10 — no insect, no bird-call. Unnaturally quiet.

**Encounter:** None.

**Treasure:** None. (The "Sister of Caen" inscription is free foreshadowing.)

**Connections:** Down to Room 02.

**GM Notes:** Do not narrate the place as "haunted" — let the wind and the quiet do the work. Brother Laen stays at the way-house.

**Memory Fragment (optional):**
> *Aelwen the silversmith walked this path once, on a spring morning not unlike this one, to deliver a rose to a Baron. She remembered the walk. Later, she could not remember her daughter's name.*

---

### Room 02 — The Antechamber of Tears

**Read-aloud:**
> The stair ends in a round chamber, twenty feet across. Water weeps from one wall in a slow silver line, collecting in a stone bowl sunk into the floor. The bowl is half full. The air is cold and tastes of iron. Two archways leave the chamber, east and west.

**Features:**
- **Weeping wall (north):** seepage at the pace of tears. Drinkable.
- **Stone bowl (floor, center):** Arcana DC 12 — warded never to overflow.
- **The air:** Wisdom save DC 10. On **failure**, the character hears *"... and the winter was colder than any I have known ..."* — ask the player to write the fragment down. **This phrase repeats verbatim in Room 06 when the Rose is taken.**
- **East archway:** a faint *click-scrape* carries from beyond — stone settling. Leads to Room 03.
- **West archway:** a dry smell — old vellum, parchment dust, ink. Above the lintel, chiseled deep: **VANOR.** Investigation DC 13 — the carver meant to spell *Vaenor* and did not correct the slip. The tomb is forgetting the name of the woman it holds. Leads to Room 04.

**Encounter:** None. This is the Stuart room.

**Treasure:** None.

**Connections:** Up (stair) to Room 01; east to Room 03; west to Room 04.

**GM Notes:**
- The VANOR inscription is a curse symptom. Don't explain. If later the party sees *Vaenor* spelled correctly elsewhere and notices the disagreement, shrug.
- The repeated phrase — *"and the winter was colder than any I have known"* — will repeat verbatim in Room 06. Write it in your notes. Say it the same way both times.

**Memory Fragment (optional):**
> *Aelwen forged in the dark. She said afterward that the rose wanted the nights — she had tried to work in sunlight and could not, her hands would not hold steady. In the dark her hands worked without her. She wrote a letter in those nights she did not send.*

---

### Room 03 — The Pillar Hall

**Read-aloud:**
> Eight pillars, two rows of four, support a low vaulted ceiling. Each pillar is carved with a rose — some defaced, slashed across. The mosaic floor shows a woman in Solamnic plate accepting a silver rose from a figure whose face has been chiseled away. A stair descends through the far wall.

**Features:**
- **Eight pillars.** Three are scored from *inside the tomb* (Investigation DC 13); strike-marks are rose-petal-shaped.
- **Easternmost pillar** bears an inscription near its base: *"We do not carry the dead within us. We carry the shape of ourselves against their absence. — Aelwen."* A careful party (Investigation DC 12) will later see the same sentence in Room 06, **uncredited.** The rose has taken Aelwen's name from one of the two.
- **Mosaic floor:** Ilendra receiving the rose from a faceless figure. History DC 13; Investigation DC 15 — scouring post-dates the laying.
- **Stair (east wall):** ten feet down to Room 05.
- **Silence:** tightens when the party crosses the centerline between pillar-rows — triggers the encounter.

**Encounter — The Pillar Hall Attendants** *(triggered by crossing centerline):*

4 × Skeleton (SRD, CR ¼, 50 XP each; 200 XP base × 2 multiplier = **400 adjusted XP**).

- **AC** 13 · **HP** 13 · **Speed** 30 ft. · Darkvision 60 ft.
- Vulnerabilities: bludgeoning. Immunities: poison; exhaustion, poisoned.
- **Shortsword:** +4, 1d6+2 piercing. **Shortbow:** +4, 80/320 ft, 1d6+2 piercing.
- One carries the **Notched Longsword** (treat as shortsword mechanically; the notch is the key to Room 06 Option B).

**Tactics:** Silent attacks. Use pillars for cover (half-cover, effective AC 15). Flank. **Do not pursue across the centerline backward.** Collapse at 0 HP; re-rise only on a new party-crossing.

**After combat:** Religion DC 15 — bones bear no necromantic aura. They are not undead in the spell-sense. They are *held.*

**Treasure:**
- **Notched Longsword** (15 gp scrap; **KEY** to Room 06 Option B).
- **Attendants' gravegoods:** 25 gp Ergothian mintage (50 gp to collector).
- **Pillar-rubbing** if taken: evidence.

**Connections:** West to Room 02; east (stair down) to Room 05.

**GM Notes:**
- The skeletons are *attendants performing a duty,* not raucous undead. Describe as ritual.
- The attribution-drift inscription on the easternmost pillar pairs with Room 06's Panel 3 caption. A party that tracks this has solved the tomb's sickness on a textual level.

**Memory Fragment (optional):**
> *The Baron held the rose once, on the ride home from Aelwen's shop, and that night he woke weeping for a man he could not name. The man's name was his son's. He never told his daughter he had held the gift first.*

---

### Room 04 — The Scriptorium

**Read-aloud:**
> Three stone lecterns stand in a triangle; on each, a small bound book. The far wall is painted — a funeral. Bearers carry a young man's body down a hillside. A woman in Solamnic plate stands apart, watching. In the floor before you, a round iron shaft-cover set with a silver rose.

**Features:**
- **Book I — A Knight's Elegy.** Ilendra's annotations; she writes *to* her brother Caen.
- **Book II — On Memory.** Ilendra underlined: *"We do not carry the dead within us. We carry the shape of ourselves against their absence."* Below, in her hand: *"as Aelwen said to my father."* **(Same sentence will appear in Room 06's Panel 3 caption, uncredited.)**
- **Book III — A Silversmith's Letter.** Signed Aelwen. *"When I held it, I began to forget my own daughter's face..."* (first prior owner's warning).
- **Funeral fresco (north wall):** young man carried downhill; same woman from Room 03 mosaic, but here her face is *not defaced.* History DC 13 — predates Ilendra's burial by 80+ years.
- **Shaft in floor (center):** circular iron plate, silver rose inlaid, sealed.

**Unlocking the shaft (any ONE works):**
1. **Narrative:** Read any 2 of 3 books (5 min each, no check). Shaft-rose irises open.
2. **Arcana DC 17.**
3. **Religion DC 15** (prayer to Paladine).
4. **Athletics DC 20** to pry — success cuts the character 1d4 slashing.

**Encounter:** None.

**Treasure:**
- Book I annotations (0 / 30 gp to historian — roleplay artifact).
- Book II (15 gp to scholar; **attribution-drift setup**).
- Book III — Aelwen's Letter (priceless as evidence; changes Brother Laen negotiation entirely).

**Connections:** East to Room 02; down (shaft) to Room 05.

**GM Notes:**
- Do not push players toward the books. Reward curiosity; don't railroad.
- The attribution drift (Book II → Room 06 Panel 3 caption) is only noticed by a party that reads Book II carefully and then examines Room 06's frescoes. Don't explain.

**Memory Fragment (optional):**
> *Baron Edric wrote in a journal he later burned: "I understood at the end what Aelwen had begged me to hear. I could not remember whether I had understood it for a day, or a year, or whether I had been understanding it in the wrong tense the whole time. I forgot her daughter's name also. Her daughter was named for my wife."*

---

### Room 05 — The Rose Stair

**Read-aloud:**
> A small vestibule, square and low. To your right the stair you descended; above, a circular shaft — cold air sighs through it. A dead brazier stands by a single oaken door. Above the lintel, chiseled deep: *Est Sularus oth Mithas.*

**Features:**
- **Stair (south):** up to Room 03.
- **Shaft (ceiling):** up to Room 04 once opened. Climb DC 10.
- **Brazier (dead):** Investigation DC 13 reveals: a silver rose-petal pressed into the ash AND, scratched into the ash with what looks like a fingernail — or a bone — a name: **VESK**. Beside it, smaller: **PELLA.**
- **Door (north, oak + iron-banded):** unlocked. Solamnic Oath inscription. A Solamnic-trained character speaking the words aloud causes the door to open silently (roleplay beat).
- **The air:** dry. Unusually so.

**Who Vesk was:** A Bone-Collector scout of Neraka, 46, killed in this room three weeks ago by the rose's residue. Father of Pella, 9, living in a waystation north of Neraka with his sister. Vesk had not seen his daughter in three years. When the rose began taking his memory of her, he chose to write her name — with his own arm-bone as stylus, his own blood as ink — so someone would know her name at all costs.

**Encounter (CONDITIONAL):** If the party was **loud** in Rooms 03 or 04 (combat triggered, OR brute-force solution):

1 × Ghoul (Vesk; SRD, CR 1, 200 XP).

- **AC** 12 · **HP** 22 · **Speed** 30 ft. · Darkvision 60 ft.
- Immunities: poison; charmed, exhaustion, poisoned.
- **Bite:** +2, 2d6+2 piercing.
- **Claws:** +4, 2d4+2 slashing; **non-elf humanoid** DC 10 Con save or paralyzed 1 min (repeat end-of-turn).
- Tactics: ambush from behind brazier. Priority: claw (paralysis). Retreat below 5 HP toward door he came in.

**If NOT triggered:** Vesk's desiccated corpse, long still. Medicine DC 12 — gnawed through own left arm not for food but as a *writing tool.*

**Treasure:**
- **Silver rose-petal in ashes:** 25 gp silver; unsettling to any future rose-attuner.
- **Vesk's Bone-Collector signet:** 10 gp; **faction clue seeds adventure #0002.**
- **Pella's crayon drawing** (Vesk's rag-pocket, Investigation DC 13): 5 gp sentimental; **KEY — unlocks Memory Echo's second line in Room 06.**

**Connections:** Up (stair) to Room 03; up (shaft, DC 10) to Room 04; north (door) to Room 06.

**GM Notes:**
- Vesk's names are the moral weight of this room. He is not the villain. His last act was to remember. A player who notices and cares has an answer ready when Room 06 asks them what they will give up.

**Memory Fragment (optional):**
> *Vesk, on the third day: "I will not look at the rose again. I will think of her face. I will think of her face. I will think of her —" And he forgot the word he was reaching for, and picked up the bone, and began to scratch her name in the ash.*

---

### Room 06 — The Sarcophagus Chamber

**Read-aloud:**
> An octagon, twenty feet across. In the center, a sarcophagus of pale stone, carved as a knight in repose — hands crossed on the breastplate. A silver rose is set into the breastplate between her hands, petals folded shut. Frescoes cover the walls — a life, in panels — and each panel is scored across, the same pattern, again and again.

**Features:**
- **Sarcophagus (central):** pale limestone, 8 ft long. Sir Ilendra Vaenor in Knight of the Rose plate. Stone hands crossed; silver rose set between them, petals folded shut. Her **right stone fist** is closed around nothing — Investigation DC 15 reveals a hidden slot sized for a sword-tip.
- **Frescoes (8 panels):** Ilendra's life. **Panel 3 (Caen's death in battle)** bears a caption: *"We do not carry the dead within us. We carry the shape of ourselves against their absence."* — **uncredited.** (A party that read Book II in Room 04 will recall this sentence was attributed to Aelwen. The rose has taken Aelwen's name.) All panels **except #4** are scored rose-petal-shaped.
- **Air:** colder than Rooms 02-05. Still dry.
- **Silence:** holds a beat when weapons are drawn, then sound returns.

### Retrieving the Rose — Three Options

- **Option A — Brute.** Athletics DC 15 to lever open the sarcophagus lid. Loud. **Triggers the Armor.** Inside: Ilendra's remains; silver pendant (40 gp, not cursed).
- **Option B — The Notched Longsword Key.** Insert the Room 03 notched longsword into the hidden slot in Ilendra's stone fist. The breastplate-clasp releases silently. **The Armor does NOT animate.** Reward for thoroughness.
- **Option C — Smash.** Athletics DC 18 with a heavy weapon to break the breastplate carving. Loud + destructive. **Triggers the Armor AND the Memory Echo mid-combat** (worst outcome).

### Encounter — Ilendra's Armor *(triggered by Options A or C)*

1 × Animated Armor (SRD, CR 1, 200 XP).

- **AC** 18 · **HP** 33 · **Speed** 25 ft. · Blindsight 60 ft.
- Immunities: poison, psychic; blinded, charmed, deafened, exhaustion, frightened, paralyzed, petrified, poisoned, stunned.
- **Antimagic Susceptibility:** incapacitated in *antimagic field*; *dispel magic* = Con save or unconscious 1 min.
- **False Appearance.**
- **Multiattack:** 2 slam attacks.
- **Slam:** +4, 1d6+2 bludgeoning.

**Tactics:** Priority = whoever is closest to the Rose (or carrying it). Does not pursue out of room. Cold deliberation. At 0 HP sags to a seated position against the east wall and ceases.

### The Memory Echo (non-statted)

When the Rose is taken (any option), a translucent figure of Ilendra at age 50 appears briefly by the sarcophagus.

- She speaks one sentence: *"Tell my brother I did not forget."* Then she fades.
- The room hushes for her sentence even mid-combat; the Armor (if fighting) pauses a beat, then resumes.

**Interaction rules:**
- Cannot be touched (hand passes through).
- Answers only to *"my brother,"* not to questions about the rose.
- A character who speaks **Caen** aloud: she weeps silver light for a heartbeat — recognition. Ask the player what it was like.
- **A character who shows her Pella's drawing (from Room 05) and speaks of remembering:** she turns her head, smiles, and says a second sentence — *"Then someone is still remembering."* Then fades as usual. **This is a gift for players who paid attention in Room 05.**
- Wisdom (Insight) DC 12: she does not remember that her brother is dead.

### The Reaction Moment — the Fresco Heals

At the moment the Rose is lifted (any option), **Panel 6 of the frescoes** (Ilendra at her parents' funeral) **heals for one heartbeat.** The scoring retreats; the faces are visible — a man and a woman, aged, both with Ilendra's cheekbones. Then the scoring re-etches itself and the faces are gone.

A character watching may make Wisdom (Perception) DC 12 to glimpse the faces clearly. **The DM asks the player what the parents looked like. The player answers.** Write it down. The rose has returned memories it stole — they belong to the player now.

Simultaneously, **Panel 3's caption briefly reacquires its attribution** — *— Aelwen* visible at the caption's end, for the same heartbeat, then gone.

### The Repeated Phrase

At the instant the Rose is lifted, the DM says — softly, as narration, not in any voice:

> *"And the winter was colder than any I have known."*

If any player reacts — if they recognize the phrase from Room 02 — the DM does not confirm. Just keeps going.

**Treasure:**
- **The Silver Rose of Vaenor** — see [Treasures](#treasures).
- **Ilendra's Silver Pendant** (in sarcophagus, Option A or C only): 40 gp, NOT cursed.
- **Ilendra's sword** (in sarcophagus): 50 gp (150 to the Order).
- **Ilendra's armor** (post-fight): 75 gp merchant / 250 to the Order.

**Connections:** South (door) to Room 05.

**GM Notes:**
- Let them see the frescoes before the fight. Let them understand what they are standing in.
- The fresco heal is a single heartbeat — narrate it fast. Players who catch it feel they caught something.
- The Pella-drawing interaction is a reward for Room 05 engagement. Do not volunteer.
- When they leave with the rose, the wind outside is suddenly warm — unseasonably so. The cairn has finished its work.

**Memory Fragment (optional):**
> *Sir Ilendra, at twenty-six, when the rose first touched her palm: "It was cold, and it fit. I understood, for a moment, that if I held it I would not have to carry what I had been carrying. I did not yet know that what I had been carrying was who I had loved, and what I would be given instead would be who she had loved, and that a century later I would not know the difference. I would know only that there had been grief, and that grief was mine now, and that I could go on."*

---

## Treasures

### The Silver Rose of Vaenor *(central artifact)*

*A rose of moon-silver, petals hinged sharp as razors. It is cold even through a glove.*

**Appearance:** ~4 inches across, moon-silver alloy, 7 petals hinged to fold shut like a fist, barbed stem, always colder than ambient air.

**Presence / Desire:** The rose wants to be held, and it wants to be held *by the right hand.* It is drawn to the grief-carrier in the party — the character who has lost the most. In that hand it warms by a quarter-degree and fits, too well, the cup of the palm. In the hand of the ungrieving, it stays cold, the barbed stem angling inward. Set down, it does not tarnish; left untouched too long, it grows perceptibly colder and the air around it dries, as if calling to be picked up.

It is silent. It does not speak. But it has preferences. It fits in some pockets, not others. It chimes faintly — once, softly, in its lifetime — when the bearer passes near something it remembers. It will not be carried in a bag with food. It prefers to be held.

**Rarity:** Rare (reads as uncommon without attunement).

**Attunement:** Required. No class/alignment prerequisite.

**Provenance:**
1. **Aelwen the Silversmith of Vaenshold (PC 180)** — forger. Began forgetting her daughter's face during the work. Hanged herself a year later.
2. **Baron Edric of Vaenshold (PC 145 given; PC 143 died)** — gave it to his daughter Ilendra. Died two winters later.
3. **Sir Ilendra Vaenor (received PC 145, buried PC 100)** — Knight of the Rose. Stopped aging at 50. Asked to be interred holding the rose.

(Fourth, recent victim: **Vesk the Bone-Collector** — died in Room 05 three weeks ago.)

**Benefits (while attuned):**
- **Steady Heart.** Advantage on saves vs. frightened / charmed.
- **Relic of the Lost.** Once per long rest, ask the rose about any named deceased person — the rose answers one true fact.
- **Silent Step.** Proficiency in Stealth while holding.

**Curse — Memory Erosion:**
- End of each long rest: **DC 11 Wisdom save** or lose a memory of a loved one; replaced with a fragment of Ilendra's grief for Caen.
- **First reveal on the third long rest** — player is asked to describe memories lost on rests 1 and 2 and realizes they cannot.
- DC increases by 1 per failed save, max 18.

**Ending the Curse:**
1. Rose returned to its cairn (Room 06) under Paladine's first light (Solinari waxing).
2. Bearer voluntarily surrenders the memory of their most-beloved *living* person (or dearest deceased). Permanently consumed.
3. A witness speaks **Caen Vaenor**'s name at the moment of surrender.

Lesser effects (*remove curse*, *greater restoration*) suspend the loss for spell duration; next rest resumes. Already-lost memories never return.

**Hooks:**
- **Bone-Collectors of Neraka** tracking the rose (adventure #0002).
- **Brother Laen** will pay up to 400-500 gp for quiet surrender if pressed.
- **House Vaenor-Meryn** (surviving cousin line) will pay to see the rose.
- **Ilendra's list of names** — returning stolen memories to families is a campaign arc.

### Minor Loot Index (items with Purpose)

| Item | Room | Purpose | Value (gp) |
|---|---|---|---|
| Ergothian mint coins | 3 | Coin + setting-ground | 25 (50 to collector) |
| Notched Longsword | 3 | **KEY** (R6 Option B) + Evidence | 15 scrap |
| Scored pillar-rubbing | 3 | Evidence | 0 |
| Book I (Ilendra's annotations) | 4 | Roleplay trigger | 0 / 30 to historian |
| Book II (On Memory) | 4 | Attribution-drift setup | 15 |
| Book III (Aelwen's Letter) | 4 | **KEY** (Brother Laen neg.) | priceless as evidence |
| Silver rose-petal | 5 | Evidence + foreshadow | 25 silver |
| Vesk's Bone-Collector signet | 5 | Faction clue → #0002 | 10 |
| Pella's crayon drawing | 5 | **KEY** (Memory Echo 2nd line) | 5 sentimental |
| Ilendra's Silver Pendant | 6 | Recognition token | 40 |
| Ilendra's sword | 6 | Coin + roleplay | 50 (150 to Order) |
| Ilendra's armor post-fight | 6 | Coin | 75 (250 to Order) |

---

## NPCs

### Brother Laen of the Rose Council's Clerkwork

A Knight of the Crown in his mid-thirties, Solamnic clerk to the Rose Council. Narrow man, ink-stained fingers, tabard one size too large. Soft-spoken, avoids eye contact during the hard parts of conversations. Carries an almost-empty leather folio everywhere.

**Stat block (Knight, SRD reskin):** AC 18 (plate + shield) · HP 35 · Speed 30 ft · Str 14, Dex 10, Con 13, Int 12, Wis 12, Cha 13 · Saves Con +3, Wis +3 · Skills History +3, Insight +3, Persuasion +3 · Brave (adv. vs. frightened) · **Longsword** +4, 1d8+2 slashing. Will not initiate combat; runs if hostile.

**Public story:** The Silver Rose is a "sigil of the fallen Vaenor line"; the Order wishes to retire it with honors. 80 gp on return, plus letter of Solamnic service.

**Private story:** The Rose Council has kept a file on the rose for a century. It was not sanctioned by the Wizards of High Sorcery. It erodes memory. Sir Ilendra's list of names is in the Council's vault. If publicly acknowledged, the Order would have to explain why a Rose Knight carried an unsanctioned relic. No explanation exists that does not embarrass the Order.

**Behavior matrix:**

| Party does... | Brother Laen does... |
|---|---|
| Accepts hook, returns rose, leaves | Pays 80 gp. Gratitude. Clean end. |
| Asks what the rose does | Deflects: "A sigil of the Vaenor line." |
| Presses (Insight DC 16) | Low voice: *"It is not a simple sigil. The Council wishes it sealed."* |
| **Presents Aelwen's Letter** | Goes quiet. **Raises offer to 300 gp.** Takes letter as "archive material." |
| Demands to know curse directly | Admits it at the way-house. **Offers up to 400 gp.** Requires a Solamnic-sealed vow of silence. |
| **Presents letter AND refuses surrender** | **Offers 500 gp + letter of service + a Council favor.** If still refused: retreats, reports, adventure #0002 begins within a tenday. |
| Keeps rose without surrender | Pays 80 gp as agreed (bound by oath). Forty days later, Solamnic retrieval team — three Knights of the Sword. |
| Kills Brother Laen | Varduin finds his body. Order opens investigation. Within a season: Solamnic enemies from Abanasinia to Palanthas. Campaign-ending if careless. |

**Private motive:** His younger sister **Wena** is a novice with the Revered Daughters of Paladine. A public scandal around the rose would reach her cloister. He believes (rightly or wrongly) that the Council has quietly used her position as leverage for his discretion. **Insight DC 18** during a long conversation: he carries two things in his folio — a blank page and a small letter in a woman's hand that he touches when he thinks no one is watching.

**Notes:** Full name **Laen of Varduin-by-the-Pines**. Came to the Order through local patronage, not a knight's pedigree. His mother still lives in Varduin; she has heard from him and is not discreet.

---

## Wandering Pressure

**Cold Pulse Table** — roll d6 every **10 min** in the tomb (Rooms 02-06). Stops in Room 06.

| d6 | Effect |
|---|---|
| 1 | Nothing. |
| 2 | A hush — no sound for three heartbeats. |
| 3 | Cold deepens. Con save DC 10 or **1 point of exhaustion** (fades outside tomb). |
| 4 | A forgotten word — one random PC can't recall a home-settlement NPC's name for 1 min (roleplay; no penalty). |
| 5 | Distant weeping — Investigation DC 15 localizes to Room 02 regardless of current location. |
| 6 | The rose stirs — if retrieved, it warms in the bearer's hand 1 min; if not, a single petal-chime from Room 06. |

**Wandering Encounter Table** — roll d6 every **30 min** in the tomb.

| d6 | Encounter |
|---|---|
| 1-2 | Nothing. |
| 3 | **Bone-Collector scout (Bandit, SRD CR ⅛)** climbs into Room 01. Perception DC 13 to notice. Carries Nerakan signet. |
| 4 | **Collapse.** A corridor partially collapses (DM choice). DC 12 Acrobatics passing through or 1d4 bludg + prone. |
| 5 | **Second ghoul** (SRD CR 1) from a fresh crack in Room 05 wall. If Vesk already fought: this replaces; if corpse-variant: emerges from the corpse's location. |
| 6 | **The tomb speaks.** DM whispers one memory-fragment (from any room visited) to a random PC only. No effect; roleplay beat. |

Do not force-trigger either table. Let the dice do the work. Threat matters as much as reality.

---

## Encounters Appendix

**Skeleton (×4, Room 03):** AC 13 · HP 13 · Vulnerable bludg; immune poison, exhaustion, poisoned. Shortsword +4, 1d6+2 piercing. Shortbow +4, 80/320, 1d6+2 piercing. CR ¼, 50 XP.

**Ghoul — Vesk (×1, Room 05, conditional):** AC 12 · HP 22 · Immune poison; charmed, exhaustion, poisoned. Bite +2, 2d6+2 piercing. Claws +4, 2d4+2 slashing; non-elf humanoid DC 10 Con save or paralyzed 1 min. CR 1, 200 XP.

**Animated Armor (×1, Room 06):** AC 18 · HP 33 · Immune poison, psychic; many conditions. Antimagic Susceptibility · False Appearance. Multiattack: 2 slams. Slam +4, 1d6+2 bludg. CR 1, 200 XP.

**XP Thresholds (4 PCs, L3):** Easy 300 · Medium 600 · Hard 900 · Deadly 1,600. Adjusted multipliers: 1 mon ×1, 2 ×1.5, 3-6 ×2.

---

## DM Cheatsheet

### Quick References — Key DCs by Room

- **R1:** Athletics 13 (capstone) · Investigation 13/15 (rose carving) · Survival 10 (wind)
- **R2:** Wisdom save 10 (voice-fragment) · Arcana 12 (bowl ward) · Investigation 13 (VANOR slip)
- **R3:** Investigation 12 (Aelwen-attributed inscription) · Investigation 13 (pillars scored inside) · Investigation 15 (mosaic date) · Religion 15 post-combat (no necro aura)
- **R4:** Arcana 17 OR Religion 15 OR Athletics 20 (shaft) · History 13 (fresco predates burial)
- **R5:** Investigation 13 (rose-petal in ashes + Vesk/Pella names + Pella's drawing) · Medicine 12 (self-gnawed arm as writing tool) · Climb DC 10 (shaft)
- **R6:** Athletics 15 (A lid) · use Notched Longsword + Investigation 15 (B slot) · Athletics 18 (C smash) · Insight 12 (Ilendra forgot brother is dead) · Perception 12 (fresco-heal faces)

### Key saves

- Skeleton encounter: standard.
- Vesk paralysis: **non-elf humanoid DC 10 Con save or paralyzed 1 min (repeat end-of-turn).**
- Silver Rose curse: **DC 11 Wisdom save** at end of long rest; DC +1 per fail, max 18.
- Cold Pulse: **DC 10 Con save** or 1 exhaustion (outcome 3 only).

### Attunement rules (inlined)

- **Short rest (1 hour)** focused on item to attune.
- **3 magic items attuned per character max.**
- **Curse revealed on attunement** (for the Silver Rose: first reveal on the **third long rest** specifically).
- *Remove curse* suspends memory-loss for spell duration; next rest resumes. *Greater restoration* same.

### Conditions used (inlined)

- **Paralyzed:** incapacitated; can't move or speak; auto-fails Str/Dex saves; attacks have advantage; any attack that hits from within 5 ft is a critical hit.
- **Exhaustion Level 1:** disadvantage on ability checks. (Max level this adventure can inflict: 1, via Cold Pulse outcome 3.)
- **Frightened:** disadvantage on ability checks and attacks while source is in line of sight; can't move closer to source.
- **Charmed:** can't attack charmer; charmer has advantage on social checks vs. charmed.

### XP Budget (4 PCs, L3)

Easy 300 · Medium 600 · Hard 900 · Deadly 1,600. (Per-party totals, adjusted per monster count.)

### Scene Triggers

- **Brother Laen asked about the curse** → Dissembles unless DC 16 Insight; then: *"It is not a simple sigil. The Council wishes it sealed."* Never volunteers memory-loss.
- **Rose taken, no Options disturb the sarcophagus** → Impossible; rose is set in stone. Direct them to Options A/B/C.
- **Curse reveals in play** → On bearer's 3rd long rest while attuned, ask them to describe memories lost on rests 1 and 2. They can't. Let the silence sit.
- **Party destroys the rose early** → Ordinary weapons mark but don't harm it. Only High Sorcery ritual. Roleplay the frustration.
- **Party keeps rose, doesn't tell Laen** → He pays 80 gp. Seeds Solamnic retrieval in later adventures.
- **Party sells to Bone-Collectors** → ~500 gp with implied debt. Seeds adventure #0002.
- **Party kills Brother Laen** → Order investigates; within a season, Solamnic enemies everywhere. Campaign-ending for careless parties.
- **Party avoids Room 04 entirely** → Fine. No Aelwen's Letter, no warning — the curse lands harder.
- **Party uses Option B (Notched Longsword)** → No Armor fight. Memory Echo, fresco heal, take rose, leave in silence. Best outcome.
- **Party brings Aelwen's Letter to Brother Laen** → 300 gp offered. Laen accepts letter as archive material.
- **Player shows Memory Echo Pella's drawing + speaks of remembering** → Ilendra smiles; says *"Then someone is still remembering."* Fades.
- **Player speaks "Caen" aloud in Echo's presence** → She weeps silver light for a heartbeat.
- **Party watches Panel 6 when rose is lifted** → Perception DC 12: faces visible for one heartbeat. Ask player what they looked like. Write it down.
