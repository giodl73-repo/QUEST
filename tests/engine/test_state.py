import json
import pytest
from pathlib import Path
from scripts.engine.state import PartyState, SessionState, CampaignFacts, StateManager


def test_party_state_from_dict():
    data = {
        "aelric-of-crownhold": {
            "hp": 28, "hp_max": 28,
            "spell_slots": {"L1": 3, "L2": 0},
            "attunements": ["varran-reliquary"],
            "lay_on_hands": 15,
            "concentration": None,
            "conditions": []
        }
    }
    ps = PartyState.from_dict(data)
    assert ps["aelric-of-crownhold"].hp == 28
    assert ps["aelric-of-crownhold"].attunements == ["varran-reliquary"]


def test_party_state_apply_hp_delta():
    data = {"fighter": {"hp": 28, "hp_max": 28, "spell_slots": {}, "attunements": [],
                        "lay_on_hands": 0, "concentration": None, "conditions": []}}
    ps = PartyState.from_dict(data)
    ps.apply_hp_delta("fighter", -10)
    assert ps["fighter"].hp == 18


def test_party_state_hp_floor_zero():
    data = {"fighter": {"hp": 5, "hp_max": 28, "spell_slots": {}, "attunements": [],
                        "lay_on_hands": 0, "concentration": None, "conditions": []}}
    ps = PartyState.from_dict(data)
    ps.apply_hp_delta("fighter", -100)
    assert ps["fighter"].hp == 0


def test_party_state_hp_ceil_max():
    data = {"fighter": {"hp": 5, "hp_max": 28, "spell_slots": {}, "attunements": [],
                        "lay_on_hands": 0, "concentration": None, "conditions": []}}
    ps = PartyState.from_dict(data)
    ps.apply_hp_delta("fighter", +100)
    assert ps["fighter"].hp == 28


def test_party_state_use_spell_slot():
    data = {"wizard": {"hp": 16, "hp_max": 16, "spell_slots": {"L1": 4, "L2": 2},
                       "attunements": [], "lay_on_hands": 0, "concentration": None,
                       "conditions": []}}
    ps = PartyState.from_dict(data)
    ps.use_spell_slot("wizard", "L1")
    assert ps["wizard"].spell_slots["L1"] == 3


def test_party_state_use_spell_slot_raises_when_empty():
    data = {"wizard": {"hp": 16, "hp_max": 16, "spell_slots": {"L1": 0, "L2": 2},
                       "attunements": [], "lay_on_hands": 0, "concentration": None,
                       "conditions": []}}
    ps = PartyState.from_dict(data)
    with pytest.raises(ValueError, match="no L1 slots remaining"):
        ps.use_spell_slot("wizard", "L1")


def test_session_state_from_dict():
    data = {
        "adventure": "0004-the-wrath-coin",
        "session": "S04",
        "dice_seed": "S04-20260419",
        "scene_index": 3,
        "scenes_completed": [0, 1, 2],
        "pending_checkpoint": None
    }
    ss = SessionState.from_dict(data)
    assert ss.scene_index == 3
    assert ss.scenes_completed == [0, 1, 2]


def test_session_state_advance_scene():
    data = {"adventure": "test", "session": "S01", "dice_seed": "S01",
            "scene_index": 1, "scenes_completed": [0], "pending_checkpoint": None}
    ss = SessionState.from_dict(data)
    ss.advance_scene()
    assert ss.scene_index == 2
    assert 1 in ss.scenes_completed


def test_state_manager_write_and_read(tmp_path):
    sm = StateManager(state_dir=tmp_path)
    party_data = {"fighter": {"hp": 20, "hp_max": 20, "spell_slots": {}, "attunements": [],
                               "lay_on_hands": 0, "concentration": None, "conditions": []}}
    session_data = {"adventure": "test", "session": "S01", "dice_seed": "S01",
                    "scene_index": 0, "scenes_completed": [], "pending_checkpoint": None}
    campaign_data = {"hints": {"hint-1": "caught"}, "campaign_permanent": []}

    sm.write_session(
        party=PartyState.from_dict(party_data),
        session=SessionState.from_dict(session_data),
        campaign=CampaignFacts.from_dict(campaign_data),
    )

    loaded = sm.read_session()
    assert loaded["session"].adventure == "test"
    assert loaded["party"]["fighter"].hp == 20


def test_state_manager_atomic_write(tmp_path):
    sm = StateManager(state_dir=tmp_path)
    party_data = {"f": {"hp": 5, "hp_max": 5, "spell_slots": {}, "attunements": [],
                        "lay_on_hands": 0, "concentration": None, "conditions": []}}
    session_data = {"adventure": "t", "session": "S1", "dice_seed": "S1",
                    "scene_index": 0, "scenes_completed": [], "pending_checkpoint": None}
    campaign_data = {"hints": {}, "campaign_permanent": []}
    sm.write_session(
        party=PartyState.from_dict(party_data),
        session=SessionState.from_dict(session_data),
        campaign=CampaignFacts.from_dict(campaign_data),
    )
    assert not (tmp_path / "session.json.tmp").exists()
    assert (tmp_path / "session.json").exists()


def test_state_manager_no_session_returns_none(tmp_path):
    sm = StateManager(state_dir=tmp_path)
    assert sm.read_session() is None


# ---------------------------------------------------------------------------
# New fields: route, party_slug
# ---------------------------------------------------------------------------

def test_session_state_route_defaults_to_none():
    data = {"adventure": "t", "session": "S1", "dice_seed": "s",
            "scene_index": 0, "scenes_completed": [], "pending_checkpoint": None}
    ss = SessionState.from_dict(data)
    assert ss.route is None


def test_session_state_route_can_be_set():
    data = {"adventure": "t", "session": "S1", "dice_seed": "s",
            "scene_index": 0, "scenes_completed": [], "pending_checkpoint": None,
            "route": "D"}
    ss = SessionState.from_dict(data)
    assert ss.route == "D"


def test_session_state_party_slug_defaults():
    data = {"adventure": "t", "session": "S1", "dice_seed": "s",
            "scene_index": 0, "scenes_completed": [], "pending_checkpoint": None}
    ss = SessionState.from_dict(data)
    assert ss.party_slug == "compact-wardens"


def test_session_state_party_slug_preserved():
    data = {"adventure": "t", "session": "S1", "dice_seed": "s",
            "scene_index": 0, "scenes_completed": [], "pending_checkpoint": None,
            "party_slug": "varduin-muster"}
    ss = SessionState.from_dict(data)
    assert ss.party_slug == "varduin-muster"


def test_session_state_to_dict_includes_route_and_party_slug():
    data = {"adventure": "t", "session": "S1", "dice_seed": "s",
            "scene_index": 0, "scenes_completed": [], "pending_checkpoint": None,
            "route": "A", "party_slug": "compact-wardens"}
    ss = SessionState.from_dict(data)
    d = ss.to_dict()
    assert d["route"] == "A"
    assert d["party_slug"] == "compact-wardens"


def test_state_manager_write_and_read_preserves_party_slug(tmp_path):
    sm = StateManager(state_dir=tmp_path)
    party_data = {"fighter": {"hp": 20, "hp_max": 20, "spell_slots": {}, "attunements": [],
                               "lay_on_hands": 0, "concentration": None, "conditions": []}}
    session_data = {"adventure": "test", "session": "S01", "dice_seed": "S01",
                    "scene_index": 0, "scenes_completed": [], "pending_checkpoint": None,
                    "party_slug": "compact-wardens"}
    campaign_data = {"hints": {}, "campaign_permanent": []}
    sm.write_session(
        party=PartyState.from_dict(party_data),
        session=SessionState.from_dict(session_data),
        campaign=CampaignFacts.from_dict(campaign_data),
    )
    loaded = sm.read_session()
    assert loaded["session"].party_slug == "compact-wardens"


def test_state_manager_write_checkpoint_and_read(tmp_path):
    sm = StateManager(state_dir=tmp_path)
    payload = {"session": "S01", "beat_type": "read_aloud", "scene_id": 0}
    sm.write_checkpoint(payload)
    loaded = sm.read_checkpoint()
    assert loaded["beat_type"] == "read_aloud"


def test_state_manager_delete_checkpoint(tmp_path):
    sm = StateManager(state_dir=tmp_path)
    sm.write_checkpoint({"x": 1})
    assert sm.checkpoint_path.exists()
    sm.delete_checkpoint()
    assert not sm.checkpoint_path.exists()


def test_state_manager_delete_checkpoint_no_error_when_absent(tmp_path):
    sm = StateManager(state_dir=tmp_path)
    sm.delete_checkpoint()  # should not raise


def test_state_manager_corrupted_session_raises(tmp_path):
    (tmp_path / "session.json").write_text("NOT JSON", encoding="utf-8")
    sm = StateManager(state_dir=tmp_path)
    with pytest.raises(RuntimeError, match="corrupted"):
        sm.read_session()


def test_party_state_any_below_half_hp_true():
    data = {
        "a": {"hp": 5, "hp_max": 28, "spell_slots": {}, "attunements": [],
              "lay_on_hands": 0, "concentration": None, "conditions": []},
        "b": {"hp": 28, "hp_max": 28, "spell_slots": {}, "attunements": [],
              "lay_on_hands": 0, "concentration": None, "conditions": []},
    }
    ps = PartyState.from_dict(data)
    assert ps.any_below_half_hp() is True


def test_party_state_any_below_half_hp_false_when_all_healthy():
    data = {
        "a": {"hp": 28, "hp_max": 28, "spell_slots": {}, "attunements": [],
              "lay_on_hands": 0, "concentration": None, "conditions": []},
    }
    ps = PartyState.from_dict(data)
    assert ps.any_below_half_hp() is False


def test_party_state_slugs():
    data = {
        "thessaly": {"hp": 32, "hp_max": 32, "spell_slots": {}, "attunements": [],
                     "lay_on_hands": 0, "concentration": None, "conditions": []},
        "orik": {"hp": 52, "hp_max": 52, "spell_slots": {}, "attunements": [],
                 "lay_on_hands": 0, "concentration": None, "conditions": []},
    }
    ps = PartyState.from_dict(data)
    assert set(ps.slugs()) == {"thessaly", "orik"}
