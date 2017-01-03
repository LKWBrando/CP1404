def menu_Input(menuInput):
    while menuInput not in menuInputList:
        print("Invalid Option. Please enter an option from the menu.")
        menuInput = str(input("Menu:\n R - List required books\n C - List completed books\n A - Add new book\n M - Mark a book as completed\n Q - Quit\n")).lower()


def required_books():
    print("Required books:")
    required_pageCount = 0
    required_bookCount = 0
    for i, book in enumerate(bookList):
        if book[3] == 'r':
            required_pageCount = required_pageCount + int(book[2])
            required_bookCount = required_bookCount + 1
            print("{:<1}.{:<40s}by {:<20s} {:<4}pages".format(i,book[0], book[1], book[2]))
    print("Total pages for {} book(s):{}".format(required_bookCount, required_pageCount))


def completed_books():
    print("Completed books:")
    completed_pageCount = 0
    completed_bookCount = 0
    for i, book in enumerate(bookList):
        if book[3] == 'c':
            completed_pageCount = completed_pageCount + int(book[2])
            completed_bookCount = completed_bookCount + 1
            print("{:<1}.{:<40s}by {:<20s} {:<4}pages".format(i, book[0], book[1], book[2]))
    print("Total pages for {} book(s):{}".format(completed_bookCount, completed_pageCount))

def marking_books():
    checker1 = True
    while checker1:
        try:
            mark_book = int(input("Enter the number of a book to mark as completed."))
            while mark_book > (len(bookList) - 1):
                print("Error, number not in list.")
                mark_book = int(input("Enter the number of a book to mark as completed."))
            checker1 = False
        except ValueError:
            print("Invalid format; enter a valid number.")
    return mark_book

print("Reading List v 1.0 by Brandon Lum")

bookList = []
bookFile = open("books.csv", "r")
for line, data in enumerate(bookFile.readlines()):
    lineIndex = data.strip()
    lineData = lineIndex.split(",")
    bookList.append(lineData)
print("{} books loaded from books.csv".format(len(bookList)))
print(bookList)

menuInputList = ['r', 'c', 'a' ,'m', 'q']
menuInput = str(input("Menu:\n R - List required books\n C - List completed books\n A - Add new book\n M - Mark a book as completed\n Q - Quit\n")).lower()
menu_Input(menuInput)

while menuInput in menuInputList:

    if menuInput == 'r':
        required_books()
        menuInput = str(input("Menu:\n R - List required books\n C - List completed books\n A - Add new book\n M - Mark a book as completed\n Q - Quit\n")).lower()
        menu_Input(menuInput)

    elif menuInput == 'c':
        completed_books()
        menuInput = str(input("Menu:\n R - List required books\n C - List completed books\n A - Add new book\n M - Mark a book as completed\n Q - Quit\n")).lower()
        menu_Input(menuInput)

    elif menuInput == 'm':
        required_books()
        mark_book = marking_books()

        if bookList[mark_book][3] == 'r':
            print("{:<40s} by {:<20s} marked as completed".format(bookList[mark_book][0], bookList[mark_book][1]))
            bookList[mark_book].pop(3)
            bookList[mark_book].insert(3,'c')
        else:
            print("That book is already completed")
        menuInput = str(input("Menu:\n R - List required books\n C - List completed books\n A - Add new book\n M - Mark a book as completed\n Q - Quit\n")).lower()
        menu_Input(menuInput)

    elif menuInput == 'a':
        title_Input = input(str("Title:"))
        author_Input

