class Book:
    def __init__(self, title="", author="", pages=0, status=""):
        self.title = title
        self.author = author
        self.pages = int(pages)
        self.status = status

    def __str__(self):
        return "{} by {}, total pages is {}.".format(self.title, self.author, self.pages)

    def book_length(self):
        """
        Simple method used to determine which colour button, green(short) or yellow(long),
        to be displayed based on the number of pages
        :return:string value of 'green' or 'yellow
        """
        if self.pages <= 300:
            colour_code = 'green'
        else:
            colour_code = 'yellow'
        return colour_code

    def mark_book(self):
        """
        Simple method used to change the status of a required book to completed.
        """
        self.status = 'c'


