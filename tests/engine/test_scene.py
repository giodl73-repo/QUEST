"""Tests for scripts/engine/scene.py — SceneRunner beat loop."""
from __future__ import annotations
import pytest
from pathlib import Path

FIXTURES = Path("tests/fixtures")


# ---------------------------------------------------------------------------
# Helpers / fixtures
# ---------------------------------------------------------------------------

def _make_party(slugs=("test-fighter",)):
    from scripts.engine.state import PartyState
    pcs = {
        slug: {
            "hp": 28, "hp_max": 28, "spell_slots": {},
            "attunements": [], "lay_on_hands": 0,
            "concentration": None, "conditions": [],
        }
        for slug in slugs
    }
    return PartyState.from_dict(pcs)


def _make_session(scene_index=0):
    from scripts.engine.state import SessionState
    return SessionState.from_dict({
        "adventure": "test-adventure",
        "session": "S01",
        "dice_seed": "S01-test",
        "scene_index": scene_index,
        "scenes_completed": [],
        "pending_checkpoint": None,
    })


def _make_campaign():
    from scripts.engine.state import CampaignFacts
    return CampaignFacts.from_dict({"hints": {}, "campaign_permanent": []})


def _make_runner(tmp_path, adventure=None):
    """Build a SceneRunner with default mini_module + test-fighter."""
    from scripts.engine.loader import load_adventure, load_party
    from scripts.engine.dice import DiceEngine
    from scripts.engine.heuristics import Heuristics
    from scripts.engine.emitter import Emitter
    from scripts.engine.scene import SceneRunner

    if adventure is None:
        adventure = load_adventure(FIXTURES / "mini_module.md")

    pcs = load_party(FIXTURES)
    dice = DiceEngine(seed="test-scene")
    heuristics = Heuristics(pcs)
    emitter = Emitter(state_dir=tmp_path, party_slugs=[pc.slug for pc in pcs])

    return SceneRunner(
        adventure=adventure,
        dice=dice,
        heuristics=heuristics,
        emitter=emitter,
        state_dir=tmp_path,
    )


# ---------------------------------------------------------------------------
# Test 1: SceneRunner can be constructed
# ---------------------------------------------------------------------------

def test_scene_runner_can_be_constructed(tmp_path):
    """SceneRunner can be instantiated with all required dependencies."""
    from scripts.engine.scene import SceneRunner
    runner = _make_runner(tmp_path)
    assert runner is not None


# ---------------------------------------------------------------------------
# Test 2: read_aloud beat → llm_required, checkpoint written
# ---------------------------------------------------------------------------

def test_read_aloud_beat_returns_llm_required(tmp_path):
    """First beat of scene 0 (read_aloud) → status llm_required, checkpoint written."""
    runner = _make_runner(tmp_path)
    party = _make_party()
    session = _make_session(scene_index=0)
    campaign = _make_campaign()

    result = runner.run_next_beat(party, session, campaign)

    assert result.status == "llm_required"
    assert result.beat_type == "read_aloud"
    assert result.checkpoint_written is True
    assert (tmp_path / "checkpoint.json").exists()


def test_read_aloud_checkpoint_contains_scene_text(tmp_path):
    """Checkpoint context includes the read_aloud text from the scene."""
    import json
    runner = _make_runner(tmp_path)
    party = _make_party()
    session = _make_session(scene_index=0)
    campaign = _make_campaign()

    runner.run_next_beat(party, session, campaign)

    checkpoint = json.loads((tmp_path / "checkpoint.json").read_text(encoding="utf-8"))
    assert checkpoint["beat_type"] == "read_aloud"
    # read_aloud text should appear somewhere in checkpoint
    ctx = checkpoint.get("context", {})
    dp = checkpoint.get("decision_point", {})
    all_text = str(ctx) + str(dp)
    assert "testing ground" in all_text or "arrival" in all_text.lower()


# ---------------------------------------------------------------------------
# Test 3: scene_exit beat → scene_complete or session_complete
# ---------------------------------------------------------------------------

def test_scene_exit_on_last_scene_returns_session_complete(tmp_path):
    """scene_exit on the last scene (index 1 of 2) → session_complete."""
    runner = _make_runner(tmp_path)
    party = _make_party()
    # start at scene 1 (last scene), beat 3 = scene_exit
    session = _make_session(scene_index=1)
    # Manually position to scene_exit beat (beat index 3)
    session.pending_checkpoint = "scene_1_beat_3"
    campaign = _make_campaign()

    result = runner.run_next_beat(party, session, campaign)

    assert result.status == "session_complete"
    assert result.beat_type == "scene_exit"


def test_scene_exit_on_non_last_scene_returns_scene_complete(tmp_path):
    """scene_exit on scene 0 (not last) → scene_complete."""
    runner = _make_runner(tmp_path)
    party = _make_party()
    # Scene 0 has no stat_blocks → beats are: read_aloud(0), scene_narration(1), scene_exit(2)
    session = _make_session(scene_index=0)
    session.pending_checkpoint = "scene_0_beat_2"
    campaign = _make_campaign()

    result = runner.run_next_beat(party, session, campaign)

    assert result.status == "scene_complete"
    assert result.beat_type == "scene_exit"


# ---------------------------------------------------------------------------
# Test 4: encounter_dice beat on scene with stat_blocks → python_resolved, dice non-empty
# ---------------------------------------------------------------------------

def test_encounter_dice_beat_python_resolved_with_dice(tmp_path):
    """Scene 2 encounter_dice beat rolls initiative for stat_blocks → python_resolved."""
    runner = _make_runner(tmp_path)
    party = _make_party()
    # Scene 1 (The Vault) has stat_blocks; beats: read_aloud(0), encounter_dice(1), ...
    session = _make_session(scene_index=1)
    session.pending_checkpoint = "scene_1_beat_1"
    campaign = _make_campaign()

    result = runner.run_next_beat(party, session, campaign)

    assert result.status == "python_resolved"
    assert result.beat_type == "encounter_dice"
    assert len(result.dice_results) > 0


def test_encounter_dice_rolls_one_per_enemy(tmp_path):
    """encounter_dice rolls 1d20 initiative for each stat_block enemy."""
    runner = _make_runner(tmp_path)
    party = _make_party()
    session = _make_session(scene_index=1)
    session.pending_checkpoint = "scene_1_beat_1"
    campaign = _make_campaign()

    result = runner.run_next_beat(party, session, campaign)

    # Scene 1 (The Vault) has exactly 1 stat_block (Test Guard)
    assert len(result.dice_results) == 1
    roll = result.dice_results[0]
    assert roll.expression == "1d20"
    assert 1 <= roll.total <= 20


# ---------------------------------------------------------------------------
# Test 5: beat index advances after each resolved beat
# ---------------------------------------------------------------------------

def test_beat_index_advances_after_python_resolved_beat(tmp_path):
    """After a python_resolved beat, session.pending_checkpoint advances beat_index."""
    runner = _make_runner(tmp_path)
    party = _make_party()
    # Scene 1 beat 1 = encounter_dice (python_resolved)
    session = _make_session(scene_index=1)
    session.pending_checkpoint = "scene_1_beat_1"
    campaign = _make_campaign()

    runner.run_next_beat(party, session, campaign)

    # After running beat 1, pending_checkpoint should reflect beat 2
    assert session.pending_checkpoint == "scene_1_beat_2"


def test_beat_index_set_on_llm_required_beat(tmp_path):
    """On llm_required beat, session.pending_checkpoint is set to current beat cursor."""
    runner = _make_runner(tmp_path)
    party = _make_party()
    session = _make_session(scene_index=0)
    campaign = _make_campaign()

    # Beat 0 = read_aloud → llm_required; pending_checkpoint set to scene_0_beat_0
    result = runner.run_next_beat(party, session, campaign)

    assert result.status == "llm_required"
    assert session.pending_checkpoint == "scene_0_beat_0"


# ---------------------------------------------------------------------------
# Test 6: Full two-scene adventure run → session_complete
# ---------------------------------------------------------------------------

def test_full_two_scene_adventure_reaches_session_complete(tmp_path):
    """
    Run all beats across both scenes; the final call should return session_complete.

    Beat sequence:
      Scene 0 (no stat_blocks): read_aloud(LLM), scene_narration(LLM), scene_exit(PY)
      Scene 1 (1 stat_block):   read_aloud(LLM), encounter_dice(PY), scene_narration(LLM), scene_exit(PY)

    We simulate LLM beats by calling run_next_beat, checking llm_required, then
    manually advancing the beat index (as the CLI resume flow would) before calling again.
    """
    runner = _make_runner(tmp_path)
    party = _make_party()
    session = _make_session(scene_index=0)
    campaign = _make_campaign()

    max_beats = 20
    final_status = None
    narrative_so_far: list[str] = []

    for _ in range(max_beats):
        result = runner.run_next_beat(party, session, campaign, narrative_so_far=narrative_so_far)
        narrative_so_far = result.narrative_so_far

        if result.status in ("session_complete", "scene_complete"):
            if result.status == "session_complete":
                final_status = result.status
                break
            # scene_complete: the runner has already advanced scene_index; continue
            continue

        if result.status == "llm_required":
            # Simulate the CLI resume: advance beat_index past the LLM beat
            # parse current beat from pending_checkpoint
            cp = session.pending_checkpoint  # e.g. "scene_0_beat_0"
            parts = cp.split("_")  # ["scene", "0", "beat", "0"]
            scene_i = int(parts[1])
            beat_i = int(parts[3])
            session.pending_checkpoint = f"scene_{scene_i}_beat_{beat_i + 1}"
            narrative_so_far.append(f"[LLM narrative for beat {beat_i}]")
            continue

        # python_resolved → keep going
        if result.status == "python_resolved":
            continue

    assert final_status == "session_complete", (
        f"Adventure did not reach session_complete within {max_beats} beats; "
        f"last result: {result.status}/{result.beat_type}"
    )


# ---------------------------------------------------------------------------
# Test 7: scene without stat_blocks skips encounter_dice
# ---------------------------------------------------------------------------

def test_scene_without_stat_blocks_skips_encounter_dice(tmp_path):
    """Scene 0 has no stat_blocks; beat 1 should be scene_narration, not encounter_dice."""
    runner = _make_runner(tmp_path)
    party = _make_party()
    session = _make_session(scene_index=0)
    # Beat 0 = read_aloud → LLM; manually advance to beat 1
    session.pending_checkpoint = "scene_0_beat_1"
    campaign = _make_campaign()

    result = runner.run_next_beat(party, session, campaign)

    # Scene 0 has no stat_blocks, so encounter_dice is skipped → scene_narration
    assert result.beat_type == "scene_narration"
    assert result.status == "llm_required"


# ---------------------------------------------------------------------------
# Test 8: RunResult fields are correctly populated
# ---------------------------------------------------------------------------

def test_run_result_fields(tmp_path):
    """RunResult has correct fields populated on a read_aloud beat."""
    from scripts.engine.scene import RunResult
    runner = _make_runner(tmp_path)
    party = _make_party()
    session = _make_session(scene_index=0)
    campaign = _make_campaign()

    result = runner.run_next_beat(party, session, campaign)

    assert isinstance(result, RunResult)
    assert isinstance(result.status, str)
    assert isinstance(result.beat_type, str)
    assert isinstance(result.dice_results, list)
    assert isinstance(result.narrative_so_far, list)
    assert isinstance(result.checkpoint_written, bool)
