from pathlib import Path

import pytest

from source_file import SourceFile
from wood_chipper import chip_wood

CASE_DIR = Path(__file__).resolve().parent / 'integration_tests'


def _parse_case(path: Path) -> tuple[SourceFile, set[SourceFile]]:
    original_file, result_dir = path.iterdir()
    if original_file.is_dir():
        original_file, result_dir = result_dir, original_file

    expected_output = {
        SourceFile.from_file(file)
        for file in result_dir.iterdir()
    }

    return SourceFile.from_file(original_file), expected_output


cases = [
    _parse_case(case)
    for case in CASE_DIR.iterdir()
]


@pytest.mark.parametrize('case', cases)
def test_chip_wood(case: tuple[SourceFile, set[SourceFile]]) -> None:
    source_file, expected_output = case
    assert chip_wood(source_file) == expected_output
