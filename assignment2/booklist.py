from operator import itemgetter

# create your BookList class in this file
class BookList:
    def __init__(self):
        self.book_list = []
        bookFile = open("books.csv", "r")
        for line, data in enumerate(bookFile.readlines()):
            line_index = data.strip()
            line_data = line_index.split(",")
            self.book_list.append(line_data)
        bookFile.close()
        self.book_list.sort(key=itemgetter(1, 2))

    def __getitem__(self, item):
        return self.book_list[item]

    def add_book(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        line_data = list((self.title, self.author, self.pages, 'r'))
        self.book_list.append(line_data)

    def get_book(self, book_title):
        self.book_title = book_title
        for index, book in (self.book_list):
            if book[0] == self.book_title:
                print("{} by {} , {}pages (Completed)".format(book[0], book[1], book[2]))

#self.booklists.append(book)


