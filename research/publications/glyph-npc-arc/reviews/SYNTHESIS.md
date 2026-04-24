# Review Synthesis: Designing NPC Arc-Completion Conditions for Session-Invariant Emotional Payoffs in AI-Simulated TRPG

**Venue:** CHI 2027
**Mean Score:** 3.0 (Murray 3, Riedl 3, Bogost 3, Morningstar 4, Bernstein 2)
**Recommendation:** Accept with Revisions

---

## P1 — Priority 1 (3+ reviewers, blocking)

**Drama management comparison is thin.**
Four of five reviewers cited this. The paper positions itself against DM scripting but does not adequately engage with drama management theory (Riedl & Young's narrative planner, Louchart & Aylett's emergent narrative) as the academic foil. This is the paper's primary theoretical gap.

- **Required fix**: Add a substantive comparison (minimum one full paragraph, ideally a dedicated related-work subsection) characterizing drama management's approach to NPC arc resolution and explaining why the character-logic template is distinct in kind, not just implementation. The argument should be: drama management uses a central narrative controller to ensure story outcomes; character-logic-driven arc-completion uses the NPC's specified emotional state as the sufficient condition. These are different architectural commitments with different failure modes.

---

## P2 — Priority 2 (2+ reviewers, required for acceptance)

**Operationalize "memorable payoff" independently of the rubric score.**
Bernstein and Bogost both raised the circularity concern. The rubric was designed around these sessions; using rubric scores as evidence for "memorable payoffs" is self-referential. Two paths:

- **Path A (preferred)**: Conduct a small independent validation study. Have human DMs or players rate a sample of session transcripts for NPC moment memorability, blind to rubric scores. Report correlation with rubric scores. Even weak correlation is useful evidence.
- **Path B (revision without new study)**: Revise all "memorable payoff" language throughout the paper to "rubric-score-correlated payoff" and add an explicit acknowledgment of the operationalization gap in the limitations section. Describe the independent validation study as concrete future work with a specific protocol.

---

## P3 — Advisory (1–2 reviewers, strengthens but does not block)

**Player study future work section.**
Bernstein and Murray both asked for it. Add a concrete future-work section describing what a human player study would look like: how many players, what materials (session transcripts or play sessions), what measures (recall protocols, affect scales), and what the study would add to the current findings.

---

## Convergent Strengths (Do Not Revise Away)

- 40+ arc-completion instances with 0 DM scripting: all five reviewers cited this as the paper's headline result. Protect it in the abstract and introduction.
- The three-part design template: Morningstar (strong accept), Murray, and Riedl all endorsed the template as a practical contribution. Do not compress the template specification.
- Cross-campaign archetype validation: the claim that the template works across grief-themed, compact-wardens, and the-witnesses parties is important and should be in the abstract.

---

## Divergent Notes

- Morningstar is the only strong accept (4). His practitioner enthusiasm is genuine but his review does not provide academic cover for the theoretical gaps Bernstein identifies.
- Bernstein's weak accept is conditional on the "memorable payoff" revision — this is more tractable than his A1 demand for inter-rater reliability. Path B (revision without new study) is sufficient.
- The paper is at CHI's acceptance threshold. A clean revision addressing P1 and P2 should bring all five reviewers to accept.
