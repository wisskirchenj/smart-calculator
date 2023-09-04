class Calculator:

    def run(self):
        line = input()
        while line != '/exit':
            if line:
                print(sum([int(token) for token in line.split()]))
            line = input()
        print('bye')


if __name__ == '__main__':
    Calculator().run()
