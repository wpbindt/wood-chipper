import ast


def ast_stmt_to_name(statement: ast.stmt) -> str:
    if isinstance(statement, (ast.FunctionDef, ast.ClassDef)):
        return statement.name
    elif isinstance(statement, ast.Assign):
        if len(statement.targets) == 1:
            target = statement.targets[0]
            if isinstance(target, ast.Name):
                return target.id
    raise ValueError('Could not discern single name in statement')
