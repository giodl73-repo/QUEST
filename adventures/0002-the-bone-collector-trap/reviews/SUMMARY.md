---
adventure: 0002-the-bone-collector-trap
author: human (5-persona aggregate)
created: 2026-04-19
sources:
  - reviews/gygax-2026-04-19.md
  - reviews/jaquays-2026-04-19.md
  - reviews/schick-2026-04-19.md
  - reviews/moldvay-2026-04-19.md
  - reviews/patrick-stuart-2026-04-19.md
---

# Review Summary — *The Bone-Collector Trap*

Aggregated 5-persona design review of adventure #0002, run at design time (pre-S02 play).

## Weighted Score Board

| Persona | Unweighted /80 | Weighted /80 | Relative to mean | Δ vs. #0001 |
|---|---:|---:|---:|---:|
| **Patrick Stuart** | 68 | **71.2** | +2.4 | +0.7 |
| **Lawrence Schick** | 68 | **69.5** | +0.7 | +0.3 |
| **Jennell Jaquays** | 67 | **68.6** | -0.2 | +4.0 |
| **Tom Moldvay** | 68 | **68.4** | -0.4 | +1.7 |
| **Gary Gygax** | 66 | **66.2** | -2.6 | +4.4 |
| **Panel mean (weighted)** | **67.4** | **68.8** | | **+2.2** |

**Panel verdict:** 68.8 / 80 weighted mean — **shippable** (per rubric's 65+ "shippable; run as-is" band). Panel spread **5.0 points** (Stuart high, Gygax low), tighter than #0001's 8.7-point spread.

**Notable improvements over #0001:**
- **Jaquays up 4.0 weighted points.** His chief critique of #0001 was static inhabitants; #0002 has dynamic inhabitants (patrol timing, Pella's off-screen distraction, Keloth's state transitions).
- **Gygax up 4.4 weighted points.** The Cold Pulse rubric v1.1 fix specifically answered his concern about mechanics damaging atmospheric payoffs. He explicitly approved the redesign.
- **Stuart remains the highest scorer.** The reliquary's specific-minute mechanic, Mensa's bread-to-a-dead-brother, Pella-not-knowing-her-mother's-name — all the image-level precision he asked for at the end of S01.

## Per-Axis Averages (unweighted)

| Axis | Avg | Low | High | Spread |
|---|---:|---:|---:|---:|
| Treasure-as-story | **9.4** | 9 (Gygax, Jaquays, Moldvay) | 10 (Schick, Stuart) | 1 |
| Player agency | **9.2** | 8 (Schick) | 10 (Gygax, Jaquays) | 2 |
| Curse/consequence | **9.0** | 8 (Jaquays, Moldvay) | 10 (Schick, Stuart) | 2 |
| Premise clarity | **8.8** | 8 (Jaquays) | 9 (others) | 1 |
| Table-readiness | **8.0** | 7 (Stuart) | 9 (Moldvay) | 2 |
| Lore grounding | **7.8** | 7 (Gygax, Jaquays) | 9 (Stuart) | 2 |
| Dungeon integrity | **7.6** | 7 (Gygax, Schick, Stuart) | 9 (Jaquays) | 2 |
| Encounter craft | **7.6** | 7 (Gygax, Stuart) | 8 (Jaquays, Schick, Moldvay) | 1 |

## Strongest Consensus

**Treasure-as-story (9.4).** Unanimous 9-or-10. Schick: *"The Varran-occupancy is the masterstroke."* Stuart: *"The central object is a specific minute of a specific death."* Gygax even, not prone to praise, grants 9.

**Player agency (9.2).** Gygax and Jaquays both scored 10. The trade-at-the-altar is the most agentic scene in the workshop's output.

**Curse/consequence (9.0).** Schick and Stuart both 10. Schick called it *"the best treasure this workshop has made, and by a real margin."*

## Most Dissent

**Dungeon integrity (7.6).** Gygax 7 ("five stronghold rooms is still thin") vs. Jaquays 9 ("Jaquaysed at its scale; earned shortcut, loops, verticality"). The philosophical split: size vs. density. Gygax wants more rooms for more attrition; Jaquays approves the topology *at the scale chosen*.

**Table-readiness (8.0).** Moldvay 9 (cheatsheet now includes 19 scene-triggers, per-PC reception table, consequence-tracking for #0003) vs. Stuart 7 (denser than a tier-1 DM with an hour of prep should be expected to run). Both lenses correct for their own weights; Moldvay carries weight 1.5 on this axis, Stuart 0.4.

## Convergent Suggestions (multiple personas agree)

### Priority-1

1. **Raise the climax combat baseline.** Gygax (more Cultists at Routine; returning-Lieutenant at Alert) and Jaquays (pre-offer Idra encounter in the corridor before the altar) propose different-but-compatible fixes: the combat path needs more weight. **Unified fix:** Routine = Keloth + Idra + 1 Cultist (3 creatures; 500 base × 2 = 1000 XP, moves from hard → deadly); Alert = Keloth + Idra + 3 Cultists + a returning Lieutenant mid-fight as a second-wave (+200 XP midway through; genuine TPK-risk for a deadly climax).

2. **Add the Vault wall-ledger.** Schick proposed (charcoal list of names, decades long, crossed/circled); Stuart echoed (the ledger should include one phrase verbatim from #0001 — *"I will not look at the rose again"* from Vesk's memory fragment — uncredited, as cross-adventure signal); Moldvay would approve as a tracker. **Unified fix:** add to `rooms/06-reliquary-vault.md` Features: a charcoal ledger on the north wall, decades of names with dates and locations; one entry is uncredited and reads *"I will not look at the rose again"*; briefly brightens when the Varran-reliquary is lifted (Kessa Perception DC 13).

### Priority-2

3. **Add interior layers to the Cell-Block.** Jaquays (tally-marks, second-cell chalk-drawing, third-cell floor-stain) + Stuart (environmental density) converge. **Fix:** three quick additions to `rooms/07-cell-block.md` Features: tally-marks near cell two's bolt (counting days, suggests a long-term prior prisoner), a chalk woman-figure half-wiped in cell one (a prior prisoner's attempt at portrait), a dark floor-stain in cell three (Investigation DC 13: old blood).

4. **Add the attribution-drift tracker to the cheatsheet.** Moldvay explicit; Schick implicit. **Fix:** six-row table on the cheatsheet listing the six beats with scene references so a DM can tick boxes during play.

5. **Add the Keloth-trade decision table to the cheatsheet.** Moldvay explicit. **Fix:** four-line decision summary on the cheatsheet, replacing the narrative-prose-at-the-altar for in-scene reference.

6. **Inline Pella's stat block at Scene 06.** Moldvay explicit. **Fix:** two-line reminder in Scene 06 Features.

### Priority-3 (divergent; keep or ignore)

- **Gygax:** a two-paragraph sketch of Brother Laen's retrieval-team defense of Varduin (the western feint) to include on the ride-home scene. Currently "resolved off-screen" — Gygax wants texture.
- **Jaquays:** partial ledge in the well-shaft (sealed second-level landing; hook for a future session); one Bandit at the well-cover in Alert state; the Alert-state should include a well-guard.
- **Schick:** commit to the empty reliquary's appearance (polished, eye-sockets open, silver thread at the ready); make one shelf-reliquary carry a specific named woman (not abstract) as a future-hook.
- **Moldvay:** post-S02, update premise.md from intent-state to post-play state.
- **Stuart:** commit to Pella's interior at the Aelric-recognition moment — one sentence the DM is told she *has decided* the answer with certainty; add a sensory echo at reliquary-lift (charcoal ledger briefly brightens).

## Questions Raised About the Module or the System

1. **The Cold Pulse v1.1 fix landed cleanly.** Both Gygax and Moldvay explicitly noted the redesign; neither flagged cross-dimensional damage. The rubric amendment worked. This is evidence the workshop's feedback loop is operating as designed.

2. **Atmospheric-landing-per-PC (rubric v1.1 addition) was met by the design, not by the scoring panel.** Gate-stage hasn't happened yet (S02 not played). The 15-row tracking table in `module.md`'s cheatsheet is the design's answer; the panel could not score it against play.

3. **The combat-path vs. stealth-path asymmetry** is a recurring note. A party that takes the well shortcut bypasses two sub-encounters and faces Keloth with near-full resources. Jaquays, Gygax, Schick all touched this. The priority-1 fix (raise climax baseline) partly addresses it.

4. **The cross-adventure signal** (the repeated phrase "*I will not look at the rose again*" proposed to appear in Keloth's wall-ledger) is Stuart's most ambitious note. It asks the workshop to commit to **cumulative cross-session signaling** as a design principle. If adopted, future adventures should all carry at least one such signal backward.

5. **The narrative-XP award for accepting the trade (400 XP/PC with no combat)** is an untested mechanic. Gygax would prefer it be earned through *something* — a Persuasion check to parley cleanly, or a cost paid (Aelric surrenders the Notched Longsword as gesture, say). Worth considering: a narrative award that costs something still feels earned, where a narrative award that costs nothing risks feeling free.

## Panel Verdict (unified)

**#0002 is shippable at 68.8 / 80 weighted.** Priority-1 fixes should be applied pre-S02 (they're small and they clear the strongest dissent): raise the climax baseline; add the wall-ledger with cross-adventure phrase. Priority-2 fixes are polish and can land post-S02. Priority-3 suggestions are per-lens preferences; adopt as taste dictates.

**Compared to #0001:** the workshop's feedback loop is producing real quality-gain. Rubric v1.1 amendments landed. Lint discipline held. Manifest-distribution improved. Cross-adventure continuity is starting to function (moon-silver alloy linking #0001 and #0002, Mira Vaenshold-Silversmith seeded from #0001, Varran as reliquary-occupant mirroring Ilendra-Caen as grief-pair). This is what emergent design looks like when a workshop has a working rubric-amendment cycle.

## Next Actions

- **Apply Priority-1 fixes** (raise climax; wall-ledger + cross-adventure phrase). Update `module.md` to reflect.
- **Apply Priority-2 fixes** at leisure (cell-block layers, cheatsheet additions).
- **Run S02** — Varduin Muster on #0002, rubric v1.1 locked in PREP frontmatter.
- **Post-S02:** full harvest pipeline (gate → panel → innovation → handoff). Watch for cross-session clustering — if any pattern from S01's innovations recurs, player-style emergence is in range.
