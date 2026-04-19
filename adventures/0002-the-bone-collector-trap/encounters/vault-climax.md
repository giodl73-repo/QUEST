---
adventure: 0002-the-bone-collector-trap
tier: 1
author: human
created: 2026-04-18
sources:
  - reference/srd/monsters-tier1.md
  - adventures/0002-the-bone-collector-trap/npcs/keloth.md
  - adventures/0002-the-bone-collector-trap/treasures/reliquary.md
---

# Encounter — The Vault Climax (Keloth)

**Location:** Scene 06 — Reliquary Vault.
**Trigger:** Party refuses Keloth's trade OR attacks without parley OR Keloth feels cornered.

## Adversaries *(rev 2: baseline raised per Gygax/Jaquays convergent suggestion)*

- **Keloth, Bone-Priest** (Cult Fanatic reskin, CR 2, 450 XP). Full stats: `npcs/keloth.md`.
- **Idra, Bone-Collector Lieutenant** (CR ½, 100 XP; same stats as the Howl-Stones lieutenant — AC 15, HP 22, Multiattack, Scimitar +4 / Heavy crossbow +4, Reaction Parry). **Always present at the climax.**
- **1 × Cultist (Bandit, CR ⅛, 25 XP)** — always present on Routine.
- **Alert additions:** +2 Cultists at combat start (3 total at opening). **Plus a second-wave Lieutenant** (Bone-Collector Lieutenant, CR ½, 100 XP) — arrives at the start of round 3, entering from the cell-block door (roused by the alarm bell and traveling from the west wing). If the party is still engaged, the second-wave can turn the fight.

## Encounter Math

- **Routine (Keloth + Idra + 1 Cultist):** 450 + 100 + 25 = 575 base × 2 (3 creatures) = **1,150 XP**. **Deadly** for 4 × L3 party (threshold 1600 deadly, 900 hard).
- **Alert (Keloth + Idra + 3 Cultists):** 450 + 100 + 75 = 625 base × 2 = **1,250 XP**. Second-wave Lieutenant at round 3 adds +100 base; effective encounter weight ~1,450 XP (**deadly+, TPK-risk**).

Both scenarios are appropriate climaxes. Routine is genuinely hard now; Alert approaches TPK territory. The party earned the difficulty by their tactical choices earlier.

## Setup

- Keloth stands behind the altar, hands folded, Pella bound on the altar between him and the party.
- Idra (if routine) is off to the side, watching — will intervene on Round 1 if combat opens.
- Additional Cultists (if Alert) are on the shelf-side of the room, having been summoned from Cell-Block or Vault Approach when the bell rang.

## Opening Sequence

1. **Keloth speaks first.** See `rooms/06-reliquary-vault.md` read-aloud. He offers the trade. This is NOT an action in combat rounds; it's a pre-combat scene.
2. **Party responds.** Accept trade / refuse / negotiate / attack.
3. **If attack or refuse:** roll initiative. Keloth's initiative is +2 (Dex 14). Idra's is +2. Cultists +0.

## Round 1 — Keloth's opening

- **Bonus action:** Draw one of his two daggers.
- **Action:** Cast **Shield of Faith** (V, S; 1 slot) on himself. AC rises to 15 for 10 min (concentration).
- **Movement:** Stays behind the altar, using Pella as a psychological block (not as direct cover — he will not hide behind a child physically).

## Round 2 — Keloth's command

- **Action:** Cast **Command** (V; 1 slot) on the party's heaviest-armored melee PC (Aelric first, Grom second). Wisdom save DC 11. On fail: one word — *"Halt"* — target loses their next action standing still. If the PC has just moved into the vault, they halt mid-room.
- **Bonus action:** Shift behind the altar.
- **Movement:** Repositions to keep the altar between himself and melee.

## Round 3+ — Keloth's pressure

- **Action:** **Inflict Wounds** (V, S; 1 slot). Melee spell attack (+3). On hit: 3d10 necrotic. Uses this when a PC has closed to melee range.
- **Alternatively:** **Multiattack (2 daggers)** if Inflict Wounds is not charged. +4 to hit each, 1d4+2 piercing.
- **At half HP (16 or below):** he **stops attacking** and repeats the trade offer. This is the critical narrative beat — see Scene 06 Decision section.

## Idra's tactics (Cult Fanatic reskin or standard Bandit)

- Stats (routine, as standard Bandit): AC 12, HP 11, Scimitar +3 1d6+1, Crossbow +3 1d8+1.
- **Round 1:** Ranged crossbow at whoever looks softest (Kessa).
- **Round 2+:** Close to melee if outnumbered; retreat toward the cell-block iron door if Keloth is downed.
- **If Keloth surrenders or accepts trade:** Idra obeys and stands down.

## Additional Cultists (Alert only)

- Stats: Bandit (CR ⅛).
- **Tactics:** Form a line between Keloth and the party. Interposition. Do not engage melee unless attacked; if attacked, scimitar.
- **If Keloth surrenders:** they surrender.

## Using the Environment

- **The shelf of reliquaries (east wall).** Destroying a reliquary mid-combat (AC 12, HP 5 each) shatters it — the stored last-minute is lost forever. **Keloth will visibly flinch** if a PC attacks the shelf. He considers this desecration of dying. If the party threatens to destroy the shelf, Keloth surrenders immediately (below 25% HP threshold; surrender happens upon the first shelf-reliquary shattered).
- **Pella on the altar.** Pella is bound but alert. If the party can free her without Keloth intervening (Sleight of Hand DC 14 + one turn), she will bite/kick/run. She cannot fight effectively, but her movement disrupts Keloth's line of sight. **Keloth will not harm Pella in combat.** He considers her essential to the trade; killing her dishonors his priesthood. The one exception: if the party attacks Keloth *after he has surrendered*, he does not defend himself — but the Cultists (if alive) will kill Pella in Keloth's name, as an act of zealous mourning. This is a DM gut-check for the party.

## Resolution Branches

### A — Party accepts the trade before combat
- Aelric (or any PC who can attune) attunes the Varran-reliquary at the altar. Keloth waits patiently.
- Upon attunement completion (60 sec real-time, see reliquary.md), Keloth hands the iron-box key (already used) and releases Pella.
- Keloth and his people leave via the rear tunnel. They take only their personal effects. The shelf-reliquaries stay.
- **XP awarded:** No combat XP; but **400 XP "narrative climax"** to each PC for the roleplay (DM discretion).

### B — Party refuses trade and wins combat
- Keloth surrenders at half HP; restates the trade. Party decides again.
- OR Keloth is killed (his HP reaches 0 before his surrender-round). Party has all loot; they also have the moral weight of having killed a surrendering-inclined priest.
- Idra and Cultists surrender when Keloth falls (they are not zealots).
- **XP awarded:** combat-normal (713 or 1050 XP).

### C — Party refuses trade, AND kills Keloth during his surrender offer
- Aelric specifically may do this (his Oath-vs-Order conflict makes Keloth's priesthood a target). If he does, the party is splintered — Grom will push back hard, Kessa may argue, Thera may defer.
- The act is not evil by D&D alignment rules, but it is *significant*. Note in session log.
- Idra and Cultists escape if possible; otherwise they fight to the death to preserve Keloth's legacy. Combat continues.

### D — Party accepts trade but then kills Keloth anyway
- Betrayal. Keloth dies without defending himself. The cell (his seven people at Varduin) will learn of this within the week and will swear **blood-feud** on the party. This changes #0003's entire shape.
- Noted in session log. Flag for DM.

## XP Summary

- **Accept trade (no combat):** narrative 400 XP / PC.
- **Defeat Keloth routinely (hard):** 713 XP / 4 = ~180 XP / PC + loot.
- **Defeat Keloth on Alert (deadly):** 1050 XP / 4 = ~260 XP / PC + loot.
- **Kill-after-surrender variant:** same as above, but with a session-log flag.

Either way, with S01's 50 XP plus this session's ~200 XP per PC, the party ends #0002 at **~900 XP each**, putting them at **level 4** at session end (level 4 threshold is 900 XP).

## Designer notes

- **The climax is a moral scene, not just a combat.** Do not rush to roll initiative. Let Keloth's offer breathe.
- **Keloth's half-HP surrender** is the test of the party's moral clarity. A "chaotic good" party takes the trade or lets him go; a "rigid lawful" party fights through. Either is valid.
- **Pella is the visible stakes.** Her presence constrains the combat's shape. Do not forget her during initiative; she watches, she breathes, the DM should remind the players periodically.
- **Rubric v1.1:** the Memory-Echo-equivalent here is the Minute itself (if the reliquary is attuned). Per-PC reception is explicit. Inter-PC chain: Aelric's attunement decision chains structurally to the whole party.
