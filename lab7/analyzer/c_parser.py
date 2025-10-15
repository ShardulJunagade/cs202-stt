from typing import Tuple


def read_c_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as handle:
        return handle.read()


def strip_preprocessor_and_comments(source: str) -> str:
    """Remove preprocessor lines and C/C++ style comments.

    This is a lightweight cleaner adequate for lab programs; it does not handle
    strings with comment-like content rigorously but works for typical inputs.
    """
    import re

    # Remove /* ... */ block comments (non-greedy, across lines)
    source = re.sub(r"/\*.*?\*/", "", source, flags=re.S)
    # Remove // line comments
    source = re.sub(r"//.*", "", source)
    # Remove preprocessor lines
    lines = []
    for line in source.splitlines():
        if line.lstrip().startswith("#"):
            lines.append("")
        else:
            lines.append(line)
    return "\n".join(lines)


def find_main_function_bounds(source: str) -> Tuple[int, int]:
    """Return (start_index, end_index) character offsets of main() body braces.

    start_index points to the first character after the opening '{'.
    end_index points to the closing '}' (exclusive).
    Raises ValueError if not found.
    """
    import re

    # Find 'main' function signature roughly
    match = re.search(r"\bint\s+main\s*\([^)]*\)\s*\{", source)
    if not match:
        # Try without assuming return type strictly
        match = re.search(r"\bmain\s*\([^)]*\)\s*\{", source)
    if not match:
        raise ValueError("No function named 'main' found in the provided file.")
    open_brace_idx = source.find("{", match.end() - 1)
    if open_brace_idx == -1:
        raise ValueError("Malformed main(): missing opening '{'.")
    depth = 0
    i = open_brace_idx
    while i < len(source):
        ch = source[i]
        if ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth == 0:
                # body is between open_brace_idx+1 and i (exclusive)
                return (open_brace_idx + 1, i)
        i += 1
    raise ValueError("Malformed main(): missing closing '}'.")


def extract_main_function_source(source: str) -> Tuple[str, int]:
    """Extract the body text of main() and its starting line number (1-based).

    Returns (body_text, start_line).
    """
    start, end = find_main_function_bounds(source)
    body = source[start:end]
    start_line = source[:start].count("\n") + 1
    return body, start_line
