from unittest import TestCase
from unittest.mock import patch
from books import location_menu


class Test(TestCase):

    @patch('builtins.input', side_effect=['2'])
    def test_location_menu_correct_input(self, mock_input):
        book_locations = {1: 'Home', 2: 'Noguchi', 3: 'Reading', 4: 'Island', 5: 'Gaby'}
        actual = location_menu(book_locations)
        expected = 'Noguchi'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['', '2'])
    def test_location_menu_empty_input(self, mock_input):
        book_locations = {1: 'Home', 2: 'Noguchi', 3: 'Reading', 4: 'Island', 5: 'Gaby'}
        actual = location_menu(book_locations)
        expected = 'Noguchi'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['a', '3'])
    def test_location_menu_wrong_input(self, mock_input):
        book_locations = {1: 'Home', 2: 'Noguchi', 3: 'Reading', 4: 'Island', 5: 'Gaby'}
        actual = location_menu(book_locations)
        expected = 'Reading'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['a', 'b', '8', '1982', '3'])
    def test_location_menu_multiple_wrong_input(self, mock_input):
        book_locations = {1: 'Home', 2: 'Noguchi', 3: 'Reading', 4: 'Island', 5: 'Gaby'}
        actual = location_menu(book_locations)
        expected = 'Reading'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['1', '2'])
    def test_location_menu_home_shelf(self, mock_input):
        book_locations = {1: 'Home', 2: 'Noguchi', 3: 'Reading', 4: 'Island', 5: 'Gaby'}
        actual = location_menu(book_locations)
        expected = '2'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['1', 'a', '30'])
    def test_location_menu_home_shelf_wrong_input(self, mock_input):
        book_locations = {1: 'Home', 2: 'Noguchi', 3: 'Reading', 4: 'Island', 5: 'Gaby'}
        actual = location_menu(book_locations)
        expected = '30'
        self.assertEqual(expected, actual)
