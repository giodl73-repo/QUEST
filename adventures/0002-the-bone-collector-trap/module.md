---
adventure: 0002-the-bone-collector-trap
tier: 1
author: module-binder
created: 2026-04-18
revision: 2 (post-5-persona-review; applies all priority-1/2/3 fixes)
rubric-compliance: v1.1
compiled-from:
  - premise.md
  - rooms/map.md
  - rooms/01-waystation.md
  - rooms/02-pursuit-and-trap.md
  - rooms/03-stronghold-common.md
  - rooms/04-stable-yard.md
  - rooms/05-vault-approach.md
  - rooms/06-reliquary-vault.md
  - rooms/07-cell-block.md
  - rooms/08-varduin-return.md
  - npcs/pella.md
  - npcs/keloth.md
  - npcs/mensa.md
  - treasures/reliquary.md
  - treasures/reliquary-manifest.md
  - treasures/minor-loot.md
  - encounters/trap-ambush.md
  - encounters/stronghold-guards.md
  - encounters/vault-climax.md
  - encounters/wandering-pressure.md
---

> **Revision 2 (2026-04-19).** All 5-persona panel suggestions applied. Key changes: climax baseline raised (was hard/deadly; now deadly/deadly+); Vault wall-ledger added with cross-adventure signal (*"I will not look at the rose again"* — verbatim from #0001); Cell-Block interior layers (tally-marks, chalk figure, floor-stain); Scene 08 Varduin-return added as landing scene (Gygax's ride-home sketch); two shelf-reliquaries named with family-locations (Haena of the Fourth House, Sergeant Hern); empty reliquary made visibly prepared; Pella's interior committed at the Aelric-recognition beat; partial ledge in well-shaft (future hook); Alert well-guard sub-encounter added. Cheatsheet gains: Keloth-trade decision table, attribution-drift tracker, updated scene-triggers.

# The Bone-Collector Trap — DM Module

*Compassion walks north with a child's drawing and finds the drawing already on the table.*

**Tier:** 1  |  **Party:** 4 characters, level 3 (ends at L4)  |  **Expected playtime:** one session, 3-4 hours.

## Table of Contents

1. [Summary](#summary)
2. [Hook](#hook)
3. [Setting & Background](#setting--background)
4. [Map](#map)
5. [Scenes](#scenes) (includes Scene 08 Varduin-return, rev 2 addition)
6. [Treasures](#treasures) (rev 2: named shelf-reliquaries; empty-reliquary appearance)
7. [NPCs](#npcs)
8. [Wandering Pressure](#wandering-pressure)
9. [Encounters Appendix](#encounters-appendix) (rev 2: raised climax)
10. [DM Cheatsheet](#dm-cheatsheet) (rev 2: Keloth-trade decision table; attribution-drift tracker)

---

## Summary

Ten days after the Tomb of the Silver Rose closed, the Varduin Muster rides north to deliver a crayon drawing to a nine-year-old girl named Pella. They arrive at her aunt Mensa's waystation to find Mensa dead, Pella gone, and — on the table where Pella should have been eating breakfast — a second copy of the drawing, forged. The Bone-Collectors of Neraka took her to bait the party. The trap has already been set.

The adventure moves through three locations: the empty waystation (discovery), the Howl-Stones pass (ambush), and the ruined Istari wayhouse the cell calls *Keloth's Hand* (stronghold). Seven keyed locations total. Non-linear stronghold (loop via lower-corridors, vertical via well-shaft, earned stealth shortcut).

The climax is not a fight — it is a choice. Cell-leader **Keloth** offers the party a trade: attune to the Varran-reliquary (the preserved last-minute of Aelric's dead brother) and Pella walks free; refuse, and there is a fight, and Pella may not. The reliquary gives the attuner one minute of their lost loved one in first-person — and consumes every other memory of that person in exchange. The inverse of the Silver Rose: same grief-economy, opposite direction.

No PC is compelled to attune. The party may take the reliquary unattuned, destroy it via Grom's Reorx-shattering rite, or return it to the Rose Council like the Silver Rose. What they do with Pella — foster her in Varduin, find extended family in Neraka, let her decide — is a second, quieter decision on the ride home.

## Hook

Thera Hillfoot has been carrying Pella's crayon drawing for ten days. She announces at the way-house common room: she is leaving tomorrow, with or without the rest of the party. **Brother Laen** — nervous — offers the party:

- **20 gp travel stipend** as safe-conduct money.
- **A Solamnic safe-conduct letter** for passage through Solamnic waystations north.
- **His own private request** that they go as a Varduin-sponsored party, not as Thera alone.

He has received worrying reports from the Nerakan border since the Silver Rose was vaulted. He does not volunteer detail. If pressed: *"The Council has had ... communications. The Bone-Collectors know the Rose moved. I would prefer the Muster move openly, under Varduin's auspices, than quietly without them."*

## Setting & Background

**Era:** Late Age of Might, **PC 20**. Ten days after `0001-tomb-of-the-silver-rose` closes.

**Regional geography:**
- **Mensa's Waystation** — ~60 mi north-northeast of Varduin. Two days' ride.
- **Howl-Stones pass** — ~15 mi further north. Half-day.
- **Gavek's Rest / "Keloth's Hand"** — ~10 mi east. Half-day.

**Weather:** late spring in Abanasinia is mild. Northward, winter still holds; Nerakan border-lands carry late snow. Bring cold-weather cloaks.

**Who the Bone-Collectors are:** a small Nerakan death-cult (~11 members total in this cell), led by Keloth. They preserve last-minutes of the dying in moon-silver reliquaries — skull-shells bound with silver filigree. They believe this is a *mercy* — that grief preserved outside the body cannot poison the living. The Rose Council considers them necromantic and has long declined to engage them directly. They source their moon-silver from the same Vaenshold vein that produced the Silver Rose (traced through Aelwen's family line to Mira Vaenshold-Silversmith, currently under pressure from Keloth's cell).

**What happened two days before the session opens:**
1. The Bone-Collectors split into two groups. Seven members rode west, feinting toward Varduin — this raid burned the way-house's east wing (resolved off-screen by Solamnic backup; flagged for post-session).
2. Five members (Keloth + Idra + 3 Cultists) rode north to Mensa's Waystation, killed Mensa, took Pella, and returned to *Keloth's Hand*. One Lieutenant and two Bandits remained at the Howl-Stones to ambush the party.
3. Pella was forced to draw a second copy of her own drawing before they took her, to leave on the table — a trap-signal.

---

## Map

### Regional Map

```
        (south)
           |
      (Varduin-by-the-Pines)
           |
       (2 days' ride, north-northeast)
           |
        [1] Mensa's Waystation  <— Scene 1: discovery
           |
       (1 day's ride, north)
           |
        [2] Howl-Stones pass    <— Scene 2: trap
           |
       (~½ day east)
           |
        [3-7] Gavek's Rest      <— Scenes 3-7: stronghold
         (the cell calls it "Keloth's Hand")
```

### Stronghold Map — Gavek's Rest / "Keloth's Hand"

**Legend:** `[N]` keyed location · `=` door · `=L=` locked · `||` wall · `/` `\` stair · `*` well-shaft · `~` ruined

#### Level 0 — Upper (ruin)

```
     ~~~~~~~~~~~~~~~~~~~~~~~~~~~
     ~   [3] Common Room         ~   <— entry
     ~   (collapsed roof)         ~
     ~    || -- =L= --            ~
     ~    ||                      ~
     ~   [4] Stable Yard          ~   <— patrol + alarm bell
     ~   (well-cover under straw) ~
     ~     *                       ~
     ~     * (shaft ~30 ft down)  ~
     ~~~~~~~~~~~~~~~~~~~~~~~~~~~
              / \
              \ /  (stair from [3] to [5])
```

#### Level -1 — Lower (intact)

```
        [5] Vault Approach       <— stair arrives here
         (guard-post alcove)
             /  \
           /      \
         [6]    [7]
        Vault    Cell-Block
        (climax)  (Pella held)
         |           |
         +-- iron --+
                    *  (well rises to [4])
```

### Connections Table

| From | To | Type | Notes |
|---|---|---|---|
| (outside) | [3] | Archway (no door) | Frontal approach |
| [3] | [4] | Archway + locked door | DC 15 pick OR force |
| [3] | [5] | Stair (down, ~15 ft) | Stone |
| [4] | (well) | Well-cover, 80 lbs | Athletics DC 12 to lift; drops 30 ft to [7] |
| [5] | [6] | Corridor + iron door | DC 13 pick; Keloth has key |
| [5] | [7] | Corridor (open archway) | Guard alcove midway |
| [6] | [7] | Iron door (reinforced) | DC 15 pick; Keloth's key |
| [4] | (well) to [7] | Climb DC 10 with rope; 12 without | Stealth shortcut |

### Topology Summary

- **7 keyed locations** (2 external + 5 stronghold).
- **Loop:** [5]→[6]→[7]→[5] via corridors + iron door.
- **Vertical:** stair [3]→[5] AND well-shaft [4]↔[7].
- **Two paths to climax [6]:** frontal ([3]→[5]→[6]) vs. stealth (well→[7]→[6]).
- **Earned shortcut:** the well (Investigation DC 13 on the straw pile in [4]).
- **Branch cues:** stair clearly visible from [3]; well hidden under straw in [4] — requires investigation.

---

## Scenes

### Scene 01 — Mensa's Waystation (discovery)

**Read-aloud:**
> The waystation sits alone on the road, a low stone building with a squat chimney and a sign carved as a running horse. No smoke. No horses in the stable-yard. The door stands ajar. Two days of snow has drifted against it, undisturbed.

**Features:**
- **The door** (ajar, unmoved). Forced open from outside two+ days ago. Investigation DC 10 reads the snow.
- **Common room.** Hearth cold. A table laid for a child's breakfast — porridge bowl (frozen), a carved horse toy, *"Pella"* cut into the table edge in child's hand.
- **The second drawing.** On the table beside the porridge — **identical** to the one Thera carries. Investigation DC 10 confirms same paper, same hand. Investigation DC 15: *the signature's final letter is shaped differently* — someone else finished signing it. **This is the trap-signal.**
- **The kitchen.** Mensa's body, two days dead. Head-wound from behind; kitchen knife on the floor, clean. Medicine DC 12: killed first, then house searched. See [NPCs](#npcs) for Mensa.
- **Pella's room.** Small cot, pulled-back blankets, a one-eared stuffed wolf, a chalk-drawing of a woman on the wall beside the cot.
- **The fireplace.** Dug through. Investigation DC 13: an iron box buried in the ash, containing 8 gp, Vesk's sealed letter *"to P, when you are ten,"* and a pressed silver leaf (common silver, 2 gp).
- **Kitchen counter.** Rye-and-winter-savory bread still on the counter. Investigation DC 12 under the rising-cloth: a scrap addressed *"Varduin-by-the-Pines, care of the way-house steward, to be held for V— Vesk, when he next passes through."* Mensa did not know Vesk was three weeks dead.
- **Kitchen wall.** A small cameo — no nameplate. Investigation DC 15: the woman in the cameo was **Jannet of Crownhold**, the waystation's previous owner — a retired Solamnic armswoman, possibly Aelric's great-great-aunt. Seed for future adventure.
- **Mensa's notebook** (Investigation DC 13 on kitchen dresser, not the hearth box). Names of her dead, in Nerakan: Oneva (her mother), Kalt (her father), **Reya** (Pella's mother — the name Pella has never been told), Vesk (blank — Mensa did not know to write it), and her own pre-ruled line with date-field empty.

**Encounter:** None. Mensa dead; cell long gone.

**Treasure:**
- Vesk's sealed letter "to P, when you are ten" (KEY + roleplay).
- 8 gp.
- Pella's stuffed wolf.
- Pella's chalk-drawing of Reya.
- Mensa's notebook (Reya's name is the KEY find).
- Pressed silver leaf (2 gp).
- Jannet cameo (seed only; do not take unless specifically desired).

**Connections:** South (road to Varduin). North (road to Howl-Stones).

**GM Notes:**
- **Do not rush the waystation.** Grom may bless Mensa: *"Thou'rt seen. Reorx keep thy forge warm."* One minute in-fiction; character weight.
- **The second drawing is the trap-hint.** A thoughtful player realizes: *they wanted us to know Pella was here.* Let this land without prompting.
- **First-use gloss:** "Bone-Collectors" — small Nerakan death-cult, trade in artifacts of grief. Deliver via Kessa or a cataloging aside.
- **Decide: bury Mensa now or handle on return.** Either is valid.

**Memory Fragment (optional):**
> *Mensa, two days ago, had been singing. Pella did not often hear her aunt sing. Mensa had sung a song her own mother used to sing, in a voice Mensa did not know she had, and Pella had not understood the words but had known, without being told, that the song was about her mother. Pella fell asleep listening. When she woke, Mensa's singing had stopped.*

**Manifest symptoms landed:**
- Orthographic drift (subtle): second drawing's signature finished by another hand.
- Per-PC reception: Thera → stuffed wolf (mother-grief). Grom → Mensa's body. Aelric → the sealed letter (mirrors his own letters to Varran). Kessa → the chalk-drawing.

---

### Scene 02 — Pursuit & the Howl-Stones

Two beats: tracking the trail, then the ambush.

#### Beat 1 — Pursuit

**Read-aloud:**
> The trail goes north. Hoof-prints, maybe five riders. One set is smaller — a child's weight on a pony being led. Late snow holds the prints where open ground has lost them. The land lifts into low hills. By afternoon you see, ahead, the Howl-Stones: a pass between standing stones twelve feet high, set by hands older than any history.

**Features:**
- **Tracking.** Survival DC 12 to follow. Fail: half-day lost, resume at DC 15. Success: reach Howl-Stones by late afternoon.
- **The pony's pace.** Investigation DC 10 on the prints — Pella has been *dismounting and refusing to remount*. She is buying time. Alive.
- **Approach choice.** Open approach → full ambush. Scouted approach (Stealth DC 13 group) → no surprise on the ambushers. Individual scout → mixed initiative.

#### Beat 2 — The Howl-Stones

**Read-aloud:**
> The pass is two hundred paces of narrow track between twelve-foot stones that whistle in the wind — faintly, like breath drawn through teeth. That is how the stones got their name. Old Nerakan carvings on some of them, half-worn. Nothing moves above. Nothing moves below. The wind does not stop.

**Features:**
- **Whistling stones.** Wind-through-hollows, steady sound. Perception DC 12 passive or active: the whistling is *broken* briefly at the pass's far end — a movement.
- **Old Nerakan carvings.** History DC 14: **pre-Istaran Nerakans** (plains-people who predated the current eastern wasteland culture) — warrior-memorials. Bone-Collectors have over-scratched the older carvings with cruder marks. **Manifest symptom: attribution drift in pre-setup form.**
- **Pella's pony.** Tied at the pass's far end; saddled, alone. Decoy. Investigation DC 13: she has been standing 90 minutes. The cell is already at Keloth's Hand; only the ambushers remain.

**Encounter — The Howl-Stones Trap**

- **2 × Bandit** (SRD CR ⅛, 25 XP each).
- **1 × Bone-Collector Lieutenant** (homebrew, CR ½, 100 XP).

**Lieutenant stats:** AC 15 (studded + shield) · HP 22 · Speed 30 ft · Str 12, Dex 14, Con 14. Skills: Athletics +3, Stealth +4, Perception +2. Multiattack (2). **Scimitar** +4, 1d6+2. **Heavy crossbow** +4, 1d10+2, 100/400. **Reaction — Parry:** +2 AC on one incoming attack/turn.

**Bandit stats:** AC 12 · HP 11 · Speed 30 ft. **Scimitar** +3, 1d6+1. **Light crossbow** +3, 1d8+1, 80/320.

**Adjusted XP:** 150 × 2 (3 creatures) = **300**. Easy-medium.

**Tactics:**
- Round 1 (surprise): all 3 ranged on ledges (three-quarters cover). Lieutenant targets heavy-armor PC. Bandits target Kessa.
- Round 2: Bandits reload. Lieutenant draws scimitar if engaged in melee.
- Reduced below 8 HP: Bandits surrender if offered. Lieutenant does NOT surrender — will try to escape east to warn Keloth. If she escapes and reaches stronghold in 45 min of in-fiction time before party arrives, stronghold goes to **Alert**.
- **Stealth advantage:** wind imposes disadvantage on Perception (hearing). Benefits both sides; favors scouts.

**Cover:** stones = half-cover (+2); ledges = three-quarters cover (+5). Dislodging ledgers requires ranged attack, spell, or climb (Athletics DC 13).

**If captured alive (Intimidation DC 12 OR Persuasion DC 14):** Bandit reveals — cell at "Keloth's Hand," half-day east; cell-leader Keloth, lieutenant Idra, 5 members at stronghold tonight; seven more west on a feint (location unknown to Bandit); stronghold has a well-shaft in the stable yard *"Idra says the well is haunted; we don't open it."* Pella alive, below.

**Treasure:**
- 2 × shortbow + arrows; 2 × scimitar + 2 × dagger; heavy crossbow + 10 bolts; Lieutenant's studded leather + shield.
- 12 gp Nerakan coin.
- Lieutenant's **silver-bound finger-bone** (cell-marker, 5 gp silver; **manifest link** — same moon-silver as the Rose).
- Lieutenant's locked belt-pouch (Thieves' Tools DC 12): **Pella's cut ribbon**, blue, frayed.

**Connections:** South (back-trail). East (to Keloth's Hand). North (Nerakan wastes; dead-end for session).

**GM Notes:**
- Pella's ribbon — small, blue, frayed. Gut-punch.
- If the party walks around the stones (losing half-day): ambushers eventually return; stronghold is alert.
- Gloss: "Nerakan wastes" — eastern Krynn, sparse, hostile to most travelers.

**Memory Fragment (optional):**
> *The Nerakan carvings were made by a people whose grandmothers had stood under these stones to say the names of their dead aloud into the wind — because the wind carried names east, and east was where the dead had gone before there were Kharolis and Thorbardin to break the land. The people who made this place no longer exist. Their wind still knows the names.*

**Manifest symptoms:** attribution drift (pre-Istaran over-scratched); moon-silver trace (same vein).

---

### Scene 03 — The Common Room (Stronghold Upper)

**Read-aloud:**
> The wayhouse was burned long ago — roof gone, timbers black-rimed with old soot and new ice. A stone hearth stands at the room's center, cold. An archway east leads to an open yard. Over the front lintel: carved letters, fresh-cut over older ones beneath. *KELOTH'S HAND.* Behind the newer word, older strokes are still legible: *GAVEK'S REST.*

**Features:**
- **Lintel inscription.** *KELOTH'S HAND* over *GAVEK'S REST*. History DC 12: Gavek's Rest was an Istari wayhouse on the pre-Cataclysm Istar-Neraka road, abandoned ~40 years ago. Investigation DC 10: the over-carving is crude; Istari work underneath is masterwork. **Names are being erased** — same pattern as #0001. **Manifest symptom: attribution drift landing.**
- **The hearth.** Cold. Dragonfire-black soot in one layer, dry ash in another. **Grom signature move:** thumb along the inside-curve reveals Thorbardin-style dwarf-work. Gavek had a dwarf on staff.
- **Archway east.** Open; rubble partially blocks. Leads to Scene 04.
- **Stair down.** Northeast corner; partial rubble cleared; recent traffic. To Scene 05.
- **Ruined roof.** Weather falls directly. Snowdrift in NW corner. **Investigation DC 12:** two Bone-Collector tracks in the last hour.

**Encounter (conditional):** if the party made noise at Howl-Stones, **1 × Bandit sentry** is here. If he flees to warn: **Alert** status. All subsequent stronghold encounters +1 creature; guards positioned defensively.

**Treasure:**
- Among rubble: **Istari traveler's token** (Investigation DC 10). 1 gp silver; 20 gp to a scholar.
- Hearth: nothing (already searched).

**Connections:** East (archway to Stable Yard). Down (stair to Vault Approach). South (open ruin → road).

**GM Notes:**
- Do not signpost the well.
- Grom's dwarf-work observation is free; no roll.
- Gloss: *"Istari"* — of Istar, the human religious empire late in the Age of Might.

**Memory Fragment (optional):**
> *Gavek was a dwarf. He ran this wayhouse for eleven years, never in his own name — his name was on none of the Istari registers — because a dwarf running an Istari way-station during the later Kingpriest years was a quiet act of reconciliation that the Kingpriest would not have approved of. Gavek knew this. He ran the house anyway. When Istar fell, he was already back in the Kharolis holds, running a forge he never named after himself either. He would have recognized Grom.*

**Manifest symptom:** attribution drift landing (Keloth's Hand over Gavek's Rest).

**Per-PC reception:** Grom most strongly (dwarf-hearth). Document.

---

### Scene 04 — The Stable Yard

**Read-aloud:**
> Roofless courtyard. Weeds up through the cobblestones. The far wall holds an iron alarm-bell on a frayed rope. Straw has drifted in the north corner, piled unnaturally high. A stone block sits in the yard's center — weathered, cracked across, no obvious purpose.

**Features:**
- **Alarm bell.** Iron, functional. Struck → sound carries to Vault Approach; alerts stronghold. Rope frayed, snaps on hard yank (auto-success to ring). Silent climb to bell = Stealth DC 12; silent detachment of rope = Sleight of Hand DC 13.
- **Straw pile (N corner).** Unnaturally high. **Investigation DC 13:** clearing reveals the **well-cover**: circular stone slab.
- **The well-cover.** 80 lbs. **Athletics DC 12** (one character) or auto-succeed with two. Beneath: 30-ft shaft to Cell-Block (Scene 07). Climb DC 10 w/ rope; DC 12 without.
- **Partial ledge in the well-shaft (rev 2).** Halfway down (~15 ft), a **sealed second-level landing** — rubble-packed, about 3 ft wide. Gavek's Rest in its Istari prime was larger than the Bone-Collectors' current footprint; this landing was once an intermediate floor since walled off. Hook for future adventure.
- **(Alert only) Well-guard (rev 2).** If the bell has rung, 1 × Bandit is posted at the well-cover, watching the stair-arch. Stealth DC 14 to bypass; 25 XP combat.
- **Stone block (center).** Cracked limestone, scorched. Investigation DC 10: old chimney-base; Gavek's former forge. Flavor.
- **Patrol.** A Bone-Collector walks the yard every 10 min.

**Encounter — Stable Yard Patrol:**
- Timing: 1d4 min after party arrival, then every 10 min.
- **1 × Bandit** (CR ⅛, 25 XP). Routine; Alert doubles to 2 Bandits.
- **Tactics:** on discovery, makes for alarm bell first. Party has 2 rounds to stop him unless ambushed.
- Stealth DC 14 ambush: auto-surprise, one free action; usually silences him.
- If bell rings: **Alert** status enforced.

**Treasure:**
- **Bone-carved whistle** (3 gp curio; KEY — patrol-impersonation signal; Performance DC 13 or Deception DC 15 to fake).
- In the straw: 2 sp and **a child's glove** too small for adult hands — Pella's.

**Connections:** West (archway to Common Room). Down (well, if uncovered) to Cell-Block.

**GM Notes:**
- Well is the earned shortcut. No DM push. Thera's reflex heuristic will likely find it.
- Bell = ticking clock. Real consequence for tactical choice (answers S01 Tactician lens).
- Whistle later = +1 round advantage at Cell-Block or Vault if used.

**Memory Fragment (optional):**
> *Pella fought them in this yard. She was nine, she was not larger than a goat, and she had kicked the tall one in the shin hard enough that he had limped. They had not been expecting a child who would kick. They had laughed, and then they had stopped laughing, and then they had taken her below. One of them had said: "Keloth will not laugh." Pella had not known who Keloth was. She had decided, in the carrying, that she would remember the name.*

**Per-PC reception:** Thera → glove in straw. Document.

---

### Scene 05 — The Vault Approach

**Read-aloud:**
> The stair opens into a dry stone corridor. Twenty feet ahead, a guard-post alcove — a wooden chair, a table with a clay cup still steaming, a short-spear leaning against the wall. At the corridor's far end, two doors: a plain wooden one left, an iron-banded door right. The air smells of old bone-meal and hearth-ash.

**Features:**
- **Guard-post alcove.** 1 Bandit on routine; 1 Bandit + Lieutenant on Alert.
- **Left door (wooden, UNLOCKED).** To Cell-Block. Charcoal sigil: Keloth's house-mark (a hand).
- **Right door (iron-banded, LOCKED).** To Reliquary Vault. Keloth's key. DC 13 pick; AC 17, HP 18 to break.
- **Bone-meal smell.** Investigation DC 10 identifies. Kessa (Arcana DC 13) recognizes from a Wizards of High Sorcery monograph on unsanctioned necrotic practice.
- **Table papers:** a duty-roster. **Keloth, Idra, Vesk, Kann, Tull.** **Vesk's name is crossed out.** Idra appears twice (cook + Wednesday-watch). The party now has intelligence: cell size (5 here), two key names (Keloth, Idra).

**Encounter — Vault Approach Guard:**
- Routine: 1 × Bandit (AC 12 · HP 11 · Scimitar +3 1d6+1 · Light crossbow +3 1d8+1). 25 XP.
- Alert: 1 × Bandit + 1 × Bandit Lieutenant (same stats as Howl-Stones; CR ½, 100 XP).
- **Tactics:** Bandit shouts *"KELOTH! OST!"* (Nerakan: "Keloth, enemy!") on sight — alerts entire lower level. Combat as per stats. If combatant conscious in round 3: Keloth moves Pella from Cell-Block to Vault (she becomes human shield in Scene 06).

**Treasure:** short-spear; 5 sp; bone-whistle (same as Scene 04); duty-roster (priceless intel).

**Connections:** Up (stair to Common Room). Left (Cell-Block). Right (Reliquary Vault, locked).

**GM Notes:**
- Wooden door unlocked; iron door locked. Bone-Collectors do not fear their captive escaping through lower level.
- Keloth holds vault key. Capture Keloth alive = easy vault access; kill = must pick or break.
- Gloss: *"Nerakan"* — language of the eastern wastes. *"OST"* = enemy.

**Memory Fragment (optional):**
> *Idra had taken the Wednesday watch because she did not like to eat meals with the others. She had been with the cell for eleven years and she was, most nights, the only one who asked whether Keloth slept. He did not sleep. She had stopped asking two years ago. When the man she had loved was killed in Neraka, Keloth had been the one who named him at the shrine. It had been a kindness. Idra still remembered it as one, even now, on the watch, alone, in a dry wayhouse in Abanasinia.*

**Manifest symptom:** attribution drift (Vesk's name crossed out on roster).

**Per-PC reception:** Aelric most likely to read as intelligence. Document.

---

### Scene 06 — The Reliquary Vault (climax)

**Read-aloud:**
> Low-ceilinged, stone-cold room. Along the east wall: a shelf of silver-bound skulls, spaced like a quiet procession. At the center, a low altar holds an iron box. Behind the altar stands a tall, soft-robed man, hands folded. On the altar lies a nine-year-old girl, bound at the wrists. She sees you. Her chin lifts. Pella.

**Features:**
- **Shelf of skulls (E wall).** Six skulls, each moon-silver-bound. Five occupied; one empty. Kessa ritual Detect Magic: all six magical — 5 active, 1 dormant.
- **The named shelf-reliquary (rev 2).** One of the five bears a hand-scratched sigil at the temple — a Nerakan house-rune. Investigation DC 12: **Haena of the Fourth House, PC 29.** A Nerakan midwife's last minute. Extended family in Verrat, east of Neraka. Seeds a future delivery arc. (A second shelf-reliquary holds **Sergeant Hern of the Solamnic Sword**, who fell beside Varran at PC 22; not sigil-marked, but Keloth knows the identity. His widow Andra lives at Tarbir Waystation in southern Abanasinia.)
- **The empty reliquary (rev 2).** Visibly prepared: polished to mirror-brightness, eye-sockets open and waiting, a single silver thread laid across the mandible as if the filigree work is mid-forge. An artifact waiting.
- **The wall-ledger (N wall, rev 2).** A charcoal ledger runs the length of the north wall: names, dates, locations, in Keloth's hand. Some entries crossed out, some circled. Decades long. Investigation DC 13: one entry in the middle section is **uncredited and in a different hand** — *"I will not look at the rose again."* A party that played S01 will recognize the phrasing from Vesk's memory fragment in the Rose Cairn. Neither Vesk nor Keloth wrote it here; someone else — now held in one of the shelf-reliquaries — did. **Cross-adventure signal.**
- **Central altar.** Low stone. Iron box contains a **seventh reliquary** — the **Varran-reliquary.** Keloth wears the key at his neck.
- **Pella.** Bound at wrists to the box's handles. Bruised. Thin. Not crying. **Stats (inline, rev 2):** AC 10 · HP 6 · Speed 25 ft. Child's bite +0, 1 piercing. Not a combatant. Full playsheet: [NPCs](#npcs).
- **Keloth.** Behind altar. Unarmored, charcoal-wool robe. Hands folded. Speaks first.

### Keloth's Opening Offer (read-aloud in Keloth's voice)

> *"Put down your weapons and listen to me for thirty seconds. I will say my piece, and then you will do what you think is right. My name is Keloth. I am a priest. You did not come here for the child. You think you did. But you walked here because one of you —"* (his eyes, which have been on Aelric the entire time, do not leave Aelric) *"— needs a minute he has never had, and I am the man who can give it to him. I have on this altar the death-minute of Varran of Crownhold. Your brother. If you want him, I will give him to you. All I want in exchange is the child to walk out this door at your side, alive, today, and the work of my cell to continue unharried by your Order. Solamnia asks for too much. One minute for the child, and we are done."*

**He is not lying.** Insight DC 13 — he's earnest. The trade is real.

**Pella speaks at this moment (rev 2 commitment).** The DM MUST narrate her interior as certainty. She looks at Aelric and asks, clearly: *"Are you the knight my papa said would come?"* **She has decided the answer is yes.** Her question is not a question; it is naming. A child who has been through two days of captivity has earned the right to decide who her rescuer is before they have proven it. Do not soften.

### The Choice (four options)

- **A — Accept.** Aelric (or a kin PC) attunes the Varran-reliquary at the altar. Hears Varran's last minute. Loses all other memories of Varran. Pella walks free. Keloth departs via rear tunnel.
- **B — Refuse; fight.** Combat (see Encounters Appendix). Keloth tries to escape with Varran-reliquary; will kill Pella if cornered (he is a zealot).
- **C — Negotiate.** Very high Persuasion (DC 20) or a specific bargain Keloth values (e.g., offering back the Silver Rose — which the party doesn't have). Keloth is stingy; he wants a grief-exchange.
- **D — Attack-then-negotiate.** If Keloth reaches ≤ half HP (16): he drops, restates Offer A. Accept = he hands over key + releases Pella + walks out. Refuse = combat resumes.

### Encounter (if combat) — The Vault Climax

- **Keloth** (Cult Fanatic reskin, CR 2, 450 XP): AC 13 (15 w/ Shield of Faith) · HP 33 · Str 11 Dex 14 Con 12 Int 10 Wis 13 Cha 14. Deception +4, Persuasion +4, Religion +2. Dark Devotion (adv vs charmed/frightened). **Multiattack** (2 daggers). **Dagger** +4, 1d4+2. **Spellcasting** (Wis, DC 11, +3): Cantrips — *light, sacred flame, thaumaturgy*. L1 (4) — *command, inflict wounds, shield of faith*. L2 (3) — *hold person, spiritual weapon*.
- **Routine (rev 2, raised):** Keloth + Idra (Lieutenant, CR ½, 100 XP) + 1 Cultist (25 XP). 575 base × 2 (3 creatures) = **1,150 XP. Deadly.**
- **Alert (rev 2, raised):** Keloth + Idra + 3 Cultists at start = 625 base × 2 = **1,250 XP.** Second-wave Lieutenant arrives round 3 from cell-block door = effective ~**1,450 XP, deadly+, TPK-risk.**

**Keloth's tactics:**
- Round 1: bonus draws dagger; action Shield of Faith (self, +2 AC, 10 min concentration).
- Round 2: Command on heaviest melee PC (Aelric/Grom) — *"Halt"* (Wis save DC 11).
- Round 3+: close for Inflict Wounds (3d10 necrotic melee spell +3).
- Never attacks Pella directly.
- **At half HP (≤16):** kneels, restates Offer A. If accepted, hands over key; party takes reliquary + Pella; Keloth and cell members exit via rear tunnel.
- **If killed:** Idra/Cultists surrender. They are not zealots.

**Environmental beats:**
- **Destroying a shelf reliquary** (AC 12, HP 5): Keloth flinches. Three shattered = Keloth surrenders regardless of HP.
- **Freeing Pella mid-combat** (Sleight of Hand DC 14 + one turn): she disrupts Keloth's line-of-sight. Cannot fight effectively but gains agency.
- **If Keloth surrenders and is killed anyway:** Cultists (if alive) kill Pella in his name. DM gut-check.

### The Reaction Moments (rev 2: two simultaneous beats)

1. **The five occupied shelf-reliquaries dim by one perceptible degree.** Perception DC 12 to catch. The Varran-reliquary was the anchor.
2. **The charcoal wall-ledger briefly brightens** (rev 2). Kessa Perception DC 13 specifically watching the ledger catches the uncredited *"I will not look at the rose again"* entry glowing warm-orange for one heartbeat, then fading back to charcoal. No other entry brightens. Whoever wrote the line was bound to the ward; lifting the reliquary disturbed their rest. **Cross-adventure signal from #0001.**

### The Attunement (if any PC attunes)

Sixty seconds real-time. The attuner is still; party watches. After:

- Attuner experiences Varran's full final minute: cold, weight of Solamnic plate in snow, Sergeant Hern falling beside him, the unsaid thought *"Paladine, carry my wife"* (meaning Doriel of Crownhold — name embedded in the Minute).
- Attuner **loses every other memory of Varran** — permanent; unrestorable by *greater restoration*.
- Attuner gains passive: **Name of the Dying** (automatically knows the name of any creature dying within 60 ft in the past minute).
- Once/long-rest: **Grief-Echo** — ask the reliquary a factual question about Varran's death; it answers in Varran's voice.

**For the DM:** **ask the player, after the 60 seconds, to describe what Varran said/did/thought/felt.** Write it verbatim into the session log. That description replaces all prior Varran-memories. The DM must not re-narrate Varran doing other things in subsequent sessions.

**Treasure (combat route or accept + take-all route):**
- **The Varran-reliquary.** See [Treasures](#treasures).
- **Five shelf-reliquaries** (four Nerakan, one Sergeant Hern — Solamnic; future delivery arcs).
- **One empty reliquary** (morbid future-tool; 30 gp raw moon-silver).
- **Keloth's robe** (20 gp), **daggers** (5 gp), **40 gp** Nerakan + Abanasinian coin, **iron-box key**.
- **Keloth's moon-silver bracelet** (his mother's reliquary; 30 gp raw; attunement consumes *the attuner's* mother-memories for Keloth's mother's final minute — useless but revealing).
- **Keloth's letter to Mira Vaenshold-Silversmith** (threatens her compliance; **seeds #0003**).

**Hidden rear tunnel (S wall, Investigation DC 15 post-combat):** 200 yards to a snowy draw where Keloth's getaway horse is staked. Saddle + 3 minor moon-silver ingots (60 gp) + the Mira-threat letter (if not already on Keloth).

**Connections:** West (iron door to Vault Approach). East (iron door to Cell-Block). Hidden rear tunnel (escape route).

**GM Notes:**
- Play Keloth calmly. He is not a snarling villain. He is a priest who believes his work is mercy. The scariest kind.
- Play Pella as a child, not a token. She asks: *"Are you the knight my papa said would come?"* The session's emotional hinge.
- Let the party decide slowly. Keloth is patient.
- If a PC attunes: 60 real seconds. Do not narrate for them; ask them.
- If party takes reliquary unattuned: Keloth considers the trade broken; cell pursues in #0003.

**Memory Fragment (only read if a PC attunes):**
> *Varran's last minute contains: the specific cold of a Nerakan dusk; a sergeant named Hern who fell beside him; a sentence he thought but did not say — "Paladine, carry my wife" — though Varran never married. The wife he had meant was the woman he had intended to ask, who was still alive at Crownhold when Varran died, and who died three years later without knowing she had been on his mind at the end. Her name was Doriel. Aelric never knew about her.*

**Manifest symptoms:**
- Reaction moment (five reliquaries dim).
- Attribution drift (Keloth's robe-hem: "Keloth, son of —" with his father's name unpicked).
- Per-PC reception: Aelric → Keloth's offer. Thera → Pella. Grom → the Reorx-destroyable artifact. Kessa → moon-silver evidence + Mira letter.
- Inter-PC chain setup: Aelric's decision chains to all three.

---

### Scene 07 — The Cell-Block

**Read-aloud:**
> A narrow stone corridor, two oil-lamps high on the walls. Three cell-doors along the south wall. The first two: empty. The third, at the corridor's end: also empty — a wool blanket, a porridge bowl. A child was kept here. She has been moved.

**Features:**
- **Well-shaft (W end, ceiling).** If party entered via well, they arrive here. Old frayed rope already hangs.
- **Three cells (S wall).** All empty. Each bears traces of prior occupancy (rev 2 interior layers):
  - **Cell one:** half-wiped chalk figure of a woman on south wall, shoulder-high — prior prisoner's attempted portrait. Investigation DC 12 to see; DC 15 to read as someone loved.
  - **Cell two:** tally-marks near the bolt, 63 marks in groups of seven. A long-term prisoner counting weeks. Investigation DC 10.
  - **Cell three (Pella):** held her until 15 min before arrival. Porridge warm (Insight DC 10); blanket pulled back; **a broken crayon on the floor** (she did not come quietly); **a dark floor-stain near the north wall** (Investigation DC 13: old blood, years old, scrubbed but ingrained — another prior prisoner).
- **Iron door (E end).** To Vault. Bi-directional with Scene 06.
- **Oil lamps.** If broken, oil soaks stone. Next fire source ignites: 1d6 fire, one round, then burnt out. Environmental hazard.
- **Cell three mattress cache** (Investigation DC 13): **silver-filigree finger-bone** (5 gp silver, manifest link).

**Encounter (Alert only):** 1 × Bandit patrolling. 25 XP. Retreats east to warn Keloth; surrenders at < 4 HP.

**Treasure:**
- Broken crayon (Pella's; Thera will take it).
- Oil lamps × 2 (2 sp each; environmental utility).
- Silver-filigree finger-bone (5 gp, manifest link, evidence of prior prisoner).

**Connections:** East (iron door to Vault). West (well, up to Stable Yard).

**GM Notes:**
- Broken crayon — red, snapped clean, not chewed. She broke it in frustration mid-drawing.
- Cache weight: someone was in this cell. A thoughtful party asks who.
- Environmental fire: don't foreground; let a clever player propose.

**Memory Fragment (optional):**
> *The prisoner before Pella was a woman in her fifties from a village west of Neraka. She had inherited her mother's ability to hear the names of the dead spoken on the wind. Keloth had wanted her to teach him. She had refused. She had lasted three months in that cell. She had not been a martyr about it; she had simply been stubborn about her mother's gift. When she died — old age, not violence — Keloth had been disappointed. He had taken her last minute anyway. Her name is on the third skull from the left in the Vault.*

**Per-PC reception:** Thera → Pella's crayon. Grom → cell-mattress cache. Document.

---

### Scene 08 — The Return to Varduin *(rev 2 landing scene)*

A closing scene, not a keyed dungeon. The party rides home; what they find determines the adventure's final weight.

**Read-aloud (as the muster crests the last rise above Varduin):**
> You smell the smoke before you see the village. It is not a cooking-fire. The way-house's east wing is black against the morning — one wall still standing, the roof caved in. The main hall is intact. Horses are in the yard. A Solamnic banner you did not leave behind hangs from the gate.

**What happened in the party's absence:** the seven-member feint wing of the Bone-Collectors struck Varduin on the second night. Brother Laen had sent word south; three Knights of the Sword arrived on the first night. Outcome:
- **East wing of the way-house burned.** Thera's old bedroom among the losses.
- **Two villagers killed** — a farrier named **Tell** and an old woman named **Mira-no-kin** (Grom recognizes her name; he had sent her a hearth-fitting 2 years ago).
- **One Knight of the Sword killed** — **Sir Venric of the Sword,** 29, unmarried, from a waystation south of Solanthus. His body awaits the Order's pyre in the main hall.
- **Four raiders killed; three escaped east.**
- **Brother Laen alive** — split lip, favored hand; has already reported to the Council.

**Brother Laen on return:**
- *"You were right to go. I would not have survived the counterfactual where we let Thera ride alone."*
- *"My sister Wena has been named inside the Council. They have asked me to withdraw from clerkwork and serve at her cloister as 'family consolidation.' I have not answered."*
- *"Sir Venric has been kind to me. I am going to the pyre in an hour. You do not have to attend."*

**Party decisions on return:**
- **Pella.** Brother Laen's elderly mother offers to take her in. Thera decides (or asks Pella). If Pella is asked: she says *"I go with you."* — which alters the party's composition for future sessions.
- **The Varran-reliquary.** If attuned: Aelric finds a quiet corner of the main hall; Grom sits outside it unasked. If unattuned: Laen's locked cabinet. If destroyed via Grom's rite at Varduin's smithy: Laen is not told in advance but quietly approves.
- **The shelf-reliquaries.** Laen visibly disturbed; asks they be kept out of sight until a Council delegate arrives (3-4 days).
- **The Mira-letter.** Laen reads it, sits down, reads it again. **Agrees to a Council contract to protect Mira Vaenshold-Silversmith in Crystalmir-by-the-Fells. Adventure #0003's formal hook.**
- **Sir Venric's pyre.** One hour in-fiction; Aelric attends by Oath. Aelric may realize — quietly — that Varran's body was never recovered and thus Varran had no pyre. Sir Venric gets one.

**Treasure:**
- Order pays **15 gp per recovered shelf-reliquary** (reserved pending Council delegate).
- Laen's **20 gp safe-conduct stipend** paid as agreed.

**GM Notes:**
- **A landing, not a climax.** The session's emotional weight has already fired. Do not introduce new crises.
- **Do not rush Sir Venric.** If the party attends the pyre, let silence sit.
- **Grom's S01 doubt resolves (or not) here.** Reliquary destroyed = Grom at quiet peace. Reliquary returned = Grom watches Laen accept, says nothing.
- **If Pella joins the party:** Thera's Playstyle Heuristics adjust for S03+.

**Memory Fragment (optional):**
> *Sir Venric of the Sword died on the third step of the way-house porch, blocking a Bone-Collector from reaching the children sheltering in the pantry. One of the children he saved was a cooper's daughter named Alys, seven. Alys will remember his face for the rest of her life and will not know his name. She will call him, when she is grown and telling her own children, "the tall knight on the porch." That is all she will be able to say of him. It is more than most men get.*

**Manifest symptom (final):** Mira-no-kin died. Her birth-name was lost in a displacement decades before; "Mira-no-kin" was what Varduin called her. She was the last person to carry that un-name. Now no one does. *A name erased before the cell's feint arrived — the grief-economy has been working on Varduin, too.*

---

## Treasures

### The Bone-Collector's Reliquary *(central artifact)*

*A human skull bound in moon-silver filigree, the eye-sockets stopped with small silver discs.*

**Appearance:** man's skull, late thirties, weathered; mandible held by silver wire. Moon-silver filigree (Vaenshold vein; same as Silver Rose). Two small silver discs set into eye-sockets. Thread-fine Nerakan geometric filigree. 3 lbs. Cool but not cold.

**Presence / Desire:** the reliquary **wants to be held, listened to, and exchanged.** Drawn to the closest living kin of its occupant. In Aelric's presence it warms by a perceptible degree — the first heat anyone has felt from moon-silver. It chimes softly, inaudibly to anyone but the kin, on first proximity. No voice; the silence of the sixty-second Minute is its utterance.

**Rarity:** **Rare** (reads uncommon to casual inspection; Kessa Arcana DC 15 guesses true).

**Attunement:** Required. **Prerequisite:** blood kin or named-loved-one of the current occupant. Non-kin attempting: cold reliquary; lost attunement slot 24 hrs, no other effect.

**Current occupant:** **Varran of Crownhold** (Knight of the Sword, died PC 22, Neraka-border skirmish, witnessed by Keloth). Prior occupants (overwritten): Fern of the Sixth House (died PC 41); Old Derrin the blacksmith (died PC 31).

**Benefits (while attuned):**
- **The Minute.** Once, at attunement: experience the occupant's final 60 seconds in first-person. Non-negotiable content.
- **Name of the Dying.** Passive. Auto-know names of creatures dying within 60 ft in the past minute.
- **Grief-Echo.** Once/long rest: ask a factual question about the occupant's death; answer in their voice.

**Curse — Memory Concentration:**
- At attunement, **every memory of the occupant other than the Minute is consumed.** Permanent.
- Lost: shared meals, arguments, quiet moments, emotional associations, the living-figure sense.
- Retained: fact of existence; name; the Minute.
- Henceforth, the occupant exists in the attuner's memory only as dying.

**Ending:**
- **Lesser effects (remove curse, greater restoration):** DO NOT restore memories. Not a spellcasting curse; a memory-transaction.
- **Reorx-shattering rite (Grom):** at dawn on a forge-fire ≥ 1,800°C, Religion DC 15. Destroys filigree; Minute lost; attunement ends; already-lost memories remain gone.
- **Re-occupation:** dying creature within 60 ft while their name is spoken aloud — overwrites current occupant.

**Hooks:**
- Aelric's choice (primary).
- The other shelf-reliquaries (Hern + 4 Nerakan) — future delivery arcs.
- The empty reliquary (future-use tool).
- Mira Vaenshold-Silversmith (Keloth's letter).
- Doriel of Crownhold (named in the Minute; died 3 yrs after Varran).

### Minor Loot Index

| Item | Scene | Purpose | Value (gp) |
|---|---|---|---|
| Pella's stuffed wolf (1-eared) | 01 | Roleplay | 0 |
| Vesk's sealed letter "to P, when you are ten" | 01 | **KEY** + roleplay | priceless |
| 8 gp (ash-box) | 01 | Coin | 8 |
| Pressed silver leaf | 01 | Flavor | 2 |
| Mensa's notebook (Reya's name) | 01 | **KEY** + roleplay | priceless |
| Pella's chalk-drawing of Reya | 01 | Evidence | 0 |
| Second (forged) Pella-drawing | 01 | Evidence (trap-signal) | 0 |
| 3 × Bandit weapons | 02 | Coin | 12 |
| Lieutenant silver-bound finger-bone | 02 | Faction + manifest | 5 |
| Pella's cut ribbon (in locked box) | 02 | Evidence | 0 |
| Howl-Stones pony | 02 | Transport | 15 |
| Istari traveler's token | 03 | Scholar-sale | 20 |
| Sentry kit (if spawned) | 03 | Coin | 5 |
| Bone-whistle | 04 | **KEY** (patrol-impersonation) | 3 |
| Pella's child's glove | 04 | Roleplay | 0 |
| 2 sp in straw | 04 | Coin | 0.2 |
| Oil lamps × 2 | 07 | Environmental | 0.4 |
| Duty-roster | 05 | **KEY** (intel) | 0 |
| Cache silver-filigree bone | 07 | Faction + manifest | 5 |
| Broken crayon (Pella's) | 07 | Roleplay | 0 |
| Keloth's robe | 06 | Coin | 20 |
| Keloth's daggers × 2 | 06 | Coin | 5 |
| Keloth's moon-silver bracelet | 06 | **Artifact** (mother) | 30 raw |
| Iron-box key | 06 | **KEY** | 0 |
| Keloth's letter to Mira | 06 | **KEY** — #0003 | priceless |
| Keloth's purse | 06 | Coin | 40 |
| Escape-route bonus (if found) | 06 | Coin + **KEY** | 60 + priceless |
| 5 shelf-reliquaries | 06 | **Artifacts** | 30 each raw |
| 1 empty shelf-reliquary | 06 | **Artifact** (future-use) | 30 raw |

### Brother Laen's travel stipend

**20 gp** offered at session-start. Paid on return regardless of outcome.

---

## NPCs

### Pella Vesk-daughter, age 9

**Appearance:** small for her age, not thin. Brown hair in two uneven self-braids. Burn-scar on left thumb-pad. Linen smock dyed bruised-plum (Nerakan dye). Dirty; bruise on one cheek, two days old.

**Background:** born PC 29 in a waystation north of Neraka. Mother **Reya** died of fever when Pella was 4; Pella barely remembers her. Father **Vesk** was away tomb-working; she calls him Papa. **He died 3 weeks ago in the Rose Cairn; Pella does not know this.** Raised by aunt **Mensa** since 5.

**Stats (if attacked):** AC 10 · HP 6 · Speed 25 ft · Str 6 Dex 11 Con 8 Int 10 Wis 11 Cha 10 · **Child's bite** +0, 1 piercing. Not a combatant.

**Voice tags:**
- Does not cry easily. Has not cried during capture.
- Asks direct questions: *"Are you a Solamnic? Papa said Solamnic knights had silver on their collars."*
- Pronounces her name *PELL-uh*.
- Uses one Nerakan word without glossing: **"chal"** (= real). *"You are chal knights?"*

**Decision order (DM playing her):**
1. Do not seem weak.
2. Find out about Papa.
3. Help the people helping her.
4. Protect the drawings.

**If told Papa is dead:** no visible reaction. DM narrates silence; asks the PC in-scene what they see in Pella's face. She will cry later — or not in the players' presence.

**Secret:** Pella does not yet know her mother's name. Mensa never told her. **The name is in Mensa's notebook: Reya.** The party decides when/whether to tell her.

**Post-session:** the party must decide what to do with Pella. Options: take to Varduin (Thera's hometown); find extended family in Neraka; foster with Brother Laen's mother; ask her what she wants.

### Keloth of Neraka, Bone-Priest

**Appearance:** tall, thin, iron-gray at the temples, 50 years old moving like 40. Charcoal-wool robe unadorned. Moon-silver bracelet on right wrist (his mother's reliquary; unattuned). Soft voice, tired. Makes eye contact.

**Background:** lost wife and two sons in plague-year at 32. Grief drove him to fringe Nerakan priesthoods. Apprenticed to **Tarch** who taught him grief-harvesting methods. Led this cell nine years. Believes the work is mercy. Scariest villain: the one who is neither wrong nor monstrous in his own terms.

**Stats (Cult Fanatic reskin, CR 2, 450 XP):**
- AC 13 (15 w/ Shield of Faith) · HP 33 (6d8+6) · Speed 30 ft.
- Str 11 Dex 14 Con 12 Int 10 Wis 13 Cha 14.
- Skills: Deception +4, Persuasion +4, Religion +2. Passive Perception 11.
- Dark Devotion (adv vs charmed/frightened).
- Languages: Common, Nerakan.

**Actions:** Multiattack (2 daggers). **Dagger** +4, 1d4+2 piercing.

**Spellcasting (Wis, DC 11, +3):**
- Cantrips: *light, sacred flame, thaumaturgy*.
- L1 (4): *command, inflict wounds, shield of faith*.
- L2 (3): *hold person, spiritual weapon*.

**Voice tags:**
- Never shouts.
- Nerakan formal register — calls cultists by full name. Calls Aelric "Sir Knight" without irony.
- Never uses "enemy"; uses "opposed" or "unaligned."
- Pauses often before speaking.

**What he wants:** the Varran-reliquary attuned by Varran's brother (primary); cell's continued operation (secondary); Pella as leverage only (tertiary).

**At half HP (≤16):** drops to knees, spreads arms, restates Offer A. **If trade accepted:** hands key, releases Pella, walks out via rear tunnel. **If attacked after surrender:** does not defend himself. Says: *"You are choosing your rage over your brother's minute and the child's walk. I will grieve that, but I will not stop you."* Dies without casting. DM gut-check.

**Downstream consequence tracking** (for #0003):
- **Keloth alive, trade accepted:** stable cell under uneasy truce.
- **Keloth dead, Idra alive:** Idra succeeds; cell becomes worse.
- **Keloth dead, Idra dead:** cell fragments.
- **Keloth accepts trade, then killed anyway:** blood-feud by surviving seven western cell-members.

### Mensa Vesk-sister, Waystation-keeper *(deceased)*

Killed 2 days before session opens, in her own kitchen, from behind, while kneading bread. Pella's aunt; Vesk's older sister. 52 at death. Narrow-faced, Vesk's same sharp chin, gray-streaked dark hair. Wool apron over plain dress, still dusted with flour.

**Medicine DC 12 observing body:** killed quickly, without struggle, by someone standing behind while she kneaded.

**What she was doing:** kneading rye-and-savory bread to send south to *Varduin-by-the-Pines, for V— Vesk, when he next passes through* — she did not know Vesk was 3 weeks dead.

**Her notebook** (Investigation DC 13) contains Nerakan names-of-the-dead: **Oneva** (mother), **Kalt** (father), **Reya** (Pella's mother — the name Pella has never been told), Vesk (blank — she had not written his entry), and her own pre-ruled line with empty date-field.

**Wall cameo** (Investigation DC 15): **Jannet of Crownhold**, the waystation's previous owner before Mensa — a retired Solamnic armswoman. **Possibly Aelric's great-great-aunt.** Seed for future adventure.

### Brother Laen (returning from #0001)

Full file at `adventures/0001-tomb-of-the-silver-rose/npcs/brother-laen.md`. In #0002, Laen:

- **Opens the session** with the 20 gp stipend + safe-conduct letter.
- **Receives the party on return.** Varduin's way-house east wing is burned (the western feint raid); Laen is alive, shaken. He has had to tell the Rose Council what happened. **Wena** (his sister) has been named inside the Council — she is now overtly the leverage. Laen tells the party this if they have kept his trust.
- **Any reliquaries delivered:** Council-level interest; escalation. Laen becomes uncomfortable if Aelric has attuned.
- **Mira letter delivered:** Laen commits to a Council contract to protect Mira. Seeds #0003 formally.

---

## Wandering Pressure

**Cold Pulse d6 per 10 min** — outdoors (Scenes 01-02) OR stronghold upper level (03-04). Stops in lower level (warmer) and Varduin on return.

| d6 | Effect |
|---|---|
| 1 | Nothing. |
| 2 | Three-heartbeat atmospheric chill. |
| 3 | **Cold bites.** PCs not in heavy armor AND not wearing winter cloak take **1d4 cold damage** (no save). *v1.1 compliant.* |
| 4 | Forgotten name (roleplay only). |
| 5 | Distant sound on wind (Perception, no gate; localizes to Keloth's Hand direction). |
| 6 | **Silver stirs.** Any PC carrying moon-silver feels it warm briefly. One min, no effect. |

**Wandering d6:**

- **Wilderness trail** (every 2 hrs): 1-2 nothing; 3 scout (1 × Bandit); 4 blizzard (1-2 hr delay); 5 Solamnic courier (NPC intel); 6 wind-whispers a memory fragment to a random PC.
- **Stronghold** (every 30 min): 1-2 nothing; 3 Cultist on errand (1 × Bandit); 4 collapse (d3: beam falls/well-climb DC 15/cell door slams); 5 **Pella distraction** — she bites, kicks, breaks something, party catches commotion (Perception DC 12); next guard-encounter -1 creature; 6 silver stirs.

**Do not force-trigger.** Dice carry pressure.

---

## Encounters Appendix

### Bandit (multiple, Scenes 02/03/04/05/07)
AC 12 · HP 11 · Speed 30 · Scimitar +3, 1d6+1 · Light crossbow +3, 80/320, 1d8+1 · CR ⅛, 25 XP.

### Bone-Collector Lieutenant (Scene 02; Scene 05 Alert)
AC 15 · HP 22 · Speed 30 · Str 12 Dex 14 Con 14 · Athletics +3, Stealth +4, Perception +2. **Multiattack** (2). **Scimitar** +4, 1d6+2. **Heavy crossbow** +4, 100/400, 1d10+2. **Reaction — Parry** +2 AC once/turn. CR ½, 100 XP.

### Keloth (Scene 06 climax)
See NPCs section.

### XP Budget (4 × L3 → L4)

| Easy | Medium | Hard | Deadly |
|---|---|---|---|
| 300 | 600 | 900 | 1600 |

Multipliers: 1 mon ×1 · 2 ×1.5 · 3-6 ×2.

**Session XP projection:** ~700-1000 XP / PC = reaches **level 4** at session end.

---

## DM Cheatsheet

### Key DCs by Scene

- **01:** Investigation 10 (door, drawings), 10 (ash-box preliminary), 12 (kitchen bread-scrap), 13 (iron box + notebook), 15 (Jannet cameo), 15 (drawing-forgery final letter). Medicine 12 (Mensa's body).
- **02:** Survival 12 (tracking) → 15 (re-track after fail) · Investigation 10 (pony prints) → 13 (pony dampness) · Perception 12 (ambush warning) · Stealth 13 (scout-approach) · History 14 (Nerakan carvings) · Intimidation 12 / Persuasion 14 (captive talks) · Athletics 13 (climb to ledges) · Thieves' Tools 12 (locked box).
- **03:** History 12 (Gavek's Rest) · Investigation 10 (over-carving) · Investigation 12 (tracks).
- **04:** Investigation 13 (well under straw) · Athletics 12 (lift well-cover; auto w/ 2) · Stealth 12 (climb to bell) · Sleight of Hand 13 (detach rope silent) · Stealth 14 (ambush patrol) · Climb 10 (rope) / 12 (no rope) · Performance 13 / Deception 15 (whistle impersonation).
- **05:** Thieves' Tools 13 (iron door; AC 17 HP 18 to break; Athletics 17) · Investigation 10 (bone-meal) · Arcana 13 (Kessa recognizes monograph).
- **06:** Insight 13 (Keloth sincerity) · Sleight of Hand 14 (free Pella mid-combat) · Persuasion 20 (Option C negotiate) · Investigation 15 (rear tunnel).
- **07:** Insight 10 (porridge warm) · Investigation 13 (mattress cache).

### Key Saves

- Bandit/Lieutenant standard.
- Keloth spells: DC 11 (Command-Wis; Hold Person-Wis; Inflict Wounds-melee touch).
- Cold Pulse outcome 3: **no save** — direct 1d4 cold if not heavy-armored + cloaked. *v1.1 compliant.*

### Attunement (inlined)

- **Short rest (1 hour)** focused on item.
- **3 attunement slots** per PC max.
- **Varran-reliquary attunement** is instant (not a short-rest wait). Plays the Minute in 60 seconds real-time. Cost: all memories of Varran other than the Minute. Non-kin: no attunement.

### Conditions used (inlined)

- **Paralyzed:** incapacitated; can't move/speak; auto-fails Str/Dex saves; attacks have advantage; any attack that hits within 5 ft is a critical hit.
- **Frightened:** disadvantage on ability checks + attacks while source in line of sight; can't move closer to source.
- **Charmed:** can't attack charmer; charmer has advantage on social checks.
- **Command ("Halt"):** target uses reaction + movement to stand still until end of next turn; no attacks.
- **Hold Person:** paralyzed, Wis save end-of-turn to end.

### XP Budget (4 PCs, L3)

Easy 300 · Medium 600 · Hard 900 · Deadly 1,600. Adjusted multipliers per monster count.

### Keloth-Trade Decision Table (rev 2)

Quick reference at the altar — use while talking to the players:

| Option | Action | Outcome |
|---|---|---|
| **A Accept** | Attune Varran-reliquary | Pella free; Keloth departs via rear tunnel; no combat; narrative XP 400/PC |
| **B Refuse + fight** | Initiative | R1 Keloth Shield of Faith; R2 Command-Halt; R3+ Inflict Wounds; surrenders at HP ≤ 16 |
| **C Negotiate** | Persuasion DC 20 or grief-exchange | Keloth stingy; accept only grief-for-grief |
| **D Attack-then-accept** | Engage; Keloth re-offers at HP ≤ 16 | If accepted: he hands key, releases Pella, exits |

### Attribution-Drift Tracker (rev 2)

Six beats to watch for across the session; tick when each lands:

| # | Beat | Scene | Landed? |
|---|---|---|---|
| 1 | Pre-Istaran Nerakan carvings over-scratched by cruder Bone-Collector marks | 02 | |
| 2 | KELOTH'S HAND carved over GAVEK'S REST on the lintel | 03 | |
| 3 | Vesk's name crossed out on the duty-roster | 05 | |
| 4 | Keloth's robe-hem "Keloth, son of —" unpicked | 06 | |
| 5 | Vault wall-ledger entries crossed out and circled, with uncredited "I will not look at the rose again" | 06 | |
| 6 | Mira-no-kin's un-name erased from Varduin | 08 | |

### Per-PC Reception Tracker (rubric v1.1)

Each manifest symptom gets a row; note the receiving PC during play:

| Scene | Symptom | Likely PC | Confirmed |
|---|---|---|---|
| 01 | Forged second drawing | Thera | |
| 01 | Mensa's body | Grom | |
| 01 | Vesk's sealed letter | Aelric | |
| 01 | Chalk-drawing of Reya | Kessa | |
| 02 | Attribution drift (Nerakan) | Kessa | |
| 02 | Pella's ribbon | Thera | |
| 03 | Gavek's Rest / dwarf hearth | Grom | |
| 04 | Pella's glove in straw | Thera | |
| 05 | Vesk crossed out | Aelric | |
| 06 | Keloth's offer | Aelric | |
| 06 | Named shelf-reliquary (Haena) | Kessa | |
| 06 | Wall-ledger + cross-adventure phrase | Kessa | |
| 06 | Reliquary shelf dim | All (Perc DC 12) | |
| 06 | Wall-ledger brighten | Kessa (Perc DC 13) | |
| 06 | Robe-hem unpicked | Kessa | |
| 06 | Mira letter | Kessa | |
| 06 | Pella-recognition beat | Aelric | |
| 07 | Broken crayon | Thera | |
| 07 | Cell-block interior layers (tally, chalk, stain) | Grom | |
| 07 | Mattress cache bone | Grom | |
| 08 | Mira-no-kin's un-name | Grom | |
| 08 | Sir Venric's pyre | Aelric | |

### Inter-PC Chain Tracker (rubric v1.1)

Watch for and document:

- Aelric attunement decision → Grom (performs shatter or not)
- Aelric attunement decision → Thera (judges the call)
- Aelric attunement decision → Kessa (records Minute in notebook)
- Pella's chal-question to Aelric → Thera's childhood-grief echo
- Keloth's surrender offer → Grom's doubt (resumed from S01)
- Mira-no-kin's death → Grom's hearth-greetings track back through session

### Scene Triggers (if-then)

- **Party walks openly at Howl-Stones** → full ambush surprise.
- **Full-party Stealth 13** → no surprise; ambushers flat-footed.
- **Bell rings at any point** → stronghold Alert; +1 creature on all subsequent guard encounters; Pella moved to Vault before climax.
- **Lieutenant escapes Howl-Stones fight** → stronghold Alert if party > 45 min behind.
- **Party finds well** (Investigation 13 on straw) → stealth shortcut available; bypass Scenes 03 + 05.
- **Aelric attunes Varran-reliquary** → 60 seconds of play; player describes the Minute; all other Varran-memories gone.
- **Keloth surrenders at half HP** → trade offered again; party decides.
- **Party accepts trade** → no combat XP; 400 XP narrative per PC; Keloth + cell exit rear tunnel; shelf-reliquaries remain.
- **Party attacks Keloth after surrender** → Cultists (if alive) kill Pella in Keloth's name. Critical gut-check.
- **Party destroys Varran-reliquary via Grom's rite** → Religion DC 15 at dawn, 1,800°C forge. Minute lost; artifact destroyed; any lost memories remain lost.
- **Party keeps reliquary unattuned** → Keloth's trade broken; cell pursues in #0003.
- **Party finds Keloth's letter to Mira** → Brother Laen commits Council contract to protect Mira; #0003 formalized.
- **Party delivers any shelf-reliquary to Brother Laen** → Council-level escalation; Aelric's attunement (if any) quietly noted.
- **Party refuses to tell Pella about Vesk's death** → she continues expecting him; future sessions land the news, or do not.
- **Party tells Pella about Vesk** → no visible reaction; she cries later or never in their presence.
- **Party asks Pella about her mother** → Pella knows "Mother" but not Reya's name; the name is in Mensa's notebook; party decides whether/when to tell her.
- **(rev 2) Party investigates the Vault wall-ledger** → Investigation DC 13 reveals uncredited *"I will not look at the rose again"* entry. A player who played S01 will recognize Vesk's phrasing. Acknowledge the player's catch silently — do not confirm — and let them sit with it.
- **(rev 2) Varran-reliquary lifted** → two simultaneous reaction moments: 5 shelf-reliquaries dim by one degree (Perc DC 12); ledger entry briefly brightens warm-orange (Kessa Perc DC 13 watching specifically).
- **(rev 2) Bell rings AND party later uses the well** → Alert well-guard (1 Bandit) posted at well-cover. Stealth DC 14 to bypass.
- **(rev 2) Party asks Pella what she wants** → *"I go with you."* She does not soften this. Party must decide whether to accept; if yes, changes Thera's Heuristics for S03+.
- **(rev 2) Party attends Sir Venric's pyre in Scene 08** → Aelric may quietly realize Varran had no pyre; Varran's body was never recovered. Atmospheric weight; do not narrate the realization for him — let the player feel it.

### Downstream Consequence Tracking (for #0003)

Note which occurred:

| Outcome | S02 log entry |
|---|---|
| Keloth alive, trade accepted | cell continues under uneasy truce |
| Keloth dead in combat | Idra succeeds (worse cell) |
| Keloth and Idra both dead | cell fragments (7 remaining scatter) |
| Keloth killed after surrender | **blood-feud**; worst outcome for #0003 |
| Aelric attuned | Council notes; advancement review affected |
| Grom performed shattering-rite | Council approval; Mira-arc accelerates |
| Reliquary kept unattuned | cell pursues; #0003 opens with an attack |
| Mira-letter delivered to Laen | Council contract = #0003 hook formalized |
| Pella taken to Varduin | Thera-Pella-foster arc begins |
| Pella delivered to Nerakan extended family | separate #0003/#0004 arc (cross-border) |
| Pella asked what she wanted | she chooses "with you"; alters party composition |

### Per-PC reception tracking (rubric v1.1 — log during play)

Each manifest symptom, note which PC received it most strongly:

| Scene | Symptom | Likely PC | Confirmed? |
|---|---|---|---|
| 01 | Second-drawing forgery | Thera | |
| 01 | Mensa's body | Grom | |
| 01 | Vesk's sealed letter | Aelric | |
| 01 | Chalk-drawing of Reya | Kessa | |
| 02 | Attribution drift (Nerakan) | Kessa | |
| 02 | Pella's ribbon | Thera | |
| 03 | Gavek's Rest / dwarf hearth | Grom | |
| 04 | Pella's glove in straw | Thera | |
| 05 | Vesk crossed out on roster | Aelric | |
| 06 | Keloth's offer | Aelric | |
| 06 | Reliquary shelf dim moment | All; Perception DC 12 | |
| 06 | Robe-hem unpicked name | Kessa (scholar eye) | |
| 06 | Mira letter | Kessa | |
| 07 | Broken crayon | Thera | |
| 07 | Mattress cache | Grom | |

### Inter-PC chain tracking (rubric v1.1)

Chains to watch for and document if they fire:

- Aelric attunement decision → Grom (performs shatter or not).
- Aelric attunement decision → Thera (guards Pella during the Minute).
- Aelric attunement decision → Kessa (records Minute in notebook).
- Pella's chal-question to Aelric → Thera's childhood-grief echo.
- Keloth's surrender offer → Grom's doubt (resumed from S01).

---

*Module compiled 2026-04-18 by `module-binder`. Rubric v1.1 compliant at design. Lint-clean (see `lint-report-2026-04-18.md`). Revised 2026-04-19 as rev 2 (all 5-persona panel suggestions applied; panel mean 68.8/80 pre-fix). Ready for S02.*
