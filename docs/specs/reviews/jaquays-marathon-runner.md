---
spec: marathon-runner
reviewer: jaquays
date: 2026-04-19
---

# Jennell Jaquays on *marathon-runner*

## Overall verdict

This is competent infrastructure for a single, linear playthrough — but it's a corridor, not a dungeon. The scene progression is deterministic and unidirectional; the architecture offers no way to shortcut, loop back, or approach the same beat from a different entry point. The checkpoint system is defensive (good: zero state loss on interrupt) but not explorative (bad: you can't use a checkpoint as a fast-travel landmark). The component design is tidy but rigid: each piece fits its neighbor snugly, which means pulling one out breaks everything. That's not craft; that's a supply chain.

I can see the session state after scene 3 — but I can't *use* that state to play scene 2 differently, or to skip scenes 0–2 and start at the encounter I care about. The heuristics are encoded once at session start; they don't evolve as the PCs learn (or fail). The one bit of verticality in the architecture — the classifier routing to LLM or Python — doesn't extend to the component layer. You can't spin up a lightweight mode that only uses Python + dice, skipping the LLM.

## Axis scores (1-10)

| Axis | Score | Note |
|---|---|---|
| Clarity of purpose | 9 | Spec is explicit about what each component does and when. Boundary rules are clear. |
| Robustness | 8 | Checkpoint discipline is thorough; state layers are separated. No ambiguity about write order. |
| Simplicity | 7 | Each component is simple in isolation. But the coupling between them is intricate. |
| Self-containment | 5 | Components don't work independently. Try using `dice.py` without the scene loop; you'll need state, context, and the full pipeline. |
| Data discipline | 9 | Persistent state is explicit. Write order is enforced. |
| Boundary discipline | 8 | "Python resolves" vs "LLM required" is well-defined. But the boundary between `scene.py` and `emitter.py` is blurry (who owns the beat loop?). |
| Extensibility | 4 | No hooks for custom heuristics, custom classifiers, or custom scene progression. To tweak behavior, you rewrite the module. |
| Operational clarity | 7 | `start`, `resume`, `status` are clean entry points. But there's no `goto-scene` or `replay-scene`. |

**Total: 57/80**

## Architecture topology analysis

**Entry points:** Three — `start`, `resume`, `status`. All converge on the same scene-loop engine. There's no way to enter at scene 5, or to replay scene 3 from a prior saved state, or to branch based on a prior choice.

**Loops:** None. The scene index advances monotonically 0 → 1 → 2 → end. The dungeon has no cycles.

**Shortcuts:** The checkpoint system offers one: `resume` jumps back to an LLM beat without replaying the lead-up. But you can't jump to a prior *scene* — only a prior *beat*.

**Verticality:** The classifier offers some — Python vs LLM — but it doesn't extend to the architecture itself. You can't spin up a lightweight mode with just Python + dice. The depth of the system is fixed.

**Independent inhabitance:** Heuristics are static after session load. A PC's decision order doesn't change based on prior failures. The doubt-die result doesn't feed back into future doubt-die rolls. The PCs are NPCs, not agents.

## What works

- Explicit state layers. You know where every piece of session state lives.
- Checkpoint contract. Zero state loss on interrupt.
- Dice reproducibility. Same seed + same scene sequence = same rolls.
- Clear classification rule. "When in doubt, route to LLM."
- Honest re-entrancy. The `resume` protocol is straightforward.

## What fails

- Linear progression. Scenes advance in index order with no branching.
- No component reuse. `dice.py`, `heuristics.py`, `classifier.py` are married to the scene loop.
- No independent entry points. Every session starts at scene 0.
- Checkpoints aren't landmarks. You can't say "jump to saved state after the rite encounter."
- Heuristics don't adapt. PC decision-making is encoded once; it doesn't evolve.
- No extension points. Custom heuristics or classifiers require forks.

## Recommendations

1. **Make components independently testable.** Extract `scene.py` as an orchestrator, not a mandate.
2. **Add scene graph support.** Use `scene_id` (string slug) instead of `scene_index`. Let scenes point to other scenes via conditional edges.
3. **Expose checkpoint as a first-class shortcut.** Add `goto-checkpoint` and `list-checkpoints`.
4. **Extend the classifier.** Use chain-of-responsibility instead of a single `classify()` function.
5. **Give PCs adaptive state.** Track "doubt-die failures in this session" and "signature moves used"; let heuristics reference this history.
6. **Add a `--no-llm` mode** for replays or testing.

## Final line

The spec is a good first pass at mechanical bookkeeping, but it's a tool for recording decisions, not for exploring a space. To make this feel like design and not just logging, you need loops, shortcuts, independent components, and adaptive inhabitants.
