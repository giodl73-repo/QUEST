# QUEST CONOPS

## Scope

Repo: QUEST

VTRACE stage: CONOPS

Baseline date: 2026-06-01

This CONOPS describes how QUEST users design, run, review, and learn from D&D
adventures while keeping mechanical state deterministic, narrative generation
bounded, and rubric/player-style evolution forward-only.

## Operational Scenarios

| Scenario ID | Actor | Trigger | Nominal Flow | Degraded / Failure Flow | Evidence Output |
|---|---|---|---|---|---|
| CON-QST-001 | Adventure designer | A new adventure or campaign beat is needed. | Use the design skill pipeline, bind module, run persona review, prepare session materials. | If module binding or review evidence is missing, block session prep. | Adventure files, module, review notes, DM letter. |
| CON-QST-002 | Session runner | A live or rehearsal session starts. | Start/resume engine, roll deterministic dice, emit/check checkpoint packets, update state and event logs. | If checkpoint or inbound state is invalid, halt at resume/recovery instead of inventing state. | State files, dice log, event log, checkpoint packet. |
| CON-QST-003 | Playtest lead | Session play ends. | Run gate scorecard, panel review, innovation logging, seed tracking, and handoff. | If any close stage is missing, session remains incomplete and next prep is blocked. | Gate, panel summary, innovations, handoff, `TRACKER.md` update. |
| CON-QST-004 | Rubric/player-style steward | Repeated innovations cluster. | Apply threshold checks, draft amendment or player style, ratify forward-only, lock next session rubric version. | If threshold or ratification is missing, record candidate only and do not mutate rubric/catalog. | Rubric version bump, style entry, innovation cluster. |
| CON-QST-005 | MUDDLE adapter maintainer | QUEST surface needs shared-client proof. | Run product-owned MUDDLE host/surface launcher and transcript path while QUEST owns rules/state. | If renderer requires adventure rules, reject boundary and add interface requirements. | MUDDLE save/transcript/checkpoint evidence. |

## Operating Modes

| Mode | Purpose | Entry Condition | Exit Condition |
|---|---|---|---|
| Design pipeline | Build reviewed adventure material. | New adventure, revision, or campaign beat. | Module and review evidence are ready for prep. |
| Session runtime | Own dice, state, checkpoints, and logs. | Session starts or resumes. | State is advanced or recovery is required. |
| Learning closeout | Convert play evidence into gate/panel/innovation/handoff. | Session ends. | Next session has a clean handoff and locked rubric version. |
| Shared-client fixture | Exercise MUDDLE without moving QUEST rules. | QUEST host/surface is stable. | Fixture evidence passes and remains product-owned. |

## Role Review Summary

Role lenses applied from `.roles/`: table module editing, treasure-story
curation, dice/state auditing, rubric governance, session integrity, and
player-style observation.

Findings:

| Role | Finding | Disposition |
|---|---|---|
| Dice State Auditor | CONOPS needs an invalid-checkpoint degraded path. | Addressed in CON-QST-002. |
| Session Integrity Auditor | Closeout cannot be optional. | Addressed in CON-QST-003. |
| Rubric Governance Steward | Rubric/style mutation requires threshold and ratification. | Addressed in CON-QST-004. |
| Table Module Editor | Module binding and review must gate session prep. | Addressed in CON-QST-001. |

Fixed-point decision:

No critical or major actionable findings remain for the CONOPS stage. Exact
requirement IDs, validation command levels, interface rows, and work packages
are deferred to later VTRACE stages.
