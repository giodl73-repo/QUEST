---
adventure: 0005-the-pride-circlet
campaign: moon-silver-cycle
tier: 2
author: human
created: 2026-04-19
---

# 0005 — The Pride-Circlet

**Tier:** 2 (party of 4 entering at L4; ~2,075 XP; session adds ~450 XP).
**Expected playtime:** one session, 3-4 hours.
**Setting:** Korrath-by-the-Sea, Istaran port city; Revered Daughters chapter-house + Lady Tiran's harbor estate; late Age of Might (PC 20, ~3 weeks after S04).
**Status:** Designed rev 1. Awaiting 5-persona design review, then S05 play (via marathon-runner CLI).
**Campaign position:** #0005 of 7 in the Moon-Silver Cycle. Emotion: **Pride.** Spotlight: **Aelric.**

## One-line logline

A dying Istaran noblewoman is commissioning moon-silver artifacts to preserve her name past death — and the Revered Daughter novice she has chosen as her instrument is Wena Laen, Brother Laen's sister, who knows exactly what a Pride-Circlet is.

## What's in this directory

```
premise.md                                      logline, setting, hook, constraints, seeds
npcs/lady-tiran-of-the-purple-rose.md           Tiran; 68; dying; Second House patron
npcs/wena-laen.md                               Wena; 28; novice; the party's moral anchor
npcs/felor-of-second-house.md                   Felor; 51; factotum; Kann's client
treasures/pride-circlet.md                      Central artifact — Aelwen's 5th forging
treasures/pride-circlet-manifest.md             Cross-skill handshake (rubric v1.3 compliant)
treasures/minor-loot.md                         Items with Purpose tags; cross-adventure seeds
encounters/felor-intervention.md                Conditional Scene 5 combat
encounters/wandering-pressure.md                Korrath urban variant (rubric v1.3)
rooms/map.md                                    City + estate + chapter-house layout
rooms/01-korrath-arrival.md                     Harbor + market; Vaenshold-vein silver
rooms/02-tirans-estate.md                       Tiran; Felor; empty case tell
rooms/03-wena-briefing.md                       Wena; research notes; Hint 4 near-delivery
rooms/04-joint-meeting.md                       Tiran + Wena; the real question under the meeting
rooms/05-tirans-archive.md                      Aelwen's water-reflection fragment; vault door
rooms/06-the-vault.md                           Pride-Circlet; Option C; Tiran's decision
rooms/07-aftermath.md                           Resolution; triplet fragment; sixth-forging synthesis
module.md                                       [to be compiled by module-binder]
reviews/                                        [5-persona review, pending]
sessions/                                       [S05 output goes here]
```

## Campaign-spine integration

**Seeds retrieved this adventure:**
- Wena Laen (#0004 Scene 7 — Wena's sealed note) — fully present
- Lady Tiran of the Purple Rose (#0003 Kann's client intel; #0004 Wena's note) — fully present
- Felor of Second House (#0004 Kann's finger-bone cord engraving) — fully present
- Aelric's Varran-memory gap (S02 campaign-permanent) — activated by Blank-Circlet-Trap design

**Seeds planted this adventure:**
- **Sixth forging: shame-keyed** (near-delivery via Tiran's research; pre-synthesis via Kessa if she articulates the ingot-connection)
- **Thane Thora Stoneforge** (mentioned in Tiran's network; optional seed for #0006)
- **Wena Laen post-campaign arc** — she stays at Korrath; future visit possible
- **Aelwen's water-reflection fragment** — third Aelwen writing; diptych → triplet
- **Tiran's full six-forging research** — Kessa's custody post-session

**Hint status at end of #0005:**
- Hint 1 (Fresco-Heal) — caught S01; available for recall
- Hint 2 (Vethrenn margin) — unlocked S04
- Hint 3 (Reorx's Judgment) — planted S04 (Grom holds silently)
- **Hint 4 pre-synthesis** — if Kessa articulates the ingot-as-missing-ending connection here; full delivery at #0007 auto-passive (DC 15)

## The real decisions

1. **Does Aelric touch/attune the Pride-Circlet?** Option C mandatory if he does. Blank-Circlet-Trap calibrated to his Varran-memory state.
2. **Does Tiran attune before or instead of the party?** The golden-path (Tiran heard without the Circlet) requires Scene 04 to succeed.
3. **What happens to the Circlet?** Attuned / destroyed / surrendered / party-held.
4. **Does Wena leave with the party?** She doesn't — but the party may offer. Her choice to stay is the session's final character beat.

## Player-style alignment

- **Sheet-deep-reader:** Aelric's Varran-gap is directly activated by the Blank-Circlet-Trap. His decision order (Oath first) shapes every Scene 02/04/06 beat.
- **Craft-witness:** Grom's reception of the Circlet's *wanting* in Scene 06 is the session's craft-witness moment.
- **Doctrinal-silence candidate:** if Kessa sees the water-reflection fragment and articulates the horror-of-Aelwen-trying-it without attuning — that is doctrinal-silence behavior (understand without touching).

## Rubric v1.3 compliance

- ✅ All anchor-level symptoms have ≥2 of 3 fallback paths
- ✅ Per-PC reception with finder-vs-receiver (v1.2)
- ✅ Silent reception counted (v1.2)
- ✅ Memory Fragment per scene
- ✅ Every NPC named has `npcs/<slug>.md`
- ✅ Scene 03 Hint-4 near-delivery has ≥2 fallback paths (Wena delivers path c; Kessa cross-ref path a)

## Next steps

- Run `module-binder` to produce `module.md`.
- Run 5-persona design review.
- Apply P0 revisions.
- Play **S05** via `python marathon.py start --adventure 0005-the-pride-circlet --session S05`.

## Post-session commitments (for CLAUDE.md#campaign-continuity)

After S05 plays, update `CLAUDE.md#campaign-continuity` with:
- Pride-Circlet disposition (attuned-Aelric / attuned-Tiran / destroyed / surrendered / unattuned-party).
- Aelric's attunement state if applicable (Pride-Lock active? Blank-Circlet? Reciprocal-recognition path begun?).
- Tiran's final state.
- Wena stays at Korrath.
- Sixth-forging synthesis (if Kessa articulated; near-delivery for #0007).
- Aelwen triplet fragment in Kessa's custody.
- Party XP: 2,075 + ~450 = ~2,525 each.
