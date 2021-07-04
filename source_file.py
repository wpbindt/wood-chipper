from __future__ import annotations
import ast
from dataclasses import dataclass
from pathlib import Path

from ast_utils import ast_stmt_to_name
from object import Object


@dataclass(frozen=True)
class SourceFile:
    filename: str
    lines: tuple[str, ...]

    @classmethod
    def from_file(cls, path: Path) -> SourceFile:
        lines = tuple(path.read_text().split('\n'))
        return cls(
            filename=path.name,
            lines=lines
        )

    def __str__(self) -> str:
        return '\n'.join(self.lines)

    def parse(self) -> list[ast.stmt]:
        return ast.parse(source=str(self), filename=self.filename).body

    def write(self, path: Path) -> None:
        (path / self.filename).write_text(str(self))

    @property
    def top_level_objects(self) -> list[Object]:
        return [
            Object(name=ast_stmt_to_name(statement))
            for statement in self.parse()
            if not isinstance(statement, (ast.Import, ast.ImportFrom))
        ]
