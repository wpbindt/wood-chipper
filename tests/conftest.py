from pytest import fixture

from wood_chipper import SourceFile


@fixture
def source_file() -> SourceFile:
    lines = (
        'import this',
        'import that',
        'from such import so, da, \\',
        '    fountain',
        '',
        '',
        'class HiWorld:',
        '    def say(self):',
        '        return "hi world"',
        '',
    )
    return SourceFile(
        filename='happy_path.py',
        lines=lines,
    )


@fixture
def imports() -> tuple[str, ...]:
    return (
        'import something',
        'import else',
        'import this',
        'from such import doo',
    )
