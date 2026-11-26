from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any

import yaml


class TraitType(Enum):
    PASSIVE = "passive"
    ON_EVENT = "on_event"
    ON_USE = "on_use"
    ON_HIT = "on_hit"
    ON_MINE = "on_mine"
    ON_CRAFT = "on_craft"


@dataclass(frozen=True)
class Trait:
    id: str
    name: str
    description: str
    type: TraitType
    effects: list[dict[str, Any]]
    events: list[dict[str, Any]]


class TraitLoader:
    def __init__(self, metadata_path: Path | str):
        self.metadata_file = Path(metadata_path)
        self.traits: list[Trait] = []
        self.by_id: dict[str, Trait] = {}
        self.load_metadata()

    def load_metadata(self) -> None:
        if not self.metadata_file.exists():
            raise FileNotFoundError(f"Metadata file {self.metadata_file} does not exist.")
        with self.metadata_file.open("r", encoding="utf-8") as stream:
            metadata = yaml.safe_load(stream) or {}
        rows = metadata.get("traits")
        if not isinstance(rows, list) or not rows:
            raise ValueError("Trait metadata must contain a non-empty 'traits' list.")
        loaded: list[Trait] = []
        seen: set[str] = set()
        for index, row in enumerate(rows):
            where = f"{self.metadata_file}:traits[{index}]"
            if not isinstance(row, dict):
                raise ValueError(f"{where} must be a mapping.")
            required = ("id", "name", "description", "type")
            missing = [key for key in required if key not in row]
            if missing:
                raise ValueError(f"{where} is missing required fields: {', '.join(missing)}")
            trait_id = str(row["id"])
            if trait_id in seen:
                raise ValueError(f"Duplicate trait id '{trait_id}'.")
            seen.add(trait_id)
            try:
                trait_type = TraitType(str(row["type"]).lower())
            except ValueError as exc:
                raise ValueError(f"Unsupported trait type in {where}: {row['type']}") from exc
            effects = row.get("effects", [])
            events = row.get("events", [])
            if not isinstance(effects, list) or any(not isinstance(e, dict) for e in effects):
                raise ValueError(f"{where}.effects must be a list of mappings.")
            if not isinstance(events, list) or any(not isinstance(e, dict) for e in events):
                raise ValueError(f"{where}.events must be a list of mappings.")
            if trait_type is TraitType.PASSIVE and events:
                raise ValueError(f"{where} is passive and should not define event hooks.")
            if trait_type is not TraitType.PASSIVE and not events and not effects:
                raise ValueError(f"{where} needs effects or event hooks.")
            loaded.append(Trait(trait_id, str(row["name"]), str(row["description"]), trait_type,
                                list(effects), list(events)))
        self.traits = loaded
        self.by_id = {trait.id: trait for trait in loaded}

    @property
    def traits_count(self) -> int:
        return len(self.traits)
