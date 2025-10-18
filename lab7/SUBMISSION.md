# CS202 Lab 7 — Submission

This repo contains my implementation for Lab 7: building a Control Flow Graph (CFG) and running Reaching Definitions on three C programs. I wrote a small, from-scratch analyzer in Python without using pycparser or any external parsing library.

## What I implemented

- CFG construction that follows the rules from the assignment README:
  - Find leaders: first instruction, every conditional/loop header (if/else/while/for), and the instruction immediately after a branch/jump (return/break/continue). “else” lines are treated as leaders too.
  - Form basic blocks by slicing the program between leaders.
  - Add edges:
    - Sequential: Bi → Bi+1 when the current block doesn’t end in a jump.
    - If/else: condition block → next block [true], and → block after next [false].
    - While/for: condition → body [true], condition → exit [false], plus a back-edge from body to condition.
- Reaching Definitions (intraprocedural):
  - Assign an ID (Dk) to each definition (simple regex for declarations, assignments, and ++/-- on variables).
  - Compute gen/kill for each block.
  - Iterate in/out sets until they stop changing.
- Reports/artifacts:
  - DOT + PNG for CFG (Graphviz),
  - Definitions table,
  - Reaching definitions iteration tables,
  - Ambiguity report (variables with multiple reaching definitions),
  - Metrics summary and a bar chart.

## How to run

- Programs live in `lab7/programs`. I analyzed three files: `inventory_tracker.c`, `student_performance.c`, and `weather_simulator.c`.
- To run the analyzer and generate outputs:

```powershell
python -u lab7/run_analysis.py --programs-dir lab7/programs --output-dir lab7/output
```

You should see a couple of short log lines per program. The outputs (DOT, PNG, tables) will be written under the chosen output folder, grouped by program name.

Graphviz: if `dot` isn’t in PATH, the script still writes the `.dot` file; PNG rendering is skipped with a friendly message.

## Notes on the parser

- I didn’t use a full C parser on purpose — the assignment allows a simplified approach. The code uses regex and line-based heuristics that work well for the provided programs.
- It covers the constructs required by the assignment: declarations, assignments, if/else, while, for, return, break, continue.
- It doesn’t support `switch`, `goto`, or complex type declarations. If needed, that can be added, but it wasn’t required here.

## Files I touched

- `lab7/analyzer/c_parser.py`: simple helpers to read a file, strip preprocessor lines and comments, and extract the `main()` body.
- `lab7/analyzer/cfg_builder.py`: leader-based CFG builder, basic blocks, edges, and definition extraction; also computes gen/kill.
- `lab7/analyzer/dataflow.py`: uses the CFG to compute reaching definitions.
- `lab7/analyzer/report.py`: writes DOT/PNG and markdown artifacts.
- `lab7/run_analysis.py`: ties everything together with minimal logging.

## What I checked

- Ran the analysis on the three programs and generated outputs in `lab7/output_leaders`.
- Verified node/edge counts and that the DOT files render (when Graphviz is available).
- Confirmed the iteration tables converge.

If you want me to tweak anything (e.g., else-if chains, more variable patterns, or extra visual styling), I can update quickly. 