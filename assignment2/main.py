"""
Name:Lum Kwan Wei Brandon
Date:
Brief Project Description:
GitHub URL:
Testing
"""
from assignment2.book import Book
from assignment2.booklist import BookList
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

book_list = BookList()
req_counter = 1

class ReadingListApp(App):

    def build(self):
        self.title = "Reading list application"
        self.root = Builder.load_file("app.kv")
        self.on_required()
        return self.root

    def on_required(self):
        required_page_count = 0
        required_book_count = 0
        req_counter = 1
        for index, book in enumerate(book_list):
            if book[3] == 'r':
                required_page_count += int(book[2])
                required_book_count += 1
                book_text = book[0]
                temp_button = Button(text = book_text)
                temp_button.bind(on_press=self.mark)
                self.root.ids.entriesBox.add_widget(temp_button)
        if required_book_count == 0:
            self.root.ids.display_pages.text = ("All books completed")
            self.root.ids.display_text.text = ("All books completed")
            req_counter = 0
            return req_counter
        else:
            self.root.ids.display_pages.text = ("Total pages for {} book(s):{}".format(required_book_count, required_page_count))
            self.root.ids.display_text.text = ("Click books to mark them as completed")
            return req_counter

    def mark(self, instance):
        book_text=instance.text
        for book in book_list:
            for item in book:
                if item == book_text:
                    book.pop(3)
                    book.insert(3,'c')
        self.reset()



    def on_completed(self):
        completed_page_count = 0
        completed_book_count = 0
        for index, book in enumerate(book_list):
            if book[3] == 'c':
                completed_page_count += int(book[2])
                completed_book_count += 1
                book_text = book[0]
                temp_button = Button(text=("{}".format(book_text)))
                temp_button.bind(on_release=self.book_details)
                self.root.ids.entriesBox.add_widget(temp_button)
        self.root.ids.display_pages.text = ("Total pages completed:{}".format(completed_page_count))
        self.root.ids.display_text.text = ("Click on a book for more information")

    def book_details(self, instance):
        self.clear_display_text()
        book_text = instance.text
        for index, book in enumerate(book_list):
            if book[0] == book_text:
                self.root.ids.display_text.text = ("{} by {} , {}pages (Completed)".format(book[0], book[1], book[2]))

    def save_book(self, input_title, input_author, input_pages):
        self.input_title = str(input_title)
        self.input_author = str(input_author)
        self.input_pages = int(input_pages)
        book_list.add_book(self.input_title, self.input_author, self.input_pages)
        self.temp_button = Button(text=("{}".format(self.input_title)))
        self.on_required()
        self.clear_fields()
        return book_list

    def clear_display_text(self):
        self.root.ids.display_text.text = ""

    def clear_fields(self):
        self.root.ids.input_title.text = ""
        self.root.ids.input_author.text = ""
        self.root.ids.input_pages.text = ""

    def reset(self):
        self.clear_all()
        self.on_required()

    def clear_all(self):
        self.root.ids.entriesBox.clear_widgets()

ReadingListApp().run()