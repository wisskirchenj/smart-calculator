# IDEA EDU Course

Project implemented in the track 'Python OOP' of hyperskill.org JetBrains Academy. Purpose of doing this
project is to further practice and stay in touch with Python programming.

## Technology / External Libraries

- Python 3.11.5,
- with packages: random, unittest, unittest.mock, parameterized

## Repository Contents

The sources of main project tasks (7 stages) and pytest testing.

## Installation

Install the wheel file using pip after clone/fork:

    > pip install dist/smart_calculator-3.11.5-py3-none-any.whl

## Program description

Smart calculator is a Python written calculator, that not only adds, subtracts, and multiplies, but is also smart enough
to work with variables, remember your previous calculations and more.

Have fun!

## Project status

Project was completed on 18.09.23

## Progress

03.09.23 Project started - gitHub repo and project structure setup.

03.09.23 Stage 1 completed - just add given numbers.

04.09.23 Stage 2 completed - input loops now and handles different number inputs per line.

04.09.23 Stage 3 completed - add help. Use `StringIO.splitlines()` in pytest.

04.09.23 Stage 4 completed - calc formulas given with `+` and `-` operators. Simplify multiple operators.

11.09.23 Stage 5 completed - add error handling for invalid expressions and unknown commands.

15.09.23 Stage 6 completed - introduce variables, which are stored in a Calculator dictionary field.

18.09.23 Final Stage 7 completed - tokenize, parse an expression with 5 operators including precedence, convert it to
postfix notation and evaluate it. Then calc the result using a stack. Use unittest.mock.patch to mock input() in pytest.
