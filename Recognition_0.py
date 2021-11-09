from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock, mainthread
from kivy.core.text import LabelBase
from KivyCalendar import CalendarWidget
from kivy.uix.popup import Popup
from kivy.properties import StringProperty
import speech_recognition as sr
from kivy.clock import Clock
import time
import datetime
  
LabelBase.register(name="Lato" , fn_regular="Lato-BlackItalic.ttf") #font_style 

class Principal(Screen):
    def BtnEscuchar(self):
        self.ids.lblMensaje.text = "Recording Start !"
        Clock.schedule_once(lambda d: self.GetAudio(), 0)
        
    def setDateHA(self):
        self.calSetDate=CalendarWidget(as_popup=True)
        self.popup = Popup(title='Calendar',content=self.calSetDate,size_hint=(0.8,0.6))
        self.popup.open()
    def GetAudio(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
        self.audio = audio
        try:
            self.ids.lblMensaje.text = "Your Hospital  appointment on " + r.recognize_google(audio, language = 'es')
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
class testspkApp(App):
    time = StringProperty()
    def update(self,*args):
        self.time = str(time.asctime())
    def build(self):
        sm = ScreenManager()
        self.sm = sm
        sm.add_widget(Principal(name='Principal'))
        Clock.schedule_interval(self.update,1)
        return sm
 
    def on_pause(self):
        return False
 
 
main = testspkApp()
main.run()
