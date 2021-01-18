import io
from unittest import TestCase
from unittest.mock import patch

from books import main_menu


class Test(TestCase):

    @patch('builtins.input', side_effect=['1'])
    def test_main_menu_right_choice(self, mock_input):
        actual = main_menu()
        expected = 1
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['abc', '2'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_main_menu_wrong_input(self, mock_input, mock_output):
        actual = main_menu()
        expected = 2
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['a', '9', '3'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_main_menu_two_wrong_inputs(self, mock_input, mock_output):
        actual = main_menu()
        expected = 3
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['a', '6', '9', 'b', '100', '2'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_main_menu_five_wrong_inputs(self, mock_input, mock_output):
        actual = main_menu()
        expected = 2
        self.assertEqual(expected, actual)
