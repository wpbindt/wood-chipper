import ast
import re

from ast_utils import ast_stmt_to_name
from source_file import SourceFile


def to_snake_case(name: str) -> str:
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()


def ast_stmt_to_filename(statement: ast.stmt) -> str:
    return to_snake_case(ast_stmt_to_name(statement)) + '.py'


def node_to_source_lines(
    node: ast.stmt,
    context: SourceFile
) -> tuple[str, ...]:
    offset = len(getattr(node, 'decorator_list', []))
    node_lines = tuple(
        context.lines[line_number]
        for line_number in range(
            node.lineno - 1 - offset, node.end_lineno
        )
    )
    return *node_lines, ''


def node_to_source_file(
    node: ast.stmt,
    context: SourceFile
) -> SourceFile:
    return SourceFile(
        filename=ast_stmt_to_filename(node),
        lines=node_to_source_lines(node, context)
    )
