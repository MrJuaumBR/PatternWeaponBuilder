"""Typed loaders for the project's documented YAML metadata."""

from pathlib import Path
from typing import Optional, Union

from .craft_loader import Craft, CraftLoader, Pattern, Station
from .material_loader import Material, CategoryType, MaterialLoader, MaterialType
from .part_loader import Part, PartLoader, PatternDefinition
from .texture_loader import TextureLoader, TextureRegion
from .trait_loader import Trait, TraitLoader, TraitType


class Loader:
    def __init__(self, root_path: Optional[Union[Path, str]] = None):
        self.root_path = Path(root_path) if root_path else Path(__file__).parent.parent.parent.parent

        self._craft_loader = CraftLoader(self.root_path / "data" / "crafts.yaml")
        self._material_loader = MaterialLoader(self.root_path / "data" / "materials.yaml")
        self._texture_loader = TextureLoader(self.root_path / "data" / "texture.yaml")
        self._trait_loader = TraitLoader(self.root_path / "data" / "traits.yaml")
        self._part_loader = PartLoader(
            self.root_path / "data" / "parts.yaml",
            texture_ids=(texture.id for texture in self._texture_loader.textures),
            material_types=MaterialType,
            material_categories=CategoryType,
        )

        known_patterns = {pattern.id for pattern in self._part_loader.patterns}
        for craft in self._craft_loader.crafts:
            if craft.pattern not in known_patterns:
                raise ValueError(f"Craft '{craft.name}' references pattern '{craft.pattern.value}' with no parts definition.")
        known_traits = set(self._trait_loader.by_id)
        for material in self._material_loader.materials:
            unknown = set(material.traits) - known_traits
            if unknown:
                raise ValueError(f"Material '{material.id}' references unknown traits: {', '.join(sorted(unknown))}.")

    @property
    def Texture(self) -> TextureLoader:
        return self._texture_loader

    @property
    def Crafts(self) -> CraftLoader:
        return self._craft_loader

    @property
    def Material(self) -> MaterialLoader:
        return self._material_loader

    @property
    def Traits(self) -> TraitLoader:
        return self._trait_loader

    @property
    def Parts(self) -> PartLoader:
        return self._part_loader


__all__ = [
    "Loader", "Craft", "CraftLoader", "Pattern", "Station",
    "Material", "CategoryType", "MaterialLoader", "MaterialType",
    "Part", "PartLoader", "PatternDefinition", "TextureLoader", "TextureRegion",
    "Trait", "TraitLoader", "TraitType",
]
