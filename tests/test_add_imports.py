from source_file import SourceFile
from wood_chipper import add_imports


def test_add_imports(
    source_file_info: tuple[SourceFile, tuple[str, ...], set[SourceFile]],
    imports: tuple[str, ...]
) -> None:
    source_file, *_ = source_file_info
    actual = add_imports(source_file, imports)
    expected = SourceFile(
        filename=source_file.filename,
        lines=(
            *imports,
            '',
            '',
            *source_file.lines
        )
    )
    assert actual == expected
