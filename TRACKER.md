# Marathon Tracker

Last updated: 2026-04-19 by `session-handoff` (S03).

## Sessions

| S# | Adventure | Party | Date | Gate /80 | Panel weighted /80 | Verdict |
|---|---|---|---|---:|---:|---|
| S01 | 0001-tomb-of-the-silver-rose | varduin-muster | 2026-04-18 | 65 | 65.0 | ADVISORY |
| S02 | 0002-the-bone-collector-trap | varduin-muster | 2026-04-19 | 65 | 65.0 | ADVISORY |
| S03 | 0003-the-silversmiths-mirror | varduin-muster | 2026-04-19 | **74** | **74.48** | ADVISORY (last advisory) |

## Adventures

| Slug | Status | Revision | Sessions run | Notes |
|---|---|---|---|---|
| 0001-tomb-of-the-silver-rose | played, rev 3 | 3 | S01 | Rev 3: Scriptorium compressed; Cold Pulse v1.1-compliant; Aelwen's daughter Heva named; Mira Vaenshold-Silversmith seeded. |
| 0002-the-bone-collector-trap | **played, rev 2** | 2 | S02 | Rev 2 applied all 5-persona review fixes pre-play. Played 2026-04-19; gate 65/80; panel mean 65.0/80. Outcome: Varran-reliquary attuned by Aelric (campaign-permanent: remembers Varran only as dying); Keloth killed in Scene 6 combat; Pella at Brother Laen's mother's by her own choice; Mira-letter delivered; 5 shelf-reliquaries recovered; Varduin east wing burned; Sir Venric fell. **Cross-adventure signal missed on dice** (Kessa Inv 12 / Perc 11 vs DC 13 twice). |
| 0003-the-silversmiths-mirror | **played, P0-revised** | P0 post-5-persona | S03 | Campaign position 3/7 Moon-Silver Cycle. Emotion: Love. Spotlight: Kessa. **Played 2026-04-19; gate 74/80; panel mean 74.48/80 (spread 0.9). Highest-scoring session in workshop history (+9 over prior mean).** Outcome: Mira saved and departed for Stonfold with Harel; **Mirror destroyed via Reorx-rite (Kessa Portent rescue)**; no PC attuned; Kann + Vend dead; Pevra + Lorn + Gorr captured. **Cross-adventure phrase CAUGHT** (Kessa Inv 16). Aelwen's journal page, Kann's Stonfold finger-bone, Tova Stonfold + Felor all planted as seeds for #0004-#0007. |

## Parties

| Slug | Members | Status | Sessions played | Notes |
|---|---|---|---|---|
| varduin-muster | Aelric of Crownhold · Thera Hillfoot · Kessa Moonweave · Grom Ironhand | active | 3 | Post-S03: Aelric's Varran-memory state unchanged (still only remembers him dying). **No new attunements** — all four PCs declined the Mirror. **Kessa carries:** Aelwen's journal page (Hint 4 pre-plant), cross-adventure phrase in notebook (S02 recovery — pattern-link pending), Kann's Stonfold finger-bone ID'd (Felor engraved on cord). **Grom carries:** ~8 oz inert un-forged Mirror-silver; Mira's Council file-note with Seralen's name in ink. **Thera carries:** Seralen's *"Do not look"* note. **Aelric:** Mira's silver pendant (gift). **XP 1,675 each** (L3; 125 shy of L4). |

## Parties (historical note)

*Earlier party state (post-S01): no attunement; carried Notched Longsword, Pella's drawing, 25 gp Ergothian, 10 gp Bone-Collector signet. Current state above.*

## Rubric

- Current version: **v1.2** (amended 2026-04-19 post-S02).
- **Amendments adopted:**
  - v1.0 → v1.1 proposal A: Mechanical fairness cross-dimensional-harmlessness anchor.
  - v1.0 → v1.1 proposal B: Atmospheric landing per-PC reception + chain-reaction anchors.
  - v1.1 → v1.2 proposal C: Module fidelity anchor-level passive-Perception fallback + recovery-path.
  - v1.1 → v1.2 proposal D: Atmospheric landing finder-vs-receiver separation + silent-reception recognition.
- **Amendments PROPOSED post-S03 (v1.2 → v1.3, pending user approval):**
  - **Proposal E:** Module Fidelity — positional-redundancy + NPC-delivered-recall as third fallback mechanism for anchor-level symptoms.
- Amendment history: see `personas/playtest-rubric.md#amendment-history`.

## Innovations Catalog

| Status | Count |
|---|---:|
| Logged | 24 (7 from S01 + 10 from S02 + 7 from S03) |
| **Adopted** | **9** (5 v1.1 + 4 v1.2) |
| Proposed (v1.3 candidates) | 3 (Proposal E constituents) |
| Reviewed — not adopted | 0 |
| Promoted to style (pending) | 12 (4 × `sheet-deep-reader` from S01-S02 + 1 S03 reinforcement; 4 × `craft-witness` from S01-S02 + 3 S03 reinforcements) |

## Player Styles

| Slug | Proposed on | Source sessions | Status |
|---|---|---|---|
| `sheet-deep-reader` | 2026-04-19 post-S02 | S01 (3) + S02 (1) + S03 (1) = **5 instances across 3 sessions** | PROPOSED — **strongly ready, pending approval** |
| `craft-witness` | 2026-04-19 post-S02 | S01 (2) + S02 (2) + S03 (3) = **7 instances across 3 sessions** | PROPOSED — **strongly ready, pending approval** |
| `doctrinal-silence` *(candidate; not formally proposed)* | 2026-04-19 post-S03 | S03 (1) = 1 instance | CLUSTER CANDIDATE — watch for S04 repeat |

**Player-style cluster evidence continues to strengthen.** Both proposals have grown every session; `craft-witness` has 7 instances (nearly double Chronicle's 3-instance threshold). Stalling approval is harmless but leaves `personas/player-styles/` unpopulated for lens-tuning in #0004+.

## Skills Built

| Skill | Built on | Status | Runs |
|---|---|---|---|
| dungeon-smith | 2026-04-18 | with quality gates (rev 2) | 1 (adventure 0001) |
| treasure-forger | 2026-04-18 | with manifest handshake | 1 (Silver Rose + manifest) |
| module-binder | 2026-04-18 | with inlined-SRD rule | 1 (module.md for 0001) |
| adventure-lint | 2026-04-18 | new | 1 (0001 baseline) |
| party-builder | 2026-04-18 | new | 1 (varduin-muster) |
| dice-roller | 2026-04-18 | `scripts/dice.sh` verified | many (per S01) |
| session-runner | 2026-04-18 | new | 1 (S01) |
| session-gate | 2026-04-18 | new | 1 (S01-gate) |
| playtest-panel | 2026-04-18 | new | 1 (S01-panel) |
| playtest-innovation | 2026-04-18 | new | 1 (S01 append) |
| session-handoff | 2026-04-18 | new | 1 (HANDOFF-S01) |
| lore-weaver | — | deferred | 0 |
| encounter-balancer | — | deferred | 0 |
| rule-lookup | — | deferred | 0 |
| persona-review | — | deferred (5 design reviews ran manually) | 0 |

## Recent Activity

**2026-04-19 (S03):**
- #0003 fully designed (rooms, NPCs, treasures, encounters, module). 5-persona design review: aggregate 64.2/80 (strong draft on shippable edge). **P0 revisions applied** (7 convergent critiques, ~45min authorial pass): Scene 2 sensory texture, Harel's aside, Scene 6 chamber detail, Blank-Mirror read-aloud, Option C no-Agent fallback, campaign-continuity MANDATORY callout, Mira combat-spatial.
- **S03 played end-to-end.** 7 scenes, ~5,500 word log, 28+ dice rolls traced to seed `S03-20260419`.
- **Outcome:** Mira + Harel saved and departed for Stonfold; Mirror DESTROYED via Grom's Reorx-rite (rescued by Kessa's Portent [14]); no PC attuned; Kann + Vend dead; Pevra + Lorn + Gorr captured. **Cross-adventure phrase CAUGHT** (S02 recovery complete).
- **Gate 74/80 ADVISORY** (last advisory session; S04+ binding). **Panel mean 74.48/80; spread 0.9** — +9.48 over S01/S02 mean; narrowest spread in workshop history.
- 7 innovations logged (I-S03-01 through I-S03-07). Amendment Proposal E drafted (v1.3 candidate: Module Fidelity positional-redundancy). Player-style promotions strongly ready.

**2026-04-19 (S02):**
- #0002 revised to rev 2 post-5-persona-panel (panel mean 68.8/80 pre-fix; all priority-1/2/3 suggestions applied).
- S02 played end-to-end — 8 scenes, ~3,500 word log, 30+ dice rolls traced to seed.
- Outcome: Aelric attuned Varran-reliquary (campaign-permanent memory-loss); Keloth killed; Pella rescued; Mira-letter delivered.
- Gate 65/80 ADVISORY (identical to S01). Panel mean 65.0/80 (identical to S01). **Quality holding, not improving.**
- 10 innovations logged. 2 amendment proposals (v1.2). **2 player-style proposals — first ever.**
- Cross-adventure signal ("I will not look at the rose again") was in the room and missed on dice twice. Kessa's notebook has it transcribed — re-discovery path open for S03.

**2026-04-18 (S01):**
- Adventure 0001 built to rev 2, reviewed by 5 design personas, linted. Varduin Muster party built.
- S01 played end-to-end. 12 innovations logged; rubric amended v1.0 → v1.1.
- Seeds for #0002: Bone-Collectors, Pella, Brother Laen's sister Wena, Aelric's condition on Laen, Kessa's Vethrenn connection.

## Pipeline Position

S01, S02, S03: all 7 stages completed (PREP → PLAY → LOG → GATE → PANEL → INNOVATE → HANDOFF).

## Next Priorities

1. ~~v1.1 amendments A + B~~ ✓ adopted 2026-04-18.
2. ~~Module-level convergent suggestions pre-S02~~ ✓ applied 2026-04-18.
3. ~~#0002 design + rev 2 + play~~ ✓ complete 2026-04-19.
4. ~~v1.2 amendments C + D~~ ✓ adopted 2026-04-19 (before S03 play).
5. ~~Option C pipeline~~ ✓ designed + triggered (did not fire S03 — all PCs declined; infrastructure ready for S04+).
6. ~~Anthology/campaign policy reconciliation~~ ✓ resolved (campaign-reward on anthology-floor; S03 first tested).
7. ~~Campaign spine built~~ ✓ (campaign-planner, seed-tracker, arc-audit skills; Moon-Silver Cycle 7-adventure spine).
8. ~~Design + play #0003~~ ✓ complete 2026-04-19; highest-scoring session to date.
9. **User approves / declines Amendment Proposal E (v1.3)** — Module Fidelity positional-redundancy. Rubric holds at v1.2 until action.
10. **User approves / declines player-style promotions** — 5 + 7 instances across 3 sessions; ready.
11. **Write campaign-continuity updates to `CLAUDE.md`:** Mirror destroyed; no PC attuned; Mira at Stonfold; Kann dead.
12. **Design adventure #0004** — the Rage adventure. Thane Krun Ironhaft; Duren's murder revealed; Hint 2 unlock at Reorx-rite; spotlight Grom.
13. **Optional #0003 rev 2** — apply S03 panel suggestions (positional-redundancy for filigree anchor; destruction-path design-weight; Scene 4 silence-cue; Portent cheatsheet line).
14. **Engineer Kessa journal-reading beat** — between-adventure scene where Kessa cross-refs her S02 notebook with the ledger-phrase. Closes finder-vs-receiver partial-reception (I-S03-02).
