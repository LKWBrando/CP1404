from kivy.app import App
from kivy.uix.button import Button
import sys


class CheckSetupApp(App):

    def build(self):
        return Button(text='hello world')

if __name__ == '__main__':
    # In PyCharm, right-click here and choose 'Run check_setup'
    print("Python version information:", sys.version)
CheckSetupApp().run()