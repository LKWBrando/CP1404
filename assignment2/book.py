# create your simple Book class in this file
class Book:
    def __init__(self, title="", author="", pages=0, status=""):
        self.title = title
        self.author = author
        self.pages = pages
        self.status = status

    def __str__(self):
        return "{} by {}, total pages is {}.".format(self.title, self.author, self.pages)



