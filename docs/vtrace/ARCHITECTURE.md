# QUEST Architecture

## Scope

Repo: QUEST

VTRACE stage: Architecture

Baseline date: 2026-06-01

## Architecture Elements

| Architecture ID | Parent Specs | Element | Responsibility | Boundary | Verification Target |
|---|---|---|---|---|---|
| ARCH-QST-001 | SPEC-QST-001 | Adventure skill pipeline | Composes adventure artifacts and review gates before session prep. | Skills create reviewed artifacts; runtime does not invent design. | Inspect skills/adventure/module state. |
| ARCH-QST-002 | SPEC-QST-002 | Deterministic runtime engine | Owns dice, state, checkpoints, logs, module binding, and recovery. | Narrative generation cannot bypass mechanical truth. | Run selected engine commands/tests. |
| ARCH-QST-003 | SPEC-QST-003, SPEC-QST-004 | Learning closeout layer | Gates sessions, panel reviews, logs innovations, updates rubric/style state forward-only. | No retroactive rescore. | Inspect session and persona artifacts. |
| ARCH-QST-004 | SPEC-QST-005 | MUDDLE fixture boundary | Exposes QUEST-owned state/commands to shared clients. | MUDDLE owns rendering/client behavior, not adventure rules. | Run or inspect MUDDLE fixture commands. |

## Data And Control Flow

```text
campaign/adventure need -> skill pipeline -> module/review
  -> runtime start/resume/roll/checkpoint
  -> gate/panel/innovation/handoff
  -> forward-only rubric/style updates
  -> optional MUDDLE fixture proof
```

## Architecture Risks

| Risk ID | Risk | Mitigation |
|---|---|---|
| RISK-QST-001 | Narrative output bypasses deterministic state. | Runtime engine owns mechanical truth and recovery. |
| RISK-QST-002 | Session closeout is skipped. | Learning closeout layer blocks completion. |
| RISK-QST-003 | Rubric changes rewrite history. | Forward-only governance boundary. |

## Role Review Summary

No critical or major actionable findings remain. Exact package IDs, interface
schemas, and verification commands are deferred to later stages.
