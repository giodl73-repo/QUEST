---
name: arc-audit
description: Audit a campaign's state against its spine. Checks for orphan seeds, missing foreshadowing, hint-drift, campaign-continuity violations, PC-spotlight balance. Runs pre-every-adventure-design and pre-finale. Writes a report; does not modify files unless explicitly asked.
---

# arc-audit

Check the campaign's current state against its spine. Surface drift before it compounds.

## Preconditions

- Campaign spine exists (`docs/campaign/<slug>.md`).
- Seed-tracker exists (`campaign/seed-tracker.md`).
- At least one adventure has been designed or played.

## What arc-audit checks

### 1. Orphan seeds

A seed is an orphan if:
- Planted, target adventure scheduled, target adventure **has played**, seed status still `active`.
- Planted, status `active`, target adventure `TBD`, and N adventures have played since (N threshold configurable; default 2).

### 2. Missing foreshadowing

A retrieval is missing-foreshadowing if:
- An adventure retrieves a seed, but no planting entry exists in seed-tracker.
- An adventure's premise.md references a seed-like entity that has no tracker entry.

### 3. Hint drift

For campaigns with hint-gated endings:
- A hint planted in an adventure that should-have-been-caught per session log but tracker says `missed` — DM oversight.
- A hint whose recovery path is due to activate but hasn't — DM should schedule the recovery.

### 4. Campaign-continuity violations

Checks played session logs + CLAUDE.md#campaign-continuity for:
- Facts established as campaign-permanent that were contradicted in a later session (e.g., a DM re-narrated a memory Aelric had permanently lost — violation).
- Workshop-canon entities whose state in a session log disagrees with the canon file.

### 5. PC-spotlight balance

Counts spotlights across played + scheduled adventures:
- Is any PC spotlit twice before all PCs have been spotlit once?
- Is any PC never scheduled for a spotlight in the remaining adventures?

### 6. Artifact-slot coverage

For campaigns with an artifact-per-adventure structure:
- Is every artifact assigned to an adventure?
- Is any adventure missing its assigned artifact?

## Procedure

### 1. Read all context
- Campaign spine.
- Seed-tracker.
- All played session logs + handoffs.
- `reference/dragonlance/workshop-canon.md`.
- `CLAUDE.md#campaign-continuity`.
- `TRACKER.md`.

### 2. Run the six checks above

Each check produces: PASS, WARNING, or VIOLATION.

- PASS = no drift.
- WARNING = drift forming; DM should notice.
- VIOLATION = drift concrete; requires action.

### 3. Write the report

Output to `campaign/audits/arc-audit-YYYY-MM-DD.md`:

```markdown
---
campaign: <slug>
date: <today>
author: arc-audit
---

# Arc Audit — <Campaign Name> — <Date>

## Summary
- ✗ N violations
- ⚠ N warnings
- ✓ N passes

## Check 1 — Orphan seeds
<results>

## Check 2 — Missing foreshadowing
<results>

## Check 3 — Hint drift
<results>

## Check 4 — Campaign-continuity violations
<results>

## Check 5 — PC-spotlight balance
<results>

## Check 6 — Artifact-slot coverage
<results>

## Recommended actions
<prioritized list>
```

### 4. Update seed-tracker's orphan-alerts section

If Check 1 produced orphans, write them to the seed-tracker's "Orphan alerts" section with timestamp.

## When to run

- **Pre-every-adventure-design:** confirm the adventure's planned seed-retrievals are legal (the seeds exist + are active).
- **Post-every-session-handoff:** confirm no campaign-continuity violations from the played session.
- **Pre-finale:** full check across all played + scheduled adventures.
- **On-demand:** any time the DM suspects drift.

## Output to user

- One-line summary (violations / warnings / passes).
- Report file path.
- Strongest recommended action (the one fix that resolves the most issues).

## Quality gates

- [ ] All six checks run.
- [ ] Report file written with timestamp.
- [ ] Seed-tracker's orphan-alerts updated if orphans exist.
- [ ] Recommended actions prioritized (not just listed).

## Anti-patterns

- Auto-modifying the spine or seed-tracker to "fix" violations (the DM decides).
- Flagging every seed as a potential orphan (apply threshold correctly).
- Missing to check session logs (they're authoritative for what actually happened).
- Conflating warnings with violations (warnings are drift-forming; violations are drift-concrete).
