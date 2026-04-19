---
spec: marathon-runner
reviewer: moldvay
date: 2026-04-19
---

# Tom Moldvay on *marathon-runner*

## Overall verdict

This spec has the bones of a good engine: clear problem statement, modular architecture, and serious thought about state management and re-entrancy. The checkpoint discipline (write before blocking, read on resume) is sound. But the spec is not yet table-ready. It assumes the reader knows your existing session logs and understands vague boundaries ("when in doubt, route to LLM"). A new developer would ask three questions per component. Tighten the interfaces, show complete examples, and name your error cases explicitly.

## Axis scores (1-10)

| Axis | Score | Note |
|---|---|---|
| Clarity of purpose | 9 | Problem stated crisply. Why this system exists is evident. |
| Robustness | 5 | Error cases mostly absent. What happens if checkpoint parse fails? If module.md has malformed stat block? |
| Simplicity | 7 | Architecture is clean, but re-entrancy contract adds moving parts. Worth it, but acknowledged. |
| Self-containment | 6 | References "established format" for S01-S04 logs without showing it. References CLAUDE.md without explaining the schema. |
| Data discipline | 8 | State layers well-defined. Write discipline clear *except* "per scene boundary" + "per dice roll" could overlap. |
| Boundary discipline | 6 | Classifier's LLM boundary fuzzy: "any decision involving grief-paragraph" (undefined term), "when in doubt, route to LLM" invites guessing. |
| Extensibility | 7 | Component structure allows adding new parsers. But no versioning strategy if module format changes. |
| Operational clarity | 7 | Terminal loop well-explained. But `status` output is undefined, and recovery path (^C mid-checkpoint?) is unspecified. |

**Total: 55/80**

## Implementation-readiness check

**What a developer can build immediately:**
- `dice.py` — the RollResult dataclass is precise; the interface is concrete. Implementable cold.
- Terminal loop — the example is concrete. Good.
- `state.py` — the three JSON schemas are shown. Clear.

**Where they will stall:**

1. **`log_writer.py`**: Says "matches S01-S04 format" but doesn't show it. Is the dice roll format `**🎲 PC action**` or something else? Where does read-aloud go relative to mechanical resolution?

2. **`loader.py` PC parsing**: Says "parse YAML frontmatter" but doesn't show the frontmatter schema. The Decision Order example is Python code, not the format it parses from.

3. **`heuristics.py` decision order**: Shows encoding but not how decision-order lists are serialized in PC sheets. What does the source YAML look like?

4. **Error cases absent:**
   - What if `module.md` has a `### Scene N` header but no read-aloud text?
   - What if stat block is incomplete (AC but no HP)?
   - What if checkpoint.json is corrupted?
   - What if LLM response is missing `narrative` or `advance_to_scene`?
   - What if dice expression is invalid like `"1d20+"`?

5. **State write conflict**: "Party state written at every scene boundary. Session state written after every dice roll." If a dice roll happens mid-scene, session.json writes happen before the party state snapshot. Is that intended?

6. **Classifier boundary vague**: "any event where `event.involves_grief_paragraph == True`" — but `event` dataclass is never defined.

7. **Parallel beats**: Scene.py mentions wandering-pressure rolls happening "in parallel" while LLM narrates, but the scene loop is sequential. How do parallel beats get collected?

8. **Re-entrancy edge case**: What if user starts session, reaches checkpoint, then force-quits? On next `resume`, does the script detect a stale checkpoint and ask to delete it, or overwrite silently?

## What works

1. Checkpoint discipline is sound. Write before blocking, delete after response.
2. Dice seed locking solves the original bash problem cleanly.
3. Three-layer state model has good separation of concerns.
4. Component modularity is good. Each module has a single responsibility.
5. Terminal loop example is concrete and shows the user experience unambiguously.

## What fails

1. Examples are illustrative, not exact. The outbound packet has `{ "...current party state..." }`.
2. Source formats undefined. How are PC heuristics serialized? What does module.md's DC table look like as text?
3. Vague boundaries. "When in doubt, route to LLM" is editorial, not a rule.
4. Error cases absent. "Failure modes: raise LoadError" is a start; there are ten more failure modes not listed.
5. State write conflicts unresolved.
6. Log format not shown.
7. `marathon.py status` output undefined.

## Recommendations

1. **Show the log format inline.** Include a minimal S01-style log example. Show where dice rolls appear, where read-aloud goes.
2. **Add a "Source Formats" appendix.** YAML frontmatter schema for PC sheets; DC table format from module.md; Hint system schema.
3. **Define the event dataclass.** Show the minimal fields needed for the classifier: `event.is_dice`, `event.involves_grief_paragraph`, `event.is_option_c`.
4. **Enumerate error cases per component.** A table: Component | Failure | Handler | Raises.
5. **Resolve state write timing.** Propose: "Session state written *after* party state update at scene boundary. Dice rolls within a scene don't trigger session.json writes until scene COMPLETE."
6. **Define re-entrancy recovery.** Checkpoint > 1 hour old → delete and prompt user. Malformed LLM response → checkpoint persists, ask to paste valid JSON.
7. **Show exact terminal flow for `status`.**

## Final line

The spec solves a real problem and the architecture is sound, but it's written for someone who already knows your session format and your world. Tighten the interfaces, show complete examples, name every error case, and resolve the gray zones.
