from assignment2.book import Book

class BookList:
    def __init__(self):
        """
        Initialising the book_list by reading the file (loading the books)
        """
        self.book_list = []
        bookFile = open("books.csv", "r")
        for line, data in enumerate(bookFile.readlines()):
            line_index = data.strip()
            line_data = line_index.split(",")
            book_details = Book(line_data[0],line_data[1],line_data[2],line_data[3])
            self.book_list.append(book_details)
        bookFile.close()

    def __getitem__(self, item):
        return self.book_list[item]

    def get_book(self, book_text):
        """
        Method to determine index of the book in the book_list based on the title of the book
        :param book_text:
        :return:
        """
        for book in self.book_list:
            if book_text == book.title :
                return book

    def add_book(self, book_details):
        """
        Method to append the book details into the book_list
        :param book_details:
        :return:
        """
        self.book_list.append(book_details)

    def save_file(self):
        """
        Method used to save books from book_list into csv file (books.csv)
        :return:
        """
        bookFile = open("books.csv", "w")
        for book in self.book_list:
            bookFile.write(str(book.title) + "," + str(book.author) + "," + str(book.pages) + "," + str(book.status) + "\n")
        bookFile.close()

