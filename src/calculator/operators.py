class Operator:

    precedences: dict = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    functions: dict = {'+': lambda x, y: x + y,
                       '-': lambda x, y: x - y,
                       '*': lambda x, y: x * y,
                       '/': lambda x, y: x // y,
                       '^': lambda x, y: x ** y}

    def __init__(self, symbol: str):
        self.symbol = symbol
        self.precedence = Operator.precedences[symbol]

    def __str__(self):
        return self.symbol

    def apply(self, x, y):
        return Operator.functions[self.symbol](x, y)


def to_operator(symbol: str) -> Operator or None:
    if symbol not in Operator.precedences:
        return None
    return Operator(symbol)
