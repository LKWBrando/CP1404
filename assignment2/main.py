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

class ReadingListApp(App):

    def build(self):
        self.title = "Reading list application"
        self.root = Builder.load_file("app.kv")
        self.book_list = BookList()
        self.on_required()
        return self.root

    def on_required(self):
        required_page_count = 0
        required_book_count = 0
        for book in self.book_list:
            if book.status == 'r':
                required_page_count += int(book.pages)
                required_book_count += 1
                colour_code = book.book_length()
                if colour_code == 'green':
                    temp_button = Button(text = book.title)
                    temp_button.background_color = 0,1,0,1
                    temp_button.bind(on_press=self.mark)
                    self.root.ids.entriesBox.add_widget(temp_button)
                else:
                    temp_button = Button(text=book.title)
                    temp_button.background_color = 1,1,0,1
                    temp_button.bind(on_press=self.mark)
                    self.root.ids.entriesBox.add_widget(temp_button)

        if required_book_count == 0:
            self.root.ids.display_pages.text = ("All books completed")
            self.root.ids.display_text.text = ("All books completed")
        else:
            self.root.ids.display_pages.text = ("Total pages for {} book(s):{}".format(required_book_count, required_page_count))
            self.root.ids.display_text.text = ("Click books to mark them as completed")

    def mark(self, instance):
        book_text = instance.text
        book_selected = self.book_list.get_book(book_text)
        book_selected.mark_book()
        self.reset()

    def on_completed(self):
        completed_page_count = 0
        completed_book_count = 0
        for book in self.book_list:
            if book.status == 'c':
                completed_page_count += int(book.pages)
                completed_book_count += 1
                temp_button = Button(text=("{}".format(book.title)))
                temp_button.bind(on_release=self.complete_book_details)
                self.root.ids.entriesBox.add_widget(temp_button)
        self.root.ids.display_pages.text = ("Total pages completed:{}".format(completed_page_count))
        self.root.ids.display_text.text = ("Click on a book for more information")

    def complete_book_details(self, instance):
        self.clear_display_text()
        book_text = instance.text
        book_selected = self.book_list.get_book(book_text)
        self.root.ids.display_text.text = book_selected.__str__()

    def save_book(self, input_title, input_author, input_pages):
        self.input_title = str(input_title)
        self.input_author = str(input_author)
        self.input_pages = str(input_pages)
        if self.input_title.isspace() or self.input_author.isspace() or input_pages.isspace():
            self.root.ids.display_text.text = "All fields must be completed"
        else:
            try:
                if int(self.input_pages) <= 0:
                    self.root.ids.display_text.text = 'Please enter a valid number'
                    book_details = Book(self.input_title, self.input_author, self.input_pages, 'r')
                    self.book_list.add_book(book_details)
                    self.temp_button = Button(text=("{}".format(self.input_title)))
                    self.clear_fields()
                    self.reset()
            except ValueError:
                self.root.ids.display_text.text = 'Please enter a valid number'
        return self.book_list

    def display_error(self):
        self.root.ids.display_text.text = "All fields must be completed"

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