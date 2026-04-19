---
spec: marathon-runner
reviewer: patrick-stuart
date: 2026-04-19
---

# Patrick Stuart on *marathon-runner*

## Overall verdict

This is a capable and honest spec — it knows what it wants to solve, it solves it cleanly, and it doesn't lie about the hard edges. The re-entrancy contract is real; the seed-locked dice is a small work of engineering discipline. But the prose itself is thin. This reads like a system designed to *service* play rather than *shape* it. A checkpoint.json arrives as JSON, not as an object with history or consequence. The classifier's boundary rule — "when in doubt, LLM" — is the only sentence in the spec that has philosophy in it, and it's buried in a list.

The spec doesn't yet know it is *about something*. It is about mechanics serving narrative, which is correct, but the spec doesn't say what *kind* of narrative, what *kind* of play, what the marriage between Python and LLM believes about doubt. Read this expecting competence and clarity. Don't expect it to haunt you.

## Axis scores (1-10)

| Axis | Score | Note |
|---|---|---|
| Clarity of purpose | 9 | "Replace bash dice + LLM-only pipeline" is crystalline. |
| Robustness | 8 | Re-entrancy contract is bulletproof. But no stated recovery for corrupted checkpoint or split state. |
| Simplicity | 8 | Architecture is hierarchical and lean. But classifier rules are prose-enumerated, not expressed as code. |
| Self-containment | 8 | Declares dependencies cleanly. But relies on external LLM; if stdin blocks, system blocks. |
| Data discipline | 9 | Three-layer state model is consistent. Write discipline is stated. Checkpoint born-and-deleted per LLM beat. |
| Boundary discipline | 7 | Classifier boundary is *stated* clearly but not *integrated*. "When in doubt, LLM" is a rule without teeth — no metric for what "doubt" means. |
| Extensibility | 6 | Module parsing is hard-coded to module.md sections. Adding a new encounter type requires code change, not data change. |
| Operational clarity | 8 | Three run modes are documented. Terminal output example is concrete. No stated LLM timeout policy. |

**Total: 63/80**

## The checkpoint as object

The checkpoint is a masterwork of *clarity* — it contains everything the LLM needs to narrate the next beat, no more, no less. But it doesn't feel like an object. It feels like a shipping container.

In *Deep Carbon Observatory*, the Seven-Coin is treasure with history. It's described in a way that makes you understand it was *wanted*, that someone carried it and died. The spec should treat checkpoint.json the same way. Right now it's a data structure that happens to contain LLM context. What if the checkpoint itself *felt* like what was happening? The emitter.py doesn't just write JSON — it writes a transition that has voice.

The classifier's boundary rule — "when in doubt, route to LLM. False-LLM-required is cheap. False-Python-resolved corrupts voice" — is the closest the spec gets to moral weight. It says: if you're unsure, err toward keeping the LLM in the loop, because Python making a narrative choice it's not sure about is worse than Python asking for help. That's a *value*, and it's right. But the spec states this as a postscript to a list. It should be the opening sentence of the classifier section. It should be the foundation that everything else rests on.

## What works

- The re-entrancy contract is unambiguous. Zero state loss.
- Seed-locked dice with position tracking. Not just reproducible — *auditable*.
- The three-layer state model has the right shape. Party state changes fast; session state is historical; campaign facts are read-only.
- Classification of what Python owns vs. what LLM owns is honest.
- Listing the 8 LLM-required events is *better* than saying "narrative stuff." Specific is honest.
- The "out of scope" section acknowledges what's not being built.

## What fails

- The spec describes *what* the system does but not *why it matters*. No narrative about what this engine believes play should feel like.
- Classifier decision rules are enumerated as prose. They should be code or felt as consequence.
- No failure recovery policy. What happens if checkpoint.json is corrupted? If dice_log.jsonl is truncated? The spec documents normal paths; it doesn't document the grief.
- PC heuristics are encoded as Python lambdas — the spec shows them as examples, not specifying the language they're written in or the failure mode when a lambda crashes.
- The log writer is specified as producing "the exact format established by S01-S04" but that format is not inlined or referenced.
- No stated policy for LLM availability. What if stdin never receives a response?

## Recommendations

1. **Open with the moral center.** Before listing what Python does, say: "The classifier believes that false-Python-resolved beats corrupt voice more than false-LLM-required beats waste time. When unsure, route to the LLM." Make that the aperture.
2. **Give the checkpoint a voice.** The `context` field in the outbound packet should be enough that the LLM can narrate without reading the module. Currently it almost works; make it fully work.
3. **Specify classifier rules in code or consequence, not prose.** Either show pseudocode for `classify()`, or describe each rule as a consequence: "If the event involves a PC's personal faith choice, route to LLM, because Python cannot weigh Aelric's oath against party survival without false certainty."
4. **Drill failure modes.** Add a "Recovery and Failure" section: what happens if checkpoint.json is missing on resume? If a PC sheet has no heuristics section? If the LLM response doesn't include required fields?
5. **Inline or reference the log format.** Show the exact template.
6. **State the LLM contract timeout.** How long does Python wait? Can the user resume from a checkpoint where the LLM response was never received?

## Final line

*marathon-runner* is an honest tool that knows its job. Give it a moral center, drill its failures, and let the checkpoint feel like a moment of transition rather than a data packet, and you'll have something that whispers its values to the DM every time they run it.
