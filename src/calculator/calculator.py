import re


class Calculator:

    def __init__(self):
        self.variables: dict = {}

    def run(self):
        line = input()
        while line != '/exit':
            if line.startswith('/'):
                self.execute_command(line[1:])
            elif '=' in line:
                self.assign_variable(line)
            elif line:
                self.simplify_term(line.split())
            line = input()
        print('Bye!')

    def simplify_term(self, tokens: list[str]):
        try:
            result = self.resolve_term(tokens[0])
            for i in range(1, len(tokens), 2):
                result = self.calc(result, self.resolve_operator(tokens[i]), self.resolve_term(tokens[i + 1]))
            print(result)
        except (IndexError, ValueError):
            print('Invalid expression')
        except KeyError:
            print('Unknown variable')

    def assign_variable(self, line: str):
        try:
            variable, value = line.split('=')
            variable = variable.strip()
            if not variable.isalpha():
                raise ValueError
            self.variables[variable] = self.resolve_term(value.strip())
        except ValueError:
            print('Invalid assignment')
        except KeyError:
            print('Unknown variable')

    def resolve_term(self, value: str):
        if value.isalpha():
            value = self.variables[value]
        return int(value)

    @staticmethod
    def execute_command(command: str):
        if command == 'help':
            print('The program simplifies a term of sums and differences')
        else:
            print('Unknown command')

    @staticmethod
    def calc(x, op, y):
        return eval(f'{x} {op} {y}')

    @staticmethod
    def resolve_operator(operator_token: str) -> str:
        if not re.match('[-+]+', operator_token):
            raise ValueError
        return '-' if operator_token.count('-') % 2 else '+'


if __name__ == '__main__':
    Calculator().run()
