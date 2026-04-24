---
slug: glyph-npc-arc
title: "NPC Arc-Completion Design: Session-Invariant Emotional Payoffs Without DM Scripting"
paper-type: EMPIRICAL
target-venue: CHI 2027 or CSCW (games/narrative track)
status: plan
created: 2026-04-21
evidence-base: 40+ NPC arc-completion instances across 49 sessions, 7 campaigns
primary-number: "40+ NPC arc-completion instances across 49 sessions (C5: 8, C6: 5, C7: 3 confirmed); session coverage ≥88%; all fired by character logic"
---

# Paper Plan: glyph-npc-arc

## Research Question

When NPCs are designed with explicit arc-completion conditions — a specific thing they are capable of saying or doing, and the specific party action required to trigger it — how reliably do those arc-completions fire by character logic during play? Does the GLYPH corpus of 28 sessions demonstrate that pre-designed, condition-gated NPC arc-completions produce higher-quality narrative moments than improvised DM-scripted ones, and does the design method generalize across campaign types and party archetypes?

## Core Claim

**One falsifiable sentence:** NPCs designed with explicit arc-completion conditions fire their arc-completion moments by character logic — not DM scripting — in ≥86% of sessions across 4 campaigns.

**Paper type:** EMPIRICAL — design pattern analysis. The NPC arc-completion design method is the independent variable; firing-by-character-logic rate, quality scoring (Atmospheric Landing and Module Fidelity scores for sessions with arc-completions vs. without), and session-log evidence of trigger conditions being met are the dependent variables.

**Falsification condition:** If fewer than 75% of designed arc-completions fire by character logic (i.e., party action meets designed trigger condition), or if sessions with arc-completions do not score significantly higher on Atmospheric Landing than sessions without (t-test, p > 0.05), the design method's effectiveness claim fails.

## Quantification Contract

**Primary number:**
- 40+ documented NPC arc-completion instances across 49 sessions
- C1-C4 confirmed: ~24 instances (Tomek, Maret, Hessa, Dene, Luca, Asholt, Saren; Mig, Veth, Gorret, Sharr, Morren, Aldric, Velantha, Doran; Mira Vaenshold, Tiran, Laen; Tessamine, Lenne, Morreth, Mira Coldsteel, Vorn)
- C5-C7 confirmed: C5 8 instances, C6 5 instances, C7 3 instances
- 0 instances requiring DM scripting to fire: all documented completions trace to a trigger condition being met by party action
- Sessions with 2+ simultaneous arc-completions: C2-S04 (4 simultaneous), C4-S07 (Asholt + Saren simultaneous); additional simultaneous instances in C5 and C6

**Falsification condition:** Firing-by-character-logic rate < 75% (< 18 of ~24 instances trace to met trigger conditions), OR Atmospheric Landing dimension does not differ significantly between sessions with vs. without arc-completions.

**Null fallback:** If firing rate is high but quality effect is absent, paper reframes as design-discipline study: the method produces consistent arc-firings without quality uplift from the arc-completions themselves — a null result worth reporting.

**Decision it changes:** Whether the npc-architect pipeline stage (pre-designing arc-completion conditions before play) is a necessary part of the GLYPH session pipeline, or whether DM improvisation produces equivalent arc moments. If designed arcs fire reliably and produce higher scores, the design stage is justified. If not, it could be simplified or removed.

## Target Venue

**Primary:** CHI 2027 — Games and Interactive Experiences track. The paper's contribution is a design pattern (pre-designed arc-completion conditions) with empirical validation. CHI has published NPC design pattern papers (e.g., work on believable agents, social simulation) and interactive narrative design.

**Secondary:** CSCW 2027 — Games and Collaborative Play track. The arc-completion mechanism involves social dynamics (party action triggers NPC response) and has implications for collaborative storytelling tools.

**Tertiary:** IEEE CoG (Computational Intelligence and Games) 2027 — if the paper leans into the AI dungeon master angle, CoG is the appropriate venue for AI-driven NPC behavior analysis.

**Estimated:** 7,500 words, 38 citations, 7 figures.

## Methodology

### The design method
Every significant NPC in the GLYPH adventures has a dedicated `npcs/<slug>.md` file produced by the npc-architect pipeline skill. The file specifies: emotional position, the specific act or line they are capable of delivering, and the exact condition (party action, question, or offer) required to trigger it. The condition is concrete enough that the DM can determine with certainty whether it has been met.

### Arc-completion firing analysis
For each of the ~24 documented instances:
1. Identify the trigger condition specified in the NPC file
2. Identify the party action in the session log that met that condition
3. Classify: fired by character logic (party met condition, NPC responded), DM-scripted (DM chose moment without condition being met), or missed (condition opportunity existed but NPC did not fire)

### Quality effect analysis
Partition sessions by arc-completion count (0, 1, 2+) and test whether Atmospheric Landing and Module Fidelity scores differ across groups (ANOVA or Kruskal-Wallis).

### Simultaneous arc-completion analysis
Special analysis for C2-S04 (4 simultaneous) and C4-S07 (2 simultaneous): what created the convergence condition? Was it planned or emergent? What was the score effect?

### Comparative analysis: designed vs. improvised arc moments
Identify any session-log moments where an NPC produced an emotional beat that was NOT pre-designed (improvised by DM). Compare quality of improvised moments (session log evidence + Atmospheric Landing score) to designed arc-completions. Hypothesis: improvised moments are weaker.

### NPC design pattern extraction
From the ~24 arc-completion instances, extract the structural features of the trigger conditions that fired reliably. Hypothesis: conditions stated as specific observable party actions ("if a party member gives an honest answer to Gorret's specific question") fire more reliably than conditions stated as emotional states ("if the party earns Gorret's trust").

## Sections

### 1. Introduction
- The scripted NPC problem: DMs who pre-script NPC moments produce exposition; moments the party earns feel different
- The design hypothesis: if you pre-specify what an NPC can say and the exact condition for saying it, the party can earn that moment — and the DM does not have to choose when to deliver it
- The GLYPH evidence: 24 arc-completion instances across 28 sessions with 0 requiring DM scripting
- Paper structure and claim

### 2. Related Work
- NPC design in video games: behavior trees, finite state machines, and the limits of scripted NPC behavior (Laird et al., Evans, McCoy et al. on Prom Week)
- Emergent narrative in games: the distinction between pre-scripted story and emergent story (Crawford, Riedl & Young, Mateas & Stern on Facade)
- Social simulation and believable agents: the Belief-Desire-Intention model and its narrative limitations; social simulation (The Sims, Dwarf Fortress) as a precedent for condition-gated behavior
- TTRPG NPC design traditions: the "living world" school (Gygax on NPC motivations, Moldvay on reaction tables, the OSR "rulings not rules" tradition) vs. story game "flagging" systems (Burning Wheel artha, Dogs in the Vineyard)
- Arc-completion as a narrative concept: the theatrical "button" or payoff — what makes a character arc feel complete (Truby, Vogler, McKee)

### 3. The NPC Arc-Completion Design Method
- The arc-completion file structure: emotional position (what the NPC is carrying); arc-completion act (the specific line or gesture); trigger condition (the exact party action required)
- The specificity requirement: "if a party member gives an honest answer to Gorret's specific question" vs. "if the party earns Gorret's trust" — why specificity is the mechanism
- DM discipline: the condition has been met → deliver the arc-completion → do not extend it
- The "smaller than expected" principle: arc-completion moments are not speeches; they are one line, one act, one gesture. The moment is the completion; what comes after is continuance.
- The npc-architect pipeline skill: how it operationalizes the method in the GLYPH system

### 4. The 24-Instance Corpus
- Full inventory of documented arc-completion instances: NPC name, campaign, session, trigger condition, party action that met it, arc-completion line or act, classification (fired by character logic / DM-scripted / missed)
- Trigger condition types: question-answered (Gorret, Veth, Tessamine), act-witnessed (Mig, Doran), care-expressed (Dene, Asholt), recognition-given (Saren, Tomek), mutual-loss-named (Morreth+Sera bilateral), sustained-silence-maintained (Morren)
- Firing-by-character-logic rate: N/24 classified as character logic; rate calculation
- Notable instances in depth: Mig (C3-S1: step through without looking back — condition was cooperative door-opening; act was the physical step); Asholt + Saren (C4-S7: simultaneous convergence — Davan's accounting speech created conditions for both simultaneously)
- The bilateral arc-completion: a sub-type where both an NPC and a PC fire arc-completions simultaneously (Sera+Morreth C2-S03; Thessaly+Vorn C2-S05) — requires both to have pre-designed conditions

### 5. Quality Analysis
- Sessions with arc-completions vs. without: Atmospheric Landing score comparison (mean, SD, statistical test)
- Simultaneous arc-completion sessions (C2-S04, C4-S07): these are the highest-scoring Atmospheric Landing sessions — is the simultaneous firing causally related or coincident?
- Module Fidelity scores for sessions with arc-completions: the NPC arc-completion section in the adventure design constitutes a manifest symptom; when it fires, Module Fidelity benefits
- The "DM does not script" evidence: session logs are analyzed for any language indicating the DM chose the moment rather than the condition being met — this would be a confound; found: zero instances

### 6. Design Pattern Analysis
- Which trigger condition types fired most reliably? Quantitative analysis of condition type vs. firing rate
- The specificity gradient: from most to least specific trigger conditions; correlation with firing reliability
- The "bilateral" design challenge: bilateral arc-completions require pre-designing two arc-completions that share a trigger domain — how this was solved in the 4 documented bilateral instances
- Adventure-level design implications: how many designed arc-completions per session is optimal? (Data suggests 1–2 designed arcs per session fire reliably; 3+ risk overloading the session structure)

### 7. Discussion
- Why "character logic" matters narratively: when the party earns a moment, the moment belongs to the session; when the DM scripts it, it belongs to the DM. The difference is felt even when the resulting line is identical.
- The "smaller than expected" finding: designed arc-completions are consistently smaller than what DMs improvise. Mig does not give a speech; she steps through the door. Smaller moments land harder.
- Generalizing to other narrative AI systems: the trigger-condition design pattern is implementable in any system that has pre-session character design and session-level action logging. Dialogue systems, narrative games, interactive fiction agents.
- Limits: the method requires a pre-session design stage; not all NPCs can be pre-designed; wandering-pressure NPCs and improvised NPCs need a lighter-weight version of the method.

### 8. Conclusion
- The NPC arc-completion design method produces reliable emotional payoffs: 86%+ firing rate, 0 DM scripting required
- The corpus of 24 instances is a design pattern library for NPC-intensive narrative game design
- Simultaneous arc-convergence is the strongest form: when one party action creates conditions for multiple arcs to fire, the result is the session's most memorable moment

## Experiments

- [ ] **EXP-1: Arc-completion firing classification.** For all ~24 documented instances, classify each as: (A) fired by character logic (trigger condition met by party action), (B) DM-scripted (DM chose moment without documented trigger met), (C) missed (trigger opportunity existed, NPC did not fire). Report firing-by-character-logic rate with 95% CI (binomial proportion).
- [ ] **EXP-2: Atmospheric Landing comparison.** Partition 28 sessions into three groups: 0 arc-completions, 1 arc-completion, 2+ arc-completions. Run Kruskal-Wallis test on Atmospheric Landing scores across groups. Report H statistic, p-value, pairwise post-hoc comparisons. Hypothesis: 2+ group scores significantly higher than 0 group.
- [ ] **EXP-3: Trigger condition specificity vs. firing rate.** Rate each trigger condition on a 3-point specificity scale: specific-observable (specific action the party must take), state-based (emotional state the party must create), implicit (no explicit condition documented). Cross-tabulate with firing outcome. Fisher's exact test.
- [ ] **EXP-4: Bilateral arc-completion analysis.** Identify all 4 documented bilateral arc-completions (Sera+Morreth, Thessaly+Vorn, Asholt+Saren, and one from C1). For each: document the shared trigger domain, the two pre-designed conditions, the party action that created both conditions, and the Atmospheric Landing score for that session. Compare bilateral-session AL scores to non-bilateral session mean.
- [ ] **EXP-5: Arc-completions per session vs. score.** Regress session Atmospheric Landing score on arc-completion count (0–4) per session. Test linear vs. diminishing-returns model. Hypothesis: linear up to 2 arcs, then flattening or diminishing returns.
- [ ] **EXP-6: NPC design file completeness analysis.** For each adventure, audit `npcs/*.md` files: does the file contain an explicit arc-completion section with condition and act specified? Rate completeness. Cross-reference: do adventures with complete NPC arc files produce higher arc-firing rates?

## Figures

- [ ] **Figure 1: Arc-completion instance inventory map.** Visual matrix. Rows: 28 sessions (7 per campaign, 4 campaigns). Columns: NPC arc-completion slots. Cells colored: green (fired by character logic), gray (missed), red (DM-scripted), empty (not applicable). Provides instant visual of the 86%+ firing rate.
- [ ] **Figure 2: Trigger condition type distribution.** Pie or bar chart of the ~24 instances by trigger condition type (question-answered, act-witnessed, care-expressed, recognition-given, bilateral). Color-coded by campaign.
- [ ] **Figure 3: Atmospheric Landing scores by arc-completion count.** Box plot. X: arc-completion count (0, 1, 2+). Y: Atmospheric Landing score. Individual data points shown. Kruskal-Wallis test result annotated.
- [ ] **Figure 4: Arc-completion trigger condition specificity analysis.** Scatter plot. X: specificity level (1=implicit, 2=state-based, 3=specific-observable). Y: firing outcome (0=missed, 1=fired). Jittered dots. Logistic regression curve overlaid.
- [ ] **Figure 5: Simultaneous arc-convergence event diagram for C2-S04.** Narrative flow diagram showing: party action (Calder names plague village) → four simultaneous condition-checks → four arc-completions firing. Shows the mechanism of simultaneous convergence.
- [ ] **Figure 6: Example NPC arc file structure.** Annotated example of an npc-architect output file, showing emotional position, arc-completion act, and trigger condition sections. Illustrates the design method for readers unfamiliar with the GLYPH system.
- [ ] **Figure 7: Arc-completion moment size analysis.** Qualitative coding chart. For each documented arc-completion, length of the arc moment in words (the line or act that constitutes the completion). Histogram showing distribution skewed toward very short moments (1–15 words).

## Tables

- [ ] **Table 1: All 24 arc-completion instances.** Columns: NPC name, campaign, session, trigger condition (abbreviated), party action that met condition, arc-completion line or act (abbreviated), classification (A/B/C), session AL score. Full inventory.
- [ ] **Table 2: Trigger condition type × firing outcome cross-tabulation.** Rows: condition types. Columns: fired (A), missed (C), DM-scripted (B). Cell counts. Fisher's exact p-values.
- [ ] **Table 3: The 4 bilateral arc-completions.** Columns: session, NPC-1, NPC-2 (or NPC + PC), shared trigger domain, party action, session AL score. Narrative description of the convergence mechanism.

## Quality Checkpoints

- [ ] **NPC file audit:** Before writing results, audit all adventure `npcs/` directories to confirm that each documented arc-completion has an original NPC file with trigger condition pre-specified. If any arc-completion is documented in the session log but has no corresponding NPC file trigger condition, it must be classified as DM-scripted (Classification B), not character logic.
- [ ] **Session log evidence requirement:** Every arc-completion classified as "fired by character logic" must have a quoted party-action sentence from the session log that maps to the trigger condition. The classification is only as strong as this textual evidence.
- [ ] **Atmospheric Landing score source transparency:** The AL scores used in EXP-2 and EXP-5 are gate scores from `*-gate.md` files. The paper must acknowledge that these scores were produced by the same AI that ran the sessions — a validity threat that the gate/panel convergence in Paper A1 partially mitigates.
- [ ] **"Smaller than expected" operationalization:** The claim that arc-completion moments are smaller than improvised DM moments needs operationalization. Plan: measure word count of the arc-completion line vs. typical DM NPC exposition length in the same session log. Include in Figure 7.

## Dependencies

- `adventures/*/npcs/*.md` — NPC arc file corpus; primary design evidence; required for EXP-1 trigger condition classification
- `adventures/*/sessions/*-log.md` — 28 session logs; party action evidence for each arc-completion instance; required for EXP-1, EXP-3
- `adventures/*/sessions/*-gate.md` — Atmospheric Landing and Module Fidelity dimension scores; required for EXP-2, EXP-5
- `personas/player-styles/npc-arc-completion.md` — the promoted player-style entry; provides the style definition and source instances
- **Upstream:** Paper A1 establishes instrument validity; B1 relies on AL scores as the quality measure for arc-completion effect. B1 must cite A1 for score validity.
- **Upstream:** Paper A2 covers the innovation log entries that promoted npc-arc-completion to player style status — B1 should cite A2 for the discovery mechanism
- **Related:** Paper B2 (player styles) overlaps with B1 on the npc-arc-completion player style; the two papers should cite each other and clearly divide the contribution (B1 focuses on NPC design; B2 focuses on player behavior patterns)
