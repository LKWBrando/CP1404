from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934


class MilesConverterApp(App):

    def build(self):
        self.title = 'Conversion Calculator'
        self.root = Builder.load_file('dfs1.kv')
        return self.root

MilesConverterApp().run()