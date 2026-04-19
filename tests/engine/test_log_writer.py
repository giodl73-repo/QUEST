import json
import pytest
from pathlib import Path
from scripts.engine.log_writer import LogWriter


@pytest.fixture
def session_data():
    return {
        "session": "S04",
        "adventure": "test-adventure",
        "dice_seed": "S04-20260419",
        "scenes_completed": [0, 1],
        "scene_index": 2,
    }


@pytest.fixture
def party_data():
    return {
        "aelric": {"hp": 18, "hp_max": 28, "hp_start": 28, "spell_slots": {"L1": 1},
                   "attunements": ["varran-reliquary"], "lay_on_hands": 15,
                   "concentration": None, "conditions": []},
        "thera": {"hp": 20, "hp_max": 20, "hp_start": 20, "spell_slots": {},
                  "attunements": [], "lay_on_hands": 0,
                  "concentration": None, "conditions": []},
    }


@pytest.fixture
def dice_log(tmp_path):
    log = tmp_path / "dice_log.jsonl"
    entries = [
        {"expression": "1d20+5", "rolls": [14], "kept": None, "mod": 5,
         "bless_roll": None, "total": 19, "crit": False, "fumble": False,
         "seed_position": 0, "scene_id": 0, "beat_index": 1,
         "pc_slug": "aelric", "action_label": "attack",
         "log_stub": "DICE_STUB_0"},
    ]
    log.write_text("\n".join(json.dumps(x) for x in entries))
    return log


def test_log_writer_produces_file(tmp_path, session_data, party_data, dice_log):
    narratives = {"0": "Scene one narrative.", "1": "Scene two narrative."}
    lw = LogWriter(
        adventure_slug="test-adventure",
        session=session_data,
        party_start=party_data,
        party_end=party_data,
        narratives=narratives,
        dice_log_path=dice_log,
        output_dir=tmp_path,
    )
    out = lw.write()
    assert out.exists()
    assert out.name == "S04-log.md"


def test_log_writer_frontmatter(tmp_path, session_data, party_data, dice_log):
    lw = LogWriter("test-adventure", session_data, party_data, party_data,
                   {}, dice_log, tmp_path)
    out = lw.write()
    content = out.read_text()
    assert "session: S04" in content
    assert "dice-seed: S04-20260419" in content


def test_log_writer_party_table(tmp_path, session_data, party_data, dice_log):
    lw = LogWriter("test-adventure", session_data, party_data, party_data,
                   {}, dice_log, tmp_path)
    out = lw.write()
    content = out.read_text()
    assert "aelric" in content
    assert "thera" in content


def test_log_writer_injects_dice_roll_format(tmp_path, session_data, party_data, dice_log):
    narratives = {"0": "Aelric attacked. DICE_STUB_0 Then continued."}
    lw = LogWriter("test-adventure", session_data, party_data, party_data,
                   narratives, dice_log, tmp_path)
    out = lw.write()
    content = out.read_text()
    assert "🎲" in content
    assert "1d20+5" in content
    assert "total=19" in content


def test_log_writer_summary_section(tmp_path, session_data, party_data, dice_log):
    session_with_summary = {**session_data, "summary": "The party defeated the guards."}
    lw = LogWriter("test-adventure", session_with_summary, party_data, party_data,
                   {}, dice_log, tmp_path)
    out = lw.write()
    content = out.read_text()
    assert "Session Summary" in content
    assert "defeated the guards" in content
