# Review Synthesis: Innovation-Cluster-Driven Rubric Amendment: Evidence-Based Evolution of a Playtest Scoring System

**Venue:** NeurIPS D&B 2027
**Mean Score:** 2.6 (Liang 2, Bernstein 3, Bogost 3, Morningstar 3, Riedl 2)
**Recommendation:** Revise and Resubmit — with venue decision required

---

## P1 — Priority 1 (3+ reviewers, blocking)

**Statistical formalization of the amendment threshold.**
Four of five reviewers cited the 3-innovation threshold as lacking formal justification. For NeurIPS D&B specifically, this is a blocking issue. The threshold is the pipeline's operative decision rule, and it is currently a design intuition rather than a principled criterion.

- **Required fix (NeurIPS D&B path)**: Conduct a sensitivity analysis over threshold values (2, 3, 4, 5). Show amendment count and mean gate trajectory for each. Provide a formal criterion (Bayesian, frequentist, or information-theoretic) that the chosen threshold is approximating. Add a formal algorithm box presenting the pipeline as a method.
- **Alternative (venue redirect path)**: If the authors redirect to FDG 2027, the threshold justification becomes a minor issue rather than blocking. FDG reviewers will accept a well-motivated design rationale; they do not require formal convergence analysis.

**Venue decision is required in revision.** The paper cannot succeed at NeurIPS D&B without formal treatment. The authors must either commit to the formalization required for NeurIPS D&B or redirect to FDG/CSCW. Both options are viable; the paper's content is strong either way.

---

## P2 — Priority 2 (2+ reviewers, required for acceptance)

**Comparison to alternative amendment methods.**
Three reviewers noted the absence of a comparison. The most tractable comparison is a frozen-rubric baseline: reconstruct the mean gate trajectory if no amendments had been made after v1.0. If this analysis can be recovered from existing data, it requires no new data collection and would substantially strengthen the pipeline's contribution claim.

- **Required fix**: Add at minimum a frozen-rubric (v1.0 throughout) comparison. Optionally add a periodic-review alternative (e.g., full-rubric review every 10 sessions, no innovation-cluster detection).

---

## P3 — Advisory (1–2 reviewers, strengthens but does not block)

**Venue recommendation: FDG or CSCW.**
Bogost, Riedl, and Morningstar all independently raised the venue question. NeurIPS D&B is a high bar for a contribution that is fundamentally a design and empirical methods paper. FDG 2027 is a natural home; CSCW is also appropriate. The authors should weigh the effort required for NeurIPS formalization against the certainty of a strong FDG submission.

---

## Convergent Strengths (Do Not Revise Away)

- 120+ innovation instances across 13 amendment versions: all reviewers cited this as the paper's empirical foundation. Do not compress it.
- Innovation-cluster-to-amendment pipeline: all reviewers found this conceptually sound. The pipeline's description should be made more formal (algorithm box) but not simplified.
- Archetype-burst-and-decay finding: Bogost and Morningstar both want this made more prominent. It is currently buried; it deserves a dedicated figure and a more prominent position in the evaluation section.

---

## Divergent Notes

- Liang and Riedl are the skeptics — both focused on the NeurIPS formalization gap. Bernstein, Bogost, and Morningstar are more generous, all citing the dataset and pipeline as genuinely valuable contributions.
- No reviewer recommended rejection. The paper's content is accepted on its merits; the question is venue fit and formalization level.
