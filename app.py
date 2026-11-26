__GAME_NAME__       = 'Pattern Weapon Builder'
__GAME_VERSION__    = 'v0.1'


# Building Metadata, Crafts, Patterns, Materials, Traits and Textures
from data.scripts.loader import Loader as DataLoader
Loader = DataLoader()

print(
    "Loaded metadata successfully:\n"
    f"Textures: {Loader.Texture.texture_count}\n"
    f"Crafts: {Loader.Crafts.crafts_count}\n"
    f"Materials: {Loader.Material.materials_count}\n"
    f"Traits: {Loader.Traits.traits_count}\n"
    f"Patterns: {Loader.Parts.pattern_count} ({Loader.Parts.parts_count} parts)"
)

from lunaengine import LunaEngine
from lunaengine.core import Scene
from lunaengine.ui import *


class _game_scene(Scene):
    def __init__(self, engine):
        super().__init__(engine=engine)
        self.ui_setup()

    def ui_setup(self):
        self.add_ui_element(TextLabel(32, 32, 'Build Your Weapon', 72))
        self.add_ui_element(TextLabel(self.WIDTH - 8, self.HEIGHT - 6, __GAME_VERSION__, 16, pivot=(1.0, 1.0)))
        self.tabs: Tabination = self.add_ui_element(
            Tabination(self.WIDTH // 2, self.HEIGHT // 2 + 40, self.WIDTH * 0.8, self.HEIGHT * 0.85, 26, pivot=(0.5, 0.5))
        )
        self.tabs.add_tab('Info')


if __name__ == '__main__':
    engine = LunaEngine(__GAME_NAME__, 1280, 720, False)
    engine.add_scene('game', _game_scene)
    engine.set_scene('game')
    engine.run()
