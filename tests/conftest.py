from pytest import fixture

from wood_chipper import SourceFile


@fixture
def source_file_info() -> tuple[SourceFile, tuple[str, ...], set[SourceFile]]:
    imports = (
        'from dataclasses import dataclass',
        'import this',
        'import that',
        'from such import so, da, \\',
        '    fountain',
        'import os',
    )
    non_import1 = SourceFile(
        filename='hi_world.py',
        lines=(
            'class HiWorld:',
            '    def say(self):',
            '        return "hi world"',
            '',
        )
    )
    non_import2 = SourceFile(
        filename='another_class.py',
        lines=(
            '@dataclass',
            'class AnotherClass:',
            '    def execute(self):',
            '        return os.name',
            '',
        )
    )
    lines = (
        *imports,
        '',
        '',
        *non_import1.lines,
        '',
        *non_import2.lines,
    )
    return (
        SourceFile(
            filename='happy_path.py',
            lines=lines,
        ),
        imports,
        {non_import1, non_import2},
    )


@fixture
def imports() -> tuple[str, ...]:
    return (
        'import something',
        'import else',
        'import this',
        'from such import doo',
    )
