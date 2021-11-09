import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

from plyer import tts
from plyer import notification
notification.notify(
    title='Set Reminder',
    message='Your Reminder has been set',
    app_icon='Ultra-logo.ico',
    timeout=10,  # seconds
)

