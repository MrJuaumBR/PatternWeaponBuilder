
# Building Metadata, Crafts and Patterns
## Textures
from data.scripts.texture_loader import TextureLoader
Texture = TextureLoader("data/texture.yaml")

## Crafts
from data.scripts.craft_loader import CraftLoader, Craft, Pattern, Station
Crafts = CraftLoader("data/crafts.yaml")

print(f"Loaded successfully Textures and Crafts:\nTextures: {Texture.texture_count}\nCrafts: {Crafts.crafts_count}")