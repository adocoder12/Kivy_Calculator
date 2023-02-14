from kivy.app import App
from kivy.uix.widget import Widget
#from kivy.core.window Window #jotta fullscreen

class CalcWidget(Widget):
    def __init__(self):
        super().__init__()
    # laskimen toiminnallisuus tänne

class Calculator(App):
    def build(self):
        return CalcWidget()

if __name__=='__main__':
    Calculator().run()