import unittest
from io import StringIO
from unittest.mock import patch, MagicMock

from calculator.calculator import Calculator


class TestCalculator(unittest.TestCase):

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_example1(self, mock_stdout: StringIO, mock_input: MagicMock):
        mock_input.side_effect = ['5 8 2 -13', '', '1 -1', '-5 12345', '7', '', '/help', '/exit']
        Calculator().run()
        lines = mock_stdout.getvalue().splitlines()
        self.assertEqual(6, len(lines))
        self.assertEqual('2', lines[0])
        self.assertEqual('0', lines[1])
        self.assertEqual('12340', lines[2])
        self.assertEqual('7', lines[3])
        self.assertEqual('The program calculates the sum of numbers', lines[4])
        self.assertEqual('bye', lines[5])
