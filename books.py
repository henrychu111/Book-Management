"""
COMP 1510
Henry Chu
A01212982
Book collection manager.
"""
import doctest


def get_list_of_books():
    """
    Return a list of books from data given

    :postcondition: list of books from the data
    :return:        list of books

    """
    filename = "Books UTF-16.txt"
    books = []
    locations = ["Home"]
    with open(filename, encoding='utf-16') as file_object:
        for line_number, line in enumerate(file_object):
            if line_number == 0:
                books.append(line.strip().split("\t"))
            else:
                book = line.strip().split("\t")
                book_header = books[0]
                book_dictionary = {}
                for index in range(0, len(book_header)):
                    book_dictionary[book_header[index]] = book[index]
                books.append(book_dictionary)
                if not book_dictionary['Shelf'].isdigit() and book_dictionary['Shelf'] not in locations:
                    locations.append(book_dictionary['Shelf'])
    return books, {number: location for number, location in enumerate(locations, 1)}


def main_menu():
    """
    Chooses an option in the menu


    :post condition: one of three(1-3) options is chosen
    :return:        option chosen

    """
    print("This is a library for a collection of books. \n"
          "Please choose an option in the menu below:")
    main_menu_dictionary = {1: 'Search for books', 2: 'Move books', 3: 'Quit'}
    print_dictionary(main_menu_dictionary)

    main_menu_selection = input("Enter the number:  ")

    while not validate_menu(main_menu_dictionary, main_menu_selection):
        main_menu_selection = input("Sorry, you have entered an invalid choice. Please choose a number: ")

    return int(main_menu_selection)


def print_dictionary(item_dictionary):
    """
    Prints the key-value items in the dictionary

    :param item_dictionary: a dictionary of the options
    :precondition:          must be a dictionary
    :postcondition:         prints all the options in the dictionary

    >>> print_dictionary({1: 'Search for books', 2: 'Move books', 3: 'Quit'})
    1: Search for books
    2: Move books
    3: Quit

    >>> print_dictionary({1: 'Author', 2: 'Title', 3: 'Publisher', 4: 'Shelf', 5: 'Category', \
    6: 'Subject'})
    1: Author
    2: Title
    3: Publisher
    4: Shelf
    5: Category
    6: Subject

    """
    try:
        for key, value in item_dictionary.items():
            print(str(key) + ": " + value)
    except AttributeError:
        raise AttributeError()


def validate_menu(menu_dictionary, input_option):
    """
    Validates the menu selection

    :param menu_dictionary: a dictionary of the menu options
    :param input_option:    the users choice in the menu
    :precondition:
    :postcondition:     checks to see if users input is possible
    :return:            True if user input is in list_of_options
                        False if not

    >>> validate_menu({1: 'Search for books', 2: 'Move books', 3: 'Quit'},'1')
    True
    >>> validate_menu({1: 'Search for books', 2: 'Move books', 3: 'Quit'}, 'jk')
    False
    >>> validate_menu({1: 'Search for books', 2: 'Move books', 3: 'Quit'}, '9')
    False
    """
    try:
        input_number = int(input_option)
    except ValueError:
        return False
    else:
        if input_number in menu_dictionary.keys():
            return True
        else:
            return False


def search_menu(list_of_books):
    """
    Chooses an option to search for books

    :param list_of_books:   a list of all the books in the data provided
    :precondition:          the list must have a list with the book details(Author, Title, etc.)
    :postcondition:         option to find books
    :return:                option chosen

    """
    if len(list_of_books) == 0:
        print("There is nothing in the file")
        return

    print("Please choose how you would like to search for your book:")
    search_menu_dictionary = {}
    for menu_number, menu_item in enumerate(list_of_books[0], 1):
        search_menu_dictionary[menu_number] = menu_item

    print_dictionary(search_menu_dictionary)

    users_input = input("Enter the number: ")
    validate_menu(search_menu_dictionary, users_input)

    while not validate_menu(search_menu_dictionary, users_input):
        users_input = input("Sorry, you have entered an invalid choice. Please choose a number: ")

    return search_menu_dictionary[int(users_input)]


def search_books(search_option, list_of_books):
    """
    Search for the books

    Search for books by the option chosen
    Ask user what to search with (search_keyword)

    :param search_option:   an option(positive integer) from search_menu
    :param list_of_books:           a list of all the books in the data provided
    :precondition:          search_option must be a positive integer between 1-6
    :postcondition:         a list of all matching books(results)
    :return:                enumerate list of results

    """
    search_keyword = input("Please enter what you want to search for: ")
    results = []
    number_of_results = 0

    for line_number, book in enumerate(list_of_books):
        if line_number > 0:
            if not search_keyword:
                if book[search_option] == search_keyword:
                    results.append([line_number, book])
                    number_of_results += 1
            else:
                if search_keyword.lower() in book[search_option].lower():
                    results.append([line_number, book])
                    number_of_results += 1
    return results, number_of_results


def move_books(list_of_books, book_locations):
    """
    Moves the book from one shelf to another

    :param list_of_books:   a list of all the books in the data provided
    :param book_locations:  a list of all possible book locations
    :postconditions:        moves the book to the desired shelf

    """
    book_parameter = search_menu(list_of_books)
    search_result, number_of_results = search_books(book_parameter, list_of_books)
    while number_of_results == 0:
        print("There were no results, please search again!")
        search_result, number_of_results = search_books(book_parameter, list_of_books)
    print_result(search_result, number_of_results)
    book_number_to_move = input("Which book would you like to move? \n"
                                "Please enter the book number in the results: ")
    book_results_dictionary = {result_number: book for result_number,
                               book in enumerate(search_result, 1)}

    while not validate_menu(book_results_dictionary, book_number_to_move):
        book_number_to_move = input("Sorry, you have entered an invalid choice. Please choose a number: ")

    book_chosen = search_result[int(book_number_to_move) - 1]
    location_chosen = location_menu(book_locations)
    list_of_books[book_chosen[0]]["Shelf"] = location_chosen
    print("Your book has been moved to shelf %s" % location_chosen)


def location_menu(book_locations):
    """
    Chooses a location to move the book

    :param book_locations:  a list of all possible book locations
    :precondition:          must be a list
    :postcondition:         determines where to move the book,
                            if user chooses Home determines the shelf number to move the book
    :returns:               location where the book will be moved

    """
    print("Please choose a location in the menu below:")
    print_dictionary(book_locations)

    location_selection = input("Enter the number:  ")

    while not validate_menu(book_locations, location_selection):
        location_selection = input("Sorry, you have entered an invalid choice. Please choose a number: ")

    if int(location_selection) == 1:
        shelf_number = input("Which shelf number would you like to move to? ")
        while not shelf_number.isdigit():
            shelf_number = input("Please enter a valid number: ")
        return shelf_number
    else:
        return book_locations[int(location_selection)]


def print_result(result, number_of_results):
    """
    Prints the result in correct format

    :param result:              a list of the result
    :param number_of_results:   amount in the result
    :precondition:              result is a list of dictionaries
    :postcondition:             prints out result and number of results

    >>> print_result([[308, {'Author': 'Anderson', 'Title': 'Starfarers', 'Publisher': 'Tor', \
    'Shelf': '24','Category': 'Fiction', 'Subject': 'SF' }]], 1)
    Total results: 1
    **********************************
    Result #1
    Author: Anderson
    Title: Starfarers
    Publisher: Tor
    Shelf: 24
    Category: Fiction
    Subject: SF
    ------------------------------
    """
    print("Total results: %d" % number_of_results)
    print("**********************************")
    for result_number, book in enumerate(result, 1):
        print("Result #%d" % result_number)
        print_dictionary(book[1])
        print("------------------------------")


def quit_books(list_of_books):
    """
    Quits the program while saving all changes

    :param list_of_books:   a list of all the books in the data provided
    :precondition:          option to quit is chosen
    :postcondition:         Saves changes to the files and quits

    Save changes and quits the program
    """
    filename = "Books UTF-16.txt"
    tab = "\t"
    with open(filename, "w", encoding="utf-16") as file_object:
        for line_number, line in enumerate(list_of_books):
            if line_number == 0:
                file_object.write(tab.join(line))
            else:
                file_object.write("\n")
                file_object.write(tab.join(line.values()))


def main():
    """
    Drives the program.

    """
    list_of_books, locations = get_list_of_books()

    main_menu_selection = main_menu()

    while main_menu_selection != 3:
        if main_menu_selection == 1:
            book_parameter = search_menu(list_of_books)
            result, number_of_results = (search_books(book_parameter, list_of_books))
            if number_of_results > 0:
                print_result(result, number_of_results)
            else:
                print("No results!")
        elif main_menu_selection == 2:
            move_books(list_of_books, locations)
        main_menu_selection = main_menu()

    quit_books(list_of_books)
    print("Your books have been saved. Thank you for using the program!")
    doctest.testmod()


if __name__ == "__main__":
    main()
