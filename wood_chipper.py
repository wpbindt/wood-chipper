import ast
from dataclasses import dataclass
import re


@dataclass(frozen=True)
class SourceFile:
    filename: str
    lines: tuple[str]

    def parse(self) -> ast.Module:
        return ast.parse('\n'.join(self.lines), self.filename)


def get_import_lines(syntax_tree: ast.Module) -> list[int]:
    return [
        line_number
        for node in syntax_tree.body
        for line_number in range(node.lineno - 1, node.end_lineno)  # ast has 1-indexed line numbers
        if isinstance(node, (ast.Import, ast.ImportFrom))
    ]


def extract_imports(code: SourceFile) -> list[str]:
    syntax_tree = code.parse()
    import_lines = get_import_lines(syntax_tree)
    return [
        code.lines[import_lineno]
        for import_lineno in import_lines
    ]


def camel_to_snake(name: str) -> str:
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()


def break_up_source_file(code: SourceFile) -> set[SourceFile]:
    output = set()
    imports = extract_imports(code)
    non_imports = [
        node
        for node in code.parse().body
        if not isinstance(node, (ast.Import, ast.ImportFrom))
    ]
    for non_import in non_imports:
        output.add(SourceFile(
            lines=tuple([
                *imports,
                '',
                '',
                *code.lines[non_import.lineno - 1 - len(non_import.decorator_list): non_import.end_lineno],
                '',
            ]),
            filename=camel_to_snake(non_import.name) + '.py'
        ))

    return output
