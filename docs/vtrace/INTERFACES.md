# QUEST Interfaces

## Scope

Repo: QUEST

VTRACE stage: Interfaces

Baseline date: 2026-06-01

## Interface Matrix

| Interface ID | Parent Architecture | Interface | Producer | Consumer | Contract | Evidence |
|---|---|---|---|---|---|---|
| IF-QST-001 | ARCH-QST-001 | Adventure module packet | Skill pipeline and adventure files | DM, session prep reviewer | Packet carries adventure material, module binding, persona review, and prep readiness evidence before session start. | Inspect adventure/module/review files. |
| IF-QST-002 | ARCH-QST-002 | Runtime command surface | Rust engine | Session runner, rules auditor | Commands own start/resume/status/roll/bind-module/checkpoint behavior and reject invalid inbound state. | Run selected engine commands/tests. |
| IF-QST-003 | ARCH-QST-002 | Checkpoint and event log | Runtime engine/state files | Session runner, handoff reviewer | State changes, dice, event log, and checkpoint packets are deterministic and resumable. | Inspect state/log/checkpoint output. |
| IF-QST-004 | ARCH-QST-003 | Learning closeout packet | Gate, panel, innovation, seed tracker, handoff artifacts | Playtest lead, rubric steward | Packet is complete only when every closeout stage exists and rubric/style mutations are forward-only and ratified. | Inspect session/persona/tracker artifacts. |
| IF-QST-005 | ARCH-QST-004 | MUDDLE quest surface | QUEST MUDDLE fixture | MUDDLE host/client | QUEST exposes product-owned state and commands; MUDDLE owns rendering/client behavior and must not own adventure rules or mechanical truth. | Run or inspect MUDDLE fixture. |

## Boundary Rules

- Narrative output cannot bypass deterministic dice, state, checkpoint, or event-log evidence.
- Invalid checkpoint or inbound state enters recovery instead of invented continuity.
- Rubric amendments and player-style promotions are forward-only.
- Shared clients must not own QUEST adventure rules or mechanical truth.

## Role Review Summary

Role lenses applied from `.roles/`: table module editing, treasure-story
curation, dice/state auditing, rubric governance, session integrity, and
player-style observation.

No critical or major actionable findings remain. Exact command levels,
closeout checklist rows, and trace IDs are deferred to later stages.
