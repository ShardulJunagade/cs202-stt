from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Iterable, List, Optional, Set, Tuple

from pycparser import c_ast, c_generator


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
        self.generator = c_generator.CGenerator()
        self._block_counter = 0
        self._definition_counter = 0
        self._blocks: List[BasicBlock] = []
        self._definitions: Dict[str, Definition] = {}
        self._var_to_defs: Dict[str, Set[str]] = {}
        self._loop_stack: List[Tuple[BasicBlock, BasicBlock]] = []
        self._loop_continue_stack: List[BasicBlock] = []

    def build(self, function_body: c_ast.Compound) -> CFG:
        entry_block = self._new_block()
        entry_block.open_for_append = True
        open_blocks = {entry_block}
        statements = self._normalize_block_items(function_body.block_items)
        open_blocks = self._build_from_statements(statements, open_blocks)
        exit_ids = {block.identifier for block in open_blocks if not block.terminated}
        self._compute_gen_kill_sets()
        return CFG(
            blocks=self._blocks,
            definitions=self._definitions,
            entry_id=entry_block.identifier,
            exit_ids=exit_ids,
        )

    # ------------------------------------------------------------------
    # Core CFG construction helpers
    # ------------------------------------------------------------------
    def _build_from_statements(
        self, statements: Iterable[c_ast.Node], open_blocks: Set[BasicBlock]
    ) -> Set[BasicBlock]:
        current_blocks = set(open_blocks)
        for statement in statements:
            handler = self._dispatch_handler(statement)
            current_blocks = handler(statement, current_blocks)
        return current_blocks

    def _dispatch_handler(self, statement: c_ast.Node):
        if isinstance(statement, c_ast.Compound):
            return self._handle_compound
        if isinstance(statement, c_ast.If):
            return self._handle_if
        if isinstance(statement, c_ast.While):
            return self._handle_while
        if isinstance(statement, c_ast.For):
            return self._handle_for
        if isinstance(statement, c_ast.Break):
            return self._handle_break
        if isinstance(statement, c_ast.Continue):
            return self._handle_continue
        if isinstance(statement, c_ast.Return):
            return self._handle_return
        if isinstance(statement, c_ast.EmptyStatement):
            return self._handle_empty
        if isinstance(statement, c_ast.Switch):
            raise NotImplementedError("Switch statements are not supported in this analyzer.")
        return self._handle_simple

    # ------------------------------------------------------------------
    # Statement handlers
    # ------------------------------------------------------------------
    def _handle_compound(
        self, statement: c_ast.Compound, open_blocks: Set[BasicBlock]
    ) -> Set[BasicBlock]:
        items = self._normalize_block_items(statement.block_items)
        return self._build_from_statements(items, open_blocks)

    def _handle_empty(
        self, statement: c_ast.EmptyStatement, open_blocks: Set[BasicBlock]
    ) -> Set[BasicBlock]:
        return open_blocks

    def _handle_simple(
        self, statement: c_ast.Node, open_blocks: Set[BasicBlock]
    ) -> Set[BasicBlock]:
        valid_blocks = self._filter_open_blocks(open_blocks)
        if not valid_blocks:
            return set()
        if len(valid_blocks) == 1 and valid_blocks[0].open_for_append:
            target_block = valid_blocks[0]
        else:
            target_block = self._materialize_block(valid_blocks)
        code = self._generate_code(statement)
        line = self._extract_line(statement)
        definition_ids = self._record_definitions(statement, code, line, target_block.identifier)
        target_block.add_statement(
            Statement(text=code, line=line, node_type=type(statement).__name__, definition_ids=definition_ids)
        )
        target_block.open_for_append = True
        return {target_block}

    def _handle_if(self, statement: c_ast.If, open_blocks: Set[BasicBlock]) -> Set[BasicBlock]:
        valid_blocks = self._filter_open_blocks(open_blocks)
        if not valid_blocks:
            return set()
        condition_block = self._new_block()
        condition_block.open_for_append = False
        cond_text = f"if ({self._generate_expression(statement.cond)})"
        line = self._extract_line(statement.cond or statement)
        condition_block.add_statement(Statement(text=cond_text, line=line, node_type="If"))
        for block in valid_blocks:
            block.add_edge(condition_block, None)
        then_entry = self._new_block()
        condition_block.add_edge(then_entry, "true")
        then_items = self._normalize_block_items(statement.iftrue)
        then_exits = self._build_from_statements(then_items, {then_entry})
        else_items = self._normalize_block_items(statement.iffalse)
        join_block = self._new_block()
        for exit_block in then_exits:
            if not exit_block.terminated:
                exit_block.add_edge(join_block, None)
        if else_items:
            else_entry = self._new_block()
            condition_block.add_edge(else_entry, "false")
            else_exits = self._build_from_statements(else_items, {else_entry})
            for exit_block in else_exits:
                if not exit_block.terminated:
                    exit_block.add_edge(join_block, None)
        else:
            condition_block.add_edge(join_block, "false")
        join_block.open_for_append = True
        return {join_block}

    def _handle_while(self, statement: c_ast.While, open_blocks: Set[BasicBlock]) -> Set[BasicBlock]:
        valid_blocks = self._filter_open_blocks(open_blocks)
        if not valid_blocks:
            return set()
        condition_block = self._new_block()
        line = self._extract_line(statement.cond or statement)
        cond_expr = self._generate_expression(statement.cond) if statement.cond is not None else "true"
        condition_block.add_statement(
            Statement(text=f"while ({cond_expr})", line=line, node_type="While")
        )
        condition_block.open_for_append = False
        for block in valid_blocks:
            block.add_edge(condition_block, None)
        exit_block = self._new_block()
        body_entry = self._new_block()
        condition_block.add_edge(body_entry, "true")
        condition_block.add_edge(exit_block, "false")
        self._loop_stack.append((exit_block, condition_block))
        self._loop_continue_stack.append(condition_block)
        body_items = self._normalize_block_items(statement.stmt)
        body_exits = self._build_from_statements(body_items, {body_entry})
        self._loop_stack.pop()
        self._loop_continue_stack.pop()
        for exit_candidate in body_exits:
            if not exit_candidate.terminated:
                exit_candidate.add_edge(condition_block, None)
        exit_block.open_for_append = True
        return {exit_block}

    def _handle_for(self, statement: c_ast.For, open_blocks: Set[BasicBlock]) -> Set[BasicBlock]:
        valid_blocks = self._filter_open_blocks(open_blocks)
        if not valid_blocks:
            return set()
        current_blocks = set(valid_blocks)
        init_statements = self._normalize_for_part(statement.init)
        for init_stmt in init_statements:
            current_blocks = self._handle_simple(init_stmt, current_blocks)
        condition_block = self._new_block()
        cond_expr = self._generate_expression(statement.cond) if statement.cond is not None else "true"
        line = self._extract_line(statement.cond or statement)
        condition_block.add_statement(
            Statement(text=f"for-cond ({cond_expr})", line=line, node_type="ForCond")
        )
        condition_block.open_for_append = False
        for block in current_blocks:
            block.add_edge(condition_block, None)
        exit_block = self._new_block()
        iter_target: BasicBlock
        iter_statements = self._normalize_for_part(statement.next)
        if iter_statements:
            iter_target = self._new_block()
        else:
            iter_target = condition_block
        body_entry = self._new_block()
        condition_block.add_edge(body_entry, "true")
        condition_block.add_edge(exit_block, "false")
        self._loop_stack.append((exit_block, iter_target))
        self._loop_continue_stack.append(iter_target)
        body_items = self._normalize_block_items(statement.stmt)
        body_exits = self._build_from_statements(body_items, {body_entry})
        self._loop_stack.pop()
        self._loop_continue_stack.pop()
        live_body_exits = {b for b in body_exits if not b.terminated}
        if iter_statements:
            for block in live_body_exits:
                block.add_edge(iter_target, None)
            iter_exits = {iter_target}
            for iter_stmt in iter_statements:
                iter_exits = self._handle_simple(iter_stmt, iter_exits)
            iter_exits = {b for b in iter_exits if not b.terminated}
            for block in iter_exits:
                block.add_edge(condition_block, None)
        else:
            for block in live_body_exits:
                block.add_edge(condition_block, None)
        exit_block.open_for_append = True
        return {exit_block}

    def _handle_break(self, statement: c_ast.Break, open_blocks: Set[BasicBlock]) -> Set[BasicBlock]:
        if not self._loop_stack:
            raise ValueError("Encountered 'break' outside of a loop.")
        break_target, _ = self._loop_stack[-1]
        return self._handle_jump_statement(statement, open_blocks, break_target, "break;")

    def _handle_continue(
        self, statement: c_ast.Continue, open_blocks: Set[BasicBlock]
    ) -> Set[BasicBlock]:
        if not self._loop_continue_stack:
            raise ValueError("Encountered 'continue' outside of a loop.")
        continue_target = self._loop_continue_stack[-1]
        return self._handle_jump_statement(statement, open_blocks, continue_target, "continue;")

    def _handle_return(self, statement: c_ast.Return, open_blocks: Set[BasicBlock]) -> Set[BasicBlock]:
        valid_blocks = self._filter_open_blocks(open_blocks)
        result_blocks: Set[BasicBlock] = set()
        code = self._generate_code(statement)
        line = self._extract_line(statement)
        for block in valid_blocks:
            target = block if block.open_for_append and not block.terminated else self._materialize_block([block])
            definition_ids = self._record_definitions(statement, code, line, target.identifier)
            target.add_statement(
                Statement(text=code, line=line, node_type="Return", definition_ids=definition_ids)
            )
            target.terminated = True
            target.open_for_append = False
            result_blocks.add(target)
        return result_blocks

    def _handle_jump_statement(
        self,
        statement: c_ast.Node,
        open_blocks: Set[BasicBlock],
        target_block: BasicBlock,
        text: str,
    ) -> Set[BasicBlock]:
        valid_blocks = self._filter_open_blocks(open_blocks)
        result_blocks: Set[BasicBlock] = set()
        line = self._extract_line(statement)
        for block in valid_blocks:
            target = block if block.open_for_append and not block.terminated else self._materialize_block([block])
            target.add_statement(Statement(text=text, line=line, node_type=type(statement).__name__))
            target.add_edge(target_block, None)
            target.terminated = True
            target.open_for_append = False
            result_blocks.add(target)
        return result_blocks

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

    def _normalize_block_items(self, items: Optional[Iterable[c_ast.Node]]) -> List[c_ast.Node]:
        if items is None:
            return []
        if isinstance(items, c_ast.Node):
            if isinstance(items, c_ast.Compound):
                return self._normalize_block_items(items.block_items)
            if isinstance(items, c_ast.EmptyStatement):
                return []
            if isinstance(items, c_ast.DeclList):
                return list(items.decls)
            return [items]
        normalized: List[c_ast.Node] = []
        for item in items:
            if isinstance(item, c_ast.DeclList):
                normalized.extend(item.decls)
            else:
                normalized.append(item)
        return normalized

    def _normalize_for_part(self, node: Optional[c_ast.Node]) -> List[c_ast.Node]:
        if node is None:
            return []
        if isinstance(node, c_ast.ExprList):
            return list(node.exprs)
        if isinstance(node, c_ast.DeclList):
            return list(node.decls)
        return [node]

    def _generate_code(self, node: c_ast.Node) -> str:
        return self.generator.visit(node).strip()

    def _generate_expression(self, node: Optional[c_ast.Node]) -> str:
        if node is None:
            return ""
        return self.generator.visit(node).strip()

    def _extract_line(self, node: Optional[c_ast.Node]) -> int:
        if node is None or node.coord is None:
            return -1
        return node.coord.line

    def _record_definitions(
        self,
        node: c_ast.Node,
        statement_text: str,
        line: int,
        block_id: str,
    ) -> List[str]:
        variables = self._extract_defined_variables(node)
        definition_ids: List[str] = []
        for variable in variables:
            identifier = self._new_definition_id()
            definition = Definition(
                identifier=identifier,
                variable=variable,
                statement=statement_text,
                line=line,
                block_id=block_id,
            )
            self._definitions[identifier] = definition
            self._var_to_defs.setdefault(variable, set()).add(identifier)
            definition_ids.append(identifier)
        return definition_ids

    def _extract_defined_variables(self, node: c_ast.Node) -> Set[str]:
        variables: Set[str] = set()
        if isinstance(node, c_ast.Assignment):
            target = self._resolve_lvalue(node.lvalue)
            if target:
                variables.add(target)
        elif isinstance(node, c_ast.Decl):
            if node.name:
                variables.add(node.name)
        elif isinstance(node, c_ast.UnaryOp) and node.op in {"p++", "p--", "++", "--"}:
            target = self._resolve_lvalue(node.expr)
            if target:
                variables.add(target)
        return variables

    def _resolve_lvalue(self, node: Optional[c_ast.Node]) -> Optional[str]:
        if node is None:
            return None
        if isinstance(node, c_ast.ID):
            return node.name
        if isinstance(node, c_ast.ArrayRef):
            return self._resolve_lvalue(node.name)
        if isinstance(node, c_ast.StructRef):
            base = self._resolve_lvalue(node.name)
            if base and isinstance(node.field, c_ast.ID):
                return f"{base}.{node.field.name}"
        return None

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


def build_cfg_from_function(function: c_ast.FuncDef) -> CFG:
    body = function.body
    builder = CFGBuilder()
    return builder.build(body)
