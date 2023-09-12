import re


class Calculator:

    def run(self):
        line = input()
        while line != '/exit':
            if line.startswith('/'):
                self.execute_command(line[1:])
            elif line:
                self.simplify_term(line.split())
            line = input()

    @staticmethod
    def execute_command(command):
        if command == 'help':
            print('The program simplifies a term of sums and differences')
        else:
            print('Unknown command')

    def simplify_term(self, tokens):
        try:
            result = int(tokens[0])
            for i in range(1, len(tokens), 2):
                result = self.calc(result, self.resolve_operator(tokens[i]), int(tokens[i + 1]))
            print(result)
        except (IndexError, ValueError):
            print('Invalid expression')

    def calc(self, x, op, y):
        return eval(f'{x} {op} {y}')

    def resolve_operator(self, operator_token):
        if not re.match('[-+]+', operator_token):
            raise ValueError
        return '-' if operator_token.count('-') % 2 else '+'


if __name__ == '__main__':
    Calculator().run()
