> **Note:** This is an AI-generated simulated review, written by Claude in the voice of a named-expert persona. It is not an actual review by the named person and does not reflect their views or endorsement.

# Review: Designing NPC Arc-Completion Conditions for Session-Invariant Emotional Payoffs in AI-Simulated TRPG
**Reviewer:** Mark Riedl, Georgia Tech Entertainment Intelligence Lab
**Score:** 3 — accept
**Expertise:** AI narrative generation, procedural content generation, game AI

## Summary
This paper tackles a genuine problem in AI narrative design: how do you build NPCs that have emotionally complete arcs without scripting the resolution? The design template — specifying emotional position, completion condition, and triggering context — is a principled answer, and the 40+ instance corpus provides substantial empirical backing. The paper's distinction between character-logic-driven and DM-scripted arc-completions is the right theoretical framing and connects meaningfully to prior work on drama management and character-based narrative planning.

## Major Issues (P1 if 3+ reviewers or blocking)
- **Drama management comparison is insufficient**: The paper cites Riedl & Young and Louchart & Aylett but does not compare the arc-completion design template against drama management approaches. The paper's claim — that character-logic is a better trigger than DM scripting — is a strong claim that requires a stronger defense. At minimum, the paper should characterize drama management's approach to NPC arc resolution and explain why the character-logic approach is different in kind, not just in implementation.

## Minor Issues
- **Correlation vs. causation in "memorable" claim**: The paper claims NPC arc-completions produce "memorable payoffs" and backs this with rubric scores. But the rubric was partly designed around these sessions — there is a circularity risk. An independent operationalization of "memorable payoff" (even a post-session AI-simulated player recall task) would strengthen the causal claim.
- **Morally grey validation**: The claim that the template handles morally grey NPCs is supported by a few instances. A more systematic breakdown of NPC moral valence across the 40+ corpus would make this claim empirically solid.

## Detailed Comments
### Introduction
The introduction is clear and well-motivated. The practitioner framing ("what a game designer actually needs to write") is appropriate for a CHI audience. The theoretical framing (character logic vs. DM scripting) is the paper's most important conceptual move and deserves more prominence in the abstract.

### Methodology
The design template is the paper's primary contribution. The paper would benefit from a figure showing the template structure — the three-part arc specification (emotional position, completion condition, triggering context) — as a formal diagram alongside the prose description. This would make the template citable and adoptable.

### Evaluation
The 88% session coverage figure is strong. The paper should report it with confidence intervals and should break down coverage by session position (early, mid, late campaign) — is arc-completion more reliable when the NPC has had more scenes?

## Recommendation
Accept with revisions. The drama management comparison is the critical revision. The paper is a solid CHI contribution; the template is clear, the corpus is substantial, and the character-logic framing is important. Revision is manageable within a standard revision cycle.
