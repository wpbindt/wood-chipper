from wood_chipper import non_imports, SourceFile


def test_happy_path(
    source_file_info: tuple[SourceFile, tuple[str, ...], set[SourceFile]]
) -> None:
    source_file, _, non_import_sources = source_file_info
    assert non_imports(source_file) == non_import_sources
