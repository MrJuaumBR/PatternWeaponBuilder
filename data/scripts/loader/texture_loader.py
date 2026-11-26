import yaml
from lunaengine.graphics import SpriteSheet, Image
from pathlib import Path

class TextureLoader:
    _texture_path: Path|None = None
    _textures: list[dict] = []
    def __init__(self, metadata_file:Path|str):
        self.metadata_file = Path(metadata_file)
        self.load_metadata()
        
    def load_metadata(self):
        if not self.metadata_file.exists():
            raise FileNotFoundError(f"Metadata file {self.metadata_file} does not exist.")
        
        with open(self.metadata_file, 'r') as f:
            metadata = yaml.safe_load(f)
        
        filename = metadata.get('filename')
        if not filename:
            raise ValueError("Metadata file must contain a 'filename' key.")
        
        self._texture_path = self.metadata_file.parent / "assets" / Path(filename)
        if not self._texture_path.exists():
            raise FileNotFoundError(f"Texture file {self._texture_path} does not exist.")
        
        self._textures = metadata.get('textures', [])
        
    @property
    def texture_count(self) -> int:
        return len(self._textures)
    