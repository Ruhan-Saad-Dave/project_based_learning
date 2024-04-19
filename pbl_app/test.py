#This file is used for testing of code concepts.

from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def but(self, instance, val):
        print(val)
    
    def build(self):
        button = Button(text = "me", on_press = lambda instance: self.but(instance, "hi"))
        return button

MyApp().run()