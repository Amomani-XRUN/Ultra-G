from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from database import Database



class MyFloat(FloatLayout):
    pass
class UserCreateWindow(Screen):
    UltraCode = ObjectProperty(None)
    UltraPass = ObjectProperty(None)


    def submit (self):
        if self.UltraCode.text !="":
            if self.UltraPass !="":
                db.add_user(self.UltraCode.text,self.UltraPass.text)

                self.reset()

                sm.current = "userlogin"
            else:
                invalidForm()
        else:
            invalidForm() 

    def login(self):
        self.reset()
        sm.current = "userlogin"
    def reset(self):
        self.UltraCode.text = ""
        self.UltraPass.text = "" 

class UserLoginWindow(Screen):
    UltraCode = ObjectProperty(None)
    UltraPass = ObjectProperty(None)

    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "main"
        else:
            invalidLogin()
    def createBtn(self):
                self.reset()
                sm.current ="usercreate"
    def reset(self):
                    self.UltraPass.text = ""

class MainWindow(Screen):
    
    def logOut(self):
        sm.current = "userlogin"
       
                

class WindowManager(ScreenManager):
     pass
    
def invalidForm():
        Vpop = Popup(Title = 'Invalid',content=Label(text='Login Falid :(INVALID PASSWORD)'), size_hint=(None, None), size=(400, 200))
        Vpop.open()


def invalidLogin():
        Vpop = Popup(Title = 'Invalid',content=Label(text='Login Falid :(INVALID PASSWORD)'), size_hint=(None, None), size=(400, 200))
        Vpop.open()

db=Database("UltraUserPass.text")
kv = Builder.load_file("ultra.kv")
sm=WindowManager()
screens=[UserCreateWindow(name="userlogin"),UserLoginWindow(name="usercreate"),MainWindow(name="main")]
for screen in screens :
    sm.add_widget(screen)

sm.current = "userlogin"
class UltraGApp(App):
    def build(self):
        return sm
if __name__=="__main__":
    UltraGApp().run()        


        


