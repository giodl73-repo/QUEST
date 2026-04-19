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
