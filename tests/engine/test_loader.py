import pytest
from pathlib import Path
from scripts.engine.loader import load_adventure, load_party, Adventure, Scene, PC, LoadError

FIXTURES = Path("tests/fixtures")


def test_load_adventure_returns_adventure_object():
    adv = load_adventure(FIXTURES / "mini_module.md")
    assert isinstance(adv, Adventure)


def test_load_adventure_two_scenes():
    adv = load_adventure(FIXTURES / "mini_module.md")
    assert len(adv.scenes) == 2


def test_load_adventure_scene_names():
    adv = load_adventure(FIXTURES / "mini_module.md")
    assert adv.scenes[0].name == "The Arrival"
    assert adv.scenes[1].name == "The Vault"


def test_load_adventure_scene_read_aloud():
    adv = load_adventure(FIXTURES / "mini_module.md")
    assert "testing ground" in adv.scenes[0].read_aloud


def test_load_adventure_dc_table():
    adv = load_adventure(FIXTURES / "mini_module.md")
    assert len(adv.dc_table) == 2
    dcs = {row["dc"] for row in adv.dc_table}
    assert 10 in dcs
    assert 15 in dcs


def test_load_adventure_stat_block_in_scene():
    adv = load_adventure(FIXTURES / "mini_module.md")
    s2 = adv.scenes[1]
    assert len(s2.stat_blocks) == 1
    guard = s2.stat_blocks[0]
    assert guard["name"] == "Test Guard"
    assert guard["ac"] == 14
    assert guard["hp"] == 22


def test_load_adventure_missing_file_raises():
    with pytest.raises(LoadError, match="not found"):
        load_adventure(Path("nonexistent/module.md"))


def test_load_party_returns_pc_list():
    pcs = load_party(FIXTURES)
    assert len(pcs) == 1


def test_load_party_pc_name():
    pcs = load_party(FIXTURES)
    assert pcs[0].slug == "test-fighter"


def test_load_party_pc_stat_block():
    pcs = load_party(FIXTURES)
    pc = pcs[0]
    assert pc.ac == 16
    assert pc.hp == 28
    assert pc.hp_max == 28


def test_load_party_heuristics_decision_order():
    pcs = load_party(FIXTURES)
    pc = pcs[0]
    assert len(pc.heuristics["decision_order"]) == 2
    assert pc.heuristics["decision_order"][0]["key"] == "survival"


def test_load_party_heuristics_doubt_die():
    pcs = load_party(FIXTURES)
    pc = pcs[0]
    dd = pc.heuristics["doubt_die"]
    assert dd["1-3"] == "attack"
    assert dd["4-6"] == "defend"


def test_load_party_missing_heuristics_raises():
    import tempfile, textwrap
    content = textwrap.dedent("""\
        ---
        party: test
        pc: bad-pc
        class: fighter
        level: 1
        ---
        # Bad PC
    """)
    with tempfile.NamedTemporaryFile(suffix=".md", mode="w", delete=False, encoding="utf-8") as f:
        f.write(content)
        tmppath = Path(f.name)
    with pytest.raises(LoadError, match="No heuristics block"):
        load_party(tmppath.parent)
    tmppath.unlink()
