---
session: S05
adventure: 0012-the-reckoning-stone
party: compact-wardens
date: 2026-04-20
dice-seed: S05-20260420
author: session-runner
rubric-version-locked: v1.5
---

# S05 PREP — The Reckoning Stone

## Party at start

| PC | HP | Spell slots | Attunements | Notable inventory |
|---|---|---|---|---|
| Thessaly | 32/32 | L1:4, L2:3, L3:2 | 0/3 | 4 shards (all unattuned); reconstruction doc |
| Orik | 52/52 | —; 4 sup dice | 0/3 | Full |
| Sera | 44/44 | L1:3, L2:2 | 0/3 | Clause of Grief (unattuned) |
| Calder | 48/48 | L1:4, L2:3, L3:2 | 0/3 | Full |
| Lenne | 44/44 | Full; Ward 22 HP | 0/3 | Full; notebook filling |

**Party XP:** 1,312 each. **Party purse:** 190 gp. **Convergence: 79 days.**

## Open questions

1. **Does Thessaly name the Test wound?** This is the session's entire question. Does she perform the reckoning that the Clause of Reckoning asks her to perform? Route D fires on this and nothing else.
2. **If Route C triggers:** Is Lenne ready for the Counterspell duel? Does she save her L3 slots for the Mage-guard's Fireball?
3. **Hint 4 delivery.** The panel is visible from the doorway. Does the party engage with it? Does Calder read it and go still again (his third time, after the inscription at the White Quill and the Dalimvar minutes)?
4. **Vorn and Lenne.** Two researchers who have been doing the same work alone. Does Lenne acknowledge this? Does Vorn?
5. **Event logging.** If Route C fires: log all attacks, saves, reactions, Counterspells. If Route D: log the arc-completion as a social_roll.

## Party-specific threads

- **Thessaly** — This is her spotlight. She has been carrying the Test wound since Session 1. She named it to Tessamine (S01). It has been in the background since. Vorn will ask, implicitly, for her to name it again — to a peer, not a mentor. The DM-letter explains the hold-space.
- **Orik** — He will read the building (signature move). He will note that the researchers are also security. He will position himself accordingly. He will not have a personal moment this session; he is in support mode. craft-witness watch: if he touches any structural element, it's a fourth consecutive session.
- **Sera** — She will do a full perimeter assessment (exits, observed vs. unobserved). She will report to Orik. She will notice that Vorn and Thessaly are mirrors without naming it. She has been accumulating patterns. She is close to naming the carved-figure pattern.
- **Calder** — He read the Dalimvar voting minutes in the private archive. He has put them down twice now (White Quill and Vorn's archive). He is the most processed member of the party. He will be supportive this session, not in the lead.
- **Lenne** — She will read Vorn's research. She will recognize Vorn as a methodological peer. She has been doing the same work alone, less rigorously, for eight years. This recognition matters.

## Event logging

```bash
python scripts/marathon.py start --adventure 0012-the-reckoning-stone --session S05 --party compact-wardens
```

Log: social_roll for Hint 4 delivery; social_roll for arc-completion; feature_used for Orik (if structural check); If Route C: attack/save/reaction/spell_cast for all combat.
