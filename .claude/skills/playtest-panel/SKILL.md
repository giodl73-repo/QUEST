---
name: playtest-panel
description: Run the 5 player-experience lens reviews against a session log. Each lens (Tactician, Roleplayer, Lorekeeper, Improviser, Fresh Face) reviews from its distinct perspective, producing structured friction. Writes one review per lens plus a SUMMARY with weighted aggregate. One round only — sessions do not get revised.
---

# playtest-panel

Run the 5-lens review against a session log. The lenses disagree by design; their tension surfaces what a single reviewer would miss.

## Pipeline position

Stage 5 of 7. Input: `sessions/S{N}-log.md` and `sessions/S{N}-gate.md`. Output: `sessions/S{N}-panel/` directory with 5 reviews + `SUMMARY.md`.

## Preconditions

- `sessions/S{N}-log.md` finalized.
- `sessions/S{N}-gate.md` written.
- All 5 lens files exist at `personas/player-lenses/<slug>.md`.

## The Five Lenses

| Lens | File | Core question |
|---|---|---|
| **The Tactician** | `personas/player-lenses/tactician.md` | Were encounters fair, was positioning tactical, did mechanics matter? |
| **The Roleplayer** | `personas/player-lenses/roleplayer.md` | Did my PC get to be someone specific? |
| **The Lorekeeper** | `personas/player-lenses/lorekeeper.md` | Did the setting feel lived in? |
| **The Improviser** | `personas/player-lenses/improviser.md` | When I went off-book, did the DM say yes? |
| **The Fresh Face** | `personas/player-lenses/fresh-face.md` | Could a new player have followed this? |

Read each lens file before writing its review.

## Review Protocol

For each of the 5 lenses, write a review to `sessions/S{N}-panel/<lens-slug>.md`:

```markdown
---
session: S{N}
lens: <lens-slug>
adventure: <adventure-slug>
author: playtest-panel
created: <today>
---

# Review — <Lens Name> on S{N} — <Adventure Title>

## Scorecard (lens-weighted)

| Dimension | Raw (from gate) | Lens weight | Weighted |
|---|---:|---:|---:|
| Engagement | N/10 | W | N×W |
| Mechanical fairness | N/10 | W | N×W |
| Pacing | N/10 | W | N×W |
| Character agency | N/10 | W | N×W |
| Module fidelity | N/10 | W | N×W |
| Atmospheric landing | N/10 | W | N×W |
| Surprise | N/10 | W | N×W |
| Table readiness | N/10 | W | N×W |
| **Weighted total** | | | **N/80** |

## Critique

### Overall assessment (2-3 sentences in the lens's voice)

### What worked (≥ 2 specific citations)
- **Scene X:** <specific passage cited, with scene reference, in lens voice>.

### What needs work (≥ 2 specific citations)
- **Scene X:** <passage + what's wrong + why, in lens voice>.

### The question I'd push on
The single most important unresolved issue, in the lens's voice.
```

## SUMMARY Protocol

After all 5 reviews are written, write `sessions/S{N}-panel/SUMMARY.md`:

```markdown
---
session: S{N}
adventure: <slug>
author: playtest-panel
created: <today>
---

# Panel Summary — S{N}

## Weighted Scores by Lens

| Lens | Unweighted /80 (from gate) | Weighted /80 | Relative |
|---|---:|---:|---:|
| Tactician | <from gate> | <computed> | +/- mean |
| Roleplayer | ... | ... | ... |
| Lorekeeper | ... | ... | ... |
| Improviser | ... | ... | ... |
| Fresh Face | ... | ... | ... |
| **Panel mean** | ... | ... | |

## Strongest Consensus

Which dimension got uniformly high marks across lenses? Cite.

## Most Dissent

Which dimension produced the widest spread? What's the philosophical disagreement?

## Convergent Suggestions (multiple lenses agree)

List suggestions that 2+ lenses made (even in different wording). These are the highest-leverage next-session changes.

## Divergent Suggestions (single-lens; keep or ignore)

Specific suggestions from a single lens. Each tagged with lens-of-origin.

## Questions Raised About the Module or the System

Meta-level notes: where the playtest pipeline itself needs work; where the module should be revised; where the rubric may need amendment (feed into `playtest-innovation`).

## Ratified Player-Style Instances

| Style | Instances this session | Key scene references |
|---|---|---|
| sheet-deep-reader | N | ... |
| craft-witness | N | ... |

Cross-session running totals (for cluster / de-promotion tracking):
- sheet-deep-reader: N total across M sessions
- craft-witness: N total across M sessions

## NPC-Arc-Completion Instances

NPCs who delivered their arc-completion moment by character logic (not DM scripting) this session:

- None / <NPC name — scene ref — what they said or did>

Campaign running total: N instances across M sessions. Cluster promotion threshold: 3 instances across ≥ 2 sessions.
```

## Discipline

- **One round only.** Chronicle runs panels twice (opening, then production bible); playtest runs once. The session happened; it cannot be revised.
- **Lens voice discipline.** Each review must sound like the lens, not like a generic reviewer. Re-read the lens file before writing.
- **Productive tension is the goal.** If all 5 reviews agree on everything, you didn't read the log carefully enough. Real sessions produce disagreement.
- **Evidence cited.** Every "what worked" / "what needs work" line must cite a specific scene + quote or summary.

## Never overwrite silently

If the panel directory exists, write `S{N}-panel.v2/` and report.

## Output to user

- Panel mean score (weighted).
- Lens ranges (highest, lowest).
- Top 3 convergent suggestions.
- Suggested next step: `playtest-innovation`.

## Anti-patterns

- Reviews that sound identical (lens voice lost).
- Scorecard math errors (weights must sum to 8.0).
- Suggestions without session-log citations.
- "What worked" lines without specifics.
- Skipping the SUMMARY (each individual review is incomplete without the cross-lens synthesis).
