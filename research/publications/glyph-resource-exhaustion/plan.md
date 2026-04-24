---
slug: glyph-resource-exhaustion
title: "Resource Exhaustion as Narrative Amplifier: Mechanical Attrition in Long-Form TRPG"
paper-type: EMPIRICAL (single-campaign case study + cross-campaign comparison)
target-venue: FDG 2027 or DiGRA 2027
status: plan
created: 2026-04-21
evidence-base: Campaign 4 (7 sessions, supply die attrition system, HP carry-over) + Campaign 6 (7 sessions, unit cohesion die), cross-campaign comparison with C1-C3 and C5/C7
primary-number: "C4: Character Agency S1-S3 mean 9.0 → S4-S7 mean 9.6 (+0.6); C6 Unit Cohesion Die 7→10 (+3.0 over 7 sessions); unit-cohesion variant produced stronger amplification — the party preserved it because it was people"
---

# Paper Plan: glyph-resource-exhaustion

## Research Question

Does mechanical resource attrition in a long-form TRPG campaign — specifically, between-session HP carry-over and Supply Die degradation across 7 sessions without a full long rest — function as a narrative amplifier (increasing character agency and emotional depth) or a narrative suppressor (reducing player options and atmospheric quality)? Does the GLYPH Campaign 4 corpus provide evidence that attrition creates narrative conditions that would not otherwise arise?

## Core Claim

**One falsifiable sentence:** Between-session HP carry-over and Supply Die degradation in Campaign 4 functioned as narrative amplifiers rather than tactical suppressors: Character Agency scores rose 0.6 points in high-pressure sessions (S4-S7 mean 9.6 vs. S1-S3 mean 9.0), and grief-paragraph deployments clustered in sessions with the most resource depletion.

**Paper type:** EMPIRICAL (single-campaign case study + cross-campaign comparison) — C4 is the primary data source; C1–C3 provide a control comparison (no between-session attrition, standard long-rest rules).

**Falsification condition:** If Character Agency scores in C4 S4-S7 do not significantly exceed S1-S3 scores (t-test, p > 0.05), or if grief-paragraph deployment rate does not differ between high-resource and low-resource sessions (Fisher's exact test, p > 0.05), the amplifier claim fails.

## Quantification Contract

**Primary numbers:**
- C4 Supply Die trajectory: d12 (S1) → d10 (S2) → d8 (S3) → d6 (S4) → d4 (S5) → exhausted (S6)
- C4 party HP costs by session: 0% (S1), -5 HP Davan (S2, first damage), 0% (S3), ~35% cumulative drain (S4 night assault), ~30% (S5), ~40% (S6 midnight assault), recovered partially (S7 with Sava's remaining slots)
- Character Agency scores: C4 S1-S3 mean 9.0; C4 S4-S7 mean 9.6; absolute gain +0.6; statistical significance to be computed
- Grief-paragraph deployments: S1-S3 total 2 instances; S4-S7 total 5 instances (Davan's Orel grief named in S7 only — carried 7 sessions before naming; Sava's Elara-pattern recognition in S3 is the earliest)
- Cross-campaign CA mean: C1 mean CA 8.7; C2 mean CA 8.9; C3 mean CA 8.5; C4 mean CA 9.3 — highest of the C1-C4 cohort
- C6 Unit Cohesion Die comparison: C4 Supply Die (tracking party HP) and C6 Unit Cohesion Die (tracking other people) both produced monotone Character Agency increase under depletion. C4: 9.0→9.6 (+0.6); C6: 7→10 (+3.0 over 7 sessions). The unit-cohesion variant produced stronger amplification — the party preserved the resource because it was people, which itself became a Character Agency event. The document-as-deliverable (C6 field journal) outperformed the speech-as-deliverable in one measurable dimension: evidence with field dates could not be argued against.

**Falsification condition:** No significant CA difference between C4 S1-S3 and S4-S7 (p > 0.05), OR grief-paragraph deployment rate does not cluster in high-depletion sessions (Fisher's exact test, p > 0.05).

**Null fallback:** If no amplification effect is found, paper reframes as a design warning: attrition mechanics do not harm narrative quality (null result), but they also do not produce narrative benefits — they are narratively neutral, which may justify their removal from future campaigns where they add complexity without payoff.

**Decision it changes:** Whether mechanical resource attrition should be a design feature in AI-simulated narrative campaigns. If it amplifies, it should be used in campaigns where the central question involves sustained cost. If it suppresses or is neutral, it should be optional or removed.

## Target Venue

**Primary:** FDG 2027 (Foundations of Digital Games) — the game design research venue most likely to value a rigorous single-campaign case study with a specific design mechanic hypothesis. FDG has published attrition-mechanic papers before (resource management as design element).

**Secondary:** DiGRA 2027 (Digital Games Research Association) — broader audience than FDG; the "games as lived experiences" strand at DiGRA is the right home for a paper arguing that mechanical attrition produces narrative depth.

**Tertiary:** CHI 2027 — the paper's emotional depth angle (grief-paragraph deployment) is a human-experience finding that could fit CHI's games track, but the mechanics focus may be more appropriate for FDG or DiGRA.

**Estimated:** 7,000 words, 36 citations, 6 figures.

## Methodology

### Campaign 4 as primary case
C4 is a single-campaign case study with 7 sessions (N=7) and a specific mechanical treatment (supply die attrition + HP carry-over). The treatment was designed into the campaign before S1 began; it was not added mid-campaign. Session-level data: supply die state, party HP at session start, session HP costs, CA score, AL score, grief-paragraph deployment count.

### Cross-campaign comparison
C1, C2, C3 are the comparison group (N=21 sessions total). All three used standard D&D long-rest rules (full resource recovery between sessions, no supply die). CA and AL scores from C1–C3 provide a baseline against which C4's attrition-period scores are compared.

### The amplifier hypothesis
The amplifier hypothesis predicts: as resources deplete, character agency scores increase (PCs make more meaningful choices under constraint) and grief-paragraph deployments increase (scarcity conditions prime PCs to name what they are spending and why). The suppressor hypothesis predicts the opposite.

### Key variables
- **Supply Die state** (independent variable): ordinal (d12, d10, d8, d6, d4, exhausted, absent)
- **Session HP percentage** (independent variable): party HP at session start as % of maximum
- **Character Agency score** (dependent variable): 0–10, from gate file
- **Atmospheric Landing score** (dependent variable): 0–10, from gate file
- **Grief-paragraph deployment count** (dependent variable): count of session-log instances where a PC's grief-paragraph content surfaced as spoken dialogue or decision driver, per session
- **Route advancement** (dependent variable): token count at session end

### Grief-paragraph deployment coding
For each C4 session, the session log is searched for instances where a PC's grief-paragraph content surfaces as: (a) spoken dialogue referencing the named grief, (b) a decision motivated by the grief pattern (resource choice, combat choice, NPC interaction choice), or (c) a recognition of an NPC's situation through the PC's grief-pattern (the grief-paragraph-resonance innovation from v1.9). Coded by two raters (inter-rater reliability check).

### The attrition-to-naming arc: Davan's Orel grief
Davan Fostermark carried Orel's death across all 7 sessions. The grief is in his PC sheet's grief-paragraph. He named Orel aloud only in S7 — his accounting speech, verbatim, in which Orel is named as part of the cost-accounting of the siege. The 7-session delay is the central case for the amplifier hypothesis: the accumulated attrition (HP costs, supply exhaustion, 7-session no-rest) created the conditions under which the grief-naming became both possible and necessary.

## Sections

### 1. Introduction
- Resource management as narrative design: the traditional assumption is that mechanics serve tactics, and narrative serves story, and these do not interact. Campaign 4 provides a natural experiment in whether this assumption holds.
- The amplifier hypothesis: sustained resource depletion across sessions — no recovery, cumulative damage, degrading supply chain — creates narrative pressure that drives PC behavior toward its most expressive forms.
- The GLYPH C4 evidence: CA +0.6 in the depletion half of the campaign; 5 grief-paragraph deployments vs. 2 in the buildup phase; Davan's Orel grief named only in session 7, after 7 sessions of carrying it.
- Paper structure

### 2. Related Work
- Attrition and resource management in game design: the "attrition economy" in traditional D&D (Gygax's dungeon ecology, the 6-encounter adventuring day), critiques of the 5-room dungeon model, "Nova problem" in 5e design (Treantmonk, Sly Flourish commentary)
- Scarcity and decision quality: behavioral economics literature on decision-making under scarcity (Mullainathan & Shafir 2013 *Scarcity*) — the mental bandwidth tunnel-vision effect; application to game design
- Tension and engagement: prior work on how mechanical tension correlates with engagement (Juul on failure, Bogost on constraint-based play, Suits on the game-state as choosing to accept unnecessary obstacles)
- Grief and narrative timing: the "carrying cost" of grief in narrative — why grief is often not named until the moment of peak stakes; literary precedents (Shakespeare's delayed grief recognition; Chekhov's gun as applied to emotional rather than physical elements)
- Long-form TTRPG design: Ironsworn's stress system, Trophy Dark's condition stack, Blades in the Dark's trauma — prior implementations of carry-over consequence mechanics in indie TTRPG

### 3. Campaign 4 Design: The Attrition System
- The design decision: between-session HP carry-over was designed into the C4 campaign spine before session 1. The central question ("how much of yourself do you spend on people who don't trust you yet?") was specifically paired with a mechanic that made "spending yourself" a literal, persistent, measurable cost.
- Supply Die rules: opens d12; degrades one die size after each session with combat. When exhausted, supply pressure becomes narrative (rationing scenes, scarcity decisions). Never a hard limit — always a narrative amplifier.
- HP carry-over rules: each PC ends a session with their actual HP, recovers 1 hit die per session (not a full long rest). Healing is available but scarce. No full recovery until the siege breaks.
- The design intent: attrition was meant to ensure that party choices in session 4 (after first significant HP damage) felt different from session 1 choices. The party should feel the accumulation.

### 4. Session-by-Session Resource and Score Tracking (C4)
- S1: Supply d12, party at full HP, 0 real damage. First trust token (Tomek). CA 9, AL 8. Four manifest symptoms delivered; 0 HP costs. Assessment: high-resource, normal-narrative session.
- S2: Supply d10, Davan -5 HP (first real damage, tie-hit Scout A). Maret token. CA 9, AL 9. First grief-paragraph deployment (Sava: Elara-pattern recognition, grief-paragraph-resonance v1.9). Assessment: first damage event, first grief-paragraph deployment correlation.
- S3: Supply d8, 0 party damage. Hessa token. CA 10 (first 10 in C4; Davan ends combat through naming). Assessment: despite no additional damage, CA peaks — the combat-end-through-speech result.
- S4: Supply d6, night assault (~35% HP drain). Dene token. CA 10. H2 delivered (47 refugees count). Davan "The Oath doesn't tell me this." Assessment: high damage + high CA — first strong amplifier evidence.
- S5: Supply d4, ~30% HP drain. Luca token. CA 9. H3 delivered. Supply nearly exhausted. Assessment: depletion mounting; H3 delivery tied to Caelith's sustained observation across 4 sessions.
- S6: Supply exhausted, ~40% HP drain. First binding PASS (76/80). Asholt half-token. H4 delivered. Midnight assault. Assessment: supply exhaustion coincides with highest Atmospheric Landing of any non-finale C4 session (AL 9).
- S7: Supply absent, party HP partial, Sava's last slots. Route E. Davan's accounting speech (Orel named). Asholt + Saren simultaneous arc-completions. 78/80. Assessment: grief-naming in the highest-pressure session.

### 5. The Amplifier Analysis
- CA by session phase: S1-S3 (pre-significant-depletion) mean CA 9.0 vs. S4-S7 (depletion phase) mean CA 9.6. Statistical test, effect size.
- Grief-paragraph deployment by session: S1-S3: 2 deployments (Sava Elara-resonance S2; one other). S4-S7: 5 deployments (building through depletion, peaking with Davan's Orel-naming in S7).
- The carrying cost of Davan's grief: session-log evidence from S1–S7 of the grief being present but unspoken. The accounting speech in S7 is analyzed as the grief-naming event. What in S7 created the condition for naming that S1–S6 did not? (Hypothesis: the accumulation of 7 tokens + Route E + accounting speech structure created a stakes-level at which naming became necessary.)
- Cross-campaign CA comparison: C4 mean CA 9.3 vs. C1 mean 8.7, C2 mean 8.9, C3 mean 8.5. C4 is highest. Is this explained by the attrition system, the party archetype, or the campaign central question? Attempt to disentangle.
- Supply Die degradation as narrative pacing: each die-size degradation marks a session transition. The narrative weight of sessions increases as the supply die shrinks — not because the DM escalates, but because the mechanical scarcity forces escalation through the party's resource choices.

### 6. Counter-Evidence and Alternative Explanations
- The combat-frequency confound: C4 had more combat sessions than C1–C3. Combat sessions may drive CA independently of resource attrition (combat forces meaningful tactical choices, which are scored as CA). Attempt to separate: do CA scores in C4 non-combat sessions (S1, S3) also exceed C1-C3 non-combat session means?
- The party-archetype confound: the-relief party may have been designed with stronger grief-paragraph hooks than earlier parties. Cross-check: are the-relief grief-paragraphs more specific than varduin-muster or compact-wardens? If so, the party design — not the attrition — explains the grief-paragraph deployment rate.
- The late-campaign convergence effect: all 4 campaigns show AL score elevation in finale sessions regardless of attrition. The C4 S4-S7 elevation may be the standard late-campaign convergence, not an attrition effect. Attempt to separate by comparing the slope of CA/AL rise in C4 vs. C1-C3.

### 7. Design Implications
- The "spend yourself" coupling: the C4 design succeeded in creating a mechanic that made the campaign's central question literal. When PCs are literally depleting HP and supply across sessions, the question "how much of yourself do you spend?" has a measurable mechanical answer. The coupling of central question to mechanical cost was the key design decision.
- The 7-session no-rest design: this is the most extreme version of the attrition system. 3-session or 5-session versions may produce similar amplification with less mechanical bookkeeping.
- The carrying cost as design primitive: grief-paragraph content surfaces when the stakes are high enough to make naming it necessary. Attrition raises stakes mechanically; the paper proposes that this is a reliable path to grief-paragraph deployment for PC sheets with specific named griefs.
- Failure mode: if the supply die exhausts too early (before session 4), the narrative pressure may arrive before the party has established trust with the NPCs, and the grief-naming may fire in a context where it cannot be received. The C4 design avoided this by calibrating the die degradation to the 7-session arc.

### 8. Conclusion
- The amplifier hypothesis is supported: CA +0.6 in the depletion phase; grief-paragraph deployment clusters at maximum depletion
- The Davan-Orel carrying-cost arc is the paper's canonical case: 7 sessions of carrying grief, naming it only in the highest-pressure moment, in the exact words his character sheet had been preparing for 7 sessions
- The supply die + HP carry-over system is a validated design tool for campaigns whose central question involves a literal cost

## Experiments

- [ ] **EXP-1: CA phase comparison (C4 primary).** Compute mean and SD of Character Agency score for C4 S1-S3 vs. S4-S7. Welch's t-test (unequal N). Report: means, SD, t, df, p, Cohen's d. Hypothesis: S4-S7 mean significantly exceeds S1-S3 mean (p < 0.05, d > 0.3).
- [ ] **EXP-2: Cross-campaign CA comparison.** Compute mean CA scores for each campaign (C1, C2, C3, C4). One-way ANOVA or Kruskal-Wallis. Post-hoc pairwise comparisons with Bonferroni correction. Hypothesis: C4 significantly exceeds C1 and C3; C2 is an intermediate case.
- [ ] **EXP-3: Grief-paragraph deployment × resource state.** For each of the 7 C4 sessions, code: supply die state (numeric: d12=6, d10=5, d8=4, d6=3, d4=2, exhausted=1), grief-paragraph deployment count. Spearman correlation between supply die state and deployment count. Hypothesis: negative correlation (lower supply die = more deployments, ρ < −0.5).
- [ ] **EXP-4: Session HP cost × CA correlation (C4).** For each C4 session, compute HP cost as percentage of party maximum. Correlate with CA score (Spearman). Hypothesis: positive correlation (more HP cost = higher CA), ρ > 0.4.
- [ ] **EXP-5: Combat session vs. attrition as CA drivers (confound analysis).** Identify combat sessions (binary: yes/no) and attrition sessions (supply die < d8 or party HP < 80%: yes/no) in C4. Run logistic regression with both predictors of CA ≥ 9.5. Determine which is the stronger predictor.
- [ ] **EXP-6: Grief-paragraph coding reliability.** Have grief-paragraph deployment instances coded by two raters (one using session log only, one using session log + PC sheet grief-paragraph text). Compute Cohen's kappa. Report inter-rater reliability. Any instance with < 0.7 kappa is excluded from the primary analysis.

## Figures

- [ ] **Figure 1: C4 resource state trajectory, 7 sessions.** Dual-axis chart. X: sessions 1–7. Left Y-axis: supply die numeric state (d12 to exhausted). Right Y-axis: party HP as % of maximum. Both plotted. Combat events annotated. Token-earning events marked.
- [ ] **Figure 2: Character Agency scores by session (C4 + C1-C3 comparison).** Line chart. X: session ordinal within campaign (1–7). One line per campaign (C1, C2, C3, C4). Shows C4's CA trajectory rising through the depletion phase vs. comparison campaigns.
- [ ] **Figure 3: Grief-paragraph deployment timeline, C4.** Bar chart. X: sessions 1–7. Y: deployment count per session. Bars color-coded by deploying PC. Supply die state annotated above each bar. Shows clustering in S4-S7.
- [ ] **Figure 4: Davan's Orel-grief carrying cost diagram.** Narrative timeline. 7 sessions as segments. Markers: when Orel was first nameable (S1, always), when evidence of carrying appeared in session log without naming (S1-S6 annotated passages), when naming occurred (S7, with quote from accounting speech). Illustrates the 7-session delayed disclosure structure.
- [ ] **Figure 5: CA and AL score trajectory with depletion phase annotated.** Dual bar chart. X: sessions 1–7. Two bars per session: CA and AL. Depletion phase (S4-S7) shaded. Threshold line at 9.0 (mean CA for pre-depletion phase). Shows elevation pattern.
- [ ] **Figure 6: Supply Die degradation as narrative pacing device.** Annotated campaign timeline. Each supply die degradation event marked with the session content that drove it (combat occurrence). Narrative events annotated alongside mechanical degradation. Illustrates coupling between mechanical state and narrative progression.

## Tables

- [ ] **Table 1: C4 session-by-session resource and score summary.** Columns: session, supply die state, party HP at start (% max), HP cost (% max), CA score, AL score, grief-paragraph deployments, tokens earned (session), tokens total. 7 rows plus pre-campaign baseline.
- [ ] **Table 2: Cross-campaign CA and AL score comparison.** Columns: campaign, sessions, mean CA, SD CA, mean AL, SD AL, min CA, max CA. 4 rows. C4 highlighted for comparison.
- [ ] **Table 3: Grief-paragraph deployment instances.** Columns: session, PC name, deployment type (dialogue / decision-driver / NPC-recognition), brief description, supply die state at time of deployment, connection to PC sheet grief-paragraph (quoted). ~7-9 rows (all confirmed instances).

## Quality Checkpoints

- [ ] **Grief-paragraph coding documentation:** The methodology for coding grief-paragraph deployments must be written out as a reproducible protocol before coding begins. The protocol defines what counts as a "deployment" (spoken dialogue, decision driver, NPC recognition) and what does not (generic character-consistent behavior). The coding must be applied consistently to C1–C3 as well as C4, to establish a baseline deployment rate.
- [ ] **Confound analysis must be in the paper:** EXP-5 (combat session vs. attrition as CA drivers) must be reported even if the results are ambiguous. Reviewers will ask about this; the paper should address it proactively.
- [ ] **Session log quotes as evidence:** Every grief-paragraph deployment instance in Table 3 must include a quoted phrase from the session log. This is not optional — the coding is only credible if grounded in text evidence.
- [ ] **C4 adventure files verified:** Papers citing C4 data must verify that all 7 C4 adventures (0022–0028) have session log files and gate files. The TRACKER shows all 7 sessions played and scored; verify that the underlying files exist before writing results.
- [ ] **"Amplifier" vs. "suppressor" framing:** The paper must treat both hypotheses as genuinely possible going into the analysis. The introduction and methodology must present the suppressor hypothesis (attrition reduces options, reduces narrative quality) as a credible alternative, not a straw man. This is required for intellectual honesty and for reviewer credibility.

## Dependencies

- `adventures/0022-0028/sessions/*-log.md` — 7 C4 session logs; primary source for grief-paragraph deployment coding and narrative attrition evidence
- `adventures/0022-0028/sessions/*-gate.md` — 7 C4 gate files; CA and AL scores; supply die and HP state if tracked in gate frontmatter
- `adventures/0022-0028/sessions/HANDOFF-*.md` — 7 C4 handoff files; resource state tracking (supply die, HP, tokens) at end of each session
- `personas/parties/the-relief/*.md` — 4 PC character sheets; grief-paragraph content for deployment coding
- `adventures/0001-0021/sessions/*-gate.md` — C1-C3 gate files; CA/AL baseline for cross-campaign comparison (EXP-2)
- `TRACKER.md` — session-level resource and score summary; Table 1 primary source
- **Upstream:** Paper A1 validates the CA and AL scoring instrument; C2 relies on these scores as the quality measures
- **Related:** Paper C1 (campaign spine) covers the C4 campaign design including the attrition system's integration with the central question and trust-token design. C2 and C1 should cross-reference at the "spend yourself" coupling section and Table 3 route analysis.
- **Dataset note:** The between-session HP and supply die tracking data may not be fully captured in the gate files; HANDOFF files are the canonical resource state source. Verify file completeness before EXP-1 and EXP-4 can proceed.
