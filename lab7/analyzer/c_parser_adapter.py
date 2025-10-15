from __future__ import annotations

from typing import List

from pycparser import c_ast, c_parser


def _strip_preprocessor(source: str) -> str:
    lines: List[str] = []
    for line in source.splitlines():
        if line.lstrip().startswith("#"):
            lines.append("")
        else:
            lines.append(line)
    return "\n".join(lines)


def parse_c_file(path: str) -> c_ast.FileAST:
    parser = c_parser.CParser()
    with open(path, "r", encoding="utf-8") as handle:
        source = handle.read()
    stripped = _strip_preprocessor(source)
    return parser.parse(stripped, filename=path)


def find_main_function(ast: c_ast.FileAST) -> c_ast.FuncDef:
    for ext in ast.ext:
        if isinstance(ext, c_ast.FuncDef) and getattr(ext.decl, "name", None) == "main":
            return ext
    raise ValueError("No function named 'main' found in the provided file.")
