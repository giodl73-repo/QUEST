# QUEST Work Packages

## Scope

Repo: QUEST

VTRACE stage: Work Packages

Baseline date: 2026-06-01

## Package Backlog

| WP ID | Source | Title | Outcome | Verification / Validation | Status |
|---|---|---|---|---|---|
| WP-QST-001 | GAP-QST-001, REV-QST-001 | Lock complete-session checklist | `README.md` already defines the closeout sequence as gate, panel, innovation, seed tracker, and handoff with artifact paths; checklist is locked as the current closeout contract. | VER-QST-006, VAL-QST-004 | complete |
| WP-QST-002 | GAP-QST-002, REV-QST-002 | Prove checkpoint/recovery path | `cargo test --quiet checkpoint` passed existing checkpoint resume coverage, but no explicit invalid-inbound-state proof was found; blocked until that test or command evidence is added. | VER-QST-005, VAL-QST-003 | blocked |
| WP-QST-003 | GAP-QST-003, REV-QST-003 | Prove MUDDLE quest surface | `cargo run --bin quest-muddle -- --save target\quest-ai.muddle --transcript target\quest-ai.txt` passed and produced product-owned save/transcript proof. | VER-QST-007, VAL-QST-005 | complete |
| WP-QST-004 | TR-QST-001 | Lock module binding prep gate | `cargo run --bin quest -- bind-module 0007-the-silver-ingot-confession` succeeded but regenerated a large `module.md` delta; package is blocked until that generated module change is reviewed instead of accepted blindly. | VER-QST-001, VAL-QST-001 | blocked |

## Execution Rules

- Mechanical truth must stay in engine state, dice, checkpoints, and logs.
- Rubric/style updates are prospective only.
- Do not mark a session complete with partial closeout evidence.
