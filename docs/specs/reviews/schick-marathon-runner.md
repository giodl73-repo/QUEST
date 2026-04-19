---
spec: marathon-runner
reviewer: schick
date: 2026-04-19
---

# Lawrence Schick on *marathon-runner*

## Overall verdict

This is a dungeon engineer's spec. Not a narrative one — Python owns the mechanics, the LLM handles the voice. What strikes me first is the honesty: the author knows where the line is, and they're not trying to make code do what prose does. The checkpoint protocol is the treasure here — the one architectural decision that earns its weird complexity. Before every LLM beat, write the full state and dice history to JSON, then re-enter from that point if the session interrupts. That's a narrative checkpoint with a full mechanical ledger.

What worries me is whether the checkpoint actually contains *enough* context for the LLM to be re-entrant without reading the module. The outbound packet includes `read_aloud` — but only for the *current beat*, not for the entire scene so far. If you get interrupted mid-scene and resume, you've lost the scene-opening narration and all prior NPC dialogue. The promise of checkpoint re-entrancy without re-reading the module isn't fully delivered.

## Axis scores (1-10)

| Axis | Score | Note |
|---|---|---|
| Clarity of purpose | 9 | "Replace bash-dice + LLM-only with Python owning mechanics." Clear. |
| Robustness | 7 | Seed-locked RNG, three-layer state, re-entrancy contract solid. No error recovery for malformed LLM responses; no checkpoint cleanup on failure. |
| Simplicity | 8 | Eight components, clear boundaries. JSON-in-JSON packets add complexity. |
| Self-containment | 8 | Dependencies minimal (pyyaml optional). But `loader.py` parses eagerly — no lazy loading for large adventures. |
| Data discipline | 8 | Three state layers, write discipline clear. Checkpoint.json and session.json have overlapping `scene_index` — potential de-sync. |
| Boundary discipline | 8 | Classifier draws the line cleanly. But the sixteen LLM-required events live in prose; they should be an enum or config, not derived at runtime. |
| Extensibility | 6 | No plugin points. Adding a new doubt-die interpretation requires code change, not data change. |
| Operational clarity | 8 | Three CLI modes are clear. Terminal output example is readable. `marathon.py status` doesn't specify what happens when a checkpoint exists. |

**Total: 62/80**

## What works

1. **The checkpoint-as-ledger model.** Writing full state + dice history before blocking on LLM input. Zero state loss on interruption.
2. **Dice engine as a first-class object.** Seed-locked, auditable, position-tracked. You can replay "what if Kessa had rolled 14" with the same seed at the same position.
3. **Heuristics as mechanical interpretation only.** The decision not to let `heuristics.py` handle narrative choices is wise. Mechanical → Python, narrative → LLM. Clean line.
4. **Read-only campaign facts.** Preventing mid-game drift in permanent story decisions.
5. **Explicit LLM packet structure.** Inbound and outbound JSON detailed enough for mechanical context. Almost enough for full narrative re-entry.

## What fails

1. **Checkpoint re-entrancy is incomplete.** The checkpoint example doesn't include the full scene-opening read-aloud or all prior NPC dialogue in that scene. If interrupted mid-scene, the LLM re-enters without the scene's narrative context. This breaks the promise.
2. **No version or rollback semantics.** What happens if the LLM's inbound packet references a nonexistent PC? If `advance_to_scene` jumps backward? No validation clause, no "reject and re-prompt," no state rollback.
3. **State de-sync risk.** Both `session.json` and `checkpoint.json` contain `scene_index`. If checkpoint deletion fails after LLM response, next `resume` sees a stale checkpoint.
4. **Heuristics as static lambdas.** `AELRIC_DECISIONS` is hardcoded. Where does this live? In PC YAML? In Python source? If in source, it can't scale to a new PC without code changes.
5. **Log writer undertreated.** The final output — S{N}-log.md — is described as "exact format established by S01-S04" without showing that format. This is the treasure the whole session produces; it deserves clarity.
6. **Eager loading.** If an adventure grows to 15 scenes, parsing all at load time could be slow.

## Recommendations

1. **Extend checkpoint completeness.** Include the full read-aloud for the current scene, plus a summary of all NPC dialogue so far in that scene.
2. **Add state validation and rollback.** When `inbound.json` arrives, validate all referenced PCs exist, `advance_to_scene` is forward-only, `state_updates` keys are valid fields.
3. **Specify heuristics source.** Show the YAML format. Make clear whether a new PC requires code changes or just a new YAML file.
4. **Elevate log_writer to first-class spec.** Show the format inline. Show how dice rolls are tagged so the log writer can extract them.
5. **Add a lazy scene loader note.** Parse scenes on-demand for large adventures.
6. **Specify `status` output completely.** Current scene, read-aloud (for re-orientation), party HP/slots, pending checkpoint.

## Final line

This is a well-engineered checkpoint protocol in search of a complete spec. The core idea — separate mechanical truth (Python) from narrative truth (LLM) — is the right dungeoncraft. But the promise of re-entrancy without re-reading the module isn't fully delivered, and the signature component (heuristics) is underspecified. Trace the design all the way through, especially in state validation and the completeness of the LLM's re-entry context.
