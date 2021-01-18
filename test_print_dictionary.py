import io
from unittest import TestCase
from unittest.mock import patch

from books import print_dictionary


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_dictionary_empty(self, mock_output):
        dictionary = {}
        print_dictionary(dictionary)
        actual = mock_output.getvalue()
        expected = ''
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_dictionary_three_items(self, mock_output):
        dictionary = {1: 'Item 1', 2: 'Item 2', 3: 'Item 3'}
        print_dictionary(dictionary)
        actual = mock_output.getvalue()
        expected = '1: Item 1\n' \
                   '2: Item 2\n' \
                   '3: Item 3\n'
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_dictionary_test_string(self, mock_output):
        dictionary = 'test string'
        with self.assertRaises(Exception) as context:
            print_dictionary(dictionary)
        self.assertRaises(Exception, context.exception)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_dictionary_test_list(self, mock_output):
        dictionary = ['1', '2', '3']
        with self.assertRaises(Exception) as context:
            print_dictionary(dictionary)
        self.assertRaises(Exception, context.exception)

