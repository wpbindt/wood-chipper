import pytest

from object import Object
from source_file import SourceFile


get_top_level_objects_cases = [
    (
        SourceFile(
            filename='unimportant',
            lines=(
                'class C:',
                ' def __init__(self, a):',
                '  self.a = a',
                '',
                '',
                'class D:',
                ' ...',
                '',
            )
        ),
        [
            Object(name='C'),
            Object(name='D'),
        ]
    ),
    (
        SourceFile(
            filename='unimportant',
            lines=(
                'import dataclasses',
                'import something',
                'from donkey import everything',
            )
        ),
        []
    ),
    (
        SourceFile(
            filename='unimportant',
            lines=(
                'def f(a, b):',
                ' return a',
                '',
                '',
                'def g(x):',
                ' ...',
                '',
            )
        ),
        [
            Object(name='f'),
            Object(name='g'),
        ]
    ),
    (
        SourceFile(
            filename='unimportant',
            lines=(
                'CONSTANT = 3.14',
                'OTHER_CONSTANT = "all good man"',
                '',
            )
        ),
        [
            Object(name='CONSTANT'),
            Object(name='OTHER_CONSTANT'),
        ]
    ),
]


@pytest.mark.parametrize('case', get_top_level_objects_cases)
def test_top_level_objects_gets_top_level_classes(
        case: tuple[SourceFile, list[Object]]
) -> None:
    source_file, top_level_objects = case
    assert source_file.top_level_objects == top_level_objects
