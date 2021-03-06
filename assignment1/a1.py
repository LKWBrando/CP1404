"""
CP1404 Assignment One
Done by: Lum Kwan Wei Brandon
Student number: 13379339
Program details:
    Program loads values from the given file, books.csv into a temporary list
    Displays a menu, listing available options that the user can input
    Depending on the user input the program will;
        Display the list of books that are required to be read
        Display the list of books that have been completed
        Display the list of books that are required to be read, then allows the user to change a book status to completed
        Allow the user to input a book, along with it's details
        Exit the program, saving and overwriting the original file, books.csv, with the updated values based on the temporary list.
Github link:
https://github.com/LKWBrando/CP1404/tree/master/assignment1 (Private repository)
"""

from operator import itemgetter

def loading_books():
    """
    A function that reads the file, extracts the data and formats it, then appends it into a local variable
    pseudocode:
    open file 'books.csv'
    read values from file 'books.csv'
    for line and corresponding value in file 'books.csv'
        get value for line_index by removing blank spaces from values in file 'books.csv'
        get value for line_data by splitting line_index based on commas
        add line_data into book_list
    close file 'books.csv'
    sort book_list values based on author, then pages
    print number of books loaded from 'books.csv' based on length of book_list(number of values)
    :return:
    """
    bookFile = open("books.csv", "r")
    for line, data in enumerate(bookFile.readlines()):
        line_index = data.strip()
        line_data = line_index.split(",")
        book_list.append(line_data)
    bookFile.close()
    book_list.sort(key=itemgetter(1, 2))
    print("{} books loaded from books.csv".format(len(book_list)))

def menu_input():
    """
    A function that prompts user for the input based on the menu options, complete with an error checking loop.
    :return menu_option: A string value based on user's input that is used in the program to determine the path to take.
    """
    menu_option = str(input("Menu:\n R - List required books\n C - List completed books\n A - Add new book\n M - Mark a book as completed\n Q - Quit\n")).lower()
    while menu_option not in menu_option_list:
        print("Invalid menu choice")
        menu_option = str(input("Menu:\n R - List required books\n C - List completed books\n A - Add new book\n M - Mark a book as completed\n Q - Quit\n")).lower()
    return menu_option

def required_books():
    """
    A function that runs through the list, book_list, to determine if the book is marked as required.
    :param required_page_count: A variable that is used to calculate the total amount of pages based on the required books.
    :param required_book_count: A variable that is used to calculate the total count of required books.
    :return req_counter: An integer value used to determine if there are any required books left
    """
    print("Required books:")
    required_page_count = 0
    required_book_count = 0
    req_counter = 1
    for index, book in enumerate(book_list):
        if book[3] == 'r':
            required_page_count += int(book[2])
            required_book_count += 1
            print("{:<1}. {:<40s} by {:<20s} {:<4}pages".format(index, book[0], book[1], book[2]))
    if required_book_count == 0:
        print("No required books")
        req_counter = 0
        return req_counter
    else:
        print("Total pages for {} book(s):{}".format(required_book_count, required_page_count))
        return req_counter

def completed_books():
    """
    A function that runs through the list, book_list, to determine if the book is marked as completed.
    :param required_page_count: A variable that is used to calculate the total amount of pages based on the completed books.
    :param required_book_count: A variable that is used to calculate the total count of completed books.
    :return:
    """
    print("Completed books:")
    completed_page_count = 0
    completed_book_count = 0
    for index, book in enumerate(book_list):
        if book[3] == 'c':
            completed_page_count += int(book[2])
            completed_book_count += 1
            print("{:<1}.{:<40s}by {:<20s} {:<4}pages".format(index, book[0], book[1], book[2]))
    print("Total pages for {} book(s):{}".format(completed_book_count, completed_page_count))

def marking_books():
    """
    A function that takes the integer input of the user based on the selection from the reading list and runs it through an error checking loop.
    It then replaces values on the list, book_list, based on the variable mark_book, and prints a statement

    pseudocode:
    get value for mark_book
    while mark_book is more than the number of values in book_list then:
        print("Error, number not in list")
        get value for mark_book
    if required book_count = 0
        return null
    else if value for position [3] of the value based on position of [mark_book] of the book_list is equals to 'r'
        print book is marked as completed, with corresponding book_list values
        remove value for position [3] of the value based on position of [mark_book] of the book_list
        insert value of 'c' into position [3] of the data based on position of [mark_book] of the book_list
    else print (" That book is already completed")
    :return:
    """
    while True:
        try:
            mark_book = int(input("Enter the number of a book to mark as completed."))
            while mark_book > (len(book_list) - 1):
                print("Error, number not in list.")
                mark_book = int(input("Enter the number of a book to mark as completed."))
            break
        except ValueError:
            print("Invalid input; enter a valid number.")

    if book_list[mark_book][3] == 'r':
        print("{} by {} marked as completed".format(book_list[mark_book][0], book_list[mark_book][1]))
        book_list[mark_book].pop(3)
        book_list[mark_book].insert(3, 'c')
    else:
        print("That book is already completed")

def adding_books():
    """
    A function that adds the user inputs for a new book into the book list.
    :param title_input: User's input for title of the book
    :param author_input: User's input for author of the book
    :param page_input: User's input for the number of pages in the book
    :param line_data: A list consisting of the user inputs for the new book
    :return:
    """
    title_input = str(input("Title:"))
    while title_input == '' or title_input.isspace():
        print("Input cannot be blank")
        title_input = input("Title:")

    author_input = str(input("Author:"))
    while author_input == '' or author_input.isspace():
        print("Input cannot be blank")
        author_input = input("Author:")

    while True:
        try:
            page_input = int(input("Pages:"))
            while page_input < 0:
                print("Number must be >= 0")
                page_input = int(input("Pages:"))
            break
        except ValueError:
            print("Invalid input; enter a valid number")

    line_data = list((title_input, author_input, page_input, 'r'))
    book_list.append(line_data)
    book_list.sort(key=itemgetter(1, 2))
    print("{} by {}, ({} pages) added to reading list".format((title_input), (author_input), (page_input)))

def save_file():
    """
    A function that saves and overwrites the file, books.csv, with the values from book_list
    :return:
    """
    file_edit = open("books.csv", "w")
    data_line = ''
    for line in book_list:
        for value in line:
            if data_line == '':
                data_line = str(value)
            else:
                data_line = (str(data_line) + ',' + str(value))
        file_edit.write(data_line + '\n')
        data_line = ''
    file_edit.close()

#Start of program

print("Reading List v 1.0 by Brandon Lum")

book_list = []
loading_books()

menu_option_list = ['r', 'c', 'a', 'm', 'q']
menu_option = menu_input()

req_book_counter = 1
while menu_option in menu_option_list:

    if menu_option == 'r':
        req_book_counter = required_books()
        menu_option = menu_input()

    elif menu_option == 'c':
        completed_books()
        menu_option = menu_input()

    elif menu_option == 'm':
        req_book_counter = required_books()
        if req_book_counter == 1:
            marking_books()
        menu_option = menu_input()

    elif menu_option == 'a':
        adding_books()
        menu_option = menu_input()

    else:
        save_file()
        menu_option = 'e'

print("{} books saved to books.csv".format(len(book_list)))
print("Have a nice day :)")