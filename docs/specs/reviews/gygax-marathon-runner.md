---
spec: marathon-runner
reviewer: gygax
date: 2026-04-19
---

# Gary Gygax on *marathon-runner*

## Overall verdict

A sound dungeon map — terse, keyed, each room knows its purpose. The engine respects dice and state in the way a proper wargame does: seed-locked randomness, no hidden subsystems, mechanical truth written to disk before every choice. The LLM is the DM; the Python engine is the dungeon referee. That's a proper division. But the emitter and checkpoint protocol are under-specified; they dance between JSON and prose in a way that will corrupt narrative fidelity in play. And the heuristics encoding is bold but untested — you've moved PC decision-making into lambdas and strings, which means the day you need to debug a PC's choice, you'll be staring at encoded bias that doesn't translate back to natural language. The spec tells you what to build, not why it's there. A player in your dungeon should feel the walls; here, the engineering is invisible, which is a mark of good design — but only if the invisible parts don't leak.

## Axis scores (1-10)

| Axis | Score | Note |
|---|---|---|
| Clarity of purpose | 9 | Each module has one job: own the mechanical layer. No confusion about Python vs. LLM domains. |
| Robustness | 7 | Checkpoint discipline is solid; state writes are frequent. But no error recovery spec for malformed LLM responses or mid-beat interruptions. |
| Simplicity | 7 | Eight components, each with a clear interface. But heuristics.py encodes decision trees as Python predicates — clever, but opaque to post-hoc audit. |
| Self-containment | 8 | A developer with only this spec and the adventure/PC files can run a session cold. LLM protocol is explicit (stdin/stdout). Caveat: no spec for the adventure/PC file formats themselves. |
| Data discipline | 9 | State model is explicit and three-layered (party, session, campaign facts). Write discipline clear: per-scene for party, per-roll for session, read-only for campaign. No wandering writes. |
| Boundary discipline | 8 | Python/LLM boundary is sharp. But classifier.py is the scar tissue — "when in doubt, route to LLM" is a confession that the boundary isn't always clear. |
| Extensibility | 7 | Scene state machine is extensible. But heuristics.py grows via hardcoding PC lambdas. No mechanism for data-driven decision encoding. |
| Operational clarity | 8 | Three run modes are unambiguous. But no validation spec for malformed inbound JSON or partial LLM responses. |

**Total: 63/80**

## What works

1. **Checkpoint discipline.** Before every LLM beat, write `state/checkpoint.json`, then block. On resume, re-enter from that packet. Zero state loss on interruption.
2. **Seed-locked dice with `seed_position` tracking.** Every roll is reproducible by index. The day you need to replay "what if Kessa had rolled 14," you can.
3. **Three-layer state model.** Party / session / campaign facts are separate, independently inspectable. No god-object.
4. **Heuristics as ordered predicates.** Decision order encodes *why* Aelric picked that target — not memory, not instinct. Rule.
5. **LLM as stdin/stdout, not SDK.** No library coupling. Copy-paste or pipe both work.
6. **`loader.py` parses once, holds in memory.** Respects the file system; no per-beat re-parsing.

## What fails

1. **Inbound packet validation is absent.** The outbound packet is verbose and exact; the inbound spec shows optional fields with no schema. What happens if `advance_to_scene` is a string not an int? If `state_updates` is missing entirely? The spec says "Python validates" but shows no schema.
2. **Heuristics lambdas don't scale.** When Thera's signature move depends on whether Hint 2 has been unlocked this session, the lambda needs context that isn't passed to it. The spec doesn't show how deep context gets threaded through.
3. **Classifier boundary rule is a kludge.** "When in doubt, route to LLM" isn't a design decision; it's an admission the boundary isn't watertight. The sixteen "LLM required" cases aren't derived from a principle — they're a list.
4. **Log reconstruction is post-hoc.** `log_writer.py` reconstructs dice rolls from `dice_log.jsonl` + LLM narrative text. But if the narrative says "Grom casts bless," how does the log writer know whether that's narrating a *completed* check or an *upcoming* one? The checkpoint packet should include a `log_entry_stub` the LLM fills in.
5. **No adventure/PC file format spec.** `loader.py` parses `### Scene N` headers and `**AC** N · **HP** N` patterns — but what if AC is written `AC15`? No reference to actual file formats.
6. **Scene exit conditions undefined.** "Encounter resolved? Trust established? Key loot found?" — but how does Python know the LLM has narrated the condition it's waiting for? Who triggers scene completion?
7. **Parallel beats have no interface.** Wandering-pressure rolls and symptom tracking are mentioned as "parallel" but there's no data structure, write discipline, or log path defined.

## Recommendations

1. Write a JSON Schema for the inbound packet. Show three malformed examples and how Python handles each.
2. Encode heuristics as data (rule lists), not lambdas — more testable, auditable, accessible to non-coders.
3. Add a `log_entry_stub` field to outbound packets. LLM fills in prose around the stub; log writer uses the filled stub as ground truth.
4. Specify adventure/PC file format with regex patterns. Show one minimal example of each.
5. Define "scene complete" precisely — Python-verified vs LLM-triggered, and what happens if they disagree.
6. Give `scene.py` a `pending_beats: list[ParallelBeat]` queue checked after every LLM response.

## Final line

Build the engine, but don't ship it until you've written the schemas, the boundary diagrams, and the file format specs — the things that let someone else run a session from this document without reading your code.
