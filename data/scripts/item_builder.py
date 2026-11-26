from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Iterable

from .loader.craft_loader import Craft
from .loader.material_loader import Material
from .loader.part_loader import Part, PatternDefinition


@dataclass(frozen=True)
class BuiltPart:
    part: Part
    material: Material


@dataclass(frozen=True)
class BuiltItem:
    craft: Craft
    definition: PatternDefinition
    parts: list[BuiltPart]
    stats: dict[str, float]


def compatible_materials(part: Part, materials: Iterable[Material]) -> list[Material]:
    return [material for material in materials if part.accepts(material)]


def modifier_for_stat(material: Material, stat: str) -> float:
    """Resolve a material modifier for an item stat (attack is backed by README `damage`)."""
    return float(material.damage if stat == "attack" else getattr(material, stat))


def build_item(craft: Craft, definition: PatternDefinition,
               materials: Iterable[Material], rng: random.Random | None = None) -> BuiltItem:
    rng = rng or random.Random()
    material_list = list(materials)
    built_parts: list[BuiltPart] = []
    for part in definition.parts:
        eligible = compatible_materials(part, material_list)
        if not eligible:
            raise ValueError(f"No compatible materials for part '{part.id}' in pattern '{definition.id.value}'.")
        built_parts.append(BuiltPart(part, rng.choice(eligible)))

    stats: dict[str, float] = {}
    for stat, base_value in definition.base_stats.items():
        modifier = sum(item.part.weight * modifier_for_stat(item.material, stat) for item in built_parts)
        stats[stat] = round(base_value * (1.0 + modifier), 2)
    return BuiltItem(craft, definition, built_parts, stats)


def random_build(crafts: Iterable[Craft], patterns: dict, materials: Iterable[Material],
                 rng: random.Random | None = None) -> BuiltItem:
    rng = rng or random.Random()
    craft_list = list(crafts)
    if not craft_list:
        raise ValueError("Cannot build an item without any crafts.")
    craft = rng.choice(craft_list)
    definition = patterns.get_pattern(craft.pattern)
    return build_item(craft, definition, materials, rng)
