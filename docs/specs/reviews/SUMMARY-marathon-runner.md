---
spec: marathon-runner
document: review-summary
date: 2026-04-19
reviewers: [gygax, jaquays, schick, moldvay, stuart]
---

# Board Review Summary — *marathon-runner*

## Scores

| Reviewer | Total /80 | Band |
|---|---:|---|
| Gygax | 63 | Strong draft |
| Jaquays | 57 | Core is there; revision needed |
| Schick | 62 | Strong draft |
| Moldvay | 55 | Core is there; revision needed |
| Stuart | 63 | Strong draft |
| **Average** | **60** | **Strong draft — one more pass** |

## Strongest axes (consensus above 8)

- **Clarity of purpose (8.8 avg):** Everyone agrees the problem statement is crisp and each component has one job.
- **Data discipline (8.6 avg):** Three-layer state model, write discipline, seed-locked dice — all sound.
- **Checkpoint contract (implicit 9):** All five reviewers praise the checkpoint-before-block / delete-after-response discipline as the spec's strongest architectural decision.

## Weakest axes (consensus below 7)

- **Self-containment (6.8 avg):** The spec assumes knowledge of S01-S04 log format, CLAUDE.md schema, and existing PC sheet structure. A new implementer would stall on three questions per component.
- **Extensibility (5.8 avg):** Jaquays is harshest (4/10). No hooks, no plugin points, no way to extend heuristics without forking code.
- **Robustness (7.0 avg):** Moldvay is harshest (5/10). Error cases nearly absent across the board.

## Convergent critiques (3+ reviewers)

**P0 — must fix before implementation:**

1. **Inbound JSON validation is absent** (Gygax, Schick, Moldvay). The outbound packet is precise; the inbound spec shows optional fields with no schema. Show 3 malformed examples and how Python handles each. Add a validation dataclass.

2. **Heuristics source format undefined** (Gygax, Schick, Moldvay). Show the YAML format for Playstyle Heuristics in the PC sheet. Show how `loader.py` parses it into Python. Make clear whether a new PC requires code changes or just YAML.

3. **Log writer format not inlined** (Schick, Moldvay, Stuart). "Exact format established by S01-S04" is a promise without delivery. Show a minimal template. Show how dice rolls are tagged for extraction.

4. **Error cases absent** (Gygax, Moldvay, Stuart). A "Recovery and Failure" section is needed. At minimum: corrupted checkpoint.json, malformed LLM response, missing stat block field, invalid dice expression.

5. **Classifier rules should be code, not prose** (Gygax, Jaquays, Stuart). The sixteen LLM-required events are a checklist. Express them as an enum, a dataclass, or pseudocode — something auditable and testable.

**P1 — should fix:**

6. **Checkpoint re-entry context is incomplete** (Schick, Stuart). The checkpoint contains beat-level context but not scene-level: no scene-opening read-aloud, no accumulated NPC dialogue. If interrupted mid-scene, the LLM re-enters without the scene's narrative history. Extend checkpoint to include `scene_narrative_so_far`.

7. **State write timing ambiguity** (Moldvay). "Party state at scene boundary" + "session state after every roll" can interleave. Define ordering explicitly.

8. **`marathon.py status` output undefined** (Gygax, Moldvay, Schick). Specify exactly what prints: current scene, scene read-aloud, party HP/slots, pending checkpoint or none.

**P2 — authorial judgment:**

9. **(Jaquays) Scene graph instead of linear index.** Replace `scene_index` with `scene_id` string slug. Allow conditional edges. Enable loops and re-entry.
10. **(Stuart) Open classifier section with the moral center.** Move "False-Python-resolved corrupts voice more than false-LLM-required wastes time" to be the first sentence of the classifier section.
11. **(Gygax) Log entry stubs in outbound packet.** Include a `log_entry_stub` field; LLM fills it in; log writer uses filled stubs as source of truth. Prevents post-hoc prose-parsing.
12. **(Jaquays) Independent component usability.** `dice.py` and `heuristics.py` should be usable without the full scene loop. Extract `scene.py` as orchestrator, not mandate.

## Divergent critiques (single reviewer)

- **(Jaquays, 4/10 extensibility):** No hooks, no adaptive PC state. Heuristics don't learn from failures. "The inhabitants are NPCs, not agents."
- **(Moldvay, 5/10 robustness):** Harshest on error cases. Wants a full failure-modes table per component.
- **(Stuart):** Wants the spec to have a "voice" — to state what kind of play this system believes in. The checkpoint should feel like a transition, not a shipping container.
- **(Schick):** Wants checkpoint extended to cover full scene narrative context, not just current-beat context. "The promise of re-entrancy without re-reading the module isn't fully delivered."

## Go/No-Go

**One more pass before implementation.** P0 fixes (1-5) are all addenda to the spec, not architectural rethinks. None require changing the components or the interfaces. Estimated time: 45-60 minutes of spec work. After P0 fixes, the spec is implementation-ready.

The architecture is sound. The core insight — Python owns mechanical truth; LLM owns narrative truth; checkpoint is the handoff — is validated by all five reviewers. No one asked for a different architecture. Everyone asked for the same thing: complete what you started.
