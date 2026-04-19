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

*(Future sessions append below this line.)*
