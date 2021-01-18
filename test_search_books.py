from unittest import TestCase
from unittest.mock import patch
from books import search_books


class Test(TestCase):

    @patch('builtins.input', side_effect=['1'])
    def test_search_books_empty_list(self, mock_input):
        list_of_books = []
        search_option = 'Shelf'
        actual_one, actual_two = search_books(search_option, list_of_books)
        expected_one, expected_two = [], 0
        self.assertEqual(expected_one, actual_one)
        self.assertEqual(expected_two, actual_two)

    @patch('builtins.input', side_effect=['Author'])
    def test_search_books_one_item_list_no_result(self, mock_input):
        list_of_books = [['Author', 'Title', 'Publisher']]
        search_option = 'Author'
        actual_one, actual_two = search_books(search_option, list_of_books)
        expected_one, expected_two = [], 0
        self.assertEqual(expected_one, actual_one)
        self.assertEqual(expected_two, actual_two)

    @patch('builtins.input', side_effect=['1'])
    def test_search_books_two_item_list_no_result_for_input(self, mock_input):
        list_of_books = [['Author', 'Title', 'Publisher'],
                         {'Author': 'Anderson', 'Title': 'Starfarers','Publisher': 'Tor',
                          'Shelf': '24', 'Category': 'Fiction', 'Subject': 'SF'}]
        search_option = 'Shelf'
        actual_one, actual_two = search_books(search_option, list_of_books)
        expected_one, expected_two = [], 0
        self.assertEqual(expected_one, actual_one)
        self.assertEqual(expected_two, actual_two)

    @patch('builtins.input', side_effect=['Tor'])
    def test_search_books_two_item_list_correct_input(self, mock_input):
        list_of_books = [['Author', 'Title', 'Publisher'],
                         {'Author': 'Anderson', 'Title': 'Starfarers', 'Publisher': 'Tor',
                          'Shelf': '24', 'Category': 'Fiction', 'Subject': 'SF'}]
        search_option = 'Publisher'
        actual_one, actual_two = search_books(search_option, list_of_books)
        expected_one, expected_two = [[1, {'Author': 'Anderson', 'Title': 'Starfarers', 'Publisher': 'Tor',
                                      'Shelf': '24', 'Category': 'Fiction', 'Subject': 'SF'}]], 1
        self.assertEqual(expected_one, actual_one)
        self.assertEqual(expected_two, actual_two)

    @patch('builtins.input', side_effect=['travel'])
    def test_search_books_three_item_list(self, mock_input):
        list_of_books = [['Author', 'Title', 'Publisher'], {'Author': 'Anderson', 'Title': 'Starfarers',
                        'Publisher': 'Tor', 'Shelf': '24', 'Category': 'Fiction', 'Subject': 'SF'},
                         {'Author': 'Sinclair', 'Title': 'Morrisseau', 'Publisher': 'Editions Franco-Amerique',
                          'Shelf': 'Reading', 'Category': 'Art', 'Subject': 'Canadian'},
                         {'Author': 'Eyewitness Travel', 'Title': 'Vietnam', 'Publisher': 'DK',
                          'Shelf': '1', 'Category': 'Travel', 'Subject': ''}]
        search_option = 'Category'
        actual_one, actual_two = search_books(search_option, list_of_books)
        expected_one, expected_two = [[3, {'Author': 'Eyewitness Travel', 'Title': 'Vietnam', 'Publisher':
                                      'DK', 'Shelf': '1', 'Category': 'Travel', 'Subject': ''}]], 1
        self.assertEqual(expected_one, actual_one)
        self.assertEqual(expected_two, actual_two)

    @patch('builtins.input', side_effect=['s'])
    def test_search_books_three_item_list_two_results(self, mock_input):
        list_of_books = [['Author', 'Title', 'Publisher'], {'Author': 'Anderson', 'Title': 'Starfarers',
                        'Publisher': 'Tor', 'Shelf': '24', 'Category': 'Fiction', 'Subject': 'SF'},
                         {'Author': 'Sinclair', 'Title': 'Morrisseau', 'Publisher': 'Editions Franco-Amerique',
                          'Shelf': 'Reading', 'Category': 'Art', 'Subject': 'Canadian'},
                         {'Author': 'Eyewitness Travel', 'Title': 'Vietnam', 'Publisher': 'DK',
                          'Shelf': '1', 'Category': 'Travel', 'Subject': ''}]
        search_option = 'Title'
        actual_one, actual_two = search_books(search_option, list_of_books)
        expected_one, expected_two = [[1, {'Author': 'Anderson', 'Title': 'Starfarers', 'Publisher':
                                      'Tor', 'Shelf': '24', 'Category': 'Fiction', 'Subject': 'SF'}],
                                    [2, {'Author': 'Sinclair', 'Title': 'Morrisseau', 'Publisher': 'Editions '
                                   'Franco-Amerique', 'Shelf': 'Reading', 'Category': 'Art', 'Subject': 'Canadian'}]], 2
        self.assertEqual(expected_one, actual_one)
        self.assertEqual(expected_two, actual_two)

    @patch('builtins.input', side_effect=[''])
    def test_search_books_three_item_list_input_empty(self, mock_input):
        list_of_books = [['Author', 'Title', 'Publisher'], {'Author': 'Anderson', 'Title': 'Starfarers',
                         'Publisher': 'Tor', 'Shelf': '24', 'Category': 'Fiction', 'Subject': 'SF'},
                         {'Author': 'Sinclair', 'Title': 'Morrisseau', 'Publisher': 'Editions Franco-Amerique',
                          'Shelf': 'Reading', 'Category': 'Art', 'Subject': 'Canadian'},
                         {'Author': 'Eyewitness Travel', 'Title': 'Vietnam', 'Publisher': 'DK',
                          'Shelf': '1', 'Category': 'Travel', 'Subject': ''}]
        search_option = 'Subject'
        actual_one, actual_two = search_books(search_option, list_of_books)
        expected_one, expected_two = [[3, {'Author': 'Eyewitness Travel', 'Title': 'Vietnam', 'Publisher':
                                      'DK', 'Shelf': '1', 'Category': 'Travel', 'Subject': ''}]], 1
        self.assertEqual(expected_one, actual_one)
        self.assertEqual(expected_two, actual_two)

