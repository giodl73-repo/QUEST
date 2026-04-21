---
session: S04
adventure: 0011-the-defiant-word
party: compact-wardens
date: 2026-04-20
dice-seed: S04-20260420
author: session-runner
rubric-version-locked: v1.5
---

# S04 PREP — The Defiant Word

## Party at start

| PC | HP | Spell slots | Attunements | Notable inventory |
|---|---|---|---|---|
| Thessaly | 32/32 | L1:4, L2:3, L3:2 | 0/3 | 3 shards (all unattuned); reconstruction doc; convergence date (82 days) |
| Orik | 52/52 | —; 4 superiority dice | 0/3 | Full resources |
| Sera | 44/44 | L1:3, L2:2 | 0/3 | Clause of Grief (unattuned) |
| Calder | 48/48 | L1:4, L2:3, L3:2 | 0/3 | Full resources |
| Lenne | 44/44 | L1:4, L2:3, L3:3, L4:1; Arcane Ward 22 HP | 0/3 | Volenn's research notes; empty page in notebook (from S03) |

**Party XP:** 1,012 each
**Party purse:** 190 gp

## Open questions for this session

1. **The Black Robe question.** Does the party ask Deva? Does Lenne recognize her as a practitioner by school? Does Thessaly make the formal request? Does the party consider messaging Mira instead (2-day delay)?
2. **Calder names the plague village.** Does he name it in Scene 04 (Route D)? Does he read Sylaren's note in Scene 05?
3. **First binding-threshold session.** This is the first S04 for campaign 2 — advisory period ended. Gate score is now PASS/FAIL, not just calibration.
4. **Event logging quality.** This session has an Easy encounter (dice!) and social checks. Log all: attack rolls, saving throws, persuasion checks, Calder's accounting (feature_used or social_roll?), Deva's arc-completion (social_roll).
5. **Splinter cell intel.** Three cells; Palanthas contact. This seeds adventure 0012. Note the intel in state_updates.

## Curse-symptoms seeded

| Symptom | Where | Anchor |
|---|---|---|
| Two inscriptions (Symptom 1) | Scene 04 — shard presented | Visible when shard shown; Lenne reads first |
| Second inscription / Hint 3 (Symptom 2) | Scene 04 — Calder + Sevven | Calder passive Insight 14 auto → Sevven points to it |
| Route D warmth (Symptom 3) | Scene 04 — if Calder names village | Route D only |
| Three-Order requirement (Symptom 4) | Scene 04 — Deva assembled | When third Order stands present |

## Party-specific threads

- **Thessaly** — She has four shards after this session. She still hasn't attuned any of them. The Clause of Defiance's curse (awareness of unjust commitments) connects to her wound — the commitment she made at her Test that cost Mira her gift. Does she attune this one?
- **Orik** — He will count exits (entrance encounter provides exits to count). He will check the tunnel entrance for structural quality. He may check the air-shaft in Sevven's study.
- **Sera** — She found the emergency exit. She doesn't announce things. She may note that Calder is sitting with the Sylaren correspondence without opening it. She has been watching Calder since the Grief Inscription.
- **Calder** — This is his spotlight. The Dalimvar withdrawal is the thing he has been thinking about since Scene 03 of the Grief Inscription. He read the inscription three times then. He will read Sylaren's second inscription and understand where forty-one comes from in the history of the compact. The accounting is his mode; let it be.
- **Lenne** — She will want Sylaren's *Survey of Compact Artifact Responses*. She will find the organizational philosophy (chronological, not subject) immediately compelling. She may have filled the empty page in her notebook by the time they leave.

## Rubric version locked

v1.5 — first binding-threshold session for campaign 2. PASS/FAIL applies. Threshold 56+/80.

## Event logging

Include `events` in every `state_updates`. This session has:
- **Combat dice**: entrance encounter (initiative, attack rolls, damage if any)
- **Social rolls**: Persuasion to stand down agents; Deva's arc-completion
- **Saving throws**: any from combat
- **Feature used**: Calder's accounting (use `social_roll` type with `skill: "religion"` or just `"accounting"`); Lenne's artifact reading (feature_used)

```bash
python scripts/marathon.py start --adventure 0011-the-defiant-word --session S04 --party compact-wardens
```

**DM-letter:** Read `dm-letter-scene-04.md` before running. Calder's accounting: precision is the emotion.
