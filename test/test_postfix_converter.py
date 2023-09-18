import unittest

from calculator.calculator_main import Calculator


class TestPostfixConverter(unittest.TestCase):

    #  Test with a simple expression containing only integers and operators
    def test_simple_expression_integers_operators(self):
        calculator = Calculator()
        result = calculator.convert_to_postfix("2+3*4")
        self.assertEqual(result, "2 3 4 * +")

    #  Test with a simple expression containing variables and operators
    def test_simple_expression_variables_operators(self):
        calculator = Calculator()
        calculator.variables = {'x': 2, 'y': 3, 'z': 4}
        result = calculator.convert_to_postfix("x+y*z")
        self.assertEqual(result, "2 3 4 * +")

    #  Test with a complex expression containing variables and operators
    def test_complex_expression_variables_operators(self):
        calculator = Calculator()
        calculator.variables = {'x': 2, 'y': 3, 'z': 4}
        result = calculator.convert_to_postfix("(x+y)*z-x/y")
        self.assertEqual(result, "2 3 + 4 * 2 3 / -")

    #  Test with an empty string as input
    def test_empty_string_input(self):
        calculator = Calculator()
        result = calculator.convert_to_postfix("")
        self.assertEqual(result, "")

    #  Test with an input containing only one token
    def test_single_token_input(self):
        calculator = Calculator()
        result = calculator.convert_to_postfix("-5-5")
        self.assertEqual(result, "-5 5 -")

    #  Test with an input containing only one operator
    def test_single_operator_input(self):
        calculator = Calculator()
        result = calculator.convert_to_postfix("+")
        self.assertEqual(result, "+")

    #  Test with an input containing only one operator
    def test_invalid_input(self):
        calculator = Calculator()
        result = calculator.convert_to_postfix("(3+4")
        self.assertEqual(result, "3 4 + (")
