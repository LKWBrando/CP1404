from kivy.app import App
from kivy.lang import Builder

class Loopingstring(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.string_list = ['a', 'b', 'c', 'd', 'e']

    def build(self):
        self.title("Looping string")
        self.root = Builder.load_file('dfs1.kv')
        self.create_string()
        return self.root

    def create_string(self):
        for name in self.string_list:
            temp_button = Button(text=name)
            temp_button.bind(on_release=self.press_entry)
            # add the button to the "entriesBox" using add_widget()
            self.root.ids.entriesBox.add_widget(temp_button)

Loopingstring().run()