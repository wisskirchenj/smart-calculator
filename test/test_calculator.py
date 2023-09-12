import unittest
from io import StringIO
from unittest.mock import patch, MagicMock

from calculator.calculator import Calculator


class TestCalculator(unittest.TestCase):

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_example1(self, mock_stdout: StringIO, mock_input: MagicMock):
        mock_input.side_effect = ['-2 + 4 - 5 + 6', '', '1 -- -1', '9 +++ 10 -- 8', '+7', '', '/help',
                                  '14       ---   12', '/', '/go', '23+', '23 +', '23 12', 'a + b', '2 * 3', '/exit']
        Calculator().run()
        lines = mock_stdout.getvalue().splitlines()
        self.assertEqual(13, len(lines))
        self.assertEqual('3', lines[0])
        self.assertEqual('0', lines[1])
        self.assertEqual('27', lines[2])
        self.assertEqual('7', lines[3])
        self.assertEqual('The program simplifies a term of sums and differences', lines[4])
        self.assertEqual('2', lines[5])
        self.assertEqual('Unknown command', lines[6])
        self.assertEqual('Unknown command', lines[7])
        self.assertEqual('Invalid expression', lines[8])
        self.assertEqual('Invalid expression', lines[9])
        self.assertEqual('Invalid expression', lines[10])
        self.assertEqual('Invalid expression', lines[11])
        self.assertEqual('Invalid expression', lines[12])
