#!/usr/bin/env python3
"""run_beats.py — advance the session until the next LLM-required checkpoint."""
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.engine.loader import load_adventure, load_party
from scripts.engine.state import StateManager
from scripts.engine.dice import DiceEngine
from scripts.engine.heuristics import Heuristics
from scripts.engine.emitter import Emitter
from scripts.engine.scene import SceneRunner

state_dir = Path("state")
sm = StateManager(state_dir=state_dir)
loaded = sm.read_session()

if loaded is None:
    print("No active session. Run: python marathon.py start ...")
    sys.exit(1)

party = loaded["party"]
session = loaded["session"]
campaign = loaded["campaign"]

adventure = load_adventure(Path(f"adventures/{session.adventure}/module.md"))
party_slug = getattr(session, "party_slug", "compact-wardens")
pcs = load_party(Path(f"personas/parties/{party_slug}"))

dice = DiceEngine(seed=session.dice_seed, log_path=state_dir / "dice_log.jsonl")
heuristics = Heuristics(pcs)

# Get party slugs from the loaded party
party_slugs = list(party.slugs())
emitter = Emitter(state_dir=state_dir, party_slugs=party_slugs)

# Determine SceneRunner constructor signature from actual code
import inspect
from scripts.engine.scene import SceneRunner
sig = inspect.signature(SceneRunner.__init__)
params = list(sig.parameters.keys())

# Build kwargs based on actual signature
kwargs = {}
for p in params[1:]:  # skip 'self'
    if p in ('adventure',):
        kwargs[p] = adventure
    elif p in ('state_manager', 'sm'):
        kwargs[p] = sm
    elif p in ('dice_engine', 'dice'):
        kwargs[p] = dice
    elif p in ('heuristics', 'h'):
        kwargs[p] = heuristics
    elif p in ('emitter', 'e'):
        kwargs[p] = emitter
    elif p in ('state_dir',):
        kwargs[p] = state_dir

runner = SceneRunner(**kwargs)

narrative_so_far = []
beats_run = 0

while True:
    result = runner.run_next_beat(party, session, campaign)
    beats_run += 1

    if result.status == "llm_required":
        sm.write_session(party=party, session=session, campaign=campaign)
        cp = sm.read_checkpoint()
        print(f"\n{'='*60}")
        print(f"CHECKPOINT: scene_{session.scene_index} | beat={result.beat_type}")
        if cp:
            ctx = cp.get("context", {})
            dp = cp.get("decision_point", {})
            if ctx.get("read_aloud"):
                print(f"\nREAD-ALOUD:\n{ctx['read_aloud']}")
            if dp.get("description"):
                print(f"\nPROMPT: {dp['description']}")
            dice_r = cp.get("dice_results", [])
            if dice_r:
                print(f"\nDICE ROLLED:")
                for dr in dice_r:
                    print(f"  {dr.get('label','?')} → {dr.get('total','?')}")
            narr = cp.get("scene_narrative_so_far", [])
            if narr:
                print(f"\nNARRATIVE SO FAR: {len(narr)} prior beats")
        print(f"{'='*60}")
        print("\nRESUME COMMAND:\n  python scripts/marathon.py resume")
        break

    elif result.status == "python_resolved":
        sm.write_session(party=party, session=session, campaign=campaign)
        dice_str = ""
        if result.dice_results:
            dice_str = " | dice: " + ", ".join(
                f"{r.expression}={r.total}" for r in result.dice_results
            )
        print(f"  [ok] Python beat: {result.beat_type}{dice_str}")

    elif result.status == "scene_complete":
        sm.write_session(party=party, session=session, campaign=campaign)
        print(f"  [ok] Scene {session.scene_index - 1} complete -> advancing to scene {session.scene_index}")

    elif result.status == "session_complete":
        sm.write_session(party=party, session=session, campaign=campaign)
        print(f"\n{'='*60}")
        print("SESSION COMPLETE")
        print(f"{'='*60}")
        break

    else:
        print(f"  ? Unknown status: {result.status}")
        break

print(f"\n[{beats_run} beats advanced]")
