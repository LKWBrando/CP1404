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
while menuInput not in menuInputList:
    print("Invalid Option. Please enter an option from the menu.")
    menuInput = str(input("Menu:\n R - List required books\n C - List completed books\n A - Add new book\n M - Mark a book as completed\n Q - Quit\n")).lower()

if menuInput == 'r':
    required_books()

elif menuInput == 'c':
    completed_books()

elif menuInput == 'm':
    required_books()
    markingCondition = False
    while markingCondition:
        try:
            mark_book = int(input("Enter the number of a book to mark as completed."))
            while bookList[mark_book]
            markingCondition = True
        except ValueError:
            print("Invalid input; enter a valid number.")
    print(bookList[mark_book])
