# parse file to SourceFile object (filename and source lines)
# convert SourceFile to ast object
# extract the imports from the sourcefile object (tuple of str)
# extract non-imports from SourceFile object, whose name is snake case version of class name (set of sourcefile objects)
# compile list of imports of newly created files
# combine the above 3 items in sourcefiles
# write all SourceFile object to actual files in new module named after original file
# purge unused imports
# clean code style for imports
# include imports in __init__.py

# SOMEWHERE:
# deal with comments

from __future__ import annotations
import ast
from dataclasses import dataclass
from pathlib import Path

from utils import to_snake_case


@dataclass(frozen=True)
class SourceFile:
    filename: str
    lines: tuple[str, ...]

    @classmethod
    def from_file(cls, path: str) -> SourceFile:
        ...

    def parse(self) -> ast.Module:
        source = '\n'.join(self.lines)
        return ast.parse(source=source, filename=self.filename)

    def write(self, path: Path) -> None:
        ...


def get_imports(source_file: SourceFile) -> tuple[str, ...]:
    import_line_numbers: list[int] = []
    for node in source_file.parse().body:
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            # ast line numbers are 1-indexed
            import_line_numbers.extend(
                range(node.lineno - 1, node.end_lineno)
            )

    return tuple(
        source_file.lines[line_number]
        for line_number in import_line_numbers
    )


def non_imports(source_file: SourceFile) -> set[SourceFile]:
    non_import_source_files = set()
    for node in source_file.parse().body:
        if not isinstance(node, (ast.Import, ast.ImportFrom)):
            offset = len(getattr(node, 'decorator_list', []))
            node_lines = tuple(
                source_file.lines[line_number]
                for line_number in range(
                    node.lineno - 1 - offset, node.end_lineno
                )
            )
            node_filename = to_snake_case(node.name) + '.py'
            non_import_source_files.add(
                SourceFile(
                    filename=node_filename,
                    lines=(*node_lines, '')
                )
            )

    return non_import_source_files


def add_imports(source_file: SourceFile, imports: tuple[str, ...]) -> SourceFile:
    return SourceFile(
        filename=source_file.filename,
        lines=(
            *imports,
            '',
            '',
            *source_file.lines,
        )
    )


def purge_unused_imports(source_file: SourceFile) -> SourceFile:
    # auto_flake
    ...
