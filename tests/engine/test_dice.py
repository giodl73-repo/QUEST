import pytest
from scripts.engine.dice import DiceEngine, RollResult, DiceError


def test_roll_result_is_dataclass():
    r = RollResult(
        expression="1d20+5",
        rolls=[14],
        kept=None,
        mod=5,
        bless_roll=None,
        total=19,
        crit=False,
        fumble=False,
        seed_position=0,
    )
    assert r.total == 19


def test_same_seed_same_rolls():
    d1 = DiceEngine(seed="S04-20260419")
    d2 = DiceEngine(seed="S04-20260419")
    r1 = d1.roll("1d20+3")
    r2 = d2.roll("1d20+3")
    assert r1.rolls == r2.rolls
    assert r1.total == r2.total


def test_different_seeds_may_differ():
    d1 = DiceEngine(seed="S04-20260419")
    d2 = DiceEngine(seed="S05-20260419")
    rolls1 = [d1.roll("1d20").total for _ in range(10)]
    rolls2 = [d2.roll("1d20").total for _ in range(10)]
    assert rolls1 != rolls2


def test_modifier_applied():
    d = DiceEngine(seed="test-seed")
    r = d.roll("1d6+3")
    assert r.total == r.rolls[0] + 3
    assert r.mod == 3


def test_advantage_keeps_higher():
    d = DiceEngine(seed="test-seed")
    r = d.roll("1d20+2", adv=True)
    assert len(r.rolls) == 2
    assert r.kept == max(r.rolls)
    assert r.total == max(r.rolls) + 2


def test_disadvantage_keeps_lower():
    d = DiceEngine(seed="test-seed")
    r = d.roll("1d20", disadv=True)
    assert r.kept == min(r.rolls)


def test_crit_on_nat_20():
    for seed_suffix in range(100):
        d = DiceEngine(seed=f"crit-test-{seed_suffix}")
        r = d.roll("1d20")
        if r.rolls[0] == 20:
            assert r.crit is True
            assert r.fumble is False
            return
    pytest.skip("Could not find a nat-20 in 100 seeds")


def test_fumble_on_nat_1():
    for seed_suffix in range(100):
        d = DiceEngine(seed=f"fumble-test-{seed_suffix}")
        r = d.roll("1d20")
        if r.rolls[0] == 1:
            assert r.fumble is True
            assert r.crit is False
            return
    pytest.skip("Could not find a nat-1 in 100 seeds")


def test_bless_adds_d4():
    d = DiceEngine(seed="bless-test")
    r = d.roll("1d20+3", bless=True)
    assert r.bless_roll is not None
    assert 1 <= r.bless_roll <= 4
    base = r.kept if r.kept is not None else r.rolls[0]
    assert r.total == base + r.mod + r.bless_roll


def test_multi_die_expression():
    d = DiceEngine(seed="multi-die")
    r = d.roll("2d6+2")
    assert len(r.rolls) == 2
    assert all(1 <= v <= 6 for v in r.rolls)
    assert r.total == sum(r.rolls) + 2


def test_seed_position_increments():
    d = DiceEngine(seed="position-test")
    r1 = d.roll("1d20")
    r2 = d.roll("1d20")
    assert r2.seed_position == r1.seed_position + 1


def test_invalid_expression_raises():
    d = DiceEngine(seed="error-test")
    with pytest.raises(DiceError):
        d.roll("1d20+")


def test_roll_results_logged_to_jsonl(tmp_path):
    import json
    log_file = tmp_path / "dice_log.jsonl"
    d = DiceEngine(seed="log-test", log_path=log_file)
    d.roll("1d20+3")
    d.roll("2d6")
    lines = log_file.read_text().strip().split("\n")
    assert len(lines) == 2
    entry = json.loads(lines[0])
    assert "expression" in entry
    assert "total" in entry
    assert "seed_position" in entry


def test_roll_result_has_log_stub_fields():
    d = DiceEngine(seed="stub-test")
    r = d.roll("1d20", scene_id=3, beat_index=1, log_stub="STUB_ABC")
    assert r.scene_id == 3
    assert r.beat_index == 1
    assert r.log_stub == "STUB_ABC"


def test_roll_result_log_stub_defaults_to_none():
    d = DiceEngine(seed="stub-default")
    r = d.roll("1d20")
    assert r.scene_id is None
    assert r.log_stub is None
