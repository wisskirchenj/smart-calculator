import re
from calculator.operators import Operator


def tokenize_operator(expression: str) -> tuple[str, str]:
    match = re.match(r'[-+]+|[/*^]', expression)
    operator = match.group()
    to_skip = len(operator)
    if to_skip > 1:
        operator = '-' if operator.count('-') % 2 else '+'
    return operator, expression[to_skip:]


def tokenize_variable(expression: str) -> tuple[str, str]:
    match = re.match(r'[a-zA-Z]+', expression)
    variable = match.group()
    return variable, expression[len(variable):]


def tokenize_number(expression: str) -> tuple[str, str]:
    match = re.match(r'-?\d+', expression)
    number = match.group()
    return number, expression[len(number):]


def tokenize(expression: str) -> list[str]:
    tokens = []
    while expression:
        if expression[0] in '()':
            tokens.append(expression[0])
            expression = expression[1:]
        elif expression[0].isalpha():
            variable, expression = tokenize_variable(expression)
            tokens.append(variable)
        elif expression[0].isdigit() or expression[0] == '-' and not tokens:
            number, expression = tokenize_number(expression)
            tokens.append(number)
        elif expression[0] in Operator.precedences:
            operator, expression = tokenize_operator(expression)
            tokens.append(operator)
        else:
            raise ValueError
    return tokens
