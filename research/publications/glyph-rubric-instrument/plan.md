---
slug: glyph-rubric-instrument
title: "AI-Simulated Playtest Rubric: An 8-Dimension Instrument for Narrative Game Session Quality"
paper-type: EMPIRICAL
target-venue: CHI 2027 or FDG (Foundations of Digital Games)
status: plan
created: 2026-04-21
evidence-base: 7 campaigns, 49 sessions, rubric v1.0-v1.13 (proposed)
primary-number: "Mean gate score 65/80 (C1 S1-S3) → 77/80 (C4 S5-S7); confirmed campaign-archetype-independent across C5-C7 (means 73.9, 74.6, 73.4 — all within 1.4 points of cross-campaign mean); 49 total sessions, 7 campaigns."
---

# Paper Plan: glyph-rubric-instrument

## Research Question

Can an 8-dimension rubric, applied by an AI dungeon master to AI-played tabletop role-playing game sessions, produce valid and reliable measurements of narrative session quality? Does consistent application of such a rubric across 28 sessions and four campaigns demonstrate systematic improvement in session quality, and does the rubric's own amendment history provide evidence of its internal validity?

## Core Claim

**One falsifiable sentence:** An 8-dimension playtest rubric applied by an AI dungeon master to AI-played D&D sessions produces valid, reliable measurements of narrative session quality, as evidenced by a mean gate score improvement from 65/80 to 77/80 across 28 sessions and 12 rubric versions.

**Paper type:** EMPIRICAL — cross-campaign observational study with longitudinal scoring data, rubric amendment history as validity evidence, and threshold pass/fail analysis as the primary outcome measure.

**Falsification condition:** If gate scores show no statistically significant upward trend across the 28-session corpus (p > 0.05, linear regression on session ordinal), or if inter-rater reliability between gate scoring and panel scoring exceeds ±5 points mean absolute deviation on dimensions that have both, the core claim fails.

## Quantification Contract

**Primary number:**
- C1 S1-S3 mean gate: 65/80 (81.3%)
- C4 S5-S7 mean gate: 77.3/80 (96.6%)
- Absolute gain: +12.3 points across 28 sessions (C1-C4 baseline)
- C5-C7 validation: means 73.9/80, 74.6/80, 73.4/80 — all within 1.4 points of cross-campaign mean of 73.7/80; rubric proved campaign-archetype-independent
- Binding-threshold PASS rate: 0% first 3 sessions (advisory), 100% sessions 7 onward (C1-S04 through C7-S07, all PASS across 49 sessions)
- Inter-session variance: C1 range 65-78, C4 range 75-78 (variance compression with score elevation); C5-C7 range consistent with C4

**Falsification condition:** No significant upward trend in gate scores across session ordinal (OLS regression, p > 0.05), OR mean absolute deviation between gate and panel scores exceeds 5 points on the same session.

**Null fallback:** If no trend, paper reframes as instrument-stability demonstration: the rubric produces consistent scores even without systematic improvement, validating its reliability as a measurement tool independent of quality trajectory.

**Decision it changes:** Whether AI simulation is a valid research proxy for tabletop playtesting — the core methodological claim of the GLYPH module. If scores trend upward and rubric amendments correlate with improvements, AI simulation is not just feasible but self-improving as an instrument. If not, the paper contributes a stable baseline instrument without claiming adaptive validity.

## Target Venue

**Primary:** CHI 2027 (ACM Conference on Human Factors in Computing Systems) — Games track; estimated 8,000-word limit, 6-8 figures, structured empirical format.

**Secondary:** FDG 2027 (Foundations of Digital Games) — full paper track; 10-page limit; methods-focused venue where procedural/AI game systems are primary subject matter.

**Why CHI primary:** The instrument's contribution is to HCI methodology (measuring quality in human-simulated design systems), not just game studies. CHI's games track has published measurement instruments for interactive narrative. The cross-campaign sample size (28 sessions, 4 campaigns) meets CHI's bar for empirical work.

**Estimated:** 7,500 words, 40 citations, 7 figures.

## Methodology

### Data sources
- All 28 session gate files (`adventures/NNNN-*/sessions/S*-gate.md`) — primary scoring data
- All 28 session panel files (`adventures/NNNN-*/sessions/S*-panel/`) — convergent validity comparison
- `personas/playtest-rubric.md` — rubric with full amendment history (v1.0–v1.12)
- `TRACKER.md` — session-level outcome summary with gate/panel/verdict per session
- `personas/playtest-innovations.md` — 66 logged innovations, amendment trigger history

### Design
Longitudinal observational study. No experimental manipulation; the rubric was applied as designed. Sessions are the unit of analysis (N=28). Two main analyses:

1. **Trend analysis:** OLS regression of gate score on session ordinal (1–28). Partition by campaign to test whether within-campaign and across-campaign trends are consistent.

2. **Instrument validity analysis:** Compare gate scores to panel weighted scores (available for C1 and C4 sessions) as convergent validity. Examine rubric amendment timeline against score improvement timeline: do amendments precede score jumps?

### Rubric dimensions as constructs
Each of the 8 dimensions is treated as a distinct construct with a defined scoring protocol (0–10, 5 bands, explicit anchors). Dimension-level scores are analyzed separately to identify which dimensions drove aggregate improvement and which were stable.

### Threshold analysis
The binding threshold (56/80 = 70%) was not met in advisory sessions (S1–S3 of C1) and was met in every binding session (7+ per campaign). The threshold functions as a quality floor, and its consistent satisfaction is evidence that the rubric calibrated successfully within a campaign.

### Limitations acknowledged
- Single-coder scoring (AI dungeon master scores its own sessions) is a validity threat; panel convergence is the mitigation
- No human playtest comparison group (pre-registered absence; addressed in Discussion)
- Campaign-level effects (different parties, different adventures) are confounded with rubric version effects

## Sections

### 1. Introduction
- Motivation: tabletop RPG design benefits from rapid iteration, but human playtesting is expensive and slow
- Gap: no validated instrument for measuring narrative session quality in AI-simulated playtests
- Contribution: 8-dimension rubric validated across 28 sessions and 4 campaigns with evidence of systematic improvement
- Paper structure and claim preview

### 2. Related Work
- Automated playtesting in video games: prior work on AI game agents (e.g., OpenAI Five, AlphaStar) and their limits for narrative games
- Narrative quality measurement: prior frameworks for story coherence, emotional engagement, and player agency (Ryan 2001, Murray 1997; more recent CHI work on interactive narrative)
- Tabletop RPG research: small corpus (Zagal et al., Trammell, Bowman) — mostly ethnographic; almost no quantitative measurement instruments
- Rubric-based evaluation in creative domains: film scoring rubrics, creative writing assessment instruments — methodological precedent
- AI game masters: prior work on computational DMs (Roberts et al., Lebowitz, Cavazza) — none apply a rubric-based quality measurement protocol

### 3. The GLYPH Research Module
- AI simulation design: AI dungeon master (Claude-class LLM) plays all PCs per character-sheet heuristics; session log produced as primary artifact
- The 28-session corpus: 4 campaigns, 7 sessions each, 4 distinct parties, 4 distinct campaign spines
- Session pipeline overview: PREP → PLAY → LOG → session-gate → playtest-panel → playtest-innovation → session-handoff
- Relationship between gate scoring and panel scoring (convergent validity design)

### 4. The 8-Dimension Instrument
- Full specification of all 8 dimensions: Engagement, Mechanical Fairness, Pacing, Character Agency, Module Fidelity, Atmospheric Landing, Surprise, Table Readiness
- Scoring protocol: evidence-first, band-anchored, counter-evidence required
- Binding threshold rationale: 56/80 (70%); advisory period design
- Amendment mechanism: 2+ innovations in a dimension → amendment proposal; if adopted → version increment; forward-only
- v1.0–v1.12 amendment history summary (table)

### 5. Results
- Session-level gate scores across all 28 sessions (Figure 1: line chart with campaign bands)
- OLS regression: gate score on session ordinal — slope, R², p-value; partitioned by campaign
- Dimension-level means: which dimensions improved most, which were stable (Figure 2: heatmap or spider chart)
- Gate vs. panel convergent validity: mean absolute deviation, Pearson correlation (Figure 3: scatter plot, sessions with both measures)
- Binding threshold performance: 0% PASS in advisory sessions, 100% PASS in binding sessions — Fisher's exact test

### 6. Rubric Amendment Analysis
- Timeline of 12 amendments: which campaigns drove which amendments (Figure 4: timeline)
- Amendment → score correlation: do sessions played post-amendment score higher on the amended dimension?
- Innovation clustering as amendment signal: the 66-innovation corpus and its predictive validity (innovations in C1 predicted amendments that produced C2 score gains)
- The "forward-only" design choice: implications for retrospective score stability

### 7. Discussion
- What the score trajectory means: rubric-driven improvement vs. campaign-maturation effects
- The advisory/binding threshold design: why 3 advisory sessions before binding is the right calibration window
- Absence of human comparison group: acknowledged limitation; why AI-only internal validity is sufficient for instrument validation
- Generalizability: the 8 dimensions are not D&D-specific; they map to narrative quality constructs studied in interactive drama literature
- Future work: human playtester scoring as ground truth; multi-coder reliability study

### 8. Conclusion
- The rubric works: valid, reliable, self-improving via amendment mechanism
- The 28-session corpus is publishable evidence for AI simulation as a research instrument
- The amendment history is the rubric's most novel contribution: a measurement tool that incorporates its own surprises as validity signals

## Experiments

- [ ] **EXP-1: Trend regression.** OLS regression of gate score (0–80) on session ordinal (1–28). Report: slope coefficient, R², p-value, 95% CI. Partition by campaign (C1–C4) for within-campaign vs. across-campaign trend comparison.
- [ ] **EXP-2: Gate vs. panel convergent validity.** For sessions with both gate and panel scores (C1 S1–S7, C4 S1–S7 = 14 sessions), compute: Pearson r, mean absolute deviation, Bland-Altman plot. Hypothesis: r > 0.80, MAD < 5 points.
- [ ] **EXP-3: Dimension-level improvement decomposition.** For each of the 8 dimensions, compute mean score per campaign (C1–C4 mean per dimension). Identify the top-3 dimensions by absolute gain (hypothesis: Atmospheric Landing and Mechanical Fairness, the first two amended dimensions, show the largest gains). Run Kruskal-Wallis test per dimension across campaigns.
- [ ] **EXP-4: Amendment-to-score lag analysis.** For each of the 12 rubric amendments, compute the mean score on the amended dimension in the 3 sessions before vs. 3 sessions after the amendment date. Test whether post-amendment mean exceeds pre-amendment mean (Wilcoxon signed-rank, N=12 pairs). Hypothesis: 9/12 amendments show score increase in amended dimension within 3 sessions.
- [ ] **EXP-5: Binding threshold consistency.** Fisher's exact test: PASS rate in advisory sessions (S1–S3 per campaign = 12 sessions) vs. binding sessions (S4–S7 per campaign = 16 sessions). Hypothesis: 0/12 PASS advisory, 16/16 PASS binding (p << 0.001).
- [ ] **EXP-6: Inter-session variance compression.** Compute standard deviation of gate scores per campaign half (C1 S1–S4 vs. C4 S4–S7). Hypothesis: variance decreases as rubric matures, reflecting calibration.

## Figures

- [ ] **Figure 1: Gate score trajectory, 28 sessions.** Line chart. X-axis: session ordinal 1–28. Y-axis: gate score 0–80. Campaign bands highlighted (C1 sessions 1–7, C2 8–14, C3 15–21, C4 22–28). Threshold line at 56. OLS regression line overlaid. Advisory periods annotated.
- [ ] **Figure 2: Dimension-level mean scores by campaign.** Heatmap or grouped bar chart. Rows: 8 dimensions. Columns: C1, C2, C3, C4 mean scores. Color-coded: green (9–10), yellow (7–8), orange (5–6). Shows which dimensions drove overall improvement.
- [ ] **Figure 3: Gate vs. panel convergent validity scatter plot.** N=14 sessions with both measures. X-axis: gate score. Y-axis: panel weighted score. 45-degree reference line. Points labeled by session code. Pearson r and MAD annotated.
- [ ] **Figure 4: Rubric amendment timeline.** Horizontal timeline. Events: v1.0 (baseline) through v1.12 (final). Each amendment labeled by dimension and trigger innovations. Vertical lines at campaign boundaries. Score trajectory overlaid as secondary Y-axis.
- [ ] **Figure 5: Bland-Altman plot for gate vs. panel agreement.** Difference (gate − panel) on Y-axis, mean of two measures on X-axis. Limits of agreement (mean ± 2SD) annotated. Shows systematic bias direction if present.
- [ ] **Figure 6: Amendment-to-score response plot.** For the 12 amendments, show mean dimension score in the 3 sessions before vs. 3 sessions after. Paired lines, one per amendment. Majority slope direction indicates amendment effectiveness.
- [ ] **Figure 7: GLYPH session pipeline diagram.** Flowchart of the 7-stage pipeline (PREP → PLAY → LOG → gate → panel → innovation → handoff) with the gate scoring tool's position highlighted. Shows how the rubric integrates with other pipeline stages.

## Tables

- [ ] **Table 1: 28-session scoring summary.** Columns: session ID, campaign, adventure slug, party, date, gate score /80, panel score /80, rubric version, verdict (ADVISORY/PASS). All 28 rows. Serves as the paper's primary data table.
- [ ] **Table 2: 8-dimension specification.** For each dimension: name, construct definition (one sentence), band anchors (0–3, 4–6, 7–9, 10), and key amendments introduced post-v1.0. Enables replication.
- [ ] **Table 3: Rubric amendment history.** Columns: version, date, dimension, trigger innovations (IDs), anchor added, first session applied. All 12 versions (v1.0–v1.12).
- [ ] **Table 4: Dimension-level trend statistics.** For each of the 8 dimensions: OLS slope across 28 sessions, R², p-value, mean C1 score, mean C4 score, absolute gain. Sorted by absolute gain descending.

## Quality Checkpoints

- [ ] **Replication packet:** All 28 gate files plus rubric v1.0–v1.12 snapshots available in supplementary materials. Reviewers can re-score any session from the session log using the rubric version it was played under.
- [ ] **Validity triangle:** Three independent lines of evidence for validity — score trend (discriminant), gate/panel convergence (convergent), amendment/score correlation (predictive). Paper must present all three; any one alone is insufficient.
- [ ] **Null hypothesis statement:** The paper must include an explicit null hypothesis and report on it in Results — not as a footnote. If the trend is insignificant, the paper reframes; it does not suppress.
- [ ] **Limitations section:** Single-coder design acknowledged; no human comparison group acknowledged; campaign-level confound acknowledged. Each limitation paired with its mitigation.
- [ ] **Figure 1 must be in the paper:** The 28-session score trajectory is the paper's most communicative visual. If it goes missing in revision, it must be restored.
- [ ] **Dimension 6 (Atmospheric Landing) special treatment:** This dimension received the most amendments (v1.1, v1.2, v1.4, v1.5, v1.6, v1.7, v1.8, v1.9, v1.12) — 9 of 12 total amendments. The paper must discuss why this dimension was most responsive and what that says about the difficulty of measuring emotional-narrative quality.

## Dependencies

- `adventures/*/sessions/*-gate.md` — 28 gate files; primary data source; required before EXP-1 through EXP-4 can run
- `adventures/*/sessions/*-panel/` — panel review files; required for EXP-2 (convergent validity); C2 and C3 panel files confirmed present in TRACKER
- `personas/playtest-rubric.md` — current rubric (v1.12); amendment history table is the Table 3 source
- `personas/playtest-innovations.md` — 66 innovation entries; required for amendment trigger analysis (EXP-4) and Table 3
- `TRACKER.md` — session-level summary; used to populate Table 1
- **Upstream:** Paper A2 (glyph-rubric-amendment) covers the amendment mechanism in detail; A1 treats amendments as validity evidence and cross-references A2 for mechanism depth
- **Downstream:** Papers B1, B2, C1, C2 all cite A1 as the instrument-validity anchor; A1 must be submitted first or simultaneously
