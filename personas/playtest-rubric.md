---
name: playtest-rubric
description: Versioned, forward-only session-quality rubric for the marathon playtest pipeline. Scores session logs on 8 dimensions, 0-10 each. Updates via innovation-amendment when 2+ innovations cluster in a dimension.
version: v1.3
status: ratified from S03 Amendment Proposal E
created: 2026-04-18
last-amended: 2026-04-19 (post-S03)
---

# Playtest Session Rubric

Each session log (finalized at LOG stage) is scored against this rubric by `session-gate`. Scoring is forward-only: a new version applies to sessions scored **after** the amendment; old scores never retroactively adjust.

**Threshold (advisory through S03, binding S04+):** 56+ / 80 (70%).

## The 8 Dimensions

### 1. Engagement (0-10)
**Question:** Did each PC contribute, and did the session hold the table's attention?

- **0-3:** One or more PCs drifted; the DM ran scenes by himself.
- **4-6:** All PCs nominally present; contributions uneven.
- **7-9:** Each PC had at least one scene they drove.
- **10:** Every PC drove at least one scene AND their combined contributions produced an outcome the DM did not pre-script.

### 2. Mechanical Fairness (0-10)
**Question:** Did dice land honestly, DCs feel calibrated, outcomes feel earned — AND did mechanics respect other dimensions?

- **0-3:** Rolls were faked, ignored, or re-rolled for narrative.
- **4-6:** Rolls honest; some DCs misaligned; one or two fudges.
- **7-9:** Every roll traced to seed; DCs felt appropriate; dice-driven surprises welcomed. **Plus:** no session mechanic regularly destroyed atmospheric-landing, module-fidelity, or character-agency payoffs as a side-effect of its designed behavior.
- **10:** Dice produced emergent story the DM could not have predicted AND mechanics compounded narratively (e.g., exhaustion shaped a later decision).

> **v1.1 cross-dimensional-harmlessness anchor:** A score of 7+ requires that no session mechanic **regularly** damages atmospheric-landing, module-fidelity, or character-agency payoffs as its designed behavior. A mechanic that costs resources cleanly (HP, slots, hit dice, time) is fine; a mechanic that inflicts check-disadvantage on atmospheric-gate rolls is cross-dimensionally damaging and caps the dimension at 6.

### 3. Pacing (0-10)
**Question:** Did scenes earn their length? Did the session feel tight or slack?

- **0-3:** Long filler scenes; combat dragged; read-alouds re-narrated.
- **4-6:** Some scenes over- or under-stayed; combat rounds not tight.
- **7-9:** Scenes opened and closed cleanly; transitions felt earned.
- **10:** The session had an arc — rising tension, climax, resolution — without forcing.

### 4. Character Agency (0-10)
**Question:** Did PCs make choices that mattered? Did decisions come from character, not module?

- **0-3:** Railroad; PC choices cosmetic; decisions pre-determined by module.
- **4-6:** Some choices real, most forced.
- **7-9:** Multiple meaningful decisions; PC heuristics visibly shaped outcomes.
- **10:** The session's final state depended on specific PC choices the module anticipated but did not require.

### 5. Module Fidelity (0-10)
**Question:** Did the adventure deliver what it was designed to? Did manifest symptoms land — including anchor-level ones?

- **0-3:** Key set-pieces missed; manifest symptoms did not land.
- **4-6:** Some designed beats landed; others lost to pacing or rolls.
- **7-9:** ≥ 75% of manifest symptoms landed; core set-pieces hit.
- **10:** All manifest symptoms landed AND the module's *hidden* payoffs (rewards for attention) were unlocked. **Plus:** anchor-level symptoms (cross-adventure signals; named-NPC reveals; reaction moments) had documented passive-Perception fallbacks AND documented recovery-paths for post-session re-discovery.

> **v1.2 anchor-level passive-Perception + recovery-path anchor:** A score of 9+ requires that *anchor-level* manifest symptoms (as defined by the adventure's manifest file — cross-adventure signals, named-NPC reveals, reaction moments, foreshadowing clues that gate future-adventure hooks) have documented **passive-Perception fallback at DC = active-check + 2**. A score of 10 additionally requires **recovery-path** documentation: how a party that missed an anchor-level symptom in play could still encounter it post-session (geographic persistence, future-session prompts, NPC-delivered recall). Rationale: S02 (pre-v1.2) missed its cross-adventure signal by one point on two consecutive Investigation rolls; the module's most ambitious design element failed on a single-gate-by-one.

> **v1.3 positional-redundancy anchor (new):** A score of 9+ requires anchor-level symptoms have at least **TWO of these three fallback mechanisms:**
> **(a)** active-check + passive-Perception fallback at DC = active+2 (v1.2 current);
> **(b)** redundant placement in at least two locations or two scenes, such that the symptom can be perceived from multiple positions;
> **(c)** NPC-delivered recall — an NPC (named, present, with in-fiction reason to mention) can re-surface the symptom in a later scene as a final fallback.
>
> Adventures that rely on a single-location positional symptom with only (a) cap at 8/10. Rationale: S03 (pre-v1.3) documented a v1.2-compliant filigree-dim anchor-symptom with passive-Perception DC 14 fallback. The fallback could not fire because nobody was *positioned* to roll when the symptom triggered (party in lower chamber; only witnesses were NPCs with passive <14). The v1.2 fallback-mechanic assumes someone is in-position; S03 showed a distinct failure mode where the check-infrastructure exists but the geometry prevents the roll. Three fallback paths OR'd against each other prevent this.

### 6. Atmospheric Landing (0-10)
**Question:** Did intended emotional/sensory moments hit the players? Who found them? Who received them? Did they chain?

- **0-3:** Mood beats flat; sensory details not used.
- **4-6:** Some beats landed; atmosphere inconsistent.
- **7-9:** Multiple atmospheric moments hit; at least one will be remembered. **Plus:** the session log documents *which PCs* found each beat AND *which PCs* received its emotional weight (finder-vs-receiver may differ). Silent reception (character-interior without dice or narration) counts.
- **10:** The session produced a specific sensory/emotional image that will outlive the session in the players' memory AND at least one **inter-PC chain** occurred (one PC's atmospheric reception triggered another PC's interior response without dice).

> **v1.1 per-PC reception + chain-reaction anchor:** A score of 9+ requires documenting *which PCs received each atmospheric flag* in the session log. A score of 10 additionally requires at least one inter-PC grief-chain or atmospheric-chain.

> **v1.2 finder-vs-receiver + silent reception anchor (new):** A score of 7+ requires **two-column per-PC tracking** — *finder* (who rolled or noticed the beat) separated from *receiver* (which PC the beat emotionally landed on). They may be the same PC; they may diverge. **Silent reception** (character-interior realization without dice or narration, per module's explicit instruction) counts as reception — it need not be externalized to count. Rationale: S02 showed Kessa finding the bread-scrap but Grom receiving its weight (I-S02-01); the module's per-PC table under-predicted this kind of chain. Also S02 showed Aelric's Varran-no-pyre realization at Sir Venric's pyre (I-S02-08) — fully interior, no dice, module's explicit *"let the player feel it"* instruction.

### 7. Surprise (0-10)
**Question:** Did anything emergent happen that the DM, the players, or the module did not predict?

- **0-3:** Entirely predictable; no `<!-- SURPRISE -->` tags.
- **4-6:** 1-2 surprises; minor.
- **7-9:** 3-6 surprises; at least one substantive.
- **10:** ≥ 7 surprises AND ≥ 1 is substantive enough to warrant a rubric-amendment proposal or player-style seed.

### 8. Table Readiness (0-10)
**Question:** Could the DM have run this session cold from the module + party files?

- **0-3:** DM required significant outside prep; repeated lookups derailed play.
- **4-6:** Some pauses to consult sources; runnable with effort.
- **7-9:** Runnable from `module.md` + party files + dice script; minimal consulting.
- **10:** Ran cold; every lookup the DM needed was inline in the artifact.

## Scoring Protocol

For each dimension:

1. Read the session log with this dimension in mind.
2. Find evidence — quote specific passages or cite scene numbers.
3. Find counter-evidence — quote passages that lower the score.
4. Assign score using the bands above.
5. Write the evidence cell — not generic assessment, but specific citation.

Do not score generously out of sympathy. Do not score harshly to seem rigorous. Score what is in the log.

## Amendment History

| Version | Date | Change | Source innovations |
|---|---|---|---|
| v1.0 | 2026-04-18 | Initial 8-dimension rubric | — |
| v1.1 | 2026-04-18 | **Mechanical fairness** — cross-dimensional-harmlessness anchor. **Atmospheric landing** — per-PC reception tracking + inter-PC chain-reaction. | Mech fair: I-S01-08, I-S01-09. Atmos: I-S01-02, I-S01-10, I-S01-12. |
| v1.2 | 2026-04-19 | **Module fidelity** — anchor-level passive-Perception fallback (DC = active+2) + recovery-path for post-session re-discovery (9+ and 10 bands). **Atmospheric landing** — finder-vs-receiver two-column tracking + silent-reception recognition (7+ band). | Mod fid: I-S01-03, I-S02-02, I-S02-03, I-S02-06. Atmos: I-S02-01, I-S02-07, I-S02-08. |
| v1.3 | 2026-04-19 | **Module fidelity** — positional-redundancy anchor: anchor-level symptoms require at least 2 of 3 fallback paths (check+passive; multi-location placement; NPC-delivered recall). Adventures relying on single-location positional symptoms cap at 8. | Mod fid: I-S03-01, I-S03-04, I-S03-07. |

## How Amendments Work

- **2+ logged innovations in a dimension** → propose amendment. If adopted, increment version.
- **3+ clustered by theme across ≥ 2 sessions** → propose new `personas/player-styles/<slug>.md`. Separate from rubric.
- Amendments are **forward-only**.

## Pre-Session Rubric Sync

`session-runner` reads this file's version and records it in PREP frontmatter. `session-gate` uses the version the session was played under.
