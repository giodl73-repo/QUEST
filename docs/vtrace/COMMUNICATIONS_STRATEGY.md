# QUEST Communications Strategy

## Purpose

This artifact maps accepted QUEST VTRACE intent to user-facing docs surfaces.
The docs package explains adventure design workflow, deterministic mechanical
state, session closeout, checkpoint recovery, and MUDDLE fixture boundaries
without moving narrative authority into engine docs.

## Surface Plan

| Surface ID | Source IDs | Audience | User Question | Generated Docs | Cadence | Owner | Status |
|---|---|---|---|---|---|---|---|
| COMMS-QST-README-001 | NEED-QST-001 / MSC-QST-001 / WP-QST-001 | DM / adventure designer / future agent | Where do I start, and what campaign/session state is current? | `docs/README.md` docs map plus README routing | every docs wave | QUEST maintainer | planned |
| COMMS-QST-CONCEPTS-001 | NEED-QST-004 / REQ-QST-004 / WP-QST-001 | rubric steward / player-style observer | How does QUEST learn without retroactive rescore? | `docs/concepts/forward-only-learning.md` | when rubric or style rules change | QUEST rubric owner | planned |
| COMMS-QST-HOWTO-001 | NEED-QST-002 / IF-QST-001 / WP-QST-002 | session runner / rules auditor | How do I resume or reject checkpoint state safely? | `docs/how-to/checkpoint-recovery.md` | when checkpoint behavior changes | QUEST engine owner | planned |
| COMMS-QST-MODULE-001 | CON-QST-001 / TR-QST-001 / WP-QST-004 | adventure designer / DM | How do I bind a module and confirm the prep gate? | `docs/how-to/bind-module.md` | when module binding changes | QUEST module owner | planned |
| COMMS-QST-CLOSEOUT-001 | CON-QST-003 / VER-QST-006 / VAL-QST-004 / WP-QST-001 | playtest lead / future agent | What artifacts make a session complete? | `docs/traces/session-closeout-walkthrough.md` | when closeout gates change | QUEST playtest owner | planned |
| COMMS-QST-MUDDLE-001 | NEED-QST-005 / IF-QST-005 / WP-QST-003 | MUDDLE adapter maintainer | What QUEST state and commands are exposed to shared clients? | `docs/examples/muddle-quest-surface.md` | when MUDDLE fixture behavior changes | QUEST fixture owner | planned |
| COMMS-QST-CORPUS-001 | REV-QST-003 / WP-QST-001 / WP-QST-002 / WP-QST-003 / WP-QST-004 | docs owner / future agent | Who owns docs updates for campaign, engine, closeout, and fixture surfaces? | `docs/CORPUS.md` | every docs wave | QUEST docs owner | planned |

## Review Checklist

| Item | Required | Decision | Evidence / Rationale |
|---|---|---|---|
| Docs claims trace to controlled source IDs. | yes | accepted | Rows cite mission, CONOPS, interfaces, verification, validation, trace, review, and work packages. |
| Concepts/tutorials/examples do not overclaim unvalidated behavior. | yes | accepted | Rows keep narrative authority, engine state, and shared-client boundaries separate. |
| Public interfaces have expected usage or expected output docs. | if applicable | accepted | Checkpoint, module binding, closeout, and MUDDLE surfaces map to docs. |
| `docs/CORPUS.md` names ownership and update obligations. | if multiple surfaces exist | planned | COMMS-QST-CORPUS-001 records the corpus surface. |
