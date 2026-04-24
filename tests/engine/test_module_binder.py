"""Tests for module_binder.py"""
import re
import textwrap
from pathlib import Path

import pytest

from scripts.module_binder import (
    bind,
    _read,
    _split_h2,
    _extract_dcs,
    _last_blockquote,
    _stat_line,
    _parse_stat_blocks_from_encounter,
    _convert_arc,
    _dc_table,
    _strip_headers,
)


# ---------------------------------------------------------------------------
# Unit tests
# ---------------------------------------------------------------------------

def test_split_h2_basic():
    body = "preamble\n## Section A\ncontent A\n## Section B\ncontent B"
    secs = _split_h2(body)
    assert "Section A" in secs
    assert secs["Section A"].strip() == "content A"
    assert "Section B" in secs
    assert secs["Section B"].strip() == "content B"


def test_split_h2_preamble():
    body = "# H1 title\n\nsome preamble\n## First\ncontent"
    secs = _split_h2(body)
    assert "# H1 title" in secs["__pre__"]
    assert "First" in secs


def test_extract_dcs():
    features = textwrap.dedent("""\
        - **DC 12 Perception** to notice the warmth.
        - **DC 15 Athletics** to climb without the rope.
        - No roll needed for obvious things.
    """)
    rows = _extract_dcs(features, scene_num=2)
    dcs = [r["dc"] for r in rows]
    assert 12 in dcs
    assert 15 in dcs
    assert all(r["scene"] == 2 for r in rows)


def test_extract_dcs_no_dcs():
    assert _extract_dcs("No rolls needed here.", scene_num=1) == []


def test_last_blockquote_returns_last():
    text = textwrap.dedent("""\
        > First longer blockquote that has many words and goes on a bit.

        *(80 words — trim to:)*

        > Second shorter one.
    """)
    result = _last_blockquote(text)
    assert "Second shorter" in result
    assert "First longer" not in result


def test_last_blockquote_multiline():
    text = "> Line one.\n> Line two.\n\n*(50 words)*"
    result = _last_blockquote(text)
    assert "Line one" in result
    assert "Line two" in result


def test_stat_line_format():
    line = _stat_line("Grisk", ac=11, hp=12)
    assert "**Grisk —" in line
    assert "**AC** 11" in line
    assert "**HP** 12" in line


def test_stat_line_loader_parseable():
    """Verify the stat line matches loader.py's _parse_stat_blocks pattern."""
    from scripts.engine.loader import _parse_stat_blocks
    line = _stat_line("Grisk", ac=11, hp=12)
    # Wrap in a scene body
    body = f"### Scene 1 — Test\n\n> Read aloud.\n\n**Stat blocks:**\n\n{line}\n"
    blocks = _parse_stat_blocks(body)
    assert len(blocks) == 1
    assert blocks[0]["name"] == "Grisk"
    assert blocks[0]["ac"] == 11
    assert blocks[0]["hp"] == 12


def test_parse_stat_blocks_from_encounter():
    body = textwrap.dedent("""\
        ### Grisk
        *Gully dwarf. HP 12. AC 11. Speed 20 ft.*
        - **Attack:** Iron rod +3, 1d6+1.

        ### Torva
        *Gully dwarf. HP 10. AC 11. Speed 20 ft.*
    """)
    lines = _parse_stat_blocks_from_encounter(body)
    assert len(lines) == 2
    assert any("Grisk" in l and "AC** 11" in l and "HP** 12" in l for l in lines)
    assert any("Torva" in l and "HP** 10" in l for l in lines)


def test_convert_arc_basic():
    body = textwrap.dedent("""\
        # Mig

        Some description.

        ## Arc-Completion

        **Condition:** Party opens the door and Mig steps through.

        **The act:** She steps through without looking back.

        ## Behavior Matrix
    """)
    result = _convert_arc(body)
    assert "**The moment:**" in result
    assert "**The condition:**" in result
    assert "She steps through without looking back" in result
    assert "Party opens the door" in result


def test_convert_arc_uses_h4():
    """_convert_arc outputs #### Arc-Completion (H4) so it doesn't terminate the ## NPCs section."""
    body = textwrap.dedent("""\
        # Mig

        Description.

        ## Arc-Completion

        **Condition:** The door is opened and Mig steps through.

        **The act:** She crosses the threshold.

    """)
    converted = _convert_arc(body)
    assert "#### Arc-Completion" in converted
    assert "**The moment:** She crosses the threshold" in converted
    assert "**The condition:** The door is opened" in converted


def test_convert_arc_loader_parseable():
    """Verify converted arc (H4) is found by loader.py's _parse_npc_arc_completions."""
    from scripts.engine.loader import _parse_npc_arc_completions
    body = textwrap.dedent("""\
        # Mig

        Description.

        ## Arc-Completion

        **Condition:** The door is opened and Mig steps through.

        **The act:** She crosses the threshold.

    """)
    converted = _convert_arc(body)
    # Wrap in an NPCs section — the H4 Arc-Completion should not cut the ## NPCs section
    module_text = f"## NPCs\n\n### Mig\n\n{converted}\n\n## DM Cheatsheet\n"
    arcs = _parse_npc_arc_completions(module_text)
    assert "mig" in arcs, f"Expected 'mig' in arcs, got keys: {list(arcs.keys())}"
    assert "She crosses the threshold" in arcs["mig"]["arc_completion"]


def test_strip_headers_downgrades_h1_h2_h3():
    text = "## Type\nSome content.\n### Setup\nMore content.\n#### Keep\nNot changed."
    result = _strip_headers(text)
    assert "## Type" not in result
    assert "### Setup" not in result
    assert "**Type**" in result
    assert "**Setup**" in result
    assert "#### Keep" in result  # H4 and deeper are not stripped


def test_inline_encounter_strips_headers(tmp_path):
    """Encounter headers should not appear as H2 in compiled scene bodies."""
    from scripts.module_binder import _inline_encounter
    enc_dir = tmp_path / "encounters"
    enc_dir.mkdir()
    (enc_dir / "test-enc.md").write_text(
        "---\nadventure: test\n---\n## Type\nSocial.\n## Setup\nGrisk enters.", encoding="utf-8"
    )
    section = "See `encounters/test-enc.md`"
    result, _ = _inline_encounter(section, tmp_path)
    assert "## Type" not in result
    assert "## Setup" not in result
    assert "**Type**" in result


def test_dc_table_format():
    rows = [
        {"dc": 12, "check": "Perception", "scene": 1, "consequence": "notice the warmth"},
        {"dc": 15, "check": "Athletics", "scene": 2, "consequence": "climb safely"},
    ]
    table = _dc_table(rows)
    assert "| DC |" in table
    assert "| 12 |" in table
    assert "| 15 |" in table
    # loader parses: r"\|\s*(\d+)\s*\|\s*([^|]+)\s*\|\s*(\d+)\s*\|\s*([^|]+)\s*\|"
    from scripts.engine.loader import _parse_dc_table
    # Wrap in cheatsheet context
    text = f"### Quick Reference — Key DCs (by scene)\n\n{table}\n\n## Next"
    parsed = _parse_dc_table(text)
    assert len(parsed) == 2
    assert parsed[0]["dc"] == 12
    assert parsed[1]["dc"] == 15


# ---------------------------------------------------------------------------
# Integration test: bind produces loader-parseable output
# ---------------------------------------------------------------------------

def test_bind_produces_loadable_module(tmp_path):
    """Create a minimal adventure directory and verify bind() output loads cleanly."""
    adv_slug = "9999-test-adventure"
    adv_dir = tmp_path / "adventures" / adv_slug
    (adv_dir / "rooms").mkdir(parents=True)
    (adv_dir / "treasures").mkdir()
    (adv_dir / "encounters").mkdir()
    (adv_dir / "npcs").mkdir()

    # Minimal premise.md
    (adv_dir / "premise.md").write_text(textwrap.dedent("""\
        ---
        adventure: 9999-test-adventure
        tier: 1
        party: the-witnesses (4 characters, level 3)
        author: test
        created: 2026-04-21
        ---
        # Premise — Test Adventure

        **Logline:** A test adventure for the module binder.

        ## Setting

        A test setting.

        ## Hook

        A test hook.
    """), encoding="utf-8")

    # Minimal map.md
    (adv_dir / "rooms" / "map.md").write_text(textwrap.dedent("""\
        ---
        adventure: 9999-test-adventure
        document: map
        ---
        # Map

        ```
        [R1] -- [R2]
        ```
    """), encoding="utf-8")

    # Room 01
    (adv_dir / "rooms" / "01-entry.md").write_text(textwrap.dedent("""\
        ---
        adventure: 9999-test-adventure
        room: 01
        ---
        # Room 01 — Entry Hall

        ## Read-aloud

        > A short read-aloud for room one.

        ## Features

        - **DC 12 Perception** to notice the door.

        ## Encounter

        None.

        ## Treasure

        None.

        ## Connections

        - **East:** Room 2

        ## GM Notes

        This is a test room.
    """), encoding="utf-8")

    # Room 02
    (adv_dir / "rooms" / "02-inner.md").write_text(textwrap.dedent("""\
        ---
        adventure: 9999-test-adventure
        room: 02
        ---
        # Room 02 — Inner Chamber

        ## Read-aloud

        > The second room read-aloud text.

        ## Features

        - **DC 14 Investigation** to find the chest.

        ## Encounter

        None.

        ## Treasure

        None.

        ## Connections

        - **West:** Room 1

        ## GM Notes

        Test room two.
    """), encoding="utf-8")

    # Monkeypatch _REPO_ROOT
    import scripts.module_binder as mb
    original_root = mb._REPO_ROOT
    mb._REPO_ROOT = tmp_path

    try:
        out = bind(adv_slug, force=True)
    finally:
        mb._REPO_ROOT = original_root

    assert out.exists()
    text = out.read_text(encoding="utf-8")

    # Frontmatter present
    assert "adventure: 9999-test-adventure" in text

    # Scenes present
    assert "### Scene 1 — Entry Hall" in text
    assert "### Scene 2 — Inner Chamber" in text

    # Read-alouds present as blockquotes
    assert "> A short read-aloud" in text
    assert "> The second room read-aloud" in text

    # Now verify loader can parse it
    from scripts.engine.loader import load_adventure
    adventure = load_adventure(out)
    assert adventure.slug == "9999-test-adventure"
    assert len(adventure.scenes) == 2
    assert adventure.scenes[0].name == "Entry Hall"
    assert adventure.scenes[1].name == "Inner Chamber"
    assert "short read-aloud" in adventure.scenes[0].read_aloud
    assert len(adventure.dc_table) == 2
