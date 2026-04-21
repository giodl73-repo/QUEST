import subprocess, sys, json, os
from pathlib import Path

CWD = Path(__file__).parent.parent
CLI = [sys.executable, str(CWD / "scripts/marathon.py")]
BASE_ENV = {**os.environ, "PYTHONUTF8": "1"}


def run(*args, stdin_text=None, state_dir=None):
    env = {**BASE_ENV}
    if state_dir:
        env["MARATHON_STATE_DIR"] = str(state_dir)
    return subprocess.run(
        CLI + list(args),
        capture_output=True, text=True, cwd=CWD,
        input=stdin_text,
        env=env,
    )


def test_full_start_and_status_cycle(tmp_path):
    """start writes state; status reads and prints it."""
    import shutil
    (tmp_path / "adventures" / "test-adventure").mkdir(parents=True)
    (tmp_path / "personas" / "parties" / "test-party").mkdir(parents=True)
    shutil.copy(
        CWD / "tests/fixtures/mini_module.md",
        tmp_path / "adventures/test-adventure/module.md",
    )
    shutil.copy(
        CWD / "tests/fixtures/mini_pc.md",
        tmp_path / "personas/parties/test-party/test-fighter.md",
    )

    # Need to run from tmp_path so module paths resolve
    r_start = subprocess.run(
        CLI + ["start", "--adventure", "test-adventure",
               "--session", "S01", "--party", "test-party"],
        capture_output=True, text=True, cwd=tmp_path,
        env={**BASE_ENV, "MARATHON_STATE_DIR": str(tmp_path / "state")},
    )
    assert r_start.returncode == 0, r_start.stderr

    r_status = run("status", state_dir=tmp_path / "state")
    assert r_status.returncode == 0
    assert "S01" in r_status.stdout
    assert "test-fighter" in r_status.stdout
    assert "No active session" not in r_status.stdout


def test_set_route_after_start(tmp_path):
    """set-route D updates route in session state."""
    import sys, shutil
    sys.path.insert(0, str(CWD))
    from scripts.engine.state import StateManager, PartyState, SessionState, CampaignFacts

    state_dir = tmp_path / "state"
    sm = StateManager(state_dir=state_dir)
    sm.write_session(
        party=PartyState.from_dict({
            "thessaly": {"hp": 32, "hp_max": 32, "spell_slots": {},
                         "attunements": [], "lay_on_hands": 0,
                         "concentration": None, "conditions": []}
        }),
        session=SessionState.from_dict({
            "adventure": "test-adventure", "session": "S01",
            "dice_seed": "S01-test", "scene_index": 0,
            "scenes_completed": [], "pending_checkpoint": None,
            "party_slug": "compact-wardens",
        }),
        campaign=CampaignFacts.from_dict({"hints": {}, "campaign_permanent": []}),
    )

    r = run("set-route", "D", state_dir=state_dir)
    assert r.returncode == 0
    assert "Route set to: D" in r.stdout

    loaded = sm.read_session()
    assert loaded["session"].route == "D"


def test_resume_with_events_logs_to_jsonl(tmp_path):
    """resume with events in state_updates writes to event_log.jsonl."""
    import sys
    sys.path.insert(0, str(CWD))
    from scripts.engine.state import StateManager, PartyState, SessionState, CampaignFacts
    from scripts.engine.event_log import EventLogger

    state_dir = tmp_path / "state"
    sm = StateManager(state_dir=state_dir)
    sm.write_session(
        party=PartyState.from_dict({
            "thessaly": {"hp": 32, "hp_max": 32, "spell_slots": {},
                         "attunements": [], "lay_on_hands": 0,
                         "concentration": None, "conditions": []}
        }),
        session=SessionState.from_dict({
            "adventure": "test-adventure", "session": "S01",
            "dice_seed": "S01-test", "scene_index": 1,
            "scenes_completed": [0], "pending_checkpoint": "scene_1_beat_0",
            "party_slug": "compact-wardens",
        }),
        campaign=CampaignFacts.from_dict({"hints": {}, "campaign_permanent": []}),
    )
    sm.write_checkpoint({
        "session": "S01", "scene_id": 1, "scene_name": "The Tower",
        "beat_type": "scene_narration", "state_snapshot": {}, "dice_results": [],
        "resolved_mechanics": {}, "decision_point": {"description": "Narrate"},
        "context": {}, "scene_narrative_so_far": [],
    })

    valid_response = json.dumps({
        "narrative": "Lenne casts Shield to protect herself.",
        "state_updates": {
            "events": [
                {"type": "spell_cast", "pc": "lenne", "spell": "Shield",
                 "level": 1, "scene": 1, "context": "combat"},
                {"type": "reaction", "pc": "lenne", "reaction": "shield",
                 "trigger": "incoming_attack", "scene": 1},
            ]
        },
        "advance_to_scene": 2,
    })

    r = run("resume", stdin_text=valid_response + "\n", state_dir=state_dir)
    assert r.returncode == 0, r.stderr + r.stdout
    assert "Events logged: 2" in r.stdout

    el = EventLogger(state_dir / "event_log.jsonl")
    spells = el.spells_table()
    assert len(spells) == 1
    assert spells[0]["spell"] == "Shield"
    assert len(el.load()) == 2


def test_resume_with_valid_response(tmp_path):
    """resume accepts a valid JSON response and clears the checkpoint."""
    import sys
    sys.path.insert(0, str(CWD))
    from scripts.engine.state import StateManager, PartyState, SessionState, CampaignFacts

    state_dir = tmp_path / "state"
    sm = StateManager(state_dir=state_dir)
    sm.write_session(
        party=PartyState.from_dict({
            "test-fighter": {"hp": 28, "hp_max": 28, "spell_slots": {},
                              "attunements": [], "lay_on_hands": 0,
                              "concentration": None, "conditions": []}
        }),
        session=SessionState.from_dict({
            "adventure": "test-adventure", "session": "S01",
            "dice_seed": "S01-test", "scene_index": 1,
            "scenes_completed": [0], "pending_checkpoint": "scene_1_read_aloud",
        }),
        campaign=CampaignFacts.from_dict({"hints": {}, "campaign_permanent": []}),
    )
    sm.write_checkpoint({
        "session": "S01", "scene_id": 1, "scene_name": "The Vault",
        "beat_type": "read_aloud", "state_snapshot": {}, "dice_results": [],
        "resolved_mechanics": {}, "decision_point": {"description": "Narrate scene 1"},
        "context": {}, "scene_narrative_so_far": [],
    })

    valid_response = json.dumps({
        "narrative": "The vault door stands, ancient and sealed.",
        "state_updates": {},
        "advance_to_scene": 2,
    })

    r = run("resume", stdin_text=valid_response + "\n", state_dir=state_dir)
    assert r.returncode == 0, r.stderr + r.stdout
    assert "validated" in r.stdout.lower()
    assert not (state_dir / "checkpoint.json").exists()
