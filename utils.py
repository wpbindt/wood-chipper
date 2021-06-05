import ast
import re


def to_snake_case(name: str) -> str:
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()


def node_to_filename(node: ast.AST) -> str:
    node_name = getattr(node, 'name', None)
    if node_name is None:
        raise ValueError(
            f'Nameless top-level node on line {getattr(node, "lineno", "??")}'
        )
    return to_snake_case(node_name) + '.py'
