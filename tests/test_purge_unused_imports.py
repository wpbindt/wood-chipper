from source_file import SourceFile
from wood_chipper import purge_unused_imports


def test_purge_unused_imports(
    source_file_info: tuple[SourceFile, tuple[str, ...], set[SourceFile]]
) -> None:
    source_file, imports, _ = source_file_info
    actual = purge_unused_imports(source_file)

    unused_imports = (
        'import this',
        'import that',
        'from such import so, da, \\',
        '    fountain',
    )
    expected = SourceFile(
        filename=source_file.filename,
        lines=tuple(
            line
            for line in source_file.lines
            if line not in unused_imports
        )
    )

    assert actual == expected
