import yaml
from pathlib import Path
from enum import Enum
from dataclasses import dataclass
from lunaengine.backend.types import Color
class MaterialType(Enum):
    NATURAL = "natural"
    MISC = "misc"
    METAL = "metal"
    CHEMICAL = "chemical"
    ALLOY = "alloy"
    GEM = "gem"

class CategoryType(Enum):
    NATURAL = "natural"
    ORES = "ores"
    METALS = "metals"
    CHEMICALS = "chemicals"
    ALLOYS = "alloys"
    GEMS = "gems"
    WIRES = "wires"

@dataclass
class Material:
    id:str
    name:str
    description:str
    durability:float
    damage:float
    defense:float
    color:Color
    type: MaterialType
    category: CategoryType

class MaterialLoader:
    materials:list[Material] = []
    def __init__(self, metadata_path: Path|str):
        self.metadata_file:Path = Path(metadata_path)
        self.load_metadata()
        
    def load_metadata(self):
        if not self.metadata_file.exists():
            raise FileNotFoundError(f"Metadata file {self.metadata_file} does not exist.")
        
        with open(self.metadata_file, 'r') as f:
            metadata = yaml.safe_load(f)
            
        materials = metadata.get('materials')
        if not materials:
            raise ValueError("Materials Metadata may be corrupted, it doesn't have a 'materials' value.")
        
        for material in materials:
            # , 'durability': 0.46, 'damage': 0.3, 'defense': 0.22, 'color': '#87633A', 'type': 'natural', 'category': 'natural'}
            m = Material(
                id=str(material['id']),
                name=str(material['name']),
                description=str(material['description']),
                durability=float(material['durability']),
                damage=float(material['damage']),
                defense=float(material['defense']),
                color=Color.from_hex(str(material['color'])),
                type=MaterialType(str(material['type']).lower()),
                category=CategoryType(str(material['category']).lower())
            )
            self.materials.append(m)
        
    @property
    def materials_count(self) -> int:
        return len(self.materials)