from calculator.operators import to_operator, Operator
from calculator.tokenizer import tokenize


class Calculator:

    def __init__(self):
        self.variables: dict = {}

    def run(self):
        line = input().replace(' ', '')
        while line != '/exit':
            if line.startswith('/'):
                self.execute_command(line[1:])
            elif '=' in line:
                self.evaluate(line, self.assign_variable, 'assignment')
            elif line:
                self.evaluate(line, self.simplify_term, 'expression')
            line = input().replace(' ', '')
        print('Bye!')

    def simplify_term(self, line: str, print_it: bool = True) -> int:
        postfix = self.convert_to_postfix(line)
        result = self.calc(postfix)
        if print_it:
            print(result)
        return int(result)

    def assign_variable(self, line):
        variable, value = line.split('=')
        if not variable.isalpha():
            raise ValueError
        self.variables[variable] = self.simplify_term(value, print_it=False)

    def convert_to_postfix(self, line: str) -> str:
        postfix = ''
        operator_stack = []
        for token in tokenize(line):
            postfix += self.process_token(token, operator_stack)
        while operator_stack:
            postfix += f'{operator_stack.pop()} '
        return postfix.strip()

    def process_token(self, token: str, operator_stack: list) -> str:
        if token == '(':
            operator_stack.append(token)
            return ''
        if token.isalpha():
            return f'{self.variables[token]} '
        if to_operator(token):
            return self.process_operator(Operator(token), operator_stack)
        if token == ')':
            return self.process_closing_parenthesis(operator_stack)
        return f'{int(token)} '

    @staticmethod
    def evaluate(line: str, operation: callable, operation_text: str):
        try:
            operation(line)
        except (IndexError, ValueError):
            print('Invalid', operation_text)
        except KeyError:
            print('Unknown variable')

    @staticmethod
    def execute_command(command: str):
        if command == 'help':
            print('The program simplifies an arithmetic expression, that may contain variables')
        else:
            print('Unknown command')

    @staticmethod
    def process_operator(operator: Operator, operator_stack: list) -> str:
        contribution = ''
        while operator_stack and operator_stack[-1] != '(' and operator.precedence <= operator_stack[-1].precedence:
            contribution += f'{operator_stack.pop()} '
        operator_stack.append(operator)
        return contribution

    @staticmethod
    def process_closing_parenthesis(operator_stack: list) -> str:
        contribution = ''
        while operator_stack[-1] != '(':
            contribution += f'{operator_stack.pop()} '
        operator_stack.pop()
        return contribution

    def calc(self, postfix: str) -> int:
        operand_stack = []
        for token in postfix.split():
            if to_operator(token):
                operand_stack.append(self.calc_operation(token, operand_stack))
            else:
                operand_stack.append(int(token))
        return operand_stack.pop()

    @staticmethod
    def calc_operation(token: str, operand_stack: list[int]) -> int:
        y = operand_stack.pop()
        x = operand_stack.pop()
        return Operator(token).apply(x, y)


if __name__ == '__main__':
    Calculator().run()
