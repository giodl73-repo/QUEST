---
name: session-gate
description: Score a finalized session log against the playtest rubric. Produces a scorecard with dimension-by-dimension evidence and a pass/fail verdict. Reads personas/playtest-rubric.md for the locked version referenced in the session's PREP; applies that version's anchors. Advisory-only for sessions before the rubric is calibrated (first 3 sessions). Use after session-runner's LOG stage and before playtest-panel.
---

# session-gate

Score a session log. Produce the scorecard the rest of the pipeline consumes.

## Pipeline position

Stage 4 of 7. Input: `sessions/S{N}-log.md`. Output: `sessions/S{N}-gate.md`. Subsequent stages (`playtest-panel`, `playtest-innovation`) read both.

## Preconditions

- `sessions/S{N}-log.md` is finalized (not `status: running`).
- `personas/playtest-rubric.md` exists; its version is recorded in the session's PREP file (`rubric-version-locked`).
- The session log's frontmatter has `dice-seed`, `party`, `adventure`, `duration`, `outcome`.

## Scoring Protocol

For **each of the 8 dimensions** in the rubric version locked by PREP:

1. **Read the log** with this dimension in mind. Pass once for the whole log, not dimension-by-dimension.
2. **Find evidence** — specific scene/passage citations that support a high or low score. Quote ≥ 1 line.
3. **Find counter-evidence** — what lowered your score.
4. **Assign score** using the rubric's 0-10 bands.
5. **Write the evidence cell** — not generic, specific with file:scene references.

Do not score generously out of sympathy. Do not score harshly to seem rigorous. Score what the log says.

## Output

Write to `sessions/S{N}-gate.md`:

```markdown
---
session: S{N}
adventure: <slug>
party: <party-slug>
rubric-version-applied: v<X.Y>
date: <today>
author: session-gate
verdict: [PASS / FAIL / ADVISORY]
total: <N>/80
route: [A|C|D]
---

# S{N} GATE — <Adventure Title>

## Scorecard

| Dimension | Score | Evidence | Counter-evidence |
|---|---:|---|---|
| Engagement | N/10 | Scene X — <quote or summary> | Scene Y — <what lowered> |
| Mechanical fairness | N/10 | ... | ... |
| Pacing | N/10 | ... | ... |
| Character agency | N/10 | ... | ... |
| Module fidelity | N/10 | ... | ... |
| Atmospheric landing | N/10 | ... | ... |
| Surprise | N/10 | ... | ... |
| Table readiness | N/10 | ... | ... |
| **TOTAL** | **N/80** | | |

## Verdict

**[PASS / FAIL / ADVISORY]** at threshold [current rubric threshold, e.g., 56/80].

For advisory-only sessions (first 3, or explicit `advisory: true` in PREP), no pass/fail — the score is recorded for trend analysis.

## Dimensions Below Threshold

List any dimension that scored below 7/10. Describe what would raise it.

## Player-Style Instances

Track ratified player-style firings this session. These feed directly into `playtest-innovation`'s cluster checks.

| Style | Instances | Scene references |
|---|---|---|
| sheet-deep-reader | N | Scene X, Scene Y |
| craft-witness | N | Scene X |
| <any other ratified style> | N | ... |

Also flag any NPC-arc-completion instances: NPCs who delivered their arc-completion moment by character logic this session (not DM scripting). Running campaign total toward the 3-instance cluster threshold.

## Innovation Flags

If you notice something exceptional the rubric did not anticipate — a technique or moment that cannot be captured by scoring higher on an existing dimension — flag it here. These flags become input to `playtest-innovation`.

```
INNOVATION FLAG: <short title>
Dimension affected: <one or more>
What happened: <quote from log with scene reference>
Why the rubric missed it: <specific>
```

## Next Stage

Pipeline proceeds to `playtest-panel`.
```

## Scoring Discipline

- **Scorer is a separate role from DM.** Score what the log says, not what the DM intended.
- **Evidence must be specific.** "Good pacing" is not evidence. "Scene 7 resolved in 2 rounds, a tight fight after two long exploration scenes" is evidence.
- **Counter-evidence matters.** A 9 with no counter-evidence is an 8 that wasn't honest.
- **Innovation flags are separate from scores.** An innovation does not *raise* a dimension's score; it signals the rubric may need an amendment.

## Verdict Logic

- **PASS:** total ≥ threshold AND no dimension below 3/10.
- **FAIL:** total < threshold OR any dimension below 3/10.
- **ADVISORY:** first 3 sessions, or PREP has `advisory: true`. No pass/fail; score recorded.

For the first 3 sessions the threshold is not binding — we're calibrating. After session 3, `session-handoff` prompts the user to ratify the threshold.

## Never overwrite silently

If `sessions/S{N}-gate.md` exists, write `S{N}-gate.v2.md` and report.

## Output to user

- Verdict (PASS/FAIL/ADVISORY).
- Total score with dimension breakdown.
- Any dimensions below 7/10.
- Innovation flags count.
- Suggested next step: `playtest-panel`.

## Anti-patterns

- Generic scores with no evidence.
- Evidence that is a paraphrase rather than a quote.
- Pass/fail applied to an advisory session.
- Innovation flags that are actually just a "do better next time" note.
- Scoring the PCs rather than the session.
