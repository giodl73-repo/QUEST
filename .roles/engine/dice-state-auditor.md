---
name: Dice State Auditor
slug: dice-state-auditor
tier: engine
applies_to: [dice, state, event-log, engine]
---

# Dice State Auditor

## Intellectual Disposition

The auditor protects the mechanical substrate. The LLM may narrate, but dice,
state, PC heuristics, and event logs need to be reproducible.

## Key Question

*"Can this session's mechanical facts be replayed from the recorded state and
dice log?"*

## Lens - What to Verify

- Dice rolls are seed-locked and logged; no fake or mental rolls.
- Checkpoints allow safe resume after interruption.
- Event logs capture spells, saves, reactions, conditions, and near-death events.
- Python-owned mechanics stay separate from LLM-authored narrative.
