#!/usr/bin/env python3
"""marathon.py — CLI entry point for the Marathon D&D session engine."""
from __future__ import annotations
import argparse
import json
import os
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from scripts.engine.state import StateManager, PartyState, SessionState, CampaignFacts
from scripts.engine.loader import load_adventure, load_party, LoadError


def _state_dir() -> Path:
    """Allow overriding state dir via env var (useful in tests)."""
    return Path(os.environ.get("MARATHON_STATE_DIR", "state"))


def cmd_status(args) -> int:
    sm = StateManager(state_dir=_state_dir())
    loaded = sm.read_session()
    if loaded is None:
        print("No active session. Start one with:")
        print("  python marathon.py start --adventure <slug> --session <name>")
        return 0

    session = loaded["session"]
    party = loaded["party"]
    checkpoint = sm.read_checkpoint()

    sep = "=" * 50
    print(sep)
    print(f"SESSION: {session.session} | ADVENTURE: {session.adventure}")
    print(f"SCENE: {session.scene_index} | COMPLETED: {session.scenes_completed}")
    print()
    print("PARTY STATE:")
    for slug in party.slugs():
        pc = party[slug]
        slots = " ".join(f"{k}:{v}" for k, v in pc.spell_slots.items()) or "-"
        attune = ", ".join(pc.attunements) or "-"
        conds = ", ".join(pc.conditions) or "-"
        print(f"  {slug:<28} HP {pc.hp}/{pc.hp_max}  Slots {slots}  "
              f"Attune: {attune}  Conds: {conds}")
    print()
    if checkpoint:
        beat = checkpoint.get("beat_type", "unknown")
        scene = checkpoint.get("scene_id", "?")
        print(f"PENDING CHECKPOINT: scene_{scene}_{beat}")
        print("  (resume with: python marathon.py resume)")
    else:
        print("PENDING CHECKPOINT: none")
    print(sep)
    return 0


def cmd_start(args) -> int:
    adventure_slug = args.adventure
    session_name = args.session
    party_slug = getattr(args, "party", "varduin-muster")

    module_path = Path(f"adventures/{adventure_slug}/module.md")
    party_dir = Path(f"personas/parties/{party_slug}")

    try:
        adventure = load_adventure(module_path)
        pcs = load_party(party_dir)
    except LoadError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1

    print(f"Loaded adventure: {adventure_slug} ({len(adventure.scenes)} scenes)")
    print(f"Loaded party: {party_slug} ({len(pcs)} PCs)")

    party_dict = {
        pc.slug: {
            "hp": pc.hp, "hp_max": pc.hp_max,
            "spell_slots": pc.spell_slots,
            "attunements": pc.attunements,
            "lay_on_hands": 0,
            "concentration": None,
            "conditions": [],
        }
        for pc in pcs
    }
    import datetime
    session_dict = {
        "adventure": adventure_slug,
        "session": session_name,
        "dice_seed": f"{session_name}-{datetime.date.today().strftime('%Y%m%d')}",
        "scene_index": 0,
        "scenes_completed": [],
        "pending_checkpoint": None,
    }
    campaign_dict = {"hints": {}, "campaign_permanent": []}

    sm = StateManager(state_dir=_state_dir())
    sm.write_session(
        party=PartyState.from_dict(party_dict),
        session=SessionState.from_dict(session_dict),
        campaign=CampaignFacts.from_dict(campaign_dict),
    )
    print(f"State written to {_state_dir()}/session.json")
    return 0


def cmd_resume(args) -> int:
    sm = StateManager(state_dir=_state_dir())
    checkpoint = sm.read_checkpoint()

    if checkpoint is None:
        print("No checkpoint found. Use 'start' to begin a new session.")
        return 1

    session_id = checkpoint.get("session", "?")
    beat_type = checkpoint.get("beat_type", "?")
    scene_id = checkpoint.get("scene_id", "?")
    scene_name = checkpoint.get("scene_name", "?")

    sep = "=" * 50
    print(sep)
    print(f"RESUMING: {session_id} | SCENE {scene_id} - {scene_name}")
    print(f"BEAT: {beat_type}")
    print()

    dp = checkpoint.get("decision_point", {})
    ctx = checkpoint.get("context", {})
    if dp.get("description"):
        print(f"PROMPT: {dp['description']}")
    if ctx.get("read_aloud"):
        print(f"READ-ALOUD: {ctx['read_aloud']}")
    print()

    for dr in checkpoint.get("dice_results", []):
        label = dr.get("label", dr.get("expr", "roll"))
        print(f"  DICE: {label} → {dr.get('total')}")
    print(sep)
    print()
    print(">>> WAITING FOR LLM RESPONSE (paste JSON below, then press Ctrl+D / Ctrl+Z):")
    print()

    lines = []
    try:
        for line in sys.stdin:
            lines.append(line)
    except KeyboardInterrupt:
        print("\nInterrupted. Checkpoint preserved.")
        return 1

    raw_text = "".join(lines).strip()
    if not raw_text:
        print("No input received. Checkpoint preserved.")
        return 1

    try:
        raw = json.loads(raw_text)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON response — {e}")
        print("Checkpoint preserved. Run 'resume' again to retry.")
        return 1

    from scripts.engine.emitter import Emitter, ValidationError
    loaded = sm.read_session()
    party_slugs = list(loaded["party"].slugs()) if loaded else []
    emitter = Emitter(state_dir=_state_dir(), party_slugs=party_slugs)

    current_scene = loaded["session"].scene_index if loaded else 0
    try:
        packet = emitter.validate_inbound(raw, current_scene_index=current_scene)
    except ValidationError as e:
        print(f"ERROR: {e}")
        print("Checkpoint preserved. Run 'resume' again with a corrected response.")
        return 1

    print(f"Response validated. Advancing to scene {packet.advance_to_scene}.")

    if loaded:
        session = loaded["session"]
        party = loaded["party"]
        campaign = loaded["campaign"]

        for key, updates in packet.state_updates.items():
            if key == "hints":
                for hint_key, hint_val in updates.items():
                    campaign.hints[hint_key] = hint_val
            elif key in party.slugs():
                pc = party[key]
                for field, val in updates.items():
                    if hasattr(pc, field):
                        setattr(pc, field, val)

        session.scene_index = packet.advance_to_scene
        sm.write_session(party=party, session=session, campaign=campaign)

    sm.delete_checkpoint()
    print("Checkpoint cleared. Session state updated.")
    if packet.notes_for_log:
        print(f"Note for log: {packet.notes_for_log}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(prog="marathon.py", description="Marathon D&D session engine")
    sub = parser.add_subparsers(dest="command")

    p_start = sub.add_parser("start", help="Begin a new session")
    p_start.add_argument("--adventure", required=True)
    p_start.add_argument("--session", required=True)
    p_start.add_argument("--party", default="varduin-muster")

    sub.add_parser("resume", help="Re-enter from last checkpoint")
    sub.add_parser("status", help="Print current state snapshot")

    args = parser.parse_args()
    if args.command is None:
        parser.print_usage(sys.stderr)
        return 2

    return {"start": cmd_start, "resume": cmd_resume, "status": cmd_status}[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
