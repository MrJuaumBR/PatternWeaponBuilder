"""Exhaustive material/part compatibility and stat-result matrix.

Run with `python tests/test_material_matrix.py`, or through unittest discovery.
The test writes a Markdown README to tests/output/material_matrix_readme.md.
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from data.scripts import item_builder as _item_builder
from data.scripts.loader import Loader

compatible_materials = _item_builder.compatible_materials
if hasattr(_item_builder, "build_item_with_materials"):
    build_item_with_materials = _item_builder.build_item_with_materials
else:
    # Compatibility for project copies where this test was updated before item_builder.py.
    # Keep the same compatibility checks and weighted-stat formula as the production builder.
    def build_item_with_materials(craft, definition, materials_by_part):
        expected_ids = {part.id for part in definition.parts}
        if expected_ids != set(materials_by_part):
            raise ValueError("An explicit material assignment is required for every pattern part.")
        built_parts = []
        for part in definition.parts:
            material = materials_by_part[part.id]
            if not part.accepts(material):
                raise ValueError(f"Material '{material.id}' is not compatible with part '{part.id}'.")
            built_parts.append(_item_builder.BuiltPart(part, material))
        stats = {}
        for stat, base_value in definition.base_stats.items():
            modifier = sum(
                item.part.weight * (item.material.damage if stat == "attack" else getattr(item.material, stat))
                for item in built_parts
            )
            stats[stat] = round(base_value * (1.0 + modifier), 2)
        return _item_builder.BuiltItem(craft, definition, built_parts, stats)

DEFAULT_OUTPUT = ROOT / "tests" / "output" / "material_matrix_readme.md"


def fmt(value: float | None) -> str:
    return "—" if value is None else f"{value:.2f}"


def evaluate_material_matrix(loader: Loader) -> tuple[str, int, int]:
    """Return the report markdown, number of all attempts, and compatible builds."""
    materials = loader.Material.materials
    attempts = 0
    compatible_count = 0
    sections: list[str] = [
        "# Exhaustive Material / Part Test Results",
        "",
        "This report tests **every loaded material against every part slot** in every pattern. "
        "Compatible rows show the actual resulting item stats from the production `build_item_with_materials` "
        "calculation; incompatible combinations are listed but are not built.",
        "",
        f"- Materials checked: **{len(materials)}**",
        f"- Pattern definitions: **{loader.Parts.pattern_count}**",
        f"- Part slots tested: **{loader.Parts.parts_count}**",
        f"- Material/part combinations checked: **{len(materials) * loader.Parts.parts_count}**",
        "- Formula: `final = base × (1 + Σ(part.weight × material modifier))`.",
        "- `attack` uses each material's `damage`; defense is shown only for defensive item patterns.",
        "- For each table, non-target parts use a deterministic compatible reference material with modifiers closest to zero.",
        "",
    ]

    crafts_by_pattern = {craft.pattern: craft for craft in loader.Crafts.crafts}
    for definition in loader.Parts.patterns:
        craft = crafts_by_pattern.get(definition.id)
        if craft is None:
            raise AssertionError(f"No craft uses pattern '{definition.id.value}'.")

        reference_assignments = {}
        for part in definition.parts:
            eligible = compatible_materials(part, materials)
            if not eligible:
                raise AssertionError(f"No compatible reference material for {definition.id.value}/{part.id}.")
            reference_assignments[part.id] = min(
                eligible,
                key=lambda material: (
                    abs(material.durability) + abs(material.damage) + abs(material.defense),
                    material.id,
                ),
            )
        baseline = build_item_with_materials(craft, definition, reference_assignments)

        sections.extend([
            f"## Pattern: `{definition.id.value}` ({definition.item_type})",
            "",
            f"Base stats: {', '.join(f'{key}={value:g}' for key, value in definition.base_stats.items())}.",
            "",
        ])
        for part in definition.parts:
            attempts += len(materials)
            sections.extend([
                f"### Part: `{part.id}` — {part.role}",
                "",
                f"Material amount: **{part.material_amount}** · Stat weight: **{part.weight:.2f}** · "
                f"Reference result: {', '.join(f'{key}={value:.2f}' for key, value in baseline.stats.items())}",
                "",
                "| Material ID | Material | Compatible | Durability modifier | Attack modifier | Result durability | Result attack | Result defense |",
                "| --- | --- | :---: | ---: | ---: | ---: | ---: | ---: |",
            ])
            for material in materials:
                if not part.accepts(material):
                    sections.append(
                        f"| `{material.id}` | {material.name} | No | {material.durability:+.2f} | "
                        f"{material.damage:+.2f} | — | — | — |"
                    )
                    continue

                assignments = dict(reference_assignments)
                assignments[part.id] = material
                item = build_item_with_materials(craft, definition, assignments)
                compatible_count += 1
                sections.append(
                    f"| `{material.id}` | {material.name} | Yes | {material.durability:+.2f} | "
                    f"{material.damage:+.2f} | {fmt(item.stats.get('durability'))} | "
                    f"{fmt(item.stats.get('attack'))} | {fmt(item.stats.get('defense'))} |"
                )
            sections.append("")

    sections.extend([
        "## Summary",
        "",
        f"- Tested combinations: **{attempts}**",
        f"- Compatible builds with numeric stat results: **{compatible_count}**",
        f"- Incompatible combinations: **{attempts - compatible_count}**",
        "",
        "Generated by `tests/test_material_matrix.py`.",
        "",
    ])
    return "\n".join(sections), attempts, compatible_count


def write_report(output_path: Path = DEFAULT_OUTPUT) -> tuple[Path, int, int]:
    loader = Loader(ROOT)
    report, attempts, compatible_count = evaluate_material_matrix(loader)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")
    return output_path, attempts, compatible_count


class MaterialMatrixTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.loader = Loader(ROOT)

    def test_every_material_is_tried_against_every_part_and_reported(self) -> None:
        report, attempts, compatible_count = evaluate_material_matrix(self.loader)
        expected_attempts = self.loader.Material.materials_count * self.loader.Parts.parts_count
        self.assertEqual(attempts, expected_attempts)
        self.assertGreater(compatible_count, 0)
        for material in self.loader.Material.materials:
            self.assertIn(f"`{material.id}`", report)
        self.assertIn(f"Material/part combinations checked: **{expected_attempts}**", report)
        self.assertIn(f"Compatible builds with numeric stat results: **{compatible_count}**", report)

    def test_writes_generated_readme_report(self) -> None:
        path, attempts, compatible_count = write_report()
        self.assertTrue(path.exists())
        self.assertGreater(path.stat().st_size, 0)
        self.assertGreater(attempts, 0)
        self.assertGreater(compatible_count, 0)
        print(f"\n[material-matrix] wrote {path} ({attempts} combinations, {compatible_count} compatible)")


if __name__ == "__main__":
    unittest.main(verbosity=2)
