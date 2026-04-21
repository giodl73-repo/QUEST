---
name: campaign-planner
description: Produce a campaign spine — the living operational document that gives each adventure in a multi-adventure arc its direction + seed-placement guidance. Run once per campaign; revised sparingly when direction shifts. Output: docs/campaign/<slug>.md with adventure slots, PC spotlights, artifacts, seeds planted/retrieved, finale branches. Does not replace session emergence; lays a spine that emergence fleshes out.
---

# campaign-planner

Produce the spine doc for a multi-adventure campaign. Each adventure still runs through the normal pipeline (dungeon-smith → treasure-forger → module-binder → session-runner → gate → panel → innovation → handoff). The spine tells each adventure *what it owes backward* (seeds to retrieve) and *what it should set up forward* (seeds to plant).

## Preconditions

- A full design spec exists (typically at `docs/specs/YYYY-MM-DD-<slug>-design.md`) or is being written alongside.
- The campaign has: a party, a setting anchor, a central moral question, a target adventure count, and an identifying theme (e.g., "seven emotion-objects").
- Workshop-canon (`reference/dragonlance/workshop-canon.md`) exists.

## Inputs

Required:
- **Campaign slug** (kebab-case; e.g., `moon-silver-cycle`).
- **Party slug** (e.g., `varduin-muster`).
- **Adventure count** (e.g., 7).
- **Central moral question** (one sentence).
- **Theme** (e.g., "seven emotions transacted by moon-silver artifacts").
- **Adventure-to-theme mapping** (ordered list).

Optional:
- **PC spotlights** (which PC is centered in each adventure).
- **Finale branches** (if the campaign has explicit branching endings).
- **Hints** (if the campaign has gated endings that require hint-collection).

## Procedure

### 1. Read context
- The design spec (if any).
- Played adventures' premise.md files (seeds that already exist).
- Workshop-canon for existing named entities.

### 2. Write the spine doc

Output to `docs/campaign/<slug>.md`. Structure:

```markdown
---
campaign: <slug>
party: <party-slug>
status: active (or: draft / paused / concluded)
created: <today>
last-updated: <today>
design-spec: docs/specs/<spec-path>
---

# <Campaign Name>

## Central question
<One sentence.>

## Arc at a glance

| # | Adventure slug | Artifact | Theme | Spotlight | Status |
|---|---|---|---|---|---|
| 0001 | ... | ... | ... | ... | played / designed / pending |
| ...
| 000N | ... | ... | ... | ... | ... |

## Adventure briefs (one section each)

### #<N> — <Working Title>

**Setting:** <one line>
**Hook:** <one line>
**Artifact (emotion):** <name> — <brief mechanics hint>
**Spotlight:** <which PC>
**Seeds retrieved from earlier adventures:** (list)
**Seeds to plant for later adventures:** (list)
**Hints:** (list of D-hints or other campaign-level hints this adventure plants / unlocks / delivers)
**Open questions:** (anything to decide at brainstorm time)

## Finale branches
<If any — describe A/B/C/D etc.>

## Hint tracking
<List of D-hints with their target adventures.>

## Changelog
<Append-only log of edits to this file.>
```

### 3. Register with `seed-tracker`

Write the initial seeds-to-be-planted list to `campaign/seed-tracker.md`. See `seed-tracker` skill.

### 4. Register with workshop-canon

Any new named entities introduced by the spine (campaign-level NPCs, locations) get added to `reference/dragonlance/workshop-canon.md` as pending.

### 5. Declare living-doc protocol

Add to the spine doc:

> This spine is living. Session-learnings may change which seed activates which adventure, which PC spotlights which, or even the adventure count. Re-edit this file; note every edit in the changelog. The spec (`docs/specs/...`) is the *rationale*; this spine is the *operational plan*.

## Never overwrite silently

If `docs/campaign/<slug>.md` exists, write `<slug>.v2.md` and prompt the user — the new spine should inherit from (or explicitly supersede) the old.

## Output to user

- Campaign slug + adventure count + theme summary.
- Spine file path.
- Initial seed list count.
- Suggested next step: run `seed-tracker` to populate pre-existing seeds from played adventures; run `arc-audit` to confirm internal consistency.

## Quality gates

- [ ] Spine doc covers ALL adventures in the count (no missing slots).
- [ ] Each adventure brief has a spotlight, artifact, seeds-retrieved list, seeds-planted list.
- [ ] Finale branches have documented conditions.
- [ ] Hints have documented target adventures.
- [ ] Changelog started.
- [ ] Workshop-canon registered pending entities.
- [ ] **PC-authored finale deliverable identified** (see below).

## PC-authored finale deliverable (Campaign 2 addition)

Campaign 2 produced the most effective finale element organically: Thessaly composed the opening sentence of the new compact across four sessions (mental design S04 → not writing S05 → written silently S06 → spoken S07). The compact's opening words were designed by the PC, not the module.

When writing the spine, **identify one PC-authored deliverable for the finale** — a speech, a document, a sentence, a name — that the PC will compose or build toward across the campaign, not in a single session. This should be:
- Connected to the PC's primary grief or decision-order
- Not something the module pre-writes (the PC authors it)
- Something that can be tracked across sessions in the handoff ("Thessaly is still composing the opening sentence")
- Something that the session-runner notes when it is spoken/written/completed for the first time

**How to set it up:** In the adventure brief for the penultimate adventure (or earlier), note: *"This session should give [PC] the vocabulary/conditions to author [the deliverable]."* Do not script the deliverable. Provide the structural invitation.

## Anti-patterns

- Spine doc so detailed it becomes a railroad (adventure briefs should be *sketches*, not scripts).
- Spine doc that doesn't align with the played adventures' content.
- Seeds listed without target-adventures (orphan seeds).
- Hints without recovery paths (rubric v1.2 requires them).
- Spine that forgets which PCs have been spotlighted (uneven distribution).
- Finale designed entirely by the module (no PC-authored element).
