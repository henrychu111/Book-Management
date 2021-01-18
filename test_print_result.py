from unittest import TestCase
from books import print_result
from unittest.mock import patch
import io


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_result_empty_list(self, mock_output):
        result = []
        number_of_results = 0
        print_result(result, number_of_results)
        actual = mock_output.getvalue()
        expected = 'Total results: 0\n' \
                   '**********************************\n'
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_result_one_value_list(self, mock_output):
        result = [[1, {'Author': 'Anderson'}]]
        number_of_results = 1
        print_result(result, number_of_results)
        actual = mock_output.getvalue()
        expected = 'Total results: 1\n' \
                   '**********************************\n' \
                   'Result #1\n' \
                   'Author: Anderson\n' \
                   '------------------------------\n'
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_result_multiple_value_list(self, mock_output):
        result = [[1, {'Author': 'Anderson'}], [2, {'Title': 'Starfarers'}], [3, {'Publisher': 'Tor'}]]
        number_of_results = 3
        print_result(result, number_of_results)
        actual = mock_output.getvalue()
        expected = 'Total results: 3\n' \
                   '**********************************\n' \
                   'Result #1\n' \
                   'Author: Anderson\n' \
                   '------------------------------\n' \
                   'Result #2\n' \
                   'Title: Starfarers\n' \
                   '------------------------------\n' \
                   'Result #3\n' \
                   'Publisher: Tor\n' \
                   '------------------------------\n'
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_result_one_value_list_larger_dictionary(self, mock_output):
        result = [[1, {'Author': 'Anderson', 'Title': 'Starfarers',
                  'Publisher': 'Tor', 'Shelf': '24', 'Category': 'Fiction', 'Subject': 'SF'}]]
        number_of_results = 1
        print_result(result, number_of_results)
        actual = mock_output.getvalue()
        expected = 'Total results: 1\n' \
                   '**********************************\n' \
                   'Result #1\n' \
                   'Author: Anderson\n' \
                   'Title: Starfarers\n' \
                   'Publisher: Tor\n' \
                   'Shelf: 24\n' \
                   'Category: Fiction\n' \
                   'Subject: SF\n' \
                   '------------------------------\n'
        self.assertEqual(expected, actual)
