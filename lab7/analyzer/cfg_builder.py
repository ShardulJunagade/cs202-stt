from dataclasses import dataclass, field
from typing import Dict, Iterable, List, Optional, Set, Tuple

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
        self._loop_stack: List[Tuple[BasicBlock, BasicBlock]] = []  # (break_target, continue_target)
        self._loop_continue_stack: List[BasicBlock] = []

    def build_from_source(self, body_source: str, start_line: int = 1) -> CFG:
        entry_block = self._new_block()
        open_blocks = {entry_block}
        stmts = self._tokenize_block(body_source, start_line)
        open_blocks = self._build_from_statements(stmts, open_blocks)
        exit_ids = {b.identifier for b in open_blocks if not b.terminated}
        self._compute_gen_kill_sets()
        return CFG(blocks=self._blocks, definitions=self._definitions, entry_id=entry_block.identifier, exit_ids=exit_ids)

    # ------------------------------------------------------------------
    # Core CFG construction helpers
    # ------------------------------------------------------------------
    def _build_from_statements(self, statements: Iterable[Tuple[str, int]], open_blocks: Set[BasicBlock]) -> Set[BasicBlock]:
        # Convert iterable to a queue we can mutate
        tokens = list(statements)
        return self._build_from_tokens(tokens, open_blocks)

    def _build_from_tokens(self, tokens: List[Tuple[str, int]], open_blocks: Set[BasicBlock]) -> Set[BasicBlock]:
        current_blocks = set(open_blocks)
        while tokens:
            text, line = tokens.pop(0)
            kind = self._classify_statement(text)
            if kind == 'block':
                inner = self._extract_block_inner(text, line)
                current_blocks = self._build_from_tokens(inner, current_blocks)
            elif kind == 'if':
                current_blocks = self._handle_if_with_tokens(text, line, tokens, current_blocks)
            elif kind == 'while':
                current_blocks = self._handle_while_with_tokens(text, line, tokens, current_blocks)
            elif kind == 'for':
                current_blocks = self._handle_for_with_tokens(text, line, tokens, current_blocks)
            elif kind == 'break':
                current_blocks = self._handle_break(text, line, current_blocks)
            elif kind == 'continue':
                current_blocks = self._handle_continue(text, line, current_blocks)
            elif kind == 'return':
                current_blocks = self._handle_return(text, line, current_blocks)
            elif kind == 'empty':
                continue
            else:
                current_blocks = self._handle_simple(text, line, current_blocks)
        return current_blocks

    # ------------------------------------------------------------------
    # Statement handlers
    # ------------------------------------------------------------------
    def _handle_simple(self, code: str, line: int, open_blocks: Set[BasicBlock]) -> Set[BasicBlock]:
        valid_blocks = self._filter_open_blocks(open_blocks)
        if not valid_blocks:
            return set()
        target_block = valid_blocks[0] if len(valid_blocks) == 1 and valid_blocks[0].open_for_append else self._materialize_block(valid_blocks)
        definition_ids = self._record_definitions_from_text(code, line, target_block.identifier)
        target_block.add_statement(Statement(text=code, line=line, node_type="Stmt", definition_ids=definition_ids))
        target_block.open_for_append = True
        return {target_block}

    def _handle_if_with_tokens(self, header: str, line: int, tokens: List[Tuple[str, int]], open_blocks: Set[BasicBlock]) -> Set[BasicBlock]:
        valid_blocks = self._filter_open_blocks(open_blocks)
        if not valid_blocks:
            return set()
        cond = self._extract_parenthesized(header)
        condition_block = self._new_block()
        condition_block.add_statement(Statement(text=f"if ({cond})", line=line, node_type="If"))
        for b in valid_blocks:
            b.add_edge(condition_block, None)
        # Parse then part next statement; it can be a block {...} or a single stmt
        then_stmts = self._consume_next_statement_from_tokens(tokens)
        then_entry = self._new_block()
        condition_block.add_edge(then_entry, "true")
        then_exits = self._build_from_statements(then_stmts, {then_entry})
        # Check for optional else
        else_exits: Set[BasicBlock] = set()
        if tokens and tokens[0][0].strip().startswith('else'):
            tokens.pop(0)  # consume 'else'
            else_stmts = self._consume_next_statement_from_tokens(tokens)
            else_entry = self._new_block()
            condition_block.add_edge(else_entry, "false")
            else_exits = self._build_from_statements(else_stmts, {else_entry})
        join = self._new_block()
        for eb in then_exits:
            if not eb.terminated:
                eb.add_edge(join, None)
        if else_exits:
            for eb in else_exits:
                if not eb.terminated:
                    eb.add_edge(join, None)
        else:
            condition_block.add_edge(join, "false")
        join.open_for_append = True
        return {join}

    def _handle_while_with_tokens(self, header: str, line: int, tokens: List[Tuple[str, int]], open_blocks: Set[BasicBlock]) -> Set[BasicBlock]:
        valid_blocks = self._filter_open_blocks(open_blocks)
        if not valid_blocks:
            return set()
        cond = self._extract_parenthesized(header) or 'true'
        cond_block = self._new_block()
        cond_block.add_statement(Statement(text=f"while ({cond})", line=line, node_type="While"))
        for b in valid_blocks:
            b.add_edge(cond_block, None)
        exit_block = self._new_block()
        body_entry = self._new_block()
        cond_block.add_edge(body_entry, "true")
        cond_block.add_edge(exit_block, "false")
        self._loop_stack.append((exit_block, cond_block))
        self._loop_continue_stack.append(cond_block)
        body_stmts = self._consume_next_statement_from_tokens(tokens)
        body_exits = self._build_from_statements(body_stmts, {body_entry})
        self._loop_stack.pop()
        self._loop_continue_stack.pop()
        for eb in body_exits:
            if not eb.terminated:
                eb.add_edge(cond_block, None)
        exit_block.open_for_append = True
        return {exit_block}

    def _handle_for_with_tokens(self, header: str, line: int, tokens: List[Tuple[str, int]], open_blocks: Set[BasicBlock]) -> Set[BasicBlock]:
        valid_blocks = self._filter_open_blocks(open_blocks)
        if not valid_blocks:
            return set()
        init, cond, it = self._split_for_header(header)
        current = set(valid_blocks)
        if init:
            current = self._handle_simple(init + ';', line, current)
        cond_block = self._new_block()
        cond_text = cond if cond else 'true'
        cond_block.add_statement(Statement(text=f"for-cond ({cond_text})", line=line, node_type="ForCond"))
        for b in current:
            b.add_edge(cond_block, None)
        exit_block = self._new_block()
        iter_target = None
        if it:
            iter_target = self._new_block()
        else:
            iter_target = cond_block
        body_entry = self._new_block()
        cond_block.add_edge(body_entry, "true")
        cond_block.add_edge(exit_block, "false")
        self._loop_stack.append((exit_block, iter_target))
        self._loop_continue_stack.append(iter_target)
        body_stmts = self._consume_next_statement_from_tokens(tokens)
        body_exits = self._build_from_statements(body_stmts, {body_entry})
        self._loop_stack.pop()
        self._loop_continue_stack.pop()
        live_exits = {b for b in body_exits if not b.terminated}
        if it:
            for b in live_exits:
                b.add_edge(iter_target, None)
            # iteration code is a simple statement
            it_exits = self._handle_simple(it + ';', line, {iter_target})
            for b in it_exits:
                if not b.terminated:
                    b.add_edge(cond_block, None)
        else:
            for b in live_exits:
                b.add_edge(cond_block, None)
        exit_block.open_for_append = True
        return {exit_block}

    def _handle_break(self, code: str, line: int, open_blocks: Set[BasicBlock]) -> Set[BasicBlock]:
        if not self._loop_stack:
            raise ValueError("Encountered 'break' outside of a loop.")
        break_target, _ = self._loop_stack[-1]
        return self._handle_jump_statement(code, line, open_blocks, break_target)

    def _handle_continue(self, code: str, line: int, open_blocks: Set[BasicBlock]) -> Set[BasicBlock]:
        if not self._loop_continue_stack:
            raise ValueError("Encountered 'continue' outside of a loop.")
        continue_target = self._loop_continue_stack[-1]
        return self._handle_jump_statement(code, line, open_blocks, continue_target)

    def _handle_return(self, code: str, line: int, open_blocks: Set[BasicBlock]) -> Set[BasicBlock]:
        valid_blocks = self._filter_open_blocks(open_blocks)
        result: Set[BasicBlock] = set()
        for b in valid_blocks:
            target = b if b.open_for_append and not b.terminated else self._materialize_block([b])
            def_ids = self._record_definitions_from_text(code, line, target.identifier)
            target.add_statement(Statement(text=code, line=line, node_type="Return", definition_ids=def_ids))
            target.terminated = True
            target.open_for_append = False
            result.add(target)
        return result

    def _handle_jump_statement(self, code: str, line: int, open_blocks: Set[BasicBlock], target_block: BasicBlock) -> Set[BasicBlock]:
        valid_blocks = self._filter_open_blocks(open_blocks)
        result: Set[BasicBlock] = set()
        for b in valid_blocks:
            target = b if b.open_for_append and not b.terminated else self._materialize_block([b])
            target.add_statement(Statement(text=code, line=line, node_type="Jump"))
            target.add_edge(target_block, None)
            target.terminated = True
            target.open_for_append = False
            result.add(target)
        return result

    # ------------------------------------------------------------------
    # Utility helpers
    # ------------------------------------------------------------------
    def _new_block(self) -> BasicBlock:
        identifier = f"B{self._block_counter}"
        self._block_counter += 1
        block = BasicBlock(identifier=identifier)
        self._blocks.append(block)
        return block

    def _materialize_block(self, predecessors: List[BasicBlock]) -> BasicBlock:
        block = self._new_block()
        for predecessor in predecessors:
            predecessor.add_edge(block, None)
        block.open_for_append = True
        return block

    def _filter_open_blocks(self, blocks: Iterable[BasicBlock]) -> List[BasicBlock]:
        return [block for block in blocks if not block.terminated]

    # --------------------- Tokenization & helpers ---------------------
    def _tokenize_block(self, text: str, start_line: int) -> List[Tuple[str, int]]:
        """Split block text into top-level statements preserving line numbers.

        Supports: simple statements ending with ';', blocks {...}, and headers like
        if (...), else, while (...), for (...). For headers that require a body, we
        leave a placeholder self._pending_tokens so handlers can consume the next
        statement as the body.
        """
        tokens: List[Tuple[str, int]] = []
        i = 0
        line = start_line
        n = len(text)
        while i < n:
            # skip whitespace
            if text[i].isspace():
                if text[i] == '\n':
                    line += 1
                i += 1
                continue
            start_i = i
            start_line_cur = line
            ch = text[i]
            if ch == '{':
                # capture block
                depth = 0
                while i < n:
                    if text[i] == '{':
                        depth += 1
                    elif text[i] == '}':
                        depth -= 1
                        if depth == 0:
                            i += 1
                            break
                    if text[i] == '\n':
                        line += 1
                    i += 1
                tokens.append((text[start_i:i], start_line_cur))
            else:
                # read until ';' or '{' starts a block (header) at top-level
                par = 0
                while i < n:
                    c = text[i]
                    if c == '\n':
                        line += 1
                    if c == '(':
                        par += 1
                    elif c == ')':
                        par = max(0, par - 1)
                    if c == ';' and par == 0:
                        i += 1
                        tokens.append((text[start_i:i].strip(), start_line_cur))
                        break
                    if c == '{' and par == 0:
                        # header like if(...) { ... } will be tokenized as two tokens:
                        tokens.append((text[start_i:i].strip(), start_line_cur))
                        # now parse the block
                        start_block_line = line
                        depth = 0
                        block_start = i
                        while i < n:
                            if text[i] == '{':
                                depth += 1
                            elif text[i] == '}':
                                depth -= 1
                                if depth == 0:
                                    i += 1
                                    break
                            if text[i] == '\n':
                                line += 1
                            i += 1
                        tokens.append((text[block_start:i], start_block_line))
                        break
                    i += 1
                else:
                    # end of text without ';'
                    segment = text[start_i:].strip()
                    if segment:
                        tokens.append((segment, start_line_cur))
                    i = n
        # prepare a queue for consumption by control handlers
        self._pending_tokens = list(tokens)
        return self._pop_all()

    def _pop_all(self) -> List[Tuple[str, int]]:
        result = self._pending_tokens
        self._pending_tokens = []
        return result

    def _consume_next_statement_from_tokens(self, tokens: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
        if not tokens:
            return []
        tok, line = tokens.pop(0)
        if tok.startswith('{'):
            inner = tok[1:-1]
            return self._tokenize_block(inner, line)
        else:
            return [(tok, line)]

    def _extract_block_inner(self, tok: str, line: int) -> List[Tuple[str, int]]:
        assert tok.startswith('{') and tok.endswith('}')
        inner = tok[1:-1]
        return self._tokenize_block(inner, line)

    def _classify_statement(self, code: str) -> str:
        s = code.strip()
        if not s or s == ';':
            return 'empty'
        if s.startswith('{'):
            return 'block'
        if s.startswith('if') and '(' in s:
            return 'if'
        if s.startswith('else'):
            return 'else'  # handled via lookahead in _handle_if
        if s.startswith('while') and '(' in s:
            return 'while'
        if s.startswith('for') and '(' in s:
            return 'for'
        if s.startswith('return'):
            return 'return'
        if s.startswith('break'):
            return 'break'
        if s.startswith('continue'):
            return 'continue'
        return 'stmt'

    def _extract_parenthesized(self, header: str) -> str:
        # returns content inside the first top-level ( ... )
        start = header.find('(')
        if start == -1:
            return ''
        depth = 0
        for i in range(start, len(header)):
            c = header[i]
            if c == '(':
                depth += 1
            elif c == ')':
                depth -= 1
                if depth == 0:
                    return header[start + 1:i].strip()
        return ''

    def _split_for_header(self, header: str) -> Tuple[str, str, str]:
        # header like 'for (init; cond; it)'
        inside = self._extract_parenthesized(header)
        parts = [p.strip() for p in inside.split(';')]
        while len(parts) < 3:
            parts.append('')
        return parts[0], parts[1], parts[2]

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
    return builder.build_from_source(body_source, start_line)
