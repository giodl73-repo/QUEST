---
session: S03
adventure: 0010-the-grief-inscription
party: compact-wardens
date: 2026-04-20
dice-seed: S03-20260420
author: session-runner
rubric-version-locked: v1.5
---

# S03 PREP — The Grief Inscription

## Party at start

| PC | HP | Spell slots | Attunements | Notable inventory |
|---|---|---|---|---|
| Thessaly | 32/32 | L1:4, L2:3, L3:2 | 0/3 | Clauses of Witness + Ambition (both unattuned); reconstruction doc; convergence date (88→85 days) |
| Orik | 52/52 | —; 4 superiority dice | 0/3 | Full resources |
| Sera | 44/44 | L1:3, L2:2 | 0/3 | Full resources |
| Calder | 48/48 | L1:4, L2:3, L3:2 | 0/3 | Full resources |
| Lenne | 44/44 | L1:4, L2:3, L3:3, L4:1; Arcane Ward 22 HP | 0/3 | Volenn's moon-calendar copy; 8yr research data |

**Party XP:** 712 each (post-S02; road combat award pending from S02 resolution — add 520/5 = 104 XP each if Mira fight happens here instead of on S02 road; adjust as needed)
**Party purse:** 190 gp

## Open questions for this session

1. **Mira negotiation or combat?** Does the party attempt to explain Route D on the road? Does Mira's arc-completion fire before the chapel, or does the party fight? If fight: does Lenne win the Counterspell duel?
2. **Lenne and the shard (Scene 03).** Does she pick it up before anyone can warn her? How long does she hold it? What does her reliving of Volenn's death look like in narration?
3. **Sera's arc-completion.** Does she name the settlement? Where — interior or sanctuary? Does she name the note specifically?
4. **Morreth naming Ven.** Does the arc-completion happen bilaterally — Sera names, then Morreth names? Or does Route A fire instead?
5. **Event logging first full session.** This is the first session where `events` will be populated in state_updates. Watch for: spell_cast (Lenne's Counterspell, Fireball; Thessaly's support spells; Calder's Bless/heals), feature_used (Lenne's Projected Ward; Orik's Battle Master), saving_throw (Fireball Dex saves; shard Wis save), reaction (Lenne Counterspell; Shield; Projected Ward).

## Curse-symptoms seeded

| Symptom | Where | Anchor |
|---|---|---|
| Cold (Symptom 1) | Scene 03 — first touch of stone box or shard | First PC to touch |
| Re-experience (Symptom 2) | Scene 03 — Lenne holds shard >60 sec | Auto (she picks up objects) |
| Inscription challenge (Symptom 3) | Scene 03 — Calder reads it quietly | Calder natural behavior |
| Route D gift (Symptom 4) | Scene 04 — Sera takes shard after naming | Route D only |

## Party-specific threads

- **Thessaly** — She has two shards in her pack, unattuned. Lenne's experience with the shard will make the attunement question more urgent. She reads "Let no Order forget the cost" and knows Mira would read it differently than she does.
- **Orik** — He will read the approach (signature move). He will note the quality of Morreth's maintenance work — someone who knows what it means to guard a place. He may recognize a version of himself in the elder.
- **Sera** — This is her spotlight. She will be in the ruins (Scene 05) for a long time, watching the road. She will understand what Morreth is waiting for before the others do. The timing of when she speaks — and what she says — is everything.
- **Calder** — The inscription. "Let no Order forget the cost of what it asks." He keeps reading it. He keeps thinking about the plague village. The Orders were not there. This clause was written for exactly what happened to that village. He will not say this aloud this session, probably. Watch for him going quiet.
- **Lenne** — Scene 03 is her most vulnerable moment in the campaign so far. She will be annoyed with herself for holding the shard too long. She will be very quiet after she recovers. She will want to examine the shard systematically, which means she will have to resist the urge to pick it up again. Watch for Symptom 5 of the cold pulse (she catches herself reaching for the box).

## Event logging instructions

Include `events` in every `state_updates` checkpoint response. Minimum events to log per scene:

**Road encounter (if combat):**
- spell_cast for every spell cast (Mira: Fireball/Web/Counterspell; Lenne: Counterspell; Calder: Bless; Thessaly: any)
- feature_used for Orik's Battle Master maneuvers and Lenne's Projected Ward
- saving_throw for every save made (Fireball Dex saves; bola Dex saves)
- reaction for every reaction used (Lenne Counterspell; Shield; Projected Ward)
- near_death if any PC drops below 10 HP

**Chapel scenes (social):**
- feature_used when Lenne's Arcane Ward absorbs damage (if combat in chapel)
- social_roll for any Persuasion/Insight checks with Morreth or Mira

## Rubric version locked

v1.5 — applied to gate scoring post-session.

## Notes on running

```bash
python scripts/marathon.py start --adventure 0010-the-grief-inscription --session S03 --party compact-wardens
```

**DM-letters:** Read `dm-letter-scene-04.md` before running. Two namings; hold space for both.

**First full event-logged session:** Every spell_cast, feature_used, saving_throw, and reaction must appear in `state_updates.events`. This is the first session that will populate the mechanical event log for cross-session analysis.
