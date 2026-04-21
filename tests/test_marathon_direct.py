"""Direct (non-subprocess) tests for marathon.py CLI functions.

Imports and calls cmd_* functions in-process so pytest-cov can trace them.
Each test sets MARATHON_STATE_DIR via monkeypatch so functions write to tmp_path.
"""
import argparse
import json
import os
import shutil
import sys
from pathlib import Path

import pytest

CWD = Path(__file__).parent.parent
sys.path.insert(0, str(CWD))

FIXTURES = CWD / "tests" / "fixtures"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _load_marathon():
    """Import (or reload) marathon so _state_dir() picks up env changes."""
    import importlib
    import scripts.marathon as m
    importlib.reload(m)
    return m


def _write_minimal_session(state_dir: Path, session: str = "S01",
                            adventure: str = "test-adventure",
                            party_slug: str = "test-party"):
    from scripts.engine.state import StateManager, PartyState, SessionState, CampaignFacts
    sm = StateManager(state_dir=state_dir)
    sm.write_session(
        party=PartyState.from_dict({
            "test-fighter": {"hp": 28, "hp_max": 28, "spell_slots": {},
                             "attunements": [], "lay_on_hands": 0,
                             "concentration": None, "conditions": []}
        }),
        session=SessionState.from_dict({
            "adventure": adventure, "session": session,
            "dice_seed": f"{session}-test", "scene_index": 0,
            "scenes_completed": [], "pending_checkpoint": None,
            "party_slug": party_slug,
        }),
        campaign=CampaignFacts.from_dict({"hints": {}, "campaign_permanent": []}),
    )
    return sm


# ---------------------------------------------------------------------------
# cmd_status
# ---------------------------------------------------------------------------

def test_cmd_status_no_session_returns_0(tmp_path, monkeypatch, capsys):
    monkeypatch.setenv("MARATHON_STATE_DIR", str(tmp_path))
    m = _load_marathon()
    result = m.cmd_status(None)
    assert result == 0
    out = capsys.readouterr().out
    assert "No active session" in out


def test_cmd_status_with_session_shows_party(tmp_path, monkeypatch, capsys):
    monkeypatch.setenv("MARATHON_STATE_DIR", str(tmp_path))
    _write_minimal_session(tmp_path)
    m = _load_marathon()
    result = m.cmd_status(None)
    assert result == 0
    out = capsys.readouterr().out
    assert "test-fighter" in out
    assert "S01" in out


def test_cmd_status_shows_dice_log_count(tmp_path, monkeypatch, capsys):
    monkeypatch.setenv("MARATHON_STATE_DIR", str(tmp_path))
    _write_minimal_session(tmp_path)
    dice_log = tmp_path / "dice_log.jsonl"
    dice_log.write_text('{"roll": 1}\n{"roll": 2}\n', encoding="utf-8")
    m = _load_marathon()
    m.cmd_status(None)
    out = capsys.readouterr().out
    assert "2 rolls" in out


def test_cmd_status_shows_event_log_summary(tmp_path, monkeypatch, capsys):
    monkeypatch.setenv("MARATHON_STATE_DIR", str(tmp_path))
    _write_minimal_session(tmp_path)
    from scripts.engine.event_log import EventLogger
    el = EventLogger(tmp_path / "event_log.jsonl")
    el.log({"type": "spell_cast", "pc": "t", "spell": "Shield", "level": 1, "scene": 0})
    m = _load_marathon()
    m.cmd_status(None)
    out = capsys.readouterr().out
    assert "spell_cast" in out


def test_cmd_status_no_events_shows_message(tmp_path, monkeypatch, capsys):
    monkeypatch.setenv("MARATHON_STATE_DIR", str(tmp_path))
    _write_minimal_session(tmp_path)
    m = _load_marathon()
    m.cmd_status(None)
    out = capsys.readouterr().out
    assert "no events recorded" in out.lower()


def test_cmd_status_with_checkpoint(tmp_path, monkeypatch, capsys):
    monkeypatch.setenv("MARATHON_STATE_DIR", str(tmp_path))
    sm = _write_minimal_session(tmp_path)
    sm.write_checkpoint({"session": "S01", "scene_id": 0, "beat_type": "read_aloud",
                          "scene_name": "Test", "state_snapshot": {}, "dice_results": [],
                          "resolved_mechanics": {}, "decision_point": {},
                          "context": {}, "scene_narrative_so_far": []})
    m = _load_marathon()
    m.cmd_status(None)
    out = capsys.readouterr().out
    assert "read_aloud" in out


# ---------------------------------------------------------------------------
# cmd_start
# ---------------------------------------------------------------------------

def test_cmd_start_writes_session_json(tmp_path, monkeypatch):
    monkeypatch.setenv("MARATHON_STATE_DIR", str(tmp_path / "state"))
    # Set up fixtures in a structure marathon.py expects
    adv_dir = tmp_path / "adventures" / "test-adventure"
    adv_dir.mkdir(parents=True)
    shutil.copy(FIXTURES / "mini_module.md", adv_dir / "module.md")
    party_dir = tmp_path / "personas" / "parties" / "test-party"
    party_dir.mkdir(parents=True)
    shutil.copy(FIXTURES / "mini_pc.md", party_dir / "test-fighter.md")

    # Change cwd so adventure/party paths resolve
    orig_cwd = os.getcwd()
    os.chdir(tmp_path)
    try:
        m = _load_marathon()
        args = argparse.Namespace(adventure="test-adventure", session="S01",
                                  party="test-party")
        result = m.cmd_start(args)
    finally:
        os.chdir(orig_cwd)

    assert result == 0
    assert (tmp_path / "state" / "session.json").exists()


def test_cmd_start_clears_event_log(tmp_path, monkeypatch):
    monkeypatch.setenv("MARATHON_STATE_DIR", str(tmp_path / "state"))
    adv_dir = tmp_path / "adventures" / "test-adventure"
    adv_dir.mkdir(parents=True)
    shutil.copy(FIXTURES / "mini_module.md", adv_dir / "module.md")
    party_dir = tmp_path / "personas" / "parties" / "test-party"
    party_dir.mkdir(parents=True)
    shutil.copy(FIXTURES / "mini_pc.md", party_dir / "test-fighter.md")

    # Write a stale event log
    state_dir = tmp_path / "state"
    state_dir.mkdir()
    (state_dir / "event_log.jsonl").write_text('{"type":"spell_cast"}\n', encoding="utf-8")

    orig_cwd = os.getcwd()
    os.chdir(tmp_path)
    try:
        m = _load_marathon()
        result = m.cmd_start(argparse.Namespace(
            adventure="test-adventure", session="S02", party="test-party"))
    finally:
        os.chdir(orig_cwd)

    assert result == 0
    assert not (state_dir / "event_log.jsonl").exists()


def test_cmd_start_missing_module_returns_1(tmp_path, monkeypatch):
    monkeypatch.setenv("MARATHON_STATE_DIR", str(tmp_path / "state"))
    orig_cwd = os.getcwd()
    os.chdir(tmp_path)
    try:
        m = _load_marathon()
        args = argparse.Namespace(adventure="nonexistent-adventure",
                                  session="S01", party="test-party")
        result = m.cmd_start(args)
    finally:
        os.chdir(orig_cwd)
    assert result == 1


# ---------------------------------------------------------------------------
# cmd_set_route
# ---------------------------------------------------------------------------

def test_cmd_set_route_sets_d(tmp_path, monkeypatch, capsys):
    monkeypatch.setenv("MARATHON_STATE_DIR", str(tmp_path))
    _write_minimal_session(tmp_path)
    m = _load_marathon()
    result = m.cmd_set_route(argparse.Namespace(route="D"))
    assert result == 0
    out = capsys.readouterr().out
    assert "Route set to: D" in out

    from scripts.engine.state import StateManager
    sm = StateManager(state_dir=tmp_path)
    loaded = sm.read_session()
    assert loaded["session"].route == "D"


def test_cmd_set_route_accepts_lowercase(tmp_path, monkeypatch, capsys):
    monkeypatch.setenv("MARATHON_STATE_DIR", str(tmp_path))
    _write_minimal_session(tmp_path)
    m = _load_marathon()
    result = m.cmd_set_route(argparse.Namespace(route="a"))
    assert result == 0
    out = capsys.readouterr().out
    assert "Route set to: A" in out


def test_cmd_set_route_invalid_returns_1(tmp_path, monkeypatch, capsys):
    monkeypatch.setenv("MARATHON_STATE_DIR", str(tmp_path))
    _write_minimal_session(tmp_path)
    m = _load_marathon()
    result = m.cmd_set_route(argparse.Namespace(route="Z"))
    assert result == 1


def test_cmd_set_route_no_session_returns_1(tmp_path, monkeypatch, capsys):
    monkeypatch.setenv("MARATHON_STATE_DIR", str(tmp_path))
    m = _load_marathon()
    result = m.cmd_set_route(argparse.Namespace(route="D"))
    assert result == 1


# ---------------------------------------------------------------------------
# cmd_resume
# ---------------------------------------------------------------------------

def test_cmd_resume_stale_checkpoint_y_deletes(tmp_path, monkeypatch, capsys):
    """Lines 152-158: stale checkpoint from different session; user says y."""
    monkeypatch.setenv("MARATHON_STATE_DIR", str(tmp_path))
    _write_minimal_session(tmp_path, session="S01")
    from scripts.engine.state import StateManager
    StateManager(state_dir=tmp_path).write_checkpoint({
        "session": "S99",  # different session!
        "scene_id": 0, "scene_name": "T", "beat_type": "read_aloud",
        "state_snapshot": {}, "dice_results": [], "resolved_mechanics": {},
        "decision_point": {}, "context": {}, "scene_narrative_so_far": [],
    })
    monkeypatch.setattr("builtins.input", lambda _: "y")
    m = _load_marathon()
    result = m.cmd_resume(None)
    assert result == 0
    out = capsys.readouterr().out
    assert "Stale checkpoint deleted" in out


def test_cmd_resume_stale_checkpoint_n_keeps(tmp_path, monkeypatch, capsys):
    """Lines 159-161: stale checkpoint; user says n — keeps it and exits 1."""
    monkeypatch.setenv("MARATHON_STATE_DIR", str(tmp_path))
    _write_minimal_session(tmp_path, session="S01")
    from scripts.engine.state import StateManager
    StateManager(state_dir=tmp_path).write_checkpoint({
        "session": "S99",
        "scene_id": 0, "scene_name": "T", "beat_type": "read_aloud",
        "state_snapshot": {}, "dice_results": [], "resolved_mechanics": {},
        "decision_point": {}, "context": {}, "scene_narrative_so_far": [],
    })
    monkeypatch.setattr("builtins.input", lambda _: "n")
    m = _load_marathon()
    result = m.cmd_resume(None)
    assert result == 1
    out = capsys.readouterr().out
    assert "Keeping stale checkpoint" in out


def test_cmd_resume_no_checkpoint_returns_1(tmp_path, monkeypatch, capsys):
    monkeypatch.setenv("MARATHON_STATE_DIR", str(tmp_path))
    _write_minimal_session(tmp_path)
    m = _load_marathon()
    result = m.cmd_resume(None)
    assert result == 1
    out = capsys.readouterr().out
    assert "No checkpoint found" in out


def test_cmd_resume_with_events_writes_event_log(tmp_path, monkeypatch, capsys):
    monkeypatch.setenv("MARATHON_STATE_DIR", str(tmp_path))
    from scripts.engine.state import StateManager
    sm = _write_minimal_session(tmp_path)
    sm.write_checkpoint({
        "session": "S01", "scene_id": 0, "scene_name": "Test",
        "beat_type": "scene_narration", "state_snapshot": {},
        "dice_results": [], "resolved_mechanics": {},
        "decision_point": {"description": "narrate"},
        "context": {}, "scene_narrative_so_far": [],
    })

    # Simulate stdin with a valid JSON response including events
    response = json.dumps({
        "narrative": "The wizard casts a spell.",
        "state_updates": {
            "events": [
                {"type": "spell_cast", "pc": "lenne", "spell": "Fireball",
                 "level": 3, "scene": 0, "context": "combat"}
            ]
        },
        "advance_to_scene": 1,
    })

    import io
    orig_stdin = sys.stdin
    sys.stdin = io.StringIO(response + "\n")
    try:
        m = _load_marathon()
        result = m.cmd_resume(None)
    finally:
        sys.stdin = orig_stdin

    assert result == 0
    from scripts.engine.event_log import EventLogger
    el = EventLogger(tmp_path / "event_log.jsonl")
    spells = el.spells_table()
    assert len(spells) == 1
    assert spells[0]["spell"] == "Fireball"


def test_cmd_resume_with_route_update(tmp_path, monkeypatch, capsys):
    monkeypatch.setenv("MARATHON_STATE_DIR", str(tmp_path))
    sm = _write_minimal_session(tmp_path)
    sm.write_checkpoint({
        "session": "S01", "scene_id": 0, "scene_name": "Test",
        "beat_type": "scene_narration", "state_snapshot": {},
        "dice_results": [], "resolved_mechanics": {},
        "decision_point": {}, "context": {}, "scene_narrative_so_far": [],
    })

    response = json.dumps({
        "narrative": "The session outcome is determined.",
        "state_updates": {"route": "D"},
        "advance_to_scene": 1,
    })

    import io
    orig_stdin = sys.stdin
    sys.stdin = io.StringIO(response + "\n")
    try:
        m = _load_marathon()
        m.cmd_resume(None)
    finally:
        sys.stdin = orig_stdin

    from scripts.engine.state import StateManager
    loaded = StateManager(state_dir=tmp_path).read_session()
    assert loaded["session"].route == "D"


def test_cmd_resume_invalid_json_returns_1(tmp_path, monkeypatch, capsys):
    monkeypatch.setenv("MARATHON_STATE_DIR", str(tmp_path))
    sm = _write_minimal_session(tmp_path)
    sm.write_checkpoint({"session": "S01", "scene_id": 0, "scene_name": "T",
                          "beat_type": "read_aloud", "state_snapshot": {},
                          "dice_results": [], "resolved_mechanics": {},
                          "decision_point": {}, "context": {},
                          "scene_narrative_so_far": []})

    import io
    orig_stdin = sys.stdin
    sys.stdin = io.StringIO("NOT VALID JSON\n")
    try:
        m = _load_marathon()
        result = m.cmd_resume(None)
    finally:
        sys.stdin = orig_stdin

    assert result == 1
    capsys.readouterr()  # drain


def test_cmd_resume_empty_input_returns_1(tmp_path, monkeypatch, capsys):
    monkeypatch.setenv("MARATHON_STATE_DIR", str(tmp_path))
    sm = _write_minimal_session(tmp_path)
    sm.write_checkpoint({"session": "S01", "scene_id": 0, "scene_name": "T",
                          "beat_type": "read_aloud", "state_snapshot": {},
                          "dice_results": [], "resolved_mechanics": {},
                          "decision_point": {}, "context": {},
                          "scene_narrative_so_far": []})

    import io
    orig_stdin = sys.stdin
    sys.stdin = io.StringIO("")
    try:
        m = _load_marathon()
        result = m.cmd_resume(None)
    finally:
        sys.stdin = orig_stdin

    assert result == 1
    capsys.readouterr()


def test_cmd_resume_shows_read_aloud_and_dice(tmp_path, monkeypatch, capsys):
    """Lines 179, 183-184: read_aloud and dice_results displayed."""
    monkeypatch.setenv("MARATHON_STATE_DIR", str(tmp_path))
    sm = _write_minimal_session(tmp_path)
    sm.write_checkpoint({
        "session": "S01", "scene_id": 0, "scene_name": "Test",
        "beat_type": "read_aloud", "state_snapshot": {},
        "dice_results": [{"label": "initiative", "total": 17}],
        "resolved_mechanics": {},
        "decision_point": {"description": "Narrate the scene."},
        "context": {"read_aloud": "The door opens before you."},
        "scene_narrative_so_far": [],
    })
    # Use empty stdin to trigger "No input received" early exit after displaying checkpoint
    import io
    orig_stdin = sys.stdin
    sys.stdin = io.StringIO("")
    try:
        m = _load_marathon()
        m.cmd_resume(None)
    finally:
        sys.stdin = orig_stdin
    out = capsys.readouterr().out
    assert "READ-ALOUD" in out
    assert "DICE" in out
    assert "initiative" in out


def test_cmd_resume_hints_update(tmp_path, monkeypatch, capsys):
    """Lines 230-231: hints key in state_updates updates campaign hints."""
    monkeypatch.setenv("MARATHON_STATE_DIR", str(tmp_path))
    sm = _write_minimal_session(tmp_path)
    sm.write_checkpoint({
        "session": "S01", "scene_id": 0, "scene_name": "T",
        "beat_type": "scene_narration", "state_snapshot": {}, "dice_results": [],
        "resolved_mechanics": {}, "decision_point": {}, "context": {},
        "scene_narrative_so_far": [],
    })

    response = json.dumps({
        "narrative": "The hint fires.",
        "state_updates": {"hints": {"hint_1": "delivered"}},
        "advance_to_scene": 1,
    })
    import io
    orig_stdin = sys.stdin
    sys.stdin = io.StringIO(response + "\n")
    try:
        m = _load_marathon()
        m.cmd_resume(None)
    finally:
        sys.stdin = orig_stdin

    from scripts.engine.state import StateManager
    loaded = StateManager(state_dir=tmp_path).read_session()
    assert loaded["campaign"].hints["hint_1"] == "delivered"
    capsys.readouterr()


def test_cmd_resume_invalid_route_warns(tmp_path, monkeypatch, capsys):
    """Line 237: invalid route value prints warning."""
    monkeypatch.setenv("MARATHON_STATE_DIR", str(tmp_path))
    sm = _write_minimal_session(tmp_path)
    sm.write_checkpoint({
        "session": "S01", "scene_id": 0, "scene_name": "T",
        "beat_type": "scene_narration", "state_snapshot": {}, "dice_results": [],
        "resolved_mechanics": {}, "decision_point": {}, "context": {},
        "scene_narrative_so_far": [],
    })

    response = json.dumps({
        "narrative": "Done.",
        "state_updates": {"route": "INVALID"},
        "advance_to_scene": 1,
    })
    import io
    orig_stdin = sys.stdin
    sys.stdin = io.StringIO(response + "\n")
    try:
        m = _load_marathon()
        m.cmd_resume(None)
    finally:
        sys.stdin = orig_stdin
    out = capsys.readouterr().out
    assert "WARNING" in out


def test_cmd_resume_external_rolls_is_noop(tmp_path, monkeypatch, capsys):
    """Line 239: external_rolls key is accepted without crashing."""
    monkeypatch.setenv("MARATHON_STATE_DIR", str(tmp_path))
    sm = _write_minimal_session(tmp_path)
    sm.write_checkpoint({
        "session": "S01", "scene_id": 0, "scene_name": "T",
        "beat_type": "scene_narration", "state_snapshot": {}, "dice_results": [],
        "resolved_mechanics": {}, "decision_point": {}, "context": {},
        "scene_narrative_so_far": [],
    })

    response = json.dumps({
        "narrative": "Done.",
        "state_updates": {"external_rolls": [{"roll": 15}]},
        "advance_to_scene": 1,
    })
    import io
    orig_stdin = sys.stdin
    sys.stdin = io.StringIO(response + "\n")
    try:
        m = _load_marathon()
        result = m.cmd_resume(None)
    finally:
        sys.stdin = orig_stdin
    assert result == 0
    capsys.readouterr()


def test_cmd_resume_pc_field_update_mutable(tmp_path, monkeypatch, capsys):
    """Lines 245-249: mutable PC field (hp) updated."""
    monkeypatch.setenv("MARATHON_STATE_DIR", str(tmp_path))
    sm = _write_minimal_session(tmp_path)
    sm.write_checkpoint({
        "session": "S01", "scene_id": 0, "scene_name": "T",
        "beat_type": "scene_narration", "state_snapshot": {}, "dice_results": [],
        "resolved_mechanics": {}, "decision_point": {}, "context": {},
        "scene_narrative_so_far": [],
    })

    response = json.dumps({
        "narrative": "Done.",
        "state_updates": {"test-fighter": {"hp": 15}},
        "advance_to_scene": 1,
    })
    import io
    orig_stdin = sys.stdin
    sys.stdin = io.StringIO(response + "\n")
    try:
        m = _load_marathon()
        m.cmd_resume(None)
    finally:
        sys.stdin = orig_stdin

    from scripts.engine.state import StateManager
    loaded = StateManager(state_dir=tmp_path).read_session()
    assert loaded["party"]["test-fighter"].hp == 15
    capsys.readouterr()


def test_cmd_resume_pc_field_update_non_mutable_warns(tmp_path, monkeypatch, capsys):
    """Lines 250-251: non-mutable field warns but doesn't crash."""
    monkeypatch.setenv("MARATHON_STATE_DIR", str(tmp_path))
    sm = _write_minimal_session(tmp_path)
    sm.write_checkpoint({
        "session": "S01", "scene_id": 0, "scene_name": "T",
        "beat_type": "scene_narration", "state_snapshot": {}, "dice_results": [],
        "resolved_mechanics": {}, "decision_point": {}, "context": {},
        "scene_narrative_so_far": [],
    })

    response = json.dumps({
        "narrative": "Done.",
        "state_updates": {"test-fighter": {"hp_max": 99}},
        "advance_to_scene": 1,
    })
    import io
    orig_stdin = sys.stdin
    sys.stdin = io.StringIO(response + "\n")
    try:
        m = _load_marathon()
        result = m.cmd_resume(None)
    finally:
        sys.stdin = orig_stdin
    out = capsys.readouterr().out
    assert "ignoring non-mutable" in out
    assert result == 0


def test_cmd_resume_notes_for_log_printed(tmp_path, monkeypatch, capsys):
    """Line 271: notes_for_log is printed when present."""
    monkeypatch.setenv("MARATHON_STATE_DIR", str(tmp_path))
    sm = _write_minimal_session(tmp_path)
    sm.write_checkpoint({
        "session": "S01", "scene_id": 0, "scene_name": "T",
        "beat_type": "scene_narration", "state_snapshot": {}, "dice_results": [],
        "resolved_mechanics": {}, "decision_point": {}, "context": {},
        "scene_narrative_so_far": [],
    })

    response = json.dumps({
        "narrative": "Done.",
        "state_updates": {},
        "advance_to_scene": 1,
        "notes_for_log": "Scene 01 complete.",
    })
    import io
    orig_stdin = sys.stdin
    sys.stdin = io.StringIO(response + "\n")
    try:
        m = _load_marathon()
        m.cmd_resume(None)
    finally:
        sys.stdin = orig_stdin
    out = capsys.readouterr().out
    assert "Scene 01 complete." in out


def test_cmd_resume_advances_beat_cursor(tmp_path, monkeypatch, capsys):
    """Lines 257-264: pending_checkpoint beat cursor is incremented."""
    monkeypatch.setenv("MARATHON_STATE_DIR", str(tmp_path))
    sm = _write_minimal_session(tmp_path)
    # Set pending_checkpoint to scene_0_beat_2
    from scripts.engine.state import StateManager
    state_mgr = StateManager(state_dir=tmp_path)
    loaded = state_mgr.read_session()
    loaded["session"].pending_checkpoint = "scene_0_beat_2"
    state_mgr.write_session(**loaded)

    sm.write_checkpoint({
        "session": "S01", "scene_id": 0, "scene_name": "T",
        "beat_type": "scene_narration", "state_snapshot": {}, "dice_results": [],
        "resolved_mechanics": {}, "decision_point": {}, "context": {},
        "scene_narrative_so_far": [],
    })

    response = json.dumps({"narrative": "Done.", "state_updates": {}, "advance_to_scene": 0})
    import io
    orig_stdin = sys.stdin
    sys.stdin = io.StringIO(response + "\n")
    try:
        m = _load_marathon()
        m.cmd_resume(None)
    finally:
        sys.stdin = orig_stdin

    final = StateManager(state_dir=tmp_path).read_session()
    assert final["session"].pending_checkpoint == "scene_0_beat_3"
    capsys.readouterr()


def test_main_no_args_returns_2(monkeypatch, capsys):
    """Lines 293-322: main() returns 2 when no subcommand given."""
    monkeypatch.setattr(sys, "argv", ["marathon.py"])
    m = _load_marathon()
    result = m.main()
    assert result == 2
    capsys.readouterr()


def test_main_status_dispatches(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["marathon.py", "status"])
    monkeypatch.setenv("MARATHON_STATE_DIR", str(tmp_path))
    m = _load_marathon()
    result = m.main()
    assert result == 0
    capsys.readouterr()


def test_cmd_resume_beat_cursor_bad_int_clears(tmp_path, monkeypatch, capsys):
    """Lines 263-264: ValueError in beat cursor int() sets checkpoint to None."""
    monkeypatch.setenv("MARATHON_STATE_DIR", str(tmp_path))
    from scripts.engine.state import StateManager
    sm = _write_minimal_session(tmp_path)
    state_mgr = StateManager(state_dir=tmp_path)
    loaded = state_mgr.read_session()
    loaded["session"].pending_checkpoint = "scene_0_beat_NOTANINT"
    state_mgr.write_session(**loaded)

    sm.write_checkpoint({
        "session": "S01", "scene_id": 0, "scene_name": "T",
        "beat_type": "scene_narration", "state_snapshot": {}, "dice_results": [],
        "resolved_mechanics": {}, "decision_point": {}, "context": {},
        "scene_narrative_so_far": [],
    })

    response = json.dumps({"narrative": "Done.", "state_updates": {}, "advance_to_scene": 0})
    import io
    orig_stdin = sys.stdin
    sys.stdin = io.StringIO(response + "\n")
    try:
        m = _load_marathon()
        result = m.cmd_resume(None)
    finally:
        sys.stdin = orig_stdin

    assert result == 0
    final = StateManager(state_dir=tmp_path).read_session()
    assert final["session"].pending_checkpoint is None
    capsys.readouterr()


def test_cmd_resume_keyboard_interrupt_returns_1(tmp_path, monkeypatch, capsys):
    """Lines 194-196: KeyboardInterrupt during stdin reading returns 1."""
    monkeypatch.setenv("MARATHON_STATE_DIR", str(tmp_path))
    sm = _write_minimal_session(tmp_path)
    sm.write_checkpoint({
        "session": "S01", "scene_id": 0, "scene_name": "T",
        "beat_type": "scene_narration", "state_snapshot": {}, "dice_results": [],
        "resolved_mechanics": {}, "decision_point": {}, "context": {},
        "scene_narrative_so_far": [],
    })

    class KeyboardInterruptStdin:
        def __iter__(self):
            raise KeyboardInterrupt

    import io
    orig_stdin = sys.stdin
    sys.stdin = KeyboardInterruptStdin()
    try:
        m = _load_marathon()
        result = m.cmd_resume(None)
    finally:
        sys.stdin = orig_stdin

    assert result == 1
    out = capsys.readouterr().out
    assert "Interrupted" in out


def test_cmd_resume_invalid_validation_returns_1(tmp_path, monkeypatch, capsys):
    monkeypatch.setenv("MARATHON_STATE_DIR", str(tmp_path))
    sm = _write_minimal_session(tmp_path)
    sm.write_checkpoint({"session": "S01", "scene_id": 0, "scene_name": "T",
                          "beat_type": "scene_narration", "state_snapshot": {},
                          "dice_results": [], "resolved_mechanics": {},
                          "decision_point": {}, "context": {},
                          "scene_narrative_so_far": []})

    # advance_to_scene goes backward — should fail validation
    response = json.dumps({
        "narrative": "Text",
        "state_updates": {},
        "advance_to_scene": -1,
    })

    import io
    orig_stdin = sys.stdin
    sys.stdin = io.StringIO(response + "\n")
    try:
        m = _load_marathon()
        result = m.cmd_resume(None)
    finally:
        sys.stdin = orig_stdin

    assert result == 1
    capsys.readouterr()
