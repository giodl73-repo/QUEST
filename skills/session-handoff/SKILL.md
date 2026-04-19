---
name: session-handoff
description: End-of-session ritual. Writes the canonical HANDOFF-S{N}.md artifact, updates root TRACKER.md with metrics, re-runs innovation threshold checks, and commits. No session ends without a handoff. Pipeline stage 7 of 7.
---

# session-handoff

The pipeline's end-of-session discipline. **No session ends without a handoff.** The handoff is what lets the next session begin cold without re-deriving state.

## Pipeline position

Stage 7 of 7 — terminal. Input: everything produced by the prior stages. Output: `sessions/HANDOFF-S{N}.md`, updated `TRACKER.md`, committed state.

## Preconditions

- `sessions/S{N}-log.md` finalized.
- `sessions/S{N}-gate.md` written.
- `sessions/S{N}-panel/` directory with 5 reviews + SUMMARY.
- `playtest-innovation` has appended to `playtest-innovations.md`.
- `TRACKER.md` exists at repo root (create on first run).

## Procedure

### Step 1 — Gather state

Read:
- `TRACKER.md` — current counts.
- `sessions/S{N}-log.md` — canonical session artifact.
- `sessions/S{N}-gate.md` — score.
- `sessions/S{N}-panel/SUMMARY.md` — panel verdict.
- `personas/playtest-innovations.md` — innovations logged this session.
- `personas/playtest-rubric.md` — version, amendments history.
- `personas/parties/<slug>/shared-log.md` — party continuity.

### Step 2 — Write the handoff file

Create `adventures/<slug>/sessions/HANDOFF-S{N}.md`:

```markdown
---
session: S{N}
adventure: <slug>
party: <party-slug>
date: <today>
next-session: S{N+1}
author: session-handoff
---

# HANDOFF — S{N} → S{N+1}

## Fast-Start (read these first next session)

1. This handoff file.
2. `sessions/S{N}-log.md` — what happened.
3. `personas/parties/<slug>/shared-log.md` — party continuity.
4. `personas/playtest-rubric.md` — current rubric version.
5. `adventures/<slug>/module.md` (or next adventure's module).

## What was delivered this session

- Session **S{N}** completed — outcome: <one-line from log>.
- Gate verdict: <PASS/FAIL/ADVISORY> at <N>/80.
- Panel mean (weighted): <N>/80.
- Innovations logged: <count> (see `personas/playtest-innovations.md`).
- Any rubric amendments adopted: <list>.
- Any player-style proposals drafted / promoted: <list>.

## Party state (carried forward)

Table: PC, HP, slot reserves, exhaustion (if persistent), attunements, notable inventory, open character threads.

## Open threads (for next session's DM)

(From the session log's "Open threads" + panel's "Questions Raised" + any pending innovation proposals.)

## Priorities for S{N+1}

### Tier 1 (blocking / must-resolve)
- ...

### Tier 2 (do-if-time)
- ...

### Tier 3 (strategic / future)
- ...

## Current Metrics (from TRACKER.md after update)

| Metric | Value |
|---|---|
| Sessions played | <N> |
| Adventures with sessions | <N> |
| Unique parties | <N> |
| Rubric version | v<X.Y> |
| Innovations logged (total) | <N> |
| Innovations adopted (total) | <N> |
| Player-styles promoted | <N> |
| Mean session score (weighted, last 3) | <N>/80 |

## Open Questions

Anything unresolved that the next session needs to address.

## Innovation Threshold Re-check

Re-run `playtest-innovation`'s thresholds at handoff time (belt-and-suspenders — a cluster may have formed across the full session log only visible in summary form).

- Dimension trigger: <any 2+ in a dimension now at `logged`?>
- Cluster trigger: <any 3+ thematic cluster across ≥ 2 sessions?>

## Commit

```
git add adventures/ personas/ sessions/ TRACKER.md
git commit -m "Session S{N} handoff — <one-line>"
```

(Only run the commit if repo is git-initialized AND user has not explicitly declined commits.)
```

### Step 3 — Update TRACKER.md

Maintain `TRACKER.md` at repo root. Sections:

```markdown
# Marathon Tracker

Last updated: <today> by session-handoff (S{N})

## Sessions

| S# | Adventure | Party | Date | Gate /80 | Panel weighted /80 | Verdict |
|---|---|---|---|---:|---:|---|
| S01 | ... | ... | ... | ... | ... | ... |

## Adventures

| Slug | Status | Sessions | Revision | Notes |
|---|---|---|---|---|
| 0001-tomb-of-the-silver-rose | rev 2, played | S01 | 2 | ... |

## Parties

| Slug | Members | Status | Sessions played |
|---|---|---|---|
| varduin-muster | Aelric / Thera / Kessa / Grom | active | 1 |

## Rubric

- Current version: v<X.Y>
- Amendments history: see `personas/playtest-rubric.md`

## Innovations Catalog

| Status | Count |
|---|---:|
| Logged | N |
| Proposed | N |
| Adopted | N |
| Reviewed — not adopted | N |
| Promoted to style | N |

## Player Styles

| Slug | Promoted on | Source sessions | Status |
|---|---|---|---|
| ... | ... | ... | ... |

## Recent activity

Short log of last 3-5 handoffs (latest first).
```

### Step 4 — Append to party's shared-log (if not already updated in LOG stage)

Ensure `personas/parties/<slug>/shared-log.md` has a paragraph for this session. (If `session-runner` already appended, skip.)

### Step 4a — Update seed-tracker *(new, per campaign-planner adoption)*

If a campaign spine exists (`docs/campaign/<slug>.md`):

1. Invoke `seed-tracker` with seeds retrieved during this session (parse from the session log's "Seeds retrieved" section if present; else DM-identified).
2. Invoke `seed-tracker` with seeds planted this session.
3. Update any hint statuses: `caught` if the party engaged with a hint; `missed` if the hint was available but unnoticed; `re-available` if a recovery path is active.
4. Note any orphan-alerts flagged by the tracker in this handoff file's "Priorities for next session" section.

### Step 5 — Commit (optional, user-gated)

Run the git commit only if:
- The repo is initialized (has `.git/`).
- The user has not explicitly asked to skip commits.
- The commit does not include files that look like secrets.

If not committing, report unstaged files and let the user decide.

## Discipline

- **Every session handoff.** No skipping, no combining with the next session's PREP.
- **Forward-only dates.** Never back-date a handoff.
- **TRACKER is canonical.** If TRACKER and other files disagree, TRACKER is authoritative for counts; the other files are authoritative for content.
- **The handoff is for future-Claude.** Write it so a fresh session could pick up cold.

## Output to user

- Handoff file path.
- Current metrics (session count, rubric version, innovations totals).
- Any amendment proposals or player-style proposals pending approval.
- Whether commit was run (and commit hash) or skipped.
- **"Ready for S{N+1}."**

## Anti-patterns

- Handoffs without metrics.
- Handoffs that duplicate the session log's summary without adding forward-looking state.
- Skipping TRACKER.md updates.
- Committing without reviewing staged files for secrets.
- Running handoff before gate, panel, or innovation stages completed.
