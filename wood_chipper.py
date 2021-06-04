# parse file to SourceFile object (filename and source lines)
# convert SourceFile to ast object
# extract the imports from the sourcefile object (tuple of str)
# extract non-imports from SourceFile object, whose name is snake case version of class name (set of sourcefile objects)
# compile list of imports of newly created files
# combine the above 3 items in sourcefiles
# write all SourceFile object to actual files in new module named after original file
# purge unused imports
# clean code style for imports
# include imports in __init__.py

# SOMEWHERE:
# deal with comments

from __future__ import annotations
from ast import AST
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class SourceFile:
    filename: str
    lines: tuple[str, ...]
        
    @classmethod
    def from_file(cls, path: str) -> SourceFile:
        ...
        
    def parse(self) -> AST:
        ...
        
    def write(self, path: Path) -> None:
        ...


def get_imports(source_file: SourceFile) -> tuple[str, ...]:
    ...


def non_imports(source_file: SourceFile) -> set[SourceFile]:
    ...


def add_imports(source_file: SourceFile, imports: tuple[str, ...]) -> SourceFile:
    ...


def purge_unused_imports(source_file: SourceFile) -> SourceFile:
    # auto_flake
    ...
