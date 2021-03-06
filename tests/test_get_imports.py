from source_file import SourceFile
from wood_chipper import get_imports


def test_get_imports(
    source_file_info: tuple[SourceFile, tuple[str, ...], set[SourceFile]]
) -> None:
    source_file, imports, _ = source_file_info
    assert get_imports(source_file) == imports
