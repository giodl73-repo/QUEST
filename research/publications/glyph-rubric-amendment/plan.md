---
slug: glyph-rubric-amendment
title: "Innovation-Cluster-Driven Rubric Amendment: Evidence-Based Evolution Across 12 Versions"
paper-type: EMPIRICAL
target-venue: NeurIPS D&B track 2027 or CHI 2027 (Design track)
status: plan
created: 2026-04-21
evidence-base: 120+ logged innovations, 13 rubric versions, 49 sessions across 7 campaigns
primary-number: "120+ innovations across 49 sessions; 13 rubric versions (v1.0-v1.13 proposed); 3 new player-style-adjacent innovations proposed from C5-C7"
---

# Paper Plan: glyph-rubric-amendment

## Research Question

Can a playtest rubric be made self-improving by treating logged innovations as amendment triggers — adopting rubric amendments when two or more innovations cluster in the same dimension? Does the 66-innovation corpus from 28 sessions of AI-simulated D&D playtesting validate the cluster-trigger mechanism, and is the resulting amendment history evidence of systematic, data-driven quality instrument evolution?

## Core Claim

**One falsifiable sentence:** A playtest rubric that treats logged innovations as amendment triggers — adopting amendments when 2+ innovations cluster in the same dimension — improves measurably and systematically, with 28% of the 66 logged innovations triggering rubric changes within 3 sessions of logging.

**Paper type:** EMPIRICAL — mechanism study. The innovation-cluster-amendment pipeline is the independent variable; rubric version count, amendment-to-session lag, and post-amendment score improvement are the dependent variables.

**Falsification condition:** If fewer than 20% of logged innovations contribute to adopted amendments (trigger rate < 20%), or if post-amendment dimension scores show no improvement within 5 sessions of amendment adoption, the mechanism's effectiveness claim fails.

## Quantification Contract

**Primary number:**
- 120+ innovations logged across 49 sessions
- 13 rubric versions produced (v1.0–v1.13 proposed); 28% trigger rate within 3 sessions
- 3 new player-style-adjacent innovations proposed from C5-C7 (professional-code trigger RV1; duty-trigger RV6; situational-no-personal-stakes trigger RV9)
- Amendment-to-score lag: most amendments produce measurable dimension improvement within 3 sessions
- Most amended dimension: Atmospheric Landing (9 of 12 amendment versions through v1.12 touched this dimension)
- Campaign-level trigger rates: C1 drove v1.0→v1.4 (4 versions in 7 sessions); C4 drove v1.9→v1.12 (4 versions in 7 sessions); C5-C7 produced candidate v1.13 innovations

**Falsification condition:** Innovation trigger rate < 20% (fewer than 13 of 66 innovations contributing to amendments), OR no statistically significant post-amendment score increase in the amended dimension within 5 sessions.

**Null fallback:** If trigger rate is high but score improvement is absent, paper reframes as innovation taxonomy: the 66 innovations are a published corpus for future rubric designers regardless of whether amendments improved scores.

**Decision it changes:** Whether the cluster-trigger mechanism is the right design for self-improving evaluation instruments in creative AI systems. If it works, the mechanism is generalizable to other AI creative evaluation tools (story generators, dialogue systems, game narrative engines). If it does not, the paper identifies failure modes and proposes alternative designs.

## Target Venue

**Primary:** NeurIPS 2027 — Datasets and Benchmarks track. The 66-innovation corpus plus 28-session scoring data is a benchmark dataset for AI narrative evaluation. The amendment mechanism is a novel contribution to benchmark construction methodology.

**Secondary:** CHI 2027 — Design and Evaluation track. If NeurIPS D&B is not the right fit, CHI's design track publishes measurement instrument evolution papers and has precedent for creative domain evaluation tools.

**Tertiary:** Games and Cognition venues (CogSci, AAAI AI in Games workshop) — smaller but specialized audience for whom the D&D domain is the primary interest.

**Estimated:** 8,000 words, 45 citations, 6 figures.

## Methodology

### Innovation logging protocol
Each innovation entry in `personas/playtest-innovations.md` includes: session source, dimension tag, quoted passage from session log, explanation of why the rubric did not anticipate it, scope assessment (party-specific / adventure-specific / universal), and status (logged / adopted / promoted-to-style).

### Amendment trigger mechanism
When 2+ innovations carry the same dimension tag, the innovation-scout tool proposes a rubric amendment. The user (DM) reviews and ratifies or rejects. Adopted amendments receive a version increment; constituent innovations are marked `adopted (vX.Y)`. All amendments are forward-only: old session scores do not change.

### Analyses
1. **Innovation corpus analysis:** Dimension distribution of all 66 innovations. Session-level innovation rate over time (does the rate stabilize, increase, or decrease?). Campaign-level innovation rate.

2. **Trigger mechanism analysis:** For each of the 12 amendments, trace constituent innovations, compute cluster size, and measure time-to-trigger (sessions between first innovation and amendment adoption). Compute innovation trigger rate (adopted innovations / total innovations).

3. **Post-amendment score analysis:** For each amendment, extract the amended dimension's mean score in the N sessions before vs. N sessions after (N=3). Test whether post-amendment mean is higher (Wilcoxon signed-rank, N=12 pairs).

4. **Innovation scope analysis:** Cross-tabulate innovation scope (party-specific vs. universal) against eventual adoption status. Hypothesis: universal-scope innovations are adopted at higher rates than party-specific ones.

### The innovation taxonomy
The 66 innovations are classified along three axes: dimension (8 categories), scope (party-specific / adventure-specific / universal), and type (mechanical interaction / reception pattern / NPC behavior / PC agency expression / table-design constraint). The taxonomy is a standalone contribution.

## Sections

### 1. Introduction
- The evaluation feedback loop problem: measurement instruments improve through use, but most rubric-based systems lack a mechanism for incorporating what they learn
- The cluster-trigger proposal: log surprises; cluster by dimension; amend when clustered
- The GLYPH evidence: 66 innovations, 12 amendments, 28 sessions — the first empirical test of this mechanism in a narrative game evaluation context
- Paper structure

### 2. Related Work
- Self-improving evaluation systems: rubric evolution in educational assessment (Herman et al., Jonsson & Svingby), writing assessment (NAEP rubric revision history), automated essay scoring calibration
- Anomaly detection as evaluation signal: prior work in software testing and game QA where unexpected behavior informs test revision
- The "surprise" problem in AI evaluation: current AI benchmarks do not have principled mechanisms for incorporating novel behaviors that fall outside benchmark scope
- Benchmarks as living documents: ongoing work on benchmark contamination, versioning, and maintenance — the amendment mechanism is a contribution to this literature
- Tabletop game innovation literature: the small corpus of work on emergent play patterns in TTRPGs (Zagal, Arnaudo)

### 3. The Innovation-Cluster-Amendment Pipeline
- Stage 1: Innovation logging — playtest-innovation skill extracts SURPRISE-tagged events from session logs, computes dimension cluster, appends to master log
- Stage 2: Cluster detection — threshold logic (2+ same-dimension → amendment proposal; 3+ cross-session → player-style proposal)
- Stage 3: Amendment review — human DM ratifies or rejects; forward-only enforcement; version increment
- Stage 4: Score application — new version applied to sessions scored after the amendment date; old scores preserved
- The full pipeline integrates with the 7-stage session pipeline: innovations are extracted at the LOG stage, before gate scoring, so they can inform the next session's rubric

### 4. The 66-Innovation Corpus
- Session distribution: how many innovations per session (range, mean, mode); whether innovation rate declines with rubric maturity (calibration hypothesis) or remains stable
- Dimension distribution: which dimensions generated the most innovations (hypothesis: Atmospheric Landing, 30+; Character Agency, 20+)
- Scope distribution: universal vs. adventure-specific vs. party-specific; what fraction of each scope was eventually adopted
- Type taxonomy: the five innovation types and their campaign distributions
- Notable innovations by campaign: the 5 most consequential innovations and what they changed (Atmospheric Landing v1.1 chain-reaction; Mechanical Fairness v1.1 cross-dimensional harmlessness; Module Fidelity v1.2 recovery-path; Atmospheric Landing v1.5 act-without-announcement; Character Agency v1.9 sustained behavioral pattern)

### 5. Amendment History Analysis
- Amendment-by-amendment analysis: trigger innovations, cluster size, time-to-trigger, dimension targeted, anchor added
- Campaign-level amendment rates: C1 drove 4 amendments (v1.0→v1.4), C2 drove 1 (v1.5), C3 drove 3 (v1.6, v1.7, v1.8), C4 drove 4 (v1.9→v1.12)
- The Atmospheric Landing concentration: 9 of 12 amendments touched this dimension — what does this say about the difficulty of measuring emotional-narrative quality vs. mechanical quality?
- Amendment scope diversity: amendments ranged from band-level precision adjustments (v1.1 adding "7+" anchors) to entirely new 10-band paths (v1.6 simultaneous arc-convergence)
- No-amendment innovations: the 48 innovations that did not trigger amendments — what did they contribute? (Innovation log growth, player-style promotions, adventure design guidance)

### 6. Post-Amendment Score Analysis
- Pre/post dimension scores for each of the 12 amendments (Figure 4: paired plot)
- Aggregate: mean dimension score change post-amendment across all 12 (expected: +0.4–0.8 points per dimension per amendment)
- Confounds: campaign maturation vs. rubric amendment — design for disentangling
- The Atmospheric Landing trajectory: 9 amendments, starting at mean 8.7/10 in C1 and ending at mean 9.4/10 in C4 — is the incremental improvement attributable to amendments?

### 7. Discussion
- The cluster-trigger mechanism works: innovations cluster predictably by dimension; amendments fire at appropriate thresholds; post-amendment scores improve
- Why Atmospheric Landing concentrates: emotional-narrative quality is harder to specify in advance; mechanical dimensions (Mechanical Fairness, Table Readiness) stabilized early; narrative dimensions required more experiential calibration
- The player-style fork: 18 innovations promoted to styles rather than rubric amendments — what determines whether a cluster becomes a rubric anchor vs. a player-style entry?
- Generalizability to other AI evaluation domains: the mechanism is not D&D-specific; any AI creative system that produces session-level artifacts with surprises can implement cluster-trigger amendment
- Failure modes: the mechanism assumes a human reviewer in the amendment loop; fully automated rubric evolution without review is a risk

### 8. Conclusion
- The 66-innovation corpus is the paper's primary empirical contribution: a published benchmark for AI narrative evaluation
- The cluster-trigger mechanism is the paper's methodological contribution: a principled way to incorporate evaluation surprises into rubric evolution
- The 12-amendment trajectory is the validation: the mechanism produced measurable improvements across 4 campaigns

## Experiments

- [ ] **EXP-1: Innovation rate over time.** Plot innovation count per session (sessions 1–28). Fit a linear or quadratic trend. Hypothesis: rate is roughly stable (innovation rate ≈ 2.4/session), not declining — indicating that rubric maturation does not exhaust the innovation space.
- [ ] **EXP-2: Dimension distribution chi-square.** Expected: innovations uniformly distributed across 8 dimensions (null). Observed: Atmospheric Landing overrepresented. Chi-square test of goodness-of-fit. Report observed vs. expected counts per dimension.
- [ ] **EXP-3: Scope × adoption cross-tabulation.** For all 66 innovations, cross-tabulate scope (party-specific / adventure-specific / universal) against adoption status (adopted / promoted-to-style / unresolved). Fisher's exact test. Hypothesis: universal-scope innovations are adopted at higher rates.
- [ ] **EXP-4: Post-amendment score improvement.** For each of the 12 amendments, compute mean score on the amended dimension in the 3 sessions immediately preceding vs. 3 sessions immediately following the amendment. Wilcoxon signed-rank test on the 12 pre-post pairs. Report: proportion of amendments with positive change, median effect size.
- [ ] **EXP-5: Time-to-trigger distribution.** For each amendment, compute sessions elapsed between first constituent innovation and amendment adoption. Report: range, median, distribution shape. Hypothesis: median ≈ 2 sessions (cluster forms within one campaign, amendment fires before next campaign).
- [ ] **EXP-6: Innovation type × dimension heat map.** Cross-tabulate innovation type (5 categories) against dimension (8 categories) for all 66 innovations. Identify which types concentrate in which dimensions. Expected: reception-pattern innovations in Atmospheric Landing; mechanical-interaction innovations in Mechanical Fairness.

## Figures

- [ ] **Figure 1: Innovation rate per session, sessions 1–28.** Bar chart. X: session ordinal. Y: innovation count. Campaign bands highlighted. Trend line (linear OLS). Advisory/binding boundary annotated.
- [ ] **Figure 2: Innovation dimension distribution.** Horizontal bar chart. 8 dimensions on Y-axis, innovation count on X-axis. Color-coded by scope (party-specific / adventure-specific / universal stacked). Expected vs. observed line for uniform-distribution null.
- [ ] **Figure 3: Amendment timeline with trigger cluster visualization.** Horizontal timeline (v1.0–v1.12). Each amendment shown with bubble: size = cluster count (innovations triggering it), color = dimension. Campaign boundaries as vertical rules.
- [ ] **Figure 4: Pre/post amendment dimension score comparison.** Paired dot plot. Each pair: mean dimension score 3 sessions pre-amendment vs. 3 sessions post-amendment, connected by line. Majority of lines slope upward.
- [ ] **Figure 5: The innovation taxonomy tree.** Tree diagram. Root: "innovation." Level 1: 5 types (mechanical interaction, reception pattern, NPC behavior, PC agency, table-design constraint). Level 2: subtypes with example innovations labeled.
- [ ] **Figure 6: Atmospheric Landing amendment concentration detail.** Single-dimension deep-dive. X: session ordinal. Y: Atmospheric Landing score (0–10). Amendment events annotated with version number and anchor added. Shows the 9-amendment improvement trajectory for this one dimension.

## Tables

- [ ] **Table 1: Full amendment history.** Columns: version, date, dimension, trigger innovations (IDs and short titles), anchor added (summary), sessions-to-adoption from first trigger innovation. 12 rows.
- [ ] **Table 2: Innovation corpus summary by campaign.** Columns: campaign, sessions played, innovations logged, innovations adopted, innovations promoted-to-style, innovations unresolved. 4 rows + totals.
- [ ] **Table 3: Innovation scope × adoption status cross-tabulation.** 3×3 table (scope × status). Cell counts and percentages. Fisher's exact p-value.
- [ ] **Table 4: Top-10 most consequential innovations.** Columns: innovation ID, session, dimension, short description, scope, status, rubric anchor or style created. Curated for narrative impact in the paper.

## Quality Checkpoints

- [ ] **Corpus completeness verification:** Before submission, verify that all 66 innovation entries in `personas/playtest-innovations.md` have accurate status fields (adopted / promoted-to-style / logged). Any discrepancy between TRACKER.md counts and innovation log counts must be resolved.
- [ ] **Amendment traceability:** Every rubric amendment in `personas/playtest-rubric.md` amendment history table must map to at least one innovation entry by ID. If an amendment exists without a traceable innovation, it must be documented as a gap.
- [ ] **Null hypothesis reporting:** EXP-4 (post-amendment score improvement) must report even if results are mixed. The paper cannot selectively report only the amendments that produced score gains.
- [ ] **Player-style vs. amendment fork:** The paper must explain the design decision that routes some clusters to rubric amendments and others to player-style entries (3+ cross-session cluster → style). This is a key mechanism distinction that reviewers will probe.
- [ ] **Generalizability section:** The Discussion must include a concrete proposal for how the cluster-trigger mechanism could be implemented in a non-TTRPG AI evaluation context (e.g., dialogue system evaluation, creative writing rubric evolution).

## Dependencies

- `personas/playtest-innovations.md` — the full 66-innovation corpus; primary data source for all analyses
- `personas/playtest-rubric.md` — rubric v1.0–v1.12 with amendment history table; required for Table 1 and amendment timeline
- `adventures/*/sessions/*-gate.md` — gate scores for post-amendment score analysis (EXP-4)
- `TRACKER.md` — session-level summary including rubric version applied per session
- **Upstream:** Paper A1 (glyph-rubric-instrument) establishes the rubric as a valid instrument; A2 takes the amendment mechanism as its focus and builds on A1's validity claim
- **Downstream:** All other GLYPH papers cite the innovation corpus; A2 is the canonical reference for "how the rubric evolved" claims
- **Dataset release:** The 66-innovation corpus formatted as a JSON/CSV dataset is a planned supplementary release; the paper's EXP section assumes this dataset is prepared for submission
