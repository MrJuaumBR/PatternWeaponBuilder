from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import yaml

from .craft_loader import Pattern
from .material_loader import Material, MaterialType, CategoryType

VALID_ITEM_TYPES = {"tool", "weapon", "shield", "armor", "ingot"}
VALID_STATS = {"durability", "attack", "defense"}


@dataclass(frozen=True)
class Part:
    id: str
    material_amount: int
    weight: float
    role: str
    allowed_material_types: tuple[MaterialType, ...]
    allowed_material_categories: tuple[CategoryType, ...]

    def accepts(self, material: Material) -> bool:
        return (material.type in self.allowed_material_types and
                material.category in self.allowed_material_categories)


@dataclass(frozen=True)
class PatternDefinition:
    id: Pattern
    item_type: str
    base_stats: dict[str, float]
    parts: list[Part]


class PartLoader:
    def __init__(self, metadata_path: Path | str,
                 texture_ids: Iterable[str] | None = None,
                 material_types: Iterable[MaterialType] | None = None,
                 material_categories: Iterable[CategoryType] | None = None):
        self.metadata_file = Path(metadata_path)
        self._texture_ids = set(texture_ids) if texture_ids is not None else None
        self._material_types = set(material_types) if material_types is not None else set(MaterialType)
        self._material_categories = set(material_categories) if material_categories is not None else set(CategoryType)
        self.patterns: list[PatternDefinition] = []
        self.by_id: dict[Pattern, PatternDefinition] = {}
        self.load_metadata()

    def load_metadata(self) -> None:
        if not self.metadata_file.exists():
            raise FileNotFoundError(f"Metadata file {self.metadata_file} does not exist.")
        with self.metadata_file.open("r", encoding="utf-8") as stream:
            metadata = yaml.safe_load(stream) or {}
        rows = metadata.get("patterns")
        if not isinstance(rows, list) or not rows:
            raise ValueError("Part metadata must contain a non-empty 'patterns' list.")
        loaded: list[PatternDefinition] = []
        seen: set[Pattern] = set()
        for index, row in enumerate(rows):
            where = f"{self.metadata_file}:patterns[{index}]"
            if not isinstance(row, dict):
                raise ValueError(f"{where} must be a mapping.")
            for key in ("id", "parts", "item_type", "base_stats"):
                if key not in row:
                    raise ValueError(f"{where} is missing required field '{key}'.")
            try:
                pattern_id = Pattern(str(row["id"]).lower())
            except ValueError as exc:
                raise ValueError(f"Unknown pattern id '{row['id']}' in {where}.") from exc
            if pattern_id in seen:
                raise ValueError(f"Duplicate pattern id '{pattern_id.value}'.")
            seen.add(pattern_id)
            item_type = str(row["item_type"]).lower()
            if item_type not in VALID_ITEM_TYPES:
                raise ValueError(f"{where}.item_type must be one of {sorted(VALID_ITEM_TYPES)}.")
            base_stats = row["base_stats"]
            if not isinstance(base_stats, dict) or not base_stats:
                raise ValueError(f"{where}.base_stats must be a non-empty mapping.")
            unknown_stats = set(base_stats) - VALID_STATS
            if unknown_stats:
                raise ValueError(f"{where} has unknown base stats: {', '.join(sorted(unknown_stats))}.")
            normalized_stats = {str(k): float(v) for k, v in base_stats.items()}
            if any(value < 0 for value in normalized_stats.values()):
                raise ValueError(f"{where}.base_stats values cannot be negative.")
            if item_type not in {"shield", "armor"} and "defense" in normalized_stats:
                raise ValueError(f"{where}: defense is only valid for shields and armor.")
            if item_type in {"shield", "armor"} and "defense" not in normalized_stats:
                raise ValueError(f"{where}: {item_type} must define a defense base stat.")
            part_rows = row["parts"]
            if not isinstance(part_rows, list) or not part_rows:
                raise ValueError(f"{where}.parts must be a non-empty list.")
            parts: list[Part] = []
            total_weight = 0.0
            ids: set[str] = set()
            for part_index, part_row in enumerate(part_rows):
                part_where = f"{where}.parts[{part_index}]"
                if not isinstance(part_row, dict):
                    raise ValueError(f"{part_where} must be a mapping.")
                for key in ("id", "material_amount", "weight", "role", "allowed_material_types", "allowed_material_categories"):
                    if key not in part_row:
                        raise ValueError(f"{part_where} is missing required field '{key}'.")
                part_id = str(part_row["id"])
                if part_id in ids:
                    raise ValueError(f"Duplicate part '{part_id}' within pattern '{pattern_id.value}'.")
                ids.add(part_id)
                if self._texture_ids is not None and part_id not in self._texture_ids:
                    raise ValueError(f"{part_where}.id '{part_id}' has no matching texture region.")
                amount = int(part_row["material_amount"])
                weight = float(part_row["weight"])
                if amount <= 0 or not 0.0 <= weight <= 1.0:
                    raise ValueError(f"{part_where} needs a positive material_amount and weight in [0, 1].")
                total_weight += weight
                try:
                    allowed_types = tuple(MaterialType(str(v).lower()) for v in part_row["allowed_material_types"])
                    allowed_categories = tuple(CategoryType(str(v).lower()) for v in part_row["allowed_material_categories"])
                except ValueError as exc:
                    raise ValueError(f"{part_where} contains an unknown material type/category.") from exc
                if not allowed_types or not allowed_categories:
                    raise ValueError(f"{part_where} compatibility lists cannot be empty.")
                if not set(allowed_types).issubset(self._material_types) or not set(allowed_categories).issubset(self._material_categories):
                    raise ValueError(f"{part_where} references an unavailable material type/category.")
                parts.append(Part(part_id, amount, weight, str(part_row["role"]), allowed_types, allowed_categories))
            if abs(total_weight - 1.0) > 1e-6:
                raise ValueError(f"{where}.parts weights must sum to 1.0 (got {total_weight:.6f}).")
            loaded.append(PatternDefinition(pattern_id, item_type, normalized_stats, parts))
        self.patterns = loaded
        self.by_id = {pattern.id: pattern for pattern in loaded}

    def get_pattern(self, pattern: Pattern | str) -> PatternDefinition:
        key = pattern if isinstance(pattern, Pattern) else Pattern(str(pattern).lower())
        try:
            return self.by_id[key]
        except KeyError as exc:
            raise KeyError(f"No parts definition for pattern '{key.value}'.") from exc

    @property
    def pattern_count(self) -> int:
        return len(self.patterns)

    @property
    def parts_count(self) -> int:
        return sum(len(pattern.parts) for pattern in self.patterns)
