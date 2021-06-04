from wood_chipper import get_imports, SourceFile


def test_happy_path(
    source_file_info: tuple[SourceFile, tuple[str, ...], set[SourceFile]]
) -> None:
    source_file, imports, _ = source_file_info
    assert get_imports(source_file) == imports
