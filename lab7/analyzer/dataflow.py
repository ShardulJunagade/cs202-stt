from typing import Dict, List, Set

from .cfg_builder import CFG, BasicBlock, Definition


def compute_reaching_definitions(cfg: CFG, max_iterations: int = 100) -> List[Dict[str, Dict[str, Set[str]]]]:
    block_map = cfg.block_map
    snapshots: List[Dict[str, Dict[str, Set[str]]]] = []
    initial_snapshot: Dict[str, Dict[str, Set[str]]] = {}
    for block in cfg.blocks:
        initial_snapshot[block.identifier] = {
            "gen": set(block.gen),
            "kill": set(block.kill),
            "in": set(block.in_set),
            "out": set(block.out_set),
        }
    snapshots.append(initial_snapshot)
    iteration = 0
    changed = True
    while changed and iteration < max_iterations:
        iteration += 1
        changed = False
        snapshot: Dict[str, Dict[str, Set[str]]] = {}
        for block in cfg.blocks:
            in_set: Set[str] = set()
            for predecessor_id in block.predecessors:
                predecessor = block_map[predecessor_id]
                in_set.update(predecessor.out_set)
            out_set = set(block.gen) | (in_set - block.kill)
            if in_set != block.in_set or out_set != block.out_set:
                block.in_set = in_set
                block.out_set = out_set
                changed = True
            snapshot[block.identifier] = {
                "gen": set(block.gen),
                "kill": set(block.kill),
                "in": set(block.in_set),
                "out": set(block.out_set),
            }
        snapshots.append(snapshot)
    return snapshots


def find_ambiguous_variables(cfg: CFG) -> Dict[str, Dict[str, Set[str]]]:
    ambiguous: Dict[str, Dict[str, Set[str]]] = {}
    for block in cfg.blocks:
        var_to_defs: Dict[str, Set[str]] = {}
        for definition_id in block.in_set:
            definition = cfg.definitions[definition_id]
            var_to_defs.setdefault(definition.variable, set()).add(definition_id)
        ambiguous_vars = {var: defs for var, defs in var_to_defs.items() if len(defs) > 1}
        if ambiguous_vars:
            ambiguous[block.identifier] = ambiguous_vars
    return ambiguous
