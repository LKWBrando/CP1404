"""
Name:Lum Kwan Wei Brandon
Date of submission: 27/01/2017
Brief Project Description:

Reading list application.
As per assignment instructions, this file contains a program that creates a GUI when run.
Users will be able to select books to mark as completed and completed book details by clicking corresponding buttons.

GitHub URL: https://github.com/LKWBrando/CP1404/tree/master/assignment2 (private repository)
"""
from assignment2.book import Book
from assignment2.booklist import BookList
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
import atexit

class ReadingListApp(App):

    def build(self):
        """
        Loading of the GUI
        :return:
        """
        self.title = "Reading list application"
        self.root = Builder.load_file("app.kv")
        self.book_list = BookList()
        self.on_click_required()
        atexit.register(self.book_list.save_file)
        return self.root

    def on_click_required(self):
        """
        Method that creates the required list of books via buttons, and displays corresponding texts on panels
        """
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
                    self.root.ids.book_list_box.add_widget(temp_button)
                else:
                    temp_button = Button(text=book.title)
                    temp_button.background_color = 1,1,0,1
                    temp_button.bind(on_press=self.mark)
                    self.root.ids.book_list_box.add_widget(temp_button)

        if required_book_count == 0:
            self.root.ids.display_pages.text = ("All books completed")
            self.root.ids.display_text.text = ("All books completed")
        else:
            self.root.ids.display_pages.text = ("Total pages for {} book(s):{}".format(required_book_count, required_page_count))
            self.root.ids.display_text.text = ("Click books to mark them as completed")

    def mark(self, instance):
        """
        A method where the text of the instance is passed through other methods in order to change the book.status
        Updates and refreshes the GUI accordingly
        :param instance: Details of the button
        """
        book_text = instance.text
        book_selected = self.book_list.get_book(book_text)
        book_selected.mark_book()
        self.reset()

    def on_click_completed(self):
        """
        Method that creates the completed list of books via buttons, and displays corresponding texts on panels
        :return:
        """
        completed_page_count = 0
        completed_book_count = 0
        for book in self.book_list:
            if book.status == 'c':
                completed_page_count += int(book.pages)
                completed_book_count += 1
                temp_button = Button(text=("{}".format(book.title)))
                temp_button.bind(on_release=self.complete_book_details)
                self.root.ids.book_list_box.add_widget(temp_button)
        self.root.ids.display_pages.text = ("Total pages completed:{}".format(completed_page_count))
        self.root.ids.display_text.text = ("Click on a book for more information")

    def complete_book_details(self, instance):
        """
        A method used to display details of a book by using its title to get those details
        :param instance: Details of the button
        """
        self.clear_display_text()
        book_text = instance.text
        book_selected = self.book_list.get_book(book_text)
        self.root.ids.display_text.text = book_selected.__str__()

    def save_book(self, input_title, input_author, input_pages):
        """
        A method that allows the user to input a book and its details into the book_list.
        There is an error check to ensure there are no black spaces and that the page input must be a number
        :param input_title: Title input from user on the GUI
        :param input_author: Author input from user on the GUI
        :param input_pages: Number of pages input from user on the GUI
        :return: Updated book_list
        """
        self.input_title = str(input_title)
        self.input_author = str(input_author)
        self.input_pages = str(input_pages)
        #Line to warn user that no blank spaces are allowed for input
        if self.input_title.isspace() or input_title == "" or self.input_author.isspace() or input_author == "" or input_pages.isspace() or input_pages =="":
            self.clear_fields()
            self.reset()
            self.root.ids.display_text.text = "All fields must be completed"
        else:
            try:
                if int(self.input_pages) >= 0:
                    book_details = Book(self.input_title, self.input_author, self.input_pages, 'r')
                    self.book_list.add_book(book_details)
                    self.temp_button = Button(text=("{}".format(self.input_title)))
                    self.clear_fields()
                    self.reset()
            except ValueError:
                self.root.ids.display_text.text = 'Please enter a valid number'
                self.clear_fields()
        return self.book_list

    def display_error(self):
        """
        Simple method used to display warning text for the display_text label (Bottom label)
        """
        self.root.ids.display_text.text = "All fields must be completed"

    def clear_display_text(self):
        """
        Simple method used to reset text for the display_text label (Bottom label)
        """
        self.root.ids.display_text.text = ""

    def clear_fields(self):
        """
        Method used to reset all the user input fields in the GUI
        """
        self.root.ids.input_title.text = ""
        self.root.ids.input_author.text = ""
        self.root.ids.input_pages.text = ""

    def reset(self):
        """
        Method used to clear all widgets and reload the required book_list.
        :return:
        """
        self.clear_all()
        self.on_click_required()

    def clear_all(self):
        """
        Method used to clear all widgets in the book_list_box BoxLayout
        """
        self.root.ids.book_list_box.clear_widgets()


ReadingListApp().run()

