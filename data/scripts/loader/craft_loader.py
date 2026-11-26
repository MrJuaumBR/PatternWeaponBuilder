import yaml
from enum import Enum
from dataclasses import dataclass
from pathlib import Path

class Pattern(Enum):
    PICKAXE = "pickaxe" # 'tool_handle', 'pickaxe_joint', 'pickaxe_head'
    AXE = "axe"
    SHORTSWORD = "shortsword"
    LONGSWORD = "longsword"
    INGOT = "ingot"
    
class Station(Enum):
    FORGE = "forge"
    TABLE = "table"
    ANVIL = "anvil"

@dataclass
class Craft:
    id: str
    pattern: Pattern
    station: Station
    
class CraftLoader:
    crafts:list[Craft] = []
    def __init__(self, metadata_path: Path|str):
        self.metadata_file:Path = Path(metadata_path)
        self.load_metadata()
        
    def load_metadata(self):
        if not self.metadata_file.exists():
            raise FileNotFoundError(f"Metadata file {self.metadata_file} does not exist.")
        
        with open(self.metadata_file, 'r') as f:
            metadata = yaml.safe_load(f)
            
        crafts = metadata.get('crafts')
        if not crafts:
            raise ValueError("Crafts Metadata may be corrupted, it doesn't have a 'crafts' value.")
        
        for craft in crafts:
            # {'name': 'pickaxe_craft', 'pattern': 'pickaxe', 'station': 'anvil'}
            c = Craft(id=str(craft['name']), pattern=Pattern(str(craft['pattern']).lower()), station=Station(str(craft['station']).lower()))
            self.crafts.append(c)
            
    @property
    def crafts_count(self) -> int:
        return len(self.crafts)