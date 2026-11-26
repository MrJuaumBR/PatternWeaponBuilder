from __future__ import annotations

import re
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any

import yaml

try:
    from lunaengine.backend.types import Color
except ImportError:  # Let metadata validation and stat tests run without the game runtime installed.
    @dataclass(frozen=True)
    class Color:  # type: ignore[no-redef]
        hex_value: str

        @classmethod
        def from_hex(cls, value: str) -> "Color":
            return cls(value)

        def to_rgb_tuple(self) -> tuple[int, int, int]:
            value = self.hex_value.lstrip("#")
            return tuple(int(value[i:i + 2], 16) for i in (0, 2, 4))  # type: ignore[return-value]

        def toHex(self) -> str:
            return self.hex_value


class MaterialType(Enum):
    NATURAL = "natural"
    MISC = "misc"
    METAL = "metal"
    CHEMICAL = "chemical"
    ALLOY = "alloy"
    GEM = "gem"


class CategoryType(Enum):
    NATURAL = "natural"
    ORES = "ores"
    METALS = "metals"
    CHEMICALS = "chemicals"
    ALLOYS = "alloys"
    GEMS = "gems"
    WIRES = "wires"


@dataclass(frozen=True)
class Material:
    id: str
    name: str
    description: str
    durability: float
    damage: float
    defense: float
    color: Color
    type: MaterialType
    category: CategoryType
    roughness: float
    weight: float
    hardness: float
    elasticity: float
    thermal_conductivity: float
    melting_point: int
    magic_affinity: float
    traits: list[str]


class MaterialLoader:
    def __init__(self, metadata_path: Path | str):
        self.metadata_file = Path(metadata_path)
        self.materials: list[Material] = []
        self.load_metadata()

    def load_metadata(self) -> None:
        if not self.metadata_file.exists():
            raise FileNotFoundError(f"Metadata file {self.metadata_file} does not exist.")
        with self.metadata_file.open("r", encoding="utf-8") as stream:
            metadata = yaml.safe_load(stream) or {}
        rows = metadata.get("materials")
        if not isinstance(rows, list) or not rows:
            raise ValueError("Materials metadata must contain a non-empty 'materials' list.")

        loaded: list[Material] = []
        seen: set[str] = set()
        for index, row in enumerate(rows):
            where = f"{self.metadata_file}:materials[{index}]"
            if not isinstance(row, dict):
                raise ValueError(f"{where} must be a mapping.")
            required = ("id", "name", "description", "durability", "damage", "defense", "color", "type", "category")
            missing = [key for key in required if key not in row]
            if missing:
                raise ValueError(f"{where} is missing required fields: {', '.join(missing)}")
            material_id = str(row["id"])
            if material_id in seen:
                raise ValueError(f"Duplicate material id '{material_id}' in {self.metadata_file}.")
            seen.add(material_id)

            modifiers = {key: float(row[key]) for key in ("durability", "damage", "defense")}
            for key, value in modifiers.items():
                if not -1.0 <= value <= 1.0:
                    raise ValueError(f"{where}.{key} must be between -1.0 and 1.0.")
            physical = {
                key: float(row.get(key, default))
                for key, default in (("roughness", 0.5), ("weight", 0.5), ("hardness", 0.5),
                                     ("elasticity", 0.5), ("thermal_conductivity", 0.5), ("magic_affinity", 0.0))
            }
            for key, value in physical.items():
                if not 0.0 <= value <= 1.0:
                    raise ValueError(f"{where}.{key} must be between 0.0 and 1.0.")
            color_hex = str(row["color"])
            if not re.fullmatch(r"#[0-9a-fA-F]{6}", color_hex):
                raise ValueError(f"{where}.color must use #RRGGBB format.")
            traits = row.get("traits", [])
            if not isinstance(traits, list) or any(not isinstance(t, str) for t in traits):
                raise ValueError(f"{where}.traits must be a list of trait ids.")
            melting_point = int(row.get("melting_point", -1))
            loaded.append(Material(
                id=material_id,
                name=str(row["name"]),
                description=str(row["description"]),
                durability=modifiers["durability"],
                damage=modifiers["damage"],
                defense=modifiers["defense"],
                color=Color.from_hex(color_hex),
                type=MaterialType(str(row["type"]).lower()),
                category=CategoryType(str(row["category"]).lower()),
                roughness=physical["roughness"],
                weight=physical["weight"],
                hardness=physical["hardness"],
                elasticity=physical["elasticity"],
                thermal_conductivity=physical["thermal_conductivity"],
                melting_point=melting_point,
                magic_affinity=physical["magic_affinity"],
                traits=list(traits),
            ))
        self.materials = loaded

    @property
    def materials_count(self) -> int:
        return len(self.materials)
