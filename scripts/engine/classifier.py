from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Event:
    type: str
    pc_slug: str | None
    involves_grief_paragraph: bool
    is_option_c: bool
    is_hint_delivery: bool
    is_read_aloud: bool
    has_npc_dialogue: bool
    is_key_loot: bool
    scene_context: dict


_PYTHON_TYPES = frozenset({
    "dice_roll", "hp_delta", "resource_use", "doubt_die",
    "signature_move", "condition_apply", "scene_advance",
})

_LLM_TYPES = frozenset({
    "read_aloud", "option_c", "dialogue", "memory_fragment",
    "atmospheric_chain", "hint_delivery", "loot_narration",
})


def classify(event: Event) -> str:
    """
    Foundational rule: false-LLM-required is cheap (one extra prompt).
    False-Python-resolved corrupts voice. When in doubt, route to LLM.
    """
    if event.involves_grief_paragraph:
        return "llm"
    if event.is_option_c:
        return "llm"
    if event.is_hint_delivery:
        return "llm"
    if event.is_read_aloud:
        return "llm"
    if event.has_npc_dialogue:
        return "llm"
    if event.is_key_loot:
        return "llm"
    if event.type in _PYTHON_TYPES:
        return "python"
    if event.type in _LLM_TYPES:
        return "llm"
    return "llm"
