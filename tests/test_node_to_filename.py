import ast

import pytest

from node_to_source_file import node_to_filename


happy_cases = [
    (ast.ClassDef(name='MyClass'), 'my_class.py'),
    (ast.FunctionDef(name='my_function'), 'my_function.py'),
    (ast.ClassDef(name='APIFactory'), 'api_factory.py'),
    (ast.ClassDef(name='Magento2Repository'), 'magento2_repository.py'),
]


@pytest.mark.parametrize('case', happy_cases)
def test_node_to_filename(case: tuple[ast.AST, str]) -> None:
    node, filename = case
    assert node_to_filename(node) == filename


no_name_nodes = [
    ast.Import(
        names=[
            ast.alias(name='x')
        ]
    ),
    ast.ImportFrom(
        module='y',
        names=[
            ast.alias(name='x')
        ]
    ),
    ast.Continue(),
]


@pytest.mark.parametrize('node', no_name_nodes)
def test_node_to_filename_raises_when_no_name(node: ast.AST) -> None:
    with pytest.raises(ValueError):
        node_to_filename(node)
