---
slug: glyph-campaign-spine
title: "The 7-Session Campaign Spine: Evidence-Based Architecture for Emotionally Complete Narrative Arcs"
paper-type: EMPIRICAL (mixed-method)
target-venue: CHI 2027 or IEEE CoG 2027
status: plan
created: 2026-04-21
evidence-base: 7 campaigns, 49 sessions, 7 campaign spine documents, 7 route outcomes
primary-number: "7/7 campaigns completed; 7/7 hint structures delivered; 5/7 Route D or E (C1-C4 + C6 + C7); all 7 PC-authored deliverables produced and logged verbatim"
---

# Paper Plan: glyph-campaign-spine

## Research Question

Does a campaign spine document — pairing a central question with a scheduled 4-hint structure, a trust-token-earning system, and branching end conditions — reliably produce emotionally complete finales across different party archetypes and campaign themes? Can the structural features of a successful campaign spine be extracted from the GLYPH corpus and formalized into a generalizable design pattern?

## Core Claim

**One falsifiable sentence:** A campaign spine document pairing a central question with a scheduled 4-hint structure, a token/trust-earning system, and branching end conditions reliably produces emotionally complete finales across different party archetypes and campaign themes, as evidenced by 4/4 campaigns completing with all hints delivered and 3/4 achieving Route D or E.

**Paper type:** EMPIRICAL (mixed-method) — quantitative campaign outcome analysis plus qualitative comparative analysis of the 4 spine documents and their structural features. The campaign spine design method is the independent variable; campaign completion, route achieved, hint delivery, and PC-authored deliverable success are the dependent variables.

**Falsification condition:** If the 4-hint structure fails to deliver all hints in any campaign (< 4/4), or if the route system fails to differentiate outcomes (all 4 campaigns achieve the same route with no route variation), or if any campaign fails to produce an emotionally complete finale (as scored by Atmospheric Landing ≥ 9/10 in the finale session), the structural reliability claim fails.

## Quantification Contract

**Primary numbers:**
- 7/7 campaigns completed (100% completion rate)
- 7/7 hint structures fully delivered in finale sessions (all hints delivered in-session, on cue)
- Route outcomes: C1 Route D; C2 Route D; C3 Route D; C4 Route E; C5 Route B (false dossier); C6 Route E (journal); C7 Route E (silence)
- 5/7 Route D/E: C1-C4 + C6 + C7; C5 achieved Route B — the system produced route differentiation across 7 campaigns
- 7/7 PC-authored deliverables spoken in finale sessions
- Mean sessions-to-first-binding-PASS: 4.5 (C1-C4 baseline); consistent across C5-C7
- Finale session Atmospheric Landing scores: all 7 campaigns ≥77/80

**Falsification condition:** Any campaign with < 4 hints delivered, or any campaign finale scoring Atmospheric Landing < 9/10, or all 4 campaigns achieving identical routes (no differentiation).

**Null fallback:** If outcomes are consistent but the spine structural features do not explain them (e.g., outcomes are explained by adventure-level design rather than campaign-level architecture), the paper reframes as an adventure-design study rather than a campaign-spine study.

**Decision it changes:** Whether the campaign spine document is the right unit of design for AI-simulated narrative campaigns. If the spine drives outcomes, it should be a required pipeline stage before any campaign begins. If the adventure-level design is sufficient, the spine is an optional planning tool.

## Target Venue

**Primary:** CHI 2027 — Interactive Narrative and Games track. The campaign spine is a design artifact; CHI's tradition of design knowledge papers (including Christopher Alexander's pattern language citations) makes it the right home for a validated design pattern paper.

**Secondary:** IEEE CoG 2027 (Computational Intelligence and Games) — if the analysis leans into the AI simulation angle, CoG is the appropriate venue for AI narrative campaign architecture research.

**Tertiary:** ICIDS 2027 (Interactive Storytelling) — a specialized venue where campaign spine architecture would be the primary contribution to the interactive drama field.

**Estimated:** 8,500 words, 42 citations, 7 figures.

## Methodology

### Comparative case analysis
The 4 campaigns are the unit of analysis (N=4). Each campaign has a campaign spine document specifying: central question, 7-session adventure sequence, artifact tracking, 4-hint structure with delivery schedule, trust-token system, branching end conditions (Routes A/B/C/D/E), and PC spotlight assignments. The spine document is analyzed as a design artifact.

### Structural feature extraction
For each spine document, extract and code: central question type (relational / moral / identity), hint schedule (early-planted / mid-planted / late-planted), token system design (how many tokens, earning conditions, route thresholds), end condition design (number of routes, difficulty gradient, what differentiates them), and PC spotlight assignment (one PC per adventure or rotating).

### Outcome analysis
For each campaign, record: completion status, route achieved, sessions-to-first-binding-PASS, all-hints-delivered session, PC-authored deliverable delivery, and finale AL score. Cross-tabulate structural features with outcomes.

### Qualitative spine comparison
The 4 spines span different themes (grief/artifacts, covenant repair, faith/authority, siege/trust). Qualitative comparison identifies: what the spines share structurally (all 4 have), what varies (and whether variation correlates with route outcome), and what each campaign discovered about the design method that the others did not.

### The 4-hint mechanism deep-dive
The 4-hint structure is the spine's most distinctive element. Trace each hint from planting session through delivery session across all 4 campaigns. Analyze: hint-to-PC alignment (does each hint land on the PC for whom it was designed?), hint-to-route correlation (do Route D/E campaigns have earlier or later hint delivery?), and the simultaneous delivery moment (all 4 hints in the finale session).

## Sections

### 1. Introduction
- Campaign arc completion is the hardest problem in multi-session narrative design: most long-form game campaigns stall, lose coherence, or conclude unsatisfyingly
- The campaign spine hypothesis: a pre-session planning document with a central question, scheduled hints, and branching end conditions can produce reliable emotional completeness across diverse themes and parties
- The GLYPH evidence: 4 campaigns, 4 completions, 4 full hint deliveries, 3/4 Route D/E
- Paper structure

### 2. Related Work
- Long-form narrative structure: Freytag's pyramid, the three-act structure, and their adaptations to serialized fiction (Thompson on TV story arcs, Mittel on complex narrative)
- Campaign design in TTRPGs: the published canon (Paizo's adventure path design, Burning Wheel's beliefs/instincts/traits arc architecture, Apocalypse World's fronts system) — all designed for human DMs; none empirically validated
- AI narrative planning: story arcs in AI narrative systems (Riedl & Young's narrative planning, Porteous et al., Sullivan & Riedl) — academic systems without the playtest data to validate completeness
- Trust and token systems in game design: reputation systems in video games (Mass Effect Paragon/Renegade, Dragon Age approval); tabletop precedents (DW bonds, PBTA moves) — the trust-token system is novel in its session-spanning design
- Convergence patterns in drama: the "all-payoffs-simultaneous" finale as a narrative structure (Aristotle's recognition + reversal; screenwriting on the "obligatory scene") — the 4-hint simultaneous delivery is this structure operationalized

### 3. The Campaign Spine Design Method
- Document structure: central question (one sentence, falsifiable in-fiction); 7-adventure sequence with PC spotlights; 4-hint planting and delivery schedule; artifact/token tracking; end-condition branches (Routes A through E, difficulty-ordered)
- The central question as the spine's organizing principle: how the question's answer differentiates the routes (Route A = partial answer; Route D/E = full inversion or transcendence)
- The 4-hint mechanism: hints are planted in early sessions, retrieved progressively, and delivered simultaneously in the finale. The simultaneous delivery is designed but not forced — the finale conditions create the structural possibility; the party's actions complete it.
- The trust-token system: tokens are earned through specific party actions (not game-mechanical rolls, but narrative choices that demonstrate the PC's central question commitment). Tokens gate routes.
- Branching end conditions: each route is a different kind of answer to the central question. Route A is the minimal answer; Route E is the hardest, most complete answer. The party's token count at the finale determines which routes are available.

### 4. The 4 Campaign Spines: Comparative Analysis
- C1 (Moon-Silver Cycle): central question "can grief be returned to Aelwen's workshop and completed?"; 6 artifacts across 7 adventures; hint structure tied to Aelwen's journal; Route D = Religion 23 at Vaenshold forge
- C2 (Conclave Compact): central question "when a covenant breaks, who bears the cost of mending it?"; 6 shard artifacts; compact spine; Route D = compact spoken whole at convergence
- C3 (Halted Spire): central question "who gets to decide who is worth saving?"; dispensation letter artifact; keystone building; Route D = keystone set with Velantha's name, cathedral commissioned
- C4 (Thorngate Watch): central question "how much of yourself do you spend on people who don't trust you yet?"; 7 trust tokens; supply die attrition; Route E = all 7 tokens + honorable surrender
- Comparative table: structural features across the 4 spines, with column-level analysis of what varies (theme, artifact count, token system design, route count) and what is invariant (central question, 7-adventure sequence, 4-hint structure, simultaneous finale delivery)

### 5. Outcome Analysis
- Campaign completion: all 4/4 completed; what "completed" means operationally (all hints delivered + PC-authored deliverable spoken + finale AL ≥ 9/10)
- Route outcomes and differentiation: C1, C2, C3 achieved Route D; C4 achieved Route E. What did C4 do differently that elevated the route? (Answer: all 7 tokens, hardest end condition, 7-session resource attrition without a long rest.)
- Hint delivery analysis: session-by-session hint delivery tracking across all 4 campaigns. Hint 1 consistently delivered early (Sessions 1–2); Hints 2 and 3 mid-campaign; Hint 4 delivered in or near the finale. All 4 were delivered simultaneously in the finale session for all 4 campaigns.
- Sessions-to-first-binding-PASS: C1 S04, C2 S04, C3 S04, C4 S06. The first 3 sessions are advisory in all campaigns; the 4th session is the first binding session in 3 of 4 campaigns.
- Finale quality evidence: AL scores for all 4 finale sessions (77–79/80); the simultaneous hint delivery event as the structural trigger for high AL in all 4.

### 6. The Trust-Token System in Detail
- Token design across campaigns: C1 has Aelwen artifacts (6 across 7 adventures); C2 has compact shards (6 across 6 adventures); C3 has the dispensation letter + healer's journal; C4 has 7 interpersonal trust tokens (one per NPC, earned through specific acts)
- Token earning conditions: what distinguishes a successful token earn from a failed attempt? Analysis of the 7 C4 token earns as the most detailed case (Tomek, Maret, Hessa, Dene, Luca, Asholt, Saren — all documented with earning condition and party action)
- Token-to-route thresholds: the C4 system is the most fully specified (Route A = 3+ tokens; Route B = 4+ + Dene's; Route E = all 7). How the threshold design prevents both trivial completion and impossible completion.
- Cross-campaign token system abstraction: the common structure across 4 different token designs (trust as the underlying variable; specific acts as the earning mechanism; route thresholds as the output)

### 7. Discussion
- Why the campaign spine works: the central question creates a coherent through-line; the hint structure creates a convergence trajectory; the token system creates stakes that are earned rather than scripted; the branching end conditions create replayability
- The advisory-to-binding calibration: the first 3 sessions being advisory is not just a rubric decision — it is a campaign design decision. The first 3 sessions build the party's relationship with the central question; the binding sessions test whether that relationship produces action.
- Route differentiation as evidence of design integrity: if all campaigns achieved Route D, the system might be trivially achievable. C4's Route E is evidence that the token system can produce differentiated outcomes depending on the party's choices.
- Failure modes not observed but predicted: a campaign could fail if the central question is not answerable through party action (too abstract); if the hint structure plants hints the party cannot retrieve (geometry failure from rubric v1.3); if the token system requires actions the party's character sheets cannot support
- Generalizability: the campaign spine method is not D&D-specific. Any AI-simulated narrative system with multi-session play can implement: central question + progress indicators + branching outcomes. The 4-hint structure is the most domain-specific element (ties to the GLYPH artifact design pattern).

### 8. Conclusion
- 4/4 campaign completions, 4/4 hint deliveries, 3/4 Route D/E: the campaign spine method is validated across theme-diverse campaigns
- The simultaneous finale hint delivery is the structural mechanism that produces emotionally complete finales
- The trust-token system is the mechanism that produces route differentiation and earned outcomes
- The campaign spine document is a validated design artifact; template made available with the paper

## Experiments

- [ ] **EXP-1: Campaign completion analysis.** For each campaign: document the completion criteria (hints delivered, deliverable spoken, finale AL ≥ 9), verify against session logs and TRACKER. Report completion rate with evidence. Sensitivity analysis: if "completion" requires all criteria simultaneously, does any campaign fail? Hypothesis: all 4 meet all criteria.
- [ ] **EXP-2: Hint delivery session mapping.** For each of the 4 hints across each of the 4 campaigns (16 hint instances total), record: plant session, designed delivery session, actual delivery session, delivery mechanism (passive perception / investigation / NPC delivery / auto-delivery). Compute: plant-to-delivery lag (sessions), on-time delivery rate (designed session = actual session), simultaneous finale delivery confirmation.
- [ ] **EXP-3: Trust-token earning condition analysis (C4 deep-dive).** For each of the 7 C4 tokens: document the designed earning condition, the party action that met it, the session, and the session CA score. Test whether token-earning sessions score higher on Character Agency than non-token-earning sessions (Mann-Whitney U).
- [ ] **EXP-4: Route outcome differentiation.** Analyze what structural or performance features distinguish C4 (Route E) from C1–C3 (Route D). Candidate factors: supply die attrition (C4 unique), token count difficulty (C4 required all 7 vs. C2 requiring all 6 shards), combat session ratio, between-session HP carry-over. Log likelihood comparison of candidate explanations.
- [ ] **EXP-5: Simultaneous hint delivery as AL predictor.** Code each session as "simultaneous hint delivery event" (all 4 hints delivered in one session) vs. not. Compare AL scores between event and non-event sessions. Hypothesis: simultaneous delivery sessions score ≥2 points higher on AL than the campaign's mean.
- [ ] **EXP-6: Spine structural feature comparative coding.** Code each of the 4 campaign spine documents on 10 structural features (central question type, hint count, token system type, route count, difficulty gradient, PC spotlight structure, arc length, artifact count, finale conditions, advisory-period design). Identify which features are invariant across all 4 spines and which vary.

## Figures

- [ ] **Figure 1: Campaign completion overview matrix.** 4×5 matrix. Rows: C1–C4. Columns: completion status, route achieved, hints delivered (4/4), deliverable spoken, finale AL score. All cells green = all criteria met.
- [ ] **Figure 2: 4-hint delivery timeline, all 4 campaigns (4 panels).** Per campaign: horizontal timeline, sessions 1–7. Hint plant events (circles) and hint delivery events (stars) for each of the 4 hints. Color-coded by hint number. Shows the convergence trajectory toward simultaneous finale delivery.
- [ ] **Figure 3: Trust-token earning trajectory, C4 (canonical).** Session-level chart. X: sessions 1–7. Y: tokens earned (cumulative). Token-earning events labeled with NPC name and earning condition abbreviated. Route threshold lines (3, 4, 7) annotated. Shows Route E progression.
- [ ] **Figure 4: Campaign spine structural comparison.** Radar/spider chart or table visualization. 10 structural features on axes. 4 campaigns overlaid. Visual identification of invariant features (all 4 spines overlap) vs. variable features.
- [ ] **Figure 5: Route outcome space visualization.** Branching tree from the C4 spine. Leaves: Routes A, B, D, E (labeled with token thresholds and achieved outcome). The achieved route (E) marked. Illustrates the differentiation space the token system creates.
- [ ] **Figure 6: Finale session quality comparison across campaigns.** Grouped bar chart. Sessions 6 and 7 for each campaign (penultimate and finale). Dimensions: Atmospheric Landing, Module Fidelity, Character Agency. Shows consistent elevation in finale sessions vs. penultimate sessions.
- [ ] **Figure 7: Campaign spine template.** Annotated template of a campaign spine document, showing all required sections (central question, adventure sequence, hint structure, token system, end conditions). Based on the actual templates used for C1–C4. Intended as a practical artifact for paper readers.

## Tables

- [ ] **Table 1: Campaign outcome summary.** Columns: campaign ID, theme, central question (abbreviated), sessions played, route achieved, all hints delivered (y/n), deliverable spoken (y/n), finale AL score, party name.
- [ ] **Table 2: 4-hint delivery mapping.** Rows: 16 hint instances (4 hints × 4 campaigns). Columns: campaign, hint number, plant session, designed delivery session, actual delivery session, delivery mechanism, delivery status (on-time / early / late / simultaneous finale).
- [ ] **Table 3: Trust-token system comparison across campaigns.** Columns: campaign, token type, number of tokens, earning condition structure (narrative-act vs. artifact-collect), route thresholds, achieved route, total tokens earned.

## Quality Checkpoints

- [ ] **Spine document accessibility:** Each campaign spine document must be readable by the paper's reviewers. If the documents contain campaign-permanent spoilers that compromise their use as standalone design artifacts, prepare sanitized versions for the supplementary materials.
- [ ] **Route outcome claim specificity:** The paper must precisely define what "Route D" and "Route E" mean for each campaign. They are not identical across campaigns; the paper should not imply that Route D means the same thing in C1 as in C2. Each is a different kind of answer to a different central question.
- [ ] **"Emotionally complete" operationalization:** The claim of "emotionally complete finales" must be operationalized. Plan: AL ≥ 9/10 in the finale gate score, plus the PC-authored deliverable being spoken. Both required. The paper cannot rely solely on reader intuition about "completeness."
- [ ] **C4 Route E exception:** C4 achieved Route E, not Route D. The paper's framing (3/4 Route D/E) treats this as evidence of route differentiation, not as a partial success. This framing must be explicitly defended in the paper — not assumed.
- [ ] **Advisory session design rationale:** The paper claims the advisory-to-binding design is a campaign design decision, not just a rubric scoring decision. This must be argued, not assumed; a reviewer could challenge it as a confound.

## Dependencies

- `docs/campaign/*.md` — 4 campaign spine documents; primary design artifacts for EXP-6 structural coding and Figures 4, 5, 7
- `adventures/*/sessions/*-gate.md` — 28 gate files; required for EXP-5 (AL scores) and Figure 6
- `adventures/*/sessions/*-log.md` — 28 session logs; required for EXP-2 (hint delivery evidence) and EXP-3 (C4 token earning evidence)
- `TRACKER.md` — session-level outcome summary; primary source for Table 1
- `CLAUDE.md` — campaign-permanent facts; required for outcome verification (campaign completion, route achieved)
- **Upstream:** Paper A1 validates the AL scoring; C1's finale analysis depends on valid AL scores
- **Upstream:** Paper A2 covers the innovation mechanism; C1 cross-references the hint structure as a campaign-spine design element that innovations helped refine
- **Related:** Paper C2 (resource exhaustion) covers the C4-specific campaign mechanic (supply die, HP carry-over) that contributed to C4's Route E differentiation. C1 and C2 should cross-reference each other at this junction.
