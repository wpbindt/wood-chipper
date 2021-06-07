import ast
import re
from source_file import SourceFile


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


def node_to_source_lines(
    node: ast.AST,
    context: SourceFile
) -> tuple[str, ...]:
    offset = len(getattr(node, 'decorator_list', []))
    node_lines = tuple(
        context.lines[line_number]
        for line_number in range(
            node.lineno - 1 - offset, node.end_lineno
        )
    )
    return (*node_lines, '')


def node_to_source_file(
    node: ast.AST,
    context: SourceFile
) -> SourceFile:
    return SourceFile(
        filename=node_to_filename(node),
        lines=node_to_source_lines(node, context)
    )
