# QUEST Verification

## Scope

Repo: QUEST

VTRACE stage: Verification

Baseline date: 2026-06-01

## Verification Ladder

| Level | Verification ID | Parent Requirements / Interfaces | Command Or Inspection | Purpose | Expected Evidence |
|---|---|---|---|---|---|
| L0 | VER-QST-001 | REQ-QST-001, REQ-QST-002, IF-QST-001 | Inspect `.claude/skills`, `adventures/`, and module/review artifacts | Confirm session prep has design pipeline evidence. | Module and review status is visible. |
| L0 | VER-QST-002 | REQ-QST-003, IF-QST-002 | `cargo test --quiet` | Prove runtime baseline tests pass. | Passing test output or explicit blocker. |
| L1 | VER-QST-003 | REQ-QST-003, IF-QST-002 | `cargo run -- status` | Verify current runtime state can be inspected. | Status output names campaign/session state. |
| L1 | VER-QST-004 | REQ-QST-003, IF-QST-002 | `cargo run -- roll 1d20+5 --seed S07-scene6 --adv --bless` | Verify deterministic dice command behavior. | Deterministic roll output. |
| L2 | VER-QST-005 | REQ-QST-004, IF-QST-003 | Inspect or run checkpoint/resume recovery path | Verify invalid inbound state halts or recovers. | Recovery evidence or explicit blocker. |
| L2 | VER-QST-006 | REQ-QST-005, REQ-QST-006, REQ-QST-007, IF-QST-004 | Inspect gate, panel, innovation, seed-tracker, handoff, rubric/style artifacts | Verify complete learning closeout and forward-only mutation. | Complete closeout packet. |
| L2 | VER-QST-007 | REQ-QST-008, IF-QST-005 | `cargo run --bin quest-muddle -- --save target\quest-ai.muddle --transcript target\quest-ai.txt` | Verify product-owned MUDDLE surface. | Save/transcript proof without rule transfer. |

## Verification Rules

- Narrative work is not verification unless it is tied to engine state, dice,
  checkpoint, or closeout artifacts.
- Invalid state evidence is handled as recovery evidence, not continuity.
- Learning closeout verification is complete only when every closeout stage is
  present.

## Role Review Summary

Role lenses applied from `.roles/`: table module editing, treasure-story
curation, dice/state auditing, rubric governance, session integrity, and
player-style observation.

No critical or major actionable findings remain. Exact session checklist
thresholds are deferred to validation, trace, and work packages.
