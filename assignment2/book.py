# create your simple Book class in this file
class Book:
    def __init__(self, title="", author="", pages=0, status=""):
        self.title = title
        self.author = author
        self.pages = int(pages)
        self.status = status

    def __str__(self):
        return "{} by {}, total pages is {}.".format(self.title, self.author, self.pages)

    def book_length(self):
        if self.pages <= 300:
            colour_code = 'green'
        else:
            colour_code = 'yellow'
        return colour_code

    def mark_book(self):
        self.status = 'c'


