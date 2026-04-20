import json
import pytest
from pathlib import Path
from scripts.engine.emitter import Emitter, InboundPacket, ValidationError


@pytest.fixture
def emitter(tmp_path):
    return Emitter(state_dir=tmp_path, party_slugs=["aelric", "thera", "kessa", "grom"])


def test_emitter_builds_outbound_packet(emitter):
    packet = emitter.build_outbound(
        session="S04",
        scene_id=3,
        scene_name="The Rite",
        beat_type="hint-delivery",
        state_snapshot={"aelric": {"hp": 28}},
        dice_results=[{"expr": "1d20+3", "total": 12, "label": "Grom Religion"}],
        resolved_mechanics={"rite_result": "pass"},
        decision_point={"type": "hint-delivery", "description": "Hint 2 unlocks"},
        context={"read_aloud": "At the seventh ring..."},
        scene_narrative_so_far=["Scene opened: 'Grey slope...'"],
    )
    assert packet["session"] == "S04"
    assert packet["scene_id"] == 3
    assert packet["beat_type"] == "hint-delivery"
    assert "scene_narrative_so_far" in packet


def test_emitter_writes_checkpoint_before_blocking(emitter, tmp_path):
    packet = emitter.build_outbound(
        session="S04", scene_id=1, scene_name="Test", beat_type="read_aloud",
        state_snapshot={}, dice_results=[], resolved_mechanics={},
        decision_point={}, context={}, scene_narrative_so_far=[],
    )
    emitter.write_checkpoint(packet)
    checkpoint_path = tmp_path / "checkpoint.json"
    assert checkpoint_path.exists()
    stored = json.loads(checkpoint_path.read_text())
    assert stored["session"] == "S04"


def test_validate_inbound_good_packet(emitter):
    raw = {
        "narrative": "Kessa steps forward...",
        "state_updates": {"kessa": {"portent_used": [10]}},
        "innovations_flagged": ["portent-benediction"],
        "advance_to_scene": 4,
        "notes_for_log": "Kessa spoke Qualinesti.",
    }
    packet = emitter.validate_inbound(raw, current_scene_index=3)
    assert packet.narrative == "Kessa steps forward..."
    assert packet.advance_to_scene == 4


def test_validate_inbound_empty_narrative_raises(emitter):
    raw = {"narrative": "", "state_updates": {}, "advance_to_scene": 4}
    with pytest.raises(ValidationError, match="narrative is empty"):
        emitter.validate_inbound(raw, current_scene_index=3)


def test_validate_inbound_unknown_pc_raises(emitter):
    raw = {
        "narrative": "Some text",
        "state_updates": {"pella": {"hp": 5}},
        "advance_to_scene": 4,
    }
    with pytest.raises(ValidationError, match="unknown PC"):
        emitter.validate_inbound(raw, current_scene_index=3)


def test_validate_inbound_backward_scene_raises(emitter):
    raw = {"narrative": "Text", "state_updates": {}, "advance_to_scene": 1}
    with pytest.raises(ValidationError, match="invalid scene advance"):
        emitter.validate_inbound(raw, current_scene_index=3)


def test_validate_inbound_missing_narrative_raises(emitter):
    raw = {"state_updates": {}, "advance_to_scene": 4}
    with pytest.raises(ValidationError, match="narrative"):
        emitter.validate_inbound(raw, current_scene_index=3)


def test_validate_inbound_missing_advance_scene_raises(emitter):
    raw = {"narrative": "Text", "state_updates": {}}
    with pytest.raises(ValidationError, match="advance_to_scene"):
        emitter.validate_inbound(raw, current_scene_index=3)


def test_validate_inbound_defaults_optional_fields(emitter):
    raw = {"narrative": "Text", "state_updates": {}, "advance_to_scene": 4}
    packet = emitter.validate_inbound(raw, current_scene_index=3)
    assert packet.innovations_flagged == []
    assert packet.notes_for_log == ""


def test_validate_inbound_above_max_scene_raises(emitter):
    raw = {"narrative": "Text", "state_updates": {}, "advance_to_scene": 99}
    with pytest.raises(ValidationError, match="exceeds max scene"):
        emitter.validate_inbound(raw, current_scene_index=3, max_scene=5)


def test_validate_inbound_non_mutable_field_not_in_scope():
    # This is tested in integration — just confirm validate_inbound itself
    # passes non-mutable field through (filtering happens in marathon.py)
    from scripts.engine.emitter import Emitter, InboundPacket
    e = Emitter(state_dir=__import__("pathlib").Path("/tmp"), party_slugs=["aelric"])
    raw = {"narrative": "X", "state_updates": {"aelric": {"hp_max": 999}}, "advance_to_scene": 1}
    packet = e.validate_inbound(raw, current_scene_index=0)
    assert packet.state_updates["aelric"]["hp_max"] == 999  # validation passes; filtering in CLI
