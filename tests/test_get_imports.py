from wood_chipper import get_imports, SourceFile


def test_happy_path(source_file: SourceFile) -> None:
    imports = source_file.lines[:4]
    assert get_imports(source_file) == imports
