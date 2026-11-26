# PatternWeaponBuilder/tests/render_random_tool.py
"""
Test file for rendering a random tool from the loaded metadata.

Loads everything through the project ``Loader`` (``data/scripts/loader``),
picks a random craft and a random material for each of its parts, tints each
part sprite with the material color, and stacks the parts on a single
32x32 canvas — parts are layered (z-ordered) on top of each other via
``layer_priority`` in ``texture.yaml``.

Output:
    tests/output/test_render_{year}-{month}-{day}_{hour}-{minute}-{seconds}.png
    e.g. tests/output/test_render_2026-11-26_14-32-45.png
"""

from __future__ import annotations

import sys
import random
import datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Make the project root importable so `data.scripts.loader` and `lunaengine`
# resolve when running `python tests/render_random_tool.py` directly.
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import pygame
import yaml

from data.scripts.loader import Loader as DataLoader
from lunaengine.backend.types import Color
from lunaengine.graphics.spritesheet import SpriteSheet


# Every part sprite is authored on a 32x32 tile and stacked at the same origin.
CANVAS_SIZE = (32, 32)
PART_ORIGIN = (0, 0)


def load_parts(path: Path) -> dict[str, list[dict]]:
    """Load `parts.yaml` and return `{pattern_id: [part, ...]}`."""
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    patterns = data.get("patterns")
    if not patterns:
        raise ValueError(f"{path} has no 'patterns' key")

    return {p["id"]: p["parts"] for p in patterns}


def tinted_sprite(
    sheet: SpriteSheet,
    region: tuple[int, int, int, int],
    material,
) -> pygame.Surface:
    """Extract a sprite from the sheet and tint it with the material color."""
    sprite = sheet.get_sprite_at_rect(pygame.Rect(*region))

    color: Color | None = material.color
    tint_rgb = color.to_rgb_tuple() if color else (255, 255, 255)

    return SpriteSheet.tint(
        sprite,
        tint_rgb,
        intensity=0.8,
        blend_mode="multiply",
    )


def render_random_tool(
    output_dir: Path | None = None,
    index: int = 0,
) -> Path:
    """Render one random tool and return the output path."""
    pygame.init()
    pygame.display.set_mode((1, 1), pygame.HIDDEN)

    Loader = DataLoader(PROJECT_ROOT)

    materials = Loader.Material.materials
    crafts = Loader.Crafts.crafts

    sheet_path = Loader.Texture._texture_path

    texture_regions: dict[str, tuple[tuple[int, int, int, int], int]] = {
        t["id"]: ((t["x"], t["y"], t["w"], t["h"]), int(t.get("layer_priority", 0)))
        for t in Loader.Texture._textures
    }

    pattern_parts = load_parts(PROJECT_ROOT / "data" / "parts.yaml")

    craft = random.choice(crafts)
    pattern = craft.pattern.value

    parts = pattern_parts.get(pattern)
    if not parts:
        raise ValueError(f"No parts defined for pattern '{pattern}'")

    parts = sorted(
        parts,
        key=lambda p: texture_regions.get(p["id"], ((0, 0, 0, 0), 0))[1],
        reverse=True,
    )

    sheet = SpriteSheet(sheet_path)
    canvas = pygame.Surface(CANVAS_SIZE, pygame.SRCALPHA)

    print(f"[info] craft={craft.id} pattern={pattern}")
    for part in parts:
        part_id = part["id"]
        entry = texture_regions.get(part_id)
        if entry is None:
            print(f"[warn] no texture region for part '{part_id}', skipping")
            continue

        region, priority = entry
        material = random.choice(materials)
        sprite = tinted_sprite(sheet, region, material)

        canvas.blit(sprite, PART_ORIGIN)
        print(
            f"[info]   part={part_id:<15} "
            f"layer={priority:<3} "
            f"material={material.id:<12} "
            f"color={material.color.toHex() if material.color else 'N/A'}"
        )

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    out_dir = output_dir or (Path(__file__).resolve().parent / "output")
    out_dir.mkdir(parents=True, exist_ok=True)
    output_path = out_dir / f"test_render_{timestamp}_{index:03d}.png"

    pygame.image.save(canvas, str(output_path))
    pygame.quit()

    return output_path
if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description="Render one or more random tools.")
    parser.add_argument(
        "repeat_count",
        nargs="?",
        type=int,
        default=1,
        help="How many random renders to generate (default: 1).",
    )
    parser.add_argument(
        "-o", "--output-dir",
        type=Path,
        default=None,
        help="Override the output directory (default: tests/output).",
    )
    args = parser.parse_args()

    if args.repeat_count < 1:
        parser.error("repeat_count must be >= 1")

    for i in range(args.repeat_count):
        path = render_random_tool(output_dir=args.output_dir, index=i)
        print(f"[info] ({i + 1}/{args.repeat_count}) {path}")