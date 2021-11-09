import kivy
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.lang import Builder   # to import multiple screen
from kivy.uix.screenmanager import ScreenManager,Screen # to import multiple screen

class WindowManager(ScreenManager):
    pass
class MainWindow(Screen):
    name = ObjectProperty(None)
    email = ObjectProperty(None)

    def btn(self):
        print ("Name:", self.name.text,"Email:", self.Email.text)
        self.name.text=""
        self.Email.text=""
        kv = Builder.load_file("my.kv")
class SecondWindow(Screen): 
    def btn(self):
        show_popup()
    def show_popup():
     show = P()

    popupWindow = Popup(title="Popup Window", content=Label(text='Please fill in all inputs with valid information.'), size_hint=(None,None),size=(400,400))

    popupWindow.open()
   
class Widgets(Widget):
  pass

class P(FloatLayout):
    pass

class UTGApp(App):
    def build(self):
        return WindowManager()


if __name__ == "__main__":
    UTGApp().run()