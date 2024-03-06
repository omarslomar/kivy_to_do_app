import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="Frist Name:"))
        self.first_name = TextInput(multiline=False)
        self.add_widget(self.first_name)

        self.add_widget(Label(text="Last Name:"))
        self.last_name = TextInput(multiline=False)
        self.add_widget(self.last_name)

        self.add_widget(Label(text="Age:"))
        self.age = TextInput(multiline=False)
        self.add_widget(self.age)



class MyApp(App):
    def build(self):
        return MyGrid()
    


if __name__ == "__main__":
    MyApp().run()