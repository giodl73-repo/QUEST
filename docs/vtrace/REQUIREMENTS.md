# QUEST Requirements

## Scope

Repo: QUEST

VTRACE stage: Requirements

Baseline date: 2026-06-01

## Requirement Matrix

| Requirement ID | Requirement | Source | Rationale | Priority | Owner Surface | Verification Method | Status |
|---|---|---|---|---|---|---|---|
| REQ-QST-001 | QUEST shall keep adventure design artifacts tied to the documented skill pipeline before session prep. | NEED-QST-001 / CON-QST-001 | Design work needs repeatable review and handoff. | must | `.claude/skills`, adventures | inspection | proposed |
| REQ-QST-002 | QUEST shall block session prep when module binding or persona review evidence is missing. | CON-QST-001 | Live play should not start from unbound or unreviewed material. | must | adventure module/reviews | inspection, command | proposed |
| REQ-QST-003 | QUEST shall keep dice, state, checkpoints, event logs, and module binding under deterministic engine control. | NEED-QST-002 / CON-QST-002 | Mechanical truth must be inspectable and replayable. | must | Rust engine, state files | command | proposed |
| REQ-QST-004 | QUEST shall halt or enter recovery when checkpoint or inbound state is invalid. | CON-QST-002 | Narrative cannot invent state after invalid handoff. | must | engine checkpoint flow | command, inspection | proposed |
| REQ-QST-005 | QUEST shall require gate, panel, innovation, seed-tracker, and handoff closure before a playtest session is complete. | NEED-QST-003 / CON-QST-003 | Learning loop closure is the product. | must | sessions, personas, tracker | inspection | proposed |
| REQ-QST-006 | QUEST shall apply rubric amendments and player-style promotions only after threshold evidence and ratification. | NEED-QST-004 / CON-QST-004 | Learning must remain forward-only and evidence-triggered. | must | personas, innovations | inspection | proposed |
| REQ-QST-007 | QUEST shall not retroactively rescore earlier sessions after rubric changes. | Mission constraints | Historical evidence must stay stable. | must | tracker/session records | review | proposed |
| REQ-QST-008 | QUEST shall expose MUDDLE surfaces without transferring adventure rules or mechanical truth to shared clients. | NEED-QST-005 / CON-QST-005 | Renderer/client boundaries protect QUEST ownership. | must | MUDDLE binaries/API | command, review | proposed |

## Deferred Definitions

| Deferred ID | Item | Disposition |
|---|---|---|
| DEF-QST-001 | Exact session-close artifact checklist. | Defer to specification baseline. |
| DEF-QST-002 | Engine command L0/L1/L2 ladder. | Defer to verification. |
| DEF-QST-003 | MUDDLE interface contract rows. | Defer to interfaces. |

## Role Review Summary

Role lenses applied from `.roles/`: table module editing, treasure-story
curation, dice/state auditing, rubric governance, session integrity, and
player-style observation.

Findings:

| Role | Finding | Disposition |
|---|---|---|
| Dice State Auditor | Invalid checkpoints need a must-level recovery requirement. | Addressed by REQ-QST-004. |
| Session Integrity Auditor | Closeout stage list must be explicit. | Addressed by REQ-QST-005. |
| Rubric Governance Steward | Forward-only mutation needs threshold and ratification. | Addressed by REQ-QST-006 and REQ-QST-007. |
| Table Module Editor | Session prep must be blocked by missing module/review evidence. | Addressed by REQ-QST-002. |

Fixed-point decision:

No critical or major actionable findings remain for the requirements stage.
Exact specs, interface schemas, verification command levels, and work packages
are deferred to later VTRACE stages.
