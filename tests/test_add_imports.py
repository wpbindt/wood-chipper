from wood_chipper import add_imports, SourceFile


def test_happy_path(source_file: SourceFile, imports: tuple[str, ...]) -> None:
    actual = add_imports(source_file, imports)
    expected = SourceFile(
        filename=source_file.filename,
        lines=(
            *imports,
            *source_file.lines
        )
    )
    assert actual == expected
