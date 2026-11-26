from __future__ import annotations

import random
import unittest
from dataclasses import replace
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))

from data.scripts.item_builder import build_item, random_build
from data.scripts.loader import CategoryType, Loader, MaterialType

ROOT = Path(__file__).resolve().parent.parent


class RandomBuildTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.loader = Loader(ROOT)
        cls.materials = cls.loader.Material.materials
        cls.rng = random.Random(20261126)

    def test_random_builds_use_compatible_materials_and_valid_stats(self) -> None:
        for _ in range(250):
            item = random_build(self.loader.Crafts.crafts, self.loader.Parts, self.materials, self.rng)
            self.assertEqual(sum(part.part.weight for part in item.parts), 1.0)
            for built_part in item.parts:
                self.assertTrue(built_part.part.accepts(built_part.material))
                self.assertGreater(built_part.part.material_amount, 0)
                # Wires and unrefined ores are not finished structural parts.
                if built_part.part.role in {"head", "blade", "counterweight"}:
                    self.assertNotIn(built_part.material.category, {CategoryType.WIRES, CategoryType.ORES})
            for stat, value in item.stats.items():
                self.assertIn(stat, item.definition.base_stats)
                self.assertGreaterEqual(value, 0)
                self.assertLessEqual(value, item.definition.base_stats[stat] * 2)
            if item.definition.item_type not in {"shield", "armor"}:
                self.assertNotIn("defense", item.stats)

    def test_material_modifier_scales_base_as_percentage(self) -> None:
        iron = next(material for material in self.materials if material.id == "iron_bar")
        modified_iron = replace(iron, durability=0.5, damage=0.5)
        definition = self.loader.Parts.get_pattern("pickaxe")
        metal_parts = [replace(part, allowed_material_types=(MaterialType.METAL,),
                               allowed_material_categories=(CategoryType.METALS,))
                       for part in definition.parts]
        definition = replace(definition, parts=metal_parts)
        craft = next(craft for craft in self.loader.Crafts.crafts if craft.pattern.value == "pickaxe")
        item = build_item(craft, definition, [modified_iron], random.Random(1))
        self.assertEqual(item.stats["durability"], 150.0)
        self.assertEqual(item.stats["attack"], 150.0)

    def test_defense_applies_only_when_pattern_is_defensive(self) -> None:
        steel = next(material for material in self.materials if material.id == "steel")
        reduced_defense_steel = replace(steel, defense=-0.2)
        base = self.loader.Parts.get_pattern("longsword")
        metal_parts = [replace(part, allowed_material_types=(MaterialType.ALLOY,),
                               allowed_material_categories=(CategoryType.ALLOYS,))
                       for part in base.parts]
        armor_definition = replace(base, item_type="armor", base_stats={"durability": 100, "defense": 100}, parts=metal_parts)
        craft = next(craft for craft in self.loader.Crafts.crafts if craft.pattern.value == "longsword")
        item = build_item(craft, armor_definition, [reduced_defense_steel], random.Random(2))
        self.assertEqual(item.stats["defense"], 80.0)

    def test_wire_is_not_compatible_with_axe_heads_or_blades(self) -> None:
        copper_wire = next(material for material in self.materials if material.id == "copper_wire")
        iron_ore = next(material for material in self.materials if material.id == "iron_ore")
        for pattern in self.loader.Parts.patterns:
            for part in pattern.parts:
                if part.role in {"head", "blade", "counterweight", "joint", "hilt"}:
                    self.assertFalse(part.accepts(copper_wire), f"{copper_wire.id} incorrectly accepted by {part.id}")
                    self.assertFalse(part.accepts(iron_ore), f"{iron_ore.id} incorrectly accepted by {part.id}")

    def test_all_readme_metadata_attributes_are_loaded(self) -> None:
        material = next(material for material in self.materials if material.id == "steel")
        self.assertEqual(material.name, "Steel")
        for attribute in ("description", "durability", "damage", "defense", "color", "type", "category",
                          "roughness", "weight", "hardness", "elasticity", "thermal_conductivity",
                          "melting_point", "magic_affinity", "traits"):
            self.assertTrue(hasattr(material, attribute), attribute)
        trait = self.loader.Traits.by_id["sharp"]
        self.assertEqual(trait.type.value, "passive")
        self.assertTrue(trait.effects)
        texture = self.loader.Texture.textures[0]
        self.assertTrue(self.loader.Texture.filename)
        self.assertTrue(all(hasattr(texture, key) for key in ("id", "name", "x", "y", "w", "h", "type", "layer_priority")))
        craft = self.loader.Crafts.crafts[0]
        self.assertEqual(craft.id, craft.name)
        self.assertTrue(self.loader.Parts.get_pattern(craft.pattern).parts)


if __name__ == "__main__":
    unittest.main(verbosity=2)
