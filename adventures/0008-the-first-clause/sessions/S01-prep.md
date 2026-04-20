---
session: S01
adventure: 0008-the-first-clause
party: compact-wardens
date: TBD
dice-seed: S01-<YYYY-MM-DD>  # set at session start
author: session-runner
rubric-version-locked: v1.4
---

# S01 PREP — The First Clause

## Party at start

| PC | HP | Spell slots | Attunements | Notable inventory |
|---|---|---|---|---|
| Thessaly Nightmantle | 32/32 | L1: 4, L2: 3, L3: 2 | 0/3 | Spellbook, components, White Robe seal |
| Orik Flintback | 52/52 | — | 0/3 | Chain mail, shield, war pick, hand crossbow, 4 superiority dice |
| Sera Ashfall | 44/44 | L1: 4, L2: 2 | 0/3 | Studded leather, longbow (40 arrows), 2 shortswords, 3 utility knives |
| Calder of the Third Road | 48/48 | L1: 4, L2: 3, L3: 2 | 0/3 | Chain mail, shield, mace, healer's kit (10 uses), blessed water flask, empty stone in pack |

**Party XP:** 0 (L5 start; campaign 2 opens at Tier 2)
**Party purse:** 180 gp (starting funds; Tessamine paid a 150 gp advance for the commission)

## Open questions for this session

1. Does Thessaly read the inscription in Scene 03 with genuine attention, or does she catalog it and move on? Does Hint 1 deliver this session or fall to the recovery path?
2. Does Calder notice the moon-calendar in Tessamine's archive (passive Insight 14)? Hint 2 vehicle is available but not forced.
3. Does the party use the direct approach (letter → Henneth → honest explanation) or stealth (servant quarters approach)? What does this say about the party's operating style?
4. Does the 90-minute ambush fire? If it fires, is Orik's Battle Master toolkit (Commander's Strike; Menacing Attack) used as designed, or does the party find a different solution?
5. Does Thessaly name the inscription's meaning in Tessamine's return scene (Scene 06)? Does Tessamine's arc-completion fire?

## Curse-symptoms seeded

| Symptom | Where | Anchor |
|---|---|---|
| Dimming (lie detection) | Scene 01 (Tessamine's lie); Scene 03 (Sevel's lies) | Perception DC 10 / Arcana auto |
| Warmth | Scene 03 (first touch of display case) | First PC to open case |
| Inscription-glow (Hint 1) | Scene 03 (Thessaly reads) | Thessaly passive Arcana 18 |
| Clean shard | Scene 03 (display case) | Passive Perception 10 |
| Post-removal emptiness | Scene 03 (after Henneth gives shard) | Scripted; always fires |

## Party-specific threads

- **Thessaly** — The Clause of Witness ("Let no mortal act without witness") is her wound in compact form. She has acted without witness. Hint 1 delivery is her spotlight moment. If she reads it and names its meaning, the session reaches Route D potential. Watch for the moment she goes quiet — that is the signature move (goes still when deciding whether to speak).
- **Orik** — The dock smells of pine resin (Scene 05). His hands will go still. This is his grief landing in an ordinary moment. Do not narrate heavily; note it briefly. His encounter role: tactical anchor for any combat; Commander's Strike and Menacing Attack are in range for the ambush (if it fires). Also: he will check the exits in every new room (signature move). Honor this.
- **Sera** — She will note the side alley entrance to the townhouse before the front door (signature move: checks perimeters). She may or may not flag it. Let her decide. She will also spot the courier from the dock (Perception passive +6 = 16; meets Investigation DC 12). She may or may not pursue; that is her choice.
- **Calder** — He will notice who the party is not looking at. In Scene 03, that is Sevel — the person the party may be ignoring while focusing on Henneth. He will also notice the dimming (Arcana is not his proficiency, but Insight +7 — he reads people who are lying better than he reads the shard). Let his Insight do the work in the Sevel scene.

## Rubric version locked

v1.4 — applied to gate scoring post-session.

## Three-route tracking

Set `route:` in the session log's frontmatter at scene-end of Scene 03:
- **A (Charter):** Party recovers shard cleanly via social approach; returns before 90 min; Hint 1 not delivered or delivered but not named.
- **C (Destruction):** 90-minute ambush fires; shard recovered under pressure; Hint 1 probably not delivered.
- **D (Inversion/Optimal):** Shard recovered; Thessaly names inscription's meaning; Tessamine delivers compact's purpose. Use `marathon.py set-route D` when Route D is confirmed.

## Notes on running via marathon-runner CLI

```bash
# At session start:
python marathon.py start --adventure 0008-the-first-clause --session S01 --party compact-wardens

# At each LLM checkpoint (read-aloud, scene narration):
python marathon.py resume
# Paste the JSON response, press Ctrl+D

# To check current state:
python marathon.py status

# After the session when route is determined:
python marathon.py set-route D   # or A or C
```

**Dice seed:** Set automatically to `S01-<YYYY-MM-DD>` at start. Record it in the session log.

**DM-letters:** Read `dm-letter-scene-03.md` and `dm-letter-scene-06.md` before running. They are short. They matter.
