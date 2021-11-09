import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class Touch(Widget):#class will inherit from Widget and be responsible for 
                    #holding our widgets and GUI elements and 
                    # for handling input from the user

    btn = ObjectProperty(None)

    def on_touch_down(self, touch):#first presses on the screen
        print("Mouse Down", touch)
        self.btn.opacity = 0.5

    def on_touch_move(self, touch):#user is touching the screen and moving their finger or mouse
        print("Mouse Move", touch)

    def on_touch_up(self, touch):#user releases the mouse or moves their finger off the screen
        print("Mouse UP",touch)
        self.btn.opacity = 1





class YoApp(App): # <- Main Class
    def build(self):
        return Touch()


if __name__ == "__main__":
   YoApp().run()