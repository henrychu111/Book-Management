from unittest import TestCase
from unittest.mock import patch
from books import search_menu
import io


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['1'])
    def test_search_menu_empty_list(self, mock_input, mock_output):
        list_of_books = []
        search_menu(list_of_books)
        actual = mock_output.getvalue()
        expected = "There is nothing in the file\n"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['1'])
    def test_search_menu_one_item_list_(self, mock_input, ):
        list_of_books = [['Author', 'Title', 'Publisher']]
        actual = search_menu(list_of_books)
        expected = 'Author'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['a', '1'])
    def test_search_menu_one_item_list_one_wrong_input(self, mock_input, ):
        list_of_books = [['Author', 'Title', 'Publisher']]
        actual = search_menu(list_of_books)
        expected = 'Author'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['a', 'Author', 'title', '2'])
    def test_search_menu_one_item_list_three_wrong_input(self, mock_input, ):
        list_of_books = [['Author', 'Title', 'Publisher']]
        actual = search_menu(list_of_books)
        expected = 'Title'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['2'])
    def test_search_menu_two_item_list(self, mock_input, ):
        list_of_books = [['Author', 'Title', 'Publisher'],
                         [308, {'Author': 'Anderson', 'Title': 'Starfarers', 'Publisher': 'Tor',
                                'Shelf': '24', 'Category': 'Fiction', 'Subject': 'SF'}]]
        actual = search_menu(list_of_books)
        expected = 'Title'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['Shelf', '2'])
    def test_search_menu_two_item_list_wrong_input(self, mock_input, ):
        list_of_books = [['Author', 'Title', 'Publisher', 'Shelf', 'Category', 'Subject'],
                         [308, {'Author': 'Anderson', 'Title': 'Starfarers', 'Publisher': 'Tor',
                                'Shelf': '24', 'Category': 'Fiction', 'Subject': 'SF'}]]
        actual = search_menu(list_of_books)
        expected = 'Title'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['3'])
    def test_search_menu_ten_item_list_(self, mock_input, ):
        list_of_books = [['Author', 'Title', 'Publisher'], '1', '2', '3', ['Star', 'Wars', '4'],
                         'books', 'about', 'programming', 5, {'Author': 'Hines', 'Publisher': 'Rizzoli'}]
        actual = search_menu(list_of_books)
        expected = 'Publisher'
        self.assertEqual(expected, actual)
