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
