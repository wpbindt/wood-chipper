from dataclasses import dataclass


@dataclass
class SourceFile:
    filename: str
    contents: str


def break_up_source_file(code: SourceFile) -> set[SourceFile]:
    ...

