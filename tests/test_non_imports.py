from source_file import SourceFile
from wood_chipper import get_non_imports


def test_non_imports(
    source_file_info: tuple[SourceFile, tuple[str, ...], set[SourceFile]]
) -> None:
    source_file, _, non_import_sources = source_file_info
    assert get_non_imports(source_file) == non_import_sources
