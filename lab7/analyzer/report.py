from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Set, Optional
import shutil
import subprocess

import matplotlib.pyplot as plt

from .cfg_builder import CFG, Definition


def write_cfg_dot(cfg: CFG, destination: Path) -> None:
    lines: List[str] = ["digraph CFG {", "    node [shape=box];"]
    for block in cfg.blocks:
        label_lines = [f"{block.identifier}:"]
        for statement in block.statements:
            label_lines.append(statement.text)
        escaped = "\n".join(label_lines).replace("\"", "\\\"")
        lines.append(f"    {block.identifier} [label=\"{escaped}\"]; ")
    for block in cfg.blocks:
        for edge in block.successors:
            if edge.label:
                lines.append(
                    f"    {block.identifier} -> {edge.target} [label=\"{edge.label}\"];"
                )
            else:
                lines.append(f"    {block.identifier} -> {edge.target};")
    lines.append("}")
    destination.write_text("\n".join(lines), encoding="utf-8")


def render_dot_to_png(dot_file: Path, png_file: Optional[Path] = None) -> Optional[Path]:
    """Attempt to render a DOT file to PNG using Graphviz if available.

    Returns the path to the PNG file if successful, otherwise None.
    """
    if png_file is None:
        png_file = dot_file.with_suffix('.png')
    dot_executable = shutil.which("dot")
    if not dot_executable:
        print("Graphviz 'dot' executable not found in PATH. Skipping rendering.")
        return None
    try:
        subprocess.run([dot_executable, "-Tpng", str(dot_file), "-o", str(png_file)], check=True)
        return png_file
    except Exception:
        print(f"Failed to render {dot_file} to PNG.")
        return None


def write_definitions_table(definitions: Dict[str, Definition], destination: Path) -> None:
    rows: List[str] = [
        "| Definition ID | Variable | Block | Line | Statement |",
        "|---------------|----------|-------|------|-----------|",
    ]
    for definition in sorted(definitions.values(), key=lambda d: int(d.identifier[1:])):
        statement = definition.statement.replace("|", "\\|")
        rows.append(
            f"| {definition.identifier} | {definition.variable} | {definition.block_id} | {definition.line} | `{statement}` |"
        )
    destination.write_text("\n".join(rows), encoding="utf-8")


def _format_set(items: Iterable[str]) -> str:
    if not items:
        return "{}"
    ordered = sorted(items, key=lambda value: (value[0], int(value[1:])))
    return "{" + ", ".join(ordered) + "}"


def write_iteration_tables(
    snapshots: Sequence[Dict[str, Dict[str, Set[str]]]],
    cfg: CFG,
    destination: Path,
) -> None:
    parts: List[str] = []
    for index, snapshot in enumerate(snapshots):
        parts.append(f"## Iteration {index}")
        parts.append("| Basic Block | gen[B] | kill[B] | in[B] | out[B] |")
        parts.append("|-------------|--------|---------|-------|--------|")
        for block in cfg.blocks:
            state = snapshot.get(block.identifier, {})
            parts.append(
                "| {block_id} | {gen} | {kill} | {in_set} | {out_set} |".format(
                    block_id=block.identifier,
                    gen=_format_set(state.get("gen", set())),
                    kill=_format_set(state.get("kill", set())),
                    in_set=_format_set(state.get("in", set())),
                    out_set=_format_set(state.get("out", set())),
                )
            )
        parts.append("")
    destination.write_text("\n".join(parts), encoding="utf-8")


def write_ambiguity_report(
    ambiguous: Dict[str, Dict[str, Set[str]]],
    definitions: Dict[str, Definition],
    destination: Path,
) -> None:
    if not ambiguous:
        destination.write_text("No blocks have multiple reaching definitions for any variable.", encoding="utf-8")
        return
    parts: List[str] = []
    for block_id, variable_map in ambiguous.items():
        parts.append(f"### Block {block_id}")
        parts.append("| Variable | Definition IDs | Statements |")
        parts.append("|----------|----------------|------------|")
        for variable, definition_ids in variable_map.items():
            sorted_defs = sorted(definition_ids, key=lambda d: int(d[1:]))
            statements = [definitions[def_id].statement.replace("|", "\\|") for def_id in sorted_defs]
            parts.append(
                f"| {variable} | {', '.join(sorted_defs)} | {'<br>'.join(f'`{stmt}`' for stmt in statements)} |"
            )
        parts.append("")
    destination.write_text("\n".join(parts), encoding="utf-8")


def write_program_summary(program_name: str, metrics: Dict[str, int], destination: Path) -> None:
    summary = {
        "program": program_name,
        "metrics": metrics,
    }
    destination.write_text(json.dumps(summary, indent=2), encoding="utf-8")


def plot_cyclomatic_complexity(
    measurements: Sequence[Dict[str, object]], destination: Path
) -> None:
    labels = [str(item["program"]) for item in measurements]
    values = [int(item["cc"]) for item in measurements]
    plt.figure(figsize=(8, 4))
    plt.bar(labels, values, color="#4a90e2")
    plt.title("Cyclomatic Complexity per Program")
    plt.xlabel("Program")
    plt.ylabel("Cyclomatic Complexity")
    plt.tight_layout()
    plt.savefig(destination, dpi=150)
    plt.close()
