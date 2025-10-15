from __future__ import annotations

import argparse
from pathlib import Path
from typing import Dict, List

from analyzer.c_parser_adapter import find_main_function, parse_c_file
from analyzer.cfg_builder import build_cfg_from_function
from analyzer.dataflow import compute_reaching_definitions, find_ambiguous_variables
from analyzer.report import (
    plot_cyclomatic_complexity,
    write_ambiguity_report,
    write_cfg_dot,
    write_definitions_table,
    write_iteration_tables,
    write_program_summary,
    render_dot_to_png,
)

PROGRAMS_DIR = Path("lab7/programs")
OUTPUT_DIR = Path("lab7/output")


def analyze_program(program_path: Path) -> Dict[str, int]:
    ast = parse_c_file(str(program_path))
    main_function = find_main_function(ast)
    cfg = build_cfg_from_function(main_function)

    snapshots = compute_reaching_definitions(cfg)
    ambiguous = find_ambiguous_variables(cfg)

    nodes = len(cfg.blocks)
    edges = sum(len(block.successors) for block in cfg.blocks)
    cyclomatic_complexity = edges - nodes + 2

    program_name = program_path.stem
    program_output_dir = OUTPUT_DIR / program_name
    program_output_dir.mkdir(parents=True, exist_ok=True)

    dot_path = program_output_dir / "cfg.dot"
    write_cfg_dot(cfg, dot_path)
    render_dot_to_png(dot_path)
    write_definitions_table(cfg.definitions, program_output_dir / "definitions.md")
    write_iteration_tables(snapshots, cfg, program_output_dir / "reaching_definitions_iterations.md")
    write_ambiguity_report(ambiguous, cfg.definitions, program_output_dir / "ambiguity.md")
    write_program_summary(
        program_name,
        {"nodes": nodes, "edges": edges, "cc": cyclomatic_complexity},
        program_output_dir / "summary.json",
    )

    return {"program": program_name, "nodes": nodes, "edges": edges, "cc": cyclomatic_complexity}


def generate_metrics_summary(metrics: List[Dict[str, int]]) -> None:
    rows = [
        "| Program | Nodes (N) | Edges (E) | Cyclomatic Complexity (CC) |",
        "|---------|-----------|-----------|----------------------------|",
    ]
    for entry in metrics:
        rows.append(
            f"| {entry['program']} | {entry['nodes']} | {entry['edges']} | {entry['cc']} |"
        )
    (OUTPUT_DIR / "metrics_summary.md").write_text("\n".join(rows), encoding="utf-8")
    plot_cyclomatic_complexity(metrics, OUTPUT_DIR / "cyclomatic_complexity.png")


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run reaching definitions analysis on C programs.")
    parser.add_argument(
        "--programs-dir",
        type=Path,
        default=PROGRAMS_DIR,
        help="Directory containing C source files to analyze.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=OUTPUT_DIR,
        help="Directory where analysis artifacts will be written.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_arguments()
    programs_dir: Path = args.programs_dir
    global OUTPUT_DIR
    OUTPUT_DIR = args.output_dir
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    program_files = sorted(programs_dir.glob("*.c"))
    if not program_files:
        raise FileNotFoundError(f"No C source files found in {programs_dir}.")

    metrics: List[Dict[str, int]] = []
    for program_file in program_files:
        metrics.append(analyze_program(program_file))
    generate_metrics_summary(metrics)


if __name__ == "__main__":
    main()
