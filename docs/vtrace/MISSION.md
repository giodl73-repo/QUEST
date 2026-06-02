# QUEST Mission

## Scope

Repo: QUEST

VTRACE stage: Mission

Baseline date: 2026-06-01

QUEST is a D&D 5e adventure workshop that learns from its own playtests. Its
mission is to analyze session evidence, design adventures through small skills,
run deterministic mechanical play support, and feed gate/panel/innovation
results back into rubrics, player-style catalogs, skills, and campaign state.

## Mission Need

| Need ID | Need | Primary User | Success Signal |
|---|---|---|---|
| NEED-QST-001 | Compose adventures, parties, NPCs, treasures, encounters, and modules through a repeatable skill pipeline. | Adventure designer, DM | Design artifacts move through documented skills and persona review before play. |
| NEED-QST-002 | Run live-table mechanical state deterministically while leaving narrative to the LLM/DM. | Session runner, rules auditor | Rust commands own dice, state, checkpoints, event logs, and module binding. |
| NEED-QST-003 | Close every playtest through gate, panel, innovation, and handoff stages. | Playtest lead, rubric steward | Session outputs update scorecards, panel summaries, innovations, handoffs, and `TRACKER.md`. |
| NEED-QST-004 | Preserve emergent learning without retroactive rescore. | Future maintainer, player-style observer | Rubric amendments and player-style promotions are forward-only and evidence-triggered. |
| NEED-QST-005 | Keep MUDDLE play-surface adoption product-owned. | MUDDLE adapter maintainer | QUEST exposes game state and commands while shared clients own rendering. |

## Mission Success Criteria

| Criterion ID | Criterion | Evidence Surface | Deferred Detail |
|---|---|---|---|
| MSC-QST-001 | A future agent can identify the current campaign/session state and next stage. | `README.md`, `TRACKER.md`, `adventures/`, `state/` | Trace rows deferred to `TRACE.md`. |
| MSC-QST-002 | Mechanical operations are deterministic, resumable, and inspectable. | `cargo run -- start/resume/status/roll/bind-module` | Command levels deferred to `VERIFICATION.md`. |
| MSC-QST-003 | Rubric and player-style evolution is evidence-triggered and forward-only. | `personas/`, session gate/panel/innovation files | Validation scenarios deferred to `VALIDATION.md`. |
| MSC-QST-004 | Shared MUDDLE adoption does not transfer QUEST rules to the renderer. | `quest-muddle*` binaries | Interface ownership deferred to `INTERFACES.md`. |

## Constraints

- QUEST must not retroactively rescore earlier sessions after rubric changes.
- Rust owns mechanical truth; LLM/DM narrative must not bypass state and dice
  evidence.
- Treasure/story consequences are product claims and need campaign/session
  evidence.
- MUDDLE clients must not own QUEST adventure rules.

## Initial Validation Expectations

```powershell
cargo test --quiet
cargo run --bin quest -- status
cargo run --bin quest -- roll 1d20+5 --seed S07-scene6 --adv --bless
cargo run --bin quest -- bind-module 0007-the-silver-ingot-confession
cargo run --bin quest-muddle -- --save target\quest-ai.muddle --transcript target\quest-ai.txt
```

## Role Review Summary

Role lenses applied from `.roles/`: table module editing, treasure-story
curation, dice/state auditing, rubric governance, session integrity, and
player-style observation.

Findings:

| Role | Finding | Disposition |
|---|---|---|
| Dice State Auditor | Mission must keep deterministic mechanical truth separate from narrative generation. | Addressed in NEED-QST-002 and constraints. |
| Session Integrity Auditor | No session can skip gate, panel, innovation, or handoff closure. | Addressed in NEED-QST-003. |
| Rubric Governance Steward | Forward-only rubric evolution must be explicit. | Addressed in NEED-QST-004. |
| Treasure Story Curator | Treasure must remain story-bearing, not generic reward text. | Preserved as product mission; detailed requirements deferred. |

Fixed-point decision:

No critical or major actionable findings remain for the mission stage. Exact
requirements, command levels, interface rows, and work packages are deferred to
later VTRACE stages.
