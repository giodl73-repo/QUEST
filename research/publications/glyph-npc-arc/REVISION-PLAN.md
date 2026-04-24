# Revision Plan: glyph-npc-arc

**Paper:** Designing NPC Arc-Completion Conditions for Session-Invariant Emotional Payoffs in AI-Simulated TRPG
**Venue:** CHI 2027
**Mean Score:** 3.0
**Status:** Accept with Revisions

---

## P1 Checklist — Must complete before resubmission

- [ ] **Add drama management comparison to related work**
  - Characterize drama management's approach to NPC arc resolution: central narrative controller (Riedl & Young), emergent narrative (Louchart & Aylett), mixed-initiative approaches
  - Articulate the architectural distinction: drama management = outcome guarantor; character-logic template = condition specifier
  - Explain the different failure modes: drama management can break player agency to ensure an arc; character-logic relies on the NPC's specified emotional trajectory
  - Length: minimum one full paragraph; ideally a dedicated related-work subsection (0.5–0.75 pages)

- [ ] **Formally define "session-invariant" on first use**
  - Add a one-sentence formal definition: e.g., "An arc-completion is session-invariant if it fires across variations in party composition, encounter route, and session length, without requiring DM intervention to trigger."
  - Apply the definition consistently throughout the paper

---

## P2 Checklist — Must complete before resubmission

Choose Path A or Path B:

**Path A — Conduct independent validation study (preferred)**
- [ ] Recruit 5–10 human DMs or experienced TRPG players as raters
- [ ] Provide 10–15 session transcript excerpts containing NPC arc-completion moments (anonymized)
- [ ] Raters assess each moment: "Was this NPC moment emotionally memorable?" (5-point Likert)
- [ ] Compute correlation between rater scores and rubric NPC Arc-Completion dimension scores
- [ ] Add as Section 5.2: "Independent Validation of Memorable Payoff Operationalization"

**Path B — Revise language and acknowledge gap**
- [ ] Replace all uses of "memorable payoff" with "rubric-score-correlated payoff" or "high-scoring NPC moment" throughout
- [ ] Add to Limitations section: explicit acknowledgment that memorable-payoff operationalization is rubric-internal; describe the circularity; state it as an open validation gap
- [ ] Add to Future Work section: describe the independent validation study (rater protocol, sample size, measures) as concrete next step

---

## Do Not Change

- The 40+ instance count and 88% session coverage figure — headline results cited by all reviewers
- The zero-DM-scripted finding — Morningstar called this the paper's best result; it is
- The three-part design template specification — clear and complete; do not compress
- The cross-campaign breakdown — essential evidence for archetype-independence claim

---

## Optional Improvements (P3 / advisory)

- [ ] Add 1–2 worked NPC arc specifications from the corpus as in-body examples (Murray, Bogost, Morningstar, Bernstein all requested this)
- [ ] Add failure-case analysis: what happened in the 12% of sessions where no arc fired? (Morningstar, Murray)
- [ ] Add arc-completion timing histogram: by scene, by session, by campaign position (Bogost)
- [ ] Add future-work section with player study protocol (Bernstein, Murray)
