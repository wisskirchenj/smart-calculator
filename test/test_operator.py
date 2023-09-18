import unittest

from calculator.operators import Operator, to_operator


class TestOperator(unittest.TestCase):

    #  Create an Operator object with a valid symbol and get its string representation
    def test_valid_symbol_string_representation(self):
        operator = Operator('+')
        self.assertEqual(str(operator), '+')

    #  Create an Operator object with a valid symbol and get its precedence
    def test_valid_symbol_precedence(self):
        operator = Operator('*')
        self.assertEqual(operator.precedence, 2)

    #  Call to_operator with a valid symbol and get an Operator object
    def test_valid_symbol_to_operator(self):
        operator = to_operator('-')
        self.assertIsInstance(operator, Operator)

    #  Create an Operator object with an invalid symbol and get a KeyError
    def test_invalid_symbol_key_error(self):
        self.assertRaises(KeyError, Operator, 'x')

    #  Call to_operator with an empty string and get None
    def test_empty_string_to_operator(self):
        operator = to_operator('')
        self.assertIsNone(operator)

    #  Call to_operator with a symbol that is not a string and get a TypeError
    def test_invalid_symbol_to_operator(self):
        operator = to_operator('123')
        self.assertIsNone(operator)

    #  Test apply method with two positive integers
    def test_apply_two_positive_integers(self):
        op = Operator('+')
        result = op.apply(2, 3)
        self.assertEqual(result, 5)

    #  Test apply method with two negative integers
    def test_apply_two_negative_integers(self):
        op = Operator('-')
        result = op.apply(-5, -3)
        self.assertEqual(result, -2)

    #  Test apply method with one positive and one negative integer
    def test_apply_one_positive_one_negative(self):
        op = Operator('*')
        result = op.apply(4, -2)
        self.assertEqual(result, -8)

    #  Test apply method with large positive integers
    def test_apply_large_positive_integers(self):
        op = Operator('^')
        result = op.apply(10**6, 3)
        self.assertEqual(result, 1000000000000000000)

    #  Test apply method with large negative integers
    def test_apply_large_negative_integers(self):
        op = Operator('/')
        result = op.apply(-10**6, 2)
        self.assertEqual(result, -500000.0)

    #  Test apply method with division by zero
    def test_apply_division_by_zero(self):
        op = Operator('/')
        with self.assertRaises(ZeroDivisionError):
            op.apply(5, 0)
