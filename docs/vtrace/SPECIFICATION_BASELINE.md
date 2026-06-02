# QUEST Specification Baseline

## Scope

Repo: QUEST

VTRACE stage: Specification Baseline

Baseline date: 2026-06-01

## Baseline Inventory

| Surface | Paths | Baseline Status | Notes |
|---|---|---|---|
| Mission/CONOPS/requirements | `docs/vtrace/` | current | VTRACE planning chain established through requirements. |
| Adventure pipeline | `.claude/skills/`, `adventures/`, `campaign/` | current | Skills compose design, prep, play, review, innovation, and handoff. |
| Runtime engine | `src/`, `state/` | current | Rust engine owns dice, state, checkpoint, event log, and module binding. |
| Learning system | `personas/`, `TRACKER.md` | current | Rubrics and player styles evolve forward-only from evidence. |
| Shared-client fixture | MUDDLE binaries/API | current | Product-owned QUEST surface supports shared clients. |

## Specification Items

| Spec ID | Parent REQ IDs | Type | Baseline | Specification Statement | Verification | Validation | Owner Surface | Risk |
|---|---|---|---|---|---|---|---|---|
| SPEC-QST-001 | REQ-QST-001, REQ-QST-002 | process | current | Adventure material should pass module binding and persona review before session prep. | inspection, command | DM review | adventures/skills | high |
| SPEC-QST-002 | REQ-QST-003, REQ-QST-004 | software | current | Runtime engine owns deterministic dice, state, checkpoint, event log, and recovery behavior. | command | session review | Rust engine/state | high |
| SPEC-QST-003 | REQ-QST-005 | process | current | Session completion requires gate, panel, innovation, seed-tracker, and handoff artifacts. | inspection | playtest review | sessions/personas | high |
| SPEC-QST-004 | REQ-QST-006, REQ-QST-007 | governance | current | Rubric amendments and player-style promotions are threshold-triggered, ratified, and forward-only. | inspection | rubric review | personas/tracker | high |
| SPEC-QST-005 | REQ-QST-008 | interface | current | MUDDLE fixtures expose QUEST-owned state/commands without transferring adventure rules. | command, review | adapter review | MUDDLE binaries/API | medium |

## Unknowns And Deferred Detail

| Unknown ID | Unknown | Risk | Disposition |
|---|---|---|---|
| SPEC-QST-UNK-001 | Exact complete-session checklist is not VTRACE-indexed. | Closeout may be hard to audit. | Defer to validation/trace. |
| SPEC-QST-UNK-002 | Engine command ladder and recovery tests are not selected. | Verification may miss checkpoint edge cases. | Defer to verification. |
| SPEC-QST-UNK-003 | MUDDLE interface rows are not captured yet. | Shared-client boundary may be implicit. | Defer to interfaces. |

## Role Review Summary

Role lenses applied from `.roles/`: table module editing, treasure-story
curation, dice/state auditing, rubric governance, session integrity, and
player-style observation.

Findings:

| Role | Finding | Disposition |
|---|---|---|
| Session Integrity Auditor | Complete-session artifact list belongs in baseline. | Addressed by SPEC-QST-003. |
| Dice State Auditor | Runtime ownership and recovery must be high risk. | Addressed by SPEC-QST-002. |
| Rubric Governance Steward | Forward-only governance must be specification-level. | Addressed by SPEC-QST-004. |
| Treasure Story Curator | Treasure/story specificity remains product baseline but needs later validation rows. | Deferred to validation/trace. |

Fixed-point decision:

No critical or major actionable findings remain for the specification baseline.
Gate is `pass_with_risk` because exact closeout checklist, command ladder, and
interface rows are deferred.
