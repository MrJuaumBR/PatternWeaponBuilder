# Exhaustive Material / Part Test Results

This report tests **every loaded material against every part slot** in every pattern. Compatible rows show the actual resulting item stats from the production `build_item_with_materials` calculation; incompatible combinations are listed but are not built.

- Materials checked: **30**
- Pattern definitions: **6**
- Part slots tested: **18**
- Material/part combinations checked: **540**
- Formula: `final = base × (1 + Σ(part.weight × material modifier))`.
- `attack` uses each material's `damage`; defense is shown only for defensive item patterns.
- For each table, non-target parts use a deterministic compatible reference material with modifiers closest to zero.

## Pattern: `pickaxe` (tool)

Base stats: durability=100, attack=100.

### Part: `tool_handle` — handle

Material amount: **1** · Stat weight: **0.15** · Reference result: durability=132.00, attack=121.70

| Material ID | Material | Compatible | Durability modifier | Attack modifier | Result durability | Result attack | Result defense |
| --- | --- | :---: | ---: | ---: | ---: | ---: | ---: |
| `wood` | Wood | Yes | +0.46 | +0.30 | 136.65 | 123.20 | — |
| `bone` | Bone | Yes | -0.10 | +0.72 | 128.25 | 129.50 | — |
| `iron_ore` | Iron Ore | No | +0.57 | +0.50 | — | — | — |
| `iron_bar` | Iron Bar | No | +0.57 | +0.50 | — | — | — |
| `copper_ore` | Copper Ore | No | +0.50 | +0.45 | — | — | — |
| `copper_bar` | Copper Bar | No | +0.50 | +0.45 | — | — | — |
| `gold_ore` | Gold Ore | No | +0.40 | +0.42 | — | — | — |
| `gold_bar` | Gold Bar | No | +0.40 | +0.42 | — | — | — |
| `coal` | Coal | Yes | +0.15 | +0.20 | 132.00 | 121.70 | — |
| `carbon` | Carbon | No | +0.25 | +0.22 | — | — | — |
| `magnetite` | Magnetite | No | +0.60 | +0.45 | — | — | — |
| `fiber` | Fiber | Yes | +0.30 | +0.18 | 134.25 | 121.40 | — |
| `brass` | Brass | No | +0.55 | +0.48 | — | — | — |
| `steel` | Steel | No | +0.80 | +0.70 | — | — | — |
| `aluminium` | Aluminium | No | +0.52 | +0.35 | — | — | — |
| `titanium` | Titanium | No | +0.82 | +0.62 | — | — | — |
| `diamond` | Diamond | No | +0.90 | +0.75 | — | — | — |
| `emerald` | Emerald | No | +0.62 | +0.38 | — | — | — |
| `topaz` | Topaz | No | +0.58 | +0.32 | — | — | — |
| `amethyst` | Amethyst | No | +0.54 | +0.30 | — | — | — |
| `sapphire` | Sapphire | No | +0.78 | +0.45 | — | — | — |
| `ruby` | Ruby | No | +0.76 | +0.47 | — | — | — |
| `copper_wire` | Copper Wire | No | +0.32 | +0.20 | — | — | — |
| `gold_wire` | Gold Wire | No | +0.28 | +0.18 | — | — | — |
| `bronze` | Bronze | No | +0.62 | +0.55 | — | — | — |
| `obsidian` | Obsidian | Yes | +0.38 | +0.82 | 135.45 | 131.00 | — |
| `leather` | Leather | Yes | +0.42 | +0.08 | 136.05 | 119.90 | — |
| `tin_ore` | Tin Ore | No | +0.28 | +0.18 | — | — | — |
| `tin_bar` | Tin Bar | No | +0.35 | +0.22 | — | — | — |
| `silver_bar` | Silver Bar | No | +0.48 | +0.38 | — | — | — |

### Part: `pickaxe_joint` — joint

Material amount: **1** · Stat weight: **0.20** · Reference result: durability=132.00, attack=121.70

| Material ID | Material | Compatible | Durability modifier | Attack modifier | Result durability | Result attack | Result defense |
| --- | --- | :---: | ---: | ---: | ---: | ---: | ---: |
| `wood` | Wood | No | +0.46 | +0.30 | — | — | — |
| `bone` | Bone | No | -0.10 | +0.72 | — | — | — |
| `iron_ore` | Iron Ore | No | +0.57 | +0.50 | — | — | — |
| `iron_bar` | Iron Bar | Yes | +0.57 | +0.50 | 136.40 | 127.30 | — |
| `copper_ore` | Copper Ore | No | +0.50 | +0.45 | — | — | — |
| `copper_bar` | Copper Bar | Yes | +0.50 | +0.45 | 135.00 | 126.30 | — |
| `gold_ore` | Gold Ore | No | +0.40 | +0.42 | — | — | — |
| `gold_bar` | Gold Bar | Yes | +0.40 | +0.42 | 133.00 | 125.70 | — |
| `coal` | Coal | No | +0.15 | +0.20 | — | — | — |
| `carbon` | Carbon | No | +0.25 | +0.22 | — | — | — |
| `magnetite` | Magnetite | No | +0.60 | +0.45 | — | — | — |
| `fiber` | Fiber | No | +0.30 | +0.18 | — | — | — |
| `brass` | Brass | Yes | +0.55 | +0.48 | 136.00 | 126.90 | — |
| `steel` | Steel | Yes | +0.80 | +0.70 | 141.00 | 131.30 | — |
| `aluminium` | Aluminium | Yes | +0.52 | +0.35 | 135.40 | 124.30 | — |
| `titanium` | Titanium | Yes | +0.82 | +0.62 | 141.40 | 129.70 | — |
| `diamond` | Diamond | No | +0.90 | +0.75 | — | — | — |
| `emerald` | Emerald | No | +0.62 | +0.38 | — | — | — |
| `topaz` | Topaz | No | +0.58 | +0.32 | — | — | — |
| `amethyst` | Amethyst | No | +0.54 | +0.30 | — | — | — |
| `sapphire` | Sapphire | No | +0.78 | +0.45 | — | — | — |
| `ruby` | Ruby | No | +0.76 | +0.47 | — | — | — |
| `copper_wire` | Copper Wire | No | +0.32 | +0.20 | — | — | — |
| `gold_wire` | Gold Wire | No | +0.28 | +0.18 | — | — | — |
| `bronze` | Bronze | Yes | +0.62 | +0.55 | 137.40 | 128.30 | — |
| `obsidian` | Obsidian | No | +0.38 | +0.82 | — | — | — |
| `leather` | Leather | No | +0.42 | +0.08 | — | — | — |
| `tin_ore` | Tin Ore | No | +0.28 | +0.18 | — | — | — |
| `tin_bar` | Tin Bar | Yes | +0.35 | +0.22 | 132.00 | 121.70 | — |
| `silver_bar` | Silver Bar | Yes | +0.48 | +0.38 | 134.60 | 124.90 | — |

### Part: `pickaxe_head_left` — head

Material amount: **1** · Stat weight: **0.33** · Reference result: durability=132.00, attack=121.70

| Material ID | Material | Compatible | Durability modifier | Attack modifier | Result durability | Result attack | Result defense |
| --- | --- | :---: | ---: | ---: | ---: | ---: | ---: |
| `wood` | Wood | No | +0.46 | +0.30 | — | — | — |
| `bone` | Bone | Yes | -0.10 | +0.72 | 117.38 | 137.95 | — |
| `iron_ore` | Iron Ore | No | +0.57 | +0.50 | — | — | — |
| `iron_bar` | Iron Bar | Yes | +0.57 | +0.50 | 139.15 | 130.80 | — |
| `copper_ore` | Copper Ore | No | +0.50 | +0.45 | — | — | — |
| `copper_bar` | Copper Bar | Yes | +0.50 | +0.45 | 136.88 | 129.17 | — |
| `gold_ore` | Gold Ore | No | +0.40 | +0.42 | — | — | — |
| `gold_bar` | Gold Bar | Yes | +0.40 | +0.42 | 133.62 | 128.20 | — |
| `coal` | Coal | No | +0.15 | +0.20 | — | — | — |
| `carbon` | Carbon | No | +0.25 | +0.22 | — | — | — |
| `magnetite` | Magnetite | No | +0.60 | +0.45 | — | — | — |
| `fiber` | Fiber | No | +0.30 | +0.18 | — | — | — |
| `brass` | Brass | Yes | +0.55 | +0.48 | 138.50 | 130.15 | — |
| `steel` | Steel | Yes | +0.80 | +0.70 | 146.62 | 137.30 | — |
| `aluminium` | Aluminium | Yes | +0.52 | +0.35 | 137.52 | 125.92 | — |
| `titanium` | Titanium | Yes | +0.82 | +0.62 | 147.28 | 134.70 | — |
| `diamond` | Diamond | Yes | +0.90 | +0.75 | 149.88 | 138.93 | — |
| `emerald` | Emerald | Yes | +0.62 | +0.38 | 140.78 | 126.90 | — |
| `topaz` | Topaz | Yes | +0.58 | +0.32 | 139.47 | 124.95 | — |
| `amethyst` | Amethyst | Yes | +0.54 | +0.30 | 138.18 | 124.30 | — |
| `sapphire` | Sapphire | Yes | +0.78 | +0.45 | 145.98 | 129.17 | — |
| `ruby` | Ruby | Yes | +0.76 | +0.47 | 145.32 | 129.82 | — |
| `copper_wire` | Copper Wire | No | +0.32 | +0.20 | — | — | — |
| `gold_wire` | Gold Wire | No | +0.28 | +0.18 | — | — | — |
| `bronze` | Bronze | Yes | +0.62 | +0.55 | 140.78 | 132.43 | — |
| `obsidian` | Obsidian | Yes | +0.38 | +0.82 | 132.97 | 141.20 | — |
| `leather` | Leather | No | +0.42 | +0.08 | — | — | — |
| `tin_ore` | Tin Ore | No | +0.28 | +0.18 | — | — | — |
| `tin_bar` | Tin Bar | Yes | +0.35 | +0.22 | 132.00 | 121.70 | — |
| `silver_bar` | Silver Bar | Yes | +0.48 | +0.38 | 136.22 | 126.90 | — |

### Part: `pickaxe_head_right` — head

Material amount: **1** · Stat weight: **0.33** · Reference result: durability=132.00, attack=121.70

| Material ID | Material | Compatible | Durability modifier | Attack modifier | Result durability | Result attack | Result defense |
| --- | --- | :---: | ---: | ---: | ---: | ---: | ---: |
| `wood` | Wood | No | +0.46 | +0.30 | — | — | — |
| `bone` | Bone | Yes | -0.10 | +0.72 | 117.38 | 137.95 | — |
| `iron_ore` | Iron Ore | No | +0.57 | +0.50 | — | — | — |
| `iron_bar` | Iron Bar | Yes | +0.57 | +0.50 | 139.15 | 130.80 | — |
| `copper_ore` | Copper Ore | No | +0.50 | +0.45 | — | — | — |
| `copper_bar` | Copper Bar | Yes | +0.50 | +0.45 | 136.88 | 129.17 | — |
| `gold_ore` | Gold Ore | No | +0.40 | +0.42 | — | — | — |
| `gold_bar` | Gold Bar | Yes | +0.40 | +0.42 | 133.62 | 128.20 | — |
| `coal` | Coal | No | +0.15 | +0.20 | — | — | — |
| `carbon` | Carbon | No | +0.25 | +0.22 | — | — | — |
| `magnetite` | Magnetite | No | +0.60 | +0.45 | — | — | — |
| `fiber` | Fiber | No | +0.30 | +0.18 | — | — | — |
| `brass` | Brass | Yes | +0.55 | +0.48 | 138.50 | 130.15 | — |
| `steel` | Steel | Yes | +0.80 | +0.70 | 146.62 | 137.30 | — |
| `aluminium` | Aluminium | Yes | +0.52 | +0.35 | 137.52 | 125.92 | — |
| `titanium` | Titanium | Yes | +0.82 | +0.62 | 147.28 | 134.70 | — |
| `diamond` | Diamond | Yes | +0.90 | +0.75 | 149.88 | 138.93 | — |
| `emerald` | Emerald | Yes | +0.62 | +0.38 | 140.78 | 126.90 | — |
| `topaz` | Topaz | Yes | +0.58 | +0.32 | 139.47 | 124.95 | — |
| `amethyst` | Amethyst | Yes | +0.54 | +0.30 | 138.18 | 124.30 | — |
| `sapphire` | Sapphire | Yes | +0.78 | +0.45 | 145.98 | 129.17 | — |
| `ruby` | Ruby | Yes | +0.76 | +0.47 | 145.32 | 129.82 | — |
| `copper_wire` | Copper Wire | No | +0.32 | +0.20 | — | — | — |
| `gold_wire` | Gold Wire | No | +0.28 | +0.18 | — | — | — |
| `bronze` | Bronze | Yes | +0.62 | +0.55 | 140.78 | 132.43 | — |
| `obsidian` | Obsidian | Yes | +0.38 | +0.82 | 132.97 | 141.20 | — |
| `leather` | Leather | No | +0.42 | +0.08 | — | — | — |
| `tin_ore` | Tin Ore | No | +0.28 | +0.18 | — | — | — |
| `tin_bar` | Tin Bar | Yes | +0.35 | +0.22 | 132.00 | 121.70 | — |
| `silver_bar` | Silver Bar | Yes | +0.48 | +0.38 | 136.22 | 126.90 | — |

## Pattern: `axe` (weapon)

Base stats: durability=100, attack=100.

### Part: `tool_handle` — handle

Material amount: **1** · Stat weight: **0.15** · Reference result: durability=132.00, attack=121.70

| Material ID | Material | Compatible | Durability modifier | Attack modifier | Result durability | Result attack | Result defense |
| --- | --- | :---: | ---: | ---: | ---: | ---: | ---: |
| `wood` | Wood | Yes | +0.46 | +0.30 | 136.65 | 123.20 | — |
| `bone` | Bone | Yes | -0.10 | +0.72 | 128.25 | 129.50 | — |
| `iron_ore` | Iron Ore | No | +0.57 | +0.50 | — | — | — |
| `iron_bar` | Iron Bar | No | +0.57 | +0.50 | — | — | — |
| `copper_ore` | Copper Ore | No | +0.50 | +0.45 | — | — | — |
| `copper_bar` | Copper Bar | No | +0.50 | +0.45 | — | — | — |
| `gold_ore` | Gold Ore | No | +0.40 | +0.42 | — | — | — |
| `gold_bar` | Gold Bar | No | +0.40 | +0.42 | — | — | — |
| `coal` | Coal | Yes | +0.15 | +0.20 | 132.00 | 121.70 | — |
| `carbon` | Carbon | No | +0.25 | +0.22 | — | — | — |
| `magnetite` | Magnetite | No | +0.60 | +0.45 | — | — | — |
| `fiber` | Fiber | Yes | +0.30 | +0.18 | 134.25 | 121.40 | — |
| `brass` | Brass | No | +0.55 | +0.48 | — | — | — |
| `steel` | Steel | No | +0.80 | +0.70 | — | — | — |
| `aluminium` | Aluminium | No | +0.52 | +0.35 | — | — | — |
| `titanium` | Titanium | No | +0.82 | +0.62 | — | — | — |
| `diamond` | Diamond | No | +0.90 | +0.75 | — | — | — |
| `emerald` | Emerald | No | +0.62 | +0.38 | — | — | — |
| `topaz` | Topaz | No | +0.58 | +0.32 | — | — | — |
| `amethyst` | Amethyst | No | +0.54 | +0.30 | — | — | — |
| `sapphire` | Sapphire | No | +0.78 | +0.45 | — | — | — |
| `ruby` | Ruby | No | +0.76 | +0.47 | — | — | — |
| `copper_wire` | Copper Wire | No | +0.32 | +0.20 | — | — | — |
| `gold_wire` | Gold Wire | No | +0.28 | +0.18 | — | — | — |
| `bronze` | Bronze | No | +0.62 | +0.55 | — | — | — |
| `obsidian` | Obsidian | Yes | +0.38 | +0.82 | 135.45 | 131.00 | — |
| `leather` | Leather | Yes | +0.42 | +0.08 | 136.05 | 119.90 | — |
| `tin_ore` | Tin Ore | No | +0.28 | +0.18 | — | — | — |
| `tin_bar` | Tin Bar | No | +0.35 | +0.22 | — | — | — |
| `silver_bar` | Silver Bar | No | +0.48 | +0.38 | — | — | — |

### Part: `axe_joint` — joint

Material amount: **1** · Stat weight: **0.15** · Reference result: durability=132.00, attack=121.70

| Material ID | Material | Compatible | Durability modifier | Attack modifier | Result durability | Result attack | Result defense |
| --- | --- | :---: | ---: | ---: | ---: | ---: | ---: |
| `wood` | Wood | No | +0.46 | +0.30 | — | — | — |
| `bone` | Bone | No | -0.10 | +0.72 | — | — | — |
| `iron_ore` | Iron Ore | No | +0.57 | +0.50 | — | — | — |
| `iron_bar` | Iron Bar | Yes | +0.57 | +0.50 | 135.30 | 125.90 | — |
| `copper_ore` | Copper Ore | No | +0.50 | +0.45 | — | — | — |
| `copper_bar` | Copper Bar | Yes | +0.50 | +0.45 | 134.25 | 125.15 | — |
| `gold_ore` | Gold Ore | No | +0.40 | +0.42 | — | — | — |
| `gold_bar` | Gold Bar | Yes | +0.40 | +0.42 | 132.75 | 124.70 | — |
| `coal` | Coal | No | +0.15 | +0.20 | — | — | — |
| `carbon` | Carbon | No | +0.25 | +0.22 | — | — | — |
| `magnetite` | Magnetite | No | +0.60 | +0.45 | — | — | — |
| `fiber` | Fiber | No | +0.30 | +0.18 | — | — | — |
| `brass` | Brass | Yes | +0.55 | +0.48 | 135.00 | 125.60 | — |
| `steel` | Steel | Yes | +0.80 | +0.70 | 138.75 | 128.90 | — |
| `aluminium` | Aluminium | Yes | +0.52 | +0.35 | 134.55 | 123.65 | — |
| `titanium` | Titanium | Yes | +0.82 | +0.62 | 139.05 | 127.70 | — |
| `diamond` | Diamond | No | +0.90 | +0.75 | — | — | — |
| `emerald` | Emerald | No | +0.62 | +0.38 | — | — | — |
| `topaz` | Topaz | No | +0.58 | +0.32 | — | — | — |
| `amethyst` | Amethyst | No | +0.54 | +0.30 | — | — | — |
| `sapphire` | Sapphire | No | +0.78 | +0.45 | — | — | — |
| `ruby` | Ruby | No | +0.76 | +0.47 | — | — | — |
| `copper_wire` | Copper Wire | No | +0.32 | +0.20 | — | — | — |
| `gold_wire` | Gold Wire | No | +0.28 | +0.18 | — | — | — |
| `bronze` | Bronze | Yes | +0.62 | +0.55 | 136.05 | 126.65 | — |
| `obsidian` | Obsidian | No | +0.38 | +0.82 | — | — | — |
| `leather` | Leather | No | +0.42 | +0.08 | — | — | — |
| `tin_ore` | Tin Ore | No | +0.28 | +0.18 | — | — | — |
| `tin_bar` | Tin Bar | Yes | +0.35 | +0.22 | 132.00 | 121.70 | — |
| `silver_bar` | Silver Bar | Yes | +0.48 | +0.38 | 133.95 | 124.10 | — |

### Part: `axe_back_head` — counterweight

Material amount: **1** · Stat weight: **0.25** · Reference result: durability=132.00, attack=121.70

| Material ID | Material | Compatible | Durability modifier | Attack modifier | Result durability | Result attack | Result defense |
| --- | --- | :---: | ---: | ---: | ---: | ---: | ---: |
| `wood` | Wood | No | +0.46 | +0.30 | — | — | — |
| `bone` | Bone | Yes | -0.10 | +0.72 | 120.75 | 134.20 | — |
| `iron_ore` | Iron Ore | No | +0.57 | +0.50 | — | — | — |
| `iron_bar` | Iron Bar | Yes | +0.57 | +0.50 | 137.50 | 128.70 | — |
| `copper_ore` | Copper Ore | No | +0.50 | +0.45 | — | — | — |
| `copper_bar` | Copper Bar | Yes | +0.50 | +0.45 | 135.75 | 127.45 | — |
| `gold_ore` | Gold Ore | No | +0.40 | +0.42 | — | — | — |
| `gold_bar` | Gold Bar | Yes | +0.40 | +0.42 | 133.25 | 126.70 | — |
| `coal` | Coal | No | +0.15 | +0.20 | — | — | — |
| `carbon` | Carbon | No | +0.25 | +0.22 | — | — | — |
| `magnetite` | Magnetite | No | +0.60 | +0.45 | — | — | — |
| `fiber` | Fiber | No | +0.30 | +0.18 | — | — | — |
| `brass` | Brass | Yes | +0.55 | +0.48 | 137.00 | 128.20 | — |
| `steel` | Steel | Yes | +0.80 | +0.70 | 143.25 | 133.70 | — |
| `aluminium` | Aluminium | Yes | +0.52 | +0.35 | 136.25 | 124.95 | — |
| `titanium` | Titanium | Yes | +0.82 | +0.62 | 143.75 | 131.70 | — |
| `diamond` | Diamond | Yes | +0.90 | +0.75 | 145.75 | 134.95 | — |
| `emerald` | Emerald | Yes | +0.62 | +0.38 | 138.75 | 125.70 | — |
| `topaz` | Topaz | Yes | +0.58 | +0.32 | 137.75 | 124.20 | — |
| `amethyst` | Amethyst | Yes | +0.54 | +0.30 | 136.75 | 123.70 | — |
| `sapphire` | Sapphire | Yes | +0.78 | +0.45 | 142.75 | 127.45 | — |
| `ruby` | Ruby | Yes | +0.76 | +0.47 | 142.25 | 127.95 | — |
| `copper_wire` | Copper Wire | No | +0.32 | +0.20 | — | — | — |
| `gold_wire` | Gold Wire | No | +0.28 | +0.18 | — | — | — |
| `bronze` | Bronze | Yes | +0.62 | +0.55 | 138.75 | 129.95 | — |
| `obsidian` | Obsidian | Yes | +0.38 | +0.82 | 132.75 | 136.70 | — |
| `leather` | Leather | No | +0.42 | +0.08 | — | — | — |
| `tin_ore` | Tin Ore | No | +0.28 | +0.18 | — | — | — |
| `tin_bar` | Tin Bar | Yes | +0.35 | +0.22 | 132.00 | 121.70 | — |
| `silver_bar` | Silver Bar | Yes | +0.48 | +0.38 | 135.25 | 125.70 | — |

### Part: `axe_head` — head

Material amount: **2** · Stat weight: **0.45** · Reference result: durability=132.00, attack=121.70

| Material ID | Material | Compatible | Durability modifier | Attack modifier | Result durability | Result attack | Result defense |
| --- | --- | :---: | ---: | ---: | ---: | ---: | ---: |
| `wood` | Wood | No | +0.46 | +0.30 | — | — | — |
| `bone` | Bone | Yes | -0.10 | +0.72 | 111.75 | 144.20 | — |
| `iron_ore` | Iron Ore | No | +0.57 | +0.50 | — | — | — |
| `iron_bar` | Iron Bar | Yes | +0.57 | +0.50 | 141.90 | 134.30 | — |
| `copper_ore` | Copper Ore | No | +0.50 | +0.45 | — | — | — |
| `copper_bar` | Copper Bar | Yes | +0.50 | +0.45 | 138.75 | 132.05 | — |
| `gold_ore` | Gold Ore | No | +0.40 | +0.42 | — | — | — |
| `gold_bar` | Gold Bar | Yes | +0.40 | +0.42 | 134.25 | 130.70 | — |
| `coal` | Coal | No | +0.15 | +0.20 | — | — | — |
| `carbon` | Carbon | No | +0.25 | +0.22 | — | — | — |
| `magnetite` | Magnetite | No | +0.60 | +0.45 | — | — | — |
| `fiber` | Fiber | No | +0.30 | +0.18 | — | — | — |
| `brass` | Brass | Yes | +0.55 | +0.48 | 141.00 | 133.40 | — |
| `steel` | Steel | Yes | +0.80 | +0.70 | 152.25 | 143.30 | — |
| `aluminium` | Aluminium | Yes | +0.52 | +0.35 | 139.65 | 127.55 | — |
| `titanium` | Titanium | Yes | +0.82 | +0.62 | 153.15 | 139.70 | — |
| `diamond` | Diamond | Yes | +0.90 | +0.75 | 156.75 | 145.55 | — |
| `emerald` | Emerald | Yes | +0.62 | +0.38 | 144.15 | 128.90 | — |
| `topaz` | Topaz | Yes | +0.58 | +0.32 | 142.35 | 126.20 | — |
| `amethyst` | Amethyst | Yes | +0.54 | +0.30 | 140.55 | 125.30 | — |
| `sapphire` | Sapphire | Yes | +0.78 | +0.45 | 151.35 | 132.05 | — |
| `ruby` | Ruby | Yes | +0.76 | +0.47 | 150.45 | 132.95 | — |
| `copper_wire` | Copper Wire | No | +0.32 | +0.20 | — | — | — |
| `gold_wire` | Gold Wire | No | +0.28 | +0.18 | — | — | — |
| `bronze` | Bronze | Yes | +0.62 | +0.55 | 144.15 | 136.55 | — |
| `obsidian` | Obsidian | Yes | +0.38 | +0.82 | 133.35 | 148.70 | — |
| `leather` | Leather | No | +0.42 | +0.08 | — | — | — |
| `tin_ore` | Tin Ore | No | +0.28 | +0.18 | — | — | — |
| `tin_bar` | Tin Bar | Yes | +0.35 | +0.22 | 132.00 | 121.70 | — |
| `silver_bar` | Silver Bar | Yes | +0.48 | +0.38 | 137.85 | 128.90 | — |

## Pattern: `shovel` (tool)

Base stats: durability=100, attack=100.

### Part: `tool_handle` — handle

Material amount: **1** · Stat weight: **0.15** · Reference result: durability=132.00, attack=121.70

| Material ID | Material | Compatible | Durability modifier | Attack modifier | Result durability | Result attack | Result defense |
| --- | --- | :---: | ---: | ---: | ---: | ---: | ---: |
| `wood` | Wood | Yes | +0.46 | +0.30 | 136.65 | 123.20 | — |
| `bone` | Bone | Yes | -0.10 | +0.72 | 128.25 | 129.50 | — |
| `iron_ore` | Iron Ore | No | +0.57 | +0.50 | — | — | — |
| `iron_bar` | Iron Bar | No | +0.57 | +0.50 | — | — | — |
| `copper_ore` | Copper Ore | No | +0.50 | +0.45 | — | — | — |
| `copper_bar` | Copper Bar | No | +0.50 | +0.45 | — | — | — |
| `gold_ore` | Gold Ore | No | +0.40 | +0.42 | — | — | — |
| `gold_bar` | Gold Bar | No | +0.40 | +0.42 | — | — | — |
| `coal` | Coal | Yes | +0.15 | +0.20 | 132.00 | 121.70 | — |
| `carbon` | Carbon | No | +0.25 | +0.22 | — | — | — |
| `magnetite` | Magnetite | No | +0.60 | +0.45 | — | — | — |
| `fiber` | Fiber | Yes | +0.30 | +0.18 | 134.25 | 121.40 | — |
| `brass` | Brass | No | +0.55 | +0.48 | — | — | — |
| `steel` | Steel | No | +0.80 | +0.70 | — | — | — |
| `aluminium` | Aluminium | No | +0.52 | +0.35 | — | — | — |
| `titanium` | Titanium | No | +0.82 | +0.62 | — | — | — |
| `diamond` | Diamond | No | +0.90 | +0.75 | — | — | — |
| `emerald` | Emerald | No | +0.62 | +0.38 | — | — | — |
| `topaz` | Topaz | No | +0.58 | +0.32 | — | — | — |
| `amethyst` | Amethyst | No | +0.54 | +0.30 | — | — | — |
| `sapphire` | Sapphire | No | +0.78 | +0.45 | — | — | — |
| `ruby` | Ruby | No | +0.76 | +0.47 | — | — | — |
| `copper_wire` | Copper Wire | No | +0.32 | +0.20 | — | — | — |
| `gold_wire` | Gold Wire | No | +0.28 | +0.18 | — | — | — |
| `bronze` | Bronze | No | +0.62 | +0.55 | — | — | — |
| `obsidian` | Obsidian | Yes | +0.38 | +0.82 | 135.45 | 131.00 | — |
| `leather` | Leather | Yes | +0.42 | +0.08 | 136.05 | 119.90 | — |
| `tin_ore` | Tin Ore | No | +0.28 | +0.18 | — | — | — |
| `tin_bar` | Tin Bar | No | +0.35 | +0.22 | — | — | — |
| `silver_bar` | Silver Bar | No | +0.48 | +0.38 | — | — | — |

### Part: `pickaxe_joint` — joint

Material amount: **1** · Stat weight: **0.20** · Reference result: durability=132.00, attack=121.70

| Material ID | Material | Compatible | Durability modifier | Attack modifier | Result durability | Result attack | Result defense |
| --- | --- | :---: | ---: | ---: | ---: | ---: | ---: |
| `wood` | Wood | No | +0.46 | +0.30 | — | — | — |
| `bone` | Bone | No | -0.10 | +0.72 | — | — | — |
| `iron_ore` | Iron Ore | No | +0.57 | +0.50 | — | — | — |
| `iron_bar` | Iron Bar | Yes | +0.57 | +0.50 | 136.40 | 127.30 | — |
| `copper_ore` | Copper Ore | No | +0.50 | +0.45 | — | — | — |
| `copper_bar` | Copper Bar | Yes | +0.50 | +0.45 | 135.00 | 126.30 | — |
| `gold_ore` | Gold Ore | No | +0.40 | +0.42 | — | — | — |
| `gold_bar` | Gold Bar | Yes | +0.40 | +0.42 | 133.00 | 125.70 | — |
| `coal` | Coal | No | +0.15 | +0.20 | — | — | — |
| `carbon` | Carbon | No | +0.25 | +0.22 | — | — | — |
| `magnetite` | Magnetite | No | +0.60 | +0.45 | — | — | — |
| `fiber` | Fiber | No | +0.30 | +0.18 | — | — | — |
| `brass` | Brass | Yes | +0.55 | +0.48 | 136.00 | 126.90 | — |
| `steel` | Steel | Yes | +0.80 | +0.70 | 141.00 | 131.30 | — |
| `aluminium` | Aluminium | Yes | +0.52 | +0.35 | 135.40 | 124.30 | — |
| `titanium` | Titanium | Yes | +0.82 | +0.62 | 141.40 | 129.70 | — |
| `diamond` | Diamond | No | +0.90 | +0.75 | — | — | — |
| `emerald` | Emerald | No | +0.62 | +0.38 | — | — | — |
| `topaz` | Topaz | No | +0.58 | +0.32 | — | — | — |
| `amethyst` | Amethyst | No | +0.54 | +0.30 | — | — | — |
| `sapphire` | Sapphire | No | +0.78 | +0.45 | — | — | — |
| `ruby` | Ruby | No | +0.76 | +0.47 | — | — | — |
| `copper_wire` | Copper Wire | No | +0.32 | +0.20 | — | — | — |
| `gold_wire` | Gold Wire | No | +0.28 | +0.18 | — | — | — |
| `bronze` | Bronze | Yes | +0.62 | +0.55 | 137.40 | 128.30 | — |
| `obsidian` | Obsidian | No | +0.38 | +0.82 | — | — | — |
| `leather` | Leather | No | +0.42 | +0.08 | — | — | — |
| `tin_ore` | Tin Ore | No | +0.28 | +0.18 | — | — | — |
| `tin_bar` | Tin Bar | Yes | +0.35 | +0.22 | 132.00 | 121.70 | — |
| `silver_bar` | Silver Bar | Yes | +0.48 | +0.38 | 134.60 | 124.90 | — |

### Part: `shovel_blade` — head

Material amount: **2** · Stat weight: **0.65** · Reference result: durability=132.00, attack=121.70

| Material ID | Material | Compatible | Durability modifier | Attack modifier | Result durability | Result attack | Result defense |
| --- | --- | :---: | ---: | ---: | ---: | ---: | ---: |
| `wood` | Wood | No | +0.46 | +0.30 | — | — | — |
| `bone` | Bone | Yes | -0.10 | +0.72 | 102.75 | 154.20 | — |
| `iron_ore` | Iron Ore | No | +0.57 | +0.50 | — | — | — |
| `iron_bar` | Iron Bar | Yes | +0.57 | +0.50 | 146.30 | 139.90 | — |
| `copper_ore` | Copper Ore | No | +0.50 | +0.45 | — | — | — |
| `copper_bar` | Copper Bar | Yes | +0.50 | +0.45 | 141.75 | 136.65 | — |
| `gold_ore` | Gold Ore | No | +0.40 | +0.42 | — | — | — |
| `gold_bar` | Gold Bar | Yes | +0.40 | +0.42 | 135.25 | 134.70 | — |
| `coal` | Coal | No | +0.15 | +0.20 | — | — | — |
| `carbon` | Carbon | No | +0.25 | +0.22 | — | — | — |
| `magnetite` | Magnetite | No | +0.60 | +0.45 | — | — | — |
| `fiber` | Fiber | No | +0.30 | +0.18 | — | — | — |
| `brass` | Brass | Yes | +0.55 | +0.48 | 145.00 | 138.60 | — |
| `steel` | Steel | Yes | +0.80 | +0.70 | 161.25 | 152.90 | — |
| `aluminium` | Aluminium | Yes | +0.52 | +0.35 | 143.05 | 130.15 | — |
| `titanium` | Titanium | Yes | +0.82 | +0.62 | 162.55 | 147.70 | — |
| `diamond` | Diamond | Yes | +0.90 | +0.75 | 167.75 | 156.15 | — |
| `emerald` | Emerald | Yes | +0.62 | +0.38 | 149.55 | 132.10 | — |
| `topaz` | Topaz | Yes | +0.58 | +0.32 | 146.95 | 128.20 | — |
| `amethyst` | Amethyst | Yes | +0.54 | +0.30 | 144.35 | 126.90 | — |
| `sapphire` | Sapphire | Yes | +0.78 | +0.45 | 159.95 | 136.65 | — |
| `ruby` | Ruby | Yes | +0.76 | +0.47 | 158.65 | 137.95 | — |
| `copper_wire` | Copper Wire | No | +0.32 | +0.20 | — | — | — |
| `gold_wire` | Gold Wire | No | +0.28 | +0.18 | — | — | — |
| `bronze` | Bronze | Yes | +0.62 | +0.55 | 149.55 | 143.15 | — |
| `obsidian` | Obsidian | Yes | +0.38 | +0.82 | 133.95 | 160.70 | — |
| `leather` | Leather | No | +0.42 | +0.08 | — | — | — |
| `tin_ore` | Tin Ore | No | +0.28 | +0.18 | — | — | — |
| `tin_bar` | Tin Bar | Yes | +0.35 | +0.22 | 132.00 | 121.70 | — |
| `silver_bar` | Silver Bar | Yes | +0.48 | +0.38 | 140.45 | 132.10 | — |

## Pattern: `shortsword` (weapon)

Base stats: durability=100, attack=100.

### Part: `sword_handle` — handle

Material amount: **1** · Stat weight: **0.20** · Reference result: durability=131.00, attack=121.60

| Material ID | Material | Compatible | Durability modifier | Attack modifier | Result durability | Result attack | Result defense |
| --- | --- | :---: | ---: | ---: | ---: | ---: | ---: |
| `wood` | Wood | Yes | +0.46 | +0.30 | 137.20 | 123.60 | — |
| `bone` | Bone | Yes | -0.10 | +0.72 | 126.00 | 132.00 | — |
| `iron_ore` | Iron Ore | No | +0.57 | +0.50 | — | — | — |
| `iron_bar` | Iron Bar | No | +0.57 | +0.50 | — | — | — |
| `copper_ore` | Copper Ore | No | +0.50 | +0.45 | — | — | — |
| `copper_bar` | Copper Bar | No | +0.50 | +0.45 | — | — | — |
| `gold_ore` | Gold Ore | No | +0.40 | +0.42 | — | — | — |
| `gold_bar` | Gold Bar | No | +0.40 | +0.42 | — | — | — |
| `coal` | Coal | Yes | +0.15 | +0.20 | 131.00 | 121.60 | — |
| `carbon` | Carbon | No | +0.25 | +0.22 | — | — | — |
| `magnetite` | Magnetite | No | +0.60 | +0.45 | — | — | — |
| `fiber` | Fiber | Yes | +0.30 | +0.18 | 134.00 | 121.20 | — |
| `brass` | Brass | No | +0.55 | +0.48 | — | — | — |
| `steel` | Steel | No | +0.80 | +0.70 | — | — | — |
| `aluminium` | Aluminium | No | +0.52 | +0.35 | — | — | — |
| `titanium` | Titanium | No | +0.82 | +0.62 | — | — | — |
| `diamond` | Diamond | No | +0.90 | +0.75 | — | — | — |
| `emerald` | Emerald | No | +0.62 | +0.38 | — | — | — |
| `topaz` | Topaz | No | +0.58 | +0.32 | — | — | — |
| `amethyst` | Amethyst | No | +0.54 | +0.30 | — | — | — |
| `sapphire` | Sapphire | No | +0.78 | +0.45 | — | — | — |
| `ruby` | Ruby | No | +0.76 | +0.47 | — | — | — |
| `copper_wire` | Copper Wire | No | +0.32 | +0.20 | — | — | — |
| `gold_wire` | Gold Wire | No | +0.28 | +0.18 | — | — | — |
| `bronze` | Bronze | No | +0.62 | +0.55 | — | — | — |
| `obsidian` | Obsidian | Yes | +0.38 | +0.82 | 135.60 | 134.00 | — |
| `leather` | Leather | Yes | +0.42 | +0.08 | 136.40 | 119.20 | — |
| `tin_ore` | Tin Ore | No | +0.28 | +0.18 | — | — | — |
| `tin_bar` | Tin Bar | No | +0.35 | +0.22 | — | — | — |
| `silver_bar` | Silver Bar | No | +0.48 | +0.38 | — | — | — |

### Part: `sword_hilt` — hilt

Material amount: **1** · Stat weight: **0.20** · Reference result: durability=131.00, attack=121.60

| Material ID | Material | Compatible | Durability modifier | Attack modifier | Result durability | Result attack | Result defense |
| --- | --- | :---: | ---: | ---: | ---: | ---: | ---: |
| `wood` | Wood | No | +0.46 | +0.30 | — | — | — |
| `bone` | Bone | No | -0.10 | +0.72 | — | — | — |
| `iron_ore` | Iron Ore | No | +0.57 | +0.50 | — | — | — |
| `iron_bar` | Iron Bar | Yes | +0.57 | +0.50 | 135.40 | 127.20 | — |
| `copper_ore` | Copper Ore | No | +0.50 | +0.45 | — | — | — |
| `copper_bar` | Copper Bar | Yes | +0.50 | +0.45 | 134.00 | 126.20 | — |
| `gold_ore` | Gold Ore | No | +0.40 | +0.42 | — | — | — |
| `gold_bar` | Gold Bar | Yes | +0.40 | +0.42 | 132.00 | 125.60 | — |
| `coal` | Coal | No | +0.15 | +0.20 | — | — | — |
| `carbon` | Carbon | No | +0.25 | +0.22 | — | — | — |
| `magnetite` | Magnetite | No | +0.60 | +0.45 | — | — | — |
| `fiber` | Fiber | No | +0.30 | +0.18 | — | — | — |
| `brass` | Brass | Yes | +0.55 | +0.48 | 135.00 | 126.80 | — |
| `steel` | Steel | Yes | +0.80 | +0.70 | 140.00 | 131.20 | — |
| `aluminium` | Aluminium | Yes | +0.52 | +0.35 | 134.40 | 124.20 | — |
| `titanium` | Titanium | Yes | +0.82 | +0.62 | 140.40 | 129.60 | — |
| `diamond` | Diamond | No | +0.90 | +0.75 | — | — | — |
| `emerald` | Emerald | No | +0.62 | +0.38 | — | — | — |
| `topaz` | Topaz | No | +0.58 | +0.32 | — | — | — |
| `amethyst` | Amethyst | No | +0.54 | +0.30 | — | — | — |
| `sapphire` | Sapphire | No | +0.78 | +0.45 | — | — | — |
| `ruby` | Ruby | No | +0.76 | +0.47 | — | — | — |
| `copper_wire` | Copper Wire | No | +0.32 | +0.20 | — | — | — |
| `gold_wire` | Gold Wire | No | +0.28 | +0.18 | — | — | — |
| `bronze` | Bronze | Yes | +0.62 | +0.55 | 136.40 | 128.20 | — |
| `obsidian` | Obsidian | No | +0.38 | +0.82 | — | — | — |
| `leather` | Leather | No | +0.42 | +0.08 | — | — | — |
| `tin_ore` | Tin Ore | No | +0.28 | +0.18 | — | — | — |
| `tin_bar` | Tin Bar | Yes | +0.35 | +0.22 | 131.00 | 121.60 | — |
| `silver_bar` | Silver Bar | Yes | +0.48 | +0.38 | 133.60 | 124.80 | — |

### Part: `sword_blade` — blade

Material amount: **1** · Stat weight: **0.60** · Reference result: durability=131.00, attack=121.60

| Material ID | Material | Compatible | Durability modifier | Attack modifier | Result durability | Result attack | Result defense |
| --- | --- | :---: | ---: | ---: | ---: | ---: | ---: |
| `wood` | Wood | No | +0.46 | +0.30 | — | — | — |
| `bone` | Bone | Yes | -0.10 | +0.72 | 104.00 | 151.60 | — |
| `iron_ore` | Iron Ore | No | +0.57 | +0.50 | — | — | — |
| `iron_bar` | Iron Bar | Yes | +0.57 | +0.50 | 144.20 | 138.40 | — |
| `copper_ore` | Copper Ore | No | +0.50 | +0.45 | — | — | — |
| `copper_bar` | Copper Bar | Yes | +0.50 | +0.45 | 140.00 | 135.40 | — |
| `gold_ore` | Gold Ore | No | +0.40 | +0.42 | — | — | — |
| `gold_bar` | Gold Bar | Yes | +0.40 | +0.42 | 134.00 | 133.60 | — |
| `coal` | Coal | No | +0.15 | +0.20 | — | — | — |
| `carbon` | Carbon | No | +0.25 | +0.22 | — | — | — |
| `magnetite` | Magnetite | No | +0.60 | +0.45 | — | — | — |
| `fiber` | Fiber | No | +0.30 | +0.18 | — | — | — |
| `brass` | Brass | Yes | +0.55 | +0.48 | 143.00 | 137.20 | — |
| `steel` | Steel | Yes | +0.80 | +0.70 | 158.00 | 150.40 | — |
| `aluminium` | Aluminium | Yes | +0.52 | +0.35 | 141.20 | 129.40 | — |
| `titanium` | Titanium | Yes | +0.82 | +0.62 | 159.20 | 145.60 | — |
| `diamond` | Diamond | Yes | +0.90 | +0.75 | 164.00 | 153.40 | — |
| `emerald` | Emerald | Yes | +0.62 | +0.38 | 147.20 | 131.20 | — |
| `topaz` | Topaz | Yes | +0.58 | +0.32 | 144.80 | 127.60 | — |
| `amethyst` | Amethyst | Yes | +0.54 | +0.30 | 142.40 | 126.40 | — |
| `sapphire` | Sapphire | Yes | +0.78 | +0.45 | 156.80 | 135.40 | — |
| `ruby` | Ruby | Yes | +0.76 | +0.47 | 155.60 | 136.60 | — |
| `copper_wire` | Copper Wire | No | +0.32 | +0.20 | — | — | — |
| `gold_wire` | Gold Wire | No | +0.28 | +0.18 | — | — | — |
| `bronze` | Bronze | Yes | +0.62 | +0.55 | 147.20 | 141.40 | — |
| `obsidian` | Obsidian | Yes | +0.38 | +0.82 | 132.80 | 157.60 | — |
| `leather` | Leather | No | +0.42 | +0.08 | — | — | — |
| `tin_ore` | Tin Ore | No | +0.28 | +0.18 | — | — | — |
| `tin_bar` | Tin Bar | Yes | +0.35 | +0.22 | 131.00 | 121.60 | — |
| `silver_bar` | Silver Bar | Yes | +0.48 | +0.38 | 138.80 | 131.20 | — |

## Pattern: `longsword` (weapon)

Base stats: durability=100, attack=100.

### Part: `longsword_handle` — handle

Material amount: **1** · Stat weight: **0.15** · Reference result: durability=132.00, attack=121.70

| Material ID | Material | Compatible | Durability modifier | Attack modifier | Result durability | Result attack | Result defense |
| --- | --- | :---: | ---: | ---: | ---: | ---: | ---: |
| `wood` | Wood | Yes | +0.46 | +0.30 | 136.65 | 123.20 | — |
| `bone` | Bone | Yes | -0.10 | +0.72 | 128.25 | 129.50 | — |
| `iron_ore` | Iron Ore | No | +0.57 | +0.50 | — | — | — |
| `iron_bar` | Iron Bar | No | +0.57 | +0.50 | — | — | — |
| `copper_ore` | Copper Ore | No | +0.50 | +0.45 | — | — | — |
| `copper_bar` | Copper Bar | No | +0.50 | +0.45 | — | — | — |
| `gold_ore` | Gold Ore | No | +0.40 | +0.42 | — | — | — |
| `gold_bar` | Gold Bar | No | +0.40 | +0.42 | — | — | — |
| `coal` | Coal | Yes | +0.15 | +0.20 | 132.00 | 121.70 | — |
| `carbon` | Carbon | No | +0.25 | +0.22 | — | — | — |
| `magnetite` | Magnetite | No | +0.60 | +0.45 | — | — | — |
| `fiber` | Fiber | Yes | +0.30 | +0.18 | 134.25 | 121.40 | — |
| `brass` | Brass | No | +0.55 | +0.48 | — | — | — |
| `steel` | Steel | No | +0.80 | +0.70 | — | — | — |
| `aluminium` | Aluminium | No | +0.52 | +0.35 | — | — | — |
| `titanium` | Titanium | No | +0.82 | +0.62 | — | — | — |
| `diamond` | Diamond | No | +0.90 | +0.75 | — | — | — |
| `emerald` | Emerald | No | +0.62 | +0.38 | — | — | — |
| `topaz` | Topaz | No | +0.58 | +0.32 | — | — | — |
| `amethyst` | Amethyst | No | +0.54 | +0.30 | — | — | — |
| `sapphire` | Sapphire | No | +0.78 | +0.45 | — | — | — |
| `ruby` | Ruby | No | +0.76 | +0.47 | — | — | — |
| `copper_wire` | Copper Wire | No | +0.32 | +0.20 | — | — | — |
| `gold_wire` | Gold Wire | No | +0.28 | +0.18 | — | — | — |
| `bronze` | Bronze | No | +0.62 | +0.55 | — | — | — |
| `obsidian` | Obsidian | Yes | +0.38 | +0.82 | 135.45 | 131.00 | — |
| `leather` | Leather | Yes | +0.42 | +0.08 | 136.05 | 119.90 | — |
| `tin_ore` | Tin Ore | No | +0.28 | +0.18 | — | — | — |
| `tin_bar` | Tin Bar | No | +0.35 | +0.22 | — | — | — |
| `silver_bar` | Silver Bar | No | +0.48 | +0.38 | — | — | — |

### Part: `longsword_hilt` — hilt

Material amount: **1** · Stat weight: **0.15** · Reference result: durability=132.00, attack=121.70

| Material ID | Material | Compatible | Durability modifier | Attack modifier | Result durability | Result attack | Result defense |
| --- | --- | :---: | ---: | ---: | ---: | ---: | ---: |
| `wood` | Wood | No | +0.46 | +0.30 | — | — | — |
| `bone` | Bone | No | -0.10 | +0.72 | — | — | — |
| `iron_ore` | Iron Ore | No | +0.57 | +0.50 | — | — | — |
| `iron_bar` | Iron Bar | Yes | +0.57 | +0.50 | 135.30 | 125.90 | — |
| `copper_ore` | Copper Ore | No | +0.50 | +0.45 | — | — | — |
| `copper_bar` | Copper Bar | Yes | +0.50 | +0.45 | 134.25 | 125.15 | — |
| `gold_ore` | Gold Ore | No | +0.40 | +0.42 | — | — | — |
| `gold_bar` | Gold Bar | Yes | +0.40 | +0.42 | 132.75 | 124.70 | — |
| `coal` | Coal | No | +0.15 | +0.20 | — | — | — |
| `carbon` | Carbon | No | +0.25 | +0.22 | — | — | — |
| `magnetite` | Magnetite | No | +0.60 | +0.45 | — | — | — |
| `fiber` | Fiber | No | +0.30 | +0.18 | — | — | — |
| `brass` | Brass | Yes | +0.55 | +0.48 | 135.00 | 125.60 | — |
| `steel` | Steel | Yes | +0.80 | +0.70 | 138.75 | 128.90 | — |
| `aluminium` | Aluminium | Yes | +0.52 | +0.35 | 134.55 | 123.65 | — |
| `titanium` | Titanium | Yes | +0.82 | +0.62 | 139.05 | 127.70 | — |
| `diamond` | Diamond | No | +0.90 | +0.75 | — | — | — |
| `emerald` | Emerald | No | +0.62 | +0.38 | — | — | — |
| `topaz` | Topaz | No | +0.58 | +0.32 | — | — | — |
| `amethyst` | Amethyst | No | +0.54 | +0.30 | — | — | — |
| `sapphire` | Sapphire | No | +0.78 | +0.45 | — | — | — |
| `ruby` | Ruby | No | +0.76 | +0.47 | — | — | — |
| `copper_wire` | Copper Wire | No | +0.32 | +0.20 | — | — | — |
| `gold_wire` | Gold Wire | No | +0.28 | +0.18 | — | — | — |
| `bronze` | Bronze | Yes | +0.62 | +0.55 | 136.05 | 126.65 | — |
| `obsidian` | Obsidian | No | +0.38 | +0.82 | — | — | — |
| `leather` | Leather | No | +0.42 | +0.08 | — | — | — |
| `tin_ore` | Tin Ore | No | +0.28 | +0.18 | — | — | — |
| `tin_bar` | Tin Bar | Yes | +0.35 | +0.22 | 132.00 | 121.70 | — |
| `silver_bar` | Silver Bar | Yes | +0.48 | +0.38 | 133.95 | 124.10 | — |

### Part: `longsword_blade` — blade

Material amount: **1** · Stat weight: **0.70** · Reference result: durability=132.00, attack=121.70

| Material ID | Material | Compatible | Durability modifier | Attack modifier | Result durability | Result attack | Result defense |
| --- | --- | :---: | ---: | ---: | ---: | ---: | ---: |
| `wood` | Wood | No | +0.46 | +0.30 | — | — | — |
| `bone` | Bone | Yes | -0.10 | +0.72 | 100.50 | 156.70 | — |
| `iron_ore` | Iron Ore | No | +0.57 | +0.50 | — | — | — |
| `iron_bar` | Iron Bar | Yes | +0.57 | +0.50 | 147.40 | 141.30 | — |
| `copper_ore` | Copper Ore | No | +0.50 | +0.45 | — | — | — |
| `copper_bar` | Copper Bar | Yes | +0.50 | +0.45 | 142.50 | 137.80 | — |
| `gold_ore` | Gold Ore | No | +0.40 | +0.42 | — | — | — |
| `gold_bar` | Gold Bar | Yes | +0.40 | +0.42 | 135.50 | 135.70 | — |
| `coal` | Coal | No | +0.15 | +0.20 | — | — | — |
| `carbon` | Carbon | No | +0.25 | +0.22 | — | — | — |
| `magnetite` | Magnetite | No | +0.60 | +0.45 | — | — | — |
| `fiber` | Fiber | No | +0.30 | +0.18 | — | — | — |
| `brass` | Brass | Yes | +0.55 | +0.48 | 146.00 | 139.90 | — |
| `steel` | Steel | Yes | +0.80 | +0.70 | 163.50 | 155.30 | — |
| `aluminium` | Aluminium | Yes | +0.52 | +0.35 | 143.90 | 130.80 | — |
| `titanium` | Titanium | Yes | +0.82 | +0.62 | 164.90 | 149.70 | — |
| `diamond` | Diamond | Yes | +0.90 | +0.75 | 170.50 | 158.80 | — |
| `emerald` | Emerald | Yes | +0.62 | +0.38 | 150.90 | 132.90 | — |
| `topaz` | Topaz | Yes | +0.58 | +0.32 | 148.10 | 128.70 | — |
| `amethyst` | Amethyst | Yes | +0.54 | +0.30 | 145.30 | 127.30 | — |
| `sapphire` | Sapphire | Yes | +0.78 | +0.45 | 162.10 | 137.80 | — |
| `ruby` | Ruby | Yes | +0.76 | +0.47 | 160.70 | 139.20 | — |
| `copper_wire` | Copper Wire | No | +0.32 | +0.20 | — | — | — |
| `gold_wire` | Gold Wire | No | +0.28 | +0.18 | — | — | — |
| `bronze` | Bronze | Yes | +0.62 | +0.55 | 150.90 | 144.80 | — |
| `obsidian` | Obsidian | Yes | +0.38 | +0.82 | 134.10 | 163.70 | — |
| `leather` | Leather | No | +0.42 | +0.08 | — | — | — |
| `tin_ore` | Tin Ore | No | +0.28 | +0.18 | — | — | — |
| `tin_bar` | Tin Bar | Yes | +0.35 | +0.22 | 132.00 | 121.70 | — |
| `silver_bar` | Silver Bar | Yes | +0.48 | +0.38 | 141.10 | 132.90 | — |

## Pattern: `ingot` (ingot)

Base stats: durability=100.

### Part: `ingot_bar` — ingot

Material amount: **1** · Stat weight: **1.00** · Reference result: durability=135.00

| Material ID | Material | Compatible | Durability modifier | Attack modifier | Result durability | Result attack | Result defense |
| --- | --- | :---: | ---: | ---: | ---: | ---: | ---: |
| `wood` | Wood | No | +0.46 | +0.30 | — | — | — |
| `bone` | Bone | No | -0.10 | +0.72 | — | — | — |
| `iron_ore` | Iron Ore | No | +0.57 | +0.50 | — | — | — |
| `iron_bar` | Iron Bar | Yes | +0.57 | +0.50 | 157.00 | — | — |
| `copper_ore` | Copper Ore | No | +0.50 | +0.45 | — | — | — |
| `copper_bar` | Copper Bar | Yes | +0.50 | +0.45 | 150.00 | — | — |
| `gold_ore` | Gold Ore | No | +0.40 | +0.42 | — | — | — |
| `gold_bar` | Gold Bar | Yes | +0.40 | +0.42 | 140.00 | — | — |
| `coal` | Coal | No | +0.15 | +0.20 | — | — | — |
| `carbon` | Carbon | No | +0.25 | +0.22 | — | — | — |
| `magnetite` | Magnetite | No | +0.60 | +0.45 | — | — | — |
| `fiber` | Fiber | No | +0.30 | +0.18 | — | — | — |
| `brass` | Brass | Yes | +0.55 | +0.48 | 155.00 | — | — |
| `steel` | Steel | Yes | +0.80 | +0.70 | 180.00 | — | — |
| `aluminium` | Aluminium | Yes | +0.52 | +0.35 | 152.00 | — | — |
| `titanium` | Titanium | Yes | +0.82 | +0.62 | 182.00 | — | — |
| `diamond` | Diamond | No | +0.90 | +0.75 | — | — | — |
| `emerald` | Emerald | No | +0.62 | +0.38 | — | — | — |
| `topaz` | Topaz | No | +0.58 | +0.32 | — | — | — |
| `amethyst` | Amethyst | No | +0.54 | +0.30 | — | — | — |
| `sapphire` | Sapphire | No | +0.78 | +0.45 | — | — | — |
| `ruby` | Ruby | No | +0.76 | +0.47 | — | — | — |
| `copper_wire` | Copper Wire | No | +0.32 | +0.20 | — | — | — |
| `gold_wire` | Gold Wire | No | +0.28 | +0.18 | — | — | — |
| `bronze` | Bronze | Yes | +0.62 | +0.55 | 162.00 | — | — |
| `obsidian` | Obsidian | No | +0.38 | +0.82 | — | — | — |
| `leather` | Leather | No | +0.42 | +0.08 | — | — | — |
| `tin_ore` | Tin Ore | No | +0.28 | +0.18 | — | — | — |
| `tin_bar` | Tin Bar | Yes | +0.35 | +0.22 | 135.00 | — | — |
| `silver_bar` | Silver Bar | Yes | +0.48 | +0.38 | 148.00 | — | — |

## Summary

- Tested combinations: **540**
- Compatible builds with numeric stat results: **216**
- Incompatible combinations: **324**

Generated by `tests/test_material_matrix.py`.
