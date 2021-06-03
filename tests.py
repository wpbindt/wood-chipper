from wood_chipper import break_up_source_file, SourceFile


def test_case(source_file, expected):
    assert break_up_source_file(source_file) == expected


source_file = SourceFile(
    'filename.py',
    'from dataclasses import dataclass\n'
    'import os\n'
    '\n'
    '\n'
    '@dataclass\n'
    'class HelloWorldSayer:\n'
    '    user: str\n'
    '\n'
    '    def say(self, something: str) -> str:\n'
    '        return f"Hi, {self.user}, {something}"\n'
    '\n'
    '\n'
    'class HelloWorld:\n'
    '    def hi(self):\n'
    '        print(f"hello, {os.name}")\n'
    '\n'
)

expected_1 = SourceFile(
    'hello_world_sayer.py',
    'from dataclasses import dataclass\n'
    '\n'
    '\n'
    '@dataclass\n'
    'class HelloWorldSayer:\n'
    '    user: str\n'
    '\n'
    '    def say(self, something: str) -> str:\n'
    '        return f"Hi, {self.user}, {something}"\n'
    '\n'
)

expected_2 = SourceFile(
    'hello_world.py',
    'import os\n'
    '\n'
    '\n'
    'class HelloWorld:\n'
    '    def hi(self):\n'
    '        print("hello, {os.name}")\n'
    '\n'
)

test_case(source_file, {expected_1, expected_2})

