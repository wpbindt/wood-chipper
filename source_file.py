from __future__ import annotations
import ast
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class SourceFile:
    filename: str
    lines: tuple[str, ...]

    @classmethod
    def from_file(cls, path: str) -> SourceFile:
        ...

    def parse(self) -> ast.Module:
        source = '\n'.join(self.lines)
        return ast.parse(source=source, filename=self.filename)

    def write(self, path: Path) -> None:
        ...
