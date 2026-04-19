---
name: playtest-innovation
description: Scout a session log and panel reviews for surprises the rubric did not anticipate. Logs entries to personas/playtest-innovations.md. Runs threshold checks — 2+ in a dimension → propose rubric amendment; 3+ clustered by theme across ≥ 2 sessions → propose new player-style entry. The pipeline's learning loop.
---

# playtest-innovation

The skill that makes the playtest system **learn from itself.** Without this stage, playtests are just session recordings.

## Pipeline position

Stage 6 of 7. Input: `sessions/S{N}-log.md` (especially `<!-- SURPRISE -->` tags and "Questions Raised About the Module"), `sessions/S{N}-gate.md` (innovation flags), `sessions/S{N}-panel/SUMMARY.md` (convergent suggestions). Output: appends to `personas/playtest-innovations.md` + optional amendment/style proposals.

## Preconditions

- Session log finalized.
- Gate scorecard written.
- Panel SUMMARY written.
- `personas/playtest-innovations.md` exists.
- `personas/playtest-rubric.md` exists.

## What Counts as an Innovation

A technique, pattern, or surprise that:
1. Cannot be captured by simply scoring higher on an existing rubric dimension.
2. Represents a new way of producing a good session.
3. Originates from play, not from design preference.

**Innovations are NOT:**
- High scores on existing dimensions (that's just good play).
- Personal aesthetic preferences.
- Things the rubric already anticipates.

## Procedure

### Step 1 — Harvest surprises

Read the session log. Extract every `<!-- SURPRISE -->` tag with its surrounding context. Also:
- Read the gate scorecard's "Innovation Flags" section.
- Read the panel SUMMARY's "Questions Raised About the Module or the System."

Consolidate into a candidate list of innovations for this session.

### Step 2 — Name each innovation

For each candidate, distill to:
- **What happened** — the specific technique or moment.
- **Which dimension it touches** — one of the 8, or "cross-dimensional."
- **Why the rubric did not anticipate it** — specific.
- **Scope** — party-specific / adventure-specific / universal.

### Step 3 — Append to the log

Append each innovation to `personas/playtest-innovations.md`:

```markdown
### [Date] — S{N} — <party-slug> — <adventure-slug>

**Technique:** [Short title]
**Dimension:** [Engagement / Mechanical fairness / Pacing / Character agency / Module fidelity / Atmospheric landing / Surprise / Table readiness / cross-dimensional]
**What happened:** [Quote from session log with scene reference]
**Why the rubric did not anticipate it:** [Specific]
**Scope:** [Party-specific / Adventure-specific / Universal]
**Status:** logged
```

### Step 4 — Threshold checks (TWO pathways, run BOTH)

#### Pathway A — Dimension trigger (rubric amendment)

Scan `playtest-innovations.md` for any **dimension** with ≥ 2 entries at status `logged`. If found, draft an amendment proposal:

```
AMENDMENT PROPOSAL — v<current>.X → v<next>
Dimension: <dimension>
Constituent innovations:
  - [entry ID 1]
  - [entry ID 2]
  - ...
Proposed change: [specific rubric text to add, revise, or anchor-update]
Impact: [how this changes future scoring]
```

Prompt the user: *"N innovations cluster in <dimension>. Proposed amendment: <summary>. Adopt to v<next>?"* On approval: update `personas/playtest-rubric.md`, mark constituents `adopted (v<next>)`, log in Amendment History.

#### Pathway B — Cluster trigger (player-style emergence)

Scan ALL `logged` innovations (regardless of dimension) for thematic clusters: ≥ 3 entries sharing a principle or pattern across ≥ 2 sessions.

Cluster by **theme**, not by dimension. Example: "PC pre-adventure hook reframes session center-of-gravity" can span Engagement + Character agency + Surprise entries simultaneously.

When a cluster holds across genuinely different sessions (different party or different adventure or both), draft a player-style proposal:

```
PLAYER-STYLE PROPOSAL — <proposed-slug>
Constituent innovations:
  - [entry ID 1 from S{X}]
  - [entry ID 2 from S{Y}]
  - [entry ID 3 from S{Z}]
Definition: [what this style IS]
Triggers: [what a session looks like when this style is active]
Cross-applicability: [which parties/adventures this style amplifies or undermines]
```

Prompt the user: *"Cluster <theme> forms across S{X}, S{Y}, S{Z}. Propose player-style entry?"* On approval: create `personas/player-styles/<slug>.md`, mark constituents `promoted-to-style (<slug>)`.

### Step 5 — Report

Summarize to the user:
- **Innovations logged this session:** count + list.
- **Amendment proposals:** count.
- **Player-style proposals:** count.
- **Suggested next step:** `session-handoff`.

## When the Rubric Must Be Synced

After a rubric amendment, `session-runner`'s next PREP stage reads the new version. The PREP file records the version the session is played under; the gate scorecard applies that version.

**Forward-only.** A v1.1 rubric does not re-score S01 (scored under v1.0). It applies to S02+.

## Discipline

- **Do not invent innovations.** Every entry must cite a specific session passage.
- **Threshold is threshold.** 1 innovation in a dimension is not a 2+ trigger. Don't round up.
- **Clusters are theme-based.** A cluster of 3 "Engagement" innovations is a dimension trigger, not a cluster trigger. A cluster of 1 Engagement + 1 Agency + 1 Surprise sharing a theme is a cluster trigger.
- **The user approves amendments.** The skill proposes; the user ratifies. Do not auto-adopt.

## Output to user

- Innovations logged (count + one-line each).
- Proposals drafted (amendments + styles).
- Any proposals auto-dismissed (reason).
- Suggested next step: `session-handoff`.

## Anti-patterns

- Logging innovations that are actually just "things that went well."
- Triggering amendments on 2 innovations that happen to land in the same dimension but share no theme.
- Promoting a player-style from 3 innovations all in the same session (the cluster requires ≥ 2 sessions; otherwise it's party-specific noise).
- Auto-adopting amendments without user approval.
- Skipping the threshold check.
