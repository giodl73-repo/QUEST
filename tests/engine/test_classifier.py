import pytest
from scripts.engine.classifier import Event, classify


def make_event(**kwargs):
    defaults = dict(
        type="dice_roll",
        pc_slug="aelric",
        involves_grief_paragraph=False,
        is_option_c=False,
        is_hint_delivery=False,
        is_read_aloud=False,
        has_npc_dialogue=False,
        is_key_loot=False,
        scene_context={},
    )
    defaults.update(kwargs)
    return Event(**defaults)


def test_dice_roll_is_python():
    assert classify(make_event(type="dice_roll")) == "python"

def test_hp_delta_is_python():
    assert classify(make_event(type="hp_delta")) == "python"

def test_resource_use_is_python():
    assert classify(make_event(type="resource_use")) == "python"

def test_doubt_die_is_python():
    assert classify(make_event(type="doubt_die")) == "python"

def test_signature_move_timing_is_python():
    assert classify(make_event(type="signature_move")) == "python"

def test_condition_apply_is_python():
    assert classify(make_event(type="condition_apply")) == "python"

def test_scene_advance_is_python():
    assert classify(make_event(type="scene_advance")) == "python"

def test_read_aloud_is_llm():
    assert classify(make_event(type="read_aloud", is_read_aloud=True)) == "llm"

def test_option_c_is_llm():
    assert classify(make_event(type="option_c", is_option_c=True)) == "llm"

def test_npc_dialogue_is_llm():
    assert classify(make_event(type="dialogue", has_npc_dialogue=True)) == "llm"

def test_memory_fragment_is_llm():
    assert classify(make_event(type="memory_fragment")) == "llm"

def test_atmospheric_chain_is_llm():
    assert classify(make_event(type="atmospheric_chain")) == "llm"

def test_grief_paragraph_is_llm():
    assert classify(make_event(type="any", involves_grief_paragraph=True)) == "llm"

def test_hint_delivery_is_llm():
    assert classify(make_event(type="hint_delivery", is_hint_delivery=True)) == "llm"

def test_key_loot_is_llm():
    assert classify(make_event(type="loot_narration", is_key_loot=True)) == "llm"

def test_unknown_type_defaults_to_llm():
    assert classify(make_event(type="unrecognised_future_type")) == "llm"
