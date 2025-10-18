from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set, Tuple

import re


@dataclass
class Definition:
    identifier: str
    variable: str
    statement: str
    line: int
    block_id: Optional[str]


@dataclass
class Statement:
    text: str
    line: int
    node_type: str
    definition_ids: List[str] = field(default_factory=list)


@dataclass
class Edge:
    target: str
    label: Optional[str] = None


@dataclass
class BasicBlock:
    identifier: str
    statements: List[Statement] = field(default_factory=list)
    successors: List[Edge] = field(default_factory=list)
    predecessors: Set[str] = field(default_factory=set)
    gen: List[str] = field(default_factory=list)
    kill: Set[str] = field(default_factory=set)
    in_set: Set[str] = field(default_factory=set)
    out_set: Set[str] = field(default_factory=set)
    open_for_append: bool = True
    terminated: bool = False

    # Allow blocks to be placed in sets by hashing on stable identifier
    def __hash__(self) -> int:  # type: ignore[override]
        return hash(self.identifier)

    def add_statement(self, statement: Statement) -> None:
        self.statements.append(statement)

    def add_edge(self, target: "BasicBlock", label: Optional[str]) -> None:
        self.successors.append(Edge(target.identifier, label))
        target.predecessors.add(self.identifier)
        self.open_for_append = False


@dataclass
class CFG:
    blocks: List[BasicBlock]
    definitions: Dict[str, Definition]
    entry_id: str
    exit_ids: Set[str]

    @property
    def block_map(self) -> Dict[str, BasicBlock]:
        return {block.identifier: block for block in self.blocks}


class CFGBuilder:
    def __init__(self) -> None:
        self._block_counter = 0
        self._definition_counter = 0
        self._blocks: List[BasicBlock] = []
        self._definitions: Dict[str, Definition] = {}
        self._var_to_defs: Dict[str, Set[str]] = {}
        # Leader-based only in submission

    # ---------------- Leader-based builder per README -----------------
    def build_from_source_leaders(self, body_source: str, start_line: int = 1) -> CFG:
        lines = self._linearize_code(body_source, start_line)
        if not lines:
            # still return empty cfg with one empty block
            empty = self._new_block()
            cfg = CFG(blocks=self._blocks, definitions=self._definitions, entry_id=empty.identifier, exit_ids={empty.identifier})
            self._compute_gen_kill_sets()
            return cfg
        leaders = self._find_leaders(lines)
        blocks_meta = self._form_basic_blocks(lines, leaders)
        # Materialize BasicBlock nodes and statements
        name_to_block: Dict[str, BasicBlock] = {}
        for name, start_idx, line_slices in blocks_meta:
            block = self._new_block()
            # Ensure identifier matches planned name
            block.identifier = name
            name_to_block[name] = block
            # Add statements
            for text, line in line_slices:
                def_ids = self._record_definitions_from_text(text, line, block.identifier)
                block.add_statement(Statement(text=text, line=line, node_type="Stmt", definition_ids=def_ids))
            block.open_for_append = True
        # Reorder self._blocks to match names order
        ordered_blocks: List[BasicBlock] = [name_to_block[f"B{i}"] for i in range(len(blocks_meta))]
        self._blocks = ordered_blocks
        # Build edges per simplified rules
        edges = self._build_edges_from_blocks(lines, blocks_meta)
        for src, dst, label in edges:
            name_to_block[src].add_edge(name_to_block[dst], label or None)
        entry_id = blocks_meta[0][0]
        exit_ids = {b.identifier for b in self._blocks if not b.terminated}
        self._compute_gen_kill_sets()
        return CFG(blocks=self._blocks, definitions=self._definitions, entry_id=entry_id, exit_ids=exit_ids)

    # ---------------- Leader-based helpers -----------------
    _COND_RE = re.compile(r'^\s*(if|else\s*if|else|while|for)\b')
    _JUMP_RE = re.compile(r'^\s*(return|break|continue|goto)\b')

    def _linearize_code(self, text: str, start_line: int) -> List[Tuple[str, int]]:
        """Return list of (line_text, line_no) excluding standalone braces/semicolons and empties."""
        out: List[Tuple[str, int]] = []
        line_no = start_line
        for raw in text.splitlines():
            s = raw.strip()
            if not s:
                line_no += 1
                continue
            if s in {'{', '}', ';'}:
                line_no += 1
                continue
            out.append((s, line_no))
            line_no += 1
        return out

    def _is_cond_or_loop(self, line: str) -> bool:
        return bool(self._COND_RE.match(line))

    def _is_jump(self, line: str) -> bool:
        return bool(self._JUMP_RE.match(line))

    def _find_leaders(self, lines: List[Tuple[str, int]]) -> List[int]:
        leaders: Set[int] = set()
        if lines:
            leaders.add(0)
        n = len(lines)
        for i, (txt, _) in enumerate(lines):
            if self._is_cond_or_loop(txt):
                leaders.add(i)
                if i + 1 < n:
                    leaders.add(i + 1)
            if self._is_jump(txt):
                if i + 1 < n:
                    leaders.add(i + 1)
            if txt.startswith('else'):
                leaders.add(i)
        return sorted(leaders)

    def _form_basic_blocks(self, lines: List[Tuple[str, int]], leaders: List[int]) -> List[Tuple[str, int, List[Tuple[str, int]]]]:
        blocks: List[Tuple[str, int, List[Tuple[str, int]]]] = []
        if not leaders:
            return blocks
        leaders_sorted = sorted(leaders)
        for idx, start in enumerate(leaders_sorted):
            end = leaders_sorted[idx + 1] if idx + 1 < len(leaders_sorted) else len(lines)
            slice_lines = lines[start:end]
            blocks.append((f"B{idx}", start, slice_lines))
        return blocks

    def _build_edges_from_blocks(self, lines: List[Tuple[str, int]], blocks: List[Tuple[str, int, List[Tuple[str, int]]]]) -> List[Tuple[str, str, str]]:
        edges: List[Tuple[str, str, str]] = []
        n = len(blocks)
        for i, (bname, _start_idx, blines) in enumerate(blocks):
            if not blines:
                if i + 1 < n:
                    edges.append((bname, f"B{i+1}", ""))
                continue
            first = blines[0][0]
            last = blines[-1][0]
            cond = self._is_cond_or_loop(first)
            jump = self._is_jump(last)
            if cond:
                if i + 1 < n:
                    edges.append((bname, f"B{i+1}", "true"))
                if i + 2 < n:
                    edges.append((bname, f"B{i+2}", "false"))
                if first.startswith('while') or first.startswith('for'):
                    if i + 1 < n:
                        edges.append((f"B{i+1}", bname, "back"))
            elif not jump:
                if i + 1 < n:
                    edges.append((bname, f"B{i+1}", ""))
        # de-duplicate
        seen: Set[Tuple[str, str, str]] = set()
        uniq: List[Tuple[str, str, str]] = []
        for e in edges:
            if e not in seen:
                uniq.append(e)
                seen.add(e)
        return uniq

    # ------------------------------------------------------------------
    # Construction utilities
    # ------------------------------------------------------------------
    def _new_block(self) -> BasicBlock:
        identifier = f"B{self._block_counter}"
        self._block_counter += 1
        block = BasicBlock(identifier=identifier)
        self._blocks.append(block)
        return block

    # --------------------- Definitions extraction ---------------------
    def _record_definitions_from_text(self, statement_text: str, line: int, block_id: str) -> List[str]:
        vars_defined = self._extract_defined_variables_from_text(statement_text)
        ids: List[str] = []
        for var in vars_defined:
            did = self._new_definition_id()
            self._definitions[did] = Definition(identifier=did, variable=var, statement=statement_text.strip(), line=line, block_id=block_id)
            self._var_to_defs.setdefault(var, set()).add(did)
            ids.append(did)
        return ids

    def _extract_defined_variables_from_text(self, text: str) -> Set[str]:
        s = text.strip().rstrip(';')
        vars_defined: Set[str] = set()
        # handle declarations like 'int x = 0;' or 'int x, y;'
        decl_match = re.match(r"(int|float|double|char|long|short|unsigned|signed)\b(.*)", s)
        if decl_match:
            rest = decl_match.group(2)
            # split by commas outside parentheses
            parts = [p.strip() for p in rest.split(',')]
            for p in parts:
                name = re.split(r"\s|=|\[", p.strip())
                if name and name[0]:
                    vars_defined.add(name[0].lstrip('*'))
        # handle assignments like 'x = ...' and increments 'x++' '--x'
        assign = re.match(r"([A-Za-z_][A-Za-z0-9_\.]*)\s*([+\-*/%&|^]?=)", s)
        if assign:
            vars_defined.add(assign.group(1))
        inc = re.match(r"([A-Za-z_][A-Za-z0-9_\.]*)\s*(\+\+|--)$", s)
        pre_inc = re.match(r"(\+\+|--)\s*([A-Za-z_][A-Za-z0-9_\.]*)$", s)
        if inc:
            vars_defined.add(inc.group(1))
        if pre_inc:
            vars_defined.add(pre_inc.group(2))
        return vars_defined

    def _new_definition_id(self) -> str:
        self._definition_counter += 1
        return f"D{self._definition_counter}"

    def _compute_gen_kill_sets(self) -> None:
        for block in self._blocks:
            latest_by_var: Dict[str, str] = {}
            new_gen: List[str] = []
            for statement in block.statements:
                for definition_id in statement.definition_ids:
                    definition = self._definitions[definition_id]
                    previous = latest_by_var.get(definition.variable)
                    if previous and previous in new_gen:
                        new_gen.remove(previous)
                    latest_by_var[definition.variable] = definition_id
                    new_gen.append(definition_id)
            block.gen = new_gen
            kills: Set[str] = set()
            for variable, definition_id in latest_by_var.items():
                all_defs = self._var_to_defs.get(variable, set())
                kills.update(all_defs - {definition_id})
            block.kill = kills
            block.in_set = set()
            block.out_set = set(block.gen)


def build_cfg_from_main_source(body_source: str, start_line: int = 1) -> CFG:
    builder = CFGBuilder()
    # Use leader-based method per README instructions
    return builder.build_from_source_leaders(body_source, start_line)
