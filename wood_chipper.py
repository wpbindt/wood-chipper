# compile list of imports of newly created files
# combine the above 3 items in sourcefiles
# write all SourceFile object to actual files in new module named after original file
# purge unused imports
# clean code style for imports
# include imports in __init__.py

# SOMEWHERE:
# deal with comments

import ast

import autoflake  # type: ignore

from node_to_source_file import node_to_source_file
from source_file import SourceFile


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


def get_non_imports(source_file: SourceFile) -> set[SourceFile]:
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
    imports = get_imports(source_file)
    non_imports = get_non_imports(source_file)
    return {
        purge_unused_imports(add_imports(non_import, imports))
        for non_import in non_imports
    }
