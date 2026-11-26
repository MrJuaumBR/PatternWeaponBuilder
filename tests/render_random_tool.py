"""Render a random compatible item and report its computed stats."""
from __future__ import annotations

import sys
import random
import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import pygame
from data.scripts.item_builder import random_build
from data.scripts.loader import Loader
from lunaengine.graphics.spritesheet import SpriteSheet

CANVAS_SIZE = (32, 32)
PART_ORIGIN = (0, 0)


def tinted_sprite(sheet: SpriteSheet, region: tuple[int, int, int, int], material) -> pygame.Surface:
    sprite = sheet.get_sprite_at_rect(pygame.Rect(*region))
    color = material.color
    tint_rgb = color.to_rgb_tuple() if color else (255, 255, 255)
    return SpriteSheet.tint(sprite, tint_rgb, intensity=0.8, blend_mode="multiply")


def render_random_tool(output_dir: Path | None = None, index: int = 0,
                       rng: random.Random | None = None) -> Path:
    pygame.init()
    pygame.display.set_mode((1, 1), pygame.HIDDEN)
    loader = Loader(PROJECT_ROOT)
    item = random_build(loader.Crafts.crafts, loader.Parts, loader.Material.materials, rng)
    texture_regions = {
        texture.id: ((texture.x, texture.y, texture.w, texture.h), texture.layer_priority)
        for texture in loader.Texture.textures
    }
    ordered_parts = sorted(item.parts, key=lambda part: texture_regions[part.part.id][1], reverse=True)
    sheet = SpriteSheet(loader.Texture._texture_path)
    canvas = pygame.Surface(CANVAS_SIZE, pygame.SRCALPHA)

    print(f"[item] {item.craft.name} ({item.definition.item_type}) / pattern={item.definition.id.value}")
    print("[stats] " + " | ".join(f"{name}={value:g}" for name, value in item.stats.items()))
    for built_part in ordered_parts:
        region, priority = texture_regions[built_part.part.id]
        canvas.blit(tinted_sprite(sheet, region, built_part.material), PART_ORIGIN)
        print(f"[part] {built_part.part.id:<15} layer={priority:<3} "
              f"material={built_part.material.id:<12} amount={built_part.part.material_amount}")

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    out_dir = output_dir or (Path(__file__).resolve().parent / "output")
    out_dir.mkdir(parents=True, exist_ok=True)
    output_path = out_dir / f"test_render_{timestamp}_{index:03d}.png"
    pygame.image.save(canvas, str(output_path))
    pygame.quit()
    return output_path


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description="Render one or more random compatible items and print their stats.")
    parser.add_argument("repeat_count", nargs="?", type=int, default=1, help="Number of random items (default: 1).")
    parser.add_argument("-o", "--output-dir", type=Path, default=None, help="Image output directory (default: tests/output).")
    args = parser.parse_args()
    if args.repeat_count < 1:
        parser.error("repeat_count must be >= 1")
    for i in range(args.repeat_count):
        print(f"[render] ({i + 1}/{args.repeat_count}) {render_random_tool(args.output_dir, i)}")
