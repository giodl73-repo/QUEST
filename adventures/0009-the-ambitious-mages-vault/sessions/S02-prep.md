---
session: S02
adventure: 0009-the-ambitious-mages-vault
party: compact-wardens
date: 2026-04-20
dice-seed: S02-20260420
author: session-runner
rubric-version-locked: v1.4
---

# S02 PREP — The Ambitious Mage's Vault

## Party at start

| PC | HP | Spell slots | Attunements | Notable inventory |
|---|---|---|---|---|
| Thessaly | 32/32 | L1:4, L2:3, L3:2 | 0/3 | Clause of Witness (unattuned); Tessamine's reconstruction document |
| Orik | 52/52 | — | 0/3 | Full resources. 4 superiority dice. |
| Sera | 44/44 | L1:4, L2:2 | 0/3 | Full resources. |
| Calder | 48/48 | L1:4, L2:3, L3:2 | 0/3 | Full resources. |

**Party XP:** 300 each (post-S01)
**Party purse:** 180 gp

## Open questions for this session

1. **Road ambush — how does the party handle Osvin and the Quiet One?** This is a genuine Medium combat. Does Orik use Commander's Strike or Menacing Attack to protect spellcasters? Does Sera flank from the treeline? Does Calder use Preserve Life or hold it for the tower? Does Thessaly counterspell or let the combat play out?
2. **Lenne — which route?** Does Orik speak (Route D)? Does the party lead with the reconstruction document (Route A)? Does something go wrong and agents intrude (Route C)?
3. **Hint 2 delivery** — the moon-calendar is in Volenn's old study. Lenne points the party there after the shard is given (or as part of the negotiation). Does Thessaly read the convergence date and speak it aloud?
4. **craft-witness watch** — no instances S01. Calder's morning ritual (blessed water flask, every dawn) is the candidate. The tower cold pulse has a Calder-specific entry (failed experiments, systematic negative-result documentation). Does this produce an atmospheric reception beat?
5. **Clause of Witness attunement decision** — Thessaly still has not attuned. Does this session create pressure to decide? The curse ("Who witnessed this?" once/day after unseen actions) connects to her wound (naming it in S01). If she attunes now, the first question will land soon.

## Curse-symptoms seeded

| Symptom | Where | Anchor |
|---|---|---|
| Vibration (Symptom 1) | Scene 03 — Lenne picks up shard | Visible to all PCs; Orik specifically |
| Eight-year habit (Symptom 2) | Scene 02/03 — storage crates, bedroll, failed experiments | Orik reads the room (decision-order: "what did I miss last time?"); Sera notices living conditions |
| Inscription challenge (Symptom 3) | Scene 03 — Thessaly reads the inscription | Thessaly auto; Orik if inscription faces him |
| Vibration-stop (Symptom 4, Route D only) | Scene 03 — Lenne releases shard | Lenne feels it; all PCs present |

## Party-specific threads

- **Orik** — This is his spotlight session. His grief (seven apprentices; the fire; the pine resin) connects directly to Lenne's pattern. Decision-order: "What did I miss last time?" The heuristic that makes him read the storage crates, the bedroll, the failed experiments. He will know what he's looking at before he says anything. Let the arc-completion happen when it happens. Pine resin cold pulse (d6=3) may fire during the session — his hands go still. Do not narrate heavily.
- **Thessaly** — She has the reconstruction document and the Clause of Witness. She will identify the Clause of Ambition immediately (passive Arcana 18 = automatic). The inscription ("share of the sky") is her direct path to Hint 2. She will also notice Volenn's ward on the shard. And: she has named her wound (S01). The Clause of Witness has been in her pack, unattuned, for one session. Something may shift here.
- **Sera** — She will hear the agents on the utility ladder (passive 16 = 1 round warning if they attempt intrusion). She will also spot that the road is clear after the road encounter. Her arc this session is watching Orik recognize Lenne — and giving him space the same way she gave Thessaly space in S01.
- **Calder** — Watch for the cold pulse (d6=6): failed experiments on the shelf, systematic documentation of negative results. His first physician taught him this method. He will recognize a colleague working alone, without support, in the right way. He does not say anything about this. He may say something about Tessamine's timeline when Lenne mentions Volenn dying. This is not prompted — let Calder decide.

## Rubric version locked

v1.4 — applied to gate scoring post-session.

## Notes on running

The road ambush fires first — dice are required. Marathon-runner will generate the initiative and encounter_dice beat. The road ambush has three enemies (advantage-initiative Dagger of Warning, Bola restraint, treeline crossbow). Expect 2-3 rounds.

After the road: the session shifts to social/investigation. The tower cold pulses replace wandering pressure. The arc-completion is Orik's — watch for the moment he stops reading the room and starts speaking.

```bash
python scripts/marathon.py start --adventure 0009-the-ambitious-mages-vault --session S02 --party compact-wardens
```
