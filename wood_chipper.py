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
from os import PathLike

import autoflake  # type: ignore

from source_file import SourceFile
from node_to_source_file import node_to_source_file


def get_imports(source_file: SourceFile) -> tuple[str, ...]:
    import_line_numbers: list[int] = []
    for node in source_file.parse():
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
    return {
        node_to_source_file(node=node, context=source_file)
        for node in source_file.parse()
        if not isinstance(node, (ast.Import, ast.ImportFrom))
    }


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
    code_without_unused_imports = autoflake.fix_code(
        str(source_file),
        remove_all_unused_imports=True
    )
    return SourceFile(
        filename=source_file.filename,
        lines=tuple(code_without_unused_imports.split('\n'))
    )


def chip_wood(source_file: SourceFile) -> set[SourceFile]:
    ...
