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


def test_log_writer_uses_party_slug_param(tmp_path, session_data, party_data, dice_log):
    lw = LogWriter("test-adventure", session_data, party_data, party_data,
                   {}, dice_log, tmp_path, party_slug="custom-party")
    out = lw.write()
    content = out.read_text(encoding="utf-8")
    assert "custom-party" in content


def test_log_writer_atomic_write(tmp_path, session_data, party_data, dice_log):
    lw = LogWriter("test-adventure", session_data, party_data, party_data,
                   {}, dice_log, tmp_path)
    out = lw.write()
    assert not (tmp_path / "S04-log.md.tmp").exists()
    assert out.exists()


def test_log_writer_has_extra_sections(tmp_path, session_data, party_data, dice_log):
    lw = LogWriter("test-adventure", session_data, party_data, party_data,
                   {}, dice_log, tmp_path, innovations_flagged=["portent-benediction"])
    out = lw.write()
    content = out.read_text(encoding="utf-8")
    assert "Curse symptoms" in content
    assert "surprises" in content.lower() or "Surprises" in content
    assert "Open threads" in content


# ---------------------------------------------------------------------------
# Event log section in session log output
# ---------------------------------------------------------------------------

def test_log_writer_event_section_with_spells(tmp_path, session_data, party_data, dice_log):
    from scripts.engine.event_log import EventLogger
    event_log_path = tmp_path / "event_log.jsonl"
    el = EventLogger(event_log_path)
    el.log({"type": "spell_cast", "pc": "thessaly", "spell": "Counterspell",
            "level": 3, "scene": 1, "context": "combat"})
    el.log({"type": "spell_cast", "pc": "lenne", "spell": "Shield",
            "level": 1, "scene": 2, "context": "combat"})
    el.log({"type": "feature_used", "pc": "orik", "feature": "menacing_attack",
            "scene": 1, "result": "frightened"})

    lw = LogWriter("test-adventure", session_data, party_data, party_data,
                   {}, dice_log, tmp_path, event_log_path=event_log_path)
    out = lw.write()
    content = out.read_text(encoding="utf-8")

    assert "Mechanical events" in content
    assert "Spells cast" in content
    assert "Counterspell" in content
    assert "Shield" in content
    assert "Class features used" in content
    assert "menacing_attack" in content


def test_log_writer_event_section_with_near_death(tmp_path, session_data, party_data, dice_log):
    from scripts.engine.event_log import EventLogger
    event_log_path = tmp_path / "event_log.jsonl"
    el = EventLogger(event_log_path)
    el.log({"type": "near_death", "pc": "sera", "scene": 2,
            "cause": "fireball", "stabilized_by": "calder"})

    lw = LogWriter("test-adventure", session_data, party_data, party_data,
                   {}, dice_log, tmp_path, event_log_path=event_log_path)
    content = lw.write().read_text(encoding="utf-8")
    assert "Near-death" in content
    assert "sera" in content


def test_log_writer_event_section_no_event_log(tmp_path, session_data, party_data, dice_log):
    """When event_log_path is None, no Mechanical events section appears."""
    lw = LogWriter("test-adventure", session_data, party_data, party_data,
                   {}, dice_log, tmp_path, event_log_path=None)
    content = lw.write().read_text(encoding="utf-8")
    assert "Mechanical events" not in content


def test_log_writer_event_section_empty_log_shows_hint(tmp_path, session_data, party_data, dice_log):
    """Empty event log prompts the DM to include events in state_updates."""
    event_log_path = tmp_path / "event_log.jsonl"
    # Don't write any entries — file doesn't exist
    lw = LogWriter("test-adventure", session_data, party_data, party_data,
                   {}, dice_log, tmp_path, event_log_path=event_log_path)
    content = lw.write().read_text(encoding="utf-8")
    assert "Mechanical events" in content
    assert "state_updates" in content  # the hint message
