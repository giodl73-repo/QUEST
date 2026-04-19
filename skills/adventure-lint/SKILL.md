---
name: adventure-lint
description: Scan an adventure directory against all quality gates before module-binder runs. Reports violations per persona lens (Jaquays, Stuart, Schick, Moldvay, Gygax) with file:line references. Use between dungeon-smith/treasure-forger completion and module-binder. Catches problems the persona panel would flag, before the panel is run.
---

# adventure-lint

One-pass validator that runs all quality gates declared by `dungeon-smith`, `treasure-forger`, and `module-binder` against an adventure directory. Produces a violation report organized by persona lens.

## Preconditions

- `adventures/<slug>/` exists.
- `premise.md` exists at minimum.
- Any of: `rooms/`, `treasures/`, `encounters/`, `npcs/` may be partially populated.
- Quality gates in the 3 producer skills are the source of truth. This skill does not invent new gates; it enforces the existing ones.

## Output

A report file at `adventures/<slug>/lint-report-YYYY-MM-DD.md` with:
1. Summary counts: ✗ violations, ⚠ warnings, ✓ passed.
2. Per-lens scorecard (Jaquays / Stuart / Schick / Moldvay / Gygax).
3. Per-file violation list with exact file:section references.
4. Suggested fixes (imperative, actionable).

## Procedure

### 1. Load all adventure files
- `premise.md`, all `rooms/*.md`, all `treasures/*.md` (including manifests), all `encounters/*.md`, all `npcs/*.md`, `module.md` if it exists.
- Parse frontmatter from each; note any with missing required fields.

### 2. Run the gate suite

#### Topology gates (Jaquays)
- Map file exists at `rooms/map.md`?
- Map has ≥ 1 loop? (Parse Connections table; verify a cycle exists.)
- Map has ≥ 1 vertical connection? (Look for "stair", "shaft", "climb", "ledge" in connection types.)
- ≥ 2 paths to the artifact-holding room? (Graph-analyze connections.)
- ≥ 1 shortcut (a connection described as conditional/sealed/unlocking)?
- Each branch from a junction has a distinguishing cue? (For each room with ≥ 2 exits, check sibling-exit descriptions for distinct sensory details.)
- At least one inhabitant has dynamic behavior? (Search encounter files for "patrol", "move between", "react to noise".)

#### Temporal-pressure gates (Gygax + Stuart)
- `encounters/wandering-pressure.md` exists OR `premise.md` or a GM-notes section justifies its absence explicitly?
- Proper-encounter count ≥ ⌈room_count / 2⌉? (Count encounter files plus inline-encounter rooms; conditional encounters count 0.5.)

#### Atmosphere gates (Stuart)
- Every `rooms/NN-*.md` GM Notes section has an optional Memory Fragment beat?
- If a cursed artifact exists: `treasures/<name>-manifest.md` exists?
- If a manifest exists: ≥ 3 of its listed symptoms appear in the dungeon rooms? (String-match the symptom descriptions against room bodies.)
- If the artifact has a Presence / Desire section: ≥ 1 room expresses it in prose?

#### Signature-treasure gates (Schick)
- Every treasure file has a room that cites it in its Treasure section? (Check cross-references in both directions.)
- The artifact-holding room has a reaction moment on artifact removal? (Search room body for post-removal language: "heals", "shifts", "weeps", "fades", "chimes".)
- Every incidental item has a purpose tag (evidence, key, clue, roleplay trigger)? This is a soft warning, not a hard fail.

#### Table-readiness gates (Moldvay)
- Every read-aloud block ≤ 60 words? (Word-count the blockquote content.)
- Every DC referenced in rooms appears in the cheatsheet (if `module.md` exists)?
- Every NPC named in `premise.md` has `npcs/<slug>.md`?
- Every non-statted entity mentioned in rooms (echo, ghost, voice, presence) has an interaction rule in its GM Notes?
- No retrieval options differ only in noise level? (Parse Options A/B/C/D in artifact-retrieval rooms; flag pairs that share mechanics but differ only in a noise/silence flag.)
- `premise.md` ≤ single-page equivalent (target: ≤ 80 lines)?

#### Player-agency gates (Gygax)
- Central artifact has ≥ 2 meaningfully-different retrieval paths?
- Post-recovery real-decision has ≥ 3 valid outcomes? (Search premise + module for "return / keep / destroy / sell" or equivalent.)

#### Campaign-awareness gates *(new — if a campaign spine exists)*

- Does `premise.md` reference the campaign spine (`docs/campaign/<slug>.md`)?
- Does the adventure retrieve the seeds the spine scheduled for this slot? For each scheduled seed: is its retrieval scene identified in a room file or NPC file?
- Does the adventure plant the seeds the spine scheduled for this slot? For each: is its planting scene identified?
- If the spine schedules a hint-unlock here, is the unlocking scene present in the module?
- If the spine schedules a PC spotlight, does the spotlight-PC have at least one moment (scene-driving action, recognition beat, or decision scene) in the keyed rooms?
- Does the manifest (if cursed artifact) respect rubric v1.2 — anchor-level symptoms with passive-Perception fallbacks at DC = active + 2?
- Does the per-PC reception table use finder-vs-receiver two-column tracking (rubric v1.2)?

#### File hygiene
- Every generated file has frontmatter with required fields (adventure, author, created)?
- No orphan files (referenced but missing)?
- No unreferenced files (present but cross-ref'd from nowhere — soft warning)?
- Filename conventions (NNNN- adventure slug, NN- room slug, kebab-case)?

### 3. Score per lens

Each gate contributes to a lens score. A failing gate is a -N penalty per lens (configurable). Report the aggregate per-lens score so the human can see which persona would be unhappiest at table.

Default weights:
- Jaquays: topology gates
- Gygax: temporal pressure + player agency
- Stuart: atmosphere + curse symptoms + presence
- Schick: signature treasure + reaction moment
- Moldvay: table-readiness

Example report snippet:
```
Jaquays    [ 4/5 ✓ ]  ← fails: Room 2 branches not distinguished
Gygax      [ 2/3 ✓ ]  ← fails: encounter count below threshold
Stuart     [ 4/6 ✓ ]  ← fails: manifest exists but only 2/3 symptoms expressed; 1 room missing Memory Fragment
Schick     [ 3/3 ✓ ]
Moldvay    [ 5/6 ✓ ]  ← fails: premise.md is 210 lines, target ≤ 80
```

### 4. Write the report

Format:

```markdown
---
adventure: <slug>
author: adventure-lint
created: <today>
---
# Lint Report — <Adventure Title>

## Summary
- ✗ 5 violations (must-fix before module-binder)
- ⚠ 3 warnings (fix recommended)
- ✓ 18 passed

## Per-Lens Scorecard
| Lens | Passed | Failed |
|---|---|---|
| Jaquays (topology) | 4 | 1 |
| Gygax (pressure + agency) | 2 | 1 |
| Stuart (atmosphere) | 4 | 2 |
| Schick (treasure framing) | 3 | 0 |
| Moldvay (table-readiness) | 5 | 1 |

## Violations (must-fix)

### ✗ Jaquays — Room 02: west archway has no distinguishing cue
File: `rooms/02-antechamber-of-tears.md`, section "Features"
Issue: east and west archways described identically. Jaquays gate requires a sensory cue (draft, sound, smell) at each branch.
Fix: add one line to Features — e.g., "A faint smell of vellum drifts from the west archway."

### ✗ Gygax — encounter count below threshold
Rooms: 6. Proper encounters: 2 (03, 06). Conditional: 1 (05). Effective count: 2.5. Required: 3.
Fix: add `encounters/wandering-pressure.md` OR introduce a third proper encounter between Rooms 02-05.

<...etc...>

## Warnings (should-fix)

<...>

## Passing gates

<...>
```

### 5. Never overwrite silently
Existing lint report → write a new dated one; keep both so diffs can be reviewed.

## Output to user

- One-line summary: "X violations, Y warnings across Z gates."
- Link to the generated report.
- Strongest recommended fix (the one violation that would improve the most lens scores at once).

## When this skill does NOT apply

- Adventures in very early draft (premise only; no rooms yet). Use after `dungeon-smith` and `treasure-forger` have run.
- Adventures explicitly tagged `wip: true` in premise frontmatter — lint runs but emits all warnings instead of violations.

## Notes

- This skill is deliberately **pre-module-binder**, not post-. It catches problems before compilation so the compile is clean.
- `persona-review` (Phase 6) will use the lint report as an input — a persona's weighted score correlates with their lens's gate-pass rate, so feeding the lint report speeds up review.
- When a violation is fixed, run lint again. It is idempotent and produces differential output.
