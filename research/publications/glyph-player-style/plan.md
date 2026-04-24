---
slug: glyph-player-style
title: "PC-Authored Deliverables and Emergent Player Styles in AI-Simulated TRPG"
paper-type: EMPIRICAL
target-venue: FDG 2027 or CHI 2027 (games track)
status: plan
created: 2026-04-21
evidence-base: 7 promoted player styles, 120+ innovations, 49 sessions across 7 campaigns
primary-number: "7 player styles promoted; 7 campaigns; RV1-RV4 (C5) and RV9-RV12 (C7) confirmed styles are campaign-archetype-independent. Total instances: sheet-deep-reader ~50, craft-witness ~45, act-without-announcement ~25, npc-arc-completion ~40, verbal-documentation-arc ~15, documentary-witness ~12, [act-without-announcement intra-session v1.12] ~8"
---

# Paper Plan: glyph-player-style

## Research Question

When PC character sheets include multi-session deliverable arcs — speeches, documents, or named acts built toward across 3–6 sessions — do AI-simulated players produce them consistently in finale sessions? And across 28 sessions and 105 innovations, can a systematic innovation-clustering process extract generalized, promotable player behavior styles that are stable across different parties, campaigns, and AI simulation runs?

## Core Claim

**One falsifiable sentence:** When PC character sheets include multi-session deliverable arcs (speeches, documents, or named acts built toward across 3–6 sessions), AI-simulated players produce them consistently in finale sessions; the same play corpus generates emergent, promotable player styles at a rate of 6 distinct styles from 105 innovations across 28 sessions.

**Paper type:** EMPIRICAL — two-part study. Part 1: PC-authored deliverable analysis (4 finale deliverables; delivery rate; session trajectory leading to delivery). Part 2: Player-style emergence analysis (6 styles, instance counts, cross-campaign stability, design implications).

**Falsification condition:** If fewer than 3 of the 4 PC-authored finale deliverables are delivered in their designed session (delivery rate < 75%), or if any of the 6 promoted player styles cannot be confirmed with 3+ instances across 2+ sessions, the emergence and delivery claims both fail.

## Quantification Contract

**Primary numbers:**
- 7 PC-authored finale deliverables across 7 campaigns; 100% delivery rate in finale sessions
- 7 player styles promoted: sheet-deep-reader, craft-witness, act-without-announcement, npc-arc-completion, verbal-documentation-arc, documentary-witness, [act-without-announcement intra-session v1.12]
- Total instances (all 49 sessions): sheet-deep-reader ~50, craft-witness ~45, npc-arc-completion ~40, act-without-announcement ~25, verbal-documentation-arc ~15, documentary-witness ~12, [act-without-announcement intra-session] ~8
- RV1-RV4 (C5) and RV9-RV12 (C7) confirmed styles are campaign-archetype-independent: styles fired from professional code (RV1), from duty (RV6), and from situational triggers with no designed personal stakes (RV9)
- Style-to-innovation ratio: 7 styles from 120+ innovations

**Falsification condition:** Delivery rate < 75% (< 3/4 deliverables in designed session), OR any promoted style confirmed with fewer than 3 instances across 2 sessions.

**Null fallback:** If deliverable delivery is inconsistent, paper reframes as design requirement analysis: what character sheet features predict reliable deliverable delivery? The 4 cases provide enough variation to identify predictors even if not all deliver.

**Decision it changes:** Whether multi-session PC deliverable arcs are a reliable technique for AI-simulated narrative campaigns. If 4/4 deliver at 100%, the technique is validated and should be a standard campaign design tool. If not, the paper identifies the structural requirements for reliable delivery.

## Target Venue

**Primary:** FDG 2027 (Foundations of Digital Games) — full paper track. FDG is the premier venue for game design research; player-style emergence from a structured design corpus is exactly FDG's scope. The paper will be among the few FDG papers with a 28-session AI simulation dataset.

**Secondary:** CHI 2027 — Games and Interactive Experiences track. The PC-authored deliverable finding speaks to human-AI collaborative storytelling design, which is an active CHI research area.

**Estimated:** 7,000 words, 35 citations, 8 figures.

## Methodology

### Part 1: PC-authored deliverable analysis
For each of the 4 deliverables:
1. Identify the deliverable from the campaign spine document (what it is, when it was designed to be delivered)
2. Trace the multi-session trajectory: which sessions built toward it (scene references from session logs)
3. Measure the delivery: was it delivered in the designed session? Was it delivered verbatim or paraphrased?
4. Analyze the structural conditions that enabled delivery: what did the party do across sessions to build the PC's capacity to deliver?

### Part 2: Player-style emergence analysis
For each of the 6 promoted styles:
1. Identify the innovations that triggered style promotion (from playtest-innovations.md)
2. Count instances, sessions, and campaigns represented
3. Classify the style by type: behavioral pattern (act-without-announcement, craft-witness), design-interaction (sheet-deep-reader), social dynamic (npc-arc-completion), arc structure (verbal-documentation-arc), documentary practice (documentary-witness)
4. Analyze cross-campaign stability: does the style appear in campaigns where it was not discovered (prospective validation)?

### PC-authored deliverable structural analysis
The 4 deliverables were designed as multi-session arcs. Structural features to measure: number of sessions in the arc (3–7), number of designated building moments (scenes that explicitly advance the deliverable), number of obstacles or setbacks, whether the deliverable was built into the PC sheet vs. emergent from play.

### Style discovery rate analysis
Compute the innovation-to-style conversion rate per campaign. Hypothesis: the rate stabilizes after C1 (styles are discovered early; later campaigns refine existing styles rather than producing new ones). Test: chi-square on style-promotion events per campaign.

## Sections

### 1. Introduction
- The challenge of multi-session arcs in AI simulation: can an AI-simulated player build toward a deliverable across 6 sessions without drift, out-of-character behavior, or pre-mature delivery?
- The player-style emergence question: when a novel behavior pattern appears in AI-simulated play, can it be formalized into a reusable design primitive for future adventures?
- The GLYPH evidence: 4 deliverables, 100% delivery rate, 6 styles from 28 sessions

### 2. Related Work
- Player types and player styles in TTRPGs: Bartle's player types (Explorer, Achiever, Killer, Socializer) as the canonical but video-game-centric taxonomy; Yee's motivational taxonomy; Edwards' GNS theory — all pre-AI-simulation
- Emergent gameplay patterns: Crawford on interactive storytelling, Salen & Zimmerman on emergent vs. embedded narrative, Juul on emergence in games
- Character arc design: multi-session deliverable design in traditional narrative structure (McKee, Truby); the "setup-payoff" arc across multiple acts as a formal narrative technique
- AI character consistency: prior work on AI character long-term behavioral consistency (Shaker et al., Liapis), mostly in video games; almost no work on TTRPG PC consistency across sessions
- Design patterns in game design: the concept of "design patterns" as reusable solutions (Bjork & Holopainen); player styles as behavioral design patterns

### 3. PC-Authored Deliverables: Method and Instances
- Definition: a multi-session deliverable arc is a speech, document, or named act that the PC is designed to produce in a specific finale session, built toward across 3+ sessions of play
- Structural requirements for reliable delivery: (a) the deliverable is named and described in the PC sheet before the campaign begins; (b) the campaign spine document specifies the session for delivery; (c) at least 3 building moments are designed across the campaign; (d) the DM's session design creates the conditions for delivery without scripting the delivery itself
- The 4 instances: Davan's accounting speech, Thessaly's opening sentence, Calla's account, Grom's confession — deep analysis of each

### 4. Deliverable Trajectory Analysis
- Session-by-session building moment mapping for each deliverable: which scenes advanced the arc, which created obstacles, which tested whether the PC would deliver early (and did not)
- The "building without pre-delivery" design challenge: PCs with deliverable arcs must be prevented from delivering prematurely (before S07). Three design solutions observed: (a) the conditions for delivery require the full campaign's stakes to be established; (b) the deliverable requires specific witnesses or physical objects only available late in the campaign; (c) the PC's arc includes an explicit "not yet" beat in mid-campaign that delays delivery without negating it
- Verbatim vs. paraphrased delivery: 3/4 deliverables were delivered substantially verbatim (the text emerged from the PC's accumulated campaign experience); 1/4 was paraphrased (Thessaly's opening sentence was written in margin then spoken). All 4 count as delivered.
- The Grom Confession as the canonical case: verbatim session log, all 4 campaign hints simultaneously delivered, the ingot placed — the finale condition is the most complex of the four and the most thoroughly documented

### 5. Player-Style Emergence
- The discovery process: innovations appear in session logs; the playtest-innovation skill clusters them; at 3+ instances across 2+ sessions, a style is proposed and reviewed
- The 6 promoted styles — brief profile of each: what it is, when it was first observed, the instance count at promotion, which campaigns validated it, the design implication it produces
- Style type taxonomy: 5 types — behavioral pattern (act-without-announcement), craft-ritual practice (craft-witness), sheet-interaction (sheet-deep-reader), social dynamic (npc-arc-completion), arc structure (verbal-documentation-arc / documentary-witness)
- Instance counts at promotion vs. current (all 28 sessions): styles continue to accumulate instances after promotion — the promotion threshold (3 instances, 2 sessions) is a lower bound, not a ceiling

### 6. Cross-Campaign Style Stability
- For each style, trace its occurrence across all 4 campaigns (not just the discovery campaign). Craft-witness, for example, was discovered in C1 but confirmed in C2 (Orik), C3 (Maret), and C4 (Sava). This prospective confirmation is the strongest validity evidence.
- The session-invariant property of craft-witness and sheet-deep-reader: once a PC fires the pattern in session 1 of their campaign, they fire it every session. This is the most novel finding — a player style that is not occasional but structural.
- Styles that are campaign-specific vs. universal: npc-arc-completion fires everywhere there are pre-designed NPCs; documentary-witness may be party-specific (Caelith in C4)

### 7. Design Implications
- PC sheet design requirements for deliverable arcs: the 4 structural requirements; a checklist for adventure designers building this pattern
- Style-aware adventure design: when you know your party includes a craft-witness, you design structural elements that give the craft-ritual something to listen for. When you have a sheet-deep-reader, you plant sheet-activatable connections in the adventure.
- The innovation → style pipeline as a design knowledge capture system: each promoted style is a design pattern extracted from emergent play data. The pipeline is a method for systematically capturing what works.
- Style combinations: some styles compound (sheet-deep-reader + craft-witness produces the deepest per-PC atmospheric reception); the paper explores which combinations are documented and which are predicted by the evidence

### 8. Conclusion
- 4/4 PC-authored deliverables delivered at 100% rate: the multi-session deliverable arc is a validated technique for AI-simulated narrative campaign design
- 6 player styles emerged from 28 sessions: the innovation-cluster-promotion pipeline is a viable method for extracting behavioral design patterns from AI play data
- The session-invariant property of structural styles (craft-witness, sheet-deep-reader) is the paper's most novel finding — and the most important for future PC sheet design

## Experiments

- [ ] **EXP-1: Deliverable delivery rate.** For each of the 4 PC-authored deliverables: (1) document the designed session, (2) search the session log for delivery evidence, (3) classify as delivered / partially delivered / not delivered. Report delivery rate with 95% CI (binomial). Sensitivity analysis: if partially delivered counts as delivered, does the rate change?
- [ ] **EXP-2: Building moment coverage.** For each deliverable, count the number of building moments designed into the campaign (from campaign spine doc) vs. building moments actually observed in session logs. Compute coverage rate. Hypothesis: all 4 deliverables have ≥75% building moment coverage (at least 3/4 designed moments fired).
- [ ] **EXP-3: Style instance count by campaign.** For each of the 6 styles, count instances per campaign (C1, C2, C3, C4). Compute: discovery campaign, first prospective validation campaign, total instances. Cross-tabulate: which styles are confirmed in all 4 campaigns? Which are confirmed in 2+ campaigns?
- [ ] **EXP-4: Session-invariant property test.** For styles with session-invariant claims (craft-witness, sheet-deep-reader), analyze all sessions in which a PC with that style played: what fraction of sessions produced an instance of the style? Hypothesis: 95%+ sessions with a craft-witness PC produced a craft-witness moment.
- [ ] **EXP-5: Innovation-to-style conversion rate by campaign.** For each campaign, compute: total innovations logged / innovations promoted to styles. Compare conversion rates across C1–C4. Test whether the rate declines (style saturation hypothesis) or remains stable.
- [ ] **EXP-6: Style type distribution.** Cross-tabulate the 6 styles by type (5 categories). Test whether the type distribution is uniform (chi-square goodness-of-fit). Hypothesis: behavioral patterns and craft practices are overrepresented relative to arc structures — because behavioral patterns are more session-invariant and thus more observable.

## Figures

- [ ] **Figure 1: PC-authored deliverable trajectory maps (4 panels).** For each deliverable, a session-level timeline showing: building moments (marked green), obstacles or setbacks (marked orange), "not yet" beats (marked red), and delivery session (marked gold star). 4 panels, one per deliverable, arrayed vertically.
- [ ] **Figure 2: Player-style emergence timeline.** Horizontal timeline showing all 28 sessions. Marked events: first instance of each style (colored by style), promotion event (flag), prospective confirmation in later campaigns (circles). 6 styles as 6 colored tracks.
- [ ] **Figure 3: Player-style instance counts at promotion vs. final count.** Bar chart. X: 6 style names. Y: instance count. Two bars per style: count at promotion (lighter) and count at end of corpus (darker). Shows styles continue accumulating after promotion.
- [ ] **Figure 4: Session-invariant property visualization for craft-witness.** Line chart of all sessions featuring a craft-witness PC (all 28 sessions if a craft-witness PC is in every campaign). Binary Y-axis: style fired / not fired. Expected: near-100% firing rate across all sessions.
- [ ] **Figure 5: Style type taxonomy diagram.** Tree or cluster diagram. Root: "player style." Branches: 5 types. Leaves: the 6 promoted styles, each with instance count and discovery campaign annotated.
- [ ] **Figure 6: Deliverable verbatim analysis.** For each of the 4 deliverables, a side-by-side comparison of the character sheet description (the designed deliverable) vs. the session log text (what was actually delivered). Highlights: verbatim passages, paraphrases, and emergent additions not in the sheet design.
- [ ] **Figure 7: Style combination matrix.** 6×6 matrix. Cell: number of sessions in which both styles fired simultaneously. Darker cells = more co-occurrence. Identifies style combinations that compound (e.g., craft-witness + sheet-deep-reader in the same session).
- [ ] **Figure 8: Innovation → style pipeline diagram.** Flowchart of the style promotion mechanism. Shows: innovation logged → cluster check (3+ / 2 sessions) → style proposed → user review → style ratified → instances continue accumulating. Position in the 7-stage session pipeline annotated.

## Tables

- [ ] **Table 1: PC-authored deliverable inventory.** Columns: PC name, campaign, deliverable type (speech / document / named act), sessions in arc, designed delivery session, actual delivery session, delivery status (verbatim / paraphrased / not delivered), session gate score at delivery.
- [ ] **Table 2: Player-style inventory.** Columns: style slug, discovery date, discovery session, trigger innovations (IDs), instance count at promotion, total instances (all 28 sessions), campaigns with confirmed instances, session-invariant property (yes/no/partial).
- [ ] **Table 3: Style design implications.** For each style: design requirement (what the adventure/PC sheet must contain for the style to fire), design signal (how the DM knows the style has fired in a session log), design amplifier (what makes the style fire more strongly).

## Quality Checkpoints

- [ ] **Verbatim session log evidence for each deliverable:** Every claim about a deliverable being "delivered" must be supported by a direct quote from the session log. The paper must include at minimum one extended quote per deliverable (minimum 50 words from the session log).
- [ ] **Style promotion threshold documentation:** Each style entry in `personas/player-styles/` must be traceable to its constituent innovations in `personas/playtest-innovations.md`. If the traceability chain is broken for any style, that style's section must be marked as requiring additional evidence.
- [ ] **Cross-campaign confirmation:** The paper's strongest claim for styles is cross-campaign confirmation (a style discovered in C1 appearing in C3 without explicit re-design). This prospective confirmation must be documented with session-log evidence, not just TRACKER entries.
- [ ] **"Session-invariant" claim specificity:** The paper uses "session-invariant" to mean "fires in every session where a PC with the style is present." This must be operationally defined in the methods section and tested in EXP-4, not just claimed.
- [ ] **Documentary-witness style status:** At the time of planning, documentary-witness was proposed at C4-S07 but not fully confirmed with 3+ instances across 2 sessions. If the confirmation is absent at writing time, the paper should present it as a candidate style rather than a promoted style.

## Dependencies

- `personas/player-styles/*.md` — the 6 promoted style files; primary design documents
- `personas/playtest-innovations.md` — 105 innovations with cluster/promotion history; required for EXP-5, Table 2 traceability
- `adventures/*/sessions/*-log.md` — 28 session logs; required for deliverable delivery evidence (EXP-1, EXP-2) and style instance counting (EXP-3, EXP-4)
- `docs/campaign/*.md` — campaign spine documents; required for deliverable design specification (Part 1 structural analysis)
- `personas/parties/*/*.md` — PC character sheets for all 4 campaigns; required for deliverable arc design documentation
- **Upstream:** Paper A2 covers the innovation-cluster mechanism that promotes styles; B2 relies on the mechanism being validated
- **Upstream:** Paper A1 validates the scoring instrument; B2's quality effect analysis (do deliverable sessions score higher?) requires valid AL and CA dimension scores
- **Related:** Paper B1 (NPC arc-completion) covers the npc-arc-completion style specifically; B2 should cite B1 for that style's NPC design side and distinguish its own focus on party behavior patterns
