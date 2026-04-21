"""Tests for engine/event_log.py — full coverage of EventLogger."""
import json
import pytest
from pathlib import Path
from scripts.engine.event_log import EventLogger, VALID_TYPES


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def make_logger(tmp_path) -> EventLogger:
    return EventLogger(tmp_path / "event_log.jsonl")


def load_raw(tmp_path) -> list[dict]:
    p = tmp_path / "event_log.jsonl"
    if not p.exists():
        return []
    return [json.loads(line) for line in p.read_text(encoding="utf-8").splitlines() if line.strip()]


# ---------------------------------------------------------------------------
# log() — single event
# ---------------------------------------------------------------------------

def test_log_valid_spell_cast_writes_entry(tmp_path):
    el = make_logger(tmp_path)
    el.log({"type": "spell_cast", "pc": "thessaly", "spell": "Counterspell",
            "level": 3, "scene": 1, "context": "combat"})
    entries = load_raw(tmp_path)
    assert len(entries) == 1
    assert entries[0]["spell"] == "Counterspell"
    assert entries[0]["pc"] == "thessaly"


def test_log_unknown_type_silently_dropped(tmp_path):
    el = make_logger(tmp_path)
    el.log({"type": "INVALID_TYPE", "pc": "orik"})
    assert load_raw(tmp_path) == []


def test_log_missing_type_silently_dropped(tmp_path):
    el = make_logger(tmp_path)
    el.log({"pc": "orik", "action": "attack"})
    assert load_raw(tmp_path) == []


def test_log_all_valid_types_accepted(tmp_path):
    el = make_logger(tmp_path)
    for t in VALID_TYPES:
        el.log({"type": t, "pc": "test", "scene": 0})
    entries = load_raw(tmp_path)
    assert len(entries) == len(VALID_TYPES)


@pytest.mark.parametrize("event_type", [
    "feature_used", "attack", "saving_throw", "reaction",
    "condition_applied", "condition_cleared", "near_death",
    "social_roll", "advantage_event", "resource_recovery",
])
def test_log_each_valid_type(tmp_path, event_type):
    el = make_logger(tmp_path)
    el.log({"type": event_type, "pc": "calder", "scene": 2})
    entries = load_raw(tmp_path)
    assert entries[0]["type"] == event_type


def test_log_creates_file_on_first_write(tmp_path):
    p = tmp_path / "event_log.jsonl"
    assert not p.exists()
    el = EventLogger(p)
    el.log({"type": "spell_cast", "pc": "lenne", "spell": "Shield", "level": 1, "scene": 0})
    assert p.exists()


def test_log_appends_multiple_entries(tmp_path):
    el = make_logger(tmp_path)
    el.log({"type": "spell_cast", "pc": "thessaly", "spell": "Shield", "level": 1, "scene": 0})
    el.log({"type": "feature_used", "pc": "orik", "feature": "menacing_attack", "scene": 0})
    entries = load_raw(tmp_path)
    assert len(entries) == 2


# ---------------------------------------------------------------------------
# log_many()
# ---------------------------------------------------------------------------

def test_log_many_writes_all_valid(tmp_path):
    el = make_logger(tmp_path)
    events = [
        {"type": "spell_cast", "pc": "thessaly", "spell": "Fireball", "level": 3, "scene": 1},
        {"type": "feature_used", "pc": "orik", "feature": "action_surge", "scene": 1},
        {"type": "BOGUS"},
    ]
    el.log_many(events)
    entries = load_raw(tmp_path)
    assert len(entries) == 2  # bogus dropped


def test_log_many_empty_list_no_crash(tmp_path):
    el = make_logger(tmp_path)
    el.log_many([])
    assert load_raw(tmp_path) == []


# ---------------------------------------------------------------------------
# load()
# ---------------------------------------------------------------------------

def test_load_returns_all_entries(tmp_path):
    el = make_logger(tmp_path)
    el.log({"type": "spell_cast", "pc": "a", "spell": "X", "level": 1, "scene": 0})
    el.log({"type": "reaction", "pc": "b", "reaction": "Y", "trigger": "Z", "scene": 0})
    loaded = el.load()
    assert len(loaded) == 2


def test_load_empty_when_no_file(tmp_path):
    el = make_logger(tmp_path)
    assert el.load() == []


def test_load_skips_corrupted_lines(tmp_path):
    p = tmp_path / "event_log.jsonl"
    p.write_text('{"type": "spell_cast", "pc": "a", "spell": "B", "level": 1, "scene": 0}\nNOT JSON\n',
                 encoding="utf-8")
    el = EventLogger(p)
    entries = el.load()
    assert len(entries) == 1
    assert entries[0]["spell"] == "B"


def test_load_skips_blank_lines(tmp_path):
    p = tmp_path / "event_log.jsonl"
    p.write_text('{"type": "spell_cast", "pc": "a", "spell": "B", "level": 1, "scene": 0}\n\n\n',
                 encoding="utf-8")
    el = EventLogger(p)
    assert len(el.load()) == 1


# ---------------------------------------------------------------------------
# summary()
# ---------------------------------------------------------------------------

def test_summary_counts_by_type(tmp_path):
    el = make_logger(tmp_path)
    el.log({"type": "spell_cast", "pc": "t", "spell": "A", "level": 1, "scene": 0})
    el.log({"type": "spell_cast", "pc": "t", "spell": "B", "level": 2, "scene": 1})
    el.log({"type": "feature_used", "pc": "o", "feature": "X", "scene": 0})
    s = el.summary()
    assert s["spell_cast"] == 2
    assert s["feature_used"] == 1


def test_summary_empty_when_no_file(tmp_path):
    el = make_logger(tmp_path)
    assert el.summary() == {}


# ---------------------------------------------------------------------------
# spells_table()
# ---------------------------------------------------------------------------

def test_spells_table_returns_only_spell_cast(tmp_path):
    el = make_logger(tmp_path)
    el.log({"type": "spell_cast", "pc": "t", "spell": "A", "level": 1, "scene": 2})
    el.log({"type": "feature_used", "pc": "o", "feature": "X", "scene": 1})
    spells = el.spells_table()
    assert len(spells) == 1
    assert spells[0]["spell"] == "A"


def test_spells_table_sorted_by_scene(tmp_path):
    el = make_logger(tmp_path)
    el.log({"type": "spell_cast", "pc": "t", "spell": "Later", "level": 1, "scene": 5})
    el.log({"type": "spell_cast", "pc": "t", "spell": "Earlier", "level": 1, "scene": 1})
    spells = el.spells_table()
    assert spells[0]["spell"] == "Earlier"
    assert spells[1]["spell"] == "Later"


def test_spells_table_empty_when_none(tmp_path):
    el = make_logger(tmp_path)
    el.log({"type": "feature_used", "pc": "o", "feature": "X", "scene": 0})
    assert el.spells_table() == []


# ---------------------------------------------------------------------------
# features_table()
# ---------------------------------------------------------------------------

def test_features_table_returns_only_feature_used(tmp_path):
    el = make_logger(tmp_path)
    el.log({"type": "feature_used", "pc": "orik", "feature": "menacing_attack", "scene": 1})
    el.log({"type": "spell_cast", "pc": "t", "spell": "Shield", "level": 1, "scene": 0})
    features = el.features_table()
    assert len(features) == 1
    assert features[0]["feature"] == "menacing_attack"


def test_features_table_sorted_by_scene(tmp_path):
    el = make_logger(tmp_path)
    el.log({"type": "feature_used", "pc": "orik", "feature": "second", "scene": 3})
    el.log({"type": "feature_used", "pc": "orik", "feature": "first", "scene": 1})
    features = el.features_table()
    assert features[0]["feature"] == "first"


# ---------------------------------------------------------------------------
# near_death_events()
# ---------------------------------------------------------------------------

def test_near_death_events_filtered(tmp_path):
    el = make_logger(tmp_path)
    el.log({"type": "near_death", "pc": "sera", "scene": 2, "cause": "fireball"})
    el.log({"type": "spell_cast", "pc": "t", "spell": "X", "level": 1, "scene": 2})
    nds = el.near_death_events()
    assert len(nds) == 1
    assert nds[0]["pc"] == "sera"


def test_near_death_events_empty(tmp_path):
    el = make_logger(tmp_path)
    assert el.near_death_events() == []
