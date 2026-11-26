# Pattern Weapon Builder
A **Tinker's Construct** Based Project.

## Metadata
All of our *materials* and *crafts* are fully modular, they are designed to fit with a modular texture hand-made by [MrJuaumBR](#contribuitors)

### Crafts <small>`metadata`</small>
> You can find the file on the path [`data/crafts.yaml`](./data/crafts.yaml)

The `crafts.yaml` file has it's own structure that will be a list defined by the key `crafts`, which inside of it, all of the crafts.

#### Dataset
| Name | Type | Description | Example |
| ---- | ---- | ----------- | ------- |
| `name` | `str` | the Name/ID of the craft, it needs to be unique. | `pickaxe_craft` |
| `pattern` | `str` | The pattern of the crafting, it needs to be one of the patterns in the [**Patterns**](#patterns) section. | `pickaxe` |
| `station` | `str` | The Station that this craft needs to be done. Has to be on of the stations in [**Stations**](#stations). | `anvil` |

#### Example
```yaml
crafts:
  - name: "pickaxe_craft"
    pattern: pickaxe
    station: anvil
  - name: "axe_craft"
    pattern: axe
    station: anvil
```

### Materials <small>`metadata`</small>
> You can find the file on the path [`data/materials.yaml`](./data/materials.yaml)

The `materials.yaml` file has it's own structure that will be a list defined by the key `materials`, which inside of it, all of the materials.

#### Dataset
| Name | Type | Description | Example |
| ---- | ---- | ----------- | ------- |
| `id` | `str` | Unique identifier of the material, used by crafts and the code. | `iron_bar` |
| `name` | `str` | Display name of the material. | `Iron Bar` |
| `description` | `str` | Short flavor text shown for the material. | `Refined iron bar; balanced...` |
| `durability` | `float` | Durability modifier, ranged between `-1.0` and `1.0`. | `0.57` |
| `damage` | `float` | Damage modifier, ranged between `-1.0` and `1.0`. | `0.5` |
| `defense` | `float` | Defense modifier, ranged between `-1.0` and `1.0`. | `0.35` |
| `color` | `str` | Hex color code (`#RRGGBB`) used to tint the modular texture. | `#a19d94` |
| `type` | `str` | Material type, has to be one of [**Material Types**](#material-types). | `metal` |
| `category` | `str` | Material category, has to be one of [**Categories**](#categories). | `metals` |

#### Material Types
| Value | Description |
| ----- | ----------- |
| `natural` | Natural organic or mineral materials (Wood, Fiber, Coal). |
| `misc` | Miscellaneous materials (Bone). |
| `metal` | Metals, ores and wires (Iron, Copper, Gold, Titanium). |
| `chemical` | Chemical elements and compounds (Carbon). |
| `alloy` | Alloys made from two or more metals (Steel, Brass). |
| `gem` | Gemstones (Diamond, Emerald, Topaz, Amethyst, Sapphire, Ruby). |

#### Categories
| Value | Description |
| ----- | ----------- |
| `natural` | Natural materials. |
| `ores` | Raw ores (Iron Ore, Copper Ore, Gold Ore, Magnetite). |
| `metals` | Refined metals and bars (Iron Bar, Copper Bar, Gold Bar, Aluminium, Titanium). |
| `chemicals` | Chemical materials (Carbon). |
| `alloys` | Alloys (Steel, Brass). |
| `gems` | Gemstones (Diamond, Emerald, Topaz, Amethyst, Sapphire, Ruby). |
| `wires` | Wire variants of metals (Copper Wire, Gold Wire). |

#### Example
```yaml
materials:
  - id: "wood"
    name: "Wood"
    description: "A common natural organic material; lightweight, easy to work, and moderately durable."
    durability: 0.46
    damage: 0.3
    defense: 0.22
    color: "#87633A"
    type: natural
    category: natural
  - id: "steel"
    name: "Steel"
    description: "An iron-carbon alloy; strong, tough, and well balanced for tools, weapons, and armor."
    durability: 0.8
    damage: 0.7
    defense: 0.65
    color: "#71797E"
    type: alloy
    category: alloys
```

### Patterns
Patterns define the shape of a craft. They are tied to a **modular texture set** and are decoded by the `Pattern` enum in `craft_loader.py`.

| Value | Description | Texture Parts |
| ----- | ----------- | ------------- |
| `pickaxe` | Pickaxe pattern. | `tool_handle`, `pickaxe_joint`, `pickaxe_head` |
| `axe` | Axe pattern. | — |
| `shortsword` | Short sword pattern. | — |
| `longsword` | Long sword pattern. | — |
| `ingot` | Ingot pattern. | — |

### Stations
Stations define *where* a craft is executed. They are decoded by the `Station` enum in `craft_loader.py`.

| Value | Description |
| ----- | ----------- |
| `forge` | Crafting station for smelting and forging. |
| `table` | Crafting table for basic crafting. |
| `anvil` | Anvil for shaping tools and weapons. |

### Textures <small>`metadata`</small>
> The metadata file is passed to `TextureLoader`; its `filename` points to `assets/<filename>` next to it.

| Name | Type | Description | Example |
| ---- | ---- | ----------- | ------- |
| `filename` | `str` | Relative path to the texture image, resolved against `assets/`. | `materials.png` |
| `textures` | `list[dict]` | List of texture region definitions. | — |

## Contribuitors
- [@MrJuaumBR](https://github.com/MrJuaumBR/) - Main Lead & Coder;