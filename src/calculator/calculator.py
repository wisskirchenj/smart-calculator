class Calculator:

    def run(self):
        line = input()
        while line != '/exit':
            if line == '/help':
                print('The program simplifies a term of sums and differences')
            elif line:
                print(self.simplify_term(line.split()))
            line = input()
        print('bye')

    def simplify_term(self, tokens):
        result = tokens[0]
        for i in range(1, len(tokens), 2):
            result = self.calc(result, self.resolve_operator(tokens[i]), tokens[i + 1])
        return result

    def calc(self, x, op, y):
        return eval(f'{x} {op} {y}')

    def resolve_operator(self, operator_token):
        return '-' if operator_token.count('-') % 2 else '+'


if __name__ == '__main__':
    Calculator().run()
