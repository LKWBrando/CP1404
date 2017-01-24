"""
Name:
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
from operator import itemgetter

book_list = BookList()
req_counter = 1

class ReadingListApp(App):

    def on_required(self):
        required_page_count = 0
        required_book_count = 0
        req_counter = 1
        for index, book in enumerate(book_list):
            if book[3] == 'r':
                required_page_count += int(book[2])
                required_book_count += 1
                temp_button = Button(text = ("{:<1}. {:<40s} by {:<20s} {:<4}pages".format(index, book[0], book[1], book[2])))
                temp_button.bind(on_release=self.press)
                self.root.ids.entriesBox.add_widget(temp_button)
        if required_book_count == 0:
            temp_button = Button(text ="No required books")
            temp_button.bind(on_release=self.press)
            req_counter = 0
            return req_counter
        else:
            self.root.ids.display_pages.text = ("Total pages for {} book(s):{}".format(required_book_count, required_page_count))
            self.root.ids.display_text.text = ("Click books to mark them as completed")
            return req_counter


    def on_completed(self):
        completed_page_count = 0
        completed_book_count = 0
        for index, book in enumerate(book_list):
            if book[3] == 'c':
                completed_page_count += int(book[2])
                completed_book_count += 1
                temp_button = Button(text=("{:<1}.{:<40s}by {:<20s} {:<4}pages".format(index, book[0], book[1], book[2])))
                temp_button.bind(on_release=self.press)
                self.root.ids.entriesBox.add_widget(temp_button)
        self.root.ids.display_pages.text = ("Total pages for {} book(s):{}".format(completed_book_count, completed_page_count))
        self.root.ids.display_text.text = ("Click on a book for more information")


    def save_book(self, input_title, input_author, input_pages):
        self.input_title = str(input_title)
        self.input_author = str(input_author)
        self.input_pages = int(input_pages)
        book_list.add_book(self.input_title, self.input_author, self.input_pages)
        self.root.ids.input_title.text = ""
        self.root.ids.input_author.text = ""
        self.root.ids.input_pages.text = ""
        return book_list

    def press(self, instance):
        pass

    def clear_all(self):
        self.root.ids.entriesBox.clear_widgets()

    def build(self):
        self.title = "Reading list application"
        self.root = Builder.load_file("app.kv")
        return self.root


ReadingListApp().run()
