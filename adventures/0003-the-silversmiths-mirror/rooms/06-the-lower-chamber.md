---
adventure: 0003-the-silversmiths-mirror
tier: 1
author: dungeon-smith
created: 2026-04-19
campaign: moon-silver-cycle
sources:
  - adventures/0003-the-silversmiths-mirror/treasures/aelwens-mirror.md
  - adventures/0003-the-silversmiths-mirror/treasures/mirror-manifest.md
  - adventures/0003-the-silversmiths-mirror/npcs/mira-vaenshold-silversmith.md
---

# Scene 06 — The Lower Chamber (Mirror revealed)

## Read-aloud

> Mira unlatches the hidden door. It opens. A small chamber — six feet square — dry, cold, candle-wax-marked. A wooden stand at the center. On the stand, a cloth. Under the cloth, a palm-sized mirror.

> Mira does not go in.

## Features

- **The chamber.** 6 ft square; 6 ft ceiling. Dry — note the *continued cross-adventure dryness pattern* (Rose Cairn S01 R02, Gavek's Rest lower level S02). A faint grit underfoot: **obsidian-dust**, still present 180 years after Aelwen's forging, because obsidian does not decay. Candle-stubs on the floor around the stand are arranged in **crescent patterns** — not random scatter; Mira (and Seralen and Avel before her) lit vigil-candles here at the six moon-phases each silver-smith is trained to mark. The candles have been relit every year. The wax is layered; the outer rings are fresh.
- **The stand.** Plain oak. Active Investigation DC 10 on the stand's leg: **a half-bloomed rose is carved there**, chisel-clean, matching the shop-arch and Mirror handle. Passive Perception 12 for PCs in the chamber: **three thumb-prints worn smooth into the oak** — where Aelwen, Heva, and Seralen each held the stand at the moment of placing the Mirror down for the last time. (Mira has never touched the stand; she has never lifted the Mirror.) The cloth is a dark grey, half-woolen, threadbare at the edges.
- **The mirror.** Cloth-covered. When the cloth is lifted: palm-sized; moon-silver handle with the half-bloomed rose opening mark; obsidian back; silver face. **The face is blank until held by someone.** The polishing-lines on the silver face **do not perfectly converge** — Aelwen did not finish the polish, or chose not to. Kessa Arcana DC 10: this is unusual; moon-silver is normally polished to full convergence. A smith who stopped here stopped deliberately.
- **The silver-filigree on the shop signage (upstairs)** dims by one perceptible degree the moment the cloth is lifted. Passive-Perception DC 14 for anyone still upstairs (including Harel); DC 12 active Perception if someone is watching specifically. **Anchor-level per rubric v1.2.**

## The scene

**Mira does not enter the chamber.** She stands at the doorway and says, one sentence:

*"I have kept this for thirty years. I will not look. I will not touch it. You will decide."*

Then she turns and goes upstairs to sit with Harel.

### What the mirror does when lifted

See `treasures/aelwens-mirror.md` for the full mechanics. Summary:
- **Waits 2-3 heartbeats** before resolving.
- **Shows the holder their face as the person who loves them most sees them** — felt recognition, not observation.
- **Attunement is fast** — one look. First-time lookers typically look away at 1-2 seconds.
- **Cost:** permanent self-image replacement.
- **Blank-Mirror Trap risk:** if the holder's most-lover is dead + cannot love them anymore, OR no one alive loves them most, the mirror is blank. Blank-attunement is irrevocable and consumes 30 days of love-capacity.

### What the party can do

**A. Leave the mirror untouched.** Take the cloth; bundle the mirror; take it to the forge for Grom's Reorx-rite. Clean break.

**B. A PC looks into the mirror.** **Option C spawn triggers.** Per `session-runner` Section 2.3, spawn that PC as a subagent to describe the reflection in-voice. See "Option C subagent prompt" below.

**If the PC sees a blank mirror (Blank-Mirror Trap), read aloud:**

> *"You lift the mirror to your face. For two heartbeats, the silver is empty. No face comes. No one is there. The mirror stays blank. And you feel — "*

Then stop. Let the PC describe the feeling in-character before you deliver the mechanical cost (permanent attunement; 30 days of lost love-capacity; no other attunement holds during those 30 days). Their answer is binding.

**C. Mira looks into the mirror.** Mira has said *nyet*. She means it. However, she will look if a PC asks her to and makes a Persuasion check DC 20 (she is at 30-years-of-refusal; the DC is high). If she looks: Mira's mother Seralen is dead; Mira had a childhood friend also now dead; Mira has never had a romantic partner. The mirror shows Seralen's gaze — clear, loving, the last gaze Seralen held before her stroke. Mira bears it for 3 seconds, weeps, looks away. She does NOT attune fully (she pulls her eyes away before the fast-attune completes). But the 30-year refusal is ended.

**D. Destroy the mirror in the chamber.** Grom can attempt the Reorx-shattering rite here, but the lower chamber is not a forge. It will fail (Religion DC 15 with disadvantage = almost certain fail). The mirror must be taken to Varduin's smithy (or any 1,800°C forge) first.

## Option C subagent prompt (when a PC looks)

If a PC chooses to look into the mirror, spawn a subagent via the `Agent` tool:

```
subagent_type: general-purpose
description: "<PC> looks into Aelwen's Mirror"
prompt: "You are <PC Name> of the Varduin Muster. Your full PC sheet is at personas/parties/varduin-muster/<pc-slug>.md. READ THAT SHEET FIRST.

Context: You are in a dry stone chamber below Mira Vaenshold-Silversmith's shop in Crystalmir-by-the-Fells. On an oaken stand is a palm-sized mirror made of moon-silver, obsidian back, silver face. It is Aelwen's Mirror — her last forging. The mirror shows the holder their own face as the person who loves them most sees them.

The mirror has been uncovered. You have lifted it. The face has paused for two or three heartbeats. It is resolving.

The mirror will show you:
- If your most-loved is alive and capable of loving you: their current view of you.
- If your most-loved is dead: their pre-death view of you.
- If no one alive has loved you most, OR if your most-lover has already attuned to this mirror: the mirror is BLANK. Blank-attunement is permanent and costs you 30 days of love-capacity.

The attunement completes on the first seeing. Cost: your internal self-image (dreams, mental self-picture) is permanently replaced with the reflection. This is irrevocable except by reciprocal recognition in the reflected person's presence (usually impossible for dead reflecteds).

Your grief-paragraph from your PC sheet is the key input. Reference it. Consult your Decision Order and Voice tags.

Grom has argued quietly: this is a transaction; the Mirror is taking your own self-sense in exchange for a glimpse of being-loved. Mira has stayed upstairs. The other party members are in the chamber doorway watching.

Your task: decide what happens when you look. Respond in a single paragraph. Describe (1) what the mirror shows you — who, and what they see — OR that it is blank; (2) what your character says or does in response; (3) whether you attune (the first resolved seeing completes attunement automatically unless you look away fast — you can choose to look away within 1 second but must narrate that choice).

Stay in character. Do not break the fourth wall. Be specific — name the person you saw (or name that you saw no one). If you are Kessa: your most-lover is likely Vethrenn, whom you never met; the mirror may test whether Vethrenn's love for Kessa-who-was-not-yet-born counts as love-for-you. If you are Aelric: your most-lover is likely Doriel (named in Varran's Minute), or Varran himself (but Varran's memories are gone; does Aelric still love him?). If you are Thera: likely Adda (dead 23 years). If you are Grom: likely Duren (dead 3 years)."
```

Record the subagent's response verbatim in the session log. It is binding.

**If the `Agent` tool is unavailable** (solo DM, no subagent tooling): run the moment as a 2-3 heartbeat pause in the narration, then ask the PC in-character: *"What do you see?"* Let them answer in their own voice. Whatever they say is binding — write it verbatim in the session log. Do not prompt, do not correct, do not volunteer what the mirror "should" show. The PC's answer is the reflection.

## Treasure

- **Aelwen's Mirror** — see `treasures/aelwens-mirror.md`.
- **In the stand's drawer** (Investigation DC 10): Mira's mother Seralen's last handwritten note, addressed to *"whoever comes after me"* — two sentences: *"Do not look. Do not let Mira look."* (This is the family's other refusal, preserved.) 0 gp; emotional weight.
- **Candle stubs, wax-marked floor** — pure flavor; no treasure.

## Connections

- **Up (trapdoor and stair):** Mira's kitchen and hearth-room (Scene 4).
- **The chamber has no other exit.** The party takes what they take; they leave via the way they came.

## GM Notes

- **This is the session's moral fulcrum.** The climax of #0003 is a decision, not a combat. Scene 5's combat was setup; Scene 6 is the reckoning.
- **Do not rush the chamber.** Let the party examine. Let the cloth stay on the mirror for a beat before anyone lifts it.
- **Option C is strongly recommended if a PC attunes.** Both Roleplayer and Improviser lenses have asked for this since S02. This is the adventure's canonical Option-C moment.
- **If no PC attunes:** the party's choices are (a) destroy the mirror at a forge, (b) take it unattuned, (c) leave it with Mira. Each has downstream implications for the finale.
- **If the mirror is attuned by a PC:** campaign-continuity. The attuner's self-image is permanently replaced. Like Aelric's Varran-memories, this is **permanent and not-restorable** — enter it in `CLAUDE.md#campaign-continuity` post-session.

### Memory Fragment (optional)

> *Seralen, before she died, sat with the mirror covered in its cloth in the chamber one last time. She did not look. She touched the handle. She said, to no one: "I am sorry I did not look. Someone who comes after me may be braver. I hope they are. I hope." Then she went upstairs and made Mira a pot of tea. Mira still has the note Seralen wrote afterward. It is in this chamber's drawer. It says: "Do not look. Do not let Mira look." Mira was thirty-two. Seralen was sixty-four. They had that morning, and then Seralen went to bed and did not wake up.*

## Manifest symptoms landed

- **The 2-3 heartbeat pause before reflection** — no roll; the mirror's signature behavior.
- **The filigree-dim** (Scene 2 shop signage) — passive-Perception DC 14 from any room upstairs; anchor-level.
- **Smith-mark pulse** when a Vaenshold-line person holds it — relevant only if Kessa is in Aelwen's line (she is not), or if Mira touches it (she won't).

## Per-PC reception tracking

| Symptom | FINDER | RECEIVER | Confirmed |
|---|---|---|---|
| Chamber's dryness | Kessa (cross-adventure pattern) | Kessa | |
| Seralen's note | Whoever searches stand | Mira (via the party's mention); Grom (mending-grief) | |
| The reflection (if attuned) | the attuner | the attuner | |

## Seeds

- **PLANT:** Attuner's self-image-replacement (campaign-permanent if triggers). Mirror's custody (where does it go after session?).
- **RETRIEVE:** Aelwen (fully present via her final-forging); the six-artifact structure (Mira names 3 knows 3 suspected); Hint 4 pre-plant (journal page referenced to ingot).
