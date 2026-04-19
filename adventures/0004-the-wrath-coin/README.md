---
adventure: 0004-the-wrath-coin
campaign: moon-silver-cycle
tier: 1
author: human
created: 2026-04-19
---

# 0004 — The Wrath-Coin

**Tier:** 1 (party of 4 entering at L3 ~1,675 XP; exits at L4 ~2,075 XP).
**Expected playtime:** one session, 3-4 hours.
**Setting:** Kharolis foothills; Gavrek's Anvil shrine + Kruntharrak mine-hold; late Age of Might (PC 20, ~two weeks after S03).
**Status:** Designed rev 1 (spine-aware, rubric-v1.3-compliant, player-style-aware). Awaiting 5-persona design review, then S04 play.
**Campaign position:** #0004 of 7 in the Moon-Silver Cycle. Emotion: **Rage.** Spotlight: **Grom.**

## One-line logline

A forge-priest returns to his master's grave for the three-year rite — and discovers the mine-collapse that killed his master was no collapse. The hammer that should be buried with Duren is not. What Duren was secretly forging — Aelwen's fourth moon-silver artifact, a coin that holds the rage of every person the bearer has ever wronged — is in a Thorbardin elder's vault, and he intends to use it this week.

## What's in this directory

```
premise.md                                      logline, hook, constraints, seeds
npcs/thane-krun-ironhaft.md                     Krun; 71; Palanthan Thane; commissioner; half-brother to Duren
npcs/sigga-coalbeard.md                         Sigga; 58; Duren's widow; shrine-keeper's wife; hammer-keeper
npcs/jarek-stoneforge.md                        Jarek; 45; Krun's enforcer; Duren's killer; sleepless
treasures/wrath-coin.md                         Central artifact — Aelwen's 4th forging
treasures/wrath-coin-manifest.md                Cross-skill handshake (rubric v1.3 compliant; positional-redundancy)
treasures/minor-loot.md                         Items with Purpose tags; cross-adventure seeds
encounters/road-ambush.md                       Scene 1 conditional stall
encounters/shaft-descent.md                     Scene 5 conditional combat
encounters/krun-confrontation.md                Scene 6 climax (multi-branch)
encounters/wandering-pressure.md                Shrine-plus-road variant (rubric v1.3)
rooms/map.md                                    Regional + shrine-cluster + mine-hold layout
rooms/01-road-ambush.md                         Kharolis road; Jarek's stall
rooms/02-gavreks-anvil-arrival.md               Shrine; Sigga; Krun's "cousin" claim
rooms/03-durens-grave-reorx-rite.md             THE RITE — Hint 2 unlocks; Hint 3 plants
rooms/04-the-forge-records.md                   Archive; Aelwen's apron-scrap; kinship revealed
rooms/05-the-lower-ore-shaft.md                 Murder evidence
rooms/06-thane-kruns-hall.md                    Confrontation + attunement race
rooms/07-aftermath.md                           Duren re-interred; Grom's scar stops; Wena's note
module.md                                       [to be compiled by module-binder]
reviews/                                        [5-persona review, pending]
sessions/                                       [S04 output goes here]
```

## Campaign-spine integration

**Seeds retrieved this adventure:**
- Thane Krun Ironhaft (#0003 Mira's ledger) — fully present
- Duren Coalbeard's death context (S01 Grom PC sheet) — re-contextualized as murder
- Vethrenn's warded margin-note (#0001; near-unlocked #0003) — **UNLOCKS at Scene 3 Reorx-rite**
- Aelwen's journal page / ingot reference (#0003 Hint 4 pre-plant) — reinforced with Scene 4 apron-scrap

**Seeds planted this adventure:**
- **Hint 3 — Reorx's Judgment on Aelwen's grief-forging** (NEW; campaign-permanent; delivered Grom via craft-witness)
- **Wena Laen's note** (for #0005 Pride adventure) — delivered at Scene 7
- **Jarek Stoneforge's post-session fate** (per disposition)
- **Sigga's confession of three-year knowledge** (post-campaign moral-object)
- **Kruntharrak mine-hold confiscated or inherited** (Thorbardin political outcome)

**Hint status at end of #0004:**
- Hint 1 (Fresco-Heal) — still caught from S01; available for recall
- Hint 2 (Vethrenn warded margin) — **UNLOCKED** in full
- **Hint 3 (Reorx's Judgment) — PLANTED** (NEW hint; campaign-permanent)
- Hint 4 (Aelwen's Confession ingot) — pre-planted #0003; reinforced #0004; full delivery at #0007

## The real decisions the adventure asks

Four overlapping:

1. **Does Grom forgive, kill, or Reorx-exile Thane Krun?** The spotlight PC's Option-C moment. Grom's PC-sheet decision order is tested against a documented fratricide by his forge-master's half-brother. The Reorx-exile path is unlocked by Hint 3 received at Scene 3.
2. **Does a PC attune the Wrath-Coin?** The attunement is 1-round with a burn-warm-before-attune window; the holder can drop. Grom is the highest-risk candidate (his grief-paragraph is most aligned with attunement under rage-pressure).
3. **Is the coin destroyed, attuned, Reciprocally-Forgiveness-emptied, or surrendered?** Each routes the #0007 finale differently.
4. **Is Krun's household attacked or negotiated with?** Thorbardin political implications.

## Player-style alignment

- **Craft-witness** (ratified): this adventure **heavily features** craft-witness reception. Grom delivers at Scene 3 (Hint 3), Scene 5 (murder realization), Scene 6 (Reorx-exile ritual). If the workshop's `craft-witness` PC-style was ever going to prove itself across sessions, this is the adventure.
- **Sheet-deep-reader** (ratified): Kessa's commonplace-book-plus-apron-scrap cross-referencing fires multiple times. Her S01 private-arc-paragraph now actively drives session-mechanics.
- **Doctrinal-silence** (candidate): if a PC faces Krun's attunement-race and chooses restraint over domination (not-attacking-Krun when they could) — that is doctrinal-silence behavior. Watch for it.

## Rubric v1.3 compliance

- ✅ All anchor-level symptoms have ≥ 2 of 3 fallback paths (v1.3 positional-redundancy)
- ✅ Per-PC reception with finder-vs-receiver (v1.2)
- ✅ Silent reception counted (v1.2)
- ✅ Cross-adventure recovery path documented (v1.2)
- ✅ Memory Fragment per scene (v1.0 suggested)
- ✅ Every NPC named has `npcs/<slug>.md`

## Next steps

- Run `adventure-lint` on this directory to verify rubric v1.3 compliance + campaign-awareness gates.
- Run `module-binder` to produce `module.md`.
- Optional: 5-persona design review (Gygax, Jaquays, Schick, Moldvay, Stuart).
- Play **S04** with the Varduin Muster.

## Post-session commitments (for CLAUDE.md#campaign-continuity)

After S04 plays, update `CLAUDE.md#campaign-continuity` with:
- Wrath-Coin disposition (destroyed / attuned / emptied / surrendered).
- Thane Krun's fate (Reorx-exile / Thorbardin law / dead / escaped).
- Jarek's fate (confessed-Thorbardin / dead / escaped).
- **Hint 2 UNLOCKED** (Vethrenn's margin readable).
- **Hint 3 PLANTED** (Reorx's Judgment — Grom carries the understanding into #0007).
- Krun-Duren half-kinship publicly named.
- Grom's burn-scar state (aching resolved).
- Party XP L4; Wena's note delivered.
