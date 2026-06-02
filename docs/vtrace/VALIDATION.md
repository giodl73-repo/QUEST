# QUEST Validation

## Scope

Repo: QUEST

VTRACE stage: Validation

Baseline date: 2026-06-01

## Validation Scenarios

| Validation ID | Parent Verification | Scenario | Acceptance Standard | Evidence |
|---|---|---|---|---|
| VAL-QST-001 | VER-QST-001 | DM prepares an adventure/session. | Module binding and persona review are present before session prep is accepted. | Adventure/module/review packet. |
| VAL-QST-002 | VER-QST-002, VER-QST-003, VER-QST-004 | Session runner advances mechanical state. | Rust engine owns dice, status, state, checkpoints, and logs; narrative does not bypass mechanics. | Test/status/roll output and state artifacts. |
| VAL-QST-003 | VER-QST-005 | Invalid checkpoint or inbound state appears. | Runtime halts or enters recovery instead of inventing continuity. | Recovery evidence or blocked state record. |
| VAL-QST-004 | VER-QST-006 | Playtest closeout is claimed complete. | Gate, panel, innovation, seed-tracker, handoff, and forward-only rubric/style evidence are all present. | Complete closeout packet. |
| VAL-QST-005 | VER-QST-007 | MUDDLE consumes QUEST surface. | QUEST owns adventure rules and mechanical truth; MUDDLE owns rendering/client behavior. | MUDDLE save/transcript proof. |

## Claim Rules

- A session is incomplete until every closeout stage exists.
- Rubric and player-style changes are prospective only.
- Invalid state cannot be repaired by narrative prose.
- Shared-client proof does not transfer adventure rules.

## Role Review Summary

Role lenses applied from `.roles/`: table module editing, treasure-story
curation, dice/state auditing, rubric governance, session integrity, and
player-style observation.

No critical or major actionable findings remain. Exact checklist refinements and
implementation tasks move to trace and work packages.
