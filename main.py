import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


# Main class. Actually implements everything
class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

        """States that the whole thing is one columns (task managers and big submit are on 2 separate grids)"""
        self.cols = 1

        """Initializes the first 'to do' task for MAC"""
        self.MAC = GridLayout()
        self.MAC.cols = 3

        self.MAC.add_widget(Label(text="For MAC1147, PRECAL ALG TRIG", font_size=20))
        self.to_do_MAC = TextInput(multiline=False)
        self.finish_MAC = Button(text="Complete Task", font_size=30)

        """Finish button for this task. binds it to the functions in the botton"""
        self.finish_MAC.bind(on_press=self.MAC_small_button)
        self.MAC.add_widget(self.to_do_MAC)
        self.MAC.add_widget(self.finish_MAC)

       
        """Initializes the first 'to do' task for POS"""
        self.POS = GridLayout()
        self.POS.cols = 3

        self.POS.add_widget(Label(text="For POS2041, AMER NT GOVERN", font_size=20))
        self.to_do_POS = TextInput(multiline=False)
        self.finish_POS = Button(text="Complete Task", font_size=30)
        self.finish_POS.bind(on_press=self.POS_small_button)
        self.POS.add_widget(self.to_do_POS)
        self.POS.add_widget(self.finish_POS)

        """Initializes the first 'to do' task for EVR"""
        self.EVR = GridLayout()
        self.EVR.cols = 3

        self.EVR.add_widget(Label(text="For EVR21001, ENVIO SCI", font_size=20))
        self.to_do_EVR = TextInput(multiline=False)
        self.finish_EVR = Button(text="Complete Task", font_size=30)
        self.finish_EVR.bind(on_press=self.EVR_small_button)
        self.EVR.add_widget(self.to_do_EVR)
        self.EVR.add_widget(self.finish_EVR)

        """Actially adds all to the actual main GridLayout() object"""
        self.add_widget(self.MAC)
        self.add_widget(self.POS)
        self.add_widget(self.EVR)

        """Creates and adds submit button to main GridLayout()"""
        self.finish_all = Button(text="Finish All", font_size=40)
        self.finish_all.bind(on_press=self.all_done_button)
        self.add_widget(self.finish_all)


    """All button press functions. for minor presses and the one big one"""
    def MAC_small_button(self, instance):
        print(f"Done! Completed task: {self.to_do_MAC.text}")

    def POS_small_button(self, instance):
        print(f"Done! Completed task: {self.to_do_POS.text}")
    
    def EVR_small_button(self, instance):
        print(f"Done! Completed task: {self.to_do_EVR.text}")

    def all_done_button(self, instance):
        message = ("Congratulations! You have completed all your tasks!")
        print(message)

# I think this just displays the display on my screen
class MyApp(App):
    def build(self):
        return MyGrid()
    

# runs the whole ting
if __name__ == "__main__":
    MyApp().run()