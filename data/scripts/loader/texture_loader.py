from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path

import yaml


@dataclass(frozen=True)
class TextureRegion:
    id: str
    name: str
    x: int
    y: int
    w: int
    h: int
    type: str
    layer_priority: int


class TextureLoader:
    def __init__(self, metadata_file: Path | str):
        self.metadata_file = Path(metadata_file)
        self.filename: str = ""
        self._texture_path: Path | None = None
        self.textures: list[TextureRegion] = []
        self.load_metadata()

    @property
    def _textures(self) -> list[dict]:
        """Legacy mapping view; new code should use `textures` and TextureRegion."""
        return [asdict(texture) for texture in self.textures]

    def load_metadata(self) -> None:
        if not self.metadata_file.exists():
            raise FileNotFoundError(f"Metadata file {self.metadata_file} does not exist.")
        with self.metadata_file.open("r", encoding="utf-8") as stream:
            metadata = yaml.safe_load(stream) or {}
        filename = metadata.get("filename")
        if not isinstance(filename, str) or not filename:
            raise ValueError("Texture metadata must contain a non-empty 'filename'.")
        self.filename = filename
        self._texture_path = self.metadata_file.parent / "assets" / Path(filename)
        if not self._texture_path.exists():
            raise FileNotFoundError(f"Texture file {self._texture_path} does not exist.")
        rows = metadata.get("textures")
        if not isinstance(rows, list) or not rows:
            raise ValueError("Texture metadata must contain a non-empty 'textures' list.")
        loaded: list[TextureRegion] = []
        seen: set[str] = set()
        for index, row in enumerate(rows):
            where = f"{self.metadata_file}:textures[{index}]"
            if not isinstance(row, dict):
                raise ValueError(f"{where} must be a mapping.")
            required = ("id", "name", "x", "y", "w", "h", "type", "layer_priority")
            missing = [key for key in required if key not in row]
            if missing:
                raise ValueError(f"{where} is missing required fields: {', '.join(missing)}")
            region_id = str(row["id"])
            if region_id in seen:
                raise ValueError(f"Duplicate texture region id '{region_id}'.")
            seen.add(region_id)
            x, y, w, h = (int(row[key]) for key in ("x", "y", "w", "h"))
            if x < 0 or y < 0 or w <= 0 or h <= 0:
                raise ValueError(f"{where} coordinates must be non-negative and dimensions positive.")
            loaded.append(TextureRegion(region_id, str(row["name"]), x, y, w, h,
                                       str(row["type"]), int(row["layer_priority"])))
        self.textures = loaded

    @property
    def texture_count(self) -> int:
        return len(self.textures)
