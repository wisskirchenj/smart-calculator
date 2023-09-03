class Calculator:

    def run(self):
        a, b = [int(token) for token in input().split()]
        print(a + b)


if __name__ == '__main__':
    Calculator().run()
