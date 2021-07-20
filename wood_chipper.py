# write all SourceFile object to actual files in new module named after original file
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


def top_level_object_name(source_file: SourceFile) -> str:
    node = source_file.parse()[0]
    name = getattr(node, 'name', None)
    if name is None:
        raise ValueError('No named top-level object found')
    return name


def get_new_imports(source_files: set[SourceFile]) -> tuple[str, ...]:
    return tuple(sorted(
        f'from .{source_file.filename[:-len(".py")]} import {top_level_object_name(source_file)}'
        for source_file in source_files
    ))


def remove_self_import(
    non_import: SourceFile,
    imports: tuple[str, ...],
) -> tuple[str, ...]:
    self_import = f'from .{non_import.filename[:-len(".py")]} import {top_level_object_name(non_import)}'
    return tuple(
        import_line
        for import_line in imports
        if import_line != self_import
    )


def chip_wood(source_file: SourceFile) -> set[SourceFile]:
    old_imports = get_imports(source_file)
    non_imports = get_non_imports(source_file)
    new_imports = get_new_imports(non_imports)
    imports = (
        *old_imports,
        *new_imports,
    )
    output = set()
    for non_import in non_imports:
        imports_to_be_added = remove_self_import(non_import, imports)
        non_import_with_imports = add_imports(non_import, imports_to_be_added)
        output.add(purge_unused_imports(non_import_with_imports))
    output.add(
        SourceFile(
            filename='__init__.py',
            lines=(*new_imports, '')
        )
    )
    return output
