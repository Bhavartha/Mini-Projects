from kivy.app import App
# kivy.require("1.8.0")
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout


class Calc_layout(GridLayout):
    def answers(self, num):
        if num:
            try:
                self.ids.entry.text = str(eval(num))
                # print(self.display.text)
            except:
                self.ids.entry.text = "Error"


class CalcApp(App):

    def build(self):
        return Calc_layout()
    x = 'lol'


if __name__ == "__main__":
    CalcApp().run()
