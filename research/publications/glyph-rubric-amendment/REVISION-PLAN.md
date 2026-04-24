# Revision Plan: glyph-rubric-amendment

**Paper:** Innovation-Cluster-Driven Rubric Amendment: Evidence-Based Evolution of a Playtest Scoring System
**Venue:** NeurIPS D&B 2027 (or redirect to FDG 2027 — see P1)
**Mean Score:** 2.6
**Status:** Revise and Resubmit — venue decision required

---

## Venue Decision (required before any other revision)

Choose one path before beginning revisions:

**Path A — Stay at NeurIPS D&B:**
- Requires P1 full statistical formalization (see below)
- Requires formal algorithm box
- Requires formal convergence or threshold analysis
- Higher effort; higher reward if accepted

**Path B — Redirect to FDG 2027:**
- P1 becomes minor (design rationale replaces formal analysis)
- P2 comparison still recommended but not blocking
- Lower revision effort; higher acceptance probability
- Appropriate venue for the contribution as currently framed

---

## P1 Checklist — Must complete before resubmission

**If staying at NeurIPS D&B:**

- [ ] **Threshold sensitivity analysis**
  - Run pipeline simulation at threshold values 2, 3, 4, and 5
  - For each: count total amendments, compute mean gate trajectory, identify any regression points
  - Add table or figure showing threshold-vs-outcome tradeoff
  - Add one paragraph justifying the chosen threshold value based on this analysis

- [ ] **Formal algorithm box**
  - Add Algorithm 1: Innovation-Cluster-Driven Amendment Procedure
  - Inputs: session log, current rubric version, innovation threshold T
  - Steps: innovation detection, cluster assignment, threshold check, amendment proposal, version increment
  - Outputs: amended rubric version, amendment log entry

- [ ] **Bayesian or frequentist threshold criterion (optional but recommended)**
  - If authors can formalize the threshold selection as a statistical criterion, add as Section 4.1
  - E.g., threshold as the point at which cluster variance exceeds prior score variance

**If redirecting to FDG:**

- [ ] **Replace formal threshold analysis with design rationale**
  - Add 1 paragraph in methodology explaining the 3-innovation threshold as a design decision
  - Acknowledge it as an open calibration question for future work
  - Remove any language claiming the threshold is formally optimized

---

## P2 Checklist — Must complete before resubmission

- [ ] **Add frozen-rubric (v1.0) baseline comparison**
  - Reconstruct or estimate mean gate trajectory under no-amendment condition
  - Add to evaluation section as "Comparison to Static Rubric Baseline"
  - Quantify gap: how much does the amendment pipeline improve mean gate vs. frozen rubric?

- [ ] **Add amendment log as appendix or supplementary table**
  - For each of the 13 version transitions: triggering innovation cluster, dimension amended, amendment type (new dimension / anchor refinement / weight adjustment), measured delta on mean gate
  - Makes pipeline operation fully transparent and reproducible

---

## Do Not Change

- The 120+ innovation instance dataset description — all reviewers cited this as the paper's empirical foundation
- The archetype-burst-and-decay finding — move it more prominent (add figure, move to earlier in evaluation), but do not remove or compress
- The 13-version amendment history — this is the paper's unique empirical contribution

---

## Optional Improvements (P3 / advisory)

- [ ] Add explicit connection to NLP benchmark saturation literature (Raji et al., Gehrmann et al., Ribeiro et al.) in introduction (Liang, Riedl, Bernstein)
- [ ] Add innovation-type classification table (new-dimension / anchor-refinement / weight-adjustment) with per-type counts (Liang, Bogost, Riedl)
- [ ] Note cross-paper dependency: if A1 adds inter-rater reliability for rubric scoring, check whether the same study can include a reliability check for innovation identification (Riedl)
