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
  - name: "shortsword_craft"
    pattern: shortsword
    station: anvil
  - name: "longsword_craft"
    pattern: longsword
    station: anvil
  - name: "ingot_craft"
    pattern: ingot
    station: forge
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
| `roughness` | `float` | Surface texture (0.0–1.0); affects grip & friction. | `0.40` |
| `weight` | `float` | Mass (0.0–1.0); affects swing speed & knockback. | `0.70` |
| `hardness` | `float` | Resistance to deformation (0.0–1.0). | `0.60` |
| `elasticity` | `float` | How much it springs back under stress (0.0–1.0). | `0.40` |
| `thermal_conductivity` | `float` | Heat transfer (0.0–1.0). | `0.50` |
| `melting_point` | `int` | Melting point in °C; `-1` when not applicable. | `1538` |
| `magic_affinity` | `float` | Magic resonance (0.0–1.0). | `0.10` |
| `traits` | `list[str]` | References to trait ids defined in [`traits.yaml`](#traits). | `[reinforced, tough]` |

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
    roughness: 0.70
    weight: 0.15
    hardness: 0.20
    elasticity: 0.50
    thermal_conductivity: 0.10
    melting_point: 300
    magic_affinity: 0.10
    traits: [flammable, flexible]

  - id: "steel"
    name: "Steel"
    description: "An iron-carbon alloy; strong, tough, and well balanced for tools, weapons, and armor."
    durability: 0.8
    damage: 0.7
    defense: 0.65
    color: "#71797E"
    type: alloy
    category: alloys
    roughness: 0.30
    weight: 0.75
    hardness: 0.75
    elasticity: 0.55
    thermal_conductivity: 0.50
    melting_point: 1425
    magic_affinity: 0.10
    traits: [reinforced, sharp, tough]
```

### Traits <small>`metadata`</small>
> You can find the file on the path [`data/traits.yaml`](./data/traits.yaml)

The `traits.yaml` file is a list under the key `traits`. Traits are attached to **materials** and inherited by every craft built from them.

#### Dataset
| Name | Type | Description | Example |
| ---- | ---- | ----------- | ------- |
| `id` | `str` | Unique trait id referenced by `materials.yaml` `traits:` list. | `sharp` |
| `name` | `str` | Display name of the trait. | `Sharp` |
| `description` | `str` | Short flavor text shown in the tooltip. | `A keen edge adds flat damage.` |
| `type` | `str` | Trigger type: `passive`, `on_event`, `on_use`, `on_hit`, `on_mine`, `on_craft`. | `passive` |
| `effects` | `list[dict]` | Effects applied when the trait fires. | see below |
| `events` | `list[dict]` | Event hooks with nested effects (only when `type != passive`). | see below |

#### Effect kinds
| Kind | Description |
| ---- | ----------- |
| `stat_flat` | Adds a flat value to a stat. |
| `stat_mult` | Multiplies a stat. |
| `chance` | Rolls a chance and applies nested effects. |
| `conditional` | Applies nested effects if a condition is met. |
| `immunity` | Negates a damage type / event. |
| `flag` | Sets a boolean behaviour flag. |
| `aura` | Continuous effect in a radius. |

#### Stats used by effects
`damage`, `defense`, `durability`, `durability_cost`, `attack_speed`, `mining_speed`, `knockback`, `value`, `modifier_slots`, `durability_ratio`

#### Example
```yaml
traits:
  - id: reinforced
    name: Reinforced
    description: "20% chance to prevent durability loss on use."
    type: passive
    effects:
      - kind: chance
        event: on_use
        chance: 0.20
        effects:
          - kind: stat_flat
            stat: durability_cost
            value: -1.0

  - id: heavy
    name: Heavy
    description: "Slow but powerful; increased knockback."
    type: passive
    effects:
      - kind: stat_flat
        stat: attack_speed
        value: -0.15
      - kind: stat_mult
        stat: knockback
        value: 1.40

  - id: stonebound
    name: Stonebound
    description: "Grows stronger as it wears down."
    type: passive
    effects:
      - kind: conditional
        condition:
          stat: durability_ratio
          operator: "<"
          value: 0.5
        effects:
          - kind: stat_flat
            stat: damage
            value: 0.15
```

#### Built-in Traits
| Id | Name | Summary |
| -- | ---- | ------- |
| `jagged` | Jagged | +damage, more durability cost. |
| `reinforced` | Reinforced | Chance to prevent durability loss. |
| `sharp` | Sharp | Flat damage bonus. |
| `lightweight` | Lightweight | Faster attacks, weaker knockback. |
| `heavy` | Heavy | Slower attacks, stronger knockback. |
| `brittle` | Brittle | Faster wear. |
| `tough` | Tough | Slower wear. |
| `sparkly` | Sparkly | Increases item value. |
| `crude` | Crude | Small penalty to damage, defense, durability. |
| `flammable` | Flammable | Extra wear from fire. |
| `fireproof` | Fireproof | Immune to fire damage. |
| `conductive` | Conductive | Small bonus damage vs magic targets. |
| `magnetic` | Magnetic | Pulls nearby dropped items. |
| `brittle_gem` | Brittle Gem | +damage, much faster wear. |
| `soulbound` | Soulbound | Kept on death. |
| `writeable` | Writeable | Extra modifier slot. |
| `dense` | Dense | Increased knockback. |
| `flexible` | Flexible | Reduced wear. |
| `hardened` | Hardened | Flat defense bonus. |
| `stonebound` | Stonebound | Stronger as durability drops. |

### Patterns
Patterns define the shape of a craft. They are tied to a **modular texture set** and are decoded by the `Pattern` enum in `craft_loader.py`. Each part refers to a region in `texture.yaml`.

| Value | Description | Texture Parts |
| ----- | ----------- | ------------- |
| `pickaxe` | Pickaxe pattern. | `tool_handle`, `pickaxe_joint`, `pickaxe_head` |
| `axe` | Axe pattern. | `tool_handle`, `axe_joint`, `axe_back_head`, `axe_head` |
| `shortsword` | Short sword pattern. | `sword_handle`, `sword_hilt`, `sword_blade` |
| `longsword` | Long sword pattern. | `sword_handle`, `sword_hilt`, `sword_blade` |
| `ingot` | Ingot pattern. | `ingot_bar` |

### Parts <small>`metadata`</small>
> You can find the file on the path [`data/parts.yaml`](./data/parts.yaml)

The `parts.yaml` file describes, for every pattern, which parts it is composed of, how many material units each part consumes, and its stat-contribution weight. Weights of all parts of a pattern must sum to `1.0`. Final stats are computed as `Σ(part.material.stat * part.weight)` across all parts of the craft.

#### Dataset
| Name | Type | Description | Example |
| ---- | ---- | ----------- | ------- |
| `patterns` | `list[dict]` | Top-level list of pattern definitions. | — |
| `patterns[].id` | `str` | Pattern id; must match a value from [**Patterns**](#patterns). | `pickaxe` |
| `patterns[].parts` | `list[dict]` | Parts that make up the pattern. | — |
| `parts[].id` | `str` | Part id; must match a `textures[].id` in `texture.yaml`. | `pickaxe_head` |
| `parts[].material_amount` | `int` | Units of the material consumed by this part. | `2` |
| `parts[].weight` | `float` | Stat-contribution weight (0.0–1.0); sums to `1.0` per pattern. | `0.65` |

#### Example
```yaml
patterns:
  - id: pickaxe
    parts:
      - id: tool_handle
        material_amount: 1
        weight: 0.15
      - id: pickaxe_joint
        material_amount: 1
        weight: 0.20
      - id: pickaxe_head
        material_amount: 2
        weight: 0.65
```

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
| `filename` | `str` | Relative path to the texture image, resolved against `assets/`. | `textures/patterns.png` |
| `textures` | `list[dict]` | List of texture region definitions. | — |
| `textures[].id` | `str` | Region id referenced by `parts.yaml`. | `pickaxe_head` |
| `textures[].name` | `str` | Display name of the region. | `Pickaxe Head` |
| `textures[].x` | `int` | Region X coordinate on the sheet. | `32` |
| `textures[].y` | `int` | Region Y coordinate on the sheet. | `32` |
| `textures[].w` | `int` | Region width. | `32` |
| `textures[].h` | `int` | Region height. | `32` |
| `textures[].type` | `str` | Region type. | `pattern` |
| `textures[].layer_priority` | `int` | Z-order for stacking parts on the assembled tool. **Higher = drawn first (bottom layer)**. | `100` |

#### Layering
Every part sprite is authored on the same **32×32 tile** and blitted at the same origin. Visual ordering is decided purely by `layer_priority`, rendered in **descending** order:

| Priority | Layer | Typical parts |
| -------- | ----- | ------------- |
| `100` | Bottom | Handles (`tool_handle`, `sword_handle`) |
| `50` | Middle | Joints / hilts (`pickaxe_joint`, `axe_joint`, `sword_hilt`) |
| `10` | Top | Heads / blades (`pickaxe_head`, `axe_head`, `axe_back_head`, `sword_blade`, `ingot_bar`) |

### Example
```yaml
filename: "textures/patterns.png"

textures:
  - id: "tool_handle"
    name: "Tool Handle"
    x: 32
    y: 0
    w: 32
    h: 32
    type: "pattern"
    layer_priority: 100
  - id: "pickaxe_joint"
    name: "Pickaxe Joint"
    x: 0
    y: 32
    w: 32
    h: 32
    type: "pattern"
    layer_priority: 50
  - id: "pickaxe_head"
    name: "Pickaxe Head"
    x: 32
    y: 32
    w: 32
    h: 32
    type: "pattern"
    layer_priority: 10
```

## Tests

### Render Random Tool
> Path: [`tests/render_random_tool.py`](./tests/render_random_tool.py)

Renders a random tool by picking a random craft, assigning a random material to each of its parts, tinting each part sprite with the material color, and stacking the parts on a **32×32 canvas** in `layer_priority` order.

#### Usage
```bash
# one render (default), into tests/output/
python tests/render_random_tool.py

# ten renders, into tests/output/
python tests/render_random_tool.py 10

# five renders, into a custom folder
python tests/render_random_tool.py 5 --output-dir tests/output/batch_01

# shorthand
python tests/render_random_tool.py 5 -o tests/output/batch_01
```

#### Arguments
| Name | Type | Default | Description |
| ---- | ---- | ------- | ----------- |
| `repeat_count` | `int` (positional) | `1` | How many random renders to generate. |
| `--output-dir` / `-o` | `Path` | `tests/output` | Override the output directory. |

#### Output
```
tests/output/test_render_{year}-{month}-{day}_{hour}-{minute}-{seconds}_{index:03d}.png
```
e.g. `tests/output/test_render_2026-11-26_14-32-45_000.png`

The `_index` suffix keeps filenames unique when batch-rendering multiple tools in the same second.

## Contribuitors
- [@MrJuaumBR](https://github.com/MrJuaumBR/) - Main Lead & Coder;