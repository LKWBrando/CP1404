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

class ReadingListApp(App):
    def on_start(self): # this will do initialization
        print("on_start is called.")
        # file opening
        myfile = open("books.csv", "r")
        booklists = myfile.readlines()
        print(booklists)
        myfile.close()
        #....linking
        temp_button = Button(text="Testing one")
        temp_button.bind(on_release=self.press)
        self.root.ids.entriesBox.add_widget(temp_button)

        temp_button = Button(text="Testing two")
        temp_button.bind(on_release=self.press)
        self.root.ids.entriesBox.add_widget(temp_button)

    def press(self, instance):
        pass

    def build(self):
        self.title = "Reading list application"
        self.root = Builder.load_file("app.kv")
        return self.root


ReadingListApp().run()
