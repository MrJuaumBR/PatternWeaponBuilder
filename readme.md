# Pattern Weapon Builder

A **Tinker's Construct** Based Project.

## Metadata

All of our *materials* and *crafts* are fully modular, designed to fit with a modular texture hand-made by [MrJuaumBR](#contributors).

### Crafts <small>`metadata`</small>

> You can find the file on the path [`data/crafts.yaml`](./data/crafts.yaml)

The `crafts.yaml` file has it's own structure that will be a list defined by the key `crafts`, which inside of it, all of the crafts.

#### Dataset

| Name | Type | Description | Example |
| --- | --- | --- | --- |
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
  - name: "shovel_craft"
    pattern: shovel
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
| --- | --- | --- | --- |
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
| --- | --- |
| `natural` | Natural organic or mineral materials (Wood, Fiber, Coal). |
| `misc` | Miscellaneous materials (Bone). |
| `metal` | Metals, ores and wires (Iron, Copper, Gold, Titanium). |
| `chemical` | Chemical elements and compounds (Carbon). |
| `alloy` | Alloys made from two or more metals (Steel, Brass). |
| `gem` | Gemstones (Diamond, Emerald, Topaz, Amethyst, Sapphire, Ruby). |

#### Categories

| Value | Description |
| --- | --- |
| `natural` | Natural materials. |
| `ores` | Raw ores (Iron Ore, Copper Ore, Gold Ore, Magnetite). |
| `metals` | Refined metals and bars (Iron Bar, Copper Bar, Gold Bar, Aluminium, Titanium). |
| `chemicals` | Chemical materials (Carbon). |
| `alloys` | Alloys (Steel, Brass). |
| `gems` | Gemstones (Diamond, Emerald, Topaz, Amethyst, Sapphire, Ruby). |
| `wires` | Wire variants of metals (Copper Wire, Gold Wire). |

#### Current material catalog

The current material matrix covers **30 materials**:

| Group | Materials |
| --- | --- |
| Natural | Wood, Coal, Fiber, Leather |
| Miscellaneous | Bone, Obsidian |
| Ores | Iron Ore, Copper Ore, Gold Ore, Magnetite, Tin Ore |
| Refined metals | Iron Bar, Copper Bar, Gold Bar, Aluminium, Titanium, Tin Bar, Silver Bar |
| Alloys | Brass, Steel, Bronze |
| Chemicals | Carbon |
| Gems | Diamond, Emerald, Topaz, Amethyst, Sapphire, Ruby |
| Wires | Copper Wire, Gold Wire |

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
| --- | --- | --- | --- |
| `id` | `str` | Unique trait id referenced by `materials.yaml` `traits:` list. | `sharp` |
| `name` | `str` | Display name of the trait. | `Sharp` |
| `description` | `str` | Short flavor text shown in the tooltip. | `A keen edge adds flat damage.` |
| `type` | `str` | Trigger type: `passive`, `on_event`, `on_use`, `on_hit`, `on_mine`, `on_craft`. | `passive` |
| `effects` | `list[dict]` | Effects applied when the trait fires. | see below |
| `events` | `list[dict]` | Event hooks with nested effects (only when `type != passive`). | see below |

#### Effect kinds

| Kind | Description |
| --- | --- |
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
| --- | --- | --- |
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
| --- | --- | --- |
| `pickaxe` | Pickaxe pattern. | `tool_handle`, `pickaxe_joint`, `pickaxe_head` (left/right pair) |
| `axe` | Axe pattern. | `tool_handle`, `axe_joint`, `axe_back_head`, `axe_head` |
| `shovel` | Shovel pattern. | `tool_handle`, `pickaxe_joint`, `shovel_blade` |
| `shortsword` | Short sword pattern. | `sword_handle`, `sword_hilt`, `sword_blade` |
| `longsword` | Long sword pattern. | `longsword_handle`, `longsword_hilt`, `longsword_blade` |
| `ingot` | Ingot pattern. | `ingot_bar` |

### Parts <small>`metadata`</small>

> You can find the file on the path [`data/parts.yaml`](./data/parts.yaml)

The `parts.yaml` file describes each pattern's item type, base stats, component parts, material units consumed, stat-contribution weights, and material compatibility. Weights of all parts of a pattern must sum to `1.0`. Each final stat is the pattern's base stat scaled by the weighted average of the corresponding part materials' modifiers.

The pickaxe head is a **two-piece pair: left and right**. It is represented by the single logical part slot `pickaxe_head`; its `material_amount: 2` accounts for one head on each side. The chosen material applies to both halves, and the slot's stat weight represents the combined pair. If the two sides ever need different materials, define separate left/right part IDs and split their stat weights.

#### Dataset

| Name | Type | Description | Example |
| --- | --- | --- | --- |
| `patterns` | `list[dict]` | Top-level list of pattern definitions. | — |
| `patterns[].id` | `str` | Pattern id; must match a value from [**Patterns**](#patterns). | `pickaxe` |
| `patterns[].item_type` | `str` | Item class: `tool`, `weapon`, `shield`, `armor`, or `ingot`. | `tool` |
| `patterns[].base_stats` | `dict` | Base item stats; only declare stats relevant to that item. | `{durability: 100, attack: 100}` |
| `patterns[].parts` | `list[dict]` | Parts that make up the pattern. | — |
| `parts[].id` | `str` | Part id; must match a `textures[].id` in `texture.yaml`. | `pickaxe_head` |
| `parts[].role` | `str` | Functional role used to express part intent. | `head` |
| `parts[].material_amount` | `int` | Units of the material consumed by this part. | `2` |
| `parts[].weight` | `float` | Stat-contribution weight (0.0–1.0); sums to `1.0` per pattern. | `0.65` |
| `parts[].allowed_material_types` | `list[str]` | Material types accepted by this part. | `[metal, alloy, gem]` |
| `parts[].allowed_material_categories` | `list[str]` | Material categories accepted by this part; material must satisfy both allow-lists. | `[metals, alloys, gems]` |

#### Example

```yaml
patterns:
  - id: pickaxe
    item_type: tool
    base_stats:
      durability: 100
      attack: 100
    parts:
      - id: tool_handle
        role: handle
        material_amount: 1
        weight: 0.15
        allowed_material_types: [natural, misc]
        allowed_material_categories: [natural]
      - id: pickaxe_joint
        role: joint
        material_amount: 1
        weight: 0.20
        allowed_material_types: [metal, alloy]
        allowed_material_categories: [metals, alloys]
      - id: pickaxe_head
        role: head
        # Two physical pieces: one left head and one right head.
        material_amount: 2
        weight: 0.65
        allowed_material_types: [metal, alloy, gem, misc]
        allowed_material_categories: [metals, alloys, gems, natural]
```

### Stations

Stations define *where* a craft is executed. They are decoded by the `Station` enum in `craft_loader.py`.

| Value | Description |
| --- | --- |
| `forge` | Crafting station for smelting and forging. |
| `table` | Crafting table for basic crafting. |
| `anvil` | Anvil for shaping tools and weapons. |

### Textures <small>`metadata`</small>

> The metadata file is passed to `TextureLoader`; its `filename` points to `assets/<filename>` next to it.

| Name | Type | Description | Example |
| --- | --- | --- | --- |
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
| --- | --- | --- |
| `100` | Bottom | Handles (`tool_handle`, `sword_handle`, `longsword_handle`) |
| `50` | Middle | Joints / hilts (`pickaxe_joint`, `axe_joint`, `sword_hilt`, `longsword_hilt`) |
| `10` | Top | Heads / blades (`pickaxe_head`, `axe_head`, `axe_back_head`, `shovel_blade`, `sword_blade`, `longsword_blade`, `ingot_bar`) |

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

### Runtime metadata and item stats

The runtime `Loader` now loads and exposes all metadata domains documented above: `Crafts`, `Material`, `Traits`, `Parts`, and `Texture`. Loader objects retain the documented fields (including all material physical/magic properties, trait `effects` and `events`, part contribution weights, and texture coordinates/type/layer priority). References between crafts, patterns, parts, texture regions, and material traits are checked during loading. `Craft.name` is the metadata field; `Craft.id` remains available as a backward-compatible alias.

#### Pattern and part additions

Each `parts.yaml` pattern now includes `item_type` and `base_stats`. `base_stats` contains only stats relevant to that item: tools and weapons have `durability` and `attack`; ingots have `durability`; only `shield` and `armor` patterns may declare `defense`. The current project has no shield/armor pattern, so its generated tools, weapons, and ingots do not receive a defense stat.

Each part also declares a `role`, `allowed_material_types`, and `allowed_material_categories`. A material must satisfy both allow-lists to be used. Handles accept natural grip materials; joints/hilts accept refined metal/alloy materials; heads and blades accept suitable refined metals, alloys, gems, and bone-like `misc` materials. Wire materials have category `wires`, which is not allowed for any current part, so a wire cannot be used as an axe head, blade, or other structural part. Raw ores are also excluded from finished heads/joints; ingot bars accept refined metals and alloys only. The loader checks that all part IDs have texture regions and that each pattern's part weights sum to `1.0`.

#### Stat calculation

Material `durability`, `damage`, and `defense` are percentage modifiers in the documented `-1.0` to `1.0` range. Item `attack` uses a material's `damage` modifier. For each stat declared by the pattern, the builder calculates the weighted modifier across its parts and applies it to the base value:

```
weighted_modifier = Σ(part.weight × material_modifier)
final_stat = base_stat × (1 + weighted_modifier)
```

Thus a `+0.5` modifier on a base of `100` yields `150` (+50%), and `-0.2` yields `80` (-20%). Part weights determine how much each material contributes; `material_amount` is the quantity consumed and does not multiply combat stats. Trait metadata and effects are fully loaded and linked, but triggered/passive trait-effect execution is separate from this material-stat calculation.

## Tools

### Aseprite asset loader

> Path: [`tools/asset_loader.py`](./tools/asset_loader.py)

Copies `.png`, `.jpg`, and `.jpeg` files from the project's root `aseprite/` folder into `data/assets/textures/`, replacing files with the same names. The destination folder is created automatically. Other file types are skipped.

Run it from the project root after exporting or updating sprites:

```bash
python tools/asset_loader.py
```

## Tests

### Random item renderer

> Path: [`tests/render_random_tool.py`](./tests/render_random_tool.py)

Renders a random item by picking a random craft, assigning a compatible material to each part, tinting each part sprite with the material color, stacking the parts on a **32×32 canvas** in `layer_priority` order, and printing the resulting stats.

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
| --- | --- | --- | --- |
| `repeat_count` | `int` (positional) | `1` | How many random renders to generate. |
| `--output-dir` / `-o` | `Path` | `tests/output` | Override the output directory. |

#### Output

```
tests/output/test_render_{year}-{month}-{day}_{hour}-{minute}-{seconds}_{index:03d}.png
```

e.g. `tests/output/test_render_2026-11-26_14-32-45_000.png`

The `_index` suffix keeps filenames unique when batch-rendering multiple tools in the same second.

### Randomized build tests

The rendering utility now selects only compatible materials and prints the computed stats for each random item. The core build/stat tests do not need a graphics runtime:

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
python tests/render_random_tool.py 5
```

The unit tests generate 250 seeded random builds, verify material compatibility (including wire exclusion), check metadata loading, and exercise both the `150` (+50%) and `80` (-20%) multiplier examples. The exhaustive matrix covers **6 patterns**, **17 part slots**, and all **30 materials**.

### Exhaustive material/part matrix

`tests/test_material_matrix.py` tries every material against every part slot, records each compatibility result, and calculates the resulting item stats for compatible choices using the production item builder. In each row, the tested material is assigned to the named part and the remaining parts use deterministic compatible reference materials. The script writes the Markdown report to `tests/output/material_matrix_readme.md`.

```bash
python tests/test_material_matrix.py
# or run it as part of the full test suite:
python -m unittest discover -s tests -p 'test_*.py' -v
```

The report contains one table per pattern part, listing every material, whether it is compatible, its durability/attack modifiers, and the resulting durability/attack/defense values where applicable. The current report tests **510 material/part combinations**; **198** are compatible builds and **312** are rejected combinations. It includes the shovel and the separate longsword handle, hilt, and blade parts.

## Contributors

- [@MrJuaumBR](https://github.com/MrJuaumBR/) - Main Lead & Coder;