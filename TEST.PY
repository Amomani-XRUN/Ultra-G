from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout  # one of many layout structures
from kivy.uix.textinput import TextInput  # allow for ...text input.
from kivy.uix.button import Button
from kivy.uix.widget import Widget




class MyWidget(Widget)
pass
class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols=1

        self.inside = GridLayout()
        self.inside.cols=2
        

        self.inside.add_widget(Label(text="First Name: "))
        self.firstname = TextInput(multiline=False)
        self.inside.add_widget(self.firstname)

        self.inside.add_widget(Label(text="Last Name: "))
        self.lastname = TextInput(multiline=False)
        self.inside.add_widget(self.lastname)

        self.inside.add_widget(Label(text="Email: "))
        self.email= TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)
        self.submit = Button(text="Submit", font_size=15)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

#create function save to the system
    def pressed (self, instance):
        firstname = self.firstname.text
        lastname = self.lastname.text
        email = self.email.text
        print("name:" , firstname,"LastName:",lastname, "Email:",email)


#clear value       
        self.firstname.text=""
        self.lastname.text=""
        self.email.text=""

        

       
 
class MyApp(App):
 
    def build(self):
        return MyGrid()
if __name__=="__main__":
    MyApp().run()