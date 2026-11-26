"""
Loader Class for Metadata

- Crafts;
- Materials;
- Textures;
"""

from .craft_loader import Craft, CraftLoader, Pattern
from .material_loader import Material, CategoryType, MaterialLoader, MaterialType
from .texture_loader import TextureLoader
from typing import Optional, Union
from pathlib import Path
class Loader:
    def __init__(self, root_path:Optional[Union[Path, str]]=None):
        if root_path:
            self.root_path = Path(root_path)
        else:
            self.root_path = Path(__file__).parent.parent.parent.parent
        
        # Load Crafts
        self._craft_loader = CraftLoader(self.root_path / 'data' / 'crafts.yaml')
        
        # Load Materials
        self._material_loader = MaterialLoader(self.root_path / 'data' / 'materials.yaml')
        
        # Load Texture
        self._texture_loader = TextureLoader(self.root_path / 'data' / 'texture.yaml')
        
    @property
    def Texture(self) -> TextureLoader:
        return self._texture_loader
    
    @property
    def Crafts(self) -> CraftLoader:
        return self._craft_loader
    
    @property
    def Material(self) -> MaterialLoader:
        return self._material_loader
    
__all__ = [
    'Loader',
    'Craft', 'CraftLoader', 'Pattern',
    'Material', 'CategoryType', 'MaterialLoader', 'MaterialType',
    'TextureLoader'
]