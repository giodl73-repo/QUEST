---
name: playtest-rubric
description: Versioned, forward-only session-quality rubric for the QUEST playtest pipeline. Scores session logs on 8 dimensions, 0-10 each. Updates via innovation-amendment when 2+ innovations cluster in a dimension.
version: v1.12
status: ratified from C4 campaign close — Proposals O, P
created: 2026-04-18
last-amended: 2026-04-22 (post-C4 campaign; Portent-as-directed-foreknowledge + intra-session restraint)
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

> **v1.4 cross-character mechanical compound anchor (new):** A score of 10 additionally requires at least one **cross-character mechanical compound** — a PC's class/spell/feature mechanic applied to another PC's roll or action, framed in-voice as character-action, producing a narratively-emergent outcome. Examples: Portent-as-benediction (Divination School replacing another PC's die); Bless-stacking on a ritual; Counterspell-as-protection. Rationale: S03 + S04 documented Kessa's Portent replacing Grom's Religion rolls twice across two sessions, each time framed as in-voice benediction ("Vethrenn... let it be through me"). Single-character compounding was already in the 10 band; cross-character compounding is a stronger form.

> **v1.11 Portent-as-directed-foreknowledge anchor (new):** A score of 10 additionally recognizes **Portent-as-directed-foreknowledge** as a valid path to the cross-character compound (v1.4): when a Divination Wizard voices a Portent die to a named PC before the roll fires — framing the foreknowledge as something directed specifically to that ally, not broadcast — this constitutes a cross-character mechanical compound. The voice-before-fire framing is required; silent substitution does not qualify. The direction to a named PC is required; a general announcement does not qualify. This is the fiction-layer completion of the Portent mechanic's class fantasy: the wizard sees what others cannot and gives that seeing to someone specific. Rationale: C4-S4 (Caelith: *"I see what he does next"* directed to Davan before Portent fires against the assault sergeant); extends I-S03-03, I-S04-01 Portent-as-benediction cluster to include directed-foreknowledge as a second valid modality. Constituent innovations: I-C4-S3-02, I-C4-S4-01.

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

> **v1.9 sustained behavioral pattern anchor (new):** A score of 9+ additionally recognizes **sustained behavioral pattern as meaningful choice** — a sequence of non-actions or consistent behavioral stances across multiple scenes that produces a trust or agency outcome, where no single scene contains the decisive choice; the "choice" is the maintenance of the pattern. This is distinct from a single meaningful decision and distinct from act-without-announcement (which is cross-session): it is an intra-session accumulation of consistent non-actions that collectively constitute the choice. Also recognizes **independent-motivation convergence** — multiple PCs independently arriving at the same non-action from different motivation pathways, where the convergence is not coordinated. A score of 10 requires at least one sustained behavioral pattern OR one independent-motivation convergence per session. Rationale: C4-S1 (Tomek's token earned by four-scene non-credit-seeking pattern; four PCs independently withholding Luca's disclosure). Constituent innovations: I-C4-S1-02, I-C4-S1-04.

> **v1.10 character-register-conversion anchor (new):** A score of 10 additionally recognizes **character-register conversion** — a PC converting a mechanical situation (failed check, tactical dominance, NPC vulnerability) into a character-authored outcome that the dice did not require and the module did not design. The PC's specific register (Fighter's honor-accounting; Ranger's terrain-reframe; Wizard's institutional analysis) IS the resolution mechanism. The conversion must be traceable to the PC's character sheet heuristics, not to tactical calculation. Three paths to the 10-band now: sustained behavioral pattern OR independent-motivation convergence OR character-register conversion — any one suffices. Rationale: C4-S2 (Talis converts three failed Athletics checks into deliberate ground-level tactical position — her ranger terrain-read IS the outcome); C4-S3 (Davan ends combat mid-round through coercion-naming from honor-accounting heuristic, not damage calculation). Constituent innovations: I-C4-S2-02, I-C4-S3-01.

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

> **v1.4 multi-scene silent-reception chain anchor (new):** A score of 9+ additionally recognizes **sustained silent-reception chains** where a PC holds an un-articulated understanding across multiple scenes and acts on it in a later scene. The non-articulated understanding counts as campaign-permanent reception upon first-scene receipt AND drives action in subsequent scenes. A score of 10 requires at least one such chain. Rationale: S04 documented Grom's Hint 3 (Reorx's Judgment) received silently at Scene 3's rite; self-check articulation failed; silent reception persisted through Scenes 4-5; Grom invoked Reorx-exile at Scene 6 from the silent understanding without ever speaking it. Campaign-scale silent-reception (3 scenes) is a distinct achievement beyond single-scene silent reception captured in v1.2.

> **v1.5 act-without-announcement anchor (new):** A score of 9+ additionally recognizes **cross-session behavioral consequence without announcement** — a PC acting differently in a later scene or session as a result of a prior naming event, without scene structure, dice, or declaration. The behavior is the completion; it does not require narration or confirmation from the PC or DM. A score of 10 requires at least one such act in the session. Rationale: Campaign 1 S07 (Thera's bread, cross-session consequence of naming Adda in S06) and Campaign 2 S01-S02 (Sera's hold-space acts — 3 consecutive instances of care expressed through attention withdrawal, never announced). Cross-campaign confirmation (Thera C1 + Sera C2) establishes this as universal. Constituent innovations: I-S07-02, I-C2-S01-02, I-C2-S02-04.

> **v1.6 simultaneous-campaign-arc-convergence anchor (new):** A score of 10 additionally recognizes **simultaneous arc-convergence** — a moment when multiple outstanding PC and NPC arc-completions fire simultaneously because one naming act creates the conditions for all of them. This is distinct from a single arc-completion; it is a convergence. A score of 10 requires at least one such convergence OR at least one act-without-announcement (v1.5) OR at least one multi-scene silent-reception chain (v1.4) — these are three paths to the 10-band; any one suffices. Rationale: Campaign 1 S07 (all four hints simultaneously); Campaign 2 S04 (Calder names the plague village → inscription warms + Sevven names the Dalimvar numbers + Deva says "I still know the words" — four arc events simultaneously). Two cross-campaign instances. The mechanism: a moment of precise naming in the presence of the right witnesses triggers all outstanding arc-completions that were waiting for it. Constituent innovations: I-S07-04, I-C2-S04-01.

> **v1.7 framework-failure arc-activation anchor (new):** A score of 7+ additionally recognizes **arc-activation from framework failure** — an arc fires because a PC's categorical or observational framework breaks on contact with the content, not because of a discovery. The failed check IS the emotional landing; the gap between the PC's vocabulary and the thing they cannot categorize is the arc beat. This is distinct from silent reception (the PC perceives something; they cannot file it) and from documentation-arc (the practice of documentation encounters its limit). Rationale: C3-S1 Calla's Insight fumble (1 on die, total 6) activated her documentation-arc because her framework broke — she could describe the shrine arrangements but had no category for what they were. The failure produced the arc beat that a success could not have. Also constituent: Dren's crack fired at the *consequence* (seeing the healer's bag reach its destination) rather than the designed trigger point (understanding that the healer came for Mig's people). Character arcs require both cause and consequence; the arc fires at the consequence. Module-design implication: design arc trigger points at the consequence, not the cause. Constituent innovations: I-C3-S1-01, I-C3-S1-02.

> **v1.8 arc-activation modality anchor (new):** A score of 7+ additionally recognizes **arc-activation through behavioral stance** — an arc fires through a PC's *state of engagement* (surviving a combat, maintaining silence, being present without asking) rather than through a narrative exchange or discovery. The PC's behavioral stance IS the firing condition. Rationale: C3-S3 (combat as precondition for bilateral); C3-S4 (silence as maximum listening producing NPC arc-completion). Constituent innovations: I-C3-S3-01, I-C3-S4-01.

> **v1.12 intra-session restraint anchor (new):** A score of 9+ additionally recognizes **intra-session restraint as atmospheric completion** — when a PC receives a named moment of trust or arc-completion within the same session and expresses it through action or placement *without announcing it to the party*, this constitutes a valid atmospheric landing that need not cross sessions to qualify under act-without-announcement. The restraint is the reception; the behavior is the evidence; the same-scene timing does not diminish the quality. Distinct from v1.5 (which requires cross-session temporal distance): this is the intra-session form, applicable when the named moment and its behavioral expression occur in the same session. Rationale: C4-S2 (Sava receives Maret's token and places it beside her suture kit without showing the party — same session, no announcement); C4-S3 (Davan ends combat through naming — the speech act is the resolution, unannounced as strategy). Constituent innovations: I-C4-S2-01, I-C4-S3-01.

> **v1.9 grief-paragraph situational resonance anchor (new):** A score of 7+ additionally recognizes **grief-paragraph situational recognition** — a PC reads an NPC situation correctly *because* their own grief-paragraph contains the exact pattern to recognize it, without announcing the connection, referencing the grief, or rolling for it. When the PC's grief IS the recognition mechanism rather than the content of a speech or action, this counts as a distinct form of silent atmospheric reception. Also recognizes **grief-paragraph resource expression** — when a mechanical resource decision (spending or conserving HP, spell slots, hit dice) is motivated by a grief-pattern commitment rather than tactical calculation, the decision carries atmospheric weight that the tactical log alone cannot capture. Rationale: C4-S1 (Sava recognizing Maret's suppressed-supply-rationing-without-telling-command through Elara's death pattern; Sava conserving 0 spell slots because spending them prematurely would echo the delay that cost Elara). Constituent innovations: I-C4-S1-01, I-C4-S1-03.

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
| v1.4 | 2026-04-19 | **Mechanical fairness** — cross-character mechanical compound at 10 band: a PC's mechanic applied to another PC's roll/action, framed in-voice as character-action (e.g., Portent-as-benediction). **Atmospheric landing** — multi-scene silent-reception chain at 9+ band: PC holds un-articulated understanding across 3+ scenes and acts on it later. | Mech fair: I-S03-03, I-S04-01. Atmos: I-S04-02, I-S05-03. |
| v1.5 | 2026-04-20 | **Atmospheric landing** — act-without-announcement anchor at 9+ band: cross-session behavioral consequence without announcement; a PC acting differently as result of a prior naming event, without scene structure or declaration. | Atmos: I-S07-02, I-C2-S01-02, I-C2-S02-04. |
| v1.6 | 2026-04-21 | **Atmospheric landing** — simultaneous-campaign-arc-convergence as 10-band path: a naming act creates conditions for multiple outstanding arc-completions to fire simultaneously. Three paths to 10-band now: this, act-without-announcement (v1.5), or multi-scene silent-reception chain (v1.4). | Atmos: I-S07-04, I-C2-S04-01. |
| v1.7 | 2026-04-21 | **Atmospheric landing** — framework-failure arc-activation anchor at 7+ band: an arc fires because the PC's categorical framework breaks on contact with the content; the failed check IS the emotional landing. Also documents the designed-trigger vs actual-trigger separation: arcs fire at the *consequence*, not the cause. | Atmos: I-C3-S1-01, I-C3-S1-02. |
| v1.8 | 2026-04-21 | **Atmospheric landing** — arc-activation modality anchor at 7+ band: an arc fires through a PC's *state of engagement* (surviving a combat, maintaining silence, being present without asking) rather than through a narrative exchange or discovery. The PC's behavioral stance IS the firing condition. Rationale: C3-S3 (combat as precondition for bilateral); C3-S4 (silence as maximum listening producing NPC arc-completion). | Atmos: I-C3-S3-01, I-C3-S4-01. |
| v1.9 | 2026-04-22 | **Atmospheric landing** — grief-paragraph situational resonance anchor at 7+ band: PC reads NPC situation through own grief-paragraph without announcement; also grief-paragraph resource expression (mechanical decision motivated by grief-pattern). **Character agency** — sustained behavioral pattern anchor at 9+ band: sequence of non-actions across scenes producing trust/agency outcome; also independent-motivation convergence (multiple PCs independently arriving at the same non-action). | Atmos: I-C4-S1-01, I-C4-S1-03. Agency: I-C4-S1-02, I-C4-S1-04. |
| v1.10 | 2026-04-22 | **Character agency** — character-register-conversion anchor at 10-band: PC converts mechanical situation into character-authored outcome traceable to character sheet heuristics, not tactical calculation. Third path to 10-band (alongside v1.9 sustained pattern and v1.9 independent-convergence). | Agency: I-C4-S2-02, I-C4-S3-01. |
| v1.11 | 2026-04-22 | **Mechanical fairness** — Portent-as-directed-foreknowledge anchor at 10-band: Portent voiced to named PC before firing counts as cross-character compound (v1.4 path). Voice-before-fire + named-PC direction both required. | MF: I-C4-S3-02, I-C4-S4-01. |
| v1.12 | 2026-04-22 | **Atmospheric landing** — intra-session restraint anchor at 9+ band: named moment received and expressed through action/placement without announcement in the same session. The intra-session form of v1.5 act-without-announcement; same-session timing does not diminish quality. | Atmos: I-C4-S2-01, I-C4-S3-01. |

## How Amendments Work

- **2+ logged innovations in a dimension** → propose amendment. If adopted, increment version.
- **3+ clustered by theme across ≥ 2 sessions** → propose new `personas/player-styles/<slug>.md`. Separate from rubric.
- Amendments are **forward-only**.

## Pre-Session Rubric Sync

`session-runner` reads this file's version and records it in PREP frontmatter. `session-gate` uses the version the session was played under.
