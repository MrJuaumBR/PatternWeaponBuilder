from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import Path

import yaml


class Pattern(Enum):
    PICKAXE = "pickaxe"
    AXE = "axe"
    SHORTSWORD = "shortsword"
    LONGSWORD = "longsword"
    SHOVEL = "shovel"
    INGOT = "ingot"


class Station(Enum):
    FORGE = "forge"
    TABLE = "table"
    ANVIL = "anvil"


@dataclass(frozen=True)
class Craft:
    name: str
    pattern: Pattern
    station: Station

    @property
    def id(self) -> str:
        """Backward-compatible alias for the README's `name` attribute."""
        return self.name


class CraftLoader:
    def __init__(self, metadata_path: Path | str):
        self.metadata_file = Path(metadata_path)
        self.crafts: list[Craft] = []
        self.load_metadata()

    def load_metadata(self) -> None:
        if not self.metadata_file.exists():
            raise FileNotFoundError(f"Metadata file {self.metadata_file} does not exist.")
        with self.metadata_file.open("r", encoding="utf-8") as stream:
            metadata = yaml.safe_load(stream) or {}
        rows = metadata.get("crafts")
        if not isinstance(rows, list) or not rows:
            raise ValueError("Craft metadata must contain a non-empty 'crafts' list.")
        loaded: list[Craft] = []
        seen: set[str] = set()
        for index, row in enumerate(rows):
            where = f"{self.metadata_file}:crafts[{index}]"
            if not isinstance(row, dict):
                raise ValueError(f"{where} must be a mapping.")
            missing = [key for key in ("name", "pattern", "station") if key not in row]
            if missing:
                raise ValueError(f"{where} is missing required fields: {', '.join(missing)}")
            name = str(row["name"])
            if name in seen:
                raise ValueError(f"Duplicate craft name '{name}' in {self.metadata_file}.")
            seen.add(name)
            try:
                loaded.append(Craft(name, Pattern(str(row["pattern"]).lower()), Station(str(row["station"]).lower())))
            except ValueError as exc:
                raise ValueError(f"Invalid pattern or station in {where}: {exc}") from exc
        self.crafts = loaded

    @property
    def crafts_count(self) -> int:
        return len(self.crafts)
