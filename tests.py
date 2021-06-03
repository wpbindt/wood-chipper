from wood_chipper import break_up_source_file, SourceFile


def test_case(source_file, expected):
    actual = break_up_source_file(source_file)
    assert break_up_source_file(source_file) == expected


source_file = SourceFile(
    'filename.py',
    (
        'from dataclasses import dataclass',
        'import os',
        '',
        '',
        '@dataclass',
        'class HelloWorldSayer:',
        '    user: str',
        '',
        '    def say(self, something: str) -> str:',
        '        return f"Hi, {self.user}, {something}"',
        '',
        '',
        'class HelloWorld:',
        '    def hi(self):',
        '        print(f"hello, {os.name}")',
        '',
    )
)

expected_1 = SourceFile(
    'hello_world_sayer.py',
    (
        'from dataclasses import dataclass',
        'import os',
        '',
        '',
        '@dataclass',
        'class HelloWorldSayer:',
        '    user: str',
        '',
        '    def say(self, something: str) -> str:',
        '        return f"Hi, {self.user}, {something}"',
        '',
    )
)

expected_2 = SourceFile(
    'hello_world.py',
    (
        'from dataclasses import dataclass',
        'import os',
        '',
        '',
        'class HelloWorld:',
        '    def hi(self):',
        '        print(f"hello, {os.name}")',
        '',
    )
)

test_case(source_file, {expected_1, expected_2})

