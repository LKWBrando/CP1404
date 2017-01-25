from operator import itemgetter
from assignment2.book import Book

# create your BookList class in this file
class BookList:
    def __init__(self):
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
        for book in self.book_list:
            if book_text == book.title :
                return book

    def add_book(self, book_details):
        self.book_list.append(book_details)





BookList()