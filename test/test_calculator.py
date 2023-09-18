import unittest
from io import StringIO
from unittest.mock import patch, MagicMock

from calculator.calculator_main import Calculator


class TestCalculator(unittest.TestCase):

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_example1(self, mock_stdout: StringIO, mock_input: MagicMock):
        mock_input.side_effect = ['-2 + 4 - 5 + 6', '', '1 -- -1', '9 +++ 10 -- 8', '7', '', '/help',
                                  '14       ---   12', '/', '/go', '23+', '23 +', 'a + b', '2 * 3',
                                  'a2 = 2', 'b = 2', 'aaa=b', 'c =aaa -- b', 'c', 'b=1', 'b', 'b = AAA', '/exit']
        Calculator().run()
        lines = mock_stdout.getvalue().splitlines()
        # self.assertEqual(18, len(lines))
        self.assertEqual('3', lines[0])
        self.assertEqual('0', lines[1])
        self.assertEqual('27', lines[2])
        self.assertEqual('7', lines[3])
        self.assertEqual('The program simplifies an arithmetic expression, that may contain variables', lines[4])
        self.assertEqual('2', lines[5])
        self.assertEqual('Unknown command', lines[6])
        self.assertEqual('Unknown command', lines[7])
        self.assertEqual('Invalid expression', lines[8])
        self.assertEqual('Invalid expression', lines[9])
        self.assertEqual('Unknown variable', lines[10])
        self.assertEqual('6', lines[11])
        self.assertEqual('Invalid assignment', lines[12])
        self.assertEqual('4', lines[13])
        self.assertEqual('1', lines[14])
        self.assertEqual('Unknown variable', lines[15])
        self.assertEqual('Bye!', lines[16])
