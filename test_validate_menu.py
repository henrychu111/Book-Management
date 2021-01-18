from unittest import TestCase
from books import validate_menu


class Test(TestCase):

    def test_validate_menu_empty_dictionary(self):
        menu_dictionary = {}
        input_option = 1
        expected = False
        actual = validate_menu(menu_dictionary, input_option)
        self.assertEqual(expected, actual)

    def test_validate_menu_one_item_dictionary(self):
        menu_dictionary = {1: ' Search for books'}
        input_option = 1
        expected = True
        actual = validate_menu(menu_dictionary, input_option)
        self.assertEqual(expected, actual)

    def test_validate_menu_one_item_dictionary_empty_input(self):
        menu_dictionary = {1: ' Search for books'}
        input_option = ''
        expected = False
        actual = validate_menu(menu_dictionary, input_option)
        self.assertEqual(expected, actual)

    def test_validate_menu_one_item_dictionary_wrong_number_input(self):
        menu_dictionary = {1: ' Search for books'}
        input_option = 2
        expected = False
        actual = validate_menu(menu_dictionary, input_option)
        self.assertEqual(expected, actual)

    def test_validate_menu_one_item_dictionary_wrong_value_input(self):
        menu_dictionary = {1: ' Search for books'}
        input_option = 'b'
        expected = False
        actual = validate_menu(menu_dictionary, input_option)
        self.assertEqual(expected, actual)

    def test_validate_menu_two_item_dictionary_(self):
        menu_dictionary = {1: ' Search for books', 2: 'Say Hi'}
        input_option = 2
        expected = True
        actual = validate_menu(menu_dictionary, input_option)
        self.assertEqual(expected, actual)

    def test_validate_menu_six_item_dictionary(self):
        menu_dictionary = {1: ' Search for books', 2: 'Say Hi', 3: 'Author', 4: 'Title',
                           5: 'Category', 6: 'Unittest'}
        input_option = 5
        expected = True
        actual = validate_menu(menu_dictionary, input_option)
        self.assertEqual(expected, actual)

    def test_validate_menu_six_item_dictionary_wrong_number_input(self):
        menu_dictionary = {1: ' Search for books', 2: 'Say Hi', 3: 'Author', 4: 'Title',
                           5: 'Category', 6: 'Unittest'}
        input_option = 8
        expected = False
        actual = validate_menu(menu_dictionary, input_option)
        self.assertEqual(expected, actual)

    def test_validate_menu_six_item_dictionary_wrong_value_input(self):
        menu_dictionary = {1: ' Search for books', 2: 'Say Hi', 3: 'Author', 4: 'Title',
                           5: 'Category', 6: 'Unittest'}
        input_option = 'books'
        expected = False
        actual = validate_menu(menu_dictionary, input_option)
        self.assertEqual(expected, actual)
