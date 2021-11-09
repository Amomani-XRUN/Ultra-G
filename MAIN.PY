
from kivy.app import App
import os
from kivy.uix.dropdown import DropDown 
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.properties import ListProperty
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.event import EventDispatcher
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.graphics import Color, Line
from math import cos,sin,pi
from kivy.core.window import Window
from KivyCalendar import CalendarWidget
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
from database import *
from DatabaseSQL import*
from kivy.core.text import LabelBase
from cx_Oracle import Error
from passlib.hash import sha256_crypt
#from kivy.config import Config
#Config.set('kivy', 'keyboard_mode', 'systemandmulti')

#from clock import *
#from maincal import mainAPP


import pyodbc
from datetime import datetime
import getpass
import hashlib
import sqlite3
import calendar
import time
import datetime
import sqlite3
import  random
        



conn = sqlite3.connect('userlogin.db')
c=conn.cursor()

LabelBase.register(name="Antonio" , fn_regular="AntonioB.ttf") #font_style 

LabelBase.register(name="Lato" , fn_regular="Lato-BlackItalic.ttf") #font_style 

LabelBase.register(name="Aller" , fn_regular="Aller_BdIt.ttf") #font_style 

Window.clearcolor = (0,0,0,1)





class CreateAccountWindow(Screen):
    code = ObjectProperty()
    password = ObjectProperty() 
    
    def submit(self):
        #md5 = hashlib.md5()    // Encryption
        code =self.ids.code.text
        password = self.ids.password.text
        #md5.update(password)
       #md5.digest()x

        if code =="DPHRGCML1707013919":
            if password  != "":
                with conn:
                    #c.execute("Select * from useradd where userid = ?", (code, ))
                   # check1=c.fetchone()
                    # check1[0] != None:
                       # passexit()
                        
                   # else:  
                    c.execute("INSERT INTO  useradd  (userid, password) VALUES (?,?)", (code,password)) 
                       
                       
                   
                    
                
                  
            
                    conn.commit()

               
                

                self.ids.code.text =""
                self.ids.password.text= ""
                sm.current = "login"
            else:                                      
                invalidForm()
        else:
            invalidForm()
        

    def login(self):
        self.ids.code.text =""
        self.ids.password.text= ""
        sm.current = "login"

  
        
  


class LoginWindow(Screen):
    
    password = ObjectProperty(None)

    def loginBtn(self):
        password = self.ids.password.text
        

        c.execute("SELECT password from useradd WHERE password = ? ",(password,))
        datalog = c.fetchall()
        conn.commit()
        
        if  not datalog:
            invalidLogin()
        else:
          self.ids.password.text = ""
          sm.current = "main"  

    def createBtn(self):
        self.ids.password.text = ""
        sm.current = "create"

    
       
        
        
        


class MainWindow(Screen):
    code = ObjectProperty(None)


   
def on_enter(code, self):
        
    c.execute("Select * from useradd where userid = ?", (code, ))
    check1=c.fetchone()
    if check1[0] == "DPHRGCML1707013919":\
                   print ("DPHRGCML1707013919")\
    
   
    
    def logOut(self):
        sm.current = "login"


def passexit():
    pop = Popup(title='Invalid Login ',
                  content=Label(font_name='Lato',text='The serial code already exist'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()

def invalidMCLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(font_name='Lato',text='Please fill out the blank field'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()




def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(font_name='Lato',text='Invalid Password '),
                  size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(font_name='Lato',text='Please fill in valid information.'),
                  size_hint=(None, None), size=(400, 400))

    pop.open()

class MenuWindow(Screen):

    def CalFunctionBtn(self):
        sm.current = "cal"
    def ParkFunctionBtn(self):
        sm.current = "view"    
    def MCFunctionBtn(self):
        sm .current = "MC"    

     
    


    def helpBtnFun(self):
        hpop = Popup(title='HELP'
        ,content=Label(font_name='Lato',text='system: User able to chose one of this function\n \n Booking Parking: (help user to book handicapped tag ) \n \n Hospital Appointment : (help user to make appointment with any doctor in certain loction ) \n \nMedicen Reminder: (To remind the user about the time for taking the medication)'),
        size_hint=(None,None),size=(700,400))               

        hpop.open()  



         

   



  
    
class CalMenuWindow(Screen):
    def setDate(self):
        os.system("maincalfix.py")
       # self.calSetDate=CalendarWidget(as_popup=True)
       # self.popup = Popup(title='Calendar',content=self.calSetDate,size_hint=(0.8,0.6))
        #self.popup.open()
        

       
        popup = Popup(title='Set Reminder',content=TextInput(),size=(400,400),size_hint=(None,None))  
        popup.open()
        
    def setLocation(self):
        os.system("map_browser.py")

    def speech(self):
        os.system("Recognition.py")
    def clickpop(self):
        box = BoxLayout(orienation = 'vertical', padding = (10))
        box.add_widget(Label(text="Seve the changes ?!!"))
        btn1 = Button(text = " Save")
        btn2 = Button(text = "Go back")
        box.add_widget(btn1)
        box.add_widget(btn2)

        btn1.bind(on_press = self.dismiss)
        btn2.bind(on_press = self.hypochlorinator_1)

   

    def helpBtnCal(self):
        hpop = Popup(title='HELP'
        ,content=Label(font_name='Lato',text='To make hospital appointment the user \n\n can choose SET- REMINDER and VOCISE-REMINDER \n\n in SET- REMINDER the user able to choose the date and time also Doctor name\n\n , VOICES-REMINDER the user set the time \n\n and the date using voices recognizer\n\n The user can search nearby hospital or\n\n looking for certain hospital from the map \n\n If you found any trouble with the booking please contact : \n\n +601111217556     '),
        size_hint=(None,None),size=(600,400)) 
        hpop.open()   


class Parking2MenuWindow(Screen):
    pass
class ParkingViewWindow(Screen):
    pass
class Parking1MenuWindow(Screen):
    pass




class ParkingTimeBookOne(Screen):
    def notification(self):

        parkingNum = self.ids.parking_num.text
        Car = self.ids.Car.text
        LC = self.ids.LC.text
        EXPDate = self.ids.EXP_Date.text
        EmailAdd = self.ids.Email_Add.text

        if parkingNum  != "":
            if EmailAdd !="":

                with conn:
                
                    c.execute("INSERT INTO bookparking (parkingNumber, LCNumber, LCEXPDate, CarNumber, EmailAddress) VALUES (?,?,?,?,?)", 
                    (parkingNum, Car, LC, EXPDate, EmailAdd))
                
            
                    conn.commit()

               
                os.system("Bookparking-notification.py")

                
            
                sm.current = "function"
            else:                                      
                invalidForm()   
        else:                                      
            invalidForm()
        
    def helpBtnBook(self):
        parkingNum = self.ids.parking_num.text
        Car = self.ids.Car.text
        LC = self.ids.LC.text
        EXPDate = self.ids.EXP_Date.text
        EmailAdd = self.ids.Email_Add.text

        if parkingNum  != "":
            if EmailAdd !="":

                with conn:
                
                    c.execute("INSERT INTO bookparking (parkingNumber, LCNumber, LCEXPDate, CarNumber, EmailAddress) VALUES (?,?,?,?,?)", 
                    (parkingNum, Car, LC, EXPDate, EmailAdd))
                
            
                    conn.commit()

               
                os.system("Bookparking-notification.py")

                
            
                sm.current = "function"
            else:                                      
                invalidForm()   
        else:                                      
            invalidForm()
        hpop = Popup(title='HELP'
        ,content=Label(font_name='Lato',text='For book the handicap spot  \n \n there is three available parking that the user can choose \n\n -B1:A1:P2\n -B1:A2:P2\n -B2:A2:P3 \n\n (A) Address , (B) Building , (P) Parking \n\n To make the registeration the user need to fill-up some information as : \n\n - Valid License Number \n- Expired Date \n-Car Plate Number \n -Vaild Email Address \n\n If you found any trouble with the booking please contact : \n +601111217556    '),
        size_hint=(None,None),size=(490,420))               

        hpop.open()

class ParkingTimeBookTwo(Screen):
    def notification(self):    
        parkingNum = self.ids.parking_num.text
        Car = self.ids.Car.text
        LC = self.ids.LC.text
        EXPDate = self.ids.EXP_Date.text
        EmailAdd = self.ids.Email_Add.text

        if parkingNum  != "":
            if EmailAdd !="":

                with conn:
                
                    c.execute("INSERT INTO bookparking (parkingNumber, LCNumber, LCEXPDate, CarNumber, EmailAddress) VALUES (?,?,?,?,?)", 
                    (parkingNum, Car, LC, EXPDate, EmailAdd))
                
            
                    conn.commit()

               
                os.system("Bookparking-notification.py")

                
            
                sm.current = "function"
            else:                                      
                invalidForm()   
        else:                                      
            invalidForm()
   
        
       
    def helpBtnBook(self):
        hpop = Popup(title='HELP'
        ,content=Label(font_name='Lato',text='For book the handicap spot  \n \n there is three available parking that the user can choose \n\n -B1:A1:P2\n -B1:A2:P2\n -B2:A2:P3 \n\n (A) Address , (B) Building , (P) Parking \n\n To make the registeration the user need to fill-up some information as : \n\n - Valid License Number \n- Expired Date \n-Car Plate Number \n -Vaild Email Address \n\n If you found any trouble with the booking please contact : \n +601111217556    '),
        size_hint=(None,None),size=(490,420))               

        hpop.open()  
class ParkingTimeBookThree(Screen):
    def notification(self):
        parkingNum = self.ids.parking_num.text
        Car = self.ids.Car.text
        LC = self.ids.LC.text
        EXPDate = self.ids.EXP_Date.text
        EmailAdd = self.ids.Email_Add.text

        if parkingNum  != "":
            if EmailAdd !="":

                with conn:
                
                    c.execute("INSERT INTO bookparking (parkingNumber, LCNumber, LCEXPDate, CarNumber, EmailAddress) VALUES (?,?,?,?,?)", 
                    (parkingNum, Car, LC, EXPDate, EmailAdd))
                
            
                    conn.commit()

               
                os.system("Bookparking-notification.py")

                
            
                sm.current = "function"
            else:                                      
                invalidForm()   
        else:                                      
            invalidForm()
    def helpBtnBook(self):
        hpop = Popup(title='HELP'
        ,content=Label(font_name='Lato',text='For book the handicap spot  \n \n there is three available parking that the user can choose \n\n -B1:A1:P2\n -B1:A2:P2\n -B2:A2:P3 \n\n (A) Address , (B) Building , (P) Parking \n\n To make the registeration the user need to fill-up some information as : \n\n - Valid License Number \n- Expired Date \n-Car Plate Number \n -Vaild Email Address \n\n If you found any trouble with the booking please contact : \n +601111217556    '),
        size_hint=(None,None),size=(490,420))               

        hpop.open()  

class ParkingTimeBookFour(Screen):
    def notification(self):
        
        parkingNum = self.ids.parking_num.text
        Car = self.ids.Car.text
        LC = self.ids.LC.text
        EXPDate = self.ids.EXP_Date.text
        EmailAdd = self.ids.Email_Add.text

        if parkingNum  != "":
            if EmailAdd !="":

                with conn:
                
                    c.execute("INSERT INTO bookparking (parkingNumber, LCNumber, LCEXPDate, CarNumber, EmailAddress) VALUES (?,?,?,?,?)", 
                    (parkingNum, Car, LC, EXPDate, EmailAdd))
                
            
                    conn.commit()

               
                os.system("Bookparking-notification.py")

                
            
                sm.current = "function"
            else:                                      
                invalidForm()   
        else:                                      
            invalidForm()
    def helpBtnBook(self):
        hpop = Popup(title='HELP'
        ,content=Label(font_name='Lato',text='For book the handicap spot  \n \n there is three available parking that the user can choose \n\n -B1:A1:P2\n -B1:A2:P2\n -B2:A2:P3 \n\n (A) Address , (B) Building , (P) Parking \n\n To make the registeration the user need to fill-up some information as : \n\n - Valid License Number \n- Expired Date \n-Car Plate Number \n -Vaild Email Address \n\n If you found any trouble with the booking please contact : \n +601111217556    '),
        size_hint=(None,None),size=(490,420))               

        hpop.open()  

class ParkingTimeBookFive(Screen):
    def notification(self):
        
        parkingNum = self.ids.parking_num.text
        Car = self.ids.Car.text
        LC = self.ids.LC.text
        EXPDate = self.ids.EXP_Date.text
        EmailAdd = self.ids.Email_Add.text

        if parkingNum  != "":
            if EmailAdd !="":

                with conn:
                
                    c.execute("INSERT INTO bookparking (parkingNumber, LCNumber, LCEXPDate, CarNumber, EmailAddress) VALUES (?,?,?,?,?)", 
                    (parkingNum, Car, LC, EXPDate, EmailAdd))
                
            
                    conn.commit()

               
                os.system("Bookparking-notification.py")

                
            
                sm.current = "function"
            else:                                      
                invalidForm()   
        else:                                      
            invalidForm()
    def helpBtnBook(self):
        hpop = Popup(title='HELP'
        ,content=Label(font_name='Lato',text='For book the handicap spot  \n \n there is three available parking that the user can choose \n\n -B1:A1:P2\n -B1:A2:P2\n -B2:A2:P3 \n\n (A) Address , (B) Building , (P) Parking \n\n To make the registeration the user need to fill-up some information as : \n\n - Valid License Number \n- Expired Date \n-Car Plate Number \n -Vaild Email Address \n\n If you found any trouble with the booking please contact : \n +601111217556    '),
        size_hint=(None,None),size=(490,420))               

        hpop.open()  

class ParkingTimeBookSix(Screen):
    def notification(self):
        parkingNum = self.ids.parking_num.text
        Car = self.ids.Car.text
        LC = self.ids.LC.text
        EXPDate = self.ids.EXP_Date.text
        EmailAdd = self.ids.Email_Add.text

        if parkingNum  != "":
            if EmailAdd !="":

                with conn:
                
                    c.execute("INSERT INTO bookparking (parkingNumber, LCNumber, LCEXPDate, CarNumber, EmailAddress) VALUES (?,?,?,?,?)", 
                    (parkingNum, Car, LC, EXPDate, EmailAdd))
                
            
                    conn.commit()

               
                os.system("Bookparking-notification.py")

                
            
                sm.current = "function"
            else:                                      
                invalidForm()   
        else:                                      
            invalidForm()
    def helpBtnBook(self):
        hpop = Popup(title='HELP'
        ,content=Label(font_name='Lato',text='For book the handicap spot  \n \n there is three available parking that the user can choose \n\n -B1:A1:P2\n -B1:A2:P2\n -B2:A2:P3 \n\n (A) Address , (B) Building , (P) Parking \n\n To make the registeration the user need to fill-up some information as : \n\n - Valid License Number \n- Expired Date \n-Car Plate Number \n -Vaild Email Address \n\n If you found any trouble with the booking please contact : \n +601111217556    '),
        size_hint=(None,None),size=(490,420))               

        hpop.open()          




class CustomDropDown(DropDown):
    pass

class popMC (FloatLayout):
    
    def Note(self):
       
        
        note = self.ids.note.text
        with conn:
            c.execute("INSERT INTO MCNote (Note) VALUES(?)",(note,))
   
        os.system("MC-notification.py")   

class MCMenuWindow(Screen):
    note=ObjectProperty(None)

    def MCRegister(self):
        mctype= self.ids.mctype.text
        Exp = self.ids.Exp.text
        MCD =self.ids.MCD.text
        dname = self.ids.dname.text
        if mctype  != "":
            if Exp !="":
                with conn:
                    c.execute("INSERT INTO MCregister (McType, ExpDate, MCDescription, DoctorName)VALUES (?,?,?,?)",
                    (mctype, Exp, MCD, dname  ))
            else:
                invalidMCLogin()
        else:
            invalidMCLogin()  
    
    def helpBtnMC(self):
        pop = Popup(title='HELP',
        content=Label(font_name='Lato',text='Medicine Reminder:\n\n For save the medicine type\n and Expired date with the description .\n\n To set date and time for taking the medicine it will be in calendar   \n\n If you found any trouble with the booking please contact : \n +601111217556 '),
        size_hint=(None, None), size=(450, 440))
        pop.open()  
      
    
    def setDateMC(self):
        os.system("maincal.py")
        
        

    def popNote(self):
        show=popMC()
        self.popup = Popup(title='Note',content=show, size_hint=(None, None), size=(400, 260))
        self.popup.open()
 
       

    
class WindowManager(ScreenManager):
    pass   
Builder.load_file("kiv/my.kv")
Builder.load_file("kiv/cal.kv")
Builder.load_file("kiv/Parkingtime.kv")
#Builder.load_file("Kivy-Calender-master/calender.py")

sm = WindowManager()
#db = DatabaseSQL()




screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"),MainWindow(name="main"),
MenuWindow(name="function"),CalMenuWindow(name="cal"),Parking1MenuWindow(name="park"),
Parking2MenuWindow (name="park2"),ParkingTimeBookOne (name="book"),ParkingTimeBookTwo (name="book_2")
,ParkingTimeBookThree (name="book_3"),ParkingTimeBookFour (name="book_4"),ParkingTimeBookFive (name="book_5")
,ParkingTimeBookSix (name="book_6"),ParkingViewWindow(name="view"),MCMenuWindow(name="MC")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "login"
  

class MyMainApp(App):
    def build(self):
        return sm



if __name__ == "__main__":
    MyMainApp().run()
