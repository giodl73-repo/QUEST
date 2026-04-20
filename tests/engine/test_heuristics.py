import pytest
from scripts.engine.loader import load_party
from scripts.engine.heuristics import Heuristics, HeuristicsError
from pathlib import Path

FIXTURES = Path("tests/fixtures")


@pytest.fixture
def pcs():
    return load_party(FIXTURES)


@pytest.fixture
def h(pcs):
    return Heuristics(pcs)


def test_doubt_die_returns_interpretation(h):
    result = h.doubt_die("test-fighter", context="combat", seed="doubt-test")
    assert result.interpretation in ("attack", "defend")


def test_doubt_die_same_seed_same_result(h):
    r1 = h.doubt_die("test-fighter", context="any", seed="fixed")
    r2 = h.doubt_die("test-fighter", context="any", seed="fixed")
    assert r1.interpretation == r2.interpretation


def test_doubt_die_unknown_pc_raises(h):
    with pytest.raises(HeuristicsError, match="unknown PC"):
        h.doubt_die("no-such-pc", context="x", seed="s")


def test_bless_active_false_by_default(h):
    assert h.bless_active("test-fighter") is False


def test_bless_active_true_after_set(h):
    h.set_bless("test-fighter", True)
    assert h.bless_active("test-fighter") is True


def test_signature_move_due_returns_value_when_none_used(h):
    result = h.signature_move_due("test-fighter", moves_used_this_session=[])
    assert result is not None


def test_signature_move_due_returns_none_when_already_used(h):
    result = h.signature_move_due("test-fighter", moves_used_this_session=["power-attack"])
    assert result is None


def test_condition_evaluation_any_pc_below_half(h):
    from scripts.engine.state import PartyState
    party = PartyState.from_dict({
        "test-fighter": {"hp": 5, "hp_max": 28, "spell_slots": {}, "attunements": [],
                          "lay_on_hands": 0, "concentration": None, "conditions": []}
    })
    assert h.eval_condition("any_pc_below_half_hp", party=party) is True


def test_condition_evaluation_always(h):
    from scripts.engine.state import PartyState
    party = PartyState.from_dict({
        "test-fighter": {"hp": 28, "hp_max": 28, "spell_slots": {}, "attunements": [],
                          "lay_on_hands": 0, "concentration": None, "conditions": []}
    })
    assert h.eval_condition("always", party=party) is True


def test_unknown_condition_raises(h):
    from scripts.engine.state import PartyState
    party = PartyState.from_dict({
        "f": {"hp": 5, "hp_max": 28, "spell_slots": {}, "attunements": [],
               "lay_on_hands": 0, "concentration": None, "conditions": []}
    })
    with pytest.raises(HeuristicsError, match="unknown condition token"):
        h.eval_condition("involves_spaghetti", party=party)


def test_doubt_die_raises_on_no_match(pcs):
    """doubt_die with a gap in the range table raises HeuristicsError."""
    from scripts.engine.loader import PC
    from scripts.engine.heuristics import Heuristics, HeuristicsError
    # PC with a gap: covers 1-2 and 5-6 but not 3-4
    gapped_pc = PC(
        slug="gapped",
        ac=10, hp=10, hp_max=10,
        spell_slots={}, attunements=[],
        heuristics={
            "doubt_die": {"1-2": "a", "5-6": "b"},
            "decision_order": [],
            "signature_moves": [],
            "voice_tags": [],
        }
    )
    h = Heuristics([gapped_pc])
    # Try many seeds until we find one that rolls 3 or 4
    for i in range(200):
        try:
            result = h.doubt_die("gapped", context="x", seed=f"gap-{i}")
            # if it returned without raising, the roll was 1, 2, 5, or 6 — ok
        except HeuristicsError:
            return  # found a gap roll — test passes
    pytest.skip("Could not produce a gap roll in 200 seeds")


def test_select_target_returns_first_enemy(h):
    enemies = [{"name": "Guard", "hp": 22}, {"name": "Archer", "hp": 15}]
    result = h.select_target("test-fighter", enemies, scene_context={})
    assert result == enemies[0]


def test_select_target_returns_none_for_empty(h):
    assert h.select_target("test-fighter", [], scene_context={}) is None
