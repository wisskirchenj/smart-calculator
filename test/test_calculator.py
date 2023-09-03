import unittest
from io import StringIO
from unittest.mock import patch, MagicMock

from calculator.calculator import Calculator

class TestCalculator(unittest.TestCase):

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_example1(self, mock_stdout: StringIO, mock_input: MagicMock):
        mock_input.side_effect = ['5 8', '1 -1', '-5 12345']
        Calculator().run()
        self.assertEqual(1, mock_stdout.getvalue().count('13'))
        Calculator().run()
        self.assertEqual(1, mock_stdout.getvalue().count('0'))
        Calculator().run()
        self.assertEqual(1, mock_stdout.getvalue().count('12340'))
