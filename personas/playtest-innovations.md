---
name: playtest-innovations
description: Append-only log of surprising moves/patterns/techniques discovered during playtest sessions. Cluster → player-style (3+); dimension-concentration → rubric amendment (2+).
version-schema: v1
created: 2026-04-18
status: living
---

# Playtest Innovations Log

An append-only log of surprises the current playtest rubric did not anticipate. Each entry carries a dimension tag, source session, status, and cross-applicability note.

## Thresholds

- **Rubric amendment trigger:** 2+ `logged` innovations in the same dimension. Propose amendment; if adopted, mark constituents `adopted (vX.Y)`, increment rubric version.
- **Player-style emergence trigger:** 3+ `logged` innovations clustered by theme across ≥ 2 sessions. Propose a new entry in `personas/player-styles/<slug>.md`. If adopted, mark constituents `promoted-to-style (<slug>)`.

## Statuses

- `logged` — new entry; no action yet.
- `proposed` — part of an amendment/style proposal pending user review.
- `adopted (vX.Y)` — contributed to a rubric version or player-style.
- `reviewed — not adopted (reason)` — considered and declined.

## Entries

*(Appended by `playtest-innovation` skill after each session's LOG stage. Below is the initial entry format / template.)*

---

### Template

```markdown
### [Date] — [Session] — [Party] — [Adventure]

**Technique:** [Short title]
**Dimension:** [Engagement / Mechanical fairness / Pacing / Character agency / Module fidelity / Atmospheric landing / Surprise / Table readiness]
**What happened:** [Quoted passage from session log, with scene reference]
**Why the rubric did not anticipate it:** [Specific]
**Scope:** [Party-specific / Adventure-specific / Universal / Multi-session cluster]
**Status:** [logged / proposed / adopted (vX.Y) / promoted-to-style (slug) / reviewed — not adopted]
```

---

## S01 — 2026-04-18 — varduin-muster — 0001-tomb-of-the-silver-rose

### I-S01-01 — Pre-adventure character hook inverts session center-of-gravity

**Dimension:** Character agency (cross: Engagement, Surprise)
**What happened:** *"Kessa went still. She had spent the winter waiting for a signal. She understood, in the five seconds between Laen's sentence and her own reply, that this was the signal."* (Scene 1) Kessa's CRIT Arcana on Laen's description revealed the adventure was already Vethrenn's rose, a connection only her PC sheet carried.
**Why the rubric did not anticipate it:** Character-agency anchors assume session-scope choices. A PC-sheet-level hook that pre-aligns the PC with the adventure reframes the session's meaning for that PC before any in-session dice. The rubric has no anchor for this.
**Scope:** Universal (any well-hooked PC can produce this).
**Status:** logged (see post-S01 threshold note for adopted-to-v1.1 entries)

### I-S01-02 — Craft-ritual PC receives atmospheric flags over knowledge-casters

**Dimension:** Atmospheric landing (cross: Character agency)
**What happened:** Grom (hearth-greeting Life cleric) failed the voice-fragment save in R02 (`1d20+3` → 6 vs DC 10) — he was the one the tomb spoke to. Kessa (Divination wizard, expected "listener") passed (rolled 12).
**Why the rubric did not anticipate it:** "Atmospheric landing" is scored as session-level. It does not anticipate that *which PC* receives a flag can be counter-intuitive and character-defining, driven by failed Wisdom saves rather than caster-class.
**Scope:** Universal (applies any time wisdom saves gate atmospheric flags).
**Status:** logged (see post-S01 threshold note for adopted-to-v1.1 entries)

### I-S01-03 — Foreshadowing clues missed by exhausted opening rolls

**Dimension:** Module fidelity (cross: Mechanical fairness)
**What happened:** Opening-room clues ("Sister of Caen" at DC 13/15 and unnatural quiet at DC 10) all failed on the party's cold opening rolls (Thera 7, Grom 5). The party never recovered the foreshadowing.
**Why the rubric did not anticipate it:** Module fidelity treats "manifest symptoms landed" as binary. It does not anticipate that tier-1 opening DCs can produce a session that never sees the set-up at all, independent of any curse-mechanic.
**Scope:** Adventure-specific (the Rose Cairn's opening room DCs); pattern: universal (opening-room clue DCs need a safety-net for cold rolls).
**Status:** logged (see post-S01 threshold note for adopted-to-v1.1 entries)

### I-S01-04 — PC local-origin produces setting-knowledge the module did not anticipate

**Dimension:** Character agency (cross: Module fidelity)
**What happened:** Thera (born Varduin, raised in the Solamnic way-house) recognized VANOR as a mis-carving of Vaenor — a Solamnic family name. Kessa, with higher stats and Solamnic-adjacent education, could read the carving but did not flag its family-name-significance.
**Why the rubric did not anticipate it:** Character agency doesn't anchor on origin-expertise. A PC whose background puts them geographically or culturally local to the adventure carries setting-knowledge that module DCs alone don't capture.
**Scope:** Universal.
**Status:** logged (see post-S01 threshold note for adopted-to-v1.1 entries)

### I-S01-05 — PC private-arc investigation runs parallel to party objective without diminishing it

**Dimension:** Character agency (cross: Engagement, Surprise)
**What happened:** Kessa's private Vethrenn investigation (Scenes 1, 4, 6, 8) ran through the entire session. She did not share what she learned with the party. The party's shared arc was not diminished; the session gained a second layer.
**Why the rubric did not anticipate it:** The rubric assumes party-level shared-objective play. Parallel private arcs are not scorable as "agency" in the current anchors; they read as "engagement" loosely.
**Scope:** Universal for parties with long-hook PCs.
**Status:** logged (see post-S01 threshold note for adopted-to-v1.1 entries)

### I-S01-06 — Unspoken resource-sharing heuristics emerge without coordination

**Dimension:** Character agency (cross: Mechanical fairness)
**What happened:** *"She pulled her hood, set her teeth, and took 1 level of exhaustion ... She did not announce it. Grom noticed; said nothing; filed the information."* (Scene 4) Kessa chose not to report her exhaustion, preserving Grom's Lesser Restoration slot.
**Why the rubric did not anticipate it:** Mechanical fairness anchors assume transparent resource tracking. In-character resource discretion (hiding damage to preserve party economy) is a character-agency move, not a fairness failure.
**Scope:** Universal.
**Status:** logged (see post-S01 threshold note for adopted-to-v1.1 entries)

### I-S01-07 — Craft-metaphor PCs produce theological / structural readings knowledge-casters miss

**Dimension:** Atmospheric landing (cross: Character agency, Surprise)
**What happened:** *"This is not a device. This is a starvation. It eats who made it."* (Scene 6, Grom to party) Grom's forge-metaphor worldview produced a theological reading of the rose's deep mechanic that Kessa's scholarly cataloging had not reached.
**Why the rubric did not anticipate it:** Atmospheric landing anchors don't capture the difference between *intellectual* and *craft* readings of a curse. Craft-ritual PCs produce session-level interpretive insight the module didn't scaffold.
**Scope:** Universal for parties with craft-metaphor PCs (forge-priests, Reorx-ordained, artisan-ordained).
**Status:** logged (see post-S01 threshold note for adopted-to-v1.1 entries)

### I-S01-08 — Wandering-pressure mechanic produces narrative-door-closings as byproduct

**Dimension:** Mechanical fairness (cross: Pacing, Module fidelity)
**What happened:** Wandering roll outcome 4 (collapse) at 30-min mark triggered a collapse of R02's east archway — narratively correct but DM-selected rather than randomly-selected among specific corridors. The collapse closed a backtrack path and forced a specific ascent route.
**Why the rubric did not anticipate it:** The wandering-pressure table was designed for atmospheric/mechanical pressure, not for narrative door-closings. The mechanic produced a stronger effect than intended.
**Scope:** Adventure-specific initially; universal pattern for wandering tables with "collapse" outcomes.
**Status:** logged (see post-S01 threshold note for adopted-to-v1.1 entries)

### I-S01-09 — Exhaustion mechanic (Cold Pulse outcome 3) actively damages atmospheric payoffs

**Dimension:** Mechanical fairness (cross: Atmospheric landing, Module fidelity)
**What happened:** Cold Pulse outcome 3 (DC 10 Con or 1 exhaustion, disadvantage on ability checks) directly caused TWO missed atmospheric payoffs: Thera's R03 pillar inscription (rolled 8 kept on dis) and Aelric's post-combat Religion check (rolled 10 kept on dis).
**Why the rubric did not anticipate it:** Mechanical fairness and Atmospheric landing are scored as independent dimensions. This innovation shows they can interact destructively: a "fair" mechanic damages atmospheric payoffs. The rubric needs a cross-dimensional harmlessness anchor.
**Scope:** Adventure-specific (this Cold Pulse design); universal pattern for ability-check-based atmospheric gates.
**Status:** logged (see post-S01 threshold note for adopted-to-v1.1 entries)

### I-S01-10 — Atmospheric-reward fell on the PC with cleanest dice, not the PC with the expected grief-mirror

**Dimension:** Atmospheric landing (cross: Surprise, Mechanical fairness)
**What happened:** Panel 6's fresco-heal revealed Ilendra's parents' faces for one heartbeat. Grom (`1d20+3` → 23 CRIT) saw them clearly. Aelric (expected grief-mirror recipient; `1d20+1 dis` → 2 FUMBLE) did not.
**Why the rubric did not anticipate it:** Atmospheric landing anchors assume design-targeted PCs receive design-intended payoffs. Dice determine reception. Grom, with no curse-mirror, received the session's gift.
**Scope:** Universal.
**Status:** logged (see post-S01 threshold note for adopted-to-v1.1 entries)

### I-S01-11 — PC-interpretive-insight produces theological readings that outlive the session

**Dimension:** Surprise (cross: Atmospheric landing)
**What happened:** *"It has guilt ... Or — its maker did. And the rose remembers the guilt, even when it's taking."* (Scene 8, Kessa) Kessa reached a reading of the rose's behavior as involuntary return-of-stolen-material — not scaffolded by the module.
**Why the rubric did not anticipate it:** Surprise anchors count *tags* not *theological reach*. A PC's out-of-module interpretive leap can sharpen the adventure's own meaning in a way that survives the session.
**Scope:** Universal.
**Status:** logged (see post-S01 threshold note for adopted-to-v1.1 entries)

### I-S01-12 — Grief-paragraphs chain-react between PCs via atmospheric density, without mechanics

**Dimension:** Atmospheric landing (cross: Character agency, Surprise)
**What happened:** *"The smell of the savory-and-rye bread her mother had baked, twenty-three years ago, came into the room — briefly, impossibly — and went."* (Scene 8, Thera) Grom's offering of Pella's drawing to the Echo triggered a sensory-memory in Thera — without any save, check, or dice. Multi-PC grief-parties produce inter-PC emotional chains.
**Why the rubric did not anticipate it:** Atmospheric landing assumes session-level reception. This innovation shows atmospheric density can chain-react within a party: one PC's moment reaches another PC's interior without mechanics.
**Scope:** Universal for parties with specific named-grief paragraphs.
**Status:** logged (see post-S01 threshold note for adopted-to-v1.1 entries)

---

## Threshold Check — Post-S01

### Dimension trigger (2+ logged in a dimension)

Scanning...

| Dimension | Innovations logged | Trigger? |
|---|---|---|
| Character agency | I-S01-01, 04, 05, 06, 12 | ✓ (5 — strong) |
| Atmospheric landing | I-S01-02, 07, 09, 10, 12 | ✓ (5 — strong) |
| Mechanical fairness | I-S01-06, 08, 09 | ✓ (3) |
| Module fidelity | I-S01-03, 08, 09 | ✓ (3) |
| Surprise | I-S01-01, 05, 07, 11, 12 | ✓ (5) |

Multiple dimensions exceed the 2+ threshold. Drafting amendment proposals for the two with the most actionable patterns:

### AMENDMENT PROPOSAL A — Mechanical fairness (v1.0 → v1.1) **[ADOPTED 2026-04-18]**

**Constituent innovations:** I-S01-08, I-S01-09.

**Theme:** Mechanical fairness should include cross-dimensional harmlessness — a mechanic should not actively destroy payoffs in another dimension as its primary effect.

**Proposed rubric anchor addition (at the 7-9 band):**
> A score of 7+ requires that no session mechanic regularly destroys atmospheric-landing, module-fidelity, or character-agency payoffs as a side-effect of its designed behavior. A mechanic that costs resources cleanly (HP, slots, hit dice, time) is fine; a mechanic that inflicts check-disadvantage on atmospheric-gate rolls is cross-dimensionally damaging and caps the score at 6.

**Impact on future scoring:** Sessions using the unmodified Cold Pulse outcome 3 would cap at 6/10 on Mechanical fairness. Redesigned Cold Pulse (cost HP or slot instead of check-disadvantage) would be unaffected.

**Prompt:** *"Mechanical fairness has 3 innovations clustered. Proposed amendment v1.1: add a cross-dimensional-harmlessness anchor. Adopt?"*

### AMENDMENT PROPOSAL B — Atmospheric landing (v1.0 → v1.1) **[ADOPTED 2026-04-18]**

**Constituent innovations:** I-S01-02, I-S01-10, I-S01-12.

**Theme:** Atmospheric landing should include per-PC reception tracking — which PCs received the design-intended flags, and which PCs chain-reacted to each other's reception.

**Proposed rubric anchor addition (at the 9-10 band):**
> A score of 9+ requires documenting *which PCs received each atmospheric flag* in the session log. A score of 10 additionally requires at least one inter-PC grief-chain or atmospheric-chain (one PC's reception triggers another PC's interior response without dice).

**Impact on future scoring:** Session logs will record per-flag, per-PC reception. Chained atmospheric moments become explicitly scorable.

**Prompt:** *"Atmospheric landing has 5 innovations clustered. Proposed amendment v1.1: add per-PC reception and chain-reaction anchors. Adopt?"*

### Cluster trigger (3+ across ≥ 2 sessions)

**Not yet triggered.** All S01 innovations are within a single session. Clustering across sessions requires S02+. No player-style proposals this pass.

---

## Adoption Record — 2026-04-18 (both proposals ratified)

**I-S01-08 status:** `adopted (v1.1)` — contributed to Mechanical fairness cross-dimensional-harmlessness anchor.
**I-S01-09 status:** `adopted (v1.1)` — contributed to Mechanical fairness cross-dimensional-harmlessness anchor.
**I-S01-02 status:** `adopted (v1.1)` — contributed to Atmospheric landing per-PC reception anchor.
**I-S01-10 status:** `adopted (v1.1)` — contributed to Atmospheric landing per-PC reception anchor.
**I-S01-12 status:** `adopted (v1.1)` — contributed to Atmospheric landing chain-reaction anchor.

Remaining S01 innovations stay at `logged`:
- **I-S01-01** (Pre-adventure hook inverts session), **I-S01-04** (Local-origin setting-knowledge), **I-S01-05** (Private-arc parallel), **I-S01-06** (Unspoken resource-sharing), **I-S01-07** (Craft-metaphor theology), **I-S01-11** (PC theological reading) — Character agency / Surprise patterns awaiting S02+ clustering.
- **I-S01-03** (Exhausted opening rolls miss foreshadowing) — Module fidelity pattern; adventure-specific so far; watch for recurrence.

## S02 — 2026-04-19 — varduin-muster — 0002-the-bone-collector-trap

### I-S02-01 — Chain-reception: finder and receiver diverge

**Dimension:** Atmospheric landing (cross: Character agency)
**What happened:** Module's per-PC reception table predicted Thera would receive the Mensa-bread-scrap beat (mother-grief thread). Kessa rolled Investigation 22 and found it; Grom's silence after the reading was the session's emotional impact. Finder (Kessa) and receiver (Grom) diverged.
**Why the rubric did not anticipate it:** Rubric v1.1 per-PC reception anchor treats "who receives the beat" as a single slot per symptom. This innovation shows finder and receiver are separable roles, sometimes held by different PCs.
**Scope:** Universal.
**Status:** logged

### I-S02-02 — Signature-reflex moves can fumble on single dice, invisibling shortcuts

**Dimension:** Module fidelity (cross: Character agency)
**What happened:** Thera's Playstyle Heuristics list "checks pockets, rafters, floor-gaps reflexively" as a signature move. Module's stealth shortcut in Scene 4 was gated behind Investigation DC 13 on the straw pile — the exact reflexive move. Thera rolled natural 1 (total 4). Shortcut invisible. Party took frontal path.
**Why the rubric did not anticipate it:** Module fidelity assumes signature moves deliver reliably. They don't — dice are dice.
**Scope:** Universal.
**Status:** logged

### I-S02-03 — Named-NPC reveals can be lost to adjacent Investigation fumbles

**Dimension:** Module fidelity (cross: Lore grounding)
**What happened:** Mensa's notebook at the waystation held Reya's name (Pella's mother — the module's most carefully-placed reveal in Scene 1). Investigation DC 13 to find. Thera rolled 4, fumbled. The party left the waystation without Reya's name. Pella cannot be told her mother's name unless the party revisits the waystation.
**Why the rubric did not anticipate it:** Module fidelity does not account for "leave the named-NPC reveal behind for a later session." Reveals are treated as either landed-this-session or missed-permanently. Actually they can be *deferred* via geographic persistence — the notebook stays on the dresser.
**Scope:** Adventure-specific (this waystation); universal principle (geographically-persistent reveals can be deferred).
**Status:** logged

### I-S02-04 — Craft-ritual PCs read rooms as histories

**Dimension:** Atmospheric landing (cross: Character agency)
**What happened:** Grom read all three cells in the Cell-Block in sequence — the chalk-figure woman (Inv 13, pass DC 12), the 63 tally-marks (Inv 10, pass DC 10), the old blood floor-stain (Inv 14, pass DC 13). He then said aloud: *"They've held people here for years. Not raiders — people."* This is the same craft-reception pattern as S01's voice-fragment-to-Grom (I-S01-02) and forge-metaphor-theology (I-S01-07).
**Why the rubric did not anticipate it:** Grom's craft-ritual worldview produces room-reading as a form of atmospheric reception. The rubric treats Atmospheric landing as session-level; Grom delivers it as **archaeological-atmospheric**. 4 Grom-specific instances across 2 sessions now.
**Scope:** Universal for craft-ritual PCs; specifically patterned around Grom.
**Status:** logged — candidate for cluster promotion to player-style.

### I-S02-05 — Setting-trained PCs read intel-documents as dual grief-and-data

**Dimension:** Character agency (cross: Engagement)
**What happened:** Aelric read the duty-roster in Scene 5 — seeing Vesk's name crossed out — as Solamnic intelligence AND as grief simultaneously. He registered the crossing-out silently; he did not remark, but Grom noticed Aelric notice. The duty-roster as character-moment was not scripted.
**Why the rubric did not anticipate it:** Aelric's Solamnic-officer training + his own grief-paragraph (Varran) combined to produce a dual-read. Rubric Character agency doesn't anticipate this compounding.
**Scope:** Universal for PCs with institutional-role + personal-grief backgrounds.
**Status:** logged

### I-S02-06 — Anchor-level atmospheric symptoms can miss on single-gate rolls

**Dimension:** Module fidelity (cross: Atmospheric landing)
**What happened:** The cross-adventure signal — uncredited *"I will not look at the rose again"* on Keloth's wall-ledger — is the workshop's most ambitious design element. Gated behind Kessa Investigation DC 13 + Kessa Perception DC 13 on ledger-brighten. She rolled 12 and 11. Both failed by 1. The signal was in the room and did not fire.
**Why the rubric did not anticipate it:** Module fidelity anchors measure percentage-landed at session level. They do not protect anchor-level symptoms (cross-adventure signals; named-NPC reveals; reaction moments) from single-gate dice failure.
**Scope:** Universal.
**Status:** logged — **primary candidate for rubric v1.1 → v1.2 amendment**. Proposed anchor addition: *"For manifest symptoms tagged anchor-level, a passive-Perception fallback at DC = active-check + 2 MUST be documented. A party with passive 15+ auto-lands what active-13 gated."*

### I-S02-07 — Child-NPC interior-certainty commitment produces session-memory-worthy image

**Dimension:** Atmospheric landing (cross: Surprise)
**What happened:** Rev 2 of #0002 committed: "Pella MUST be played with interior-certainty, not hope." At the Scene 6 climax, after the fight, Pella walked silent to Aelric and said: *"You came."* Two words, small hand on pauldron. Session-memory-worthy.
**Why the rubric did not anticipate it:** The module's rev-2 commitment worked exactly as designed. This is *not* a rubric gap — this is evidence that rev-2-level module commitments (DM MUST narrate X as Y) deliver the atmospheric beats the rubric asks for. **Log as positive-confirmation.**
**Scope:** Universal pattern for child-NPCs or vulnerable-NPCs where interior-state shapes the scene.
**Status:** logged — **evidence of successful rev-2 design pattern; worth codifying**.

### I-S02-08 — Character-interior realizations can land silently

**Dimension:** Atmospheric landing (cross: Character agency)
**What happened:** Scene 8's Sir Venric pyre — Aelric stood at attention for three verses. The module's GM Note said: *"Aelric may quietly realize Varran had no pyre; let the player feel it."* The DM-as-Aelric felt the realization without narrating or rolling. No dice; no DM description; pure character-weight via the module's instruction to *not* narrate.
**Why the rubric did not anticipate it:** Rubric Atmospheric landing assumes reception is observable — via dice, description, or chain-reaction. This innovation shows reception can be *fully interior* and still count.
**Scope:** Universal.
**Status:** logged

### I-S02-09 — Trade-completed-but-cell-hostile is a legitimate module gap

**Dimension:** Table readiness (cross: Module fidelity)
**What happened:** Module's Option A presumes trade = clean departure. In play, Keloth's lieutenant Idra moved on Pella during attunement; combat opened; Keloth declared the trade completed but his cell's self-defense restored. DM adjudicated fairly but ad-hoc — module did not cover this branch.
**Why the rubric did not anticipate it:** Table readiness assumes module coverage of predictable branches. This branch was plausible and uncovered.
**Scope:** Adventure-specific for #0002; universal pattern for trade-with-cell-based antagonist modules.
**Status:** logged — candidate for module rev 3 (sub-branch addition) rather than rubric amendment.

### I-S02-10 — Portent mis-draw is lossy; design acknowledges but does not compensate

**Dimension:** Mechanical fairness
**What happened:** Kessa rolled Portent 3 and 3 at session start. Neither was low enough to force enemy misses in practice (Bandit +3 attack needs 12+ vs AC 12 — a 3 misses but no Bandit rolled less than 9). Neither could substitute Kessa's own rolls usefully. Both Portents went unused.
**Why the rubric did not anticipate it:** Mechanical fairness anchors assume mechanical resources pay off when used. Portent is a resource with lossy payoff depending on draw.
**Scope:** Universal for Divination wizards.
**Status:** logged — flag as mechanical-truth-of-the-class, not a design fix.

---

## Threshold Check — Post-S02

### Dimension trigger (2+ logged in a dimension, status `logged`)

Scanning across S01 + S02 (innovations still at `logged` status; already-adopted entries excluded):

| Dimension | Logged innovations | Trigger? |
|---|---|---|
| Module fidelity | I-S01-03, I-S02-02, I-S02-03, I-S02-06, I-S02-09 | ✓ (5) |
| Atmospheric landing | I-S02-01, I-S02-04, I-S02-07, I-S02-08 | ✓ (4) |
| Character agency | I-S01-01, I-S01-04, I-S01-05, I-S01-06, I-S01-12, I-S02-05 | ✓ (6) |
| Surprise | I-S01-01, I-S01-05, I-S01-07, I-S01-11, I-S01-12 | ✓ (5) |
| Table readiness | I-S02-09 | — (1 only) |
| Mechanical fairness | I-S02-10 | — (1 only) |

Multiple dimensions exceed the 2+ threshold. Two amendment proposals drafted:

### AMENDMENT PROPOSAL C — Module fidelity anchor-level passive-Perception fallback (v1.1 → v1.2)

**Constituent innovations:** I-S01-03, I-S02-02, I-S02-03, I-S02-06. (I-S02-09 is closer to a per-module sub-branch than a rubric amendment; marked separately.)

**Theme:** Manifest symptoms tagged as *anchor-level* (cross-adventure signals, named-NPC reveals, reaction moments, foreshadowing clues that gate future-adventure hooks) should not be lost to a single failed active-ability-check. Passive-Perception fallback required.

**Proposed rubric anchor addition (at the 9-10 band of Module fidelity):**
> A score of 9+ requires that *anchor-level* manifest symptoms (as defined by the adventure's manifest file) have documented passive-Perception fallback at DC = active-check + 2. A score of 10 additionally requires *recovery-path* documentation: how a party that missed an anchor-level symptom in play could still encounter it post-session (e.g., geographically persistent reveals, future-session prompts).

**Impact on future scoring:** Adventures without passive-Perception fallbacks on anchor-level symptoms cap at 8/10 on Module fidelity. Adventures with both fallback AND recovery-path can hit 10.

**Prompt:** *"Module fidelity has 4 logged innovations clustered on single-gate anchor-level misses. Proposed amendment v1.2: add passive-Perception-fallback and recovery-path anchors. Adopt?"*

### AMENDMENT PROPOSAL D — Atmospheric landing per-PC *finder vs. receiver* separation (v1.1 → v1.2)

**Constituent innovations:** I-S02-01, I-S02-07, I-S02-08.

**Theme:** Per-PC reception involves two separable roles — the PC who *finds* or *rolls against* a beat, and the PC who *receives* its emotional weight. Sometimes these are the same PC; sometimes they diverge. The rubric should track both. Additionally: silent reception (no dice, no narration) should count.

**Proposed rubric anchor addition (at the 7-9 band of Atmospheric landing):**
> A score of 7+ requires tracking **finder** and **receiver** separately in the per-PC reception table. Silent reception (character-interior realization without dice or narration, per module's explicit instruction) counts as reception.

**Impact on future scoring:** Session logs will use two-column per-PC tracking. Reveals the chain-reception pattern that S01 and S02 both surfaced.

**Prompt:** *"Atmospheric landing has 3 logged innovations on finder/receiver separation and silent reception. Proposed amendment v1.2: two-column per-PC tracking + silent reception recognition. Adopt?"*

### Cluster trigger (3+ innovations clustered by theme, across ≥ 2 sessions)

Scanning all `logged` innovations for thematic clusters across S01 and S02:

#### **CLUSTER A — PC-sheet-hidden content drives session-level agency**

**Constituent innovations:** I-S01-01 (Kessa pre-recognition), I-S01-04 (Thera Solamnic-house expertise), I-S01-05 (Kessa private investigation), I-S02-05 (Aelric dual-read duty-roster).

**Sessions:** S01 (3) + S02 (1) = 4 instances across 2 sessions.

**Theme:** PC backgrounds (origin, training, prior-adventure hooks) produce session-level agency *before* any in-session action. The agency is in the sheet. The module reveals what the sheet already contained.

**Proposed player-style slug:** `sheet-deep-reader`

**Proposed definition:** A PC (or DM-playing-PC under Option A) who reads their own character sheet as a live source of agency throughout session-play — surfacing backgrounds, prior-adventure hooks, and institutional training as current-scene decision inputs, without being prompted by the DM.

**Triggers/signals:** PC makes an in-fiction recognition from sheet-content that the DM did not prompt. PC's agency is *carried* by the sheet rather than *called up* by the module.

**Cross-applicability:** Amplified by parties with detailed PC sheets (grief paragraphs, local-origin notes, prior-adventure hooks). Undermined by parties with thin sheets (generic backgrounds).

**Status:** PROPOSED — first promotion candidate.

**Prompt:** *"Cluster A: 4 innovations across S01 (3) + S02 (1) share the 'PC-sheet-hidden content drives agency' theme. Propose player-style `sheet-deep-reader`. Approve?"*

#### **CLUSTER B — Craft-ritual PCs deliver non-standard atmospheric reception (Grom-pattern)**

**Constituent innovations:** I-S01-02 (Grom voice-fragment), I-S01-07 (Grom forge-theology), I-S02-01 (Grom bread-scrap receiver), I-S02-04 (Grom cell-block layers).

**Sessions:** S01 (2) + S02 (2) = 4 instances across 2 sessions.

**Theme:** Grom's hearth-greeting craft-ritual (thumb on inside-curve; "thou'rt seen") produces atmospheric reception that other PCs miss. Not a specific-caster-class effect (Grom is a cleric but the pattern isn't cleric-standard); it is a *craft-ritual* effect.

**Proposed player-style slug:** `craft-witness`

**Proposed definition:** A PC whose character sheet specifies a daily craft-ritual or attention-practice (forge-priest's inside-curve greeting; silversmith's hand-in-water; scholar's pen-blessing) and who, by virtue of that practice, receives atmospheric flags other PCs miss. The craft-practice becomes a reception-antenna.

**Triggers/signals:** PC's craft-ritual move is performed off-camera; in-scene the PC catches an atmospheric beat that the wisdom-casters missed; the PC's receptiveness is traceable to their ritual, not their wisdom score.

**Cross-applicability:** Amplifies any PC with a specified ritual-practice. Would not fire for a PC with generic "devoted to X" background (needs specific ritual).

**Status:** PROPOSED — second promotion candidate.

**Prompt:** *"Cluster B: 4 innovations across S01 (2) + S02 (2) share the 'craft-ritual receives atmosphere' theme, all tied to Grom specifically. Propose player-style `craft-witness`. Approve?"*

#### Cluster C — Anchor-level atmospheric beats miss on single-gate rolls (covered by Amendment Proposal C)

Five instances across both sessions. Already addressed by the proposed v1.1 → v1.2 amendment above; not additionally promoted as a player-style (it is a module-design pattern, not a player archetype).

---

## S03 Innovations — *The Silversmith's Mirror* (2026-04-19)

### I-S03-01 — Positional-failure anchor for passive-Perception fallback

**Dimension:** Module Fidelity
**Scene:** 6 (Lower Chamber; filigree-dim symptom)
**What happened:** Module's filigree-dim anchor symptom (shop signage dims "upstairs" when the Mirror's cloth is lifted) had a v1.2-compliant passive-Perception DC 14 fallback documented. Nobody was positioned upstairs at the trigger moment (all PCs in chamber; Harel + Mira in hearth; Harel passive 10 < 14). Fallback could not fire because no witness existed in-position.
**Why it matters:** v1.2's anchor-level passive-fallback anchor solves the "one-point-miss on a gated roll" problem. It does NOT solve the "nobody-to-roll" problem. Positional failures are a distinct failure mode — the check infrastructure is in place, but the geometry prevents the roll.
**Status:** LOGGED. Feeds cluster for potential v1.3 amendment (positional-redundancy anchor).

### I-S03-02 — Finder-vs-receiver PARTIAL reception (cross-scene deferred pattern)

**Dimension:** Atmospheric Landing
**Scene:** 4 (Mira's Hearth; cross-adventure phrase recovery)
**What happened:** Kessa rolled Investigation 16 on Mira's ledger and caught the cross-adventure phrase *"I will not look at the rose again"* (S02 recovery path fulfilled). Then rolled Investigation 9 to cross-reference her own S02 notebook — failed. She has the phrase on the page; she does not yet have the pattern-match to her own S02 transcription. **Finder-column filled; receiver-column filled only partially.** The phrase landed; the pattern-link is deferred to post-session reflection or next-session re-reading.
**Why it matters:** v1.2's finder-vs-receiver two-column tracking assumes both columns resolve within-scene. Cross-scene or deferred reception (finder-becomes-receiver-later via reflection) is a new sub-type. S03 produced the first canonical partial-reception outcome under v1.2.
**Status:** LOGGED. Cluster candidate with I-S01-02 (Grom voice-fragment deferred-receive pattern).

### I-S03-03 — Portent-as-benediction (PC-to-PC Divination ritual-rescue)

**Dimension:** Mechanical Fairness / Character Agency / Surprise (fuses three)
**Scene:** 7 (Reorx-rite at the forge)
**What happened:** Grom rolled Religion 8, failing the Reorx-shattering rite DC 15. Kessa expended her held Portent [14] to replace Grom's d20, framed in-character: *"Vethrenn. I have never met you. If this was part of what you wanted me to see — let it be through me."* Rite succeeded at 17. **The mechanical Divination School move landed as a PC-to-PC benediction.**
**Why it matters:** Mechanical Fairness at 9+ requires mechanics that "compound narratively." The current anchor is single-character framed. Cross-character mechanical benedictions are a new type — one PC's spell-feature saving another PC's ritual, framed in-voice as act-of-attention. RAW-compliant; narratively distinct.
**Status:** LOGGED. Cluster candidate for potential Mechanical Fairness v1.3 amendment (cross-character compound).

### I-S03-04 — No-attunement collective restraint (Option C declined by all PCs)

**Dimension:** Character Agency / Module Fidelity
**Scene:** 6 (Mirror uncovered; attunement offered)
**What happened:** All four PCs' doubt-dice rolled against looking — Kessa d6=1 (catalog not touch); Thera d6=1 (profit not story); Grom d6=2 (mend-as-honor → destroy); Aelric d6=2 (letter of Measure → personal grief not Council business). The module's most-designed decision beat (Option C subagent spawn for attunement) did not fire. The P0-revision Blank-Mirror read-aloud did not fire. The campaign-continuity attunement trigger did not fire.
**Why it matters:** Module Fidelity measures whether designed beats land. The Option-C-spawn is a designed beat. But "designed beat declined by PCs acting in character" is not a fidelity failure — it is the highest form of character agency. The rubric has no vocabulary for this duality. Proposed resolution: a designed beat can *legitimately* fail because PCs chose it to; the rubric should score this as fidelity-high AND agency-high, not fidelity-penalty.
**Status:** LOGGED. Part of the module-design-weight question flagged by Roleplayer and Improviser lenses.

### I-S03-05 — Unscripted NPC narrative completion (Mira's ink-writing)

**Dimension:** Atmospheric Landing
**Scene:** 7 (Aftermath; post-rite)
**What happened:** Module did not script this. Post-rite, Mira asked Thera for a corner of her notebook, tore a piece, wrote *"For the Council file. A daughter's note. My mother's name was Seralen. I am grateful. — M. Vaenshold."* First time in 30 years Seralen's name has been written in ink by Mira's hand. Scene 4's spoken disclosure → Scene 7's written affirmation — **NPC-internal arc completion**, DM-improvised within the character's logic.
**Why it matters:** Atmospheric Landing's 10 band requires an inter-PC chain. This is an *NPC*-completion chain: Grom's silent benediction Scene 4 → Mira's spoken name Scene 4 → Mira's written name Scene 7. The rubric's chain-concept is PC-centric. NPC-arc-completion chains that close session-long arcs are a new sub-type.
**Status:** LOGGED.

### I-S03-06 — Kessa heuristic crossover (sheet-deep-reader → craft-witness under blank-risk)

**Dimension:** Character Agency / Surprise
**Scene:** 6 (Mirror decision)
**What happened:** Kessa's PC sheet heuristic-priority-1 is "Understand it." Her d6 rolled 1 (catalog, don't touch). Her in-character reasoning framed the decision as craft-witness would: honor the object's refusal by not forcing it. *"I will not risk a blank."* She then used her silver-ink pen signature move to write the observation — recording without touching. **Kessa exhibited both `sheet-deep-reader` and `craft-witness` patterns simultaneously.**
**Why it matters:** The two pending player-styles (from S01+S02 cluster triggers) are tracked as separate clusters. A PC exhibiting BOTH patterns under pressure is a cross-style emergent behavior. Possible sub-style: *doctrinal-silence* — PC acts against their own primary heuristic in a way their *secondary* heuristic justifies, under existential artifact risk. First instance logged.
**Status:** LOGGED. Cluster candidate for cross-style hybrid; wait for second instance before promoting sub-style.

### I-S03-07 — Declined-path design-weight imbalance (module-template pattern)

**Dimension:** Module Fidelity (template-level)
**Scene:** 6 → 7 (attunement declined, destruction chosen)
**What happened:** Module #0003 invested heavily in the Mirror-attunement path — Option C subagent prompt (full prompt with per-PC branches), Blank-Mirror read-aloud (P0 revision), campaign-continuity trigger for permanent self-image replacement. The destruction-path had a single Religion DC 15 check with no scripted narration. When party declined attunement and chose destruction, the DM had to improvise the destruction-rite's narration (obsidian shattering along Aelwen's unconverged polish-lines). Improvisation worked, but the module's design-weight was unbalanced.
**Why it matters:** Module-template question: when a major decision is offered, design-weight should be roughly parity between paths. As-written, the attunement-path has ~1,000 words of scripted material; the destruction-path has ~50. Future modules with major artifact decisions should pre-write both paths. This is a `dungeon-smith` + `treasure-forger` template refinement, not a rubric amendment.
**Status:** LOGGED. Module-template refinement candidate.

---

### Dimension-trigger check (post-S03)

- **Module Fidelity:** I-S03-01, I-S03-04, I-S03-07. **3 new instances this session**, all topically distinct from v1.2's single-gate cluster. **PROPOSE Amendment Proposal E for v1.3.**
- **Mechanical Fairness:** I-S03-03 — 1 instance. Wait for second.
- **Atmospheric Landing:** I-S03-02, I-S03-05 — 2 new instances. Watch for third; likely v1.3 candidate by S04.
- **Character Agency:** I-S03-04 + I-S03-06 — 2 new instances in a dimension never previously amended. First-time cluster.
- **Surprise:** I-S03-03/04/05/06 — 4 new instances in one session. Worth reviewing dimension-definition refinement.

### **Amendment Proposal E (v1.2 → v1.3 candidate): Module Fidelity — positional-redundancy anchor**

**Theme:** Anchor-level symptoms with documented passive-Perception fallbacks can still fail if nobody is *positioned* to roll.

**Proposed rubric anchor addition (at the 9+ band of Module Fidelity):**
> A score of 9+ requires anchor-level symptoms have at least TWO of the following three fallback mechanisms: (a) active-check + passive-Perception fallback at DC = active+2 (v1.2 current); (b) redundant placement in at least two locations or two scenes, such that the symptom can be perceived from multiple positions; (c) NPC-delivered recall — an NPC (named, present, with reason to mention) can re-surface the symptom in a later scene. Adventures that rely on a single location for a positional symptom cap at 8.

**Impact on future scoring:** Modules with single-location-only anchor symptoms will score 8/10 module-fidelity ceiling. Modules investing in positional-redundancy will unlock 9+.

**Prompt:** *"Module Fidelity has 3 new innovations in S03 (positional-failure, declined-path, design-weight). Amendment Proposal E (v1.3): positional-redundancy + NPC-delivered-recall as third fallback. Adopt?"*

### **Player-style promotion check (post-S03)**

- `sheet-deep-reader` (proposed S01+S02): I-S03-06 reinforces. **5 total instances across 3 sessions.** Ready for adoption.
- `craft-witness` (proposed S01+S02): Grom's Scene 1 hearth-greeting, Scene 4 silent benediction, Scene 6 craft-witness reading. **7 total instances across 3 sessions.** Strongly ready for adoption.
- **New cluster candidate:** *doctrinal-silence* — PC acts against primary heuristic under existential artifact risk (Kessa S03 Scene 6 catalog-over-understand). 1 instance. Watch for S04+ repeat.

### **Cluster retire-check:** Cluster C (anchor-level single-gate misses) — addressed by v1.2. No new S03 instances. Cluster CLOSED.

---

## S04 Innovations — *The Wrath-Coin* (2026-04-19)

### I-S04-01 — Portent-as-benediction (2nd instance; cluster trigger)

**Dimension:** Mechanical Fairness / Character Agency / Surprise (fuses three)
**Scene:** 3 (Reorx-rite)
**What happened:** Kessa expended her held Portent die [10] to replace Grom's Religion d20 roll on the Reorx-rite DC 15. Framed in-voice: *"Vethrenn. Help him. You wrote: 'release is possible.' Let this be a releasing."* Kessa spoke Qualinesti aloud (first time in 3 sessions). Grom's total with Bless die = exactly 15 DC. Rite succeeded. **This is the 2nd instance of Portent-as-benediction** (first: I-S03-03 at S03 Scene 7 Mirror-destruction).
**Why it matters:** Cluster trigger fires at 2 instances / 2 sessions. Portent-as-PC-to-PC-benediction is a repeatable Kessa-pattern that integrates mechanical (Divination School feature) with narrative (spoken-prayer to never-met mentor) with craft-ritual (PC-to-PC cross-character compound). Ready for formal innovation-amendment or sub-style promotion.
**Status:** LOGGED. **Cluster candidate: promote to sub-style "divination-as-benediction" OR integrate as sheet-deep-reader extension.** Decision point for next handoff.

### I-S04-02 — Campaign-scale silent-reception chain (3 scenes)

**Dimension:** Atmospheric Landing / Module Fidelity
**Scene:** 3 → 5 → 6 (three scenes)
**What happened:** Grom received Hint 3 (Reorx's Judgment: *"grief-coiled, not forged-with-intent; a coil can be uncoiled"*) at Scene 3's rite — his articulation self-check failed (Religion 8 vs DC 10). Silent reception persisted. At Scene 5, Grom articulated the related hearth-greeting realization aloud (silent-to-spoken transition). At Scene 6, Grom invoked the Reorx-exile ritual — which required Hint-3 RECEPTION, not ARTICULATION — based on his continued silent understanding. **Campaign-permanent decision driven by 3-scene silent-reception chain.**
**Why it matters:** Rubric v1.2 silent-reception anchor was written for within-scene silent-receptions. Campaign-scale silent-reception-chains are a new sub-type where sustained non-articulated PC-knowledge drives downstream action across multiple scenes. Proposed v1.4 amendment.
**Status:** LOGGED. v1.4 amendment candidate.

### I-S04-03 — Option-A-sufficient-where-Option-C-expected

**Dimension:** Character Agency
**Scene:** 6 (Grom's Krun-fate decision)
**What happened:** Module flagged Grom's Krun-fate as "strongly recommended Option C." In play, Grom's doubt-die (stand-between) + Hint-3-silent-reception + heuristic-order produced a character-consistent Reorx-exile invocation WITHOUT agent-spawn. Solo DM Option-A play was sufficient.
**Why it matters:** The ratified player-styles (sheet-deep-reader + craft-witness) may be enabling Option-A-sufficiency where Option C was previously required. This is a design-signal: Option C can be downgraded from "strongly recommended" to "available" for PCs whose ratified styles deliver voice-distinction natively.
**Status:** LOGGED. Process-design implication: update session-runner guidance for Option C triggering.

### I-S04-04 — Dice-driven module-preferred outcomes (complementary to S03 Kann-kill)

**Dimension:** Mechanical Fairness
**Scene:** 1 (Jarek capture via overkill)
**What happened:** Module's GM notes said *"Jarek's flee is narratively preferred; the campaign wants him to live."* Scene 1 combat: Grom's Guiding Bolt dealt 24 damage against Jarek's 12 remaining HP. Overshoot: −12 (not ≤−30 instakill threshold). Jarek dropped unconscious; Thera stabilized him with healer's kit. **The module-preferred outcome (Jarek alive as witness) happened via dice damage-overshoot, not GM-fiat.**
**Why it matters:** S03 had the opposite case — Kessa killed Kann despite module-preferring escape. S04 delivered the preferred outcome via dice. Both are legitimate. Pattern: **campaign-continuity is dice-robust** when module-preferred outcomes have *mechanical paths to happen* (stabilization rules; CR-appropriate HP thresholds). Design principle: *"Module-preferred outcomes are guidance. Dice + character heuristics are authoritative. Campaign adapts."*
**Status:** LOGGED. Process-design principle for future adventure template.

### I-S04-05 — FUMBLE-transmutation via Voice-tag reading (Aelric init 1)

**Dimension:** Atmospheric Landing / Surprise
**Scene:** 6 (initiative)
**What happened:** Aelric rolled nat-1 on initiative at Scene 6. The DM did not narrate stumbling-loses-turn. The DM read Aelric's Voice tags from his PC sheet (*"Formal register always. Est Sularus oth Mithas. Titles."*) and narrated the fumble as a Solamnic kneeling-before-kinswoman-law gesture. *"Aelric stumbles at the threshold — a stumble that becomes a kneel."* Krun saw the gesture; Krun's political authority cracked. **The mechanical fail delivered narratively heavier than a clean roll would have.**
**Why it matters:** This is improvised PC-style-consistent outcome-authoring — the DM read the sheet and transmuted the result. Related to craft-witness + sheet-deep-reader active delivery. Possible rubric v1.4 anchor: "Character Agency 10+ requires DM to author style-consistent outcomes for ratified player-styles without module-pre-authorization."
**Status:** LOGGED. v1.4 amendment candidate (cross-cluster with I-S03-06 heuristic-crossover).

---

### Dimension-trigger check (post-S04)

- **Mechanical Fairness:** I-S04-01 (Portent-as-benediction 2nd), I-S04-04 (dice-driven preferred outcomes). **2 new instances.** Combined with historic: **cluster trigger fires.** Amendment candidate v1.4.
- **Atmospheric Landing:** I-S04-02 (silent-reception chain), I-S04-05 (fumble-transmutation). **2 new instances.** v1.4 amendment candidate.
- **Character Agency:** I-S04-02, I-S04-03, I-S04-05. **3 new instances.** Dimension's second cluster (first was S03's I-S03-04/06). Strong v1.4 candidate.
- **Surprise:** I-S04-01/02/03/04/05. **5 new instances in one session.** Second session (after S03) with high surprise-count; consider dimension refinement.

### **Amendment Proposal F (v1.3 → v1.4 candidate): Mechanical Fairness — PC-to-PC cross-character compound**

**Theme:** Mechanical Fairness 10+ anchor currently: *"Dice produced emergent story the DM could not have predicted AND mechanics compounded narratively (e.g., exhaustion shaped a later decision)."* This is single-character framed. Cross-character mechanical compound (Portent on another PC's ritual; Bless-stacking; etc.) is a new sub-type.

**Proposed rubric anchor addition (at the 10 band of Mechanical Fairness):**
> A score of 10 additionally requires at least one **cross-character mechanical compound** — a PC's class/spell/feature mechanic applied to another PC's roll, framed in-voice as character-action, producing narratively-emergent outcome. Examples: Portent-as-benediction (Divination School); Bless-stacking on ritual DCs; Counterspell-as-protection.

**Impact:** Mechanical Fairness 10 becomes rarer; requires cross-character play rather than within-character compounding. Raises the bar.

**Prompt:** *"Mechanical Fairness has 2 instances of cross-character compound (Portent-as-benediction × 2). Amendment Proposal F (v1.4): add cross-character-compound requirement to the 10 band. Adopt?"*

### **Amendment Proposal G (v1.3 → v1.4 candidate): Atmospheric Landing — silent-reception chain**

**Theme:** Current v1.2 silent-reception anchor: *"Silent reception (character-interior realization without dice or narration) counts as reception."* Within-scene framing. S04 demonstrated campaign-scale silent-reception chain (3 scenes; Hint-3 → hearth-greeting → Reorx-exile).

**Proposed rubric anchor addition (at the 9-10 band of Atmospheric Landing):**
> A score of 9+ additionally recognizes **multi-scene silent-reception chains** where a PC holds an un-articulated understanding across scenes and acts on it in a later scene. The non-articulated understanding counts as campaign-permanent reception upon first-scene receipt AND drives action in subsequent scenes. A score of 10 requires at least one such chain.

**Impact:** Campaign-scale silent-reception becomes formal dimension metric. Validates ratified player-styles (craft-witness silent-reception at scale).

**Prompt:** *"Atmospheric Landing has silent-reception-chain evidence (I-S04-02 three-scene Hint-3 chain). Amendment Proposal G (v1.4): recognize multi-scene silent-reception chains. Adopt?"*

### **Player-style promotion / cluster check (post-S04)**

- `sheet-deep-reader`: S01 (3) + S02 (1) + S03 (1) + S04 (2) = **7 total instances across 4 sessions.** Already ratified; continues to fire.
- `craft-witness`: S01 (2) + S02 (2) + S03 (3) + S04 (3) = **10 total instances across 4 sessions.** Already ratified; continues to fire.
- **`divination-as-benediction` (Kessa Portent-pattern)**: S03 (1) + S04 (1) = 2 instances across 2 sessions. **Cluster trigger.** Promote to sub-style OR integrate with sheet-deep-reader. Decision: **integrate as sheet-deep-reader sub-type** (Kessa's Portent-use is sheet-driven Divination School application; the innovation is the "for-another-PC" direction). Add to sheet-deep-reader sub-type watch as *"Portent-as-benediction"*.
- **`doctrinal-silence` candidate** (S03 Kessa cross-heuristic): no S04 reinforcement. 1 instance. **Retire.** S05 did not produce a doctrinal-silence beat; Aelric's Oath-decision is decision-order-consistent (Oath beats Self), not heuristic-override. Cluster inactive.
- **`fumble-transmutation`** (I-S04-05): 1 instance. Watch for S05. **S05: no fumbles.** Still 1 instance.
- **`hint-synthesis-in-voice`** (NEW S05): Kessa articulated the Hint 4 synthesis aloud in-session (I-S05-01). This is a new pattern: PC synthesizes multi-adventure hints into a named theory before the finale. Watch for #0006+ repeat.

---

## S05 Innovations — *The Pride-Circlet* (2026-04-19)

### I-S05-01 — Hint 4 synthesis articulated in-voice by a PC (first in campaign)

**Dimension:** Atmospheric Landing / Surprise
**Scene:** 03 (Wena's Briefing; Tiran's research notes)
**What happened:** Kessa read Tiran's note on the unnamed sixth forging ("shame or self-concealment") then cross-referenced her carried fragments (#0003 journal page: "I should have forged an ingot instead"; #0004 apron-scrap: "empty it, break it"). She articulated aloud: *"I think the sixth is not an object she made. I think it is the object she could not make because she was too ashamed to."* This is Hint 4's intellectual synthesis — five adventures before the auto-delivery at #0007.
**Why it matters:** Hint 4 is designed to auto-deliver via passive-Perception 15 at #0007. It was pre-planted in #0003 (ingot reference). It was reinforced in #0004 (apron-scrap). S05 produced the first in-voice synthesis by a PC — not through the module's designed delivery mechanism but through accumulated cross-session research. The #0007 finale now has a named theory waiting for confirmation. This is "hint-synthesis-in-voice" — a new category where a PC names the finale's key insight before it is formally delivered.
**Status:** LOGGED. New innovation type; watch for #0006 repeat (would confirm as cluster).

### I-S05-02 — Oath-decision replaces Option C (Aelric's Circlet choice)

**Dimension:** Character Agency / Surprise
**Scene:** 06 (The Vault)
**What happened:** Module flagged Scene 06 as "Option C strongly recommended" for Aelric's Pride-Circlet decision. In play, Aelric picked up the Circlet, felt it warm, and set it down in <20 seconds. His decision order: (2) Order's honor = a knight who cannot see failures cannot hold honor; Pride-Circlet destroys self-correction. Option C spawn not needed. The Oath resolved the decision before the grief-paragraph could be adjudicated.
**Why it matters:** Second session in a row (S04: Grom's Reorx-exile; S05: Aelric's Circlet) where the module's "strongly recommended Option C" did not fire because the ratified player-styles (sheet-deep-reader: decision order) delivered voice-distinction natively. Reinforces I-S04-03. **Cluster: Option-A-sufficient-where-Option-C-expected now at 2 instances.** Ready for formal cluster promotion.
**Status:** LOGGED. Cluster trigger with I-S04-03.

### I-S05-03 — Craft-witness produces theology by juxtaposition (Grom vault)

**Dimension:** Atmospheric Landing
**Scene:** 06 (The Vault)
**What happened:** Grom stood near the vault door, felt the Circlet wanting, and touched the vault stone wall instead. Internal observation: *"It is practicing at being worn again. The stone is cold and does not want anything."* Craft-witness produced a theological statement by contrasting two materials — the Circlet's desire vs. forge-stone's indifference. Not spoken aloud; fully silent reception.
**Why it matters:** Craft-witness has previously produced theological observations through language (S01: "This is a starvation"; S04: "A coil can be uncoiled"). S05 is the first instance where craft-witness produces theology through *juxtaposition* rather than direct statement. The forge-priest reads two materials and the comparison does the work. New sub-type within craft-witness: **material-comparison theology.**
**Status:** LOGGED. Craft-witness sub-type candidate.

### I-S05-04 — 100% manifest symptom delivery (first in campaign)

**Dimension:** Module Fidelity
**Scene:** all 7
**What happened:** 13 of 13 designed manifest symptoms landed — every symptom from the v1.3-compliant manifest file. Previous sessions: S01 (most), S02 (most), S03 (8/10 = 80%), S04 (22/23 = 96%). S05 achieved 100% for the first time.
**Why it matters:** 100% delivery is a rubric v1.3 validation point — the positional-redundancy anchor (requiring ≥2 of 3 fallback paths) is working as designed. No symptom was skipped, missed due to positioning failure, or abandoned. Combined with the marathon-runner CLI handling all 7 scenes mechanically, the pipeline is mature.
**Status:** LOGGED. Rubric v1.3 validation confirmed.

### I-S05-05 — Golden path achieved without a combat encounter or dice roll

**Dimension:** Encounter craft / Pacing
**Scene:** 04 (Joint Meeting; golden path pivot)
**What happened:** Wena offered to witness Tiran without the Circlet. Tiran accepted. No dice were rolled in this session (0 total for S05). The golden path outcome was reached entirely through:
- NPC character logic (Wena's training as a novice making the offer she was trained to make)
- PC facilitation (Aelric creating space; Kessa not interrupting; Grom reading Tiran's state)
- The joint-meeting scene structure (two NPCs with incompatible positions in the same room, party as witness)
**Why it matters:** 0-dice sessions are a new experience for the workshop (all prior sessions had 13-30+ dice rolls). This confirms the system can handle purely social/narrative resolution without mechanical weight. Also confirms that the scene-engine can produce compelling play even when Python-resolved beats are minimal.
**Status:** LOGGED.

### I-S05-06 — Wena's reciprocal-witness offer (emergent NPC resolution)

**Dimension:** Atmospheric Landing / Improviser
**Scene:** 04 (Joint Meeting)
**What happened:** The module's Scene 04 scripted dialogue included Wena's offer as a possibility ("if party navigates well"). In play, the offer emerged naturally from the character logic without DM needing to "play" it consciously. Wena said "I can be present when you tell someone who loves you what you are most proud of. That is not the Circlet. That is just talking." This unlocked Tiran's admission and pivoted the session to the golden path.
**Why it matters:** Companion to I-S03-05 (Mira's ink-writing; unscripted NPC completion). S05 produced another unscripted NPC-completion-chain: Wena's offer → Tiran's admission → golden path. Both NPCs spoke the thing the session needed to hear at the moment it was needed, from character logic rather than DM scripting.
**Status:** LOGGED. NPC-arc-completion cluster now at 2 instances (S03 Mira + S05 Wena).

---

### Dimension-trigger check (post-S05)

- **Atmospheric Landing:** I-S05-01, I-S05-03, I-S05-06 — 3 new instances (hint-synthesis, material-comparison, NPC-completion). Strong v1.4 amendment candidate.
- **Module Fidelity:** I-S05-04 — 100% delivery validates v1.3 positional-redundancy. No new amendment needed; confirmation logged.
- **Character Agency:** I-S05-02 — Option-A-sufficient cluster now at 2 instances (I-S04-03 + I-S05-02). **Promote to formal pattern?** The session-runner's "strongly recommended Option C" may need downgrading to "available" for parties with ratified player-styles.
- **Encounter craft:** I-S05-05 — 0-dice sessions are valid. Encounter craft at 8/10 without a single dice roll.

### **Player-style count update (post-S05)**

- `sheet-deep-reader`: S01 (3) + S02 (1) + S03 (1) + S04 (2) + S05 (3: Kessa-synthesis, Aelric-Oath, Aelric-silent-reception) = **10 total instances across 5 sessions.**
- `craft-witness`: S01 (2) + S02 (2) + S03 (3) + S04 (3) + S05 (3: gate-hinge, vault-stone, Wena's-hinge) = **13 total instances across 5 sessions.**
- `NPC-arc-completion` cluster: S03 Mira (1) + S05 Wena (1) = 2 instances. One more needed for cluster promotion.
- `hint-synthesis-in-voice`: S05 (1). Watch for #0006.
- `Option-A-sufficient` cluster: S04 (1) + S05 (1) = 2 instances. Ready for formal pattern promotion — "Option C is available, not mandatory, for parties with ratified player-styles."

---

## S06 Innovations — *The Thread-That-Frays* (2026-04-20)

### I-S06-01 — Gate-hinge bookend (craft-witness 4-scene silent arc)

**Dimension:** Atmospheric Landing
**Scene:** 02 (planted) → 07 (confirmed)
**What happened:** Grom checked Nenn's gate-hinge in Scene 2 (read it as honest work; "inside-curve true"). He confirmed it in Scene 7 (gate hinge still true; craft-witness closing loop). Four scenes. Zero words about Nenn between the two checks. The hinge said everything the craft-witness needed to say. Longest craft-witness silent arc in the campaign.
**Why it matters:** Previous craft-witness arcs were contained within a single session. The gate-hinge arc spans Scene 2 to Scene 7 — four scenes — without a word about the NPC. The craft-witness silent arc v1.4 amendment was ratified exactly for this pattern; this is the first instance of the amendment scoring at its designed ceiling. The arc proves that a spatial-return craft check is sufficient to close a 4-scene relationship.
**Status:** LOGGED. v1.4 amendment validated.

### I-S06-02 — Option C "I counted too" — sheet-content-surfaced line

**Dimension:** Character Agency / Surprise
**Scene:** 05 (Thera and Nenn at the gate)
**What happened:** Thera's Option C subagent produced the line "I counted too" from Thera's grief-paragraph (she counted the years after Adda died; PC sheet). The line was not in the module; it emerged from the sheet. Nenn said he had counted; Thera said she had too. This is sheet-deep-reader at its most complete: the PC's grief-paragraph contained the exact right sentence for the exact right moment.
**Why it matters:** Previous sheet-deep-reader instances surfaced decision frameworks (Aelric's Oath), institutional knowledge (Thera's Solamnic expertise), and research habits (Kessa's Vethrenn history). This is the first instance where sheet-deep-reader surfaced *grief-paragraph content* as spoken dialogue — the specific emotional fact in the PC's backstory became the character's most important line of the session.
**Status:** LOGGED. sheet-deep-reader sub-type: grief-paragraph-dialogue.

### I-S06-03 — Mira as emerging craft-witness (NPC craft-witness behavior)

**Dimension:** Atmospheric Landing
**Scene:** 07 (Aftermath at Stonfold)
**What happened:** Mira said "the forge feels cleaner" to Grom after the Thread was destroyed. She was reading the forge's spiritual state the way Grom does — sensing the forge's condition, not describing it analytically. She is not a forge-priest; she is Aelwen's great-great-great-granddaughter learning the Stonfold vein. This is craft-witness behavior outside the party's ratified craft-witness PC.
**Why it matters:** craft-witness has been defined as a PC player-style. S06 produced the first NPC instance of craft-witness behavior: Mira detecting spiritual state through material attention. This suggests craft-witness is not only a PC pattern but an NPC characterization tool. Third NPC-arc-completion-adjacent event (Mira, Wena, Mira again).
**Status:** LOGGED. NPC-arc-completion cluster now at 3 instances (S03 Mira + S05 Wena + S06 Mira). **Cluster promotion threshold reached.**

---

### Dimension-trigger check (post-S06)

- **Atmospheric Landing:** I-S06-01, I-S06-03 — craft-witness arc validation; NPC-craft-witness new type.
- **Character Agency:** I-S06-02 — sheet-deep-reader grief-paragraph-dialogue. Third consecutive sheet-deep-reader surprise.
- **NPC-arc-completion:** S03 Mira + S05 Wena + S06 Mira = **3 instances across 3 sessions. Cluster promotion threshold reached.**

### Player-style count update (post-S06)

- `sheet-deep-reader`: +1 (I-S06-02 Thera grief-paragraph) = **11 total instances across 6 sessions.**
- `craft-witness`: +1 (I-S06-01 gate-hinge arc) = **14 total instances across 6 sessions.**
- `NPC-arc-completion`: S03 Mira (1) + S05 Wena (1) + S06 Mira (1) = **3 instances — cluster trigger reached.** Promote.
- `hint-synthesis-in-voice`: S05 (1) — no S06 instance. Still 1.
- `Option-A-sufficient`: S04 (1) + S05 (1) — no S06 instance (Thera's Option C did fire). Still 2.

---

## S07 Innovations — *The Silver-Ingot Confession* (2026-04-20) — CAMPAIGN FINALE

### I-S07-01 — Campaign-debt confession (mechanic failure as carried emotional content)

**Dimension:** Atmospheric Landing / Character Agency
**Scene:** 01 (Cold-Vein Site; failure) → 06 (Confession; discharge)
**What happened:** Grom's pre-forge blessing failed (Religion 8 vs DC 10) at the cold-vein site. He said the words would come when the forge was ready. At the confession (Scene 06), he named not only Aelwen's shame but his own: *"I was slow and I was proud and I called it patience."* The failed pre-blessing — a dice outcome in Scene 01 — became carried emotional content and was discharged three scenes later as a third named thing in the confession. The ingot carries two shames: hers and his.
**Why it matters:** Atmospheric Landing anchors capture specific sensory images and finder-vs-receiver chains. They do not anticipate that a mechanic failure can be carried forward as emotional content and discharged in a binding confession three scenes later. This is a new pattern: failed-roll-as-carried-debt, discharged verbally at the session's climactic moment. The failure is not a loss; it is a setup.
**Status:** LOGGED. New pattern: failed-roll-as-carried-debt.

### I-S07-02 — Act-without-announcement (cross-session behavioral consequence)

**Dimension:** Character Agency / Atmospheric Landing
**Scene:** 07 (Road Home)
**What happened:** Thera cut bread long-ways on the road home. She was aware of doing it. She did not announce it or explain it. Grom watched and said nothing. The first time she did the thing she had been not-doing for twenty-three years, she did it without a scene or a speech or a dice roll. The S06 naming of Adda produced a cross-session behavioral change in S07 without any additional scene structure.
**Why it matters:** Character agency anchors capture decision-point choices in scenes. They do not anticipate cross-session behavioral consequences: a prior session's verbal disclosure generating a physical act in the next session, without DM prompt, without scene structure, without announcement. The act is the closure. The character does not narrate her own growth; she just does the thing.
**Status:** LOGGED. New pattern: cross-session behavioral-consequence without announcement.

### I-S07-03 — Archive-placement as closure (archivist inversion of sheet-deep-reader)

**Dimension:** Character Agency / Atmospheric Landing
**Scene:** 07 (Aftermath)
**What happened:** Kessa answered Vethrenn's two-hundred-year-old margin question in her own hand, then left the book on the workshop archive shelf rather than taking it. She did not collect the answer; she gave it back to the world. Sheet-deep-reader's usual register is accumulation (carry the evidence, cross-reference the fragments). Here, the pattern inverted: the catalog is complete; the archive is the right home for what was found.
**Why it matters:** sheet-deep-reader is defined as a PC who reads their sheet as a live source of agency and accumulates cross-session evidence. S07 produced the first instance of sheet-deep-reader *inversion*: the accumulated knowledge is placed rather than carried. The closure is spatial, not personal. This is a new sub-type: **archivist-closure** — the reader becomes the archivist.
**Status:** LOGGED. sheet-deep-reader sub-type: archivist-closure.

### I-S07-04 — Simultaneous hint delivery as campaign resonance

**Dimension:** Atmospheric Landing / Module Fidelity / Surprise
**Scene:** 06 (Ingot-Forging)
**What happened:** All four campaign hints (Fresco-Heal; Vethrenn's margin; Reorx's Judgment; Aelwen's Confession) were delivered in the same scene — Scene 06, ingot-forging — converging at the moment the silver flowed clean. Each hint was planted in a different session (S01, S01, S04, S03). The simultaneous convergence was not scripted; it emerged from the design of the rite + the specific dice outcome (Religion 23 → Route D) + the spatial logic of the forge.
**Why it matters:** Module Fidelity captures whether planned manifest symptoms land. It does not capture multi-session hint convergence as a resonance event. The rubric has no anchor for "all campaign hints delivered simultaneously at a single structural moment." This is a new phenomenon: the finale's dice outcome triggers a retroactive convergence across 7 sessions of campaign history. Seven sessions of campaign debt discharged in one moment.
**Status:** LOGGED. New pattern: simultaneous-campaign-hint-convergence.

---

### Dimension-trigger check (post-S07) — CAMPAIGN COMPLETE

**Campaign total innovations: 43 (7+10+7+5+6+3+4 across S01-S07).**

- **Atmospheric Landing:** I-S07-01, I-S07-03, I-S07-04 — three instances. Strong cluster evidence for "long-arc debt discharge" as a new Atmospheric Landing anchor above the 10-band.
- **Character Agency:** I-S07-02, I-S07-03 — cross-session behavioral consequence; archivist-closure.
- **Module Fidelity:** I-S07-04 — simultaneous-campaign-hint-convergence. First and only instance; campaign-specific.

### Player-style count update (post-S07) — FINAL CAMPAIGN TOTALS

- `sheet-deep-reader`: +2 (I-S07-01 Grom grief-paragraph discharge; I-S07-03 Kessa archivist-closure) = **13 total instances across 7 sessions.** Both new sub-types confirmed: grief-paragraph-dialogue (S06) and archivist-closure (S07).
- `craft-witness`: +2 (I-S07-01 Grom carries pre-blessing failure; I-S07-02 Grom witnesses Thera's bread without speaking) = **16 total instances across 7 sessions.** Campaign complete.
- `NPC-arc-completion` (promoted threshold reached S06): final campaign count = 3 instances. Promotion confirmed.
- `Option-A-sufficient` (I-S04-03 + I-S05-02): confirmed validated pattern across campaign. 2 instances sufficient for design principle: Option C is available, not mandatory, for parties with ratified player-styles.

---

## C2-S01 Innovations — *The First Clause* (2026-04-20) — Campaign 2 opens

### I-C2-S01-01 — NPC-self-naming (Henneth's three-year observation)

**Dimension:** Atmospheric Landing / Surprise
**Scene:** 03 (The Study)
**What happened:** Henneth asked *"Is that why it dims when Sevel lies?"* He had been observing the dimming for three years without vocabulary for it. He named the phenomenon the moment the party gave him the explanation. The NPC arc-completion was collaborative: Henneth was already halfway there; the party gave him the second half.
**Why the rubric did not anticipate it:** NPC-arc-completion captures the moment an NPC delivers their designed emotional payload. This is that, plus: the NPC was already carrying the observation; he just needed the word. The arc-completion was co-constructed, not one-directional. New sub-type: **NPC-self-naming** — the NPC names the phenomenon before the party does, once given vocabulary.
**Status:** LOGGED. NPC-arc-completion sub-type candidate. Running campaign 2 total: 1 instance.

### I-C2-S01-02 — act-without-announcement confirmed universal (new party, Session 1)

**Dimension:** Character Agency / Atmospheric Landing
**Scene:** 06 (Tessamine's Archive, Return)
**What happened:** Sera gave Thessaly space in the final scene by looking at the harbor window. She did not announce she was doing it; she did not explain it afterward. Care expressed through attention withdrawal. The pattern identified in campaign 1 S07 (Thera's bread) fired in Session 1 of campaign 2 with a completely different party and a completely different PC.
**Why it matters:** act-without-announcement was logged as a 1-instance pattern from campaign 1. Campaign 2 Session 1 confirms it as universal — it emerged from Sera's sheet (voice tags: "shows care through attention, not words") without any campaign 1 context. **Cluster trigger reached: 2 instances across 2 campaigns.** Propose amendment to Atmospheric Landing.
**Status:** LOGGED. **Amendment candidate: Atmospheric Landing anchor for cross-session behavioral consequence without announcement.**

### I-C2-S01-03 — grief-paragraph-dialogue fires Session 1 (not Session 6)

**Dimension:** Character Agency / Atmospheric Landing
**Scene:** 06 (Tessamine's Archive, Return)
**What happened:** Thessaly named her wound in Scene 06: *"I cast a spell at my Test that I was not supposed to cast. It cost someone something I can't give back. No one saw me do it."* This is grief-paragraph content surfaced as spoken dialogue in Session 1 — the same sub-type as Thera's *"I counted too"* (campaign 1 S06). Thessaly's grief-paragraph contained the exact right sentence for the exact right moment, and it emerged from the artifact's invitation (Tessamine's arc-completion condition: "Thessaly names the inscription's meaning") without DM prompting.
**Why it matters:** grief-paragraph-dialogue (sheet-deep-reader sub-type) fired in Session 1, not Session 6. The npc-architect design created the structural invitation earlier than campaign 1 did. **Cluster confirmation: grief-paragraph-dialogue now has 2 instances across 2 campaigns (Thera S06-C1; Thessaly S01-C2).** The pattern is confirmed as a design tool, not a late-campaign accident.
**Status:** LOGGED. sheet-deep-reader sub-type: grief-paragraph-dialogue. **2 instances across 2 campaigns — confirmed.**

---

### Dimension-trigger check (post-C2-S01)

- **Atmospheric Landing:** I-C2-S01-01, I-C2-S01-02, I-C2-S01-03 — three new instances. act-without-announcement (2 across 2 campaigns) now meets amendment threshold.
- **act-without-announcement amendment proposal:** Atmospheric Landing 9+ band anchor: "A score of 9+ recognizes cross-session behavioral consequence without announcement — a PC acting differently as a result of a prior session's naming event, without scene structure or declaration." Propose amendment to v1.5.

### Player-style count update (post-C2-S01)

**Campaign 2 opening counts:**
- `sheet-deep-reader`: 4 instances in S01 (Thessaly ×3 + Calder ×1). Campaign 2 opens with immediate sheet-deep-reader firing — confirmed universal, not party-specific.
- `craft-witness`: 0 instances in S01. No forge-priest; Calder's morning ritual has not produced atmospheric reception yet. Watch for S02.
- `act-without-announcement`: 1 instance (Sera S01). Campaign 2 total: 1. Cross-campaign total: 2 (Thera C1-S07 + Sera C2-S01). Amendment threshold reached.
- `NPC-arc-completion`: 1 instance (Henneth). Campaign 2 total: 1.
- `NPC-self-naming` (new sub-type candidate): 1 instance.

---

## C2-S02 Innovations — *The Ambitious Mage's Vault* (2026-04-20)

### I-C2-S02-01 — grief-paragraph-dialogue confirmed cross-campaign (3rd instance)

**Dimension:** Character Agency / Atmospheric Landing
**Scene:** 03 (Research Floor)
**What happened:** Orik named the hall — grief-paragraph content surfaced as artifact explanation: *"The shard vibrates for me because I'm still trying to prove it was worth going."* He understood the Clause of Ambition's mechanism by reading his own grief-paragraph, without prompting, and delivered it as spoken dialogue. Third instance of grief-paragraph-dialogue across 2 campaigns (Thera C1-S06, Thessaly C2-S01, Orik C2-S02). Three different PCs; three different grief-paragraphs; same pattern.
**Why it matters:** Three instances across 2 campaigns = cluster-threshold met. grief-paragraph-dialogue is now a confirmed sheet-deep-reader sub-type. Formalized in `personas/player-styles/sheet-deep-reader.md`. The structural invitation pattern is confirmed: an artifact/NPC/place that mirrors the grief creates the opening; the dialogue comes from the sheet.
**Status:** LOGGED. **sheet-deep-reader sub-type: grief-paragraph-dialogue — CONFIRMED. See sheet-deep-reader.md.**

### I-C2-S02-02 — craft-witness from hall-guard (first non-craft-priest instance)

**Dimension:** Atmospheric Landing
**Scene:** 04 (Old Study)
**What happened:** Orik touched the doorframe after receiving the shard — inside-curve structural assessment from eight years of hall-guarding. His hand went to the frame before he thought about it: load-bearing quality, settlement, wear. He was reading the tower the way he reads every structure he guards. The touch produced atmospheric reception: eight years of one person maintaining this space; the frame is true.
**Why it matters:** craft-witness has previously required a designated craft-ritual (Grom's hearth-greeting). This is the first instance from a secular professional practice — a hall-guard's habitual structural attention. If Orik fires again in S03 or S04, craft-witness is confirmed as ritual-practice-as-antenna, not religious-class-as-antenna. That changes the style's applicability significantly.
**Status:** LOGGED. craft-witness candidate, non-craft-priest. Watch for repeat before formalizing.

### I-C2-S02-03 — act-without-announcement confirmed (3 instances in 2 sessions, Sera)

**Dimension:** Atmospheric Landing / Character Agency
**Scene:** 03 and 05
**What happened:** Sera held space for Orik's arc-completion (Scene 03, parapet) and for Lenne's unfinished sentence (Scene 05, roof). Third and fourth consecutive instances of Sera expressing care through attention withdrawal — not announced, not explained, just done. Cross-campaign total now 4 (Thera C1-S07 + Sera C2-S01 + Sera C2-S02 ×2).
**Why it matters:** Amendment v1.5 ratified from this pattern. Atmospheric Landing 9+ band now anchors on act-without-announcement. The amendment was proposed after C2-S01 (2 cross-campaign instances); C2-S02 confirms it was the right threshold to fire on. Ratified.
**Status:** LOGGED. **Amendment v1.5 constituent. Ratified.**

### I-C2-S02-04 — arc-completion-as-opening (Lenne joining party)

**Dimension:** Character Agency / Surprise
**Scene:** 05 (Tower Roof)
**What happened:** Lenne's arc-completion fired in Scene 03 (gave the shard freely). Scene 05: she asked to join the party. The arc-completion did not close her NPC thread — it opened a new campaign thread (fifth party member; eight years of compact research; knowledge of Volenn's methods). First instance of an arc-completion producing a forward thread rather than a closure.
**Why it matters:** npc-architect skill designs arc-completions as closure moments ("what happens if the condition is never met"). Lenne demonstrates that arc-completion can be a pivot — the NPC reorients toward the work rather than away from it. npc-architect should be updated to flag when an NPC's arc-completion is likely to open rather than close, so the DM is prepared for the forward thread.
**Status:** LOGGED. npc-architect skill update recommended.

---

### Dimension-trigger check (post-C2-S02)

- **Atmospheric Landing:** I-C2-S02-01, I-C2-S02-02, I-C2-S02-03 — three new instances. Act-without-announcement amendment v1.5 ratified. craft-witness non-craft-priest candidate logged.
- **Character Agency / Surprise:** I-C2-S02-04 — arc-completion-as-opening. New pattern, 1 instance.

### Player-style count update (post-C2-S02)

- `sheet-deep-reader`: +4 (I-C2-S02-01 Orik grief-paragraph-dialogue; Lenne pattern-recognition; Calder dying-man's-to-do; Orik room-reading) = **8 total C2 instances across 2 sessions.** grief-paragraph-dialogue sub-type confirmed (3 cross-campaign).
- `craft-witness`: +1 (I-C2-S02-02 Orik doorframe) = **1 C2 instance.** Non-craft-priest candidate. Watch for repeat before promoting.
- `act-without-announcement`: +2 (I-C2-S02-03 Sera ×2) = **3 C2 instances; 4 cross-campaign.** Amendment v1.5 ratified.
- `NPC-arc-completion`: +1 (Lenne S02) = **2 C2 instances** (Henneth S01 + Lenne S02). 1 more for cluster promotion.
- `arc-completion-as-opening`: 1 instance. Watch.

---

## C2-S03 Innovations — *The Grief Inscription* (2026-04-20)

### I-C2-S03-01 — Bilateral arc-completion (reciprocal naming chain)

**Dimension:** Atmospheric Landing / Character Agency
**Scene:** 04 (The Sanctuary)
**What happened:** Sera named the settlement; Morreth named Ven immediately after. Neither naming could have happened without the other — Sera's naming was the condition for Morreth's, and Morreth's naming was the response that completed the exchange. The bilateral structure was designed; the execution exceeded the design in timing and emotional specificity.
**Why it matters:** NPC-arc-completion has been one-directional: party creates conditions, NPC delivers. This is the first instance where an NPC arc-completion fires in direct response to a PC arc-completion, creating a reciprocal naming chain. New sub-type: **bilateral-arc-completion**. The NPC receives the PC's grief and returns their own.
**Status:** LOGGED. NPC-arc-completion sub-type: bilateral-arc-completion.

### I-C2-S03-02 — Lenne's empty notebook (archivist confronts undocumentable experience)

**Dimension:** Character Agency / Atmospheric Landing
**Scene:** 05 (Chapel Ruins, aftermath)
**What happened:** After the arc-completion scene, Lenne opened her notebook and didn't write and put it away. She has been documenting constantly since joining the party. This is the first time she encountered something she could not categorize. The notebook open and then closed is more specific than "she was moved."
**Why it matters:** sheet-deep-reader sub-type candidate: the archivist who puts the notebook away. The arc-completion landed on her as a non-documentable experience — her documentation practice, which is her primary mode of relating to the world, was suspended by the weight of what she witnessed. This is a new register for sheet-deep-reader: the moment when the sheet's primary heuristic cannot apply.
**Status:** LOGGED. sheet-deep-reader sub-type candidate: documentation-suspension.

### I-C2-S03-03 — Mira arc-completion as faction-pivot

**Dimension:** Character Agency / Surprise
**Scene:** 01 (Road Encounter)
**What happened:** Mira Coldsteel's arc-completion fired in Scene 01 of the first session she appeared in. The Unbound Conclave's antagonist thread permanently closed before a single combat roll. Thessaly explained Route D specifically; Mira said *"That would actually fix it"* and stood her agents down permanently. She asked to witness the new compact. Thessaly accepted.
**Why it matters:** arc-completion-as-faction-pivot — the NPC's arc-completion changes the campaign's structural antagonist landscape, not just one NPC's thread. The campaign must now find its tension elsewhere than the Unbound Conclave. This is a second form of arc-completion-as-opening (from Lenne S02): instead of opening a party-composition thread, it closes the campaign's primary antagonist structure and opens a collaborative witness thread.
**Status:** LOGGED. arc-completion-as-faction-pivot (related to arc-completion-as-opening; distinct sub-type).

### I-C2-S03-04 — craft-witness pattern confirmed for non-craft-priest (Orik, second instance)

**Dimension:** Atmospheric Landing
**Scene:** 04 (The Sanctuary)
**What happened:** Orik checked the sanctuary doorframe inside-curve after the bilateral arc-completion. Second consecutive session (S02: Volenn's doorframe; S03: Morreth's doorframe). Both after significant emotional moments. His hall-guard structural assessment as grounding fires in the same register as Grom's forge-greeting.
**Why it matters:** craft-witness was defined as requiring a designated craft-ritual. Two consecutive instances of Orik's secular professional practice (hall-guard structural assessment) producing atmospheric reception in the same register confirms the pattern. craft-witness is **ritual-practice-as-antenna**, not **religious-class-as-antenna**. Orik's practice is secular; Grom's was religious; the pattern is the same. **Cluster promotion: craft-witness confirmed universal.** Any PC with a specified habitual practice can develop craft-witness.
**Status:** LOGGED. **craft-witness: confirmed universal pattern. Secular professional practice counts. No religious class required.**

---

### Dimension-trigger check (post-C2-S03)

- **Atmospheric Landing:** I-C2-S03-01, I-C2-S03-02, I-C2-S03-03, I-C2-S03-04 — four new instances.
- **NPC-arc-completion:** C2 total now 3 instances (Henneth S01 + Morreth S03 + Mira S03). **Cluster promotion threshold reached.** Promote to player-style.
- **craft-witness universal:** Second non-craft-priest instance. Pattern confirmed universal. Update craft-witness.md definition.

### Player-style count update (post-C2-S03)

- `sheet-deep-reader`: +5 (Lenne reads Mira; Calder inscription ×3 silent; Sera names settlement; Calder names promise; Lenne empty notebook) = **13 total C2 instances across 3 sessions.**
- `craft-witness`: +1 (Orik doorframe S03) = **2 C2 instances (confirmed universal).** Update definition: any habitual professional practice produces the pattern.
- `act-without-announcement`: +2 (Sera perimeter scan S03; Lenne notebook S03) = **5 C2 instances; 6 cross-campaign.** Fully ratified; counting continues.
- `NPC-arc-completion`: +2 (Morreth bilateral S03; Mira faction-pivot S03) = **4 C2 instances.** Cluster promotion threshold met. Promote.
- `bilateral-arc-completion`: 1 instance. New sub-type of NPC-arc-completion.
- `arc-completion-as-faction-pivot`: 1 instance. Second form of arc-completion-as-opening.
- `documentation-suspension`: 1 instance (Lenne S03). sheet-deep-reader sub-type candidate.

---

## C2-S04 Innovations — *The Defiant Word* (2026-04-20)

### I-C2-S04-01 — Simultaneous multi-arc-completion (second instance)

**Dimension:** Atmospheric Landing / Surprise
**Scene:** 04 (Deep Archive)
**What happened:** Four arc-completions fired simultaneously — Calder named the plague village (PC arc-completion); the second inscription warmed (artifact response); Sevven named the Dalimvar numbers (NPC arc-completion); Deva said *"I still know the words"* (NPC arc-completion). Same structure as campaign 1 S07 (all four hints simultaneously delivered).
**Why it matters:** Second instance of simultaneous-campaign-arc-convergence (I-S07-04 was the first). Pattern confirmed as not campaign-1-specific. The mechanism: a moment of precise naming in the presence of the right witnesses triggers all outstanding arc-completions that were waiting for it. The convergence is structural, not scripted.
**Status:** LOGGED. **simultaneous-campaign-arc-convergence: 2 instances across 2 campaigns. Amendment candidate for Atmospheric Landing 10-band.**

### I-C2-S04-02 — Sera's cross-adventure pattern-accumulation (perimeter-reader becomes pattern-tracker)

**Dimension:** Atmospheric Landing / Character Agency
**Scene:** 04 (Deep Archive)
**What happened:** Sera noticed the carved figure in the display case (Sylaren's, facing outward, from the ruins of Istar) and recognized it had the same placement as Morreth's carved figure in the chapel gap (S03). Two adventures apart. She said nothing about either instance.
**Why it matters:** Perimeter-reading (Sera's established mode) applied to meaning-patterns across sessions. She is accumulating the shape of a pattern she has not yet named. sheet-deep-reader / craft-witness hybrid: the perimeter-reader becomes a pattern-tracker. This is a new behavior not captured by either existing style.
**Status:** LOGGED. New behavior: cross-session pattern-tracking without announcement. Watch for what she does with the pattern when she names it.

### I-C2-S04-03 — craft-witness confirmed universal: three consecutive sessions

**Dimension:** Atmospheric Landing
**Scene:** 01 (Entrance)
**What happened:** Orik checked the tunnel hatch inside-curve on the way in. Third consecutive session with an inside-curve or structural assessment producing atmospheric reception (S02: Volenn's doorframe; S03: Morreth's sanctuary doorframe; S04: tunnel hatch). The pattern fires regardless of the emotional weight of the surrounding scene.
**Why it matters:** Three consecutive sessions confirms craft-witness as a fully integrated behavior for Orik, not a periodic firing. The secular professional practice (hall-guard structural assessment) produces consistent atmospheric reception across all session types: highly emotional (S03 bilateral arc-completion), combat-adjacent (S04 entrance), and social-heavy (S02 research tower). **craft-witness is confirmed as session-invariant for Orik.** Update craft-witness.md to reflect secular-professional as the primary trigger, not craft-priest ritual.
**Status:** LOGGED. **craft-witness: session-invariant confirmed. Three consecutive sessions. Update craft-witness.md.**

### I-C2-S04-04 — archivist-closure confirmed cross-campaign (second instance)

**Dimension:** Character Agency / Atmospheric Landing
**Scene:** 05 (Sevven's Study)
**What happened:** Calder read Sylaren's personal note and returned it to Sevven. He did not keep it. Second instance of archivist-closure across two campaigns (Kessa C1-S07 left Vethrenn's commonplace book in the workshop archive; Calder C2-S04 returned Sylaren's note to the personal correspondence).
**Why it matters:** archivist-closure (sheet-deep-reader sub-type: the PC receives the accumulated knowledge and places it rather than carrying it) has now fired with two different PCs in two different campaigns with two different grief-relationships. The pattern is not character-specific or campaign-specific. It is a mode of closure that emerges when a PC who accumulates evidence encounters something that belongs in a permanent repository. **Confirm as sheet-deep-reader sub-type.**
**Status:** LOGGED. **archivist-closure: 2 instances across 2 campaigns. Sub-type confirmed. Update sheet-deep-reader.md.**

---

### Dimension-trigger check (post-C2-S04)

- **Atmospheric Landing:** I-C2-S04-01, I-C2-S04-02, I-C2-S04-03, I-C2-S04-04 — four new instances.
- **simultaneous-campaign-arc-convergence:** 2 instances (C1-S07 + C2-S04). **Amendment candidate: Atmospheric Landing 10-band should recognize simultaneous arc-convergence as a distinct peak.**
- **archivist-closure:** 2 cross-campaign instances. Sub-type confirmed; update sheet-deep-reader.md.
- **craft-witness session-invariant:** 3 consecutive sessions for Orik. Update craft-witness.md definition.

### Player-style count update (post-C2-S04)

- `sheet-deep-reader`: +4 (Thessaly names splinter cell; Lenne reads Deva; Calder names village; Calder returns note) = **17 total C2 instances across 4 sessions.**
- `craft-witness`: +1 (Orik hatch S04) = **3 C2 instances; session-invariant confirmed for Orik.**
- `act-without-announcement`: +1 (Sera air-shaft S04) = **6 C2 instances.**
- `NPC-arc-completion` (cluster promotion reached S03): **4 C2 instances confirmed.** Formally promote.
- `archivist-closure`: 2 cross-campaign instances. Sub-type confirmed.
- `simultaneous-campaign-arc-convergence`: 2 instances. Amendment candidate.
- `cross-session-pattern-tracking` (Sera): 1 instance. New behavior. Watch.


---

## C2-S05 Innovations — *The Reckoning Stone* (2026-04-20)

### I-C2-S05-01 — Bilateral arc-completion confirmed as campaign structure

**Dimension:** Atmospheric Landing / Character Agency
**Scene:** 04 (Vorn's Study)
**What happened:** Thessaly named the Test wound; Vorn named the Crystalmir family. Second bilateral arc-completion (S03: Sera → Morreth; S05: Thessaly → Vorn). Two adventures, two bilateral namings. Each time: one PC's naming enabled one NPC's naming.
**Why it matters:** Bilateral arc-completion is confirmed as a campaign structure. The pattern is designable (npc-architect condition: "a PC names something equivalent first") and recurring.
**Status:** LOGGED. bilateral-arc-completion: 2 instances. Campaign structure confirmed.

### I-C2-S05-02 — Lenne's practitioner-recognition cascade (third consecutive session)

**Dimension:** Atmospheric Landing / Character Agency
**What happened:** Lenne identified Vorn as a methodological peer from how she engaged with research. Third consecutive session: Mira (S03, by school from posture), Deva (S04, by text-handling), Vorn (S05, by research methodology). She reads practitioners the way she reads objects — by their relationship to their material.
**Status:** LOGGED. sheet-deep-reader sub-type: practitioner-by-material-relationship.

### I-C2-S05-03 — Calder named the witness-list unprompted

**Dimension:** Character Agency
**What happened:** Calder named the witness-list — Mira, Deva, Vorn, Sevven, Morreth's chapel — without being asked. He was making sure the campaign's promises were accounted for. Decision-order: "what is the weight of this?" applied to the full campaign's commitment structure.
**Status:** LOGGED. sheet-deep-reader commitment-accounting sub-type candidate.

### I-C2-S05-04 — Lenne drafted compact language on the roof

**Dimension:** Character Agency / Surprise
**What happened:** Lenne began drafting accountability clause language with Vorn during the aftermath scene — uninvited, without asking, because she has the vocabulary and the right collaborator. documentation-suspension resolved (S03) → empty page filled (S04) → designing forward-looking documents (S05). Three-session character arc.
**Status:** LOGGED. Character arc milestone: documentation practice transformed.

---

### Player-style count update (post-C2-S05)

- `sheet-deep-reader`: +4 = **21 total C2 instances across 5 sessions.**
- `craft-witness`: +1 (Orik building-assessment) = **4 C2 instances; session-invariant.**
- `act-without-announcement`: +1 (Sera perimeter) = **7 C2 instances; 8 cross-campaign.**
- `bilateral-arc-completion`: 2 instances. Campaign structure confirmed.

---

## C2-S06 Innovations — *The Forgiveness Key* (2026-04-20)

### I-C2-S06-01 — Compact opening sentence written in silence (act-without-announcement peak)

**Dimension:** Character Agency / Atmospheric Landing
**Scene:** 04 (Pellan's Garden)
**What happened:** Thessaly wrote the opening sentence of the new compact in the margin of the reconstruction document. She has been composing it mentally for three sessions (S04: designing; S05: not writing; S06: writing). She did not show it to anyone. The most significant single act of compact preparation was performed silently, without announcement.
**Why it matters:** act-without-announcement has fired consistently (Sera's perimeter scans; Calder's grief weight; Lenne's notebook). S06 produced its highest-stakes instance: Thessaly wrote the compact's opening words — the thing the campaign has been building toward — without making it a scene. This is the pattern at its fullest expression.
**Status:** LOGGED. act-without-announcement: peak instance.

### I-C2-S06-02 — craft-witness x5: session-invariant fully confirmed

**Dimension:** Atmospheric Landing
**What happened:** Orik checked the cottage doorframe inside-curve. Fifth consecutive session with a structural assessment. The pattern has not missed a session since he joined the compact-wardens.
**Why it matters:** Session-invariant confirmed beyond doubt. craft-witness is not a periodic firing for Orik; it is his mode of entry into every new space. Every session of campaign 2 has included a craft-witness moment for Orik. This should be added to the craft-witness.md definition as the "session-invariant" clause.
**Status:** LOGGED. craft-witness: session-invariant for Orik. Update craft-witness.md.

### I-C2-S06-03 — Route D offer as campaign behavior (third consecutive)

**Dimension:** Character Agency
**What happened:** The party offered the splinter cell the same stand-down terms they gave the first agents at the White Quill entrance (S04) and the first terms they used at the Kharolis road (S02). Three encounters, three stand-down offers. The pattern is campaign behavior, not individual session choice.
**Why it matters:** The party has developed a consistent operational posture — offer the stand-down first, fight second if necessary — that is traceable to their decision-orders (Thessaly: knowledge before action; Calder: what is the weight of this?; Orik: can I fix this without a fight?). This is sheet-deep-reader applied at the party level: the party's combined decision-orders produce consistent behavior across sessions.
**Status:** LOGGED. Party-level sheet-deep-reader: operational posture as campaign pattern.

---

### Player-style count update (post-C2-S06)

- `sheet-deep-reader`: +4 = **25 total C2 instances across 6 sessions.**
- `craft-witness`: +1 = **5 C2 instances; session-invariant.** Fires every session without exception.
- `act-without-announcement`: +2 = **9 C2 instances; 10 cross-campaign.**

---

## C2-S07 Innovations — *The New Covenant* (2026-04-20) — CAMPAIGN COMPLETE

### I-C2-S07-01 — Thessaly's opening sentence (act-without-announcement peak of campaign)

**Dimension:** Character Agency / Atmospheric Landing
**What happened:** Thessaly spoke the opening sentence of the new compact for the first time — composed across three sessions, written silently in a margin, never shared. *"We speak this not to bind the Orders to each other but to bind each Order to the people who live beneath the consequences of what the Orders do."* It said exactly what twelve years of Vorn's research concluded, in one sentence, in Thessaly's register.
**Why it matters:** The opening sentence is the campaign's most consequential act-without-announcement. She composed it in S04 (mental design), committed to it in S05 (still not writing), wrote it silently in S06 (written, not shown), and spoke it in S07 (first time aloud). Four sessions of preparation without announcement, culminating in the compact's opening words.
**Status:** LOGGED. Campaign-complete act-without-announcement.

### I-C2-S07-02 — Calder incorporated Sylaren's amendment as clause completion

**Dimension:** Character Agency / Atmospheric Landing
**What happened:** Calder spoke the Defiance clause and then, as part of the clause — not as a footnote — spoke Sylaren's full amendment: *"And as Sylaren wrote, twelve years after she swore it: what any mortal swore, any mortal may unsay. This was always true."* He understood that the amendment was not separate from the clause. It was the clause's completion. Hint 3's promise honored in the speaking.
**Status:** LOGGED. Hint delivery honored in the finale speaking.

### I-C2-S07-03 — craft-witness x6: finale craft-witness

**Dimension:** Atmospheric Landing
**What happened:** Orik checked the stairs on the way down AND the first step on the way up as the water rose. Sixth consecutive session. Final craft-witness of the campaign. He is still the hall-guard in the ruins of Istar as the convergence window closes. He always will be.
**Status:** LOGGED. craft-witness: session-invariant across all seven sessions of campaign 2. One per session. Never missed.

### I-C2-S07-04 — Mira's "It's done"

**Dimension:** Atmospheric Landing / NPC arc-completion
**What happened:** Mira Coldsteel, who has not spoken during the compact speaking, said: *"It's done."* Twelve years of research, operational work, and waiting for the compact to be fixed — received. She said it the way you say the thing you have been waiting to say. It is a statement, not a celebration.
**Status:** LOGGED. NPC arc-completion finale: Mira receives what she has been working toward.

---

## C3-S1 — 2026-04-21 — the-witnesses — 0015-the-gatehouse-watch

### I-C3-S1-01 — Fumble-as-arc-activation

**Dimension:** Atmospheric Landing (cross: Character Agency, Surprise)
**What happened:** *"She cannot categorize them at all. She can describe them. She can recognize what they are not. But what they are — what tradition this represents — she has no frame for it. She holds the observation."* (Scene 2.1) Calla's Insight check fumbled (1 on die, total 6 vs DC 12). Her documentation-arc did not fail to fire — it fired precisely because her categorical vocabulary broke on contact with the congregation's shrine arrangements. The fumble IS the arc beat. The arc activated from a failed check, not from a discovery.
**Why the rubric did not anticipate it:** Every existing arc-activation pattern in the log (sheet-deep-reader, craft-witness, documentation-arc candidate) assumes a discovery, observation, or successful perception triggers the arc. I-C3-S1-01 establishes a variant: the arc fires when the observer's framework fails on contact. The content is not unusual enough to exceed the framework — the framework simply does not apply, and the gap between the two is the emotional landing.
**Scope:** Universal (any PC with an archivist, documentation, or categorization-oriented practice).
**Status:** adopted (v1.7)

---

### I-C3-S1-02 — Designed trigger-point ≠ actual firing-point for character arcs

**Dimension:** Atmospheric Landing (cross: Character Agency)
**What happened:** The module's GM Notes designed Dren Holt's crack to activate "when Dren understands Mig is holding a healer's bag — that she came here because a healer came for her people" (Scene 2.1). The understanding landed at Scene 2.1 (the DM noted "this is the seed"). The crack fired at Scene 6 — when Dren watched the healer's bag reach its destination. Seeding and firing separated by four scenes. *"He does not say anything. The pause before the word 'healer' is there, held, and released without speaking."* (Scene 6)
**Why the rubric did not anticipate it:** v1.4 captures multi-scene silent-reception chains (3+ scenes held). This is partially covered. The novel element is the module-design implication: the *designed* trigger point (understanding the cause) differed from the *actual* firing point (witnessing the consequence). Character arcs require both cause and consequence; the arc fires at the consequence, not the cause. Designing a trigger that names only the cause — as this module did — will produce delayed firing.
**Scope:** Universal. Module-design implication: design arc trigger points at the *consequence*, not the *cause*, or expect delayed firing.
**Status:** adopted (v1.7)

---

### I-C3-S1-03 — Craft-witness fires through unnamed NPC witness

**Dimension:** Atmospheric Landing (cross: Engagement)
**What happened:** *"Maret stands at the south parapet... She performs three breaths... one of the congregation members who entered R5 behind the party — a gully dwarf woman, older than Mig — sits down facing the shrine and begins a repetitive motion with a smooth stone: turning it in her hands with a specific rhythm."* (Scene 5) Craft-witness fired through an unnamed congregation member, not through the session's named NPC contact (Mig). The structural parallel was PC practice ↔ unnamed NPC practice in the same room.
**Why the rubric did not anticipate it:** Craft-witness in C1 fired through the physical environment (Orik's hall-guard practice). C2 confirmed craft-witness fires through named NPCs. C3-S1 establishes that craft-witness fires through unnamed NPCs as well — the witness does not need to be named or individually designed. The session module did not script this unnamed member's stone-turning; it emerged from the congregation's group behavior logic (they have their own rites). Craft-witness is broader than we knew.
**Scope:** Universal. Craft-witness requires only structural parallel between PC practice and observed practice; the witness may be unnamed.
**Status:** LOGGED. **Craft-witness: unnamed NPC instance. Update craft-witness.md.**

---

### I-C3-S1-04 — Class feature as social encounter architecture bypass

**Dimension:** Character Agency (cross: Mechanical Fairness)
**What happened:** *"He uses Awakened Mind to reach Mig. He says, in the space between her ears: 'We were sent to assess the building. We are not here to drive you out. We want to understand what you are protecting.'"* (Scene 3) Renn's Warlock class feature (Awakened Mind) bypassed the social encounter's entire designed architecture — no Persuasion check, no Insight roll, no shared language requirement. The social encounter resolved from a class feature, not a skill check or social roll.
**Why the rubric did not anticipate it:** Character Agency anchors assume skill-check-based resolution for social encounters. Mechanical Fairness anchors cover cross-character mechanical compounds (v1.4 — one PC's feature applied to another PC's roll). This is distinct: a PC's passive class feature replacing the encounter's resolution architecture entirely, without any roll. No roll means no dice variable; the success or failure of the communication was adjudicated narratively, not mechanically.
**Scope:** Universal. Any PC with telepathic class features (Warlock Awakened Mind, Telepathic Feat, Mind Flayer lineage) can produce this bypass in social encounters with language barriers.
**Status:** LOGGED. **Module-design implication: future social encounters should note in GM Notes whether telepathy bypasses the language barrier and, if so, what the consequence is.**

---

### C3-S1 Threshold Check

**Pathway A — Dimension trigger (2+ logged in same dimension):**

New logged entries this session:
- Atmospheric Landing: I-C3-S1-01 (fumble-as-arc-activation), I-C3-S1-02 (designed/actual trigger separation), I-C3-S1-03 (craft-witness/unnamed NPC) = **3 entries**
- Character Agency: I-C3-S1-04 (Awakened Mind bypass) = **1 entry**

Atmospheric Landing now has 3 new `logged` entries this session. Combined with existing `logged` Atmospheric Landing entries from prior sessions (see I-C2-S07-03, I-C2-S05 series, etc.), the threshold is met.

**AMENDMENT PROPOSAL — v1.6 → v1.7**
**Dimension:** Atmospheric Landing
**Constituent innovations:** I-C3-S1-01 (fumble-as-arc-activation), I-C3-S1-02 (designed/actual trigger separation)
**Theme:** Arc-activation mechanisms that differ from designed trigger points — either because the arc fires from framework failure (01) or because the actual firing point is the consequence rather than the cause (02).
**Proposed change (7+ band addition):**
> **v1.7 framework-failure arc-activation anchor:** A score of 7+ additionally recognizes arc-activation triggered by a *failed check* — where a PC's categorical or observational framework breaks on contact with the content, and the gap between framework and content IS the emotional landing. The check failure is not a setback; it is the arc beat. Arc-activation need not follow a discovery; it may follow a failure. Rationale: C3-S1 Calla's documentation-suspension activated from Insight fumble (total 6), not from a discovery.

**Prompt to user:** *"3 Atmospheric Landing innovations logged in C3-S1. Amendment proposal: v1.6 → v1.7, adding framework-failure arc-activation to the 7+ band. Adopt?"*

**Pathway B — Cluster trigger (3+ across ≥ 2 sessions):**

Checking I-C3-S1-03 (craft-witness/unnamed NPC) against existing craft-witness entries: The craft-witness pattern already has a ratified player-style file (`personas/player-styles/craft-witness.md` or equivalent). This entry is an expansion of an existing ratified style, not a new style proposal. **Action: Update craft-witness.md to note unnamed-NPC instances are valid** — no new style proposal needed.

No new player-style proposals this session (single-session cluster; needs ≥ 2 sessions).

---

### Campaign 3 running tallies (post-S1)

- `sheet-deep-reader`: 6 instances (S1) — fires in S1 with new party as predicted.
- `craft-witness`: 1 instance (S1, unnamed NPC) — research question answered: fires session-invariantly without physical object or hall.
- `verbal-documentation-arc` (provisional): 2 activations (S1) — needs S2 data before cluster evaluation.
- `NPC-arc-completion`: 1 instance (S1 — Mig). Running total: 1/3 for style-promotion threshold.
- `bilateral-arc-completion`: 0 instances (designed for 0017). On track.

---

## C3-S2 — 2026-04-21 — the-witnesses — 0016-the-nave-congregation

### I-C3-S2-01 — Cross-session craft-witness chain

**Dimension:** Atmospheric Landing (cross: Engagement)
**What happened:** Maret's craft-witness was seeded in C3-S1 Scene 5 (unnamed congregation member's stone-turning resonating with her breath-work). She held the understanding silently through the night between sessions. It activated in C3-S2 Scene 2.2's closing silence — two minutes of collective silence after the morning rite ended — when she performed her three breaths in the space the rite had just occupied. *"After the silence ends, she performs her three breaths in the same space."* (Scene 2.2)
**Why the rubric did not anticipate it:** v1.4's multi-scene silent-reception chain was documented for intra-session chains (3+ scenes within a session). This is a cross-session chain: seeded S1 → held through the night → fired S2. The cross-session variant is longer and more complete than any intra-session instance documented. Craft-witness can run across a session boundary while remaining silent.
**Scope:** Universal. Craft-witness is not session-bounded; the resonance can develop across a session break.
**Status:** promoted-to-style (verbal-documentation-arc, craft-witness update)

---

### I-C3-S2-02 — Heuristic-inversion as arc-activation

**Dimension:** Character Agency (cross: Surprise)
**What happened:** Calla's second heuristic is *"preserve access to information — no actions that close off dialogue."* In Scene 2.4, she gave the correct rite sequence to the imperfect practitioners who asked *"Is that right?"*. She gave information away rather than holding it. *"The verse comes third. The sharing comes second."* The heuristic inverted: preserving access to correct knowledge required transmitting it to those who lacked it.
**Why the rubric did not anticipate it:** Character agency anchors cover heuristic-driven decisions. The novel form is a heuristic producing its inverse as its most faithful fulfillment. The PC's core drive (preserve access to information) created an obligation to share it — the preservation happened through transmission, not retention. The arc fired from fulfilling the heuristic correctly, not from violating it.
**Scope:** Universal (any PC with an information-preservation drive facing an information-deficit in another party).
**Status:** promoted-to-style (verbal-documentation-arc)

---

### I-C3-S2-03 — Arc-completion unlocks information beyond designed scope

**Dimension:** Atmospheric Landing (cross: Module Fidelity)
**What happened:** Veth's arc-completion fired (*"I don't know if I am doing it right. I do it anyway."*). Then, without prompting, Veth added: *"The elder in the Transept was there the night she performed the ritual. I know what was passed down. He knows what actually happened. They are not the same."* This information was in his Information Readiness Condition but NOT in his Arc-Completion section. The arc-completion unlocked the readiness condition as a side effect.
**Why the rubric did not anticipate it:** Module Fidelity and Atmospheric Landing both assume arc-completion fires exactly what was designed. This session showed that an NPC who has just said something vulnerable spontaneously provides additional information — the emotional opening of the arc creates space for information transfer that was technically separate in the design. The arc-completion and the information readiness condition are not always independent.
**Scope:** Universal. When arc-completion fires for an information-holder NPC, their information readiness condition should be checked immediately — the arc may have satisfied it.
**Status:** promoted-to-style (npc-arc-completion). npc-architect update: explicitly link arc-completion to information readiness conditions in NPC files.

---

### I-C3-S2-04 — Verbal documentation-arc evolution: framework-failure → gap-identification

**Dimension:** Atmospheric Landing (cross: Character Agency)
**What happened:** In C3-S1, Calla's verbal documentation-arc fired from framework failure (Insight fumble — she could not categorize the shrine arrangements at all). In C3-S2, the same arc evolved: she recognized the imperfect rite's wrong sequence at exactly DC 13 — she succeeded at identifying a *failure* rather than naming a *thing*. *"The verse comes third. The sharing comes second."* She knows the correct form well enough to identify its absence. The arc shifted from "cannot categorize" to "can identify the gap between correct and imperfect."
**Why the rubric did not anticipate it:** v1.7's framework-failure arc-activation covers the first stage (arc fires from failure). This innovation documents the arc's second stage: the PC develops vocabulary for the gap, not the thing itself. Documentation-arc arcs through stages — the progression from "no vocabulary" to "vocabulary for the absence" is the arc's development, and it is not captured by the 7+ band anchor.
**Scope:** Universal for archivist-type PCs. Documentation-arcs have developmental stages: (1) cannot categorize → (2) can identify the gap → (3) can name the thing. The arc is complete at stage 3.
**Status:** promoted-to-style (verbal-documentation-arc)

---

### C3-S2 Threshold Check

**Pathway A — Dimension trigger:**

New logged entries this session:
- Atmospheric Landing: I-C3-S2-01 (cross-session craft-witness chain), I-C3-S2-03 (arc-completion unlocks readiness conditions) = **2 entries**
- Character Agency: I-C3-S2-02 (heuristic inversion) = **1 entry**

Existing logged Atmospheric Landing entries: I-C3-S1-03 (craft-witness/unnamed NPC). Combined with I-C3-S2-01: 2 Atmospheric Landing entries share the same theme (craft-witness variants). These are expansions of the craft-witness player-style, not new rubric anchors. **Action: update craft-witness.md; no new amendment needed.**

**Pathway B — Cluster trigger:**

**CLUSTER 1 — NPC-arc-completion:** Mig (C3-S1) + Veth (C3-S2) + Gorret (C3-S2) = **3 instances across 2 sessions.**

```
PLAYER-STYLE PROPOSAL — npc-arc-completion
Constituent innovations:
  - Mig's arc-completion (C3-S1): stepped through the inner door without looking back — condition: party opened the door cooperatively
  - Veth's arc-completion (C3-S2): "I don't know if I am doing it right. I do it anyway." — condition: party asked what he was trying to understand
  - Gorret's arc-completion (C3-S2): "At least you say what you are." — condition: Dren gave an honest answer to his question
Definition: An NPC delivers their arc-completion moment by character logic (the conditions in their npc-architect file are met) rather than DM scripting. The NPC's arc closes because the party's behavior triggered the designed condition, not because the DM decided it was time.
Triggers: Any session where an NPC with a designed arc-completion condition has that condition met by party action.
Cross-applicability: Universal. Any adventure with npc-architect-designed NPCs can produce this style.
```

**Prompt to user:** *"NPC-arc-completion cluster: 3 instances across 2 sessions (Mig C3-S1, Veth C3-S2, Gorret C3-S2). Propose player-style entry 'npc-arc-completion'?"*

**CLUSTER 2 — verbal-documentation-arc:** 5 activations across 2 sessions (2 in C3-S1 + 3 in C3-S2).

```
PLAYER-STYLE PROPOSAL — verbal-documentation-arc
Constituent innovations:
  - I-C3-S1-01 (fumble-as-arc-activation): arc fires from framework failure
  - I-C3-S1-adopted (v1.7 constituent): arc fires at consequence, not cause
  - I-C3-S2-04 (gap-identification): arc evolves through stages
  - [2 additional activations in C3-S2 Scene 2.3, Scene 2.7]
Definition: A PC whose documentation practice is verbal (recitation, oral history, memory) encounters content that exceeds, breaks, or reveals gaps in their current vocabulary. The arc progresses through stages: (1) cannot categorize → (2) identifies the gap → (3) names the thing. Each stage is an arc beat. The arc completes when the PC speaks the thing aloud to someone who can receive it.
Triggers: Any session where the PC's oral-documentation practice encounters something it cannot hold.
Cross-applicability: Applicable to any PC with oral-history, chronicle, or memory-preservation as a primary practice. Distinct from sheet-deep-reader (general PC depth) and documentation-arc (which was originally written-documentation specific).
```

**Prompt to user:** *"verbal-documentation-arc cluster: 5 activations across 2 sessions. Propose player-style entry 'verbal-documentation-arc'?"*

---

### Campaign 3 running tallies (post-S2)

- `sheet-deep-reader`: 13 instances (S1: 6 + S2: 7) across 2 sessions.
- `craft-witness`: 2 instances (S1: 1 + S2: 1), session-invariant confirmed across 2 sessions.
- `verbal-documentation-arc`: **RATIFIED 2026-04-21.** 5 activations across 2 sessions. See `personas/player-styles/verbal-documentation-arc.md`.
- `npc-arc-completion`: **RATIFIED 2026-04-21.** 3 instances (Mig + Veth + Gorret) across 2 sessions. See `personas/player-styles/npc-arc-completion.md`.
- `bilateral-arc-completion`: 0 instances (designed for 0017). On track.

---

### Campaign 2 final tallies

- `sheet-deep-reader`: +4 (S07) = **29 total C2 instances across 7 sessions.**
- `craft-witness`: +1 (Orik stairs) = **6 C2 instances; session-invariant; never missed a session.**
- `act-without-announcement`: +2 (Thessaly attunement; opening sentence is its peak) = **11 C2 instances; 12 cross-campaign.**
- `bilateral-arc-completion`: 2 instances (S03, S05). Campaign structure confirmed.
- `NPC-arc-completion`: 5+ instances (C2). Campaign complete.

**Campaign 2 innovation total: 22 (3+4+4+4+4+3+4 across S01-S07).**
**Cross-campaign innovation total: 80+ (22 C2 + 58+ C1).**

---

## C3-S3 — 2026-04-21 — the-witnesses — 0017-the-bell-tower

### I-C3-S3-01 — Combat as precondition for arc reception

**Dimension:** Atmospheric Landing (cross: Character Agency, Surprise)
**What happened:** The bilateral arc was designed to fire through social engagement with Sharr's resentment. Calla fumbled Insight (5 vs 11); hesitation registered as refusal; combat began. The bilateral fired AFTER combat — when Sharr, at 3 HP, repeated his statement slower: *"She healed us. And then she left us to it."* The party had to survive the resentment as a physical fact before they could receive it as an emotional one. (Scene 3.3)
**Why the rubric did not anticipate it:** I-C3-S1-02 (v1.7) documents arcs firing at the consequence rather than the cause. This is a specific variant: the combat IS the consequence. The resentment required physical embodiment before it could be named. The arc's conditions were met by surviving the fight, not by avoiding it.
**Scope:** Universal. For any arc-completion designed around receiving a named grievance, a failed social read triggering combat may be the necessary precondition — not an obstacle.
**Status:** LOGGED.

---

### I-C3-S3-02 — Bilateral-arc-completion first-half confirmed

**Dimension:** Character Agency
**What happened:** The campaign spine designed the bilateral to fire in adventure 0017 (Session 3 of 7). It fired in Session 3. Research question answered: bilateral-arc-completion is achievable in the campaign's first half. Both PCs' conditions were met simultaneously: *"My sergeant's name was Aldis."* / *"My sister's name was Mira. I was also late."* (Scene 3.3)
**Why the rubric did not anticipate it:** The C3 research question was whether bilateral fires in the first half (vs. C2's second-half instances in S03/S05). Confirmed.
**Scope:** Universal. Bilateral-arc-completion is not session-number-dependent; it fires when the PC sheet conditions are met and the adventure creates the trigger.
**Status:** promoted-to-style (bilateral-arc-completion — first-half confirmed).

---

### C3-S3 Threshold Check

No new amendments proposed this session. I-C3-S3-01 reinforces v1.7 rather than extending it. I-C3-S3-02 confirms existing bilateral-arc-completion style.

---

### Campaign 3 running tallies (post-S3)

- `sheet-deep-reader`: 18 instances (S1: 6 + S2: 7 + S3: 5) across 3 sessions.
- `craft-witness`: 2 instances (S1, S2), session-invariant confirmed.
- `verbal-documentation-arc`: 6 activations (S1: 2, S2: 3, S3: 1) across 3 sessions.
- `npc-arc-completion`: 4 instances (Mig S1, Veth S2, Gorret S2, Sharr S3) across 3 sessions.
- `bilateral-arc-completion`: 1 instance (S3). First-half confirmed.

**C3 S3 innovations logged: 2. C3 total: 10 (4+4+2).**

---

## C3-S4 — 2026-04-21 — the-witnesses — 0018-the-transept-witness

### I-C3-S4-01 — Silence-as-arc-receipt

**Dimension:** Atmospheric Landing (cross: Character Agency)
**What happened:** Calla Fosse, whose verbal-documentation-arc player-style is defined by what she holds without speaking, received Morren's full 7-stage account without asking a single question. Morren's arc-completion fired. He said: *"She did not call it a miracle. She called it the right thing to do."* He looked at Calla. Calla held the account. She is in Stage 3's anteroom. The verbal-documentation-arc's completion will be speaking; its preparation was silence. (Scene 4.4)
**Why the rubric did not anticipate it:** Act-without-announcement (v1.5) covers behavioral consequences of prior namings — a PC acting differently in a later scene as a result of a naming. Silence-as-arc-receipt is distinct: the PC's primary mode of engagement (listening) IS the major act. The arc did not require speaking or action; it required presence and restraint. The PC's heuristic 1 (listen before speaking) reached its maximum expression and produced the arc's key condition. Not captured by any existing anchor.
**Scope:** Universal (any PC whose primary heuristic is listening or observation, receiving content that was designed for a listener).
**Status:** adopted (v1.8)

---

### I-C3-S4-02 — Object-resonance as independent parallel discovery

**Dimension:** Character Agency (cross: Surprise)
**What happened:** Renn connected his pact to Velantha's working through objects and sensation — the ritual focus's hum (once, for him specifically) and the Sacristy's old-ink smell (Perception 20, before Morren mentioned Aldric) — rather than through Morren's narrative account. He said: *"Someone has been writing in there. For a long time."* This was before Morren finished. He arrived at the same conclusion as the account through an independent path. (Scene 4.5)
**Why the rubric did not anticipate it:** Character Agency anchors cover heuristic-driven decisions and PC arc-completions. This is a new pattern: a PC reaching a narrative conclusion through sensory and object evidence before the narrative delivers it, and that independent arrival creating a different relationship to the information than reception-through-account would have. Renn's parallel (his pact / Velantha's working) is now personal knowledge, not received knowledge.
**Scope:** Universal (any PC with sensory class features or high Perception who engages with evidence before the session's primary information source delivers the same conclusion).
**Status:** LOGGED.

---

### C3-S4 Threshold Check

**Pathway A:** I-C3-S4-01 (Atmospheric Landing) + I-C3-S3-01 (Atmospheric Landing, logged) = 2 entries. **Triggers amendment proposal.**

Constituent innovations: I-C3-S3-01 (combat-as-precondition for arc reception) and I-C3-S4-01 (silence-as-arc-receipt). Theme: **arc-reception timing and modality** — arcs fire at specific physical and behavioral conditions rather than at the narrative trigger point designed by the module.

**AMENDMENT PROPOSAL — v1.7 → v1.8**
**Dimension:** Atmospheric Landing
**Constituent innovations:** I-C3-S3-01 (combat-as-precondition), I-C3-S4-01 (silence-as-receipt)
**Theme:** The conditions under which an arc fires — and what behavior produces the firing — may be physical, behavioral, or experiential rather than purely narrative.
**Proposed change (7+ band addition):**
> **v1.8 arc-activation modality anchor:** A score of 7+ additionally recognizes arc-activation through physical or behavioral modality — where the PC's state of engagement (surviving a combat, maintaining silence, being present without asking) is the firing condition rather than a narrative exchange or discovery. The arc fires because the PC was in the right relationship to the moment, not because they performed the right action. Rationale: C3-S3 (combat as precondition for bilateral); C3-S4 (silence as maximum listening, triggering NPC arc-completion). Both require the PC to be in a specific stance rather than to speak or act.

**Prompt to user:** *"2 Atmospheric Landing innovations this session cluster with I-C3-S3-01. Propose amendment v1.7 → v1.8: arc-activation modality anchor (7+ band). Adopt?"*

**Pathway B:** No new style proposals. I-C3-S4-02 is a single instance; needs 2+ sessions for cluster.

---

### Campaign 3 running tallies (post-S4)

- `sheet-deep-reader`: 22 instances across 4 sessions.
- `craft-witness`: 2 instances (session-invariant confirmed).
- `verbal-documentation-arc`: 8 activations across 4 sessions.
- `npc-arc-completion`: 5 instances across 4 sessions.
- `bilateral-arc-completion`: 1 instance.

**C3 S4 innovations logged: 2. C3 total: 12 (4+4+2+2).**

---

## C3-S5 — 2026-04-21 — the-witnesses — 0019-the-sacristy

### I-C3-S5-01 — Relic recognition through behavioral act (not identity)

**Dimension:** Atmospheric Landing (cross: Module Fidelity)
**What happened:** The dispensation letter's warmth failed for Maret in R4 (fumble, total 6 vs DC 12) and succeeded for Maret in R3 after she answered Aldric's question honestly — after she performed the act of stating her unauthorized practice. The relic recognized her not because of who she was but because of what she did: she told the truth about practicing without permission. *"She picked up the letter again. It was warm in her hands now."* (Scene 5.3)
**Why the rubric missed it:** Previous relic recognition in C3 was based on static properties (healer, practitioner, unauthorized worker). This session showed recognition as a dynamic consequence: not-recognized → performed the act → recognized. The relic's warmth was the arc's reaction moment, but it arrived contingent on behavioral change rather than identity disclosure.
**Scope:** Universal (any relic designed to recognize a category of person can instead recognize the moment of performing the category-defining act).
**Status:** LOGGED.

---

### C3-S5 Threshold Check

No new amendments. I-C3-S5-01 extends v1.8 (arc-activation modality) rather than triggering a new amendment. One instance; needs cluster.

---

### Campaign 3 running tallies (post-S5)

- : 26 instances (S1-S5).
- : 3 instances (S1, S2, S5 — Maret's third spotlight confirmed).
- : 9 activations (S1-S5).
- : 6 instances (Mig/Veth/Gorret/Sharr/Morren/Aldric).
- : 1 instance (S3).

**C3 S5 innovations logged: 1. C3 total: 13 (4+4+2+2+1).**


---

## C3-S6 — 2026-04-21 — the-witnesses — 0020-the-crypt

### I-C3-S6-01 — Peer recognition as disclosure catalyst

**Dimension:** Character Agency (cross: Atmospheric Landing)
**What happened:** Renn Ashkeld had been withholding his pact from the party for six sessions. In the Crypt, he said "She used something that wasn't prayer. I know what that costs." Velantha recognized what he was describing and asked: "What was yours?" He answered — to the full party, in three sentences. The disclosure was not a confession he chose to make; it was a response to being recognized by someone who had done the same category of thing and survived it long enough to ask. (Scene 6.2)
**Why the rubric missed it:** Act-without-announcement (v1.5) covers behavioral consequences of prior namings. Arc-activation modality (v1.8) covers behavioral stance as firing condition. Neither captures peer recognition as disclosure catalyst — where the PC's withholding ends not because they choose to speak but because they are correctly identified by someone who understands the category of act. The recognition creates the conditions; disclosure is the response to being seen.
**Scope:** Universal (any PC withholding information about an unauthorized act; encountering someone who has done the same act and recognizes the category produces disclosure as natural response).
**Status:** LOGGED.

---

### C3-S6 Threshold Check

I-C3-S6-01 is 1 new entry. I-C3-S4-02 (object-resonance as parallel discovery) was previously logged for Renn. These two entries both document Renn's pact parallel arc — one through objects (S4), one through peer recognition (S6). Two entries in Character Agency from the same PC arc across 3 sessions.

Cluster check: 2 Character Agency entries from the same thematic arc (Renn's pact as unauthorized-act parallel). Not yet 3 for a style promotion. Watch for 0021 (the finale may produce a third instance as the pact context becomes public knowledge).

---

### Campaign 3 running tallies (post-S6)

- sheet-deep-reader: 30 instances across 6 sessions.
- craft-witness: 4 instances (S1, S2, S5, S6) — session-invariant confirmed across entire campaign.
- verbal-documentation-arc: 10 activations; Stage 3 entered.
- npc-arc-completion: 7 instances across 6 sessions.
- bilateral-arc-completion: 1 instance (S3).

**C3 S6 innovations logged: 1. C3 total: 14 (4+4+2+2+1+1).**


---

## C3-S7 — 2026-04-21 — the-witnesses — 0021-the-keystone (FINALE)

### I-C3-S7-01 — Simultaneous NPC-arc-completion delivery through PC-authored account

**Dimension:** Atmospheric Landing (cross: Module Fidelity)
**What happened:** Calla Fosse's spoken account at the Keystone delivered two NPC arc-completion lines simultaneously through her synthesis: Morren's arc-completion line ("She did not call it a miracle. She called it the right thing to do." — S4) and Aldric's arc-completion line ("She never asked for a cathedral. She asked for medicine." — S5). Both lines appeared in the account because Calla had received both arcs and incorporated them into her synthesis. The account did not quote the NPCs; it synthesized their truths. The NPC arc-completions were delivered retroactively through the campaign's final PC speech.
**Why the rubric missed it:** Simultaneous arc-convergence (v1.6) covers multiple NPCs whose arcs fire simultaneously in one moment. This is a variant: previously-delivered NPC arc-completions were carried forward in the PC's synthesis and re-delivered through her voice. The completions had already fired; the account included them as evidence. The PC's speech became the transmission channel for the campaign's completed arc-completions.
**Scope:** Universal for campaigns with a PC-authored finale deliverable — the deliverable will naturally synthesize the NPC arc-completions that preceded it.
**Status:** LOGGED.

---

### I-C3-S7-02 — Mechanical failure as final affirmation

**Dimension:** Mechanical Fairness (cross: Character Agency, Surprise)
**What happened:** Calla's Persuasion check (total 7) failed to convince Doran of Route D. Calla's spoken account (RP 23) succeeded. The dice correctly said: the mechanical tool (Persuasion) was not sufficient for this task; the non-mechanical work (seven sessions of accumulation, synthesis, delivery) was. The game mechanics failed and the campaign succeeded simultaneously. The failure was not a setback; it was a confirmation that the campaign's actual resolution pathway was the correct one.
**Why the rubric missed it:** Mechanical Fairness measures whether dice were honest and DCs were calibrated. This innovation is about what happens when the dice are honest AND insufficient: the mechanical check fails correctly (Persuasion 7 genuinely cannot move a 30-year political decision), and the non-mechanical achievement succeeds correctly (a seven-session arc of accumulation genuinely can). The rubric doesn't capture the session where failing the mechanical check IS the narrative confirmation.
**Scope:** Universal for campaigns with PC-authored deliverables — the deliverable may succeed where mechanics fail.
**Status:** LOGGED.

---

### C3-S7 Threshold Check

I-C3-S7-01 and I-C3-S7-02 are logged. No amendment proposals needed — both reinforce existing anchors (v1.6 simultaneous convergence; v1.8 arc-activation modality) rather than extending them. The campaign is complete; amendments would apply to Campaign 4.

---

### Campaign 3 FINAL TALLIES

- sheet-deep-reader: ~34 instances across 7 sessions. Session-invariant. Fires in S1 with any party and never stops.
- craft-witness: 7 instances across 7 sessions. Session-invariant. Never missed. Confirmed for non-physical practice without hall-guard.
- verbal-documentation-arc: 11 activations across 7 sessions. Stage 3 COMPLETE (S7 — account spoken at Keystone). Three-stage arc confirmed: (1) cannot categorize, (2) identifies the gap, (3) names the thing.
- npc-arc-completion: 8 instances across 7 sessions. Session-invariant (at least one per session; some sessions multiple). Pipeline discipline confirmed: every designed NPC arc fired by character logic.
- bilateral-arc-completion: 2 beats (S3 naming + S7 second beat). Both completed. First-half confirmed.

**C3 TOTAL INNOVATIONS: 16 (4+4+2+2+1+1+2).**
**C3 CAMPAIGN COMPLETE.**

---

## C4-S1 — 2026-04-22 — the-relief — 0022-the-arrival-at-the-needle

### I-C4-S1-01 — Grief-mapped resource conservation *(adopted v1.9)*

**Dimension:** Atmospheric landing (cross: Character agency)
**What happened:** Scene 1.7 — *"She is satisfied with this in the particular way of a person who has been correct in a way that most people won't notice."* Sava used 0 spell slots in a Hard combat encounter. The log frames her conservation not as tactical discipline but as grief-rooted: Elara died while Sava was delayed; spending resources before they were needed would echo that failure pattern. The resource decision is mechanically identical to optimal play — but the motivation is the PC's grief-paragraph, not the tactical situation.
**Why the rubric did not anticipate it:** The rubric does not distinguish resource decisions made from tactical calculation vs. grief-pattern commitment. Both look identical in the dice log (0 slots spent). The difference is in *why* — and the why is character-sheet-deep, not situational. v1.8 covers behavioral-stance arc-activation (firing through state of engagement); this is the mechanical-resource variant: the PC's relationship to their own stats expresses grief.
**Scope:** Universal for campaigns where resource management is both tactical and character-grounded.
**Status:** logged

---

### I-C4-S1-02 — Independent-motivation convergence toward collective restraint *(adopted v1.9)*

**Dimension:** Character agency (cross: Surprise)
**What happened:** Scene 1.8 — *"No one reports Luca's statement to Asholt or Tomek."* Four PCs, four different motivation pathways (Davan: orders don't require reporting this; Sava: not a triage situation; Talis: this belongs to Luca; Caelith: filing doesn't require routing to command), arrive at the same non-action without coordination. The collective restraint is not a joint decision; it is four independent decisions that agree.
**Why the rubric did not anticipate it:** Character agency scores "PCs made choices that mattered" and "decisions came from character." This innovation adds a group-level variant: four individually-grounded non-actions converging to one collective outcome. The rubric has act-without-announcement (v1.5) for cross-session cross-character behavioral consequence; this is intra-session, parallel-motivation, within-group convergence toward restraint. The non-action IS the meaningful choice.
**Scope:** Universal for parties where each PC's heuristics independently produce the same response to a disclosure or situation.
**Status:** logged

---

### I-C4-S1-03 — Grief-analogue NPC recognition *(adopted v1.9)*

**Dimension:** Atmospheric landing
**What happened:** Scene 1.2 — *"Sava sees Maret Stave before she is introduced. A healer's station, organized to clinical standard."* Sava immediately recognizes Maret's situation (healer rationing supplies alone, not telling command) as matching her own grief (Elara — a healer who died while Sava was delayed, at a waystation Sava arrived at too late). No dice. No announcement. No reference to Elara. Sava addressed Maret as a peer and received the disclosure that Maret hadn't given anyone else. The recognition fired the scene.
**Why the rubric did not anticipate it:** The finder-vs-receiver anchor (v1.2) tracks who finds and who receives a beat. This innovation is different: the PC's own grief-paragraph is the recognition mechanism — she finds the NPC situation *because* she has the exact grief-shape to read it. The PC is simultaneously the finder (she spots the clinical suppression) and the receiver (the scene reverberates against Elara). The session log does not announce this; it is present in scene construction only.
**Scope:** Universal for campaigns where NPC situations mirror PC grief paragraphs — which, by design, they should.
**Status:** logged

---

### I-C4-S1-04 — Behavioral-stance trust-earning across multiple scenes *(adopted v1.9)*

**Dimension:** Character agency (cross: Module fidelity)
**What happened:** Scenes 1.4 → 1.5 → 1.6 → 1.7 — the token condition (earned at dawn, Scene 1.8) required a sustained pattern across four scenes: *took position without orders* → *held the wall* → *did not report afterward*. No single scene earned the token; the trust accumulated through the pattern. The party's heuristics independently produced this pattern without coordination or awareness of the token condition.
**Why the rubric did not anticipate it:** Character agency anchors score individual meaningful decisions. This innovation is about *sustained behavioral pattern* — trust earned not by one choice but by a sequence of non-choices maintained consistently. The v1.8 arc-activation-modality anchor (behavioral stance as arc condition) covers atmospheric landing specifically; this is the same mechanism applied to trust accumulation as the adventure's primary agency outcome. The "choice" is the absence of credit-seeking, maintained across four scenes.
**Scope:** Universal for adventures where trust is earned through pattern rather than event — which the Watch-Token system requires for all seven sessions.
**Status:** logged

---

### C4-S1 Threshold Check

**Pathway A (dimension trigger):**

Two dimension pairs hit the 2+ threshold from C4-S1 alone:

1. **Atmospheric landing:** I-C4-S1-01 + I-C4-S1-03 — both involve grief-paragraph situational resonance. Distinct from existing v1.2-v1.8 anchors (which cover finder/receiver, silent-reception chains, act-without-announcement, and behavioral-stance arc-activation). What's new: the PC's grief-paragraph firing as *recognition mechanism* (I-C4-S1-03) or *resource-decision motivator* (I-C4-S1-01) rather than as named statement or act.

2. **Character agency:** I-C4-S1-02 + I-C4-S1-04 — both involve meaningful inaction. What's new: a *pattern of non-action* (I-C4-S1-04) and *convergence of independent non-actions* (I-C4-S1-02) as the campaign's primary agency mode. The rubric scores individual decisions; these innovations are about the meaningful absence of a decision.

AMENDMENT PROPOSAL — v1.8 → v1.9 (two-dimension update):

**Atmospheric landing amendment:**
> **v1.9 grief-paragraph situational resonance anchor (new):** A score of 7+ additionally recognizes **grief-paragraph situational recognition** — a PC finding or reading an NPC situation correctly *because* their own grief-paragraph contains the exact pattern to recognize it. The recognition fires without announcement, dice, or reference to the grief source; it is present in scene construction only. When the PC's grief IS the recognition mechanism rather than the content of a speech or action, this counts as a silent atmospheric reception distinct from the discovery mechanic. Rationale: C4-S1 (Sava recognizing Maret's suppressed-healer-not-telling-command situation through Elara's death; also Sava's resource conservation motivated by grief rather than tactics). Both instances: grief-paragraph informing session behavior at a pre-narrative level.

**Character agency amendment:**
> **v1.9 sustained behavioral pattern anchor (new):** A score of 9+ additionally recognizes **sustained behavioral pattern as meaningful choice** — a sequence of non-actions or consistent behavioral stances across multiple scenes that produces a trust or agency outcome. This is distinct from a single meaningful decision: the "choice" is the maintenance of a pattern (not claiming credit, not reporting, not pressing) that produces a result no single scene could deliver. Score of 10 requires at least one such pattern per session. Rationale: C4-S1 (Tomek's token earned by four-scene sustained non-credit-seeking pattern); also C4-S1 (collective restraint on Luca's disclosure — four independent heuristics converging to the same non-action).

**Pathway B (player-style):**
C4-S1 is Session 1 of Campaign 4. No player-style proposals from a single session. Watch:
- Grief-analogue NPC recognition (I-C4-S1-01 + I-C4-S1-03): if this pattern appears in C4-S2+ with a different PC, propose a new style: `grief-mirror-reader`.
- Independent convergence toward restraint (I-C4-S1-02 + I-C4-S1-04): if this appears in C4-S2+, strengthen the act-without-announcement style definition or propose a collective variant.

**C4-S1 innovations logged: 4. All four adopted (v1.9). Rubric updated. Player-style proposals: 0 (need S2+).**

---

## C4-S2 — 2026-04-22 — the-relief — 0023-the-supply-run

### I-C4-S2-01 — Intra-session act-without-announcement *(adopted v1.12)*

**Dimension:** Atmospheric Landing (cross: Character agency)
**What happened:** Scene 2.7 — *"She puts the token in her belt pouch, beside her suture kit. No announcement."* Sava receives Maret's token — a named moment of garrison trust — and stores it beside her tools without showing it to the party, explaining it, or marking it as significant. The token is placed where things she uses daily go.
**Why the rubric did not anticipate it:** v1.5 act-without-announcement is defined as cross-session behavioral consequence without announcement — a prior session's naming event producing change in the next session. This is the same mechanism within a single session: a named-arc event (the token receipt) processed and expressed through action in the same scene. The v1.5 anchor requires cross-session temporal distance; this does not have it but produces the same quality of restraint and behavioral grounding.
**Scope:** Universal; particularly likely when a PC has a private-relationship dynamic (healer-to-healer, craftsperson-to-craftsperson) that the rest of the party is not party to.
**Status:** logged

---

### I-C4-S2-02 — Failure-as-tactical-reframe *(adopted v1.10)*

**Dimension:** Character agency (cross: Engagement, Surprise)
**What happened:** Scene 2.3 — Talis fails three consecutive Athletics checks (total 5, 10, 10 vs DC 12) attempting to climb to the upper ledge. Her response: *"I'll stay on the ground and cover the south approach."* She converts the mechanical failure into a deliberate tactical position at the choke point's north entrance and in the subsequent combat fires from exactly that position — with the effective result that she covered the escape route better than the ledge would have.
**Why the rubric did not anticipate it:** Character agency scores choices that matter; this choice was precipitated by mechanical failure, not initiative. The innovation is in the framing: a trained PC who cannot accomplish an athletics task reframes the failure as a tactical decision and finds a superior position. This is distinct from v1.7 framework-failure arc-activation (in which a failed CHECK is the arc beat itself) — here, the failed check produces a *repositioning*, not an arc beat. The agency is in converting a mechanical inadequacy into a character-competent outcome.
**Scope:** Universal for parties where a PC's class competency includes tactical assessment. Rangers, Rogues, Fighters with combat positioning will produce this pattern when a terrain obstacle blocks their preferred approach.
**Status:** logged

---

### C4-S2 Threshold Check

**Pathway A (dimension triggers):**
- Atmospheric Landing: I-C4-S2-01 (intra-session act-without-announcement). Combined with prior Atmospheric Landing logged entries from C4-S1 (I-C4-S1-01, I-C4-S1-03 — both adopted v1.9): no new amendment needed. The v1.9 anchor already covers grief-paragraph resonance; I-C4-S2-01 is a variant of v1.5 (act-without-announcement), not a new dimension.
- Character Agency: I-C4-S2-02. Single entry in this dimension from C4-S2. Not a 2+ trigger.
- No amendment proposals from C4-S2.

**Pathway B (player-style emergence):**
NPC-arc-completion cluster: C4 now has **2 instances across 2 sessions** (Tomek S1, Maret S2). The third instance threshold (3+ across ≥2 sessions) is NOT yet met from C4 alone. However, the npc-arc-completion style was already ratified in C3. C4 provides additional confirmation.

No new player-style proposals from C4-S2 alone. Watch for:
- I-C4-S2-01 (intra-session act-without-announcement) + any future intra-session instance from a different PC → could seed a `within-session-restraint` player-style variant

**C4-S2 innovations logged: 2. No new amendment proposals. No new style proposals.**

---

## C4-S3 — 2026-04-22 — the-relief — 0024-the-saboteur

### I-C4-S3-01 — Combat-end through naming rather than damage *(adopted v1.10)*

**Dimension:** Character Agency (cross: Atmospheric Landing)
**What happened:** Scene 3.3 — Davan says *"We found the letter. We know about Varduin. We know about your mother. We know you didn't want to do this."* Wil stops moving. Combat ends. Two rounds, 0 party damage, Wil alive at 12/18 HP. Wil's dual stop-condition (escape fails AND coercion named) fired simultaneously. Davan chose the statement over continued damage when Wil was at 12/18 HP and grappled.
**Why the rubric did not anticipate it:** Character Agency 10-band anchors on "the choice was correct per character sheet, not per optimal play." This is that — but it is also a new TYPE: a combat-resolution mechanic replaced by a speech act. The naming IS the mechanical resolution. Not act-without-announcement (cross-session behavioral consequence without speech). Not sustained behavioral pattern (multi-scene inaction). This is active combat-end through naming: one specific sentence, at the correct moment, from the correct PC. Different from C2-S03's Mira faction-pivot (Route D offer as combat-adjacent), which was pre-combat. This is mid-combat, Round 2, with a live enemy at 12 HP.
**Scope:** Universal — but the Tactician's question applies: does it require dominant tactical position (Wil was grappled, backup in the room)? If yes, it is conditional; if it fires from non-dominant positions, it is a new universal type.
**Status:** logged

---

### I-C4-S3-02 — Portent voiced before firing *(adopted v1.11)*

**Dimension:** Mechanical Fairness (cross: Surprise)
**What happened:** Scene 3.3 — Caelith holds his action and says *"I see this coming"* before the Portent fires. He is holding the die. He announces the preparation before the deployment. When Wil's escape would succeed (natural 15+3=18), Portent [7] replaces it (total 10 < DC 14). The mechanic had been carried for three sessions; this is the first time it has a voice in the fiction.
**Why the rubric did not anticipate it:** Mechanical Fairness at 9+ requires mechanics that compound narratively. The v1.4 cross-character compound (Portent on another PC's roll, framed in-voice as gift) was ratified from Portent-as-benediction (Kessa to Grom). This is different: the same mechanic is announced in-voice BEFORE deployment against an enemy roll, giving it fiction-layer framing for the first time. The announcement makes the Portent visible as a character-specific act rather than a mechanical substitution. Makes the mechanic accessible; gives three sessions of carry-forward a narrative payoff. Possible rubric anchor for future cross-character Portent (v1.4 compound path): if Caelith in-voices a Portent gift to another PC in S4, the compound fires.
**Scope:** Universal for Divination Wizards. Requires a player willing to frame the mechanic in fiction before the roll, not after.
**Status:** logged

---

### C4-S3 Threshold Check

**Pathway A (dimension trigger — 2+ logged, non-adopted, in same dimension):**

Scanning across C4-S1 through C4-S3, logged entries only (adopted entries excluded):

| Dimension | Logged innovations | Trigger? |
|---|---|---|
| Character Agency | I-C4-S2-02 (failure-as-tactical-reframe) + I-C4-S3-01 (combat-end-through-naming) | **YES (2)** |
| Atmospheric Landing | I-C4-S2-01 (intra-session act-without-announcement) + I-C4-S3-01 (combat-end-through-naming, cross-tagged) | **YES (2)** |
| Mechanical Fairness | I-C4-S3-02 (Portent voiced before firing) | no (1 only) |
| Surprise | I-C4-S3-02 (Portent voiced, cross-tagged) | no (1 only) |

**Character Agency trigger fires.** Two logged innovations share a theme: converting a mechanical situation (failed check; tactical dominance) into a character-driven behavioral choice that produces a superior outcome. I-C4-S2-02 (failure-as-tactical-reframe: failed Athletics → deliberate repositioning) and I-C4-S3-01 (combat-end-through-naming: dominant position + character-correct speech → stops combat) are both instances where the PC's character register produces an outcome the module did not design and the dice did not require.

**Atmospheric Landing trigger fires.** Two logged innovations share a theme: named moments processed in the same scene through restraint rather than announcement. I-C4-S2-01 (Sava receives Maret token and stores it without showing the party — intra-session act-without-announcement) and I-C4-S3-01 (Davan names the coercion: a speech act that IS the resolution, unannounced to the party as a strategic choice).

**AMENDMENT PROPOSAL — v1.9 → v1.10 candidate**

**Dimension:** Character Agency
**Constituent innovations:** I-C4-S2-02 (failure-as-tactical-reframe), I-C4-S3-01 (combat-end-through-naming)
**Theme:** The PC's character register produces an outcome no module design and no dice outcome required. In I-C4-S2-02, the failed check is reframed into a superior position. In I-C4-S3-01, the dominant position is resolved through a speech act rather than through damage. Both innovations: the PC acts from their character sheet's register in a way that converts a mechanical situation into a character-authored outcome.

**Proposed rubric anchor addition (at the 10 band of Character Agency):**
> A score of 10 additionally recognizes **character-register conversion** — a PC converting a mechanical situation (failed check, tactical dominance, NPC vulnerability) into a character-authored outcome that the dice did not require and the module did not design. The PC's specific register (Fighter's honor-accounting; Ranger's tactical reframe; Wizard's institutional analysis) IS the resolution mechanism. The conversion must be traceable to the PC's character sheet, not to tactical calculation.

**Prompt:** *"Character Agency has 2 logged innovations in C4 (failure-as-tactical-reframe, combat-end-through-naming). Amendment proposal v1.9 → v1.10: character-register conversion anchor at the 10 band. Adopt?"*

**Pathway B (player-style emergence):**

npc-arc-completion cluster: C4 now has **3 instances across 3 sessions** (Tomek S1, Maret S2, Hessa S3). **Cluster threshold met.** The ratified style fires universally. No new promotion needed — the style is already ratified. C4 provides continued confirmation evidence.

Watch continuing:
- I-C4-S3-02 (Portent voiced before firing): if Caelith voices a Portent for another PC in S4 (cross-character compound path), this pairs with the v1.4 Portent-as-benediction cluster (I-S03-03, I-S04-01) for potential compound promotion.
- I-C4-S2-02 + I-C4-S3-01 (character-register-conversion): amendment proposal above. If adopted, both entries move to adopted status.

**C4-S3 innovations logged: 2. Amendment proposal pending: v1.9 → v1.10 (Character Agency 10-band character-register-conversion anchor). NPC-arc-completion cluster confirmed universal across C4.**

---

### I-C4-S4-01 — Cross-character Portent voiced as foreknowledge to named PC

**Dimension:** Mechanical Fairness (cross: Atmospheric Landing)
**What happened:** C4-S4 Scene 02, Round 2 — Caelith says *"Davan. I see what he does next."* directly to Davan before deploying Portent [6] to replace the enemy sergeant's Dex save. This is the second instance of Portent-voiced-before-firing (first: I-C4-S3-02), but with a key distinction: it is voiced TO a specific named PC, not to the room. The Portent becomes cross-character not just mechanically (replacing an enemy roll that benefits the party) but fictionally (Caelith is sharing his foreknowledge with Davan, not announcing it publicly). The mechanic functions as a gift of sight rather than a mechanical substitution.
**Why the rubric did not anticipate it:** I-C4-S3-02 captured "voiced before firing." This captures the additional layer of *directed foreknowledge* — the Portent as something Caelith gives to a specific person, not broadcasts. The Divination Wizard's class fantasy is that they see what others cannot; directing that foreknowledge to a named ally is the fiction-layer completion of the mechanic. Two instances in consecutive sessions, different but related. Amendment proposal threshold met.
**Scope:** Universal for Divination Wizards in party-combat contexts. Requires a player willing to direct the foreknowledge to a specific ally rather than announce it to the table.
**Status:** adopted (v1.11)

---

### I-C4-S4-02 — Grief-paragraph cover-retreat tactical decision

**Dimension:** Atmospheric Landing (cross: Character Agency)
**What happened:** C4-S4 Scene 02, Round 3 — Talis absorbs Soldier E's hit (7 damage) deliberately to access a better attack line — getting inside his guard for a close-range shortbow shot. Her Colossus Slayer fires because she is now inside his reach and he has already been damaged. The decision is her cover-retreat signature move applied to offense: she positions last, covers retreat, and accepts damage to protect her attack angle. The grief-paragraph parallel: Asha died because Talis was twenty-six feet ahead when the ambush hit. Talis now positions herself to absorb what she cannot prevent, rather than be ahead of it.
**Why the rubric did not anticipate it:** v1.9 grief-paragraph resource expression (spending/conserving HP motivated by grief-pattern commitment) captures this conceptually, but the previous instance (Sava conserving spell slots for Elara) was about restraint. This is about *spending* HP as grief-pattern expression — taking the hit because the grief-pattern says you stand in front of what's coming, not behind it. The distinction: resource expression can be conservative (hold back) or sacrificial (absorb forward). Sacrificial grief-pattern resource expression is a distinct form.
**Scope:** Applies to any PC whose grief-paragraph involves standing between something and a threat. Requires a player who lets tactical decisions be shaped by grief-pattern rather than optimal play.
**Status:** logged

---

### C4-S4 Threshold Check

**Pathway A (dimension trigger):**

| Dimension | Logged innovations (non-adopted) | Trigger? |
|---|---|---|
| Mechanical Fairness | I-C4-S4-01 (directed Portent foreknowledge) — paired with I-C4-S3-02 (Portent voiced before firing) | **YES (2)** |
| Atmospheric Landing | I-C4-S4-02 (grief-paragraph absorb-forward) | 1 only |
| Character Agency | I-C4-S2-02 + I-C4-S3-01 → adopted as v1.10 | adopted |

**Mechanical Fairness trigger fires.** Amendment proposal: v1.10 → v1.11. Constituent: I-C4-S3-02 + I-C4-S4-01. Theme: Portent voiced to a named PC before firing, functioning as directed foreknowledge rather than mechanical substitution. Proposed anchor: Mechanical Fairness 10-band expansion — Portent deployed as directed foreknowledge to a named PC (voiced before firing, addressed to that PC) counts as cross-character compound meeting the v1.4 standard.

**Pathway B (player-style emergence):**
NPC-arc-completion cluster: C4 now has 4 instances (Tomek S1, Maret S2, Hessa S3, Dene S4). Confirmed universal. No new promotion needed.

**C4-S4 innovations logged: 2. Amendment proposal pending: v1.10 → v1.11 (Mechanical Fairness — Portent-as-directed-foreknowledge). NPC-arc-completion cluster: 4 confirmed instances in C4.**

---

### I-C4-S5-01 — Act-without-announcement completing S4 silent-reception beat

**Dimension:** Atmospheric Landing
**What happened:** C4-S5, post-combat return — Talis passes through the courtyard and says one sentence to the older girl from S4: *"She's been doing this a long time."* In S4, Talis had silently recognized the older-girl-with-child configuration as an exact mirror of her grief-paragraph (being responsible for something smaller than you, being the last thing between a threat and someone who cannot protect themselves). She did not speak in S4. She speaks in S5 — not an announcement, not an explanation, one factual sentence. The S4 silent reception (Asha's cord, the configuration) drives a S5 verbal act without announcement, declaration, or scene structure.
**Why the rubric did not anticipate it:** v1.5 act-without-announcement captures cross-session behavioral consequence. This instance adds a refinement: the cross-session consequence is a *verbal* act (a single sentence) rather than a behavioral stance (Thera cutting bread, Sera's hold-space). The verbal act is as minimal as a behavioral stance — it does not announce itself — but it IS a statement. This is a new modality of act-without-announcement: the single-sentence recognition.
**Scope:** Universal for PCs with grief-paragraphs that contain pattern-recognition components. Requires a player willing to let the recognition speak once, minimally, without elaboration.
**Status:** logged

---

### I-C4-S5-02 — Wizard-register as resolution mechanism (non-combat)

**Dimension:** Character Agency (cross: Atmospheric Landing)
**What happened:** C4-S5, Scene 05 — Caelith says "What did you need to know?" to Luca. This is the Divination Wizard's character register applied as the resolution mechanism of a social situation — not a spell, not an Insight check, not a tactical assessment. The knowledge-gap identification heuristic (the Wizard's core operating mode: what information gap is driving this behavior?) is the question that fires Luca's token. The question could not have come from a Fighter, a Ranger, or a Cleric; it is specifically and only the Wizard's register.
**Why the rubric did not anticipate it:** v1.10 character-register-conversion captures this conceptually (ratified from Davan's S3 combat-end and Talis's S2 terrain-reframe). But both prior instances were in combat or tactical contexts. This is the first instance in a pure conversation — the character's analytical register applied to an emotional/social situation to produce the arc-completion condition. The pattern confirms that character-register-conversion is not restricted to mechanical situations; it applies to any situation where the PC's specific register IS the resolution mechanism.
**Scope:** Universal for analytical/institutional PCs (Wizards, Loremasters, institutional investigators) in conversation-heavy sessions.
**Status:** logged

---

### C4-S5 Threshold Check

**Pathway A:** No new dimension trigger fires. Both I-C4-S5-01 and I-C4-S5-02 are single instances in their respective dimensions (already-adopted). No amendment proposal pending.

**Pathway B (player-style emergence):**
- Act-without-announcement cluster: I-S07-02 (Thera's bread), I-C2-S01-02 (Sera hold-space), I-C4-S5-01 (Talis one-line to older girl) — three cross-campaign instances of act-without-announcement now confirmed universal. v1.5 anchor validated across three campaigns.
- Wizard-register-as-resolution: I-C4-S5-02 is a second instance of non-combat character-register-conversion (first: I-C4-S3-01 combat context; now I-C4-S5-02 conversation context). The pattern is generalizing from combat to all contexts. No player-style proposal yet — but watch for a third instance.

**C4-S5 innovations logged: 2. No new amendment proposals. Campaign trajectory: 70→72→73→74→75. All five advisory. S6 binding.**

---

### I-C4-S6-01 — Ranger adapts to melee after fumbled range shot

**Dimension:** Character Agency (cross: Atmospheric Landing)
**What happened:** C4-S6, assault Round 3 — Talis fumbles her shortbow shot (total 6) and, rather than retreating or finding cover (optimal Ranger behavior), she draws her shortsword and gets into the breach beside Davan. This is the first time in the campaign she has drawn a melee weapon. The grief-paragraph parallel: she has been positioning herself between things and threats (cover-retreat signature move) for six sessions; when her optimal-range capability fails, she doesn't retreat from the threat — she moves closer.
**Why the rubric did not anticipate it:** v1.10 character-register-conversion captures this type of mechanic-to-character conversion. But this instance adds a new modality: the failed roll drives the PC *toward* the threat rather than *away* from it. The fumble IS the trigger for the register-conversion; the Ranger's cover-retreat heuristic (stand between the party and the threat) overrides the tactical-optimal response (fall back to range). The dice failure became a character revelation.
**Scope:** Universal for PCs with grief-paragraphs structured around standing between threats and people they protect.
**Status:** logged

---

### I-C4-S6-02 — Six-session silent-reception arc convergence in a margin note

**Dimension:** Atmospheric Landing
**What happened:** C4-S6, Scene 02 — Caelith reads his own grey-blue-ink annotations accumulated across all six sessions and writes one sentence in the margin: *"She is not waiting to win. She is waiting to be heard."* This closes an annotation thread that began in C4-S1 (noted as a grey-blue annotation seed in that session's handoff). The silent-reception chain spans six sessions: Caelith observed, documented, cross-referenced, and the accumulated reception converged in one sentence in the quiet before the assault. No dice. No conversation partner. The annotation speaks to itself.
**Why the rubric did not anticipate it:** v1.4 multi-scene silent-reception chain (PC holds un-articulated understanding across 3+ scenes) is the correct category, but the documented instances (Grom's S04 silent Reorx-judgment, Thera's bread, Sera's hold-space) all had 3-session spans. This is a six-session span — the longest in any campaign. The innovation is not a new type but an extended instance that validates the upper bound of the mechanic. It also demonstrates that the silent-reception chain can operate entirely through text (annotation, not internal monologue) — a new modality for the mechanic.
**Scope:** Universal for analytical/documentation-oriented PCs over multi-session campaigns.
**Status:** logged

---

### C4-S6 Threshold Check

**Pathway A:** I-C4-S6-01 and I-C4-S6-02 are single instances in dimensions that already have anchors. No new amendment trigger.

**Pathway B:** Silent-reception chain instances across campaigns: I-S04-02 (Grom), I-C4-S5-01 (Talis one-line), I-C4-S6-02 (Caelith margin note) — three instances across three campaigns. **Player-style cluster threshold met.** Propose player-style: `documentary-witness` — a PC whose receipt of atmospheric content is expressed primarily through external documentation (writing, annotation, cataloging) rather than internal monologue or action-change. The documentation IS the reception; it accumulates across sessions until a single line of text names the pattern.

**C4-S6 innovations logged: 2. Player-style proposal: documentary-witness (pending). PASS threshold hit: 76/80. Campaign trajectory: 70→72→73→74→75→76.**

---

### I-C4-S7-01 — Analytical-observer failure as limit-documentation

**Dimension:** Atmospheric Landing (cross: Surprise)
**What happened:** C4-S7, Scene 03 — Caelith rolls Insight on Saren and fails (total 4). Rather than treating the failure as a non-event, he writes "unable to categorize" in his notebook. This is the first entry in six sessions of documentation that he could not file. The framework-failure (v1.7) fires in reverse: not because the PC lacks vocabulary for an NPC, but because the analytical observer correctly identifies the limit of their own framework and documents the limit rather than papering over it.
**Why the rubric did not anticipate it:** v1.7 framework-failure arc-activation describes a PC whose framework breaks and the break IS the emotional landing. This instance adds a new modality: the PC whose framework is analytical-documentation encounters a limit and files the limit as data. The failure is archived, not denied. The documentation-practice (Caelith's grey-blue annotations) has its final entry as a failed entry. This is the completion of the documentary-witness pattern proposed for player-style promotion.
**Status:** logged. Constitutes the third cross-campaign instance of the documentary-witness pattern (I-C4-S1 first grey-blue annotation; I-C4-S6-02 six-session convergence; I-C4-S7-01 failure-as-limit-documentation). **Player-style promotion threshold met: propose `documentary-witness`.**

---

### I-C4-S7-02 — Grief-paragraph deployed as deliberate resource at the table

**Dimension:** Character Agency (cross: Atmospheric Landing)
**What happened:** C4-S7, Scene 04 — Davan names Orel at the parley table. The grief-paragraph has been present in his character sheet since the campaign began. It has not been accidentally triggered by a parallel situation (the usual grief-paragraph activation pattern). It has not been surfaced in a quiet conversation. It has been deliberately deployed at the moment of maximum utility: the table where both sides need to understand that the person speaking is not outside the letter-vs-people tension, but inside it. He uses his grief as a resource — something he owns and can spend.
**Why the rubric did not anticipate it:** v1.9 grief-paragraph situational recognition (PC reads NPC situation through own grief-pattern) and grief-paragraph resource expression (mechanical decision motivated by grief-pattern) both capture unconscious grief-activation. This is the first instance of *deliberate* grief-deployment — the PC choosing when to spend their grief rather than having it triggered. The distinction: unconscious activation is something that happens to the PC; deliberate deployment is something the PC does. The grief-paragraph becomes a speech-act resource rather than a passive pattern-recognition tool.
**Status:** logged. This is a potential new category: grief-paragraph-as-deployable-resource (distinct from grief-paragraph situational recognition and grief-paragraph resource expression, both of which are pattern-activation rather than deliberate deployment).

---

### C4-S7 Threshold Check

**Pathway A:** I-C4-S7-02 is a new sub-type of grief-paragraph expression. No dimension trigger (the constituent innovations are v1.9-adjacent, not v1.9-conflicts). No new amendment proposal.

**Pathway B (player-style promotion):**
Documentary-witness cluster: I-C4-S1 (first grey-blue annotation), I-C4-S6-02 (six-session convergence), I-C4-S7-01 (failure-as-limit-documentation) — three instances across seven sessions of one campaign. **Promotion threshold met.** Propose `personas/player-styles/documentary-witness.md`: a PC whose atmospheric reception is expressed through documentation that accumulates across sessions, whose practice converges in a moment of naming the pattern, whose final entry is the thing they could not file.

**CAMPAIGN COMPLETE. Final trajectory: 70→72→73→74→75→76→78. 16 innovations logged. Route E. 7 arc-completions. Documentary-witness player-style proposed.**

---

## Campaign 5 — The Silken Ledger (2026-04-22)

### I-C5-S1-01 — C5-S1 — the-guild — 0029-the-first-contract

**Technique:** Pre-session parallel maintenance as party-dynamic-establishment
**Dimension:** Atmospheric Landing (cross: Engagement)
**What happened:** Darro named his picks (Tension wrench. Hook. Short hook. Diamond.) while Tessaly opened her ledger to a clean entry header — simultaneously, neither addressing the other. Party dynamic established in three minutes before the brief began.
**Why the rubric did not anticipate it:** No anchor captures party-establishment value of parallel loyalty-object rituals firing simultaneously pre-briefing from automatic professional behavior.
**Status:** logged. Threshold: 1/2 for new player-style (party-formation-through-parallel-maintenance).

---

### I-C5-S1-02 — C5-S1 — the-guild — 0029-the-first-contract

**Technique:** Scope-refusal as professional code execution
**Dimension:** Character Agency
**What happened:** Cael refused Bessa's drawer mention ("not the job") without consultation. The code eliminated the option before it became a temptation. The absence of outcome IS the outcome.
**Why the rubric did not anticipate it:** v1.10 captures conversion of mechanical situations. This is narrower: the code actively prevents the conversion from occurring. Refusal IS the character-authored outcome.
**Status:** logged. Threshold: 1/2 for code-refusal-as-conversion anchor.

---

### I-C5-S2-01 — C5-S2 — the-guild — 0030-the-informant

**Technique:** Insight-as-preparation enabling Words of Terror resolution
**Dimension:** Character Agency (cross: Mechanical Fairness)
**What happened:** Mira rolled Insight 21 on the officer, read floor-contact aversion from boots on cot frame, then deployed Words of Terror naming "rats." The naming was a derived conclusion from prior observation — Whispers-as-understanding, matching her professional code distinction (understanding vs manipulation).
**Why the rubric did not anticipate it:** No anchor captures the Insight-read-then-class-feature-named chain where feature content is derived from Insight result. Sheet-deep-reader through two-step mechanical chain.
**Status:** logged. Threshold: 1/2 for sheet-deep-reader-through-class-feature-chain.

---

### I-C5-S3-01 — C5-S3 — the-guild — 0031-the-double-entry

**Technique:** PC-authored deliverable accumulation as cross-session act-without-announcement
**Dimension:** Atmospheric Landing (cross: Module Fidelity)
**What happened:** Mira added to the false dossier framework in S3-S6 without disclosure. Six sessions. Announced in S7: "I have it." The accumulation was the act; the deployment was the announcement.
**Why the rubric did not anticipate it:** v1.5 captures cross-session consequence from a prior naming event. No prior naming event here. The PC accumulated toward a deliverable; the delivery was the announcement. Distinct sub-type.
**Status:** logged. Threshold: 1/2 for deliverable-accumulation-as-act-without-announcement.

---

### I-C5-S4-01 — C5-S4 — the-guild — 0032-the-burned-house

**Technique:** Cascading professional consequence from sheet-deep-reader evidence
**Dimension:** Character Agency
**What happened:** Tessaly's ledger investigation found that Pale knows her coding conventions. This was immediately translated into a forgery constraint (must diverge from historical register) without deliberation. Evidence produced constraint; constraint applied. Two character-register-conversions without deliberation between them.
**Why the rubric did not anticipate it:** v1.10 captures single conversion. This is cascading: a character-register conversion produces a second one as its immediate consequence. Chain is two conversions, no deliberation between.
**Status:** logged. Threshold: 1/2 for cascading-character-register-conversion anchor.

---

### I-C5-S5-01 — C5-S5 — the-guild — 0033-the-wrong-buyer

**Technique:** Simultaneous v1.5 and v1.12 from single act
**Dimension:** Atmospheric Landing
**What happened:** Cael's "We're not selling a name to the Watch" qualified simultaneously as v1.5 (cross-session: 15-year career pattern, no announcement) and v1.12 (intra-session: code statement received and expressed in the same scene). Both anchors fired from the same moment.
**Why the rubric did not anticipate it:** v1.5 and v1.12 described as temporally distinct. First confirmed instance of both firing simultaneously. The anchors are not mutually exclusive.
**Status:** logged. Threshold: 1/2 for compound-anchor (simultaneous multi-anchor atmospheric moment from single act).

---

### I-C5-S6-01 — C5-S6 — the-guild — 0034-the-ledger-audit

**Technique:** Self-forgery as professional cover (retroactive documentation in own hand)
**Dimension:** Character Agency (cross: Atmospheric Landing)
**What happened:** Tessaly forged a contemporaneous margin note in her own ledger — retroactive record of water-damage that had not happened — to cover the substitute's inconsistencies. Used her own documentary authority to create plausible deniability. Forging her own history while holding a code that says records are accurate.
**Why the rubric did not anticipate it:** v1.9 captures mechanical decisions motivated by grief-pattern. This is the professional-code equivalent: documentation decision that violates the spirit of the professional code while obeying its formal requirements. The tension visible in the beat before she wrote the date.
**Status:** logged. Distinct from forging another person's documents. PC forging own record while holding accuracy code.

---

### I-C5-S7-01 — C5-S7 — the-guild — 0035-the-final-job

**Technique:** Campaign-closing maintenance ritual (professional identity persists past final job)
**Dimension:** Atmospheric Landing
**What happened:** Darro performed his pick maintenance the morning after the campaign ended. Same order, same naming, same three minutes. No designed audience. The ritual persisted past narrative resolution — professional identity not contingent on the campaign continuing.
**Why the rubric did not anticipate it:** v1.5 captures cross-session behavioral consequence. This is temporal extension: behavior extends past campaign resolution. Professional-code equivalent of Thera cutting bread long-ways on the road home (C1-S7). Second confirmed instance in workshop history; both post-campaign-resolution, both private.
**Status:** logged. Threshold check: campaign-closing ritual 2/2 — promotion candidate for act-without-announcement sub-type.

---

### I-C5-S7-02 — C5-S7 — the-guild — 0035-the-final-job

**Technique:** Simultaneous four-PC loyalty-object closing acts
**Dimension:** Atmospheric Landing (cross: Engagement)
**What happened:** Campaign's final scene: Tessaly's ledger entry + satchel close; Cael's contract-touch adjusting terms; Mira's paper case (framework remains inside); Darro's pick count. Four simultaneous professional closures from four different instruments without coordination.
**Why the rubric did not anticipate it:** v1.6 captures simultaneous arc-convergence triggered by a naming act. This is the professional-code equivalent: conclusion trigger (campaign ending) rather than naming act. First instance of v1.6 form applied to professional instruments rather than emotional arcs.
**Status:** logged. v1.6 extended to professional-code convergence.

---

### C5 Campaign Threshold Check

**Pathway A:** I-C5-S1-02 + I-C5-S4-01 cluster in Character Agency (code-refusal + cascading-professional-consequence). 2+ in dimension. Propose v1.13 anchor: **professional-code cascade** — when a sheet-deep-reader decision immediately produces a second professional consequence without deliberation, the chain constitutes a character-register-conversion. Rationale: Cael drawer refusal (S1) and Tessaly convention-constraint discovery (S4).

**Pathway B:** No new player-style promotions. Sheet-deep-reader, craft-witness, act-without-announcement all validated as professionally-triggered (no-grief). RV1-RV4 confirmed.

**CAMPAIGN COMPLETE. Final trajectory: 70→72→73→74→75→76→77. 8 innovations logged. Route B. All 4 RV validations confirmed. Zero grief-triggered instances in 7 sessions.**

---

## Campaign 6 (C6) — Military Unit (Border Watch) — 2026-04-22

### I-C6-S1-01 — C6-S1 — the-unit — 0036-first-patrol
**Technique:** Journal-margin-as-reception (pre-column accumulation)
**Dimension:** Atmospheric Landing (cross: Character Agency)
**What happened:** Varet accumulated observations in the journal margin on Day 1 — correlations the column structure could not classify. The margin was designed for weather notes. It became the reception layer. Two layers in the same document: column (defended) and margin (accumulating).
**Status:** logged.

---

### I-C6-S1-02 — C6-S1 — the-unit — 0036-first-patrol
**Technique:** FUMBLE-as-micro-event (environmental consequence without DM intervention)
**Dimension:** Mechanical Fairness
**What happened:** Taris FUMBLE (d20=1) caused arrow to clip mule-post; mule shied; smugglers flinched but did not act. Dice-produced environmental ripple with downstream NPC behavior change. No DM design needed.
**Status:** logged.

---

### I-C6-S2-01 — C6-S2 — the-unit — 0037-the-cache
**Technique:** Ledger-via-position (craft-witness as spatial requirement, not roll)
**Dimension:** Module Fidelity (cross: Character Agency)
**What happened:** Hidden ledger required passive Perception 15. In S1 no PC was in-position. In S2 Taris entered the cache (player choice); passive fired. v1.3 fallback-b triggered by exploration as craft-witness.
**Status:** logged.

---

### I-C6-S2-02 — C6-S2 — the-unit — 0037-the-cache
**Technique:** Treatment-before-ask as NPC social key (professional discipline as persuasion bypass)
**Dimension:** Character Agency
**What happened:** Lenne treated Serrak before asking what happened. Professional practice order was the social key. No Persuasion roll required. Second instance of professional-practice-as-persuasion-bypass.
**Status:** logged.

---

### I-C6-S3-01 — C6-S3 — the-unit — 0038-the-missing-scout
**Technique:** v1.9 independent-motivation convergence without emotional content
**Dimension:** Character Agency
**What happened:** Four PCs independently arrived at order-defiance from four professional registers: route-bond (Taris), formation-obligation (Dorn), medical-consequence (Lenne), journal-authority (Varet). No coordination. No emotional content. First confirmed v1.9 form with zero emotional content.
**Status:** logged.

---

### I-C6-S3-02 — C6-S3 — the-unit — 0038-the-missing-scout
**Technique:** FUMBLE-as-rescue-pressure (dice as scene-designer for required tension)
**Dimension:** Mechanical Fairness (cross: Pacing)
**What happened:** Taris FUMBLE init (d20=1) put him last; Guard2 reached Brek. Created the rescue-race scenario requiring Dorn Brace. Threshold met: 2/2 FUMBLE-as-scene-designer.
**Status:** logged. Threshold 2/2 with I-C6-S1-02 — propose FUMBLE-as-collaborative-authorship anchor.

---

### I-C6-S4-01 — C6-S4 — the-unit — 0039-the-wrong-order
**Technique:** Documentary compound (two-PC documentary mechanic)
**Dimension:** Mechanical Fairness (cross: Character Agency)
**What happened:** Dorn named the legal basis (Clause 4 read aloud), Varet filed formal objection. Neither functions without the other. First confirmed documentary equivalent of v1.4 cross-character compound.
**Status:** logged.

---

### I-C6-S4-02 — C6-S4 — the-unit — 0039-the-wrong-order
**Technique:** Failed-social-as-character-register-redirect
**Dimension:** Character Agency (cross: Mechanical Fairness)
**What happened:** Varet Persuasion FAIL (7 vs DC15) stopped wrong register (managing-up). She pivoted to formal objection (documentary action). Dice denied wrong tool; character found right one. Second instance of failed-roll-as-better-outcome.
**Status:** logged.

---

### I-C6-S5-01 — C6-S5 — the-unit — 0040-the-names
**Technique:** Self-referential documentary-witness (journal fires its own arc-condition)
**Dimension:** Atmospheric Landing (cross: Character Agency)
**What happened:** Varet wrote "the arc fires" — applying her professional rule to herself. The journal contained the rule and applied the rule. The document became the mechanism of its own arc. First documented self-referential documentary arc-firing in workshop history.
**Status:** logged.

---

### I-C6-S5-02 — C6-S5 — the-unit — 0040-the-names
**Technique:** Recognition-triggered atmospheric beat
**Dimension:** Atmospheric Landing
**What happened:** "I have caught up" in journal margin acknowledging Arren was right. Not duty-triggered, not grief-triggered — recognition-triggered. First documented recognition-triggered emotion category in workshop history.
**Status:** logged. New emotion category candidate.

---

### I-C6-S6-01 — C6-S6 — the-unit — 0041-the-last-patrol
**Technique:** SpW-as-independent-compound (undesigned two-PC convergence)
**Dimension:** Mechanical Fairness (cross: Engagement)
**What happened:** Lenne Spiritual Weapon (independent attack) killed the Veteran while Dorn occupied it 4 rounds. Neither designed the convergence. Distinct from v1.4: undesigned convergence vs. intentional deployment.
**Status:** logged.

---

### I-C6-S6-02 — C6-S6 — the-unit — 0041-the-last-patrol
**Technique:** Consecutive-misses-as-character-expression
**Dimension:** Character Agency (cross: Atmospheric Landing)
**What happened:** Dorn missed Veteran 4 consecutive times (16 vs AC17 each). No tactic change. Professional obligation = presence, not success. Character showed more in 4 misses than 4 hits. Second instance of consecutive-failure-as-character-expression.
**Status:** logged.

---

### I-C6-S7-01 — C6-S7 — the-unit — 0042-the-reckoning
**Technique:** Journal-as-arc-mechanism (document IS the arc, not the record of the arc)
**Dimension:** Character Agency (cross: Atmospheric Landing, Module Fidelity)
**What happened:** The field journal was not a record of Varet's arc. It WAS the arc. Reading it delivered evidence and character simultaneously. The journal constituted the character. Strongest form of documentary-witness in workshop history. Distinct from C5 PC-authored deliverable (which was produced BY the arc; this IS the arc).
**Status:** logged.

---

### I-C6-S7-02 — C6-S7 — the-unit — 0042-the-reckoning
**Technique:** Standing-in-the-doorway (spatial-silent NPC arc-completion)
**Dimension:** Atmospheric Landing
**What happened:** Arren Vole walked into tribunal room, stood at door, said nothing, drew nothing. Derrath sat down. No roll. Twelve years as the argument expressed as a physical position. First documented spatial-silent NPC arc-completion.
**Status:** logged.

---

### I-C6-S7-03 — C6-S7 — the-unit — 0042-the-reckoning
**Technique:** Campaign-closing professional maintenance (all four PCs simultaneously)
**Dimension:** Atmospheric Landing
**What happened:** Taris folded map (will update tomorrow). Lenne wrote "cause now explained," closed log. Dorn read Clause 4 in bunk voice. Varet wrote final margin note, closed journal. Four PCs closing practices, not emotional arcs. Second campaign with this pattern.
**Status:** logged. Threshold 2/2 with I-C5-S7-01 — promote to act-without-announcement sub-type: maintenance-persists.

---

**C6 Campaign Threshold Checks:**
- FUMBLE-as-scene-designer (I-C6-S1-02 + I-C6-S3-02): 2+ instances — propose Mechanical Fairness anchor: FUMBLE-as-collaborative-authorship.
- maintenance-persists (I-C5-S7-01 + I-C6-S7-03): 2 campaigns — promote to act-without-announcement sub-type.
- recognition-triggered (I-C6-S5-02): 1 instance — watch C7.
- RV5 confirmed: depletion-amplification. RV6 confirmed: journal-as-arc. RV7 confirmed: duty-spine density. RV8 confirmed: document MORE effective than speech in institutional context.

**CAMPAIGN COMPLETE. Final trajectory: 70→72→74→75→76→77→78. 15 innovations logged. Route E. All RV5-RV8 confirmed. Zero grief-triggered instances across 7 sessions.**

---

## C7 — 2026-04-22 — the-strangers — 0043-0049

### I-C7-S1-01 — C7-S1 — the-strangers — 0043-the-roadblock
**Technique:** Passive-terrain-warning (warning stripped to operational minimum)
**Dimension:** Atmospheric Landing (cross: Character Agency)
**What happened:** Vess warns Brek about the fall line with two words ("Don't stand where you're standing") after spotting it silently in survey. She does not explain; she names the action required. The warning exists but is stripped to the operational minimum such that it functions more like a position-change than a disclosure.
**Why the rubric did not anticipate it:** This is a boundary case for act-without-announcement: the announcement exists but contains no emotional content, no reason, no relationship signal. It is purely functional. The rubric counts full silence as act-without-announcement; this is the minimum-speech form of the same phenomenon.
**Scope:** Universal.
**Status:** logged.

### I-C7-S1-02 — C7-S1 — the-strangers — 0043-the-roadblock
**Technique:** Documentation-blank-as-social-signal
**Dimension:** Atmospheric Landing
**What happened:** Sera writes "travelers encountered" with physical descriptions — not names — including a blank for Brek's destination. The blank is information: she noticed she did not have the name. She did not ask for it. The absence in the documentation is itself a finding.
**Why the rubric did not anticipate it:** The documentary-witness player style (proposed C4) documents presences. This instance documents an absence. The blank is the social-distance measure: what she could not write reveals what she did not ask for.
**Scope:** Universal (any documentary-witness PC can produce this).
**Status:** logged.

### I-C7-S3-01 — C7-S3 — the-strangers — 0045-the-refugees
**Technique:** Session-relationship-triggered arc-completion
**Dimension:** Atmospheric Landing (cross: Character Agency)
**What happened:** Elder Sorr arc-completion fired because Tam spent 30 minutes walking beside her without asking tactical questions. The attentiveness formed within the session (not from backstory). The arc fired from it. Proposed new trigger type: "session-relationship-triggered" — distinct from situational (no external event triggers it) and designed-relationship (no backstory connection).
**Why the rubric did not anticipate it:** Existing trigger types are situational (external event) and relationship-driven (accumulated across sessions). This is a third type: a relationship formed in a single session through behavioral stance, sufficient to trigger arc-completion.
**Scope:** Universal.
**Status:** logged. Threshold candidate: if confirmed 2+ instances, propose new trigger-type documentation standard.

### I-C7-S4-01 — C7-S4 — the-strangers — 0046-the-demand
**Technique:** Trigger-type transition (situational → relationship-driven, tracked by session number)
**Dimension:** Character Agency
**What happened:** Player-style trigger types shift cleanly from "situational" (S1-S3) to "relationship-driven" (S4-S7). The same player styles fire throughout. What changes is the trigger. The transition tracks session number and relationship development.
**Why the rubric did not anticipate it:** The rubric documents individual instances as situational or relationship-driven. It does not document the campaign-arc of trigger-type change — the fact that the same player styles will shift trigger types as sessions accumulate. This is a campaign-level finding that session-level scoring cannot capture.
**Scope:** Universal (any campaign where PCs have no designed backstory connections).
**Status:** logged. Cross-campaign: this confirms the hypothesis that situational familiarity becomes relational investment over time.

### I-C7-S5-01 — C7-S5 — the-strangers — 0047-the-false-trail
**Technique:** Wrong-fork-following (relationship-driven route deviation)
**Dimension:** Character Agency (cross: Surprise)
**What happened:** All three non-spotlight PCs followed Brek down the wrong fork without being asked. Vess diverted from her professional delivery route. Sera diverted from her research destination. Tam followed because he had been watching Brek since Greyford. No external event prompted any of them. The prompt was six sessions of accumulated operational familiarity.
**Why the rubric did not anticipate it:** Character agency at 10-band requires sustained behavioral pattern or character-register conversion. This is a distinct form: collective relational deviation from individual rational routes. Three PCs each had a reason NOT to follow; each followed anyway; the reasons for following were all different. This is independent-motivation convergence at the relationship-investment level.
**Scope:** Universal.
**Status:** logged.

### I-C7-S6-01 — C7-S6 — the-strangers — 0048-the-cost
**Technique:** Prepared-pouch accountability (private acknowledgment revealed through material preparation)
**Dimension:** Atmospheric Landing
**What happened:** Torven had 240 gp prepared in a pouch — set aside two years prior when he understood what he had done. The "prepared pouch" detail compressed two years of private acknowledgment into an object. The arc-completion was not the speech; it was the existence of the prepared object.
**Why the rubric did not anticipate it:** NPC arc-completion is documented as a moment of speech or action. This is a form of arc-completion where the preparatory act (setting aside the money) is the completion; the speech at the ford is just the delivery. The completion happened two years before the session.
**Scope:** Universal. Applicable to any NPC who has had time to prepare for a moment they knew was coming.
**Status:** logged.

### I-C7-S7-01 — C7-S7 — the-strangers — 0049-the-road-again
**Technique:** Silence-as-route-E-choice (PC makes Route E choice through non-speech)
**Dimension:** Character Agency (cross: Atmospheric Landing)
**What happened:** Sera made her Route E choice at the gate by saying nothing and walking through. Six sessions of delayed commitment produced a PC whose commitment requires no words. Walking was the choice. The silence was not absence of choice; it was the specific form her choice took.
**Why the rubric did not anticipate it:** Route E is a "choice that must be made." The rubric assumes choices are made through speech or declared action. Sera's non-speech route choice is the most radical form of character-register conversion in the campaign: her heuristic (delay commitment until data is sufficient) has been modified such that the commitment, when finally made, requires no articulation.
**Scope:** Universal. Any PC who has been delaying commitment through a campaign can resolve through non-speech when the data is finally sufficient.
**Status:** logged.

---

**C7 Campaign Threshold Checks:**
- Session-relationship-triggered (I-C7-S3-01): 1 instance in C7. Cross-campaign: Sorr (C7-S3) and Cassel (C7-S4) both. 2 instances in same campaign — propose documentation standard for session-relationship-triggered trigger type.
- Trigger-type transition (I-C7-S4-01): 1 campaign with clean transition. Requires 2+ campaigns for rubric-amendment proposal. Watch C8.
- RV9 confirmed: player styles emerge without personal stakes. RV10 confirmed: bilateral without designed relationship. RV11 confirmed: Route E without grief/duty anchor. RV12 confirmed: NPC arcs from situational acts.

**CAMPAIGN COMPLETE. Final trajectory: 69→71→72→74→75→76→77. 7 C7 innovations logged. Route E. All RV9-RV12 confirmed. Zero grief-triggered instances across 7 sessions — all situational or relationship-driven.**
